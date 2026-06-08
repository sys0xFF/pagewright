# Design DNA — discover a vibe, then build a CURRENT visual system

Skipping this step is the #1 reason AI pages look generic: the model falls back to its average prior —
**Inter everywhere, an indigo→purple gradient, three icon cards, soft shadows, mono eyebrow labels.**
That exact stack is what "AI-generated" looks like in 2025-26. This file exists to get you off the prior
and onto a current, specific, committed direction.

Work in three moves: **(1) Discover a vibe → (2) Look at the real references and copy faithfully →
(3) Lock a Design DNA in today's vocabulary.** Anti-convergence rules run through all three.

---

## Move 1 — Vibe Discovery (no vague adjectives)

"Clean and modern" produces the prior. Force a *specific* direction instead. Write these down:

- **MOTIF** — one concrete metaphor the whole page can embody (a control room, a ledger, a darkroom,
  a blueprint, a night drive, a printed spec sheet, a trading terminal, a garden). The motif drives
  palette, type, imagery, and the signature.
- **BRAND-COORDINATE** — "**X meets Y**" using two real brands/worlds the user would admire
  ("Aesop meets Linear", "Bloomberg terminal meets Teenage Engineering", "a Kinfolk spread meets Vercel").
  This triangulates a point in style-space instead of a cliché.
- **SENSORY + EMOTION** — 2-3 concrete sensory words (matte, tactile, humming, glacial, warm-paper)
  and the ONE feeling a visitor should get in 5 seconds (reassured / in-command / excited / understood).
- **AVOID-LIST (mandatory)** — write 4-6 things THIS page will NOT do, to pre-empt the prior. Always
  include the AI tells; add project-specific ones. Example:
  `no Inter headings · no indigo/purple gradient · no three-equal-icon-cards · no mono eyebrow labels ·
   no hero-left-text / image-right default · no centered timid hero`

Carry the MOTIF, COORDINATE, and AVOID-LIST forward — they're as important as the palette.

---

## Move 2 — Anchor on ONE real reference (the forcing function)

This is the step that actually stops convergence — and it only works if you run it as a hard procedure,
not as advice. The model's landing-page prior (**eyebrow pill → one-word-accent headline → two CTAs →
a row of three stats → logo wall → three feature cards**) is a deep attractor; "try to vary it" loses to
it every time. The one thing that beats a prior is building from a *specific real page's bones*. So:

**1. Route by niche → a shortlist.** Open `reference-library/INDEX.md`. Find your niche/context in the
   **By niche** list and your mood in **By mood**; take the 3–5 sites at that intersection.
   - *Niche not in the library?* (it covers health, fintech, dev-tools, nature, food, education, beauty,
     fitness, home, travel and more — but not everything.) Then **route by composition, not industry**:
     pick the **composition archetype** (below) that fits the mood and grab sites that use it, whatever
     their sector. A meditation app can faithfully borrow the bones of an editorial-photo fashion page; a
     farm co-op can borrow a warm-minimal CPG page. Match the *shape*, not the industry.

**2. LOOK at the pixels — mandatory.** `Read` the thumbnail `.jpg` of every shortlisted site. The text
   entry is a map; the image is the territory. Your eye calibrates to current execution — real type,
   spacing, colour temperature, how the visual is staged — in a way prose never gives you. Skipping this
   is the single most common way a build silently reverts to the prior.

**3. Pick ONE anchor and transcribe its skeleton — in writing, before any markup.** Choose the single
   site whose *structure* fits this product best (and that you haven't just used — see the ledger below).
   **If it has a full-page capture (`reference-library/full/<domain>.jpg`), OPEN IT** — that's the whole
   real page, top to bottom, not just the hero. Read off its **actual** section sequence and its structural
   quirks (an asymmetric beat, a changelog, no pricing at all, a weird order) and **write out the spine
   you'll build**, copying what the real page genuinely does — *even when it isn't the "expected" arc.*
   (No full capture? Fall back to the entry's `sections:` line, but know it's terse and the invented detail
   is exactly where you drift back to the template.) This transcription *is* the forcing function: you
   build to a real page's bones, not to your average — and your average IS the generic template you're
   fighting.
   > e.g. anchor = linear.app → its real spine (from the full capture) is `hero(live app UI) › logo-wall ›
   > 3-up › feature(UI) › feature(UI) › feature(code) › feature(chart) › changelog › 2-up-testimonial ›
   > cta › footer` — note there is **no problem-reframe and no pricing**. You build THAT, re-skinned — not
   > the template your prior wants to emit.

**4. Skin from the others — never from the anchor.** Pull palette, type, texture and motif from the
   *other* shortlisted sites + your vibe. This resolves the apparent contradiction in this skill:
   **structure from ONE (faithfully), skin from the rest (remixed).** The result clones no one — its
   surface is recombined — yet has a real spine, because its structure is faithfully one page's. Remix
   ≥3, clone 0, and copy structure boldly from the one. *Even when copying, be faithful.*

**5. Rotate the anchor (ledger).** Two pages must never share an anchor. Before you commit, recall what
   you anchored on recently; if it's the same site *or the same composition archetype*, switch. Within a
   niche especially: not every fintech page anchors on Stripe, not every health page on Oura — spread the
   load across the shortlist. **Building several at once (a batch / parallel agents)?** Parallel builders
   are blind to each other, so they collide on the trendy default (everyone reaches for Geist, the
   accent-word headline, the dark CTA band). Assign each one a *different* **anchor, page archetype
   (section-patterns.md), display-font family, accent, and hero grammar** up front — and explicitly
   **forbid the shared DTC reflexes** so two siblings don't both ship the one-accent-word headline or the
   contrarian reframe. Distinct inputs in, distinct pages out.

This is how you escape the prior: you build from a real page's bones, not from memory.

---

## Composition archetypes — rotate the SKELETON, not just the skin

Convergence is mostly *structural*: even with a fresh palette and font, two pages rhyme because they share
one skeleton. So choose the hero/page composition **deliberately**, and rotate it across builds. Each
archetype below has real exemplars in the library — anchor on one (and remember the shape is
industry-agnostic: a non-tech brief borrows these freely):

- **split-screen** — text one side, visual the other (the default — use it *least*). e.g. attio, framer
- **centered-editorial** — big centered headline, generous air, visual below. e.g. vercel, cohere
- **full-bleed-photo / cinematic** — a photo or render fills the hero, text overlaid. e.g. palantir,
  cluely, index.inc, spellbook  (← the slot Unsplash photography fills — see image-strategy.md)
- **bento-grid** — the hero *is* a grid of unequal product tiles. e.g. supabase, raycast, default
- **poster / coverline** — magazine-cover energy: oversized condensed type, minimal chrome. e.g. mux, polar
- **asymmetric-canvas** — copy in a narrow column, a sprawling visual field beside it. e.g. morphic
- **product-diorama** — a single staged 3D/photoreal object as the whole hero. e.g. lithic, oxide, three.tools
- **app-frame** — a faithful rebuild of the product UI in browser/app chrome is the hero. e.g. linear, amie
- **oversized-type** — type itself is the image; little or no graphic. e.g. clickhouse, juicebox, pipe
- **diptych / triptych** — repeated panels showing states or variants. e.g. authkit, rive

Rule of thumb: **if your last page was split-screen with three cards, this one is not.**

---

## Move 3 — Lock the Design DNA (today's vocabulary)

```
MOTIF + COORDINATE: <e.g. "control room" · "Bloomberg terminal meets Teenage Engineering">
AVOID-LIST:         <4-6 things this page won't do>
PALETTE:
  - neutrals: <TINTED, not pure — dark e.g. #09090B/#18181B/#27272A/#3F3F46 · light #FAFAFA/warm off-white>
  - accent:  <ONE or two SHARP saturated accents (can be electric); where it's allowed — NOT indigo/violet>
  - mode:    <light | dark | warm-light>
TYPE (pick a real 2025 pairing — see vocabulary below; NOT Inter-only, NO mono as a brand/UI face):
  - display: <characterful grotesque OR editorial serif + why it fits the motif>
  - body:    <neutral groteske workhorse>
  - move:    <extreme weight contrast / serif-display+sans / oversized condensed / optical sizing>
DENSITY:   <airy-editorial | balanced | dense-terminal>
MOTION:    <pick from motion.md — at least a blur-in reveal + one signature motion; match the brand>
TEXTURE:   <grain (SVG 15-30%) / dot or blueprint grid / stepped luminance / none — choose deliberately>
IMAGERY:   <real product UI / sculptural 3D (Spline) / editorial photo / custom illustration — see image-strategy.md>
SIGNATURE: <the ONE genre-breaking move (see below). Must surprise; must fit the motif.>
```

→ Then carry tokens into **build-system.md**, motion into **motion.md**, imagery into **image-strategy.md**.
→ Run the **Anti-Convergence checklist** (bottom of this file) before you build.

---

## CURRENT typography (use this, not the prior)

Inter-as-the-whole-system is the literal AI/early-stage default; mono-everywhere and Space Grotesk read
as 2021-23 crypto/AI templates. The current move is a **characterful display + a neutral grotesque body**.

**Display / headline (pick to fit the motif):**
- *Characterful grotesques* — **Geist**, Schibsted Grotesk, Bricolage Grotesque, Host Grotesk, Hanken
  Grotesk (free); Söhne, ABC Diatype, PP Neue Montreal, Aeonik, GT America/Walsheim, Monument Grotesk,
  TWK Lausanne, Suisse Int'l (paid — name as the intent / use closest free match).
- *Editorial serif display* (the 2025-26 signature, used sparingly at large size) — **Fraunces** (variable
  opsz/SOFT/WONK), **Instrument Serif**, DM Serif Display, Newsreader (free); PP Editorial New, GT Super,
  Reckless, Signifier, Tiempos Headline, Canela (paid).
  > ⚠ **Over-reflex warning:** an editorial *serif headline on dark* has become this skill's default for
  > anything "premium/authoritative". It is NOT the only premium move and it's now a tell. For at least
  > half your pages, make the headline a **characterful heavy grotesque** instead (Bricolage, Geist,
  > Aeonik, Monument, Druk-condensed) — equally premium, and it varies the output. Don't reach for Fraunces
  > on autopilot.
- *Condensed power display* — Druk, Right Grotesk, Hatton, Anton (free-ish) for magazine-coverline heroes.

**Body workhorses (replace Inter/Open Sans/Lato/Roboto):** **Geist**, Hanken Grotesk, Schibsted Grotesk,
Plus Jakarta Sans, Albert Sans, Instrument Sans, Inter *only* as a quiet body under a distinctive display.

**Mono — banned as a design choice.** It's ugly and dated (a 2021-23 crypto/AI-template tell). Do NOT use a
monospace face for eyebrows, labels, captions, nav, buttons, **numbers, stats, data, or table cells** — for
figures use the grotesque body with `font-variant-numeric: tabular-nums`, which reads far better. The ONLY
place monospacing is permitted is inside a **literal code/terminal snippet** (code is monospaced by nature) —
and even there keep it to one small surface, never the page's texture. If you're reaching for mono to add
"technical flavour," stop: that flavour *is* the generic look we're killing.

**Moves that read 2025:** extreme weight contrast (100/200 vs 800/900), optical sizing + negative
tracking on big display, tabular numerals for figures, variable-font axes, a real type scale.

**Do NOT use** (dated tells): Inter for everything incl. headings · Space Grotesk / Space Mono · Poppins
/ Montserrat · Playfair Display · Open Sans / Lato / Roboto as the brand face · **any monospace font outside
a literal code block** (no mono eyebrows, labels, numbers, or data — it's banned, see above).

→ Loading recipes (Google Fonts / Fontshare / Geist CDN) are in **build-system.md**.

## CURRENT palette & surface

- **Tinted neutrals, never pure.** Dark: `#09090B → #18181B → #27272A → #3F3F46` (zinc/stepped luminance);
  light: `#FAFAFA` or a warm off-white. Pure `#000`/`#FFF`/`#2563EB` read flat and templated.
- **One neutral + 1-2 SHARP accents.** Accents can be electric. Steal palettes from culture or IDE themes
  (e.g. a film, a city at night, a Tokyo Night / Catppuccin editor theme). **Forbidden default: indigo/
  violet, and the purple→blue hero gradient — the single strongest AI tell.**
- **Gradients only when functional** — a faint heading gradient, a blurred ambient glow behind product
  UI, a subtle mesh. Not a full purple-to-blue wash.
- **Texture as craft** — restrained SVG grain (`feTurbulence`, 15-30% opacity), 1px hairline borders,
  faint blueprint/dot grid, stepped-luminance surfaces over heavy drop-shadows and glassmorphism.

## The signature must break the genre

The ONE memorable move pages in this niche usually DON'T do — driven by the motif. If it's a genre trope
(dark dev-tool's live-console+sparkline; fintech's floating phone; the editorial-serif-on-dark that even
*this skill* now overuses), it's not a signature. Push past it: an unexpected layout archetype, a tactile
texture, a bold color block, real product UI staged unusually, a typographic punchline, a physical metaphor.

---

## Anti-Convergence — mandatory variety (run before building)

Convergence is the enemy even after you escape the obvious prior. It bites at two levels — **structure**
(the skeleton) and **surface** (the skin) — and the structural one is what makes pages rhyme even when the
colours differ. Check both; rotate so two pages by this skill never share a spine.

**Structure — the skeleton (the part everyone forgets to vary):**
- [ ] **Composition archetype** — a *deliberate* pick from the list above, different from your last build.
      Not reflexively split-screen / hero-left-text + image-right.
- [ ] **Section sequence** — transcribed from your anchor (Move 2), driven by the story — not the generic
      hook → logos → 3-cards → CTA boilerplate on autopilot.
- [ ] **Hero grammar** — break the prior chain. You do NOT need a kicker/eyebrow label, *and* a
      one-word-accent headline, *and* two CTAs (filled + ghost-with-arrow), *and* a row of exactly three
      stats. Drop or reshape **at least two** of these every build.
- [ ] **The kicker is not mandatory** — a small tracked label above the H1 (`A SLEEP & RECOVERY RING`) is
      the most reflexive opener there is, and it quietly survives even when everything else varies. For at
      least **half** your pages, lead with something else: open straight on the headline, a nav-adjacent
      one-liner, a date/price/stat, a single product word, or a question. If you *do* use one, make it do
      real work — a place, a provocation, a spec — never just restate the category in caps.
- [ ] **Feature layout** — not always three equal cards in a row. Consider a vertical alternating zigzag,
      a bento, one deep showcase, a numbered walkthrough, a comparison table.

**Surface — the skin:**
- [ ] **Typeface** — not the same display face you'd reflexively pick; does it fit THIS motif specifically?
- [ ] **Accent** — a different hue/strategy than the last build; not indigo/violet.
- [ ] **Texture** — grain / grid / flat / none — a deliberate, varied choice.
- [ ] **Icons** — a multi-weight set (Phosphor, Iconoir, Hugeicons), matched to the shape language — not
      raw single-weight Lucide/Feather.
- [ ] **Corner radius & density** — sharp+dense vs soft+airy is a real lever; don't default to 16px-rounded.
- [ ] **Signature** — present, genre-breaking, and different from your last page.

**Then self-diff before you ship.** Lay your page's skeleton next to the AI-generic stack below. If you
can't state plainly how yours differs *structurally* (not just in colour/font), you reverted — go back to
Move 2 and rebuild on a different anchor.

**Never ship the AI-generic stack:** Inter headings + indigo/purple gradient + **eyebrow-pill →
one-word-accent headline → filled-+-ghost CTA → row-of-exactly-three-stats → logo wall → three equal icon
cards** + 16px-rounded everything + faint soft shadow + hero-left/image-right + mono eyebrows + Corporate
Memphis mascots (Humaaans/unDraw/Storyset) + stock "diverse team at laptops". If two or more of these are
present, you've reverted to the prior — redo the vibe.

---

## The DTC reflexes — the model's defaults; default them OFF

Even after the kicker fix, an audit of pages built by this skill found they STILL rhymed — because the
model has a second, deeper set of "modern DTC/SaaS landing" reflexes it reaches for *every single time*.
None is wrong on its own; using the **whole set on every page IS the convergence**, and it's why output
"doesn't look like it's based on a real page" — it's based on the model's average of all pages. Treat each
as **default-OFF**: a given build may use **at most one or two**, picked deliberately, and must vary *which*
across builds. When in doubt, do the thing the reflex replaces.

1. **The one-accent-word headline** — a headline with exactly one word italicised or recoloured
   (*"the chai you **actually** miss"*, *"your air, finally **felt**"*). The single most repeated tell —
   it shows up in every hero AND every section heading. Most headlines should have **zero** accent words.
2. **The dual CTA (filled + ghost-with-arrow)** — one solid button beside one outline "→" button. Often a
   single CTA, an inline email field, or a text link is truer to the product. Vary it.
3. **The contrarian problem-reframe** — *"You don't have an X problem. You have a Y problem."* / *"A teabag
   is the ghost of chai."* A real persuasive move, now a tic. Don't open the second section this way by reflex.
4. **The dark full-bleed CTA band at the end** — a near-black closing section with an accent-word headline
   and a button. Fine occasionally; not the default ending. A footer-integrated CTA, a quiet inline close,
   or no separate CTA section are all valid.
5. **The hero stat/spec strip** — a row of 3–4 figures pinned under the hero. Earns its place sometimes;
   reflexive the rest.
6. **The arc itself** — `hero → problem → 3-up → testimonial → pricing → dark-CTA → footer`. This is the
   model's one true landing shape, and following it is how every page ends up the same. **Real pages don't
   all share it** (look at a full-page capture — Linear has no pricing and no problem-reframe; it's a
   feature-by-feature product tour ending in a changelog). Take your structure from your *anchor's real
   page*, not from this arc. See **section-patterns.md → Page archetypes**.

Self-check: if your page has the accent-word headline **and** the dual CTA **and** the contrarian reframe
**and** the dark CTA band, you didn't design a page — you printed the template. Strip it back to what your
anchor actually does.
