# Product UI — building components that look real, not generic

The fastest way to make a landing page look shipped-by-a-senior-team is a **faithful, hand-built product
surface** (dashboard, table, chart, log, card) in HTML/CSS — see image-strategy.md. But the default way the
model builds those surfaces is **generic and samey**: one dark panel, a full 1px hairline box, a status
pill, soft shadow, mono numbers — the same component on every page. This file fixes that. It's distilled
from how real top product teams (Linear, Stripe, Attio, Retool, Vercel, Mercury, Sentry, Raycast, …) build
each component, read off their real screenshots.

**How to use:** before you hand-build any product UI, open the matching section below AND `Read` the
thumbnail of a named exemplar — then build to that craft, turning the *variety levers* so two of your pages
never ship the same component.

Cross-cutting rules (they apply to every component here):
- **Dividers, not boxes.** Separate surfaces by lightness + spacing + 1px dividers or an inset top
  highlight — not a full `border` box with `rounded-xl` + `shadow-2xl` around everything.
- **Tinted neutrals**, never pure `#000`/`#fff`. Surfaces step in lightness to read as panes.
- **Ration the accent.** A single status dot / one marker — not accent on every pill, row, and number.
- **No decorative monospace — ever.** Numbers, data, table cells, captions, labels use the grotesque body
  with `font-variant-numeric: tabular-nums`. Mono appears ONLY inside a literal code/terminal snippet.
- **Restraint.** Real product UI is quiet and dense with signal. Small low-contrast labels, real-looking
  data, a clear hierarchy — not loud chrome.

→ Back to **[build-system.md](build-system.md)** for tokens/fonts, **[image-strategy.md](image-strategy.md)**
for build-vs-photograph, **[design-dna.md](design-dna.md)** for the type/colour vocabulary.

---
## Dashboards & app consoles (the product frame)

The "product frame" is the in-page replica of an app shell — sidebar + content + (often) a detail rail. It's the single most-faked component on a SaaS page and the one that most often gives away an AI build, because everyone reaches for the same dark card with a hairline box around it. Real top teams treat the frame as architecture: the *structure* (panes, rails, breadcrumbs, density) does the work, and borders almost disappear.

### What real top sites actually do

- **Linear builds a 3-pane shell, not a card.** Sidebar (~240px) / issue list / detail rail, each a *separate surface* at a slightly different lightness — the divisions read as panes, not as one box with internal lines. The whole frame sits on near-black `#08090A` (never `#000`), and the app surface is one step lighter (`~#0F1011`). The only "border" that matters is a **1px inset top highlight** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.04)`) that catches light like a real window edge — there is no full 1px box around the frame.
- **Chrome is breadcrumbs and counts, not decoration.** Linear's header carries `02 / 145`, an issue key `ENG-2703`, tiny nav chevrons — quiet wayfinding in ~13px. That positional text is what makes it read as a *real* app mid-task, not a marketing mockup. Set it in the body grotesque with `tabular-nums`, never mono.
- **Attio proves the light version: dividers, not boxes.** Its console is near-white with grouped sidebar sections and a tab row separated by single **hairline dividers** (`border-bottom`), zero card outline, generous whitespace. Density comes from tight line-height and small labels, not from cramming — restraint is the aesthetic.
- **Sidebar typography is small and low-contrast.** ~13px labels, ~16px icons, section headers ("Workspace", "Favorites") in an even smaller, dimmer, slightly tracked label. The *active* row gets a faint tinted fill (`bg-white/[.06]`) and full-ink text; everything else sits at 60-70% ink. No accent color on nav — the accent is rationed.
- **Accent is a single dot, never a flood.** Linear's indigo shows up only as the `In Progress` status dot and one inline link marker — the primary "Sign up" pill is plain white. Status lives in small colored dots + a text label, not in big filled pills everywhere.
- **Basedash shows the data-viz frame: glow, big tabular figures, tiny deltas.** Vivid multicolor bars on near-black, headline metrics like `4.3k` / `20.5k` set large with a small green `+%` delta beside them. The numbers are the hero; the delta is muted and small. (Again: real grotesque + `tabular-nums`, the green is a semantic state, not branding.)
- **Elevation is layered, not glowy by default.** Linear floats a secondary agent card *above* the frame with its own soft shadow and a close affordance — depth communicates "this is on top of that," it isn't a uniform drop-shadow on every panel.

### The generic version to AVOID

- The **single dark panel with a full 1px `border border-white/10` box** and `rounded-xl`, one soft `shadow-2xl`, floating in the center. One surface, one border, one shadow — the AI-default frame.
- **Monospace everywhere** for the issue key, counts, table cells, timestamps, and metric numbers as a "technical" flavor. Banned. It's dated and it's the tell.
- A **violet/indigo accent on everything** — active nav row, every status pill, the metric, the button — instead of rationing it to one dot.
- **Uniform medium density**: every row the same height, same `px-4 py-3`, one weight of text, equal-contrast labels — no signal hierarchy, so nothing reads as "the app is mid-task."

### Variety levers (turn these so two builds don't match)

- **Light vs dark frame.** Attio-white (hairline dividers, lots of air) vs Linear-near-black (layered panes, inset highlight). Pick per Design DNA, not by reflex-dark.
- **Border strategy.** (a) *No borders* — separate by surface lightness + spacing; (b) *dividers only* — 1px lines between rows/tabs, no outer box; (c) *inset top highlight* — the window-edge trick. Avoid the full outlined box.
- **Pane count & framing.** Single content pane / 2-pane (nav + content) / 3-pane (nav + list + detail rail). More panes = more "real app," less marketing.
- **Density.** Comfortable (≥44px rows, Attio-ish) vs compact (28-32px rows, Linear-ish). Compact reads as a power tool; comfortable as a consumer app.
- **Accent rationing & elevation.** One accent dot vs a tinted-fill active state; flat panes vs one floating overlay card with its own shadow vs Basedash glow on data viz only.

### Copy-pasteable sketch (Linear-flavored 3-pane, no decorative mono)

```html
<!-- tinted near-black frame; surfaces differ by lightness, no full box border -->
<div class="overflow-hidden rounded-xl bg-[#0F1011] text-zinc-300
            shadow-[inset_0_1px_0_rgba(255,255,255,0.05),0_24px_60px_-20px_rgba(0,0,0,0.7)]">
  <div class="grid grid-cols-[208px_1fr_220px]">

    <!-- SIDEBAR — small low-contrast labels, one tinted active row, no accent on nav -->
    <aside class="border-r border-white/[0.06] bg-[#0B0C0D] p-2 text-[13px]">
      <div class="flex items-center gap-2 px-2 py-1.5 font-medium text-zinc-100">
        <span class="size-4 rounded bg-zinc-700"></span> Kinetic
      </div>
      <nav class="mt-2 space-y-0.5">
        <a class="flex items-center justify-between rounded-md bg-white/[0.06] px-2 py-1.5 text-zinc-100">
          <span>Inbox</span><span class="text-zinc-500 tabular-nums">8</span>
        </a>
        <a class="block rounded-md px-2 py-1.5 text-zinc-400 hover:bg-white/[0.04]">My issues</a>
        <a class="block rounded-md px-2 py-1.5 text-zinc-400 hover:bg-white/[0.04]">Pulse</a>
      </nav>
      <p class="px-2 pt-4 pb-1 text-[11px] uppercase tracking-wide text-zinc-600">Workspace</p>
      <a class="block rounded-md px-2 py-1.5 text-zinc-400 hover:bg-white/[0.04]">Initiatives</a>
      <a class="block rounded-md px-2 py-1.5 text-zinc-400 hover:bg-white/[0.04]">Projects</a>
    </aside>

    <!-- LIST — breadcrumb chrome with tabular counts; dividers, not boxes -->
    <section class="min-w-0">
      <header class="flex items-center justify-between border-b border-white/[0.06] px-4 py-2.5
                     text-[13px] text-zinc-400">
        <span class="font-medium text-zinc-200">Faster app launch</span>
        <span class="tabular-nums text-zinc-500">02 / 145</span>
      </header>
      <ul class="divide-y divide-white/[0.04] text-[13px]">
        <li class="flex items-center gap-3 px-4 py-2 hover:bg-white/[0.03]">
          <span class="size-1.5 rounded-full bg-amber-400"></span>
          <span class="text-zinc-200">Render UI before vehicle_state sync</span>
          <span class="ml-auto tabular-nums text-zinc-500">ENG-2703</span>
        </li>
        <li class="flex items-center gap-3 px-4 py-2 hover:bg-white/[0.03]">
          <span class="size-1.5 rounded-full bg-emerald-400"></span>
          <span class="text-zinc-300">Cache root AGENTS file</span>
          <span class="ml-auto tabular-nums text-zinc-500">ENG-2698</span>
        </li>
        <li class="flex items-center gap-3 px-4 py-2 hover:bg-white/[0.03]">
          <span class="size-1.5 rounded-full bg-zinc-600"></span>
          <span class="text-zinc-400">Triage stale iOS startup spinner</span>
          <span class="ml-auto tabular-nums text-zinc-500">ENG-2690</span>
        </li>
      </ul>
    </section>

    <!-- DETAIL RAIL — properties as quiet label/value pairs; accent is one status dot -->
    <aside class="border-l border-white/[0.06] bg-[#0B0C0D] p-4 text-[13px]">
      <p class="text-[11px] uppercase tracking-wide text-zinc-600">Status</p>
      <p class="mt-1 flex items-center gap-2 text-zinc-200">
        <span class="size-2 rounded-full bg-indigo-400"></span> In Progress
      </p>
      <p class="mt-4 text-[11px] uppercase tracking-wide text-zinc-600">Priority</p>
      <p class="mt-1 text-zinc-300">High</p>
      <p class="mt-4 text-[11px] uppercase tracking-wide text-zinc-600">Assignee</p>
      <p class="mt-1 flex items-center gap-2 text-zinc-300">
        <span class="size-5 rounded-full bg-zinc-700"></span> jori
      </p>
      <div class="mt-5 border-t border-white/[0.06] pt-3 text-zinc-500">
        Updated <span class="tabular-nums text-zinc-400">2 min</span> ago
      </div>
    </aside>
  </div>
</div>
```

Note the craft moves: three surfaces at different lightness (`#0F1011`, `#0B0C0D`) instead of one box; an **inset top highlight** as the only "frame edge"; counts, issue keys and timestamps in the body grotesque with `tabular-nums` (zero mono); active nav as a **tinted fill**, not an accent color; and the indigo rationed to a **single status dot** in the rail. Swap to a white frame with hairline dividers (Attio) or a glow + big-figure metric grid (Basedash) when the Design DNA calls for it — same architecture, different dials.

---

## Data tables, ledgers & lists

A table is the single most "default-able" component in product UI — which is exactly why a generic one screams AI. The fix is not more chrome; it's *less*, applied with intent. Real product tables are quiet grids that let the data carry the visual weight.

### What real top sites actually do

- **Attio drops the outer box entirely.** There's no `border` around the table — separation comes from a stack of faint horizontal hairlines (`~1px` at roughly `4–6%` ink) between rows and *nothing* on the left/right edges. The table reads as part of the page, not a card sitting on it. Header row is the same width as body rows, set off only by a slightly stronger bottom rule, never a filled grey background bar.
- **Rows are short and the type is small.** Attio runs body cells at ~13–14px with row heights around 36–40px; the primary cell (record name) is the only one with an icon/avatar, and it's `font-weight: 500`, while every other cell is `400`. Density is the aesthetic — you should see 10+ rows without scrolling.
- **Outerbase (dark, spreadsheet-style) earns its grid lines.** Because it's a true data grid, it *does* show both vertical and horizontal hairlines — but at very low contrast against a *tinted* dark surface (`~#16181d`, never `#000`). It pairs that with a leading checkbox column, sortable headers with a small chevron that only appears on hover/active, and an `Add row` affordance pinned to the toolbar. Numbers (`open / high / low`) are right-aligned and tabular.
- **Hover is a tint, not a border.** Across all of them the row hover state is a barely-there background wash (a 4–8% lift of the surface or accent), never a colored outline and never a shadow. Selection is a slightly stronger tint of the *same* hue plus a `2px` accent bar on the leading edge (Outerbase-style), not a checkbox-only signal.
- **Numbers are a column citizen, not a code block.** Financial/metric columns are right-aligned, use `font-variant-numeric: tabular-nums` on the *body grotesque*, often with a muted unit/currency glyph in a lighter weight. No monospace, ever — the alignment comes from tabular figures, not from a typewriter face.
- **Status is a quiet dot or low-saturation pill.** The current trend (Linear, Geist, Attio) leans toward a small `6px` filled dot + label rather than a loud filled badge. When a pill is used it's *soft*: tinted background at ~12% of the hue with text at full saturation, `border-radius` modest (6–8px), no border. One accent color total per table — restraint.
- **The header is whisper-quiet.** Column labels are `12–13px`, often `font-weight: 500`, frequently set in the muted foreground (not full ink), occasionally `letter-spacing` a hair — but **not** uppercase-tracked-out, which now reads dated.

### The generic version to AVOID

- A fully boxed table: `border border-white/10 rounded-xl` wrapping everything, with a filled `bg-white/5` header bar and `divide-y divide-white/10` between every row — the "dark panel with a hairline cage."
- A monospace font on every number, ID, timestamp, or code-like value "to look technical." Banned. Use tabular-nums on the body font instead.
- A loud status pill in the rightmost column (`bg-green-500/20 text-green-400 border border-green-500/30 rounded-full`) on *every* row, turning the table into a Christmas-light strip.
- Identical padding everywhere (`px-4 py-3`) with a soft drop-shadow under the card — flat, uniform, and instantly recognizable as a template.

### Variety levers (turn these so two builds don't match)

1. **Border strategy** — borderless-with-hairlines (Attio), full faint grid (Outerbase data grid), or shadow-as-divider where rows sit on subtly alternating surface tints and the only line is under the header. Pick *one* per build.
2. **Density** — comfortable (44–48px rows, used for a short ledger) vs. compact (32–36px, used when the point is to show volume). Set row height and font size together, don't mix.
3. **Surface temperature & elevation** — flat-on-page (no card) vs. inset panel (table sits in a recessed well, `bg` one step *darker* than the page, top inset highlight) vs. raised card. Inset wells feel current; raised cards feel 2021.
4. **Accent role** — accent on the selection bar, OR on a single sparkline/trend cell, OR on one status hue — never all three. Decide the *one* place color is allowed.
5. **Framing of the leading column** — icon+name (CRM/list feel), checkbox+id (data-grid feel), or rank-number (leaderboard/ledger feel). This single choice changes the whole personality.

### Copy-pasteable sketch (borderless hairline ledger, dark, tabular numbers, no mono)

```html
<!-- Tinted neutral surface, no outer box; hairlines + hover-tint do the work -->
<div class="w-full max-w-3xl bg-[#15161a] text-zinc-200
            [font-feature-settings:'cv01','ss01'] antialiased">

  <!-- Toolbar: quiet, single accent only on the active filter -->
  <div class="flex items-center justify-between px-1 pb-3">
    <div class="flex items-center gap-2 text-[13px]">
      <span class="font-medium text-zinc-100">Transactions</span>
      <span class="text-zinc-500">·</span>
      <span class="text-zinc-500">Last 30 days</span>
    </div>
    <button class="rounded-md px-2.5 py-1 text-[13px] text-zinc-400
                   hover:bg-white/5 hover:text-zinc-200 transition-colors">
      Add filter
    </button>
  </div>

  <table class="w-full border-collapse text-[13px]">
    <!-- Header: muted, medium weight, one rule beneath -->
    <thead>
      <tr class="text-left text-zinc-500 [&>th]:font-medium [&>th]:py-2 [&>th]:px-3
                 border-b border-white/[0.07]">
        <th class="w-[42%]">Description</th>
        <th>Account</th>
        <th class="text-right">Status</th>
        <th class="text-right tabular-nums">Amount</th>
      </tr>
    </thead>

    <tbody class="[&>tr]:border-b [&>tr]:border-white/[0.05]">
      <!-- Each row: hover = tint, not border. Primary cell weighted up. -->
      <tr class="group relative hover:bg-white/[0.03] transition-colors">
        <td class="py-2.5 px-3">
          <span class="font-medium text-zinc-100">Stripe payout</span>
          <span class="ml-1.5 text-zinc-500">#PR-4821</span>
        </td>
        <td class="py-2.5 px-3 text-zinc-400">Operating · USD</td>
        <td class="py-2.5 px-3 text-right">
          <span class="inline-flex items-center gap-1.5 text-zinc-300">
            <span class="size-1.5 rounded-full bg-emerald-400"></span>Settled
          </span>
        </td>
        <td class="py-2.5 px-3 text-right tabular-nums text-emerald-300/90">
          +12,480.00
        </td>
      </tr>

      <tr class="group relative hover:bg-white/[0.03] transition-colors">
        <td class="py-2.5 px-3">
          <span class="font-medium text-zinc-100">AWS invoice</span>
          <span class="ml-1.5 text-zinc-500">#PR-4820</span>
        </td>
        <td class="py-2.5 px-3 text-zinc-400">Operating · USD</td>
        <td class="py-2.5 px-3 text-right">
          <span class="inline-flex items-center gap-1.5 text-zinc-300">
            <span class="size-1.5 rounded-full bg-amber-400"></span>Pending
          </span>
        </td>
        <td class="py-2.5 px-3 text-right tabular-nums text-zinc-300">
          −3,902.16
        </td>
      </tr>

      <!-- Selected row: same-hue tint + 2px leading accent bar -->
      <tr class="group relative bg-sky-400/[0.06] hover:bg-sky-400/[0.09]
                 transition-colors">
        <td class="py-2.5 px-3 before:absolute before:inset-y-0 before:left-0
                   before:w-[2px] before:bg-sky-400">
          <span class="font-medium text-zinc-100">Figma seats</span>
          <span class="ml-1.5 text-zinc-500">#PR-4819</span>
        </td>
        <td class="py-2.5 px-3 text-zinc-400">Software · USD</td>
        <td class="py-2.5 px-3 text-right">
          <span class="inline-flex items-center gap-1.5 text-zinc-300">
            <span class="size-1.5 rounded-full bg-zinc-500"></span>Draft
          </span>
        </td>
        <td class="py-2.5 px-3 text-right tabular-nums text-zinc-300">
          −540.00
        </td>
      </tr>
    </tbody>
  </table>

  <!-- Empty/footer note: low-contrast, no border -->
  <p class="px-3 pt-3 text-[12px] text-zinc-500 tabular-nums">
    3 of 128 rows · 8,037.84 net
  </p>
</div>
```

Notes on the sketch: no wrapping box, no `divide-y` cage, no card shadow — the structure is hairlines + a single header rule. Numbers use `tabular-nums` on the body grotesque (no monospace). Color is rationed: status dots are the only hues, gains use a desaturated emerald, and the sole accent (`sky`) appears *only* on the selected row's tint and `2px` edge bar. To make a second, different table, flip one lever — e.g. switch to a 32px-dense data grid *with* faint vertical lines and a leading checkbox column, or invert to a flat light surface — rather than reusing this exact look.

---

## Charts & data-viz (line, bar, funnel, cohort, sparkline)

Charts are where AI-default UI gives itself away fastest: a boxed canvas, four gridlines, a full x/y axis, a glowing accent line, and a tooltip nobody styled. Real product teams treat a chart as *typography with one shape in it* — the number is the hero, the line is supporting, the gridlines are nearly gone. Study how differently the references solve the same job: Mixpanel's funnel is all soft lilac bars + stacked percentages with no frame; Steep's "Activation" spark is a single thin charcoal line with one end-dot and a giant `46.2%` underneath; Graphy goes the opposite way with glossy rounded 3D bars; PostHog stays flat and utilitarian. None of them look like the same template.

### What real top sites actually do

- **The number leads, the chart supports.** Steep's activation card puts a large `46.2%` figure directly *under* a tiny sparkline — the viz exists to give the number a shape, not the reverse. KPI cards pair one big tabular figure with a small signed delta (`↑ 5.5% vs last week`), where the delta is the only colored element on the card.
- **Kill the axes and the box.** Sparklines and hero charts ship with *no* y-axis, no chart border, and often no x-axis labels — just the line and maybe a faint baseline. Steep's chart fragment has zero gridlines. When an axis is needed, it's 1px at ~8–10% ink, sitting *under* the plot, never a full rectangle around it.
- **Gridlines are the quietest layer or absent.** If present, horizontal-only, 1px, dashed or solid at roughly `border` opacity (6–10% ink), and never vertical. The data line is full-strength; the grid is barely perceptible. Hierarchy = line ≫ axis ≫ grid.
- **Area fill is a fade, not a flood.** Line charts use a vertical gradient under the curve from ~14% accent at the top to 0% at the baseline (Tremor/shadcn do exactly this). The stroke is 1.5–2px; the fill is a whisper. No solid accent block.
- **Funnels are stacked bars + stacked percentages, no scaffolding.** Mixpanel's funnel is horizontal stepped bars in soft lilac with each step's conversion `82.4% → 61.8% → 41.6%` set directly beneath, an `Overall` total, and faint dotted drop-off connectors between steps — sitting on white with a soft shadow, not inside a charted grid.
- **Cohort/retention = a tinted heatmap, not a table of digits.** Each cell's *background* carries the value (saturation of the accent encodes magnitude), so the eye reads the gradient before any number. Numbers are small, tabular, and centered; the color does the work.
- **One accent, restrained; categories via neutral steps.** A single line or bar gets the brand accent. Multi-series charts step through *tints of one hue* or a muted neutral ramp — not a rainbow. Steep's coral, Mixpanel's lilac: one family.
- **Sparklines round their caps and mark the endpoint.** A `stroke-linecap="round"`, a single filled dot on the last point (Steep), and the whole thing word-sized — it lives inside a card or beside a number, never framed.

### The generic version to AVOID

- A `<div>` with a 1px hairline border, a soft shadow, a 4-line dashed grid, a full x **and** y axis, and a glowing indigo line at full saturation — the "every dashboard" chart.
- Numbers and axis ticks set in monospace for a "data" feel. **Banned** — use the grotesque body with `tabular-nums`.
- A solid accent area fill (flat block of color) under the line, plus a status pill floating in the corner because the panel felt empty.
- Rainbow multi-series (indigo/green/orange/red) where each series fights for attention; legend dots in a row that nobody needs.

### Variety levers (turn these so two builds differ)

- **Number/chart ratio** — KPI-led (giant figure, sparkline as garnish, Steep) ↔ chart-led (the plot fills the card, number is a caption). Pick one per surface.
- **Grid & axis strategy** — none (pure sparkline) ↔ baseline-only ↔ faint horizontal grid ↔ labeled axis. Going lighter reads more premium; going fuller reads more "analyst tool" (PostHog).
- **Fill & stroke** — flat 1px line / no fill ↔ 2px line + gradient fade ↔ glossy rounded bars with soft glow (Graphy). This single dial swings utilitarian↔expressive.
- **Encoding for categories** — single accent + neutral ramp ↔ monochrome tints of the brand hue ↔ heatmap-tinted cells (cohort). Never default to a categorical rainbow.
- **Framing** — borderless on tinted surface ↔ inset 1px *top* border only (Linear-style, divider not box) ↔ floating card with soft shadow (Mixpanel). The container says as much as the chart.

### Copy-pasteable sketch — KPI line card with gradient fade + cohort heatmap

```html
<!-- Tinted neutral surface, no hard box. Number leads; chart supports. -->
<div class="flex flex-wrap gap-4 bg-[#FAF9F7] p-6 font-sans text-[#1C1B1A]
            [font-feature-settings:'tnum'] [&_*]:[font-feature-settings:'tnum']">

  <!-- KPI + line: figure is the hero, chart is the shape under it -->
  <div class="w-72 rounded-xl bg-white p-5 ring-1 ring-black/[0.06] shadow-[0_1px_2px_rgba(0,0,0,0.04)]">
    <div class="flex items-center justify-between">
      <span class="text-[13px] font-medium text-[#6B6864]">Activation rate</span>
      <span class="inline-flex items-center gap-1 text-[12px] font-medium text-[#2E7D5B]">
        <svg width="9" height="9" viewBox="0 0 10 10" aria-hidden="true"><path d="M5 1.5 8.5 7H1.5L5 1.5Z" fill="currentColor"/></svg>
        5.5%
      </span>
    </div>
    <div class="mt-1.5 text-[34px] font-semibold tracking-tight tabular-nums leading-none">46.2%</div>
    <div class="mt-0.5 text-[12px] text-[#9A9691] tabular-nums">vs 40.7% last week</div>

    <!-- No axes, no box. 1.5px stroke, gradient fade to baseline, endpoint dot. -->
    <svg viewBox="0 0 240 64" class="mt-4 w-full" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%"  stop-color="#E07856" stop-opacity="0.16"/>
          <stop offset="100%" stop-color="#E07856" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <line x1="0" y1="63" x2="240" y2="63" stroke="#1C1B1A" stroke-opacity="0.06"/>
      <path d="M0 50 L40 46 L80 48 L120 36 L160 30 L200 22 L232 14 L232 64 L0 64 Z" fill="url(#fade)"/>
      <path d="M0 50 L40 46 L80 48 L120 36 L160 30 L200 22 L232 14"
            fill="none" stroke="#E07856" stroke-width="1.75"
            stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="232" cy="14" r="3" fill="#E07856"/>
    </svg>
  </div>

  <!-- Cohort retention: color encodes value, numbers stay small + tabular -->
  <div class="rounded-xl bg-white p-5 ring-1 ring-black/[0.06]">
    <span class="text-[13px] font-medium text-[#6B6864]">Weekly retention by cohort</span>
    <table class="mt-3 border-separate border-spacing-1 text-[11px] tabular-nums">
      <thead class="text-[#9A9691]">
        <tr><th class="pr-3 text-left font-medium">Cohort</th>
          <th class="font-medium">W0</th><th class="font-medium">W1</th>
          <th class="font-medium">W2</th><th class="font-medium">W3</th><th class="font-medium">W4</th></tr>
      </thead>
      <tbody>
        <!-- bg saturation = magnitude; one hue family, not a rainbow -->
        <tr>
          <td class="pr-3 text-left text-[#6B6864] font-medium">May 26</td>
          <td class="w-11 rounded bg-[#E07856]/95 py-1.5 text-center text-white">100</td>
          <td class="rounded bg-[#E07856]/55 py-1.5 text-center text-[#5A2E1E]">58</td>
          <td class="rounded bg-[#E07856]/35 py-1.5 text-center text-[#5A2E1E]">41</td>
          <td class="rounded bg-[#E07856]/22 py-1.5 text-center text-[#5A2E1E]">33</td>
          <td class="rounded bg-[#E07856]/14 py-1.5 text-center text-[#6B6864]">29</td>
        </tr>
        <tr>
          <td class="pr-3 text-left text-[#6B6864] font-medium">Jun 02</td>
          <td class="rounded bg-[#E07856]/95 py-1.5 text-center text-white">100</td>
          <td class="rounded bg-[#E07856]/48 py-1.5 text-center text-[#5A2E1E]">52</td>
          <td class="rounded bg-[#E07856]/30 py-1.5 text-center text-[#5A2E1E]">38</td>
          <td class="rounded bg-[#E07856]/18 py-1.5 text-center text-[#6B6864]">31</td>
          <td class="rounded bg-black/[0.03] py-1.5 text-center text-[#C2BDB7]">—</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

The whole card has one accent (`#E07856`), tabular figures everywhere via `font-feature-settings:'tnum'`, no chart border, no gridlines beyond a 6%-ink baseline, a fade fill instead of a flood, and a cohort grid where *color* — not the digits — carries the trend. To re-skin: drop the area fill and go flat 1px for a utilitarian PostHog read, add an inset top-border-only container for a Linear read, or round the bars and add a soft glow for a Graphy read.

---

## Cards — pricing, stat, feature, product

Cards are where the "AI-default panel" is most visible: a box, a border, a pill, a soft shadow, repeat. Real top teams almost never ship that. They pick *one* surface strategy per page and commit to it, then carry signal in spacing, weight, and number formatting — not in chrome.

### What real top sites actually do

- **Linear: the card is a "window," not a "box."** On the near-black canvas (`#08090A`, never `#000`) the product panels read as one continuous surface separated by a single **1px hairline at `rgba(255,255,255,0.06–0.08)`**, often as an *inset top-border or divider* rather than a full 4-sided box. Elevation is a faint top-edge highlight (`inset 0 1px 0 rgba(255,255,255,.04)`), not a drop shadow. The indigo accent appears only as a 6–8px **status dot**, never as a card fill or border.
- **Stripe: light, editorial, almost border-less.** Feature/stat cards sit on white with **no visible border** — separation comes from generous whitespace and a near-black headline (`#0A2540`) over a muted slate body (`#425466`). When a surface is needed it's a barely-tinted `#F6F9FC` fill with radius ~`8px`, not a stroke. Hierarchy inside a long card is done by *two-tone ink* (dark promise line, slate support line), exactly like their H1.
- **Vercel / Geist: structural minimalism.** Cards are white-on-white (or `#FAFAFA` raised) with a single **`1px` `#EAEAEA` border** and tight radius (`6–8px`). The defining move is *the grid itself* — cards align to visible faint gridlines and corner ticks, so the layout reads engineered. Numbers and labels are the **grotesque body with `tabular-nums`**, never a code face. CTAs inside cards are solid-black or hairline-outline pills, high contrast, small.
- **Raycast: dark cards that earn their elevation.** Surfaces are a hair lighter than the page (`#0F0F12` on `#0A0A0C`), separation by **tonal step, not stroke**. A single brand accent (their red) is rationed to one element per card — an icon tile or a hover glow — and the rest stays neutral. Corner radius is generous (`12–16px`) to feel app-like.
- **Pricing specifically:** the recommended tier is distinguished by **one** lever, not three. Linear/Stripe-class pricing promotes a tier with a subtle tint or a slightly stronger border — *not* border + shadow + glow + scale-up + ribbon all at once. The price is set big in the grotesque with `tabular-nums` and a baseline-aligned `/mo` in muted ink; feature checks are quiet (a thin check glyph in accent-or-muted, never a filled green circle).
- **Number craft everywhere:** every figure uses `font-variant-numeric: tabular-nums` so columns and stacked prices align. Currency, decimals, and units are de-emphasized (muted color, smaller size) so the magnitude reads first. No monospace — the grotesque carries the data.

### The generic version to AVOID

- The **"dark panel kit"**: `bg-neutral-900 + rounded-2xl + border border-white/10 + shadow-lg`, applied identically to every card type on the page.
- A **status pill on everything** (filled rounded-full chip with dot) used as decoration rather than to convey real state.
- **Monospace for the number/price/label** to look "technical" — banned. It reads dated and AI-default.
- **Stacked elevation cues**: border *and* shadow *and* glow *and* a tint, so nothing is actually emphasized and every card shouts equally.

### Variety levers (turn these so two builds don't match)

1. **Surface strategy — pick ONE per page:** (a) hairline-stroke (Vercel/Linear), (b) tonal-step / no border (Raycast), or (c) borderless-on-whitespace (Stripe). Never mix all three.
2. **Separation medium:** 1px inset border vs. a single divider line vs. pure spacing vs. a one-step background tint. Changing this alone re-skins the whole grid.
3. **Density:** editorial (28–32px padding, lots of air, Stripe) vs. compact (16–20px padding, dense, Linear product UI). Set it once and hold it.
4. **Accent rationing:** accent as a 6px status dot · as a single icon tile · as the recommended-tier tint · as a hover-only glow. Use exactly one mode.
5. **Radius + elevation pairing:** tight `6–8px` flat (engineered) vs. generous `12–16px` with a faint top highlight (app-like). Radius and elevation should agree.

### Copy-pasteable sketch — pricing trio, hairline surface, accent as restraint

Tinted-neutral dark surface, separation by 1px inset border + one-step tonal tint on the recommended tier, accent (teal) rationed to the dot, the check glyph, and the active button. All figures use `tabular-nums`. No mono anywhere.

```html
<!-- tokens: bg #0B0C0E · raised #111316 · line rgba(255,255,255,.08) · ink #ECEDEE · muted #9A9DA3 · accent #2DD4BF -->
<section class="bg-[#0B0C0E] px-6 py-20 font-sans text-[#ECEDEE] [font-variant-numeric:tabular-nums]">
  <div class="mx-auto grid max-w-5xl gap-px overflow-hidden rounded-2xl border border-white/[.08] bg-white/[.08] sm:grid-cols-3">

    <!-- Tier -->
    <div class="bg-[#0B0C0E] p-7">
      <p class="text-[13px] font-medium tracking-tight text-[#9A9DA3]">Starter</p>
      <p class="mt-4 flex items-baseline gap-1">
        <span class="text-[40px] font-semibold leading-none tracking-tight">$0</span>
        <span class="text-[13px] text-[#9A9DA3]">/mo</span>
      </p>
      <p class="mt-2 text-[13px] leading-relaxed text-[#9A9DA3]">For solo projects getting off the ground.</p>
      <button class="mt-6 w-full rounded-lg border border-white/[.12] py-2.5 text-[13px] font-medium hover:bg-white/[.04]">Get started</button>
      <ul class="mt-6 space-y-2.5 text-[13px] text-[#C4C6CA]">
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> 1 workspace</li>
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> 5,000 events / mo</li>
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> Community support</li>
      </ul>
    </div>

    <!-- Recommended: distinguished by ONE lever — a faint tint + accent dot -->
    <div class="relative bg-[#111316] p-7">
      <span class="absolute right-6 top-7 flex items-center gap-1.5 text-[11px] font-medium tracking-tight text-[#2DD4BF]">
        <span class="size-1.5 rounded-full bg-[#2DD4BF]"></span>Popular
      </span>
      <p class="text-[13px] font-medium tracking-tight text-[#9A9DA3]">Team</p>
      <p class="mt-4 flex items-baseline gap-1">
        <span class="text-[40px] font-semibold leading-none tracking-tight">$24</span>
        <span class="text-[13px] text-[#9A9DA3]">/mo</span>
      </p>
      <p class="mt-2 text-[13px] leading-relaxed text-[#9A9DA3]">For teams shipping to production.</p>
      <button class="mt-6 w-full rounded-lg bg-[#ECEDEE] py-2.5 text-[13px] font-semibold text-[#0B0C0E] hover:bg-white">Start free trial</button>
      <ul class="mt-6 space-y-2.5 text-[13px] text-[#C4C6CA]">
        <li class="flex gap-2"><span class="text-[#2DD4BF]">✓</span> Unlimited workspaces</li>
        <li class="flex gap-2"><span class="text-[#2DD4BF]">✓</span> 250,000 events / mo</li>
        <li class="flex gap-2"><span class="text-[#2DD4BF]">✓</span> Roles & audit log</li>
      </ul>
    </div>

    <!-- Tier -->
    <div class="bg-[#0B0C0E] p-7">
      <p class="text-[13px] font-medium tracking-tight text-[#9A9DA3]">Scale</p>
      <p class="mt-4 flex items-baseline gap-1">
        <span class="text-[40px] font-semibold leading-none tracking-tight">$96</span>
        <span class="text-[13px] text-[#9A9DA3]">/mo</span>
      </p>
      <p class="mt-2 text-[13px] leading-relaxed text-[#9A9DA3]">Volume pricing & committed throughput.</p>
      <button class="mt-6 w-full rounded-lg border border-white/[.12] py-2.5 text-[13px] font-medium hover:bg-white/[.04]">Contact sales</button>
      <ul class="mt-6 space-y-2.5 text-[13px] text-[#C4C6CA]">
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> Everything in Team</li>
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> 5M+ events / mo</li>
        <li class="flex gap-2"><span class="text-[#6B6E74]">✓</span> SSO & SLA</li>
      </ul>
    </div>

  </div>
</section>
```

Why it doesn't read AI-default: separation is a single `gap-px` over a tinted line layer (one hairline system, no per-card boxes), the recommended tier is promoted by **one** lever (a one-step background tint plus the accent dot — no shadow/glow/scale stack), the accent is rationed to three precise spots, and every figure is the grotesque with `tabular-nums` so `$0 / $24 / $96` align optically. To re-skin for a different build, flip the surface strategy (swap the `gap-px` line layer for borderless-on-whitespace, or for a tonal-step with no border) and the density (drop padding to `p-5`) — same markup, a visibly different card system.

---

## Activity feeds, logs, streams & timelines

This component is a vertical list of events over time: an activity feed, an audit log, a deploy stream, a comment thread, a reasoning trace. The failure mode is treating every event as a fully-bordered card. Real tools treat the feed as a *quiet column of text* and spend their whole detail budget on the left edge (icon/dot/rail) and on time formatting.

### What real top sites actually do

- **The row is not a box — it hangs off a left column.** Sentry's "Root Cause" reasoning trace gives each step a small leading glyph in a fixed icon gutter and then just runs the text; there is no per-row border, no per-row card, no shadow. Liveblocks' comment feed does the same with an avatar gutter. The list reads as one surface, not fifteen stacked panels. Separation comes from line-height and the icon column, not from 15 hairline boxes.
- **Timestamps are de-emphasized and usually relative.** Liveblocks shows `now` and `5m ago` in muted gray at the same size as metadata, never bold, never colored. Use relative time for recent events (`now`, `2m`, `1h`) and reserve absolute timestamps (`14:02:31`) for true logs — and when you do show a clock time, set it in the body grotesque with `tabular-nums`, muted, so the column stays vertically aligned without shouting.
- **Level/severity is a tiny color token, not a big pill.** Better Stack's log table marks level with a small colored dot or a single muted-color word (`ERROR` in a desaturated red), inline, ~11–12px. It does not wrap every line in a filled status badge. Color is the *only* loud thing and it's 6px wide. Datadog likewise uses color purely as data encoding (red/orange/green KPIs), never as decoration.
- **Density is real and intentional.** Better Stack's log view packs rows at ~28–32px height with ~13px text and tight tracking — dozens of lines visible at once. A log that breathes like a marketing card is wrong. Tighten `leading`, drop vertical padding to `py-1.5`/`py-2`, and let the volume of rows be the texture.
- **A connector implies sequence; a glyph implies type.** Sentry runs faint horizontal lead-lines off each reasoning step (and a vertical spine would do the same job for a timeline). For a *timeline*, draw one continuous 1px vertical rail behind the icon gutter and let dots sit on it — the line is the structure, so individual rows need no borders at all.
- **Surfaces are tinted, accent is rationed.** Sentry's panel is a warm dark plum (not `#000`); the active/important step gets the one accent treatment (a brighter link, a filled dot) while every other row stays neutral. One accent per screen, applied to the thing that matters (the error, the current step, the unread item).
- **Numbers and counts use tabular figures in the body face.** Reaction counts, durations (`128ms`), byte sizes, attempt counts — all grotesque + `tabular-nums`, never a monospace face. They align in their column because of the numeric variant, not because of a typewriter font.

### The generic version to AVOID

- Every event wrapped in its own `rounded-xl border border-white/10 bg-zinc-900 p-4 shadow-sm` card, stacked with `gap-4` — fifteen identical floating panels instead of one dense column.
- A filled status **pill** (`rounded-full bg-…/15 px-2 py-0.5`) on every single row for the level/type, so severity screams on lines that are routine.
- Timestamps rendered in a **monospace** face (or as a bold colored chip) to look "technical" — banned. It's the AI-default log tell.
- Uniform medium padding (`p-4`), generous `leading-relaxed`, and a hairline divider between every row — the result breathes like a blog list, not a stream, and only ~6 events fit on screen.

### Variety levers

Turn at least two of these so two feeds don't look like the same template:

- **Structure cue:** icon-gutter list (no rail) · single vertical spine with dots (timeline) · grouped-by-day with sticky date headers · flat dense log table with columns. Pick one per build.
- **Density:** comfortable activity feed (`py-3`, 14px, relative time) vs. forensic log (`py-1.5`, 13px, absolute `tabular-nums` clock, monochrome).
- **Border strategy:** zero per-row borders (separation by rhythm) · a single inset top-border per row (Linear style, `border-t border-white/5`) · alternating row tint (`even:bg-white/[0.02]`) — never full boxes.
- **Severity expression:** 6px leading dot · one muted colored word · a 2px left accent-edge on the row · color the icon only. Don't combine more than one.
- **Time format & framing:** relative (`2m ago`) for social/activity · absolute monotonic clock for logs · duration deltas (`+340ms`) for traces. The choice signals what kind of stream this is.

### Copy-pasteable sketch

A deploy / system activity feed: icon-gutter list, no per-row boxes, a faint spine, one accent on the active item, tinted neutral surface, relative time in muted tabular figures.

```html
<div class="mx-auto max-w-md rounded-xl border border-white/[0.06] bg-[#16151c] p-1.5">
  <div class="flex items-center justify-between px-3 py-2.5">
    <h3 class="text-[13px] font-medium tracking-tight text-zinc-200">Activity</h3>
    <span class="text-[11px] text-zinc-500">Last 24h</span>
  </div>

  <ol class="relative">
    <!-- continuous spine behind the icon gutter -->
    <span class="absolute left-[26px] top-2 bottom-2 w-px bg-white/[0.07]" aria-hidden="true"></span>

    <!-- active / important event: the one accent on screen -->
    <li class="relative flex gap-3 px-3 py-2.5">
      <span class="z-10 mt-0.5 grid size-[18px] shrink-0 place-items-center rounded-full bg-emerald-400/15 ring-2 ring-[#16151c]">
        <span class="size-1.5 rounded-full bg-emerald-400"></span>
      </span>
      <div class="min-w-0 flex-1">
        <p class="text-[13px] leading-snug text-zinc-200">
          Deploy <span class="font-medium text-zinc-50">v2.14.0</span> promoted to production
        </p>
        <p class="mt-0.5 text-[11.5px] text-zinc-500">
          by maya.chen · <span class="tabular-nums">8.4s</span> · <span class="tabular-nums">now</span>
        </p>
      </div>
    </li>

    <!-- error: severity is a tiny colored word, no pill -->
    <li class="relative flex gap-3 px-3 py-2.5">
      <span class="z-10 mt-0.5 grid size-[18px] shrink-0 place-items-center rounded-full bg-white/[0.04] ring-2 ring-[#16151c]">
        <span class="size-1.5 rounded-full bg-rose-400/90"></span>
      </span>
      <div class="min-w-0 flex-1">
        <p class="text-[13px] leading-snug text-zinc-300">
          <span class="font-medium text-rose-300/90">Failed</span> health check on <span class="text-zinc-200">edge-fra-2</span>
        </p>
        <p class="mt-0.5 text-[11.5px] text-zinc-500">
          504 timeout · <span class="tabular-nums">12m ago</span>
        </p>
      </div>
    </li>

    <!-- routine event: fully neutral, no color at all -->
    <li class="relative flex gap-3 px-3 py-2.5">
      <span class="z-10 mt-0.5 grid size-[18px] shrink-0 place-items-center rounded-full bg-white/[0.04] ring-2 ring-[#16151c]">
        <span class="size-1.5 rounded-full bg-zinc-500"></span>
      </span>
      <div class="min-w-0 flex-1">
        <p class="text-[13px] leading-snug text-zinc-300">
          Cache invalidated — <span class="tabular-nums text-zinc-200">3,182</span> keys cleared
        </p>
        <p class="mt-0.5 text-[11.5px] text-zinc-500"><span class="tabular-nums">1h ago</span></p>
      </div>
    </li>
  </ol>
</div>
```

Notes on why this avoids the default: there are no per-row cards or dividers — the **spine** carries structure; severity is a 6px dot plus one muted word, not a filled badge; every figure (`8.4s`, `3,182`, `12m`) is the grotesque body face with `tabular-nums`, no mono anywhere; the surface is warm `#16151c` rather than pure black; and exactly one row earns the accent (the live deploy). To re-roll the look, swap the spine for `even:bg-white/[0.02]` rows, switch relative time to an absolute `tabular-nums` clock, and tighten to `py-1.5` for a forensic log feel.

---

## Navigation — headers, sidebars, tabs

### What real top sites actually do

- **Marketing top-nav is featherweight, not a "bar."** Vercel, Linear, Framer and Stripe all run the logo + 5–6 link items + 1–2 right-side actions at ~13px, medium weight (500), in a muted ink (~70% of body color), with generous letter-spacing-0 and ~24–28px gaps. There is **no visible container** — no border, no fill, no shadow. The nav just floats on the page background. The only chrome is the sign-up pill on the right (white/black pill on Vercel, Linear, Framer; the brand-blue solid on Stripe). Restraint is the look.
- **The pill button is the loudest element, and it's tiny.** On Linear and Framer the primary nav action is a small white pill (~32px tall, ~14–16px horizontal padding, fully rounded), and the *secondary* "Log in" is plain text with no border at all. Vercel ships a black pill + an outlined "Log In" ghost pill. The hierarchy is pill > ghost > plain-text link — never two filled buttons.
- **In-product sidebar nav = dense, flat, tinted rows.** Linear's app sidebar packs rows at ~28–30px row-height, ~13px label, with a 16px leading icon and ~8px icon-to-label gap. There are **no row borders and no dividers** — sections (Workspace, Favorites) are separated by an 11px uppercase, low-contrast gray section label and whitespace alone. The active row is a **subtle tinted fill** (a few % white over the dark canvas, ~6px radius) — not an accent bar, not a colored background. Hover is an even fainter version of the same fill.
- **Header dividers are inset hairlines or shadows, not full boxes.** Linear's in-app top bar separates from content with a single 1px **inset** bottom border in a barely-there tint (`rgba(255,255,255,0.06)`-ish), stopping at the content edges — it reads as a seam, not a frame. Where a divider would feel heavy, top teams swap the 1px line for a **1px translucent shadow** so the edge is felt, not drawn.
- **Tabs are underline-led, low-contrast, tabular counts.** The Linear issue header shows tab/breadcrumb chrome where the active item is full-ink and inactive items drop to ~50% gray; counts like `02 / 145` sit in the body grotesque with `tabular-nums`, never in a pill and never in mono. The active tab marker is a 2px underline the width of the *label* (inset), not a full-width bar.
- **Accent is reserved for state, not navigation.** Linear's indigo never colors a nav item — it only appears on a status dot or an "In Progress" chip inside content. Nav selection is communicated by ink contrast + a neutral tinted fill. Stripe is the exception that proves the rule: its accent is a marketing brand-blue on the CTA only, while the nav links stay near-black.

### The generic version to AVOID

- The **"dark panel + 1px hairline box"** sidebar: every nav region wrapped in `border border-white/10 rounded-xl bg-zinc-900` with a `shadow-lg`. Real sidebars have *no border and no shadow* — they're flat surfaces defined by tint and spacing.
- The **accent-bar active state**: a 3px colored left-border (usually indigo/violet) plus a colored text and a colored background tint, all at once. Top teams pick *one* neutral signal (a faint fill) and let ink contrast do the rest.
- **Pills for everything**: nav counts, tab labels, and section headers all stuffed into bordered status pills. Counts belong inline with `tabular-nums`; sections belong as quiet uppercase labels.
- **Mono UI chrome**: monospace eyebrows, mono nav counts, mono breadcrumb separators "to look like a dev tool." Banned — use the grotesque with `tabular-nums` for any figure.

### Variety levers (so two builds don't look identical)

1. **Border strategy:** (a) no borders at all, selection by tinted fill (Linear); (b) a single inset hairline seam under the header only; (c) shadow-as-divider (1px translucent shadow, zero drawn lines). Pick one — never stack all three.
2. **Density:** comfortable (~36px rows, 14px labels, marketing feel) vs. dense (~28px rows, 13px labels, app feel). Halve or double the row padding and the whole component changes character.
3. **Active-state signal:** tinted fill block · inset 2px underline · full-ink-vs-muted contrast only · leading icon swaps from line to filled. Choose exactly one as primary.
4. **Framing:** floating chrome on page bg (no container) vs. a tinted rail surface (`bg-white/[0.02]`) that's a shade off the canvas with no border. The rail reads more "app," the float reads more "marketing."
5. **Accent discipline:** keep the accent entirely out of nav (neutral selection) — *or* allow it on exactly one element (a single status dot, or the CTA pill), never on link text and the active row both.

### Copy-pasteable sketch (HTML + Tailwind)

```html
<!-- App shell: floating top header (inset hairline seam) + flat tinted sidebar -->
<div class="flex min-h-[520px] bg-[#0B0C0E] text-[#E8E9EB] antialiased
            [font-feature-settings:'ss01'] selection:bg-white/10">

  <!-- Sidebar: no border, no shadow — defined by tint + spacing -->
  <aside class="w-60 shrink-0 px-2.5 py-3 bg-white/[0.015]">
    <!-- workspace switcher -->
    <button class="flex w-full items-center gap-2.5 rounded-md px-2 py-1.5
                   text-[13px] font-medium hover:bg-white/[0.04] transition-colors">
      <span class="grid h-5 w-5 place-items-center rounded bg-white/10 text-[11px] font-semibold">N</span>
      Northwind
      <svg class="ml-auto h-3.5 w-3.5 text-white/40" viewBox="0 0 16 16" fill="none">
        <path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </button>

    <!-- primary nav: active row = faint tinted fill, no accent bar -->
    <nav class="mt-3 space-y-px text-[13px]">
      <a href="#" class="flex items-center gap-2.5 rounded-md px-2 py-1.5
                         bg-white/[0.06] font-medium">
        <span class="h-1.5 w-1.5 rounded-full bg-white/70"></span>
        Inbox
        <span class="ml-auto tabular-nums text-[12px] text-white/45">12</span>
      </a>
      <a href="#" class="flex items-center gap-2.5 rounded-md px-2 py-1.5
                         text-white/65 hover:bg-white/[0.035] hover:text-white/90 transition-colors">
        <span class="h-1.5 w-1.5 rounded-full bg-white/25"></span>
        My Issues
        <span class="ml-auto tabular-nums text-[12px] text-white/40">4</span>
      </a>
      <a href="#" class="flex items-center gap-2.5 rounded-md px-2 py-1.5
                         text-white/65 hover:bg-white/[0.035] hover:text-white/90 transition-colors">
        <span class="h-1.5 w-1.5 rounded-full bg-white/25"></span>
        Reviews
      </a>
    </nav>

    <!-- section: quiet uppercase label, separated by whitespace not a rule -->
    <p class="mt-5 mb-1 px-2 text-[11px] font-medium uppercase tracking-wide text-white/35">Workspace</p>
    <nav class="space-y-px text-[13px]">
      <a href="#" class="flex items-center gap-2.5 rounded-md px-2 py-1.5
                         text-white/65 hover:bg-white/[0.035] hover:text-white/90 transition-colors">Initiatives</a>
      <a href="#" class="flex items-center gap-2.5 rounded-md px-2 py-1.5
                         text-white/65 hover:bg-white/[0.035] hover:text-white/90 transition-colors">Projects</a>
    </nav>
  </aside>

  <!-- Main: header is a seam (inset 1px bottom hairline), then underline tabs -->
  <main class="flex-1">
    <header class="flex items-center gap-3 px-5 h-12
                   border-b border-white/[0.06]">
      <nav class="flex items-center gap-1.5 text-[13px] text-white/50">
        <a href="#" class="hover:text-white/80 transition-colors">Issues</a>
        <span class="text-white/25">/</span>
        <span class="font-medium text-white/90">Faster app launch</span>
      </nav>
      <span class="ml-3 tabular-nums text-[12px] text-white/40">02 / 145</span>

      <!-- right side: one pill, one ghost — never two filled buttons -->
      <div class="ml-auto flex items-center gap-2">
        <button class="rounded-md px-2.5 py-1.5 text-[13px] text-white/65
                       hover:bg-white/[0.05] hover:text-white/90 transition-colors">Filter</button>
        <button class="rounded-md bg-white px-3 py-1.5 text-[13px] font-medium text-[#0B0C0E]
                       hover:bg-white/90 transition-colors">New issue</button>
      </div>
    </header>

    <!-- Tabs: inset 2px underline on active, muted-vs-ink contrast, tabular counts -->
    <div class="flex items-center gap-5 px-5 h-10 border-b border-white/[0.06] text-[13px]">
      <a href="#" class="relative flex items-center gap-1.5 h-full font-medium text-white/90">
        Activity
        <span class="absolute inset-x-0 -bottom-px h-0.5 rounded-full bg-white/90"></span>
      </a>
      <a href="#" class="flex items-center gap-1.5 h-full text-white/50 hover:text-white/80 transition-colors">
        Sub-issues <span class="tabular-nums text-white/35">8</span>
      </a>
      <a href="#" class="flex items-center gap-1.5 h-full text-white/50 hover:text-white/80 transition-colors">
        Links <span class="tabular-nums text-white/35">3</span>
      </a>
    </div>
  </main>
</div>
```

Notes on the sketch: the canvas is a tinted near-black (`#0B0C0E`, not `#000`); the sidebar carries **no border and no shadow** — it's a flat `bg-white/[0.015]` rail with selection shown by a faint tinted fill. The header is a single inset hairline seam, tabs use an inset 2px underline, and every figure (`12`, `02 / 145`, `8`) is the grotesque body with `tabular-nums` — no mono anywhere, no accent on navigation.

---

## Code, terminal & API surfaces

This covers install snippets, terminal blocks, code samples, request/response panels, and API-reference rows — the components that *contain* mono, but must not *be* styled by it.

### What real top sites actually do

- **The snippet is a tinted surface, not a black box.** On `bun.sh` the install block sits on a panel only a few percent lighter than the page (a `#16161a`-ish neutral over a near-black page), radius ~10-12px, with a real chrome bar on top holding **OS tabs** ("Linux & macOS" / "Windows") and a "View install script" link. The code itself is one quiet line; the *frame* carries the structure. Don't lean on a 1px border to define the block — the surface step does it.
- **The command has a prompt glyph, and the glyph is muted.** `bun.sh` writes `$ curl -fSSL https://bun.sh/install | bash` — the `$` is a low-contrast neutral, the command is near-white, and that single contrast step reads as "terminal" far better than any green-on-black skin. The copy icon lives top-right, ghost-styled, only gaining contrast on hover.
- **Accent is a single highlight, never a wash.** `bun.sh`'s benchmark panel colors *only* the "Bun" bar pink; every competitor bar is grey. The active OS tab gets the same pink underline/fill. One element is hot, everything else is neutral — that's how a product surface signals "this is the answer" without shouting.
- **Numbers in code-adjacent UI are body-grotesque with tabular figures, right-aligned.** The benchmark times (`269.1 ms`, `494.9 ms`, `1,608 ms`, `2,137 ms`) and version captions (`v1.3.14`) are NOT mono — they're the same sans as everything else, right-aligned in their column so decimal points stack. The unit (`ms`) is split off in muted weight. This is the rule: data near code still uses the grotesque + `tabular-nums`.
- **Docs/API chrome is hairline-light and lifted by shadow, not boxed.** `readme.com`'s embedded docs window uses faint dividers between the sidebar tree, the toolbar (`Guides · Recipes · API Reference · Changelog`) and the content; the whole window is separated from the dark hero by a **soft drop shadow + radius**, not a heavy outline. The search field shows a `⌘K` hint chip inset on the right.
- **Method/status semantics come from tinted pills, not raw color.** API rows read best with a small uppercase method tag on a *tinted* background that matches its hue family (GET → muted teal/blue tint, POST → muted green tint, DELETE → muted red tint), low saturation, dark text on light tint. The endpoint path is the grotesque, with only the `:id` segments dimmed — never the whole path in mono-as-decoration.
- **Vercel/Geist restraint as the ceiling for elevation.** Vercel keeps these surfaces near-flat and near-monochrome; if you add a glow it's a faint top-edge sheen, not a colored halo. When in doubt, flatter and quieter wins.

### The generic version to AVOID

- The **black box with a red/yellow/green "mac traffic lights"** dot trio in the corner — it's the single most over-used AI default for "this is code." Skip it unless the design genuinely wants an OS-window metaphor; even then, prefer OS *tabs* (bun) over decorative dots.
- **Mono leaking out of the snippet** into the filename label, the line numbers, the "200 OK" status, the copy tooltip, or the benchmark figures. Mono is allowed *only inside the literal code/terminal text*. Everything else is the grotesque.
- **Neon syntax highlighting** (bright magenta keywords, lime strings) on pure `#000`. Real product code blocks use a low-contrast, tinted-neutral token palette — most tokens near the same value, one or two gently differentiated.
- The **1px hairline rectangle + soft shadow + one status pill** treatment applied identically to the snippet, the response panel, and the API row, so all three look like the same empty card.

### Variety levers

Turn at least two of these so two builds don't rhyme:

- **Framing** — bare flush snippet (just a copy button, no chrome) vs. tab-headed panel (OS/language tabs) vs. full docs-window with sidebar. bun and readme sit at opposite ends of this dial.
- **Border strategy** — surface-step only (tint defines the edge), vs. single inset hairline, vs. shadow-lift with no border. Don't combine all three.
- **Prompt & gutter** — `$`-prompt terminal style, vs. line-numbered source gutter, vs. no gutter at all. Pick one identity per block.
- **Accent role** — accent on the active tab, OR on the copy-success state, OR on one highlighted line/bar — not all at once.
- **Density** — a single hero install line (loose, generous padding) vs. a dense multi-row API table (tight 36-40px rows, hairline dividers). Match density to whether the surface is a showpiece or a reference.

### Copy-pasteable sketch

A tab-headed install panel beside a benchmark readout — tinted surface, muted prompt glyph, single-accent highlight, tabular figures in the grotesque (no decorative mono outside the snippet).

```html
<!-- tinted neutrals: page ~#0d0d10, panel ~#17171b, accent a restrained warm amber -->
<div class="grid gap-4 md:grid-cols-2 max-w-3xl font-sans text-stone-200">

  <!-- Install panel -->
  <div class="rounded-xl bg-[#17171b] ring-1 ring-white/5 overflow-hidden">
    <!-- chrome: OS tabs, not traffic lights -->
    <div class="flex items-center gap-1 px-2 pt-2 text-[13px]">
      <button class="rounded-md px-2.5 py-1 font-medium text-stone-100 bg-amber-400/10 ring-1 ring-amber-400/30">Linux & macOS</button>
      <button class="rounded-md px-2.5 py-1 text-stone-400 hover:text-stone-200">Windows</button>
      <a href="#" class="ml-auto px-2 py-1 text-stone-500 hover:text-stone-300">View script</a>
    </div>
    <!-- the ONLY place mono is allowed: the literal command -->
    <div class="flex items-center gap-3 px-3.5 py-3.5">
      <code class="font-mono text-[13px] leading-none text-stone-100">
        <span class="text-stone-500 select-none">$ </span>curl -fsSL https://acme.dev/install | sh
      </code>
      <button aria-label="Copy" class="ml-auto shrink-0 rounded-md p-1.5 text-stone-500 hover:text-stone-200 hover:bg-white/5">
        <svg viewBox="0 0 24 24" class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="1.6">
          <rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>
        </svg>
      </button>
    </div>
  </div>

  <!-- Benchmark readout: figures are grotesque + tabular-nums, NOT mono -->
  <div class="rounded-xl bg-[#17171b] ring-1 ring-white/5 px-4 py-3.5">
    <p class="text-[13px] font-medium text-stone-200">Cold build · 10k modules</p>
    <p class="text-[12px] text-stone-500 mb-3">lower is faster</p>
    <ul class="space-y-2.5 text-[13px] tabular-nums">
      <li class="flex items-center gap-3">
        <span class="w-14 text-stone-300">acme</span>
        <span class="h-1.5 flex-1 rounded-full bg-stone-800">
          <span class="block h-full w-[14%] rounded-full bg-amber-400"></span>
        </span>
        <span class="w-20 text-right text-stone-100">269.1 <span class="text-stone-500">ms</span></span>
      </li>
      <li class="flex items-center gap-3">
        <span class="w-14 text-stone-400">esbuild</span>
        <span class="h-1.5 flex-1 rounded-full bg-stone-800">
          <span class="block h-full w-[31%] rounded-full bg-stone-600"></span>
        </span>
        <span class="w-20 text-right text-stone-300">571.9 <span class="text-stone-500">ms</span></span>
      </li>
      <li class="flex items-center gap-3">
        <span class="w-14 text-stone-400">rspack</span>
        <span class="h-1.5 flex-1 rounded-full bg-stone-800">
          <span class="block h-full w-full rounded-full bg-stone-600"></span>
        </span>
        <span class="w-20 text-right text-stone-300">2,137 <span class="text-stone-500">ms</span></span>
      </li>
    </ul>
  </div>
</div>
```

For an **API-reference row**, reuse the same surface and swap the body: a tinted uppercase method pill (`text-[11px] font-semibold tracking-wide` on `bg-emerald-400/10 text-emerald-300` for POST), the path in the grotesque with `:id` segments in `text-stone-500`, and a right-aligned `tabular-nums` latency/version figure — never the whole row in mono.

---

## Forms, inputs, search & command palettes

Inputs are where AI-default product UI is most obviously fake. Real apps treat the input as a *quiet container that comes alive on focus* and treat the command palette (⌘K) as a first-class surface, not a search box with a magnifying glass. Study the screenshots: Raycast's launcher, Linear's `⌘K` and search-in-panel, Cal.com's stacked auth fields, Clerk's pixel-perfect sign-in card. None of them look like the generic "dark panel + pill + 1px box" the skill currently emits.

### What real top sites actually do

- **The resting input is almost invisible; focus does the work.** Linear and Raycast set a field at rest to a barely-raised surface (`raised` over `surface`, ~6-8% luminance lift) with a *hairline* border — sometimes no border at all, just the fill. The whole expression lives in the **focus state**: border shifts to a lighter neutral or a low-saturation accent and a soft 2-3px ring appears (`ring-2 ring-accent/15`, not a fat glowing 4px halo). At rest, signal off; on focus, signal on.
- **Search ≠ a bordered box with a centered magnifier.** Raycast's launcher and Linear's `⌘K` are *borderless inputs* sitting at the top of a floating panel, with the icon left-aligned and small (14-16px, `muted` not `ink`), placeholder at `faint`, and a `⌘K` / `Esc` keycap pinned to the right. The search field and its results are **one continuous surface separated by an inset divider**, not two stacked cards. The query line owns the top; results flow beneath it inside the same rounded shell.
- **Command-palette rows are dense, iconed, and keyboard-first.** Each row is ~36-40px tall: a 16px leading icon, a label at 13-14px medium, an optional dimmed group/breadcrumb on the right, and a keyboard hint. The *active* row is a full-width tinted fill (`raised`/`accent-tint`) with rounded corners inset ~4px from the panel edge — selection is a filled block, never an underline or a left-border stripe. A small group label ("Recent", "Navigation") in `faint` 11-12px uppercase-ish caption breaks the list — set in the **grotesque body, not mono**.
- **Keycaps are styled chrome, not text.** The `⌘K`, `↵`, `Esc` hints are tiny pill/box badges: ~18px tall, `raised` fill, hairline border, `muted` glyph at 11px, set in the **body grotesque** with `tabular-nums`. They read as physical keys, which is most of the "this is a real tool" signal.
- **Stacked auth forms are tight and label-led (Cal.com / Clerk).** Real sign-in cards use a clear field label above each input (13px medium, `muted`), ~10-12px vertical gap label-to-field, ~14-16px between fields, and full-width inputs with 10-12px internal padding. Cal.com leads with a black "Sign up with Google" button then an outlined "email" path and a quiet `No credit card required` reassurance line — the form is a short, confident column, not a floating glass panel. Clerk's card sits on a plain off-white surface with a single hairline and one soft shadow; the *restraint* is the polish.
- **Accent is rationed to one moment.** Linear's primary action in the panel is a plain white pill; the indigo only appears as a tiny status dot. In a form, spend accent on the *focused field ring* OR the submit button — rarely both. Errors are a desaturated red border + a 12px helper line, not a red-flooded field.
- **Numbers and inline tokens stay in the body face.** When an input shows a value, count, or a `⌘K` hint, it's the grotesque with `font-variant-numeric: tabular-nums`. Linear shows inline pill-tokens (`vehicle_state`) inside body text using a subtle raised chip — *not* a monospace font, just a tinted rounded background.

### The generic version to AVOID

- A pure-`#18181B` box with a uniform 1px `#3F3F46` border, `rounded-lg`, a centered grey magnifier icon, and `placeholder:Search...` — identical to every other field on the page.
- A monospace face on placeholders, keycaps, labels, captions, or any numeric value (the dated "dev-tool" tell). **Mono is banned here** — keycaps and counts go in the grotesque with `tabular-nums`.
- A command palette built as two stacked cards (a search card + a separate results card) with a heavy drop shadow, results as plain left-aligned text, and the selected row marked by a coloured left-border stripe.
- A 4px glowing accent halo on focus (`ring-4 ring-accent`) and an indigo/violet accent doing it.

### Variety levers (turn these so two builds differ)

- **Border strategy:** (a) hairline-on-all-sides at rest, (b) *no* border at rest + fill-only, focus reveals a ring, (c) Linear-style **single inset top-border** or bottom-border underline-field, (d) divider-as-structure (search and results share one shell split by one inset line). Pick one per build; don't always box everything.
- **Density:** roomy auth column (Cal.com, ~44-48px fields, generous label gaps) vs. dense palette (Raycast, 36px rows, 13px text, tight tracking). Set the row height and font size deliberately.
- **Elevation:** flat tinted-surface field (no shadow) vs. one soft layered shadow on the floating palette vs. a faint ambient `accent` glow behind it. Never stack a border *and* a heavy shadow on a resting input.
- **Accent placement:** focused-ring-only / submit-button-only / status-dot-only — choose where the single saturated moment lands.
- **Framing of the palette:** centered-modal overlay with backdrop blur, vs. inline-in-panel (anchored under a toolbar), vs. full-screen launcher (Raycast). Different frame = different page.

### Copy-pasteable sketch — command palette (⌘K)

One floating shell: a borderless query line, an inset divider, dense keyboard-first rows, real keycaps in the body face. No mono, no fat halo, accent only on the active row.

```html
<!-- tokens assumed: surface #18181B · raised #27272A · line #3F3F46 · ink #FAFAFA · muted #A1A1AA · faint #71717A · accent (one sharp non-indigo) -->
<div class="mx-auto w-full max-w-xl overflow-hidden rounded-xl border border-line/70 bg-surface
            shadow-2xl shadow-black/40 ring-1 ring-white/[0.04]">

  <!-- Query line: borderless, icon-left, keycap-right, divider below -->
  <div class="flex items-center gap-3 border-b border-line/60 px-4 py-3">
    <svg viewBox="0 0 24 24" class="h-4 w-4 shrink-0 text-muted" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>
    </svg>
    <input type="text" autofocus placeholder="Search or jump to…"
           class="w-full bg-transparent text-[15px] text-ink placeholder:text-faint focus:outline-none"/>
    <kbd class="rounded-md border border-line/70 bg-raised px-1.5 py-0.5 text-[11px] font-medium text-muted [font-variant-numeric:tabular-nums]">esc</kbd>
  </div>

  <!-- Results: one continuous list inside the same shell -->
  <div class="max-h-80 overflow-y-auto p-1.5">
    <p class="px-2.5 pb-1 pt-2 text-[11px] font-medium tracking-wide text-faint">Recent</p>

    <!-- Active row: full-width tinted fill, inset, rounded — NOT an underline or stripe -->
    <button class="flex w-full items-center gap-3 rounded-lg bg-raised px-2.5 py-2 text-left ring-1 ring-accent/20">
      <span class="grid h-6 w-6 place-items-center rounded-md bg-accent/15 text-accent">
        <svg viewBox="0 0 24 24" class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h18v4H3zM3 10h18v11H3z"/></svg>
      </span>
      <span class="text-[13.5px] font-medium text-ink">Open “Q3 revenue” dashboard</span>
      <span class="ml-auto text-[12px] text-faint">Analytics</span>
      <kbd class="rounded border border-line/60 bg-surface px-1.5 py-0.5 text-[11px] text-muted">↵</kbd>
    </button>

    <button class="mt-0.5 flex w-full items-center gap-3 rounded-lg px-2.5 py-2 text-left hover:bg-raised/60">
      <span class="grid h-6 w-6 place-items-center rounded-md bg-raised text-muted">
        <svg viewBox="0 0 24 24" class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
      </span>
      <span class="text-[13.5px] text-ink">Create new report</span>
      <span class="ml-auto text-[12px] text-faint [font-variant-numeric:tabular-nums]">⌘N</span>
    </button>

    <p class="px-2.5 pb-1 pt-3 text-[11px] font-medium tracking-wide text-faint">Navigation</p>
    <button class="flex w-full items-center gap-3 rounded-lg px-2.5 py-2 text-left hover:bg-raised/60">
      <span class="grid h-6 w-6 place-items-center rounded-md bg-raised text-muted">
        <svg viewBox="0 0 24 24" class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </span>
      <span class="text-[13.5px] text-ink">Go to Team settings</span>
      <span class="ml-auto text-[12px] text-faint">Workspace</span>
    </button>
  </div>

  <!-- Footer hint bar: keycaps in the body face, tabular-nums -->
  <div class="flex items-center justify-between border-t border-line/60 px-3 py-2 text-[11px] text-faint">
    <span class="inline-flex items-center gap-1.5">
      <kbd class="rounded border border-line/60 bg-raised px-1 py-0.5 text-muted">↑</kbd>
      <kbd class="rounded border border-line/60 bg-raised px-1 py-0.5 text-muted">↓</kbd>
      to navigate
    </span>
    <span class="[font-variant-numeric:tabular-nums]">42 results</span>
  </div>
</div>

<!-- Standalone field, for forms — fill at rest, ring on focus, label-led, accent only on the ring -->
<label class="mt-6 block w-full max-w-sm">
  <span class="mb-1.5 block text-[13px] font-medium text-muted">Work email</span>
  <input type="email" placeholder="you@company.com"
         class="w-full rounded-lg border border-line/70 bg-raised px-3 py-2.5 text-[14px] text-ink
                placeholder:text-faint transition
                focus:border-accent/50 focus:outline-none focus:ring-2 focus:ring-accent/15"/>
</label>
```

Sources: [Raycast](https://www.raycast.com/), [Raycast design notes (awesome-design-md)](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/raycast/DESIGN.md), [Linear ⌘K integration](https://linear.app/integrations/raycast)

---

## Badges, pills, status, tags & avatars

These are the smallest objects in product UI, which is exactly why they make or break the "real vs. AI-default" read. The bar is: a status reads in one glance, and the chrome around it nearly disappears.

### What real top sites actually do

- **Linear: status is an icon + plain text, not a boxed pill.** In the sidebar ("In Progress", "High", "jori", "Codex") there is no border, no filled chip, no rounded rectangle. A small colored glyph carries the state (a half-filled ring for "In Progress", a colored bar-icon for priority) and the label is just neutral ~13px text at normal weight. The color budget lives in the *icon*, never in a background. This is the single highest-leverage move: **most "statuses" should not be pills at all.**
- **When it IS a chip, the fill is a tint, not a saturated block.** Real status chips use a low-opacity wash of the accent (roughly 10-15% alpha) with the text in the *full-strength* same hue — green text on a faint green wash, amber on amber. No solid saturated badge with white text unless it's a genuine alert (error/destructive). Solid + white-text is the loud exception, not the default.
- **A leading 6px dot does the work of a whole border.** Linear's "Issue tracking is dead" chip and most "Live / Active / Degraded" indicators prefix the label with a tiny `currentColor` dot. The dot is the only color; the surface and text stay neutral. This reads as quieter and more current than a fully tinted pill.
- **Avatars are rounded squares for orgs/workspaces, circles for people.** Attio's "Basepoint" workspace switcher uses a brand glyph in a ~6px-radius rounded square, not a circle. Circles signal a human; squircles signal an entity/app/team. Mixing them deliberately is a craft tell. Avatar stacks overlap at about `-8px` with a 2px ring in the *page* background color to punch a gap, and a "+4" overflow chip matches the avatar size exactly.
- **Tags are the quietest object on screen.** Attio's labels and Linear's "Performance", "iOS" read as low-contrast text with at most a faint surface — no border, ~12-13px, muted neutral foreground. They sit *behind* the data in the visual hierarchy, never compete with it.
- **Corner radius is small and consistent, not `rounded-full` everywhere.** Status/tag chips sit around 5-7px radius (matching buttons/inputs), so they feel like part of one system. Reserve `rounded-full` for count badges and dot indicators. A pill-shaped everything is a giveaway.
- **Numbers in chips use tabular figures and that's it** — `font-variant-numeric: tabular-nums` on the body grotesque. A "+12", a "3 open", a version count: same typeface as the UI, just tabular. No monospace anywhere.
- **Sentry: severity is encoded by a colored accent edge, not a saturated pill.** The "Root Cause" rows carry state through a small leading icon and a green progress/accent line rather than a chunky badge. Color is a thin signal layered onto an otherwise neutral row.

### The generic version to AVOID

- The default dark `inline-flex items-center gap-1 rounded-full border border-white/10 bg-white/5 px-2.5 py-0.5 text-xs` pill — applied to *every* status, tag, and label identically. This is the AI-default fingerprint.
- A status dot that is *always* `bg-green-500` (or, worse, indigo/violet) regardless of meaning, paired with `text-xs uppercase tracking-wide` — the fake-enterprise look.
- Boxing things that should be borderless: priority, assignee, and category are text + glyph in real apps, not chips with hairline borders and soft shadows.
- `rounded-full` on literally everything, saturated solid fills with white text for non-alert states, and pure `#fff`/`#000` foregrounds.

### Variety levers

Turn at least two of these per build so two screens don't share a fingerprint:

- **Chrome strategy:** borderless icon+text (Linear) vs. tinted-wash chip (10% accent fill, hue-matched text) vs. dot-prefix neutral chip vs. solid only-for-alerts. Pick one as the house style for the screen.
- **Color encoding:** color in the *icon/dot* vs. color in the *fill* vs. color in an *accent edge/underline* (Sentry). Don't mix all three on one screen.
- **Radius rhythm:** small uniform radius (~6px, matches inputs) vs. true `rounded-full` pills — commit, don't blend.
- **Avatar shape language:** circles-for-people vs. squircles-for-entities; flat-colored initials vs. monochrome glyph vs. photo; ring-gap thickness on stacks.
- **Density:** dense inline labels (Attio, ~2px vertical padding, no border) vs. comfortable standalone chips (~4-6px padding). Tie this to the surrounding table/card density.

### Copy-pasteable sketch

A status row using the *borderless icon+text* convention for state/assignee, a *dot-prefix* live chip, a quiet tag, and a people avatar stack with a squircle org avatar. Tinted neutrals, no mono, tabular figures.

```html
<div class="flex items-center gap-4 rounded-lg bg-stone-900/60 px-4 py-3 text-stone-200 ring-1 ring-stone-50/[0.06]">
  <!-- Org avatar: rounded SQUARE for an entity -->
  <div class="grid h-7 w-7 place-items-center rounded-[7px] bg-emerald-400/15 text-[13px] font-semibold text-emerald-300">B</div>

  <div class="min-w-0 flex-1">
    <p class="truncate text-[13px] font-medium text-stone-100">Migrate billing webhooks</p>

    <div class="mt-1 flex items-center gap-3 text-[12px] text-stone-400">
      <!-- Status: icon carries color, label is neutral (Linear) -->
      <span class="inline-flex items-center gap-1.5">
        <svg viewBox="0 0 16 16" class="h-3.5 w-3.5 text-amber-400" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="8" cy="8" r="6"></circle><path d="M8 8V4"></path>
        </svg>
        In progress
      </span>
      <!-- Priority: also borderless icon + text -->
      <span class="inline-flex items-center gap-1.5">
        <span class="flex items-end gap-[1.5px]"><i class="h-1.5 w-[3px] rounded-[1px] bg-stone-500"></i><i class="h-2.5 w-[3px] rounded-[1px] bg-stone-300"></i><i class="h-3.5 w-[3px] rounded-[1px] bg-stone-300"></i></span>
        High
      </span>
      <!-- Quiet tag: text-weight, no border, faint surface -->
      <span class="rounded-[5px] bg-stone-50/[0.04] px-1.5 py-0.5 text-stone-300">billing</span>
    </div>
  </div>

  <!-- Dot-prefix live chip: only the dot is colored -->
  <span class="inline-flex items-center gap-1.5 rounded-[6px] bg-emerald-400/10 px-2 py-1 text-[12px] font-medium text-emerald-300">
    <span class="h-1.5 w-1.5 rounded-full bg-emerald-400"></span>
    Live
  </span>

  <!-- People avatar stack: CIRCLES, ring-gap in page bg, exact-match overflow chip -->
  <div class="flex items-center -space-x-2">
    <div class="grid h-7 w-7 place-items-center rounded-full bg-rose-400/20 text-[12px] font-semibold text-rose-200 ring-2 ring-stone-900">JL</div>
    <div class="grid h-7 w-7 place-items-center rounded-full bg-sky-400/20 text-[12px] font-semibold text-sky-200 ring-2 ring-stone-900">MK</div>
    <div class="grid h-7 w-7 place-items-center rounded-full bg-stone-700 text-[12px] font-medium text-stone-300 ring-2 ring-stone-900 [font-variant-numeric:tabular-nums]">+4</div>
  </div>
</div>
```

Note what is *absent*: no hairline-bordered pill on every element, no saturated solid badges, no `uppercase tracking-wide`, no monospace. Color appears in exactly one register per object (icon, dot, or fill), figures are tabular, and human vs. entity avatars use different shapes — the kind of variation that makes the build read as designed rather than generated.

---

## Browser/app/device chrome, elevation & framing

Framing is where "this is a real product" gets sold or lost. The frame is the proscenium around your UI — get the edge, the lift, and the layering right and the screenshot reads as a captured app; get it wrong and it reads as a `<div>` with a border. The four references solve it four different ways, and none of them is the AI-default box.

### What real top sites actually do

- **Edge is an inset highlight, not a box.** Linear's app mock has no 1px border ringing the whole panel. The top edge is a single ~1px *lighter* line (a top inset highlight, `box-shadow: inset 0 1px 0 rgba(255,255,255,.06)`), which reads as a physical bevel catching light. The bottom and sides dissolve into a large soft shadow. The frame is felt, not outlined.
- **Surfaces separate by lightness steps, not by dividers.** Inside Linear the sidebar, main column, and detail rail are differentiated by 2-4% lightness jumps on a tinted near-black (`#0d0e11` → `#15161a` → `#1a1b20`), not by hairlines. Stacked panels (the floating "Codex" agent card) lift one more step *and* gain their own shadow. Elevation = a brighter surface + a softer/larger shadow, in tandem.
- **Real window chrome, used sparingly.** Cap and Arc/Dia render actual chrome: macOS traffic-light dots (12px circles, ~8px apart, muted red/amber/green — not saturated), a short toolbar row with back/forward chevrons, and a centered, quiet title ("Dia / New Chat", "Cap 2025-05-23 ... .cap"). The title is the grotesque body at ~13px in a muted foreground, never mono. Chrome height is tight (~36-40px).
- **Nested frames signal depth.** Cap is chrome-inside-chrome: an outer app window, then an *inner* preview pane with its own mini controls, then a timeline track. Each inner panel has a smaller radius than its parent (outer ~14px, inner ~10px) and its own subtle shadow — concentric rounding is the tell that you're inside a real composited UI.
- **Generous outer radius, floated on a contrasting page.** Arc and Cap use ~12-14px on the outer frame and let the whole window *float* on the page with a large, low-opacity shadow (`0 24px 60px -24px rgba(0,0,0,.4)`) plus a single hairline. Framer skips chrome entirely — its template cards bleed a screenshot flush to an ~8px rounded edge and separate by gap + shadow, so contrast (light card on black page) does the framing.
- **Accent appears once, on the live thing.** Cap's only color is the blue timeline selection and the play button; everything else is neutral. Arc's accent is the selected-sidebar pill. The frame and chrome stay neutral so the accent marks *what's active*, not the decoration.

### The generic version to AVOID

- The "screenshot frame" = one `rounded-xl border border-white/10` box with a single uniform shadow, every surface inside the same flat color, separated by `border-t border-white/10` hairlines everywhere.
- A fake browser bar with three pure-`#ff5f56`/`#ffbd2e`/`#27c93f` dots and a mono URL in the address field. (Saturated dots + mono = instant AI tell.)
- Mono for the window title, file name, tab labels, or status text in the chrome.
- One elevation level only: everything sits on the same plane, so nothing reads as nested or active — the "soft shadow on a card" look with no layering logic.

### Variety levers

- **Frame type:** real OS window (traffic-light chrome) vs. browser chrome (back/fwd + title) vs. *no chrome* — image bleeding flush to a rounded edge (Framer). Pick one per build; don't always default to the browser bar.
- **Edge strategy:** inset top-highlight + shadow (Linear, borderless) vs. hairline + float shadow (Arc) vs. pure contrast, no border at all (Framer light-on-dark). These look meaningfully different.
- **Elevation model:** flat single plane / layered (2-3 lightness steps, concentric radii, nested shadows) / floated-on-page (one big drop shadow). Layered reads most "real."
- **Radius scale:** tight (8px, dense/technical) vs. generous (14px, consumer/friendly), and whether inner panels step *down* in radius.
- **Density of chrome:** minimal (just a title) vs. full toolbar with icons/controls. Match it to the product — a dev tool earns a denser toolbar than a consumer recorder.

### Copy-pasteable sketch

A floated app window with real-but-quiet macOS chrome, layered surfaces (sidebar steps down, detail panel steps up), inset top-highlight edge, one neutral hairline, accent used only on the active row. No border-box, no mono, tabular figures.

```html
<!-- tinted near-black palette; accent is a single teal, used once -->
<div class="relative mx-auto max-w-3xl rounded-[14px] bg-[#101216] text-[#e7e9ee]
            shadow-[0_28px_70px_-28px_rgba(0,0,0,.6)] ring-1 ring-white/[0.06]
            [box-shadow:inset_0_1px_0_rgba(255,255,255,.06)]">
  <!-- chrome: tight, muted dots, grotesque title (NOT mono) -->
  <div class="flex h-10 items-center gap-3 rounded-t-[14px] bg-white/[0.02] px-4">
    <div class="flex gap-2">
      <span class="size-3 rounded-full bg-[#e0686a]"></span>
      <span class="size-3 rounded-full bg-[#dbb04a]"></span>
      <span class="size-3 rounded-full bg-[#62b163]"></span>
    </div>
    <div class="flex-1 text-center text-[13px] text-white/45">Acme · Pipeline</div>
    <button class="text-white/35 hover:text-white/70 text-sm">⌄</button>
  </div>

  <div class="grid grid-cols-[160px_1fr]">
    <!-- sidebar: surface steps DOWN, active row = tinted pill + accent bar -->
    <nav class="space-y-0.5 bg-[#0c0e11] p-2 text-[13px] text-white/55">
      <a class="relative flex items-center rounded-md bg-white/[0.06] px-2.5 py-1.5 text-white/90">
        <span class="absolute left-0 h-3.5 w-0.5 rounded-full bg-[#3fae9b]"></span>Inbox</a>
      <a class="flex items-center justify-between rounded-md px-2.5 py-1.5 hover:bg-white/[0.04]">
        <span>Deals</span><span class="tabular-nums text-white/35">24</span></a>
      <a class="flex items-center justify-between rounded-md px-2.5 py-1.5 hover:bg-white/[0.04]">
        <span>Forecast</span><span class="tabular-nums text-white/35">8</span></a>
    </nav>

    <!-- main: surface steps UP; rows separated by ONE faint divider, not boxes -->
    <div class="bg-[#13151a] p-4">
      <div class="mb-3 flex items-baseline justify-between">
        <h3 class="text-[15px] font-medium tracking-tight">Open deals</h3>
        <span class="text-[12px] text-white/40">Q2 · <span class="tabular-nums">$1.42M</span></span>
      </div>
      <div class="divide-y divide-white/[0.05] text-[13px]">
        <div class="flex items-center justify-between py-2.5">
          <span class="text-white/85">Northwind renewal</span>
          <span class="tabular-nums text-white/55">$48,000</span></div>
        <div class="flex items-center justify-between py-2.5">
          <span class="text-white/85">Globex expansion</span>
          <span class="tabular-nums text-white/55">$126,500</span></div>
        <div class="flex items-center justify-between py-2.5">
          <span class="text-white/85">Initech pilot</span>
          <span class="tabular-nums text-white/55">$9,200</span></div>
      </div>
    </div>
  </div>
</div>
```

Notes that keep it from going generic: the outer frame has **no full border** — it's a near-invisible `ring` plus an `inset` top-highlight plus a float shadow. The three interior surfaces (`#0c0e11` sidebar, `#101216` chrome, `#13151a` main) are distinct lightness steps on a *tinted* near-black, so depth comes from value, not outlines. The only divider is a single `divide-white/[0.05]` inside the list. Accent (`#3fae9b`) appears exactly once, as the active-row bar. Every figure is `tabular-nums` on the grotesque body — zero mono.
