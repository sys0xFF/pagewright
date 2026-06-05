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
