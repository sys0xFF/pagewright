# Vocabulário de movimento — o jeito 2025-26

O movimento é grande parte do motivo pelo qual sites de verdade parecem vivos e páginas feitas por IA parecem sem graça. O gosto atual é **proposital
e contido**: micro-interações rápidas com easing de spring + revelações guiadas pelo scroll que mostram, não contam.
Escolha **pelo menos uma revelação com blur-in + um movimento de assinatura** por página. Sempre proteja movimento não essencial
atrás de `prefers-reduced-motion`.

**Toolchain padrão:** CSS nativo primeiro (animações guiadas por scroll já cobrem ~85%), depois `Motion`
(motion.dev, MIT, minúsculo) para trabalhos mais ricos, e GSAP só para timelines pesadas com pin. Não carregue GSAP por reflexo
para revelações simples e **nunca use AOS.js** — o visual de fade-up uniforme em tudo é a marca registrada de template de 2019-22.

Durações: **150-300ms** para UI/hover, **400-700ms** para revelações. Easing: spring / `cubic-bezier`
customizado / `linear()` com leve overshoot — não o `ease-in-out` chapado.

## Revelação com blur-in (a assinatura de 2025 — use isto no lugar de um fade simples)

O blur é o que separa o premium de um fade-up genérico. Combine blur + opacidade + leve subida.

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

## Revelação nativa guiada por scroll (zero JS, fora da main thread)

```css
@media (prefers-reduced-motion: no-preference){
  @supports (animation-timeline: view()){
    .reveal{ animation:reveal both; animation-timeline:view(); animation-range:entry 0% cover 35%; }
    @keyframes reveal{ from{opacity:0;filter:blur(10px);transform:translateY(24px)} to{opacity:1;filter:none;transform:none} }
  }
}
```

## Barra de progresso de scroll (uma regra, sem listeners)
```css
.progress{ position:fixed; top:0; left:0; height:2px; width:100%; transform-origin:left; transform:scaleX(0);
  background:var(--accent); animation:grow linear both; animation-timeline:scroll(root block); }
@keyframes grow{ to{ transform:scaleX(1) } }
```

## Marquee / ticker de logos só com CSS (sem biblioteca)
Duplique o conjunto de logos duas vezes dentro do track; translade `-50%`; aplique fade nas bordas; pause no hover.
```html
<div class="marquee"><div class="track"><!--logos x2--></div></div>
```
```css
.marquee{ overflow:hidden; -webkit-mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent); }
.track{ display:flex; gap:3rem; width:max-content; animation:marquee 32s linear infinite; }
.marquee:hover .track{ animation-play-state:paused; }
@keyframes marquee{ to{ transform:translateX(-50%) } }
```

## Botão magnético (premium, sutil — 6-12px no máximo)
```js
document.querySelectorAll('[data-magnetic]').forEach(b=>{
  b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();
    b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.2}px,${(e.clientY-r.top-r.height/2)*.2}px)`;});
  b.addEventListener('mouseleave',()=>b.style.transform='');
  b.style.transition='transform .3s cubic-bezier(.2,.7,.2,1)';
});
```

## Outros recursos atuais (use com parcimônia, no máximo uma assinatura)
- **Scrollytelling com sticky / pin** — `position:sticky; top:0` numa seção alta enquanto as camadas internas se trocam;
  ou GSAP ScrollTrigger `pin:true` + `scrub` para um hero/demo de produto guiado em múltiplos passos.
- **Parallax** — `animation-timeline: scroll()` transladando camadas de fundo em ritmos diferentes (barato,
  fora da main thread) em vez de rAF em JS.
- **Scramble / decode de texto** — GSAP ScrambleTextPlugin (agora gratuito) numa palavra do hero ou no rollover do nav; combine
  com SplitText para char a char. Em um único lugar.
- **View Transitions** — `@view-transition{ navigation:auto }` (MPA) ou `document.startViewTransition()`
  para morphs de elemento compartilhado (card→detalhe); degrada graciosamente.
- **Micro-interações de hover/tap** — transforms curtos de spring em cards/botões; count-ups com números tabulares
  em estatísticas via IntersectionObserver.

## Não faça
- AOS.js ou fade-up uniforme em tudo · fades com linear/ease sem blur/stagger/spring · 600ms+ no
  hover · movimento em cada elemento ("bagunça, não movimento") · carrosséis de hero com rotação automática · gimmicks
  de partículas seguindo o cursor · WebGL/3D pesado que carrega megabytes antes do paint · pular `prefers-reduced-motion`.
