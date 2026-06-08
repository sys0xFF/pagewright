#!/usr/bin/env python3
"""OPTIONAL photographic backgrounds via the Unsplash API.

For the slots Nano Banana shouldn't fake and CSS can't carry: a full-bleed editorial photo, a landscape,
an organic texture (fog, paper, stone, foliage, water). OFF by default and an *enhancement*, never a
dependency — if anything fails (no key, no match, network), it exits non-zero with a clear message and the
skill falls back to a dimensioned placeholder.

WHEN to reach for this (taste guards — the script can't enforce them, you must):
    - YES: landscapes, skies, water, foliage, stone/paper/fabric texture, abstract macro, architecture,
      still life, food/ingredients shot editorially, hands/craft detail. Things that set MOOD.
    - NO:  "diverse team at laptops", generic smiling-people stock, clip-arty business imagery. That is
      the exact AI-slop the skill exists to avoid (see design-dna.md / image-strategy.md). A photo of
      *people as subjects* almost always reads as stock — prefer place, object, texture, or abstraction.
    - Always GRADE it in CSS so it belongs to the page, not to a stock site: a color/duotone overlay in
      the Design DNA palette, a grain layer, and/or a gradient scrim for text contrast. The script prints
      a ready-to-paste grade snippet. An ungraded raw stock photo is a tell.

Setup:
    - Create a free Unsplash developer app at https://unsplash.com/developers and copy its Access Key.
      (The free "Demo" tier is rate-limited to 50 requests/hour — plenty for building a page.)
    - export UNSPLASH_ACCESS_KEY=...        (or set it in your environment)

Usage:
    python fetch_unsplash.py --query "fog over a pine forest at dawn, muted, no people" \\
        --out assets/images/hero-bg.jpg --orientation landscape --width 1600
    # pick a different result if the first isn't right:
    python fetch_unsplash.py --query "..." --out ... --index 2

Attribution: the Unsplash API Terms REQUIRE crediting the photographer with a link, and that a "download"
is registered on use. This script does both: it pings the download endpoint and appends a credit line to
`<out-dir>/UNSPLASH-CREDITS.md` plus prints a visible-credit + alt snippet for you to wire in.

Stdlib only (urllib) — no pip installs.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.unsplash.com"
APP = "pagewright"  # UTM source for attribution links, per Unsplash guidelines
PEOPLE_HINT = ("team", "people", "person", "man", "woman", "office", "meeting", "businessman", "portrait")


def fail(msg: str) -> int:
    print(f"! fetch_unsplash: {msg}", file=sys.stderr)
    print("  -> falling back: keep the placeholder, or generate the image, or pick a photo by hand.", file=sys.stderr)
    return 2


def get(url: str, key: str):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Client-ID {key}",
        "Accept-Version": "v1",
        "User-Agent": f"{APP} (landing-page builder)",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True, help="describe the MOOD/scene; favor place/object/texture, not people")
    ap.add_argument("--out", required=True)
    ap.add_argument("--orientation", default="landscape", choices=["landscape", "portrait", "squarish"])
    ap.add_argument("--index", type=int, default=0, help="which search result to use (0 = best match)")
    ap.add_argument("--width", type=int, default=1600)
    args = ap.parse_args()

    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    if not key:
        return fail("UNSPLASH_ACCESS_KEY not set (this feature is opt-in).")

    if any(w in args.query.lower() for w in PEOPLE_HINT):
        print("  ~ heads up: your query leans toward people/office imagery, which tends to read as stock.\n"
              "    Prefer place, object, or texture — or grade it hard. Proceeding anyway.", file=sys.stderr)

    # search
    q = urllib.parse.urlencode({
        "query": args.query, "orientation": args.orientation,
        "per_page": max(args.index + 1, 10), "content_filter": "high",
    })
    try:
        data = get(f"{API}/search/photos?{q}", key)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "ignore")[:300]
        hint = " (check the Access Key / rate limit)" if e.code in (401, 403) else ""
        return fail(f"search HTTP {e.code}{hint}: {detail}")
    except Exception as e:  # noqa: BLE001
        return fail(f"search request failed: {e}")

    results = data.get("results") or []
    if not results:
        return fail(f"no photos matched {args.query!r} — try a broader scene or different words.")
    if args.index >= len(results):
        args.index = 0
    pick = results[args.index]

    # download a sized JPEG off the raw URL
    raw = pick["urls"]["raw"]
    sep = "&" if "?" in raw else "?"
    img_url = f"{raw}{sep}w={args.width}&q=80&fm=jpg&fit=crop"
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(img_url, headers={"User-Agent": f"{APP}"})
        with urllib.request.urlopen(req, timeout=120) as r:
            out.write_bytes(r.read())
    except Exception as e:  # noqa: BLE001
        return fail(f"image download failed: {e}")

    # register the download (REQUIRED by the API terms) — best-effort
    try:
        get(pick["links"]["download_location"], key)
    except Exception:  # noqa: BLE001
        pass

    # attribution (REQUIRED) — links must carry UTM params
    name = pick["user"]["name"]
    uname = pick["user"]["username"]
    utm = f"utm_source={APP}&utm_medium=referral"
    profile = f"https://unsplash.com/@{uname}?{utm}"
    photo = f"{pick['links']['html']}?{utm}"
    alt = (pick.get("alt_description") or args.query).strip().capitalize()

    credit_md = f"- `{out.name}` — Photo by [{name}]({profile}) on [Unsplash]({photo})\n"
    credits_file = out.parent / "UNSPLASH-CREDITS.md"
    header = "" if credits_file.exists() else "# Image credits (Unsplash)\n\n"
    with credits_file.open("a", encoding="utf-8") as f:
        f.write(header + credit_md)

    print(f"[ok] fetched {out}  ({args.width}px, {args.orientation})")
    print("\n  Attribution (required) — appended to UNSPLASH-CREDITS.md. Wire a visible credit, e.g.:")
    print(f'    <a href="{photo}" class="text-xs opacity-60">Photo: {name} / Unsplash</a>')
    print("\n  Grade it so it belongs to the page (don't ship it raw) — example scrim + duotone:")
    print('    <div class="relative">\n'
          f'      <img src="{out.as_posix()}" alt="{alt}" class="h-full w-full object-cover" />\n'
          '      <div class="absolute inset-0 mix-blend-multiply" style="background: <accent>"></div>\n'
          '      <div class="absolute inset-0 bg-gradient-to-t from-[#0b0b0e] to-transparent"></div>\n'
          '    </div>')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
