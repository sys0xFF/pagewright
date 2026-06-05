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

## Move 2 — Look at the real references, and copy faithfully

The library (`references/reference-library/`) is 213 of the best current SaaS sites, with full
screenshots. **Don't just read the prose entries — LOOK at the actual pixels:**

1. From the vibe + niche, pick **3-5 references** from `INDEX.md` (span 2+ moods to force synthesis).
2. **Read their thumbnail images** at `reference-library/thumbs/<domain>.jpg` with the Read tool. Your
   eyes calibrate to *current* execution far better than from text — absorb the real type, spacing,
   color temperature, and how product UI is shown.
3. Pick **ONE primary** reference for **structure** and **copy its bones faithfully** — the section
   sequence, the hero composition, the grid logic, the specific signature device. Fidelity is the
   point: a faithful structural copy that you re-skin is far better than a vague "inspired by." (The
   user's rule: *even when copying, be faithful.*)
4. Pull the **skin** (palette, type, motif details) from the *other* references + your vibe, so the
   re-skinned result is nobody's clone. **Remix ≥3, clone 0 — but copy structure boldly from one.**

This is how you escape the prior: you're building from a real 2025 page's bones, not from memory.

---

## Move 3 — Lock the Design DNA (today's vocabulary)

```
MOTIF + COORDINATE: <e.g. "control room" · "Bloomberg terminal meets Teenage Engineering">
AVOID-LIST:         <4-6 things this page won't do>
PALETTE:
  - neutrals: <TINTED, not pure — dark e.g. #09090B/#18181B/#27272A/#3F3F46 · light #FAFAFA/warm off-white>
  - accent:  <ONE or two SHARP saturated accents (can be electric); where it's allowed — NOT indigo/violet>
  - mode:    <light | dark | warm-light>
TYPE (pick a real 2025 pairing — see vocabulary below; NOT Inter-only, NOT mono-everywhere):
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

**Mono — ONLY for genuinely technical content** (code, latency, data tables): Geist Mono, Berkeley Mono,
JetBrains Mono, Commit Mono. **Never** as decorative eyebrows/labels/buttons — that's the dead giveaway.

**Moves that read 2025:** extreme weight contrast (100/200 vs 800/900), optical sizing + negative
tracking on big display, tabular numerals for figures, variable-font axes, a real type scale.

**Do NOT use** (dated tells): Inter for everything incl. headings · Space Grotesk / Space Mono · Poppins
/ Montserrat · Playfair Display · Open Sans / Lato / Roboto as the brand face · mono microcopy everywhere.

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

Convergence is the enemy even after you escape the obvious prior. **Rotate these so two pages by this
skill never rhyme.** Check each:

- [ ] **Typeface** — not the same display face you'd reflexively pick; does it fit THIS motif specifically?
- [ ] **Accent** — a different hue/strategy than the last build; not indigo/violet.
- [ ] **Layout archetype** — vary it: split-screen / centered-editorial / asymmetric / full-bleed-canvas /
      bento / poster. Not always "hero-left text, image-right + three cards."
- [ ] **Texture** — grain / grid / flat / none — a deliberate, varied choice.
- [ ] **Icons** — a multi-weight set (Phosphor, Iconoir, Hugeicons), matched to the shape language — not
      raw single-weight Lucide/Feather.
- [ ] **Corner radius & density** — sharp+dense vs soft+airy is a real lever; don't default to 16px-rounded.
- [ ] **Signature** — present, genre-breaking, and different from your last page.

**Never ship the AI-generic stack:** Inter headings + indigo/purple gradient + three equal icon cards +
16px rounded everything + faint soft shadow + hero-left/image-right + mono eyebrows + Corporate Memphis
mascots (Humaaans/unDraw/Storyset) + stock "diverse team at laptops". If two or more of these are present,
you've reverted to the prior — redo the vibe.
