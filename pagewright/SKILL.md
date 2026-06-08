---
name: pagewright
description: >-
  Build beautiful, original SaaS landing pages and marketing sites as static HTML + Tailwind,
  using a curated library of real-world design patterns and a per-project "Design DNA" so every
  site looks distinct — never a clone of any single reference. Plans where AI-generated imagery
  (e.g. Nano Banana / Gemini) and real screenshots elevate the design instead of faking everything
  in CSS. Use this skill whenever the user wants to create, build, design, redesign, generate, or
  improve a landing page, marketing page, product/launch page, hero section, pricing page, or
  website for a SaaS, startup, app, tool, or digital product — even if they only describe the
  product and say "make me a site/page" without naming a framework or the word "landing". It opens
  by asking whether they want to guide the design or let you decide.
---

# SaaS Landing Page Builder

Generate landing pages that look like a senior product designer made them — not the generic
"purple-gradient AI slop" that most tools produce. The skill's whole job is to **avoid generic**.

It does that with three ideas working together:

1. **Design DNA** — before writing any markup, synthesize a *unique* visual system for THIS project
   (palette, type, mood, density, motion, imagery style). This is what makes every output look like
   its own product instead of a template.
2. **Remix, never clone** — draw structural and stylistic ideas from **≥3 different references** in
   the bundled library. Copying one site produces a derivative; remixing many produces something new.
3. **Images do the heavy lifting** — the prettiest SaaS sites aren't pure CSS. Decide up front where a
   real screenshot, an illustration, or an AI-generated image (Nano Banana / Gemini, etc.) belongs,
   and leave first-class slots for them instead of trying to fake everything in gradients and blobs.

Output is **static HTML + Tailwind** (via CDN by default — zero build step, instant preview).

---

## The build flow

Follow these steps in order. Each links to a reference file — read it when you reach that step;
don't preload everything.

### Step 0 — Intake: "guide me" vs "you decide"

The **first thing** you do is ask the user how involved they want to be. Two modes:

- **You decide** → gather only the 2–3 essentials (what's the product, who's it for, what's the one
  action you want visitors to take), then make confident choices for everything else and show a result.
- **Guide me** → run the tiered interview to pin down brand, tone, audience, sections, and assets.

Don't dump a 20-question form on anyone. Ask in tiers, with smart defaults, and stop as soon as you
have enough — over-constraining the design makes it worse, not better.

→ Read **[references/intake.md](references/intake.md)** for the exact questions and how to run each mode.

### Step 1 — Vibe Discovery → Design DNA (the make-or-break step)

This is where pages live or die. Escape the AI prior (Inter + indigo gradient + three icon cards + mono
eyebrows) by working in three moves: **discover a specific vibe** (a motif + an "X meets Y" brand-coordinate
+ a per-project AVOID-list — not vague adjectives) → **route by niche, LOOK at 3–5 real reference
screenshots, and anchor on ONE** — transcribing its section skeleton in writing before any markup → **lock
a Design DNA in today's vocabulary** (current fonts, tinted neutrals, a genre-breaking signature).

Crucial: don't just *read* the library's prose — **open the thumbnail images** (`reference-library/thumbs/
<domain>.jpg`) with the Read tool and let your eyes calibrate to current execution. The anchor's *structure*
is your spine; the *skin* is remixed from the others (structure from ONE, skin from the rest). Rotate the
anchor so two pages never share a spine, then run the anti-convergence checklist — structure **and**
surface — before building.

→ Read **[references/design-dna.md](references/design-dna.md)** — Vibe Discovery, the anchor-on-one forcing
function, composition archetypes, the current typography & palette vocabulary, and the anti-convergence rules.
→ Library: **[references/reference-library/INDEX.md](references/reference-library/INDEX.md)** — current
   SaaS **and consumer-brand** sites by niche/mood/style; **each entry has a thumbnail to LOOK at**, and
   46 **anchor-grade** sites also have a full-page capture in `full/<domain>.jpg` (copy the real structure).
→ Optional power tool: **[scripts/extract_tokens.py](scripts/extract_tokens.py)** — pull the anchor's REAL
   fonts/colours/radii/shadows from its live CSS, so you copy its *identity* literally instead of from memory.

### Step 2 — Structure & storytelling: a page is a narrative

A landing page is an argument, not a stack of boxes: hook → the problem → your solution → proof →
handle objections → ask for the action. Choose a section sequence that tells that story for THIS
product, and write **real copy** — never lorem ipsum, never "Lorem-grade" filler like "Empower your
workflow with synergy."

→ Read **[references/section-patterns.md](references/section-patterns.md)** — the section library
(hero, social proof, feature layouts, how-it-works, testimonials, pricing, FAQ, CTA, footer),
storytelling frameworks, and copy patterns that don't sound like a robot.

### Step 3 — Build: HTML + Tailwind, crafted & in motion

Assemble the page from the chosen sections, applying the Design DNA as Tailwind tokens with **current
fonts** (load them — don't default to system-ui or Inter-only). Sweat the details that separate pro from
amateur: a real type scale with weight contrast, consistent spacing rhythm, tinted-neutral surfaces, a
texture choice, **purposeful motion** (at least a blur-in reveal + one signature), responsive from 320px,
and accessibility.

→ Read **[references/build-system.md](references/build-system.md)** — Tailwind + current-font loading,
tinted-neutral tokens, texture (grain/grid), components, responsive/a11y/perf.
→ Read **[references/product-ui.md](references/product-ui.md)** — **before hand-building any product UI**
(dashboard, table, chart, log, card, nav, form, code surface): the per-component craft from real top sites,
the generic anti-pattern to avoid, and variety levers so your components don't come out samey.
→ Read **[references/motion.md](references/motion.md)** — the 2025-26 motion vocabulary (blur-in,
scroll-driven, marquee, magnetic) with copy-paste snippets.
→ Use **[scripts/new_site.py](scripts/new_site.py)** to scaffold the output folder.

### Step 4 — Images: plan them, slot them, optionally generate them

For each image slot, decide the *type* (product screenshot, abstract/3D render, illustration, photo,
logo) and write a ready-to-use generation prompt. Always ship dimensioned placeholders so the page
looks intentional with zero assets. If the user opts in and has a generator configured, generate the
assets directly; otherwise hand them the prompts to run in Nano Banana / Midjourney / etc.

→ Read **[references/image-strategy.md](references/image-strategy.md)** — where images earn their keep,
prompt recipes per image type, placeholder system, and the opt-in generation flow.
→ **[scripts/gen_image.py](scripts/gen_image.py)** — optional Gemini ("Nano Banana") image generation;
off by default, needs `GEMINI_API_KEY`.
→ **[scripts/fetch_unsplash.py](scripts/fetch_unsplash.py)** — optional real-photo fetch (landscape/
texture/editorial) from Unsplash; off by default, needs `UNSPLASH_ACCESS_KEY`; grade what it returns.
→ **[scripts/placeholder.py](scripts/placeholder.py)** — generate dimensioned placeholder images/SVGs.

### Step 5 — Preview & polish

Open the page and actually look at it. Check it at mobile and desktop widths, verify the story reads,
tighten spacing, and confirm nothing is broken or generic-looking. Iterate before declaring done.

→ Use **[scripts/preview.py](scripts/preview.py)** to serve the site locally; pair with a screenshot/
preview tool to inspect it.

---

## Operating principles (the soul of the skill)

These override any individual instruction. When a choice is unclear, optimize for these.

- **Generic is the enemy — and timidity is how you get there.** If the output could be any SaaS, it
  failed. The usual cause isn't bad taste, it's *under-committing* into a safe, tasteful, forgettable
  page. Pick one bold concept and go all in. Avoid the clichés: centered-everything, the lone purple
  gradient, three identical feature cards with line icons, "Powerful features for modern teams."
- **Don't fear strong references.** The library is raw material to be *used*, not admired from a distance.
  Remix ≥3, clone 0 — but borrow a *daring* move and push it further; a confident remix beats a polite,
  watered-down one. (See the anti-copy rule in design-dna.md.)
- **Dark/technical is the danger zone.** If the brief lands you in a dark dev-tool look, assume it will
  come out generic unless you fight it: choose a non-obvious accent (not indigo/violet), a signature that
  breaks the genre, and at least one cinematic/bold element. See the convergence-trap note in design-dna.md.
- **Use today's vocabulary, not your prior.** The model's default — Inter everywhere, indigo→purple
  gradient, three icon cards, mono eyebrows, soft shadows, pure black/white — *is* what "AI-made" looks
  like in 2025-26. Reach for current faces (Geist, a serif-display + grotesque pairing), tinted neutrals
  (`#09090B` not `#000`), real product UI, grain. Follow the do/avoid lists in design-dna.md literally.
- **Anchor on ONE real page, then vary the skin.** The convergence you're fighting is *structural* — pages
  rhyme because they share a skeleton (accent-word headline → dual CTA → 3-up → testimonial → pricing → dark
  CTA band), even with different colours, because that skeleton is the model's *average of all landings*.
  Beat it by building from a **real page's actual bones**: pick ONE anchor and **open its full-page capture
  (`reference-library/full/<domain>.jpg`)** — transcribe its REAL section sequence before any markup and
  copy it faithfully, *even when it isn't the expected arc* (Linear has no pricing and no problem-reframe).
  Remix the skin from the *other* references. Rotate the anchor every build; keep the **DTC reflexes**
  (design-dna.md) default-OFF; then self-diff against the generic stack — if you can't say how it differs
  structurally, you reverted. (Full procedure in design-dna.md; page shapes in section-patterns.md.)
- **Real words.** Write copy a founder would actually ship. Concrete nouns, real benefits, a voice that
  matches the product's mood. No lorem ipsum in anything you show the user.
- **No filler — but match the anchor's density.** Restraint means cutting *filler*, not building *few*
  sections. Length is **anchor-relative**: a minimal anchor (Vercel) gets a minimal page; a rich, dense one
  (Mercury, Stripe, Aesop — real photography, several distinct visuals, image-card grids, carousels, a stat
  row) gets a rich page — copy that density, generate the photos, vary the section *type*. Cut redundant
  copy and filler beats; never strip a lush page down to a flat stack of text panels (that reads as
  simplistic, and it's half the anchor's height). (See section-patterns.md → Length & density.)
- **No decorative mono.** Monospace is banned as a design face (eyebrows, labels, numbers, data, UI chrome)
  — it's an ugly, dated tell; use the grotesque body with tabular-nums for figures. Mono only ever appears
  inside a literal code/terminal snippet. (See design-dna.md.)
- **Build the product, don't placeholder it — but build interfaces, not objects.** The fastest path to a
  "real product" look is to build the product UI/dashboard/chart/code/chat **in HTML/CSS/SVG** (like Linear,
  Stripe, Attio do) — a gray placeholder hero is why AI pages look like wireframes. But this applies to
  *interfaces and data*, not to **physical objects**: a bottle, a ring, a device hand-drawn in SVG comes out
  as janky clip-art. Those want a **graded photo (Unsplash) or a generated render (Nano Banana)**, not
  hand-SVG. Reserve image slots + generation for photo/3D/illustration/objects, and fill them. If your hero
  is a gray box *or a clip-art object*, you're not done. (See image-strategy.md.)
- **Respect the user's control dial.** "You decide" means decide — show work, don't interrogate.
  "Guide me" means collaborate. Read the room.
- **Ship something runnable.** Every result opens in a browser with no build step and looks finished —
  placeholders and all.

## When NOT to over-reach

This skill targets SaaS/product **landing & marketing pages**. If the user wants a full web app with
routing/state, a backend, or a CMS, build the marketing page well and say plainly that the app shell is
out of scope (offer to scaffold a starting point, but don't pretend a static page is an app).
