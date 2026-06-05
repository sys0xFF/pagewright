# Build system — HTML + Tailwind, crafted & current

Output is a static site that opens with no build step and looks finished. This file is the technical
contract: how to wire a CURRENT Design DNA into Tailwind, the structure to emit, and the craft checklist.

## Output structure

`scripts/new_site.py "<project-name>"` scaffolds `index.html` + `assets/{images,favicon.svg}` + README.
Single-page by default; add sibling `.html` pages with a shared nav/footer only if needed.

## Tailwind + fonts setup

Default to the **Tailwind Play CDN** (zero build) with the DNA injected as real tokens. Load **current**
fonts — never default to Inter-only or system-ui. Pick from the vocabulary in design-dna.md; load like so:

```html
<!-- Editorial serif display + neutral grotesque body (the 2025-26 move). Swap per the DNA. -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Hanken+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
<!-- Geist + Geist Mono (dev-taste, free) — on Google Fonts: -->
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300..800&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<!-- More free current faces on Google Fonts: Instrument Serif, DM Serif Display, Newsreader, Schibsted Grotesk,
     Plus Jakarta Sans, Albert Sans, Bricolage Grotesque, Instrument Sans, Host Grotesk.
     Fontshare (api.fontshare.com) for Clash/Satoshi/Switzer if a heavier display is wanted. -->

<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = { theme: { extend: {
    colors: {                 // TINTED neutrals, not pure black/white — name by ROLE
      bg:'#09090B', surface:'#18181B', raised:'#27272A', line:'#3F3F46',
      ink:'#FAFAFA', muted:'#A1A1AA', faint:'#71717A',
      accent:'#<one sharp saturated accent — NOT indigo/violet>',
    },
    fontFamily: {            // from the DNA pairing
      display:['Fraunces','Geist','serif'], sans:['"Hanken Grotesk"','Geist','system-ui','sans-serif'],
      mono:['"Geist Mono"','ui-monospace','monospace'],   // ONLY for real technical content
    },
  } } }
</script>
```

Set `<meta name="viewport">`, a real `<title>`, OG/description meta. Light themes: use `#FAFAFA`/warm
off-white surfaces, not `#FFFFFF`.

## Design tokens → Tailwind

- **Color by role** (`bg/surface/raised/line/ink/muted/faint/accent`) so the palette is swappable and
  disciplined. Accent maps to the primary CTA + 1-2 focal moments ONLY.
- **Tinted neutrals + stepped luminance** carry depth (e.g. `#09090B → #18181B → #27272A`) over heavy
  shadows. Borders are 1px hairlines (`line`).
- **Type scale** from the DNA. Big confident display with **optical sizing + negative tracking**
  (`tracking-tight`, `leading-[1.02]`), comfortable body 16-18px, `leading-relaxed`. Use **extreme weight
  contrast** (e.g. `font-light` display vs `font-bold` accents) — it reads current.
- **Spacing rhythm** — pick a section padding scale (`py-24 md:py-32`) and reuse it; consistency is most
  of "polished". Center with `max-w-6xl mx-auto px-6`; let select visuals break wider.

## Texture (craft signal — use deliberately)

```html
<!-- SVG grain overlay (15-30% opacity), fixed, pointer-events-none -->
<svg class="pointer-events-none fixed inset-0 -z-10 h-full w-full opacity-[0.04]"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>
```
Faint dot/blueprint grid via a CSS `radial-gradient`/`linear-gradient` background on a section; a blurred
ambient `accent` glow behind product UI. Avoid heavy glassmorphism as structure.

## Components (principles, not rigid templates — templates breed sameness)

- **Buttons:** primary (accent) + secondary (ghost/outline), real hover/active/focus, specific labels.
  Consider a `data-magnetic` primary (see motion.md).
- **Nav:** `<header>` logo + 3-5 links + primary CTA; condense/blur on scroll; working mobile menu.
- **Icons:** a multi-weight set — **Phosphor / Iconoir / Hugeicons** (CDN or inline SVG) — matched to the
  shape language. NOT raw single-weight Lucide/Feather, NOT Corporate Memphis mascots.
- **Cards/bento:** vary size and content; a bento of **real product screenshots** at varied sizes beats
  three equal icon-blurb boxes (that trio is an AI tell).
- **Product visual:** frame screenshots intentionally (browser/app chrome, tilt, soft glow) so they read
  as real product — often the page's signature.
- **Sections:** semantic `<section aria-labelledby>`; one `<h1>` (hero).

## Responsive · A11y · Performance

- **Mobile-first**, verify 320px → `sm md lg xl`. Hero stacks on mobile; tap targets ≥44px; no horizontal
  scroll; `clamp()` for the hero headline.
- **A11y:** semantic landmarks, one `h1`, **alt on every meaningful image** (`alt=""` decorative), WCAG AA
  contrast (watch `muted` on `surface`), visible focus, keyboard nav, `prefers-reduced-motion` respected.
- **Perf:** `loading="lazy"` + width/height on below-fold images; SVG for logos/icons; modern formats;
  cheap CSS-transform motion; minimal vanilla JS. No multi-MB WebGL before paint.

## Motion

See **[motion.md](motion.md)** — at minimum a blur-in reveal + one signature motion, current easing
(spring/short), gated behind `prefers-reduced-motion`. Do not use AOS.js or fade-up-on-everything.

When assembled, go to **image-strategy.md** for visuals, then preview and polish.
