<div align="center">

<img src="assets/banner.jpg" alt="Pagewright" width="100%" />

# Pagewright

**Design-grade landing pages, generated — not templated.**

A skill for [Claude Code](https://claude.com/claude-code) that turns a one-line brief into an original,
modern landing page — static HTML + Tailwind, opens in any browser.
Built to do the one thing AI website tools fail at: *not look generic.*

</div>

---

## Gallery

<table>
<tr>
<td width="33%"><img src="examples/atlas/screenshot.jpg" alt="Atlas" /><br/><sub><b>Atlas</b> — treasury & banking</sub></td>
<td width="33%"><img src="examples/lumira/screenshot.jpg" alt="Lumira" /><br/><sub><b>Lumira</b> — botanical skincare</sub></td>
<td width="33%"><img src="examples/brule/screenshot.jpg" alt="Brûle" /><br/><sub><b>Brûle</b> — hot sauce</sub></td>
</tr>
<tr>
<td><img src="examples/forge/screenshot.jpg" alt="Forge" /><br/><sub><b>Forge</b> — desktop CNC</sub></td>
<td><img src="examples/northwind/screenshot.jpg" alt="Northwind" /><br/><sub><b>Northwind</b> — support analytics</sub></td>
<td><img src="examples/pageboard/screenshot.jpg" alt="Pageboard" /><br/><sub><b>Pageboard</b> — visual CMS</sub></td>
</tr>
<tr>
<td><img src="examples/aegis/screenshot.jpg" alt="Aegis" /><br/><sub><b>Aegis</b> — EDR security</sub></td>
<td><img src="examples/cortex/screenshot.jpg" alt="Cortex" /><br/><sub><b>Cortex</b> — product analytics</sub></td>
<td><img src="examples/relay/screenshot.jpg" alt="Relay" /><br/><sub><b>Relay</b> — webhook delivery</sub></td>
</tr>
</table>

<sub>Each built from a one-line brief. Open any <a href="examples/"><code>examples/&lt;name&gt;/index.html</code></a> in a browser.</sub>

---

## How it dodges the slop

🎯 **Anchors on ONE real page** — routes your niche to a curated library of **267 real sites** (with full-page captures) and copies the *real* structure, not the model's average.

🛠️ **Builds the product in HTML/CSS** — dashboards, tables, charts, code, hand-built like Linear, Stripe and Attio. Physical objects and photography are generated (Gemini) or fetched (Unsplash).

🎨 **Fights convergence** — per-build assignment of page archetype, typeface, colour and micro-grammar so two pages never rhyme.

## Install

```bash
cp -r pagewright ~/.claude/skills/pagewright
```

Then just describe a product:

> Build a landing page for **Atlas**, a treasury & banking platform for startups.

It asks whether to guide the look or just decide, then ships a complete, runnable page.

## License

[MIT](LICENSE) · reference thumbnails belong to their respective owners.
