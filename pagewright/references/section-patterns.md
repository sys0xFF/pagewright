# Section patterns & storytelling

Uma landing page é uma **narrativa persuasiva**, não uma pilha de blocos de UI. As seções são batidas de
um argumento. Escolha as batidas que contam a história DESTE produto, numa ordem que cresce, e escreva um
texto que um fundador realmente colocaria no ar.

## The narrative arc

A maioria das páginas SaaS de alta conversão percorre este arco (adapte, não siga rigidamente):

1. **Hook** — em 5 segundos: o que é isto, para quem é, por que se importar. (Hero)
2. **Credibility** — você não está sozinho / não é arriscado. (Mural de logos, métricas, "backed by")
3. **The problem** — nomeie a dor que o visitante sente agora mesmo. (Enquadramento do problema)
4. **The solution** — como você resolve, mostrando e não apenas contando. (Blocos de feature, visuais do produto)
5. **How it works** — faça parecer fácil e concreto. (Passos / fluxo de trabalho)
6. **Proof** — outras pessoas tiveram o resultado. (Depoimentos, estatísticas de casos)
7. **Objection handling** — clareza de preço, FAQ, segurança/compliance, integrações.
8. **The ask** — uma ação clara e repetida. (CTA final, depois o rodapé)

Dois frameworks clássicos de copy para se apoiar quando travar:
- **PAS** — Problem → Agitate → Solution. Ótimo para produtos movidos por dor.
- **AIDA** — Attention → Interest → Desire → Action. Ótimo para o amplo/consumidor.

Você raramente usa todas as seções. Uma página focada (hero → proof → 3 batidas de feature → how-it-works → depoimento
→ pricing → FAQ → CTA → footer) vence uma página-tudo. Corte qualquer coisa que não mova o argumento.

## Page archetypes — the arc above is ONE shape, not the only one

O arco narrativo é o *scroll de conversão clássico* — e se cada página que você constrói segue ele, toda página
rima, não importa como você a reveste. As melhores landing pages de verdade assumem **formas estruturalmente
diferentes**. Escolha uma deliberadamente por build (e faça rodízio entre builds), guiado pelo produto e — acima
de tudo — pela **página completa real do seu anchor** (abra `reference-library/full/<domain>.jpg` quando existir e
copie a sequência real, com manias e tudo; não normalize de volta para o arco).

- **Product tour** — hero (UI real do produto) → feature após feature, cada uma ancorada por seu próprio painel
  de UI, alternando os lados → uma batida de proof/changelog → CTA. Muitas vezes **sem reenquadramento de problema e
  sem pricing**. ex.: linear.app, attio.com, retool.com.
- **One-screen statement** — uma única viewport faz todo o trabalho: headline + um visual forte + uma
  ação. Pouco ou nenhum scroll. ex.: páginas de lançamento minimalistas, cohere.com, bun.sh.
- **Editorial long-read** — uma matéria de revista: fotografia full-bleed, seções de prosa em formato longo, pull-quotes,
  ar generoso. ex.: aesop.com, patagonia.com, palantir.com.
- **Catalog / product-grid** — os produtos *são* a página; uma prateleira/grade, focada na loja, com copy de marketing
  mínima. ex.: publicgoods.com, glossier.com, gymshark.com.
- **Manifesto** — um argumento ou atitude, movido por tipografia, voz sobre listas de features; o produto aparece tarde.
  ex.: liquiddeath.com, oatly.com.
- **Spec sheet** — denso e técnico: tabelas, figuras, um enquadramento de bancada de engenharia, figuras numeradas.
  ex.: oxide.computer, lithic.com.
- **Demo-led** — uma demo ao vivo, funcional/interativa é o hero e carrega a maior parte da página. ex.: cal.com,
  arcade.software.
- **Comparison-led** — construído em torno de um before/after ou de uma vs-table como batida central.
- **Classic conversion scroll** — o arco acima (hero → problem → features → proof → pricing → CTA). Ainda
  ótimo — apenas *uma* opção escolhida de propósito, não o default no piloto automático.

Regra: **nomeie o archetype da sua página antes de escrever o markup**, faça-a diferente do seu último build, e deixe
a estrutura real do anchor — não esta lista nem o arco — ditar as seções de fato.

## Length & density — match the anchor; cut filler, not richness

Contenção significa **sem enchimento** — NÃO **poucas seções**. A armadilha corta dos dois lados, e ambos são falhas reais
desta skill: builds iniciais que incharam numa página-tudo genérica; uma correção exagerada posterior na direção do "seja curto"
que despiu um anchor *rico* (Mercury — uma página densa de ~15 seções com um hero fotográfico cinematográfico, um dashboard de
produto detalhado, duas grades de cards-imagem 2×2, um carrossel de depoimentos, uma linha de estatísticas, cards de notícias,
divulgações com notas de rodapé) até um esqueleto raso de 7 seções de painéis de texto que se lia como **simplista**, não confiante.

A regra é **relativa ao anchor**: uma página é tão longa e tão densa quanto a página em que está ancorada — nem mais, nem menos.

- **Anchor minimal → página minimal.** Vercel, cohere, um lançamento one-screen: não o entupa com uma seção
  de problema, uma linha de estatísticas e um mural de depoimentos que ele não tem.
- **Anchor rico → página rica.** Mercury, Stripe, Aesop são *densos*: fotografia real, vários visuais de produto
  distintos, cards de feature lastreados em imagem, carrosséis, detalhe com notas de rodapé, tratamentos de seção variados. **Copie essa
  densidade** — gere as fotos, construa vários visuais diferentes, varie o *tipo* de seção. Uma pilha plana de
  painéis de texto não é uma cópia fiel de uma página exuberante; é o sintoma simplista, e tem metade da altura.
- **Corte ENCHIMENTO, mantenha RIQUEZA.** Enchimento = uma grade de benefícios redundante, um segundo mural de depoimentos, um
  passo super-explicado, uma frase que não muda uma opinião. Riqueza = imagem real, superfícies de produto
  distintas, o proof que uma página de verdade carrega. Corte o primeiro; nunca despoje a segunda para bater uma contagem de seções.
- **Varie o TIPO de seção, não só a copy.** Cada batida deve ser seu próprio *tipo* de coisa — uma batida de
  foto, uma UI construída, uma grade de cards-imagem, um carrossel, uma faixa de estatísticas, um pull-quote, uma linha de notícias. O mesmo painel plano
  repetido se lê como simplista mesmo no comprimento certo.

Autoteste: se sua página tem aproximadamente metade da altura do seu anchor e toda seção é um painel de texto plano, você
**sub-construiu** ela — volte e iguale a riqueza do anchor.

## Current section menu (from a ~670-example survey of live SaaS sites)

Páginas modernas de verdade se montam a partir destas, mais ou menos nesta ordem de frequência. Para qualquer seção que você esteja prestes a
construir, **abra a thumbnail de um exemplar da biblioteca** (Read `reference-library/thumbs/<domain>.jpg`) e
estude como um site real de 2025 de fato faz aquilo — então construa a sua, não reinvente de memória.

- **hero** (~122 ex) → estude: attio.com, evervault.com, cap.so, antimetal.com, amplemarket.com
- **logos / social proof** (~28) → linear.app, vercel.com, neon.tech, evervault.com, mintlify.com
- **value-proposition** (~24) → dovetail.com, neon.tech, synthesia.io, loops.so, jasper.ai
- **features / bento** (~93) → evervault.com, dovetail.com, lattice.com, highnote.com, cap.so
- **how-it-works** (~19) → synthesia.io, lattice.com, dovetail.com (+ estude qualquer um com um fluxo de "steps")
- **compare / vs-table** (~11) → outseta.com (+ tabelas estilo pricing)
- **testimonials** (~70) → framer.com, attio.com, highnote.com, lattice.com, jasper.ai
- **pricing** (~59) → attio.com, framer.com, cap.so, dovetail.com, highnote.com
- **integrations** (~23) → linear.app, dovetail.com, lattice.com, outerbase.com
- **faqs** (~20) → framer.com, equals.com, liveblocks.io, lattice.com, outerbase.com
- **cta** (~64) → framer.com, evervault.com, attio.com, dovetail.com, equals.com
- **footer** (~56) → framer.com, vercel.com, neon.tech, mintlify.com, evervault.com

Você raramente usa todas as seções — escolha as batidas que contam a história DESTE produto (a seguir). Mas quando você construir uma
batida, ancore-a num exemplo real acima.

## Section library

Para cada uma: seu trabalho, alguns **variantes estruturais** (varie-os por projeto — não recorra sempre ao
mesmo), e a armadilha a evitar. Escolha variantes que se encaixem na densidade e na assinatura do Design DNA.

### Hero (the 5-second test)
**Trabalho:** comunicar valor + CTA primário + um visual que prova que é real.
**Variantes:**
- *Split* — headline/CTA à esquerda, visual do produto à direita. Cavalo de batalha; mantenha o visual com cara de real.
- *Centered + canvas below* — headline/CTA centralizado, um screenshot/canvas grande do produto se estendendo
  por baixo. Forte quando o produto é visual.
- *Editorial* — hero conduzido por tipografia em tamanho exagerado, imagem mínima ou nenhuma, muito espaço. Para moods premium/minimal.
- *Interactive/live* — uma superfície de produto faux-live (UI animada ou estática "em uso"). Alto esforço, alto
  retorno para produtos técnicos.
**Sempre:** uma headline (o valor, não a categoria), uma linha de apoio, um CTA primário + secundário
opcional, e um visual crível ou uma escolha deliberada de não ter imagem. **Armadilha:** headline vaga
("The future of work"), tudo-centralizado por default, uma ilustração de banco de imagens que não diz nada.

### Social proof / logo wall
**Trabalho:** pegar confiança emprestada rápido. **Variantes:** faixa de logos em escala de cinza; "trusted by N teams"; uma única grande
métrica; um marquee. **Armadilha:** logos falsos apresentados como reais — use placeholders rotulados como substituíveis.

### Problem framing
**Trabalho:** fazer o visitante se sentir compreendido. **Variantes:** before/after; uma curta lista "soa familiar?";
um bloco de contraste (o jeito antigo vs o seu jeito). **Armadilha:** pular essa parte — soluções caem com mais força depois da dor.

### Feature blocks (the solution)
**Trabalho:** mostrar como você resolve. **Variantes:**
- *Alternating rows* — texto/visual, visual/texto, repetindo. Cada linha = um benefício real + um visual.
- *Bento grid* — tiles de tamanhos variados, cada um uma capacidade; ótimo para produtos "plataforma". Use conteúdo real,
  não três cards de ícone idênticos.
- *Tabbed/segmented* — um grande visual que troca por aba; bom quando as features compartilham uma superfície.
- *Spotlight* — uma feature carro-chefe ganha uma seção imersiva completa, as outras resumidas.
**Armadilha:** o clichê "3 colunas, ícone de linha, 4 palavras, blurb genérico." Se você precisar usar cards, faça-os
específicos e desiguais o bastante para parecerem autorais.

### How it works
**Trabalho:** fazer a adoção parecer sem esforço. **Variantes:** passos numerados (3–4 no máximo); um fluxo/diagrama conectado;
uma timeline curta. **Armadilha:** mais de 4 passos, ou passos que reafirmam features.

### Testimonials / case proof
**Trabalho:** humanos reais tiveram resultados reais. **Variantes:** cards de citação com rosto+nome+cargo; uma única citação
hero; um caso conduzido por estatística ("cortou o onboarding em 60%"). **Armadilha:** citações anônimas ou obviamente falsas.

### Pricing
**Trabalho:** remover a ambiguidade de custo. **Variantes:** 2–3 tiers com um em destaque; plano único + "talk to
us"; explicador baseado em uso. **Armadilha:** esconder o preço quando o público espera vê-lo; >3 tiers; checklists de feature
tão longos que intimidam.

### FAQ / objections
**Trabalho:** responder as 4–6 coisas que bloqueiam o cadastro (preço, segurança, migração, suporte, fit). **Variantes:**
accordion; Q/A em duas colunas. **Armadilha:** enrolação de marketing em vez da preocupação real.

### Final CTA
**Trabalho:** pedir mais uma vez, com confiança. **Variantes:** bloco de cor full-width; centralizado com um último ponto
de prova; um card focado. **Armadilha:** uma repetição fraca do hero. Faça parecer o fechamento.

### Nav & footer
**Nav:** logo, 3–5 links, um CTA primário; sticky e condensado no scroll. **Footer:** estrutura real
(product/company/resources/legal), não uma linha solitária de copyright.

## Copy patterns (write like a human)

**Fórmulas de headline** (escolha a que se encaixa; preencha com especificidades):
- *Outcome:* "Ship [outcome] without [pain]." → "Ship dashboards without a data team."
- *Category redefine:* "The [familiar thing], rebuilt for [shift]." → "Issue tracking, rebuilt for the
  AI era."
- *Direct value:* "[Verb] [valuable thing] [qualifier]." → "Turn support tickets into product insight."
- *Audience-named:* "For [audience] who [need]."

**Subheadline:** uma frase que diz *como* ou *para quem*, adicionando uma concretude que a headline não consegue.

**CTA copy:** específico para a ação — "Start building", "Get a demo", "Join the waitlist", "Deploy in
minutes". Nunca um "Submit"/"Sign up" pelado, a menos que o usuário insista.

**Lista anticlichê — não coloque isto no ar:**
- "Empower your workflow" / "Supercharge your productivity" / "synergy" / "seamless" (batido) /
  "next-generation" / "revolutionary" / "Powerful features for modern teams" / "Built for the way you
  work." Se uma frase poderia aparecer em qualquer site SaaS, troque por algo que só ESTE produto poderia dizer.

**Microcopy importa:** estados de botão, linhas de empty-state, dicas de tooltip, texto auxiliar de formulário — é aqui
que o capricho aparece. Gaste um pouco de cuidado aqui.

Leve as seções escolhidas para o build. Mapeie cada slot de imagem que você sugeriu aqui para o
**image-strategy.md**.
