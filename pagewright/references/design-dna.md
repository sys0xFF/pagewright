# Design DNA — descubra um clima e construa um sistema visual ATUAL

Pular esta etapa é o motivo #1 de páginas de IA parecerem genéricas: o modelo recai sobre seu padrão médio —
**Inter em tudo, um gradiente índigo→roxo, três cards com ícones, sombras suaves, eyebrows em fonte mono.**
Essa pilha exata é a cara do "gerado por IA" em 2025-26. Este arquivo existe para tirar você do padrão
e colocá-lo numa direção atual, específica e comprometida.

Trabalhe em três movimentos: **(1) Descubra um clima → (2) Olhe as referências reais e copie fielmente →
(3) Fixe um Design DNA no vocabulário de hoje.** Regras anticonvergência permeiam os três.

---

## Movimento 1 — Descoberta de clima (sem adjetivos vagos)

"Limpo e moderno" produz o padrão. Force uma direção *específica* no lugar. Anote o seguinte:

- **MOTIF** — uma metáfora concreta que a página inteira possa encarnar (uma sala de controle, um livro-razão,
  um quarto escuro de revelação, uma planta baixa, uma viagem noturna de carro, uma ficha técnica impressa,
  um terminal de trading, um jardim). O motif comanda paleta, tipografia, imagens e a assinatura.
- **BRAND-COORDINATE** — "**X meets Y**" usando dois mundos/marcas reais que o usuário admiraria
  ("Aesop meets Linear", "terminal Bloomberg meets Teenage Engineering", "uma página da Kinfolk meets Vercel").
  Isso triangula um ponto no espaço de estilo em vez de um clichê.
- **SENSORY + EMOTION** — 2-3 palavras sensoriais concretas (fosco, tátil, zumbindo, glacial, papel-quente)
  e a ÚNICA sensação que um visitante deve ter em 5 segundos (tranquilizado / no comando / animado / compreendido).
- **AVOID-LIST (obrigatória)** — escreva 4-6 coisas que ESTA página NÃO vai fazer, para antecipar o padrão. Sempre
  inclua os vícios de IA; adicione os específicos do projeto. Exemplo:
  `sem títulos em Inter · sem gradiente índigo/roxo · sem três-cards-com-ícone-iguais · sem eyebrows em mono ·
   sem o padrão hero-texto-à-esquerda / imagem-à-direita · sem hero tímido centralizado`

Leve o MOTIF, o COORDINATE e a AVOID-LIST adiante — são tão importantes quanto a paleta.

---

## Movimento 2 — Ancore em UMA referência real (a função forçante)

Esta é a etapa que de fato estanca a convergência — e ela só funciona se você a executar como um procedimento
rígido, não como conselho. O padrão de landing page do modelo (**pílula de eyebrow → título com uma palavra de
destaque → dois CTAs → uma fileira de três estatísticas → mural de logos → três cards de feature**) é um atrator
profundo; "tente variar" perde para ele toda vez. A única coisa que vence um padrão é construir a partir dos
*ossos de uma página real específica*. Então:

**1. Roteie por nicho → uma shortlist.** Abra `reference-library/INDEX.md`. Encontre seu nicho/contexto na
   lista **By niche** e seu clima em **By mood**; pegue os 3–5 sites naquela interseção.
   - *Nicho não está na biblioteca?* (ela cobre health, fintech, dev-tools, nature, food, education, beauty,
     fitness, home, travel e mais — mas não tudo.) Então **roteie por composição, não por indústria**:
     escolha o **arquétipo de composição** (abaixo) que combina com o clima e pegue sites que o usem, qualquer
     que seja o setor. Um app de meditação pode pegar emprestado fielmente os ossos de uma página de moda
     editorial-photo; uma cooperativa rural pode pegar emprestado uma página de CPG warm-minimal. Combine a
     *forma*, não a indústria.

**2. OLHE os pixels — obrigatório.** Dê `Read` no thumbnail `.jpg` de cada site da shortlist. A entrada de texto
   é um mapa; a imagem é o território. Seu olho se calibra à execução atual — tipografia real, espaçamento,
   temperatura de cor, como o visual é encenado — de um jeito que a prosa nunca dá. Pular isto é a forma mais
   comum de um build reverter silenciosamente ao padrão.

**3. Escolha UMA âncora e transcreva seu esqueleto — por escrito, antes de qualquer markup.** Escolha o único
   site cuja *estrutura* serve melhor a este produto (e que você não acabou de usar — veja o ledger abaixo).
   **Se ele tem uma captura de página inteira (`reference-library/full/<domain>.jpg`), ABRA-A** — é a página
   real inteira, de cima a baixo, não só o hero. Leia a sequência **real** de seções e suas peculiaridades
   estruturais (uma batida assimétrica, um changelog, nenhum pricing, uma ordem estranha) e **escreva a espinha
   que você vai construir**, copiando o que a página real genuinamente faz — *mesmo quando não é o arco "esperado".*
   (Sem captura inteira? Recorra à linha `sections:` da entrada, mas saiba que ela é seca e o detalhe inventado
   é exatamente onde você deriva de volta para o template.) Esta transcrição *é* a função forçante: você constrói
   sobre os ossos de uma página real, não sobre sua média — e sua média É o template genérico que você está
   combatendo.
   > ex.: âncora = linear.app → sua espinha real (da captura inteira) é `hero(UI do app ao vivo) › logo-wall ›
   > 3-up › feature(UI) › feature(UI) › feature(code) › feature(chart) › changelog › 2-up-testimonial ›
   > cta › footer` — note que não há **problem-reframe nem pricing**. Você constrói AQUILO, com nova pele — não
   > o template que seu padrão quer emitir.

**4. Tire a pele dos outros — nunca da âncora.** Pegue paleta, tipografia, textura e motif dos *outros* sites da
   shortlist + seu clima. Isto resolve a aparente contradição desta skill: **estrutura de UM (fielmente), pele
   do resto (remixada).** O resultado não clona ninguém — sua superfície é recombinada — e ainda assim tem uma
   espinha real, porque sua estrutura é fielmente a de uma página. Remixe ≥3, clone 0 e copie a estrutura com
   ousadia a partir de uma. *Mesmo ao copiar, seja fiel.*

**5. Rotacione a âncora (ledger).** Duas páginas jamais devem compartilhar uma âncora. Antes de se comprometer,
   lembre em que você ancorou recentemente; se for o mesmo site *ou o mesmo arquétipo de composição*, troque.
   Dentro de um nicho especialmente: nem toda página de fintech ancora na Stripe, nem toda página de health na
   Oura — distribua a carga pela shortlist. **Construindo várias de uma vez (um batch / agentes paralelos)?**
   Builders paralelos são cegos uns aos outros, então colidem no default da moda (todo mundo recorre ao Geist,
   ao título com palavra de destaque, à faixa de CTA escura). Atribua a cada um uma **âncora, arquétipo de página
   (section-patterns.md), família de display-font, accent e gramática de hero** *diferentes* logo de cara — e
   explicitamente **proíba os reflexos DTC compartilhados** para que dois irmãos não entreguem ambos o título
   com uma-palavra-de-destaque ou o reframe contrarian. Entradas distintas entram, páginas distintas saem.

É assim que você escapa do padrão: você constrói a partir dos ossos de uma página real, não da memória.

---

## Arquétipos de composição — rotacione o ESQUELETO, não só a pele

A convergência é majoritariamente *estrutural*: mesmo com paleta e fonte novas, duas páginas rimam porque
compartilham um esqueleto. Então escolha a composição do hero/página **deliberadamente** e rotacione-a entre
builds. Cada arquétipo abaixo tem exemplares reais na biblioteca — ancore em um (e lembre que a forma é
agnóstica de indústria: um briefing fora de tech pode pegar estes emprestado livremente):

- **split-screen** — texto de um lado, visual do outro (o default — use *o mínimo*). ex.: attio, framer
- **centered-editorial** — título grande centralizado, ar generoso, visual abaixo. ex.: vercel, cohere
- **full-bleed-photo / cinematic** — uma foto ou render preenche o hero, texto sobreposto. ex.: palantir,
  cluely, index.inc, spellbook  (← o slot que a fotografia da Unsplash preenche — veja image-strategy.md)
- **bento-grid** — o hero *é* um grid de tiles de produto desiguais. ex.: supabase, raycast, default
- **poster / coverline** — energia de capa de revista: tipografia condensada superdimensionada, chrome mínimo. ex.: mux, polar
- **asymmetric-canvas** — texto numa coluna estreita, um campo visual amplo ao lado. ex.: morphic
- **product-diorama** — um único objeto 3D/fotorrealista encenado como o hero inteiro. ex.: lithic, oxide, three.tools
- **app-frame** — uma reconstrução fiel da UI do produto em chrome de browser/app é o hero. ex.: linear, amie
- **oversized-type** — a tipografia em si é a imagem; pouco ou nenhum gráfico. ex.: clickhouse, juicebox, pipe
- **diptych / triptych** — painéis repetidos mostrando estados ou variantes. ex.: authkit, rive

Regra prática: **se sua última página foi split-screen com três cards, esta não é.**

---

## Movimento 3 — Fixe o Design DNA (vocabulário de hoje)

```
MOTIF + COORDINATE: <ex. "sala de controle" · "terminal Bloomberg meets Teenage Engineering">
AVOID-LIST:         <4-6 coisas que esta página não vai fazer>
PALETTE:
  - neutrals: <TINGIDOS, não puros — escuro ex. #09090B/#18181B/#27272A/#3F3F46 · claro #FAFAFA/off-white quente>
  - accent:  <UM ou dois accents saturados e AFIADOS (podem ser elétricos); onde é permitido — NÃO índigo/violeta>
  - mode:    <light | dark | warm-light>
TYPE (escolha um par real de 2025 — veja o vocabulário abaixo; NÃO só Inter, NADA de mono como face de brand/UI):
  - display: <grotesque cheia de caráter OU serifa editorial + por que combina com o motif>
  - body:    <grotesque neutra de trabalho pesado>
  - move:    <contraste de peso extremo / serif-display+sans / condensada superdimensionada / optical sizing>
DENSITY:   <airy-editorial | balanced | dense-terminal>
MOTION:    <escolha de motion.md — pelo menos um reveal blur-in + um movimento de assinatura; combine com a brand>
TEXTURE:   <grão (SVG 15-30%) / grid de pontos ou blueprint / luminância em degraus / nenhuma — escolha deliberadamente>
IMAGERY:   <UI real do produto / 3D escultural (Spline) / foto editorial / ilustração custom — veja image-strategy.md>
SIGNATURE: <o ÚNICO movimento que quebra o gênero (veja abaixo). Deve surpreender; deve combinar com o motif.>
```

→ Depois leve os tokens para **build-system.md**, o motion para **motion.md**, as imagens para **image-strategy.md**.
→ Rode o **checklist Anticonvergência** (no fim deste arquivo) antes de construir.

---

## Tipografia ATUAL (use esta, não o padrão)

Inter como o sistema inteiro é o default literal de IA/early-stage; mono-em-tudo e Space Grotesk leem como
templates de cripto/IA de 2021-23. O movimento atual é um **display cheio de caráter + um corpo grotesque neutro**.

**Display / headline (escolha para combinar com o motif):**
- *Grotesques cheias de caráter* — **Geist**, Schibsted Grotesk, Bricolage Grotesque, Host Grotesk, Hanken
  Grotesk (gratuitas); Söhne, ABC Diatype, PP Neue Montreal, Aeonik, GT America/Walsheim, Monument Grotesk,
  TWK Lausanne, Suisse Int'l (pagas — nomeie como a intenção / use a alternativa gratuita mais próxima).
- *Serifa editorial de display* (a assinatura de 2025-26, usada com parcimônia em tamanho grande) — **Fraunces**
  (variável opsz/SOFT/WONK), **Instrument Serif**, DM Serif Display, Newsreader (gratuitas); PP Editorial New, GT Super,
  Reckless, Signifier, Tiempos Headline, Canela (pagas).
  > ⚠ **Aviso de reflexo excessivo:** um *headline em serifa editorial sobre escuro* virou o default desta skill
  > para qualquer coisa "premium/autoritativa". NÃO é o único movimento premium e agora é um vício. Para pelo menos
  > metade das suas páginas, faça o headline ser uma **grotesque pesada e cheia de caráter** no lugar (Bricolage, Geist,
  > Aeonik, Monument, Druk-condensada) — igualmente premium, e varia o output. Não recorra ao Fraunces
  > no piloto automático.
- *Display condensada de impacto* — Druk, Right Grotesk, Hatton, Anton (mais ou menos gratuitas) para heros de coverline de revista.

**Corpos de trabalho pesado (substituem Inter/Open Sans/Lato/Roboto):** **Geist**, Hanken Grotesk, Schibsted Grotesk,
Plus Jakarta Sans, Albert Sans, Instrument Sans, Inter *apenas* como um corpo discreto sob um display distintivo.

**Mono — banida como escolha de design.** É feia e datada (um vício de template de cripto/IA de 2021-23). NÃO use uma
face monospace para eyebrows, labels, captions, nav, botões, **números, estatísticas, dados ou células de tabela** — para
algarismos use o corpo grotesque com `font-variant-numeric: tabular-nums`, que lê muito melhor. O ÚNICO lugar em que
monospaçamento é permitido é dentro de um **snippet literal de código/terminal** (código é monospaçado por natureza) —
e mesmo ali mantenha em uma pequena superfície, nunca como a textura da página. Se você está recorrendo a mono para
adicionar "sabor técnico", pare: esse sabor *é* o visual genérico que estamos matando.

**Movimentos que leem 2025:** contraste de peso extremo (100/200 vs 800/900), optical sizing + tracking negativo
em display grande, numerais tabulares para algarismos, eixos de fonte variável, uma escala tipográfica de verdade.

**NÃO use** (vícios datados): Inter em tudo, inclusive títulos · Space Grotesk / Space Mono · Poppins
/ Montserrat · Playfair Display · Open Sans / Lato / Roboto como face de brand · **qualquer fonte monospace fora
de um bloco de código literal** (sem eyebrows, labels, números ou dados em mono — é banida, veja acima).

→ Receitas de carregamento (Google Fonts / Fontshare / Geist CDN) estão em **build-system.md**.

## Paleta & superfície ATUAIS

- **Neutros tingidos, nunca puros.** Escuro: `#09090B → #18181B → #27272A → #3F3F46` (zinc/luminância em degraus);
  claro: `#FAFAFA` ou um off-white quente. `#000`/`#FFF`/`#2563EB` puros leem chapados e templatizados.
- **Um neutro + 1-2 accents AFIADOS.** Accents podem ser elétricos. Roube paletas da cultura ou de temas de IDE
  (ex.: um filme, uma cidade à noite, um tema de editor Tokyo Night / Catppuccin). **Default proibido: índigo/
  violeta, e o gradiente de hero roxo→azul — o vício de IA mais forte que existe.**
- **Gradientes só quando funcionais** — um gradiente sutil em um heading, um glow ambiente desfocado atrás da
  UI do produto, um mesh discreto. Não uma lavagem inteira de roxo-para-azul.
- **Textura como ofício** — grão SVG comedido (`feTurbulence`, 15-30% de opacidade), bordas de 1px hairline,
  grid sutil de blueprint/pontos, superfícies de luminância em degraus em vez de drop-shadows pesadas e glassmorphism.

## A assinatura precisa quebrar o gênero

O ÚNICO movimento memorável que as páginas deste nicho geralmente NÃO fazem — guiado pelo motif. Se for um clichê
do gênero (o live-console+sparkline da dev-tool escura; o telefone flutuante da fintech; a serifa-editorial-sobre-escuro
que até *esta skill* agora usa demais), não é uma assinatura. Vá além: um arquétipo de layout inesperado, uma
textura tátil, um bloco de cor ousado, UI real do produto encenada de forma incomum, um trocadilho tipográfico, uma metáfora física.

---

## Anticonvergência — variedade obrigatória (rode antes de construir)

A convergência é o inimigo mesmo depois que você escapa do padrão óbvio. Ela morde em dois níveis — **estrutura**
(o esqueleto) e **superfície** (a pele) — e a estrutural é o que faz as páginas rimarem mesmo quando as cores
diferem. Confira ambos; rotacione para que duas páginas desta skill nunca compartilhem uma espinha.

**Estrutura — o esqueleto (a parte que todo mundo esquece de variar):**
- [ ] **Arquétipo de composição** — uma escolha *deliberada* da lista acima, diferente do seu último build.
      Não reflexivamente split-screen / hero-texto-à-esquerda + imagem-à-direita.
- [ ] **Sequência de seções** — transcrita da sua âncora (Movimento 2), guiada pela história — não o boilerplate
      genérico gancho → logos → 3-cards → CTA no piloto automático.
- [ ] **Gramática do hero** — quebre a corrente do padrão. Você NÃO precisa de um kicker/eyebrow, *e* de um
      título com uma-palavra-de-destaque, *e* de dois CTAs (preenchido + ghost-com-seta), *e* de uma fileira de exatamente três
      estatísticas. Descarte ou remodele **pelo menos dois** desses a cada build.
- [ ] **O kicker não é obrigatório** — um pequeno label com tracking acima do H1 (`UM ANEL DE SONO & RECUPERAÇÃO`) é
      a abertura mais reflexiva que existe, e ele sobrevive discretamente mesmo quando todo o resto varia. Para pelo
      menos **metade** das suas páginas, comece com outra coisa: vá direto no headline, uma frase adjacente à nav,
      uma data/preço/estatística, uma única palavra de produto ou uma pergunta. Se você *usar* um, faça-o trabalhar
      de verdade — um lugar, uma provocação, um spec — nunca apenas reafirmar a categoria em caixa-alta.
- [ ] **Layout de features** — nem sempre três cards iguais numa fileira. Considere um zigue-zague vertical alternado,
      um bento, um showcase profundo, um passo a passo numerado, uma tabela comparativa.

**Superfície — a pele:**
- [ ] **Tipografia** — não a mesma face de display que você escolheria reflexivamente; ela combina com ESTE motif especificamente?
- [ ] **Accent** — uma matiz/estratégia diferente do último build; não índigo/violeta.
- [ ] **Textura** — grão / grid / chapado / nenhuma — uma escolha deliberada e variada.
- [ ] **Ícones** — um set multi-peso (Phosphor, Iconoir, Hugeicons), combinado com a linguagem de forma — não
      Lucide/Feather cru de peso único.
- [ ] **Raio de canto & densidade** — afiado+denso vs suave+arejado é uma alavanca real; não recaia no 16px-arredondado.
- [ ] **Assinatura** — presente, quebrando o gênero e diferente da sua última página.

**Depois faça um self-diff antes de entregar.** Coloque o esqueleto da sua página ao lado da pilha genérica de IA abaixo. Se você
não conseguir dizer com clareza como a sua difere *estruturalmente* (não só em cor/fonte), você reverteu — volte ao
Movimento 2 e reconstrua sobre uma âncora diferente.

**Nunca entregue a pilha genérica de IA:** títulos em Inter + gradiente índigo/roxo + **pílula de eyebrow →
título com uma-palavra-de-destaque → CTA preenchido-+-ghost → fileira de exatamente três estatísticas → mural de logos → três cards de ícone
iguais** + tudo 16px-arredondado + sombra suave sutil + hero-esquerda/imagem-direita + eyebrows em mono + mascotes Corporate
Memphis (Humaaans/unDraw/Storyset) + stock "time diverso em laptops". Se dois ou mais destes estiverem
presentes, você reverteu ao padrão — refaça o clima.

---

## Os reflexos DTC — os defaults do modelo; deixe-os DESLIGADOS por padrão

Mesmo depois da correção do kicker, uma auditoria de páginas construídas por esta skill descobriu que elas AINDA rimavam — porque o
modelo tem um segundo conjunto, mais profundo, de reflexos de "landing DTC/SaaS moderna" que ele recorre *toda vez*.
Nenhum está errado isoladamente; usar o **conjunto inteiro em toda página É a convergência**, e é por isso que o output
"não parece baseado numa página real" — é baseado na média do modelo de todas as páginas. Trate cada um
como **DESLIGADO por padrão**: um dado build pode usar **no máximo um ou dois**, escolhidos deliberadamente, e deve variar *quais*
entre builds. Na dúvida, faça o que o reflexo substitui.

1. **O título com uma-palavra-de-destaque** — um título com exatamente uma palavra em itálico ou recolorida
   (*"o chai que você **realmente** sente falta"*, *"seu ar, finalmente **sentido**"*). O vício mais repetido de todos —
   ele aparece em todo hero E em todo título de seção. A maioria dos títulos deveria ter **zero** palavras de destaque.
2. **O CTA duplo (preenchido + ghost-com-seta)** — um botão sólido ao lado de um botão "→" em outline. Muitas vezes um
   único CTA, um campo de email inline ou um link de texto é mais fiel ao produto. Varie.
3. **O problem-reframe contrarian** — *"Você não tem um problema de X. Você tem um problema de Y."* / *"Um saquinho de chá
   é o fantasma do chai."* Um movimento persuasivo real, hoje um tique. Não abra a segunda seção assim por reflexo.
4. **A faixa de CTA escura full-bleed no fim** — uma seção de fechamento quase preta com um título com palavra de destaque
   e um botão. Tudo bem ocasionalmente; não é o final default. Um CTA integrado ao footer, um fechamento inline discreto,
   ou nenhuma seção de CTA separada são todos válidos.
5. **A faixa de estatísticas/specs do hero** — uma fileira de 3–4 algarismos fixados sob o hero. Às vezes merece o lugar;
   reflexiva no resto.
6. **O arco em si** — `hero → problema → 3-up → testimonial → pricing → CTA-escuro → footer`. Esta é a única forma
   verdadeira de landing do modelo, e segui-la é como toda página acaba igual. **Páginas reais não
   compartilham todas ele** (olhe uma captura de página inteira — a Linear não tem pricing nem problem-reframe; é um
   tour de produto feature-por-feature terminando num changelog). Tire sua estrutura da *página real da sua
   âncora*, não deste arco. Veja **section-patterns.md → Page archetypes**.

Autoverificação: se sua página tem o título com palavra de destaque **e** o CTA duplo **e** o reframe contrarian
**e** a faixa de CTA escura, você não desenhou uma página — você imprimiu o template. Reduza ao que sua
âncora de fato faz.

---

## Micro-gramática — ATRIBUA-a, não apenas proíba

Lição cara: uma lista de *proibições* ("deixe estes DESLIGADOS por padrão") ainda é conselho, e **conselho perde para o padrão**.
Uma auditoria cega de páginas construídas com a lista de reflexos acima ainda as classificou como "o house system de um estúdio" — os
agentes descartaram alguns reflexos mas discretamente reemitiram o kicker, a palavra de destaque, o CTA duplo e o mesmo
footer mesmo assim. A correção é a mesma que funcionou para tipografia e page-archetype: pare de proibir e
comece a **atribuir uma micro-gramática concreta de cara**, como um ticket que o build deve preencher.

**Antes de construir (e SEMPRE ao construir várias de uma vez), escreva um ticket de gramática de uma linha por página** e
mantenha-o. Faça as escolhas *concretas* e *diferentes por página*:

- **Gramática do hero:** kicker? (sim/não) · palavra de destaque no título? (não, por padrão) · registro do título
  (declarativo / pergunta / palavra-única / duas-orações) · padrão de CTA (único sólido / único link-de-texto /
  campo inline / nenhum acima da dobra).
- **Prova:** mural de logos / um pull-quote / uma linha de estatística / uma métrica ao vivo / nenhuma.
- **Fechamento:** faixa de CTA escura / CTA integrado ao footer / inline discreto / um wordmark superdimensionado — escolha um, e
  não o mesmo da sua última página.
- **Footer:** o modelo recai em "brand + frase + três colunas com labels em caixa-alta" toda vez — isso
  em si é um vício. Varie: um footer minimalista de duas linhas, um sitemap robusto, um footer de fileira única, um footer que é
  basicamente uma newsletter, um quase vazio.
- **Família de matiz:** nomeie a matiz real (não "um accent") e mantenha páginas irmãs em famílias *diferentes*
  (não entregue dois laranjas).

Para um batch, rode um **linter de convergência** antes de entregar: coloque as páginas lado a lado e liste o que elas
compartilham (gramática de hero, ordem de seções, forma de CTA, footer, o mesmo movimento retórico). Qualquer coisa compartilhada por 2+
páginas que não foi deliberada → mude em todas menos uma. Trate o compartilhado-por-padrão como um bug.

## Copie a IDENTIDADE com tokens reais, não de um screenshot

Por que o fiel "copie este site" ainda deriva para o genérico: a biblioteca te dá uma *imagem* e *prosa* da
referência, nunca seu CSS real — então você rededuz as fontes, espaçamento, cor e sombras de memória, e
a memória é o padrão genérico. Feche essa lacuna puxando os **tokens computados reais** da âncora e construindo
para eles literalmente:

- Use **`scripts/extract_tokens.py`** (opt-in; precisa de um browser) na URL da âncora para ler as *reais*
  famílias/tamanhos/pesos/tracking de fonte, paleta de cores, border-radii, o exato `box-shadow` dos cards, anatomia de botão
  e largura de container. Construa com **aqueles valores literais** — ex.: a
  sombra real de card da Stripe é `rgba(50,50,93,.25) 0 30px 60px -10px, rgba(0,0,0,.1) 0 18px 36px -18px`; os botões da Mercury
  são pílulas de 32px de raio num periwinkle `#5266EB`; o display da Vercel é Geist com tracking `-2.4px`.
  Esses detalhes específicos SÃO a identidade — um screenshot não consegue te dá-los, e adivinhar reverte ao padrão.
- Faces proprietárias (Söhne, Arcadia, sohne-var) não vão carregar — nomeie a intenção e substitua pela alternativa gratuita
  mais próxima (lista de tipografia do design-dna), mas mantenha o real *tamanho / peso / tracking / line-height*.
- Uma página excelente vence quatro apressadas: puxe os tokens, copie a estrutura real (captura de página inteira), construa,
  **tire um screenshot, compare com a âncora e itere** até a identidade de fato ler — não entregue o
  primeiro rascunho.
