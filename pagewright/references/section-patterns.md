# Section patterns & storytelling

A landing page is a **persuasive narrative**, not a stack of UI blocks. The sections are beats in an
argument. Pick the beats that tell THIS product's story, in an order that builds, and write copy a
founder would actually ship.

## The narrative arc

Most high-converting SaaS pages walk this arc (adapt, don't follow rigidly):

1. **Hook** — in 5 seconds: what is this, who's it for, why care. (Hero)
2. **Credibility** — you're not alone / not risky. (Logo wall, metrics, "backed by")
3. **The problem** — name the pain the visitor feels right now. (Problem framing)
4. **The solution** — how you solve it, shown not just told. (Feature blocks, product visuals)
5. **How it works** — make it feel easy and concrete. (Steps / workflow)
6. **Proof** — others got the result. (Testimonials, case stats)
7. **Objection handling** — pricing clarity, FAQ, security/compliance, integrations.
8. **The ask** — one clear, repeated action. (Final CTA, then footer)

Two classic copy frameworks to lean on when stuck:
- **PAS** — Problem → Agitate → Solution. Great for pain-driven products.
- **AIDA** — Attention → Interest → Desire → Action. Great for broad/consumer.

You rarely use every section. A focused page (hero → proof → 3 feature beats → how-it-works → testimonial
→ pricing → FAQ → CTA → footer) beats an everything-page. Cut anything that doesn't move the argument.

## Page archetypes — the arc above is ONE shape, not the only one

The narrative arc is the *classic conversion scroll* — and if every page you build follows it, every page
rhymes, no matter how you skin it. Real top landing pages take **structurally different shapes**. Pick one
deliberately per build (and rotate across builds), driven by the product and — above all — by **your
anchor's actual full page** (open `reference-library/full/<domain>.jpg` when it exists and copy the real
sequence, quirks and all; don't normalise it back to the arc).

- **Product tour** — hero (real product UI) → feature after feature, each anchored by its own UI panel,
  alternating sides → a proof/changelog beat → CTA. Often **no problem-reframe and no pricing**.
  e.g. linear.app, attio.com, retool.com.
- **One-screen statement** — a single viewport does the whole job: headline + one strong visual + one
  action. Little or no scroll. e.g. minimalist launch pages, cohere.com, bun.sh.
- **Editorial long-read** — a magazine story: full-bleed photography, long-form prose sections, pull-quotes,
  generous air. e.g. aesop.com, patagonia.com, palantir.com.
- **Catalog / product-grid** — the products *are* the page; a shelf/grid, shop-forward, minimal marketing
  copy. e.g. publicgoods.com, glossier.com, gymshark.com.
- **Manifesto** — an argument or attitude, type-driven, voice over feature-lists; the product appears late.
  e.g. liquiddeath.com, oatly.com.
- **Spec sheet** — dense and technical: tables, figures, an engineering-bench framing, numbered figures.
  e.g. oxide.computer, lithic.com.
- **Demo-led** — a live, working/interactive demo is the hero and carries most of the page. e.g. cal.com,
  arcade.software.
- **Comparison-led** — built around a before/after or a vs-table as the central beat.
- **Classic conversion scroll** — the arc above (hero → problem → features → proof → pricing → CTA). Still
  great — just *one* option chosen on purpose, not the autopilot default.

Rule: **name your page archetype before you write markup**, make it different from your last build, and let
the anchor's real structure — not this list or the arc — dictate the actual sections.

## Length & density — match the anchor; cut filler, not richness

Restraint means **no filler** — NOT **few sections**. The trap cuts both ways, and both are real failures of
this skill: early builds bloated into a generic everything-page; a later over-correction toward "be short"
stripped a *rich* anchor (Mercury — a dense ~15-section page with a cinematic photo hero, a detailed product
dashboard, two 2×2 image-card grids, a testimonial carousel, a stat row, news cards, footnoted disclosures)
down to a flat 7-section skeleton of text panels that read as **simplistic**, not confident.

The rule is **anchor-relative**: a page is as long and as dense as the page it's anchored on — no more, no less.

- **Minimal anchor → minimal page.** Vercel, cohere, a one-screen launch: don't pad it with a problem
  section, a stat row, and a testimonial wall it doesn't have.
- **Rich anchor → rich page.** Mercury, Stripe, Aesop are *dense*: real photography, several distinct product
  visuals, image-backed feature cards, carousels, footnoted detail, varied section treatments. **Copy that
  density** — generate the photos, build several different visuals, vary the section *type*. A flat stack of
  text panels is not a faithful copy of a lush page; it's the simplistic tell, and it's half the height.
- **Cut FILLER, keep RICHNESS.** Filler = a redundant benefit grid, a second testimonial wall, an
  over-explained step, a sentence that won't change a mind. Richness = real imagery, distinct product
  surfaces, the proof a real page carries. Cut the first; never strip the second to hit a section count.
- **Vary the section TYPE, not just the copy.** Each beat should be its own *kind* of thing — a photo beat, a
  built UI, an image-card grid, a carousel, a stat band, a pull-quote, a news row. The same flat panel
  repeated reads as simplistic even at the right length.

Self-check: if your page is roughly half the height of its anchor and every section is a flat text panel,
you **under-built** it — go back and match the anchor's richness.

## Current section menu (from a ~670-example survey of live SaaS sites)

Real modern pages assemble from these, roughly in this order of frequency. For any section you're about to
build, **open the thumbnail of an in-library exemplar** (Read `reference-library/thumbs/<domain>.jpg`) and
study how a real 2025 site actually does it — then build yours, don't reinvent from memory.

- **hero** (~122 ex) → study: attio.com, evervault.com, cap.so, antimetal.com, amplemarket.com
- **logos / social proof** (~28) → linear.app, vercel.com, neon.tech, evervault.com, mintlify.com
- **value-proposition** (~24) → dovetail.com, neon.tech, synthesia.io, loops.so, jasper.ai
- **features / bento** (~93) → evervault.com, dovetail.com, lattice.com, highnote.com, cap.so
- **how-it-works** (~19) → synthesia.io, lattice.com, dovetail.com (+ study any with a "steps" flow)
- **compare / vs-table** (~11) → outseta.com (+ pricing-style tables)
- **testimonials** (~70) → framer.com, attio.com, highnote.com, lattice.com, jasper.ai
- **pricing** (~59) → attio.com, framer.com, cap.so, dovetail.com, highnote.com
- **integrations** (~23) → linear.app, dovetail.com, lattice.com, outerbase.com
- **faqs** (~20) → framer.com, equals.com, liveblocks.io, lattice.com, outerbase.com
- **cta** (~64) → framer.com, evervault.com, attio.com, dovetail.com, equals.com
- **footer** (~56) → framer.com, vercel.com, neon.tech, mintlify.com, evervault.com

You rarely use every section — pick the beats that tell THIS product's story (next). But when you build a
beat, anchor it to a real example above.

## Section library

For each: its job, a few **structural variants** (vary these per project — don't always reach for the
same one), and the trap to avoid. Choose variants that fit the Design DNA's density and signature.

### Hero (the 5-second test)
**Job:** communicate value + primary CTA + a visual that proves it's real.
**Variants:**
- *Split* — headline/CTA left, product visual right. Workhorse; keep the visual real-looking.
- *Centered + canvas below* — centered headline/CTA, a large product screenshot/canvas spanning under
  it. Strong when the product is visual.
- *Editorial* — oversized type-led hero, minimal or no image, lots of space. For premium/minimal moods.
- *Interactive/live* — a faux-live product surface (animated or static "in-use" UI). High effort, high
  payoff for technical products.
**Always:** one headline (the value, not the category), one supporting line, one primary + optional
secondary CTA, and a credible visual or a deliberate no-image choice. **Trap:** vague headline
("The future of work"), centered-everything by default, a stocky illustration that says nothing.

### Social proof / logo wall
**Job:** borrow trust fast. **Variants:** grayscale logo strip; "trusted by N teams"; a single big
metric; a marquee. **Trap:** fake logos presented as real — use placeholders labeled as swappable.

### Problem framing
**Job:** make the visitor feel understood. **Variants:** before/after; a short "sound familiar?" list;
a contrast block (the old way vs your way). **Trap:** skipping it — solutions land harder after pain.

### Feature blocks (the solution)
**Job:** show how you solve it. **Variants:**
- *Alternating rows* — text/visual, visual/text, repeating. Each row = one real benefit + one visual.
- *Bento grid* — mixed-size tiles, each a capability; great for "platform" products. Use real content,
  not three identical icon cards.
- *Tabbed/segmented* — one big visual that swaps by tab; good when features share one surface.
- *Spotlight* — one flagship feature gets a full immersive section, others summarized.
**Trap:** the cliché "3 columns, line icon, 4 words, generic blurb." If you must use cards, make them
specific and uneven enough to feel authored.

### How it works
**Job:** make adoption feel effortless. **Variants:** numbered steps (3–4 max); a connected flow/diagram;
a short timeline. **Trap:** more than 4 steps, or steps that restate features.

### Testimonials / case proof
**Job:** real humans got real results. **Variants:** quote cards with face+name+role; a single hero
quote; a stat-led case ("cut onboarding 60%"). **Trap:** anonymous or obviously-fake quotes.

### Pricing
**Job:** remove cost ambiguity. **Variants:** 2–3 tiers with one highlighted; single-plan + "talk to
us"; usage-based explainer. **Trap:** hiding price when the audience expects it; >3 tiers; feature
checklists so long they intimidate.

### FAQ / objections
**Job:** answer the 4–6 things blocking signup (price, security, migration, support, fit). **Variants:**
accordion; two-column Q/A. **Trap:** marketing fluff instead of the real worry.

### Final CTA
**Job:** ask once more, confidently. **Variants:** full-width color block; centered with a last proof
point; a focused card. **Trap:** a weak repeat of the hero. Make it feel like the close.

### Nav & footer
**Nav:** logo, 3–5 links, one primary CTA; sticky and condensed on scroll. **Footer:** real structure
(product/company/resources/legal), not a lonely copyright line.

## Copy patterns (write like a human)

**Headline formulas** (pick the one that fits; fill with specifics):
- *Outcome:* "Ship [outcome] without [pain]." → "Ship dashboards without a data team."
- *Category redefine:* "The [familiar thing], rebuilt for [shift]." → "Issue tracking, rebuilt for the
  AI era."
- *Direct value:* "[Verb] [valuable thing] [qualifier]." → "Turn support tickets into product insight."
- *Audience-named:* "For [audience] who [need]."

**Subheadline:** one sentence that says *how* or *for whom*, adding concreteness the headline can't.

**CTA copy:** specific to the action — "Start building", "Get a demo", "Join the waitlist", "Deploy in
minutes". Never bare "Submit"/"Sign up" unless the user insists.

**Anti-cliché list — do not ship these:**
- "Empower your workflow" / "Supercharge your productivity" / "synergy" / "seamless" (overused) /
  "next-generation" / "revolutionary" / "Powerful features for modern teams" / "Built for the way you
  work." If a phrase could appear on any SaaS site, replace it with something only THIS product could say.

**Microcopy matters:** button states, empty-state lines, tooltip hints, form helper text — these are
where craft shows. Spend a little care here.

Carry the chosen sections into the build. Map each image slot you implied here into
**image-strategy.md**.
