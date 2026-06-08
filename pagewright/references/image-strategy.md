# Image strategy — let images do the heavy lifting

The prettiest SaaS sites are not pure CSS. The thing that makes them feel expensive is usually a
**great visual**: a crisp product shot, an evocative 3D render, a characterful illustration. AI tools
tend to avoid images and simulate everything with gradients and blobs — which is exactly why their
output looks generic. This skill does the opposite: **plan the images first, reserve real space for
them, and either generate them or hand the user ready-to-run prompts.**

## Build the product visual in HTML/CSS — don't placeholder it (the #1 fidelity rule)

The single biggest reason AI landing pages look like empty wireframes is dropping a **gray placeholder box**
where the product should be. The best real sites — Linear, Stripe, Attio, Vercel — do the opposite: they
**build the product UI in HTML/CSS** right in the page. A faithful hand-built UI is what makes a hero read
as a *real shipped product* instead of a mockup.

**If the visual is a product UI, dashboard, data table, chart, code/diff, terminal, chat, map, or
diagram → BUILD IT in HTML/CSS/SVG.** Real-looking data, crisp micro-typography (~11–13px), 1px hairline
borders, status pills, avatars (CSS gradient tiles), tabular numerals; frame it in browser/app chrome. This
is usually the page's signature and costs nothing but care. (Open a library thumbnail like linear.app or
attio.com and rebuild its surface faithfully.)

**Reserve image placeholders + generation for what you genuinely CAN'T build in code:** photography,
3D/sculptural renders, illustration, brand logos. For those, ship a dimensioned placeholder AND (preferably)
generate the asset — a filled hero beats an empty one every time.

Quick test: **if your hero is a gray box, you're not done.** Build the UI, or generate the image.

## Build interfaces; photograph or generate OBJECTS (the line that saves you from clip-art)

The rule above is about **interfaces and data** — dashboards, tables, charts, code, chat, diagrams,
type-driven graphics. There, hand-building is a superpower: divs and SVG read as *real*.

It is **NOT** a licence to hand-draw a **physical object** in SVG. A bottle, a ring, a device, a can with
condensation, a piece of fruit — modelled from scratch in one pass — almost always comes out as flat,
slightly-wrong clip-art. A CSS-gradient ring reads as the *wireframe* of a ring, not a ring. This is the
single most common way a hand-built hero looks "meio pá" (janky).

Route by what the visual **is**:
- **Interface / data / diagram / code / type** → BUILD in HTML/CSS/SVG. (A data-viz ring that traces real
  sleep stages is an *interface* — build it, and invest in it.)
- **Physical object / material / organic form / 3D / a real scene** → **photograph it (Unsplash, graded —
  see below) or generate it (Nano Banana)**. A graded real photo or a clean generated render beats a
  hand-SVG object every time. A flat, rectangular thing (a card, a sticker, a UI window) is far safer to
  hand-build than a curved, lit, organic one (a bottle, a ring, a can).

If you DO hand-build an object, clear the bar or don't ship it: real proportions (look at a reference
photo first), a **material gradient** (not a flat fill), layered specular highlight + core shadow + a
contact/cast shadow on a surface, and consistent light direction. If you can't clear that bar, ship a
dimensioned **graded placeholder + a generation/photo prompt** instead — an honest placeholder beats janky
clip-art, and the photo/generation flow below will fill it properly.

## Principle

For every visual moment, ask: *would a real/generated image say this better than CSS?* If yes, make an
image slot. Don't fake a product screenshot with stacked divs when a real image (or a generated mock)
would sing. Don't fill the hero with abstract shapes when a product canvas would prove the value.

But stay disciplined: a few strong, intentional images beat a page littered with stock. Pick the moments
that matter (usually: hero visual, one or two feature visuals, maybe an illustration accent).

## Where images earn their keep

| Slot | Typical image type | Why |
|---|---|---|
| Hero visual | product screenshot / live UI / abstract-3D | proves it's real, sets the mood |
| Feature blocks | focused product shots / diagrams | show, don't tell |
| How-it-works | simple illustrations / step visuals | makes it concrete & friendly |
| Social proof | real logos (SVG) | borrowed trust |
| Testimonials | real avatars | humanizes |
| Background accents | gradient-mesh / texture / noise | mood, used sparingly |

## Image types & prompt recipes

When you create an image slot, decide its **type** and write a ready-to-use prompt. Keep prompts
aligned to the Design DNA (palette, mood). Recipes:

- **Product screenshot / app UI mock** — *"Clean [product type] dashboard UI, [dark/light] theme,
  [accent] accents, showing [key feature]; realistic SaaS interface, crisp typography, subtle depth,
  no lorem ipsum — use plausible real labels; 16:10."* Frame it in browser/device chrome in the markup.
- **Abstract / 3D render** — *"Abstract 3D render, [palette] gradient, soft studio lighting, glass/metal
  forms, premium tech aesthetic, [mood] feel, high detail, 4k, transparent or [bg] background."*
- **Illustration** — *"[flat/iso/line] illustration of [concept], [palette], consistent stroke,
  friendly modern style, on [bg]; no text."*
- **Photography** — *"Editorial photo of [subject], natural light, [mood] tone, shallow depth of field,
  authentic not stock-y."*
- **Gradient-mesh / texture** — *"Soft mesh gradient, [2-3 palette colors], grainy, subtle, abstract
  background; seamless."*

Tip: keep a consistent style descriptor across a page's images so they feel like one set.

## Placeholders (always ship these)

Every image slot gets a **dimensioned, labeled placeholder** so the page looks intentional with zero
assets and the user knows exactly what to drop in.

Use **`scripts/placeholder.py`** to emit placeholder SVGs/PNGs at the right aspect ratio, labeled with
the slot name (e.g. "HERO — product screenshot 16:10"). In the markup, give each `<img>` a real
`width`/`height`, descriptive `alt`, and a comment with the generation prompt so it's swap-ready:

```html
<!-- IMAGE SLOT: hero product screenshot — prompt: "Clean analytics dashboard, dark theme, indigo
     accents, showing a funnel chart; realistic SaaS UI, 16:10" -->
<img src="assets/images/hero-placeholder.svg" width="1280" height="800"
     alt="Acme dashboard showing conversion funnel" class="rounded-xl border border-surface" />
```

## Optional: generate the images (opt-in)

Generation is **off by default**. Offer it; if the user wants it AND a generator is configured, run it.

- **Gemini "Nano Banana" (Gemini 2.5 Flash Image)** via **`scripts/gen_image.py`**. Needs a
  `GEMINI_API_KEY` (from Google AI Studio — note: a Gemini *app* subscription is NOT API access; the
  API has its own free tier with rate limits, and image-gen availability/cost on the free tier varies,
  so the script fails gracefully and falls back to placeholders + prompts).
- **Flow:** for each slot, the script takes the prompt + dimensions, writes the result into
  `assets/images/`, and you wire it into the markup replacing the placeholder.
- **No key / declined?** Ship placeholders + the prompts list (a small `IMAGE-PROMPTS.md` in the output)
  so the user can paste them into Nano Banana / Midjourney / their tool of choice and drop the results in.

Either way the page is complete and runnable. Generation is an enhancement, never a dependency.

## Optional: fetch a real photo — Unsplash (opt-in)

Some slots want a *real photograph*, not a render: a full-bleed cinematic landscape behind the hero
(the **full-bleed-photo** composition archetype — see design-dna.md), an organic texture (fog, stone,
paper, foliage, water), an editorial still life. Generation can fake these but real photography often
reads truer and costs nothing to generate. Use **`scripts/fetch_unsplash.py`** (off by default; needs a
free `UNSPLASH_ACCESS_KEY`). It searches by a mood query, downloads a sized JPEG, registers the download
and writes the required attribution to `UNSPLASH-CREDITS.md`.

**Taste guards (the script can't enforce these — you must):**
- **Place, object, texture, abstraction — not people.** Landscapes, skies, water, foliage, stone/paper/
  fabric, macro detail, architecture, hands/craft, ingredients shot editorially. A photo with *people as
  the subject* almost always reads as stock ("diverse team at laptops") — the exact slop this skill avoids.
- **Always grade it** so it belongs to the page and not to a stock library: a duotone/colour overlay in
  the Design DNA palette, a grain layer, and a gradient scrim for text contrast. The script prints a
  copy-paste grade snippet. An ungraded raw stock photo is a tell; a hard-graded one can be the signature.
- **Pick deliberately.** Pass a specific, moody query ("low fog over black volcanic rock, muted, no
  people"), and use `--index` to step past the obvious first result if it's too generic.
- **Pairs with Nano Banana, doesn't replace it.** Real photo for place/texture; generate for 3D/product/
  illustration. Build product UI in HTML/CSS as always (the #1 rule above).

```bash
python scripts/fetch_unsplash.py --query "low fog over pine forest at dawn, muted, no people" \
    --out assets/images/hero-bg.jpg --orientation landscape --width 1600
```

No key / declined? The dimensioned placeholder IS the fallback, and you can hand the user the same query
to grab a photo by hand. The page stays complete and runnable.

## Current asset choices (so it doesn't look dated)

- **Icons — use a multi-weight set, matched to the page's shape language:** Phosphor, Iconoir, or
  Hugeicons (free, many weights), or premium Untitled UI Icons. **Avoid raw single-weight Lucide/Feather**
  used with no stylistic match — that's the default-template look.
- **Illustration / 3D — go sculptural, not flat-vector.** Lightweight 3D (Spline embed or pre-rendered
  Blender) as a hero — sculptural spheres, ribbons, liquid-metal/glass forms — reads premium. If you use
  illustration, keep it custom and characterful. **Never** Corporate Memphis mascots (Humaaans, unDraw,
  Open Peeps, Storyset, ManyPixels) or generic isometric "servers & connectivity" tech scenes — both are
  dead giveaways abandoned by real brands.
- **Photography — real over stock.** Founder/team/product photos with a consistent grade beat
  "diverse team at laptops" stock. If none exist, prefer product UI or 3D over a stock *people* photo —
  but a graded editorial **place/texture** photo (landscape, fog, stone, foliage) is fair game and often
  beautiful: fetch it with `scripts/fetch_unsplash.py` and grade it (see the Unsplash section above).
- **Texture beats sheen.** A little grain/noise over a muted background reads more human and current than
  a hyper-perfect, glossy, shadow-soft AI surface.

## Don't

- Don't use generic stock or clip-art-y illustrations that say nothing about the product.
- Don't overload — a page of images with no breathing room is as bad as none.
- Don't ship broken `<img>` with no fallback; the placeholder IS the fallback.
- Don't present invented logos/testimonial photos as if real — label placeholders as swappable.
