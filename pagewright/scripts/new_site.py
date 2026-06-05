#!/usr/bin/env python3
"""Scaffold a static SaaS landing-page project (HTML + Tailwind CDN).

Creates a clean, *neutral* starting point — folder structure, an index.html skeleton with the Tailwind
config wired for Design-DNA tokens, semantic landmarks, and comment markers for each section. The skill
(Claude) then fills in the actual design, copy, and sections. The skeleton intentionally ships NO visual
opinion so it can't push the output toward generic.

Usage:
    python new_site.py "Project Name" [--dir OUTPUT_DIR]

Then preview with:  python preview.py OUTPUT_DIR/<slug>
"""
import argparse
import re
import sys
from pathlib import Path

INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="TODO: one-line value proposition for SEO/social." />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="TODO" />
  <meta property="og:type" content="website" />
  <link rel="icon" href="assets/favicon.svg" />

  <!-- CURRENT fonts — load the DNA pairing (see build-system.md). Do NOT default to Inter-only/system-ui. -->
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Hanken+Grotesk:wght@400;500;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300..800&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <!-- Tailwind Play CDN — zero build step. Swap for a real build only if the user asks. -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    // ── Design DNA tokens ── fill these from references/design-dna.md (color by ROLE, not hue)
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            // FILL from the Design DNA. PLACEHOLDERS — never ship indigo/violet or pure #000/#fff.
            bg:'#09090B', surface:'#18181B', raised:'#27272A', line:'#3F3F46',
            ink:'#FAFAFA', muted:'#A1A1AA', faint:'#71717A',
            accent:'#f43f5e',   // ONE sharp accent — NOT indigo/violet
          }},
          fontFamily: {{
            // current pairing (load in <head>); mono ONLY for genuinely technical content
            display: ['Fraunces', 'Geist', 'serif'],
            sans:    ['"Hanken Grotesk"', 'Geist', 'system-ui', 'sans-serif'],
            mono:    ['"Geist Mono"', 'ui-monospace', 'monospace'],
          }},
        }},
      }},
    }}
  </script>
  <style>
    @media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior: smooth; }} }}
  </style>
</head>
<body class="bg-bg text-ink font-sans antialiased">
  <!-- NAV -->
  <header class="sticky top-0 z-50">
    <!-- TODO: logo + 3–5 links + primary CTA; condense/blur on scroll -->
  </header>

  <main>
    <!-- HERO — 5-second test: value headline + primary CTA + credible visual -->
    <section aria-labelledby="hero-title">
      <h1 id="hero-title" class="font-display">TODO headline</h1>
    </section>

    <!-- SOCIAL PROOF -->
    <!-- PROBLEM -->
    <!-- FEATURES (alternating rows / bento / tabbed — pick per DNA) -->
    <!-- HOW IT WORKS -->
    <!-- TESTIMONIALS -->
    <!-- PRICING -->
    <!-- FAQ -->
    <!-- FINAL CTA -->
  </main>

  <footer>
    <!-- TODO: product / company / resources / legal columns -->
  </footer>
</body>
</html>
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#6366f1"/>
  <circle cx="16" cy="16" r="7" fill="#fff"/>
</svg>
"""

README_MD = """# {title}

Static landing page (HTML + Tailwind CDN). No build step.

## Preview
```
python ../scripts/preview.py .
```
or just open `index.html` in a browser.

## Swap placeholders
Image slots are marked with `<!-- IMAGE SLOT: ... prompt: ... -->` comments and use dimensioned
placeholders in `assets/images/`. Generate real images (Nano Banana / Midjourney / etc.) using the
prompt in each comment, or run `../scripts/gen_image.py`, then drop them in and update the `src`.
"""


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return s or "site"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name", help="Project / product name")
    ap.add_argument("--dir", default=".", help="Parent directory for the project folder")
    args = ap.parse_args()

    slug = slugify(args.name)
    root = Path(args.dir) / slug
    if root.exists() and any(root.iterdir()):
        print(f"! {root} already exists and is not empty — choose another --dir or name.", file=sys.stderr)
        return 1

    (root / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (root / "index.html").write_text(INDEX_HTML.format(title=args.name), encoding="utf-8")
    (root / "assets" / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")
    (root / "README.md").write_text(README_MD.format(title=args.name), encoding="utf-8")

    print(f"[ok] scaffolded {root}")
    print("  next: fill the Design DNA tokens + fonts in index.html, then build the sections.")
    print(f"  preview: python {Path(__file__).parent / 'preview.py'} {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
