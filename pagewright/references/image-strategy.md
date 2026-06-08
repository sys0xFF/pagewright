# Estratégia de imagens — deixe as imagens fazerem o trabalho pesado

Os sites de SaaS mais bonitos não são puro CSS. O que faz com que pareçam caros geralmente é uma
**imagem excelente**: um screenshot nítido do produto, um render 3D evocativo, uma ilustração com
personalidade. Ferramentas de IA tendem a evitar imagens e simular tudo com gradientes e blobs — que é
exatamente por isso que o resultado parece genérico. Esta skill faz o oposto: **planeje as imagens
primeiro, reserve espaço real para elas e gere-as ou entregue ao usuário prompts prontos para rodar.**

## Construa a imagem do produto em HTML/CSS — não deixe um placeholder no lugar (a regra de fidelidade #1)

A maior razão isolada para landing pages de IA parecerem wireframes vazios é largar uma **caixa cinza de
placeholder** onde o produto deveria estar. Os melhores sites reais — Linear, Stripe, Attio, Vercel — fazem
o oposto: eles **constroem a UI do produto em HTML/CSS** diretamente na página. Uma UI feita à mão com
fidelidade é o que faz um hero ser lido como um *produto real lançado* em vez de um mockup.

**Se a imagem é uma UI de produto, dashboard, tabela de dados, gráfico, código/diff, terminal, chat, mapa
ou diagrama → CONSTRUA EM HTML/CSS/SVG.** Dados com cara de reais, micro-tipografia nítida (~11–13px),
bordas hairline de 1px, status pills, avatares (tiles com gradiente CSS), numerais tabulares; emoldure tudo
em chrome de browser/app. Esse costuma ser o elemento assinatura da página e não custa nada além de capricho.
(Abra um thumbnail da biblioteca como linear.app ou attio.com e reconstrua sua superfície com fidelidade.)
**→ Leia [product-ui.md](product-ui.md) antes de construir** — ele traz o craft por componente (dashboards,
tabelas, gráficos, logs, cards, nav, formulários) para que a superfície saia específica e atual, não o
default genérico de "painel escuro + caixa hairline + números mono".

**Reserve placeholders de imagem + geração para o que você genuinamente NÃO CONSEGUE construir em código:**
fotografia, renders 3D/escultóricos, ilustração, logos de marca. Para esses, entregue um placeholder
dimensionado E (de preferência) gere o asset — um hero preenchido sempre ganha de um vazio.

Teste rápido: **se o seu hero é uma caixa cinza, você não terminou.** Construa a UI ou gere a imagem.

## Construa interfaces; fotografe ou gere OBJETOS (a linha que te salva do clip-art)

A regra acima é sobre **interfaces e dados** — dashboards, tabelas, gráficos, código, chat, diagramas,
gráficos guiados por tipografia. Aí, construir à mão é um superpoder: divs e SVG são lidos como *reais*.

Isso **NÃO** é licença para desenhar à mão um **objeto físico** em SVG. Uma garrafa, um anel, um dispositivo,
uma lata com condensação, uma fruta — modelados do zero numa só tacada — quase sempre saem como clip-art
chapado e meio errado. Um anel feito de gradiente CSS é lido como o *wireframe* de um anel, não como um anel.
Essa é a forma mais comum de um hero feito à mão parecer "meio pá" (janky).

Roteie pelo que a imagem **é**:
- **Interface / dados / diagrama / código / tipografia** → CONSTRUA em HTML/CSS/SVG. (Um anel de data-viz que
  traça estágios de sono reais é uma *interface* — construa, e invista nele.)
- **Objeto físico / material / forma orgânica / 3D / uma cena real** → **fotografe (Unsplash, com grade — veja
  abaixo) ou gere (Nano Banana)**. Uma foto real com grade ou um render gerado limpo ganha de um objeto em
  SVG feito à mão toda vez. Uma coisa chapada e retangular (um card, um sticker, uma janela de UI) é muito
  mais segura de construir à mão do que uma curva, iluminada e orgânica (uma garrafa, um anel, uma lata).

Se você FOR construir um objeto à mão, atinja o nível ou não publique: proporções reais (olhe uma foto de
referência primeiro), um **gradiente de material** (não um preenchimento chapado), highlight especular em
camadas + sombra de núcleo + uma sombra de contato/projetada sobre uma superfície, e direção de luz consistente.
Se você não consegue atingir esse nível, entregue um **placeholder dimensionado com grade + um prompt de
geração/foto** — um placeholder honesto ganha de clip-art janky, e o fluxo de foto/geração abaixo vai
preenchê-lo direito.

## Princípio

Para cada momento visual, pergunte: *uma imagem real/gerada diria isso melhor do que CSS?* Se sim, crie um
slot de imagem. Não finja um screenshot de produto com divs empilhadas quando uma imagem real (ou um mock
gerado) cantaria. Não encha o hero com formas abstratas quando um canvas de produto provaria o valor.

Mas mantenha a disciplina: algumas poucas imagens fortes e intencionais ganham de uma página entupida de
stock. Escolha os momentos que importam (geralmente: imagem do hero, uma ou duas imagens de feature, talvez
um detalhe de ilustração).

## Onde as imagens valem o seu lugar

| Slot | Tipo típico de imagem | Por quê |
|---|---|---|
| Hero visual | product screenshot / live UI / abstract-3D | prova que é real, define o clima |
| Feature blocks | product shots focados / diagramas | mostre, não conte |
| How-it-works | ilustrações simples / imagens de passos | torna concreto e acolhedor |
| Social proof | logos reais (SVG) | confiança emprestada |
| Testimonials | avatares reais | humaniza |
| Background accents | gradient-mesh / textura / ruído | clima, usado com parcimônia |

## Tipos de imagem & receitas de prompt

Quando você cria um slot de imagem, decida o **tipo** dele e escreva um prompt pronto para uso. Mantenha os
prompts alinhados ao Design DNA (paleta, clima). Receitas:

- **Product screenshot / app UI mock** — *"Clean [product type] dashboard UI, [dark/light] theme,
  [accent] accents, showing [key feature]; realistic SaaS interface, crisp typography, subtle depth,
  no lorem ipsum — use plausible real labels; 16:10."* Emoldure em chrome de browser/dispositivo no markup.
- **Abstract / 3D render** — *"Abstract 3D render, [palette] gradient, soft studio lighting, glass/metal
  forms, premium tech aesthetic, [mood] feel, high detail, 4k, transparent or [bg] background."*
- **Illustration** — *"[flat/iso/line] illustration of [concept], [palette], consistent stroke,
  friendly modern style, on [bg]; no text."*
- **Photography** — *"Editorial photo of [subject], natural light, [mood] tone, shallow depth of field,
  authentic not stock-y."*
- **Gradient-mesh / texture** — *"Soft mesh gradient, [2-3 palette colors], grainy, subtle, abstract
  background; seamless."*

Dica: mantenha um descritor de estilo consistente entre as imagens de uma página para que pareçam um único
conjunto.

## Placeholders (sempre entregue estes)

Todo slot de imagem ganha um **placeholder dimensionado e rotulado** para que a página pareça intencional com
zero assets e o usuário saiba exatamente o que colocar ali.

Use **`scripts/placeholder.py`** para emitir SVGs/PNGs de placeholder na proporção certa, rotulados com o
nome do slot (ex.: "HERO — product screenshot 16:10"). No markup, dê a cada `<img>` um `width`/`height` real,
um `alt` descritivo e um comentário com o prompt de geração para que fique pronto para troca:

```html
<!-- IMAGE SLOT: hero product screenshot — prompt: "Clean analytics dashboard, dark theme, indigo
     accents, showing a funnel chart; realistic SaaS UI, 16:10" -->
<img src="assets/images/hero-placeholder.svg" width="1280" height="800"
     alt="Acme dashboard showing conversion funnel" class="rounded-xl border border-surface" />
```

## Opcional: gerar as imagens (opt-in)

A geração vem **desligada por padrão**. Ofereça; se o usuário quiser E um gerador estiver configurado, rode.

- **Gemini "Nano Banana" (Gemini 2.5 Flash Image)** via **`scripts/gen_image.py`**. Precisa de uma
  `GEMINI_API_KEY` (do Google AI Studio — nota: uma assinatura do *app* Gemini NÃO é acesso à API; a
  API tem seu próprio tier gratuito com rate limits, e a disponibilidade/custo de geração de imagem no tier
  gratuito varia, então o script falha de forma elegante e recai em placeholders + prompts).
- **Fluxo:** para cada slot, o script pega o prompt + dimensões, escreve o resultado em
  `assets/images/`, e você o conecta ao markup substituindo o placeholder.
- **Sem chave / recusou?** Entregue placeholders + a lista de prompts (um pequeno `IMAGE-PROMPTS.md` na saída)
  para que o usuário possa colá-los no Nano Banana / Midjourney / na ferramenta de escolha dele e jogar os
  resultados ali.

De qualquer forma, a página fica completa e executável. A geração é um aprimoramento, nunca uma dependência.

## Opcional: buscar uma foto real — Unsplash (opt-in)

Alguns slots querem uma *fotografia real*, não um render: uma paisagem cinematográfica full-bleed atrás do
hero (o composition archetype **full-bleed-photo** — veja design-dna.md), uma textura orgânica (neblina, pedra,
papel, folhagem, água), uma still life editorial. A geração consegue falsificar isso, mas a fotografia real
muitas vezes é lida como mais verdadeira e não custa nada para gerar. Use **`scripts/fetch_unsplash.py`**
(desligado por padrão; precisa de uma `UNSPLASH_ACCESS_KEY` gratuita). Ele busca por uma query de clima, baixa
um JPEG dimensionado, registra o download e escreve a atribuição obrigatória em `UNSPLASH-CREDITS.md`.

**Guardas de bom gosto (o script não consegue impô-las — você precisa):**
- **Lugar, objeto, textura, abstração — não pessoas.** Paisagens, céus, água, folhagem, pedra/papel/tecido,
  detalhe macro, arquitetura, mãos/artesanato, ingredientes fotografados de forma editorial. Uma foto com
  *pessoas como sujeito* quase sempre é lida como stock ("time diverso em laptops") — exatamente o slop que
  esta skill evita.
- **Sempre aplique grade** para que pertença à página e não a uma biblioteca de stock: uma sobreposição
  duotone/de cor na paleta do Design DNA, uma camada de grão e um scrim de gradiente para contraste do texto.
  O script imprime um snippet de grade pronto para copiar e colar. Uma foto de stock crua e sem grade é um
  denúncia; uma com grade pesada pode ser a assinatura.
- **Escolha deliberadamente.** Passe uma query específica e com clima ("low fog over black volcanic rock, muted,
  no people"), e use `--index` para pular o resultado óbvio se ele estiver genérico demais.
- **Combina com o Nano Banana, não o substitui.** Foto real para lugar/textura; gere para 3D/produto/ilustração.
  Construa a UI do produto em HTML/CSS como sempre (a regra #1 acima).

```bash
python scripts/fetch_unsplash.py --query "low fog over pine forest at dawn, muted, no people" \
    --out assets/images/hero-bg.jpg --orientation landscape --width 1600
```

Sem chave / recusou? O placeholder dimensionado É o fallback, e você pode entregar ao usuário a mesma query
para pegar uma foto na mão. A página continua completa e executável.

## Escolhas atuais de assets (para não parecer datado)

- **Ícones — use um conjunto multi-peso, casado com a linguagem de formas da página:** Phosphor, Iconoir ou
  Hugeicons (gratuitos, muitos pesos), ou os premium Untitled UI Icons. **Evite Lucide/Feather de peso único
  e cru** usados sem nenhum casamento estilístico — esse é o visual de template default.
- **Ilustração / 3D — vá escultórico, não flat-vector.** 3D leve (embed do Spline ou Blender pré-renderizado)
  como hero — esferas escultóricas, fitas, formas de liquid-metal/vidro — é lido como premium. Se usar
  ilustração, mantenha-a custom e com personalidade. **Nunca** mascotes Corporate Memphis (Humaaans, unDraw,
  Open Peeps, Storyset, ManyPixels) ou cenas tech isométricas genéricas de "servidores & conectividade" — ambas
  são denúncias na hora, abandonadas por marcas de verdade.
- **Fotografia — real acima de stock.** Fotos de fundador/time/produto com uma grade consistente ganham do
  stock "time diverso em laptops". Se não houver nenhuma, prefira UI de produto ou 3D em vez de uma foto de
  *pessoas* de stock — mas uma foto editorial de **lugar/textura** com grade (paisagem, neblina, pedra, folhagem)
  é jogo limpo e muitas vezes linda: busque com `scripts/fetch_unsplash.py` e aplique a grade (veja a seção
  Unsplash acima).
- **Textura ganha de brilho.** Um pouco de grão/ruído sobre um fundo suave é lido como mais humano e atual do
  que uma superfície de IA hiper-perfeita, lustrosa e de sombras suaves.

## Não faça

- Não use stock genérico ou ilustrações com cara de clip-art que não dizem nada sobre o produto.
- Não sobrecarregue — uma página de imagens sem espaço para respirar é tão ruim quanto nenhuma.
- Não publique `<img>` quebrado sem fallback; o placeholder É o fallback.
- Não apresente logos/fotos de depoimento inventados como se fossem reais — rotule placeholders como trocáveis.
