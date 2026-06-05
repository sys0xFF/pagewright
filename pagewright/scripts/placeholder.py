#!/usr/bin/env python3
"""Generate a dimensioned, labeled placeholder image (SVG — crisp at any size, no dependencies).

Every image slot ships one of these so the page looks intentional with zero real assets, and the user
sees exactly what to drop in. Style it light or dark to match the Design DNA.

Usage:
    python placeholder.py --out assets/images/hero.svg --width 1280 --height 800 \\
        --label "HERO — product screenshot" --theme dark --accent "#6366f1"
"""
import argparse
from pathlib import Path

THEMES = {
    "dark":  {"bg": "#141417", "grid": "#26262c", "fg": "#9a9aa6"},
    "light": {"bg": "#f1f1f4", "grid": "#e0e0e6", "fg": "#73737e"},
}

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
  <defs>
    <pattern id="g" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{grid}" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="{bg}"/>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect x="0.5" y="0.5" width="{w1}" height="{h1}" fill="none" stroke="{accent}" stroke-width="2" stroke-dasharray="8 8" opacity="0.7"/>
  <g fill="{fg}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" text-anchor="middle">
    <text x="{cx}" y="{cy}" font-size="{fs}" font-weight="600">{label}</text>
    <text x="{cx}" y="{cy2}" font-size="{fs2}" opacity="0.7">{w} × {h}</text>
  </g>
</svg>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=800)
    ap.add_argument("--label", default="image")
    ap.add_argument("--theme", choices=list(THEMES), default="dark")
    ap.add_argument("--accent", default="#6366f1")
    args = ap.parse_args()

    t = THEMES[args.theme]
    w, h = args.width, args.height
    fs = max(14, min(w, h) // 22)
    svg = TEMPLATE.format(
        w=w, h=h, w1=w - 1, h1=h - 1, bg=t["bg"], grid=t["grid"], fg=t["fg"],
        accent=args.accent, label=args.label.replace("&", "&amp;").replace("<", "&lt;"),
        cx=w // 2, cy=h // 2, cy2=h // 2 + fs + 8, fs=fs, fs2=max(11, fs * 2 // 3),
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"[ok] {out}  ({w}x{h}, {args.theme})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
