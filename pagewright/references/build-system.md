# Sistema de build — HTML + Tailwind, artesanal e atual

A saída é um site estático que abre sem nenhum passo de build e parece finalizado. Este arquivo é o
contrato técnico: como conectar um Design DNA ATUAL ao Tailwind, a estrutura a emitir e o checklist de craft.

## Estrutura de saída

`scripts/new_site.py "<project-name>"` faz o scaffold de `index.html` + `assets/{images,favicon.svg}` + README.
Single-page por padrão; adicione páginas `.html` irmãs com nav/footer compartilhados só se for necessário.

## Setup de Tailwind + fontes

Use por padrão o **Tailwind Play CDN** (zero build) com o DNA injetado como tokens reais. Carregue fontes
**atuais** — nunca caia no padrão de só Inter ou system-ui. Escolha a partir do vocabulário em design-dna.md; carregue assim:

```html
<!-- Editorial serif display + neutral grotesque body (the 2025-26 move). Swap per the DNA. -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Hanken+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
<!-- Geist + Geist Mono (dev-taste, free) — on Google Fonts: -->
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300..800&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<!-- More free current faces on Google Fonts: Instrument Serif, DM Serif Display, Newsreader, Schibsted Grotesk,
     Plus Jakarta Sans, Albert Sans, Bricolage Grotesque, Instrument Sans, Host Grotesk.
     Fontshare (api.fontshare.com) for Clash/Satoshi/Switzer if a heavier display is wanted. -->

<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = { theme: { extend: {
    colors: {                 // TINTED neutrals, not pure black/white — name by ROLE
      bg:'#09090B', surface:'#18181B', raised:'#27272A', line:'#3F3F46',
      ink:'#FAFAFA', muted:'#A1A1AA', faint:'#71717A',
      accent:'#<one sharp saturated accent — NOT indigo/violet>',
    },
    fontFamily: {            // from the DNA pairing
      display:['Fraunces','Geist','serif'], sans:['"Hanken Grotesk"','Geist','system-ui','sans-serif'],
      mono:['"Geist Mono"','ui-monospace','monospace'],   // ONLY inside a literal code/terminal snippet — never decorative (see design-dna.md)
    },
  } } }
</script>
```

Defina `<meta name="viewport">`, um `<title>` de verdade, meta de OG/description. Temas claros: use superfícies
`#FAFAFA`/off-white quentes, não `#FFFFFF`.

## Design tokens → Tailwind

- **Cor por papel** (`bg/surface/raised/line/ink/muted/faint/accent`) para que a paleta seja trocável e
  disciplinada. O accent mapeia para o CTA primário + 1-2 momentos focais APENAS.
- **Neutros tingidos + luminância em degraus** carregam a profundidade (ex.: `#09090B → #18181B → #27272A`) em
  vez de sombras pesadas. Bordas são hairlines de 1px (`line`).
- **Escala tipográfica** a partir do DNA. Display grande e confiante com **optical sizing + tracking negativo**
  (`tracking-tight`, `leading-[1.02]`), corpo de texto confortável 16-18px, `leading-relaxed`. Use **contraste
  extremo de peso** (ex.: display `font-light` vs. acentos `font-bold`) — passa a sensação de atual.
- **Ritmo de espaçamento** — escolha uma escala de padding de seção (`py-24 md:py-32`) e reutilize; consistência é
  a maior parte do "polido". Centralize com `max-w-6xl mx-auto px-6`; deixe visuais selecionados estourarem mais largos.

## Textura (sinal de craft — use deliberadamente)

```html
<!-- SVG grain overlay (15-30% opacity), fixed, pointer-events-none -->
<svg class="pointer-events-none fixed inset-0 -z-10 h-full w-full opacity-[0.04]"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>
```
Um grid sutil de pontos/blueprint via um background `radial-gradient`/`linear-gradient` em uma seção; um glow
ambiente `accent` desfocado atrás da UI do produto. Evite glassmorphism pesado como estrutura.

## Fotos full-bleed e overlays — a pegadinha do `-z-10`

Uma foto de hero full-bleed (ou o grain overlay acima) colocada *atrás* do conteúdo com **`-z-10`**
silenciosamente **some em preto** se a seção dela não formar um stacking context: um z-index negativo se resolve
contra o stacking context mais próximo, então numa seção `relative` transparente ele afunda *atrás do próprio
background da página* (`bg-page` no `<body>`) e desaparece. É um bug real e fácil de não perceber — a `<img>`
carrega normalmente, ela só é pintada por baixo da página. Corrija com uma destas opções:
- Adicione **`isolate`** (`isolation:isolate`) à seção → os filhos `-z-10` ficam locais, atrás do conteúdo mas
  na frente do background da página. (O mais simples.)
- Ou empilhe explicitamente: `<img>`/overlay de background em **`z-0`**, wrapper de conteúdo em **`relative z-10`**
  — sem nenhum z negativo.

Depois, um scrim **leve** para legibilidade (ex.: `from-page/55 via-transparent to-page` + um pool radial suave
atrás do título) — mantenha-o leve para que a foto realmente apareça. Uma âncora rica mostra sua foto de hero com
destaque; não a soterre sob um scrim de 85%.

## Componentes (princípios, não templates rígidos — templates geram mesmice)

- **Botões:** primário (accent) + secundário (ghost/outline), hover/active/focus de verdade, labels específicos.
  Considere um primário `data-magnetic` (veja motion.md).
- **Nav:** `<header>` logo + 3-5 links + CTA primário; condense/desfoque ao rolar; menu mobile funcional.
- **Ícones:** um conjunto multi-peso — **Phosphor / Iconoir / Hugeicons** (CDN ou SVG inline) — combinando com a
  linguagem de forma. NÃO use Lucide/Feather cru de peso único, NÃO use mascotes Corporate Memphis.
- **Cards/bento:** varie tamanho e conteúdo; um bento de **screenshots reais do produto** em tamanhos variados
  bate três caixas iguais de ícone-com-texto (esse trio é uma marca registrada de IA).
- **Visual de produto:** enquadre os screenshots intencionalmente (chrome de browser/app, inclinação, glow suave)
  para que leiam como produto real — muitas vezes é a assinatura da página.
- **Seções:** `<section aria-labelledby>` semântico; um único `<h1>` (hero).

## Responsivo · A11y · Performance

- **Mobile-first**, verifique 320px → `sm md lg xl`. O hero empilha no mobile; alvos de toque ≥44px; sem scroll
  horizontal; `clamp()` para o título do hero.
- **A11y:** landmarks semânticos, um único `h1`, **alt em toda imagem com significado** (`alt=""` para
  decorativas), contraste WCAG AA (cuidado com `muted` sobre `surface`), foco visível, navegação por teclado,
  `prefers-reduced-motion` respeitado.
- **Perf:** `loading="lazy"` + width/height em imagens abaixo da dobra; SVG para logos/ícones; formatos modernos;
  motion barato via CSS-transform; JS vanilla mínimo. Nada de WebGL de vários MB antes do paint.

## Motion

Veja **[motion.md](motion.md)** — no mínimo um reveal com blur-in + um motion de assinatura, easing atual
(spring/curto), protegido por `prefers-reduced-motion`. Não use AOS.js nem fade-up em tudo.

Quando montado, vá para **image-strategy.md** para os visuais, depois faça o preview e o polimento.
