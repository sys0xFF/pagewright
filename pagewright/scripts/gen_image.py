#!/usr/bin/env python3
"""OPTIONAL image generation via Google Gemini "Nano Banana" (Gemini 2.5 Flash Image).

This is OFF by default and is an *enhancement*, never a dependency — if anything fails (no key, model
unavailable, quota), it exits non-zero with a clear message and the skill falls back to placeholders +
handing the user the prompt to run elsewhere.

Setup:
    - Get an API key from Google AI Studio (https://aistudio.google.com/apikey).
      NOTE: a Gemini *app* subscription ("Google Pro" / Gemini Advanced) is NOT API access — the API
      is separate and has its own free tier (rate-limited). Image-gen availability/cost on the free
      tier varies, so don't assume it's free; the script reports the API's error verbatim if so.
    - export GEMINI_API_KEY=...        (or set it in your environment)
    - optional: export GEMINI_IMAGE_MODEL=gemini-2.5-flash-image   (override if the id changes)

Usage:
    python gen_image.py --prompt "Clean analytics dashboard, dark theme, indigo accents, 16:10" \\
        --out assets/images/hero.png

Stdlib only (urllib) — no pip installs.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
DEFAULT_MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")


def fail(msg: str) -> int:
    print(f"! gen_image: {msg}", file=sys.stderr)
    print("  -> falling back: keep the placeholder and run the prompt in your own image tool.", file=sys.stderr)
    return 2


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return fail("GEMINI_API_KEY not set (this feature is opt-in).")

    body = json.dumps({
        "contents": [{"parts": [{"text":
            args.prompt + "\n\nGenerate a single high-quality image. No text overlays unless asked."}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode()

    url = API.format(model=args.model, key=key)
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "ignore")[:500]
        return fail(f"API HTTP {e.code}: {detail}")
    except Exception as e:  # noqa: BLE001
        return fail(f"request failed: {e}")

    # find inline image data in the response
    try:
        parts = data["candidates"][0]["content"]["parts"]
    except (KeyError, IndexError):
        return fail(f"unexpected response shape: {json.dumps(data)[:300]}")

    img_b64 = None
    for p in parts:
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            img_b64 = inline["data"]
            break
    if not img_b64:
        return fail("no image returned (model may not support image output on your tier).")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(img_b64))
    print(f"[ok] generated {out}  (model={args.model})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
