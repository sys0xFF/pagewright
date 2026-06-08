#!/usr/bin/env python3
"""OPTIONAL: extract a site's REAL design tokens from its live computed styles.

The reference library gives you a *picture* of a site, never its CSS — so when you "copy" it you re-derive
the fonts/colour/spacing/shadows from memory, and memory is the generic prior. This pulls the anchor's
ACTUAL ingredients (font families/sizes/weights/tracking, colour palette, radii, the exact card box-shadow,
button anatomy, container width) so you can build the identity literally instead of guessing.

OFF by default / opt-in (needs a browser). Setup:
    pip install playwright  &&  python -m playwright install chromium
    # (or, on a machine with Edge, it will use the system Edge channel)

Usage:
    python extract_tokens.py https://mercury.com mercury.com
    # writes tokens/<slug>.json and prints it

If Playwright isn't installed it exits non-zero with the install hint — read the tokens off the full-page
capture as carefully as you can instead.
"""
import json
import sys
from pathlib import Path

# The extraction runs in the page via evaluate(); identical logic to _authoring/extract_tokens.js
JS = r"""() => {
  const cs = el => el && getComputedStyle(el);
  const px = v => Math.round(parseFloat(v) || 0);
  const hex = c => { const m = c && c.match(/\d+(\.\d+)?/g); if (!m) return null;
    if (m.length >= 4 && parseFloat(m[3]) === 0) return null;
    const h = n => Math.round(parseFloat(n)).toString(16).padStart(2,'0'); return '#'+h(m[0])+h(m[1])+h(m[2]); };
  const font = el => { const s = cs(el); if (!s) return null; return {
    family: s.fontFamily.split(',')[0].replace(/["']/g,'').trim(), sizePx: px(s.fontSize), weight: s.fontWeight,
    tracking: s.letterSpacing === 'normal' ? '0' : s.letterSpacing,
    leading: s.lineHeight === 'normal' ? 'normal' : (parseFloat(s.lineHeight)/(parseFloat(s.fontSize)||1)).toFixed(2) }; };
  const biggest = () => { let best=null,max=0; for (const el of document.querySelectorAll('h1,h2,[class*="hero" i] *,header *')) {
    if(!el.textContent.trim())continue; const sz=parseFloat(getComputedStyle(el).fontSize)||0;
    if(sz>max && el.getClientRects().length){max=sz;best=el;} } return best; };
  const bg={}, fg={}; for (const el of Array.from(document.querySelectorAll('*')).slice(0,4000)) {
    const r=el.getClientRects(); if(!r.length||r[0].width<4||r[0].height<4)continue; const s=getComputedStyle(el);
    const b=hex(s.backgroundColor); if(b)bg[b]=(bg[b]||0)+r[0].width*r[0].height;
    const f=hex(s.color); if(f&&el.textContent.trim())fg[f]=(fg[f]||0)+1; }
  const top=(o,n)=>Object.entries(o).sort((a,b)=>b[1]-a[1]).slice(0,n).map(e=>e[0]);
  const btn=document.querySelector('a[class*="button" i],button[class*="primary" i],[class*="btn" i],main a[href] button,header a[class]');
  const bs=cs(btn); const link=document.querySelector('main a[href],p a[href]');
  let card=null; for (const el of document.querySelectorAll('div,section,article')) { const s=getComputedStyle(el);
    if(px(s.borderRadius)>=6 && s.boxShadow!=='none' && el.getClientRects()[0]?.width>120){card=el;break;} }
  const cd=cs(card); const h1=biggest(), h2=document.querySelector('h2'), p=document.querySelector('main p,article p,p');
  return {
    fonts:{display:font(h1),subhead:font(h2),body:font(p),button:bs&&font(btn),link:link&&font(link)},
    palette:{backgrounds:top(bg,6),textColors:top(fg,5)},
    button: bs?{bg:hex(bs.backgroundColor),color:hex(bs.color),radiusPx:px(bs.borderRadius),
      padding:px(bs.paddingTop)+'px '+px(bs.paddingLeft)+'px',weight:bs.fontWeight,
      border:bs.borderStyle!=='none'?bs.border:'none',text:(btn.textContent||'').trim().slice(0,24)}:null,
    card: cd?{radiusPx:px(cd.borderRadius),shadow:cd.boxShadow,border:cd.borderStyle!=='none'?px(cd.borderWidth)+'px '+hex(cd.borderColor):'none'}:null,
    radii:[...new Set(Array.from(document.querySelectorAll('a,button,div,section')).map(e=>px(getComputedStyle(e).borderRadius)).filter(r=>r>0&&r<60))].sort((a,b)=>a-b).slice(0,8),
    container:(()=>{for(const el of document.querySelectorAll('main>div,header>div,section>div,[class*="container" i]')){const w=px(getComputedStyle(el).maxWidth);if(w>600&&w<1800)return w+'px';}return null;})(),
  };
}"""


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python extract_tokens.py <url> [slug]", file=sys.stderr)
        return 2
    url = sys.argv[1]
    slug = sys.argv[2] if len(sys.argv) > 2 else url.split("//")[-1].split("/")[0].replace("www.", "")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("! extract_tokens: Playwright not installed (opt-in).\n"
              "  pip install playwright && python -m playwright install chromium\n"
              "  -> fall back: read tokens off the full-page capture as precisely as you can.", file=sys.stderr)
        return 2

    out_dir = Path(__file__).resolve().parent.parent / "references/reference-library/tokens"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        with sync_playwright() as pw:
            for launch in ({"channel": "msedge"}, {}):  # prefer system Edge, fall back to bundled chromium
                try:
                    browser = pw.chromium.launch(headless=True, **launch); break
                except Exception:
                    browser = None
            if not browser:
                print("! extract_tokens: no browser available (run `python -m playwright install chromium`).", file=sys.stderr)
                return 2
            page = browser.new_context(viewport={"width": 1440, "height": 1000}).new_page()
            page.goto(url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(2500)
            tokens = page.evaluate(JS)
            browser.close()
    except Exception as e:  # noqa: BLE001
        print(f"! extract_tokens: failed: {e}", file=sys.stderr)
        return 2

    tokens["_meta"] = {"url": url, "slug": slug}
    dest = out_dir / f"{slug}.json"
    dest.write_text(json.dumps(tokens, indent=2), encoding="utf-8")
    print(f"[ok] wrote {dest}")
    print(json.dumps(tokens, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
