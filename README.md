# Pagewright

**Design-grade SaaS landing pages, generated — not templated.**

Pagewright is a skill for [Claude Code](https://claude.com/claude-code) that turns a one-line product
brief into an original, modern, production-ready landing page — static HTML + Tailwind, no build step,
opens in any browser. It is built to do the one thing most "AI website" tools fail at: **not look generic.**

---

## The problem

Ask a model to "make a SaaS landing page" and you tend to get the same page every time: Inter for
everything, an indigo-to-purple gradient, three identical icon cards, soft shadows, and a gray placeholder
box where the product should be. That stack *is* what "AI-generated" looks like. Pagewright is engineered
specifically to escape it.

## How it works

Three systems work together.

### 1. A curated reference library of 213 real, current SaaS sites

The best landing pages on the web today — Linear, Stripe, Vercel, Attio, CrowdStrike, Ramp, PostHog, and
200+ more — are each distilled into a structured reference: palette, typography, section sequence, the one
genre-breaking *signature* move, imagery strategy, and copy voice, alongside a screenshot the model
actually opens and looks at.

The library was assembled by an automated research pipeline:

- **~670 candidates** scraped and de-duplicated from four design galleries (saaspo, land-book, lapa.ninja,
  godly.website);
- **248 screenshotted** and **scored by a vision pass** for design quality, dropping dead/blocked/non-SaaS
  pages;
- **213 deep-extracted** into reference entries, balanced across six visual moods and weighted toward the
  bold tech, security, and enterprise tier that AI tools usually miss.

### 2. Vibe Discovery, Design DNA, and anti-convergence

Before any markup, the skill commits to a *specific* direction instead of vague adjectives: a **motif**, an
**"X meets Y" brand coordinate**, and a per-project **avoid-list**. It then locks a Design DNA in current
(2025-26) vocabulary — modern typefaces, tinted neutrals, a deliberate signature — and runs a
**mandatory-variety checklist** that rotates typeface, accent, layout, texture, and icon set so two pages
never rhyme. The typography and aesthetic guidance is grounded in research on what reads as current versus
what now reads as a template tell.

### 3. HTML-first product visuals

The biggest reason AI pages look like wireframes is a gray placeholder where the product should be.
Pagewright builds the product UI — dashboards, tables, charts, code, terminals, chat — directly in
HTML/CSS/SVG, the way Linear, Stripe, and Attio actually do. Photography, 3D, and illustration are the only
things left to image slots, which ship as dimensioned placeholders with ready-to-run generation prompts
(and optional Nano Banana / Gemini generation).

## The build flow

```
0. Intake        — "guide me" vs "you decide"
1. Vibe + DNA    — motif, "X meets Y", avoid-list -> look at real reference pixels -> Design DNA
2. Storytelling  — choose a section sequence that argues the product's case; real copy
3. Build         — HTML + Tailwind, current fonts, tinted neutrals, motion, HTML-first product UI
4. Images        — build in code where possible; placeholders + optional generation for photo/3D
5. Preview       — open it, look at it, tighten, ship
```

## Install

Copy the skill into your Claude Code skills directory:

```bash
cp -r pagewright ~/.claude/skills/pagewright
```

Or install the packaged `pagewright.skill` bundle through your Claude client.

## Usage

Invoke the skill and give it a product. It opens by asking whether you want to guide the design or let it
decide, then produces a complete, runnable page.

```
> Build a landing page for "Cortex", a product-analytics platform for PM teams.
```

## Examples

Pages generated from a one-line brief (originals, not clones), in [`examples/`](examples/):

| Example | Brief | Approach |
| --- | --- | --- |
| Aegis | EDR security platform | dark "war-room" console built in HTML |
| Cortex | product analytics | warm-light analytics dashboard built in HTML |
| Relay | webhook delivery | graphite split-flap event board built in HTML |

Each folder contains the generated `index.html` and a screenshot.

## Repository layout

```
pagewright/              the skill
├── SKILL.md             entry point and build flow
├── references/          design-dna, section-patterns, build-system, motion, image-strategy, intake
│   └── reference-library/   213 distilled entries + thumbnails + index
└── scripts/             scaffolder, placeholder + image generation, local preview
examples/                pages generated from a brief
```

## License

[MIT](LICENSE). The reference library contains thumbnails of third-party websites used as design
reference; they remain the property of their respective owners.
