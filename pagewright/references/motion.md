# Motion vocabulary — the 2025-26 way

Motion is a big part of why real sites feel alive and AI pages feel flat. Current taste is **purposeful
and restrained**: fast spring-eased micro-interactions + scroll-driven reveals that show, don't tell.
Pick **at least a blur-in reveal + one signature motion** per page. Always gate non-essential motion
behind `prefers-reduced-motion`.

**Default toolchain:** native CSS first (scroll-driven animations now ship ~85%), then `Motion`
(motion.dev, MIT, tiny) for richer work, GSAP only for heavy pinned timelines. Don't reflex-load GSAP
for simple reveals, and **never use AOS.js** — the uniform fade-up-everywhere look is a 2019-22 template tell.

Durations: **150-300ms** for UI/hover, **400-700ms** for reveals. Easing: spring / custom
`cubic-bezier` / `linear()` with slight overshoot — not flat `ease-in-out`.

## Blur-in reveal (the 2025 signature — use this instead of a plain fade)

The blur is what separates premium from a generic fade-up. Combine blur + opacity + slight rise.

```css
@media (prefers-reduced-motion: no-preference) {
  [data-reveal]{ opacity:0; filter:blur(12px); transform:translateY(20px);
    transition:opacity .6s ease, filter .6s ease, transform .6s cubic-bezier(.2,.7,.2,1);
    transition-delay:calc(var(--i,0)*80ms); }   /* stagger via --i on each child */
  [data-reveal].is-visible{ opacity:1; filter:blur(0); transform:none; }
}
```
```js
const io=new IntersectionObserver((es)=>es.forEach(e=>{ if(e.isIntersecting){
  e.target.classList.add('is-visible'); io.unobserve(e.target);} }),{threshold:.15});
document.querySelectorAll('[data-reveal]').forEach((el,i)=>{el.style.setProperty('--i',i%8);io.observe(el);});
```

## Native scroll-driven reveal (zero JS, off main thread)

```css
@media (prefers-reduced-motion: no-preference){
  @supports (animation-timeline: view()){
    .reveal{ animation:reveal both; animation-timeline:view(); animation-range:entry 0% cover 35%; }
    @keyframes reveal{ from{opacity:0;filter:blur(10px);transform:translateY(24px)} to{opacity:1;filter:none;transform:none} }
  }
}
```

## Scroll progress bar (one rule, no listeners)
```css
.progress{ position:fixed; top:0; left:0; height:2px; width:100%; transform-origin:left; transform:scaleX(0);
  background:var(--accent); animation:grow linear both; animation-timeline:scroll(root block); }
@keyframes grow{ to{ transform:scaleX(1) } }
```

## CSS-only logo marquee / ticker (no library)
Duplicate the logo set twice inside the track; translate `-50%`; fade the edges; pause on hover.
```html
<div class="marquee"><div class="track"><!--logos x2--></div></div>
```
```css
.marquee{ overflow:hidden; -webkit-mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent); }
.track{ display:flex; gap:3rem; width:max-content; animation:marquee 32s linear infinite; }
.marquee:hover .track{ animation-play-state:paused; }
@keyframes marquee{ to{ transform:translateX(-50%) } }
```

## Magnetic button (premium, subtle — 6-12px max)
```js
document.querySelectorAll('[data-magnetic]').forEach(b=>{
  b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();
    b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.2}px,${(e.clientY-r.top-r.height/2)*.2}px)`;});
  b.addEventListener('mouseleave',()=>b.style.transform='');
  b.style.transition='transform .3s cubic-bezier(.2,.7,.2,1)';
});
```

## Other current devices (use sparingly, one signature max)
- **Sticky / pinned scrollytelling** — `position:sticky; top:0` on a tall section while inner layers swap;
  or GSAP ScrollTrigger `pin:true` + `scrub` for a guided multi-step hero/product demo.
- **Parallax** — `animation-timeline: scroll()` translating background layers at different rates (cheap,
  off-main-thread) instead of JS rAF.
- **Text scramble / decode** — GSAP ScrambleTextPlugin (now free) on a hero word or nav rollover; pair
  with SplitText for char-by-char. One place only.
- **View Transitions** — `@view-transition{ navigation:auto }` (MPA) or `document.startViewTransition()`
  for shared-element morphs (card→detail); degrades gracefully.
- **Hover/tap micro-interactions** — short spring transforms on cards/buttons; tabular-number count-ups
  on stats via IntersectionObserver.

## Don't
- AOS.js or uniform fade-up on everything · linear/ease fades with no blur/stagger/spring · 600ms+ on
  hover · motion on every element ("mayhem not motion") · auto-rotating hero carousels · cursor-trail
  particle gimmicks · heavy WebGL/3D that loads megabytes before paint · skipping `prefers-reduced-motion`.
