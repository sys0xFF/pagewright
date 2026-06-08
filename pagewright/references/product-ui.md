# Product UI — construindo componentes que parecem reais, não genéricos

O jeito mais rápido de fazer uma landing page parecer entregue-por-um-time-sênior é ter uma **superfície de produto
fiel e feita à mão** (dashboard, tabela, gráfico, log, card) em HTML/CSS — veja image-strategy.md. Mas o jeito padrão
como o modelo constrói essas superfícies é **genérico e repetitivo**: um painel escuro, uma caixa com filete de 1px
fechada, uma pill de status, sombra suave, números em mono — o mesmo componente em toda página. Este arquivo corrige
isso. Ele é destilado de como times de produto realmente bons (Linear, Stripe, Attio, Retool, Vercel, Mercury, Sentry,
Raycast, …) constroem cada componente, lido direto dos screenshots reais deles.

**Como usar:** antes de construir qualquer product UI à mão, abra a seção correspondente abaixo E dê `Read` na
thumbnail de um exemplar citado — então construa naquele nível de acabamento, girando as *alavancas de variedade*
para que duas das suas páginas nunca entreguem o mesmo componente.

Regras transversais (valem para todo componente aqui):
- **Divisores, não caixas.** Separe superfícies por luminosidade + espaçamento + divisores de 1px ou um realce
  superior inset — não por uma caixa `border` completa com `rounded-xl` + `shadow-2xl` em volta de tudo.
- **Neutros tingidos**, nunca `#000`/`#fff` puros. As superfícies escalonam em luminosidade para serem lidas como painéis.
- **Racione o acento.** Um único ponto de status / um marcador — não acento em toda pill, linha e número.
- **Nada de monoespaçada decorativa — jamais.** Números, dados, células de tabela, legendas e rótulos usam a grotesca
  do corpo com `font-variant-numeric: tabular-nums`. Mono aparece SOMENTE dentro de um trecho literal de código/terminal.
- **Contenção.** Product UI de verdade é silencioso e denso de sinal. Rótulos pequenos de baixo contraste, dados com
  cara de reais, uma hierarquia clara — não um chrome berrante.

→ Volte para **[build-system.md](build-system.md)** para tokens/fontes, **[image-strategy.md](image-strategy.md)**
para construir-vs-fotografar, **[design-dna.md](design-dna.md)** para o vocabulário de tipo/cor.

---
## Dashboards e consoles de app (o product frame)

O "product frame" é a réplica embutida de um app shell — sidebar + conteúdo + (frequentemente) um trilho de detalhe. É o componente mais imitado numa página SaaS e o que mais entrega uma construção feita por IA, porque todo mundo recorre ao mesmo card escuro com uma caixa de filete em volta. Os melhores times de verdade tratam o frame como arquitetura: a *estrutura* (painéis, trilhos, breadcrumbs, densidade) faz o trabalho, e as bordas quase somem.

### O que os melhores sites de verdade fazem

- **A Linear constrói um shell de 3 painéis, não um card.** Sidebar (~240px) / lista de issues / trilho de detalhe, cada um uma *superfície separada* numa luminosidade ligeiramente diferente — as divisões são lidas como painéis, não como uma caixa só com linhas internas. O frame inteiro repousa num quase-preto `#08090A` (nunca `#000`), e a superfície do app é um passo mais clara (`~#0F1011`). A única "borda" que importa é um **realce superior inset de 1px** (`box-shadow: inset 0 1px 0 rgba(255,255,255,.04)`) que pega a luz como a borda de uma janela real — não existe caixa de 1px completa em volta do frame.
- **O chrome é breadcrumb e contagem, não decoração.** O cabeçalho da Linear carrega `02 / 145`, uma chave de issue `ENG-2703`, pequenos chevrons de navegação — orientação silenciosa em ~13px. Esse texto posicional é o que faz o componente ser lido como um app *real* no meio de uma tarefa, não como um mockup de marketing. Componha-o na grotesca do corpo com `tabular-nums`, nunca em mono.
- **A Attio prova a versão clara: divisores, não caixas.** O console dela é quase-branco, com seções de sidebar agrupadas e uma fileira de tabs separadas por **divisores de filete** únicos (`border-bottom`), zero contorno de card, espaço em branco generoso. A densidade vem de line-height apertado e rótulos pequenos, não de amontoar — contenção é a estética.
- **A tipografia da sidebar é pequena e de baixo contraste.** Rótulos de ~13px, ícones de ~16px, cabeçalhos de seção ("Workspace", "Favorites") num rótulo ainda menor, mais apagado e com leve tracking. A linha *ativa* ganha um preenchimento tingido sutil (`bg-white/[.06]`) e texto com tinta cheia; todo o resto fica em 60-70% de tinta. Sem cor de acento na navegação — o acento é racionado.
- **O acento é um único ponto, nunca uma inundação.** O índigo da Linear aparece só no ponto de status `In Progress` e num marcador de link inline — a pill principal "Sign up" é branca lisa. O status vive em pequenos pontos coloridos + um rótulo de texto, não em pills grandes preenchidas por toda parte.
- **A Basedash mostra o frame de data-viz: glow, números tabulares grandes, deltas minúsculos.** Barras multicoloridas vívidas sobre quase-preto, métricas de destaque como `4.3k` / `20.5k` grandes com um pequeno delta verde `+%` ao lado. Os números são o herói; o delta é discreto e pequeno. (De novo: grotesca real + `tabular-nums`, o verde é um estado semântico, não branding.)
- **A elevação é em camadas, não com glow por padrão.** A Linear flutua um card de agente secundário *acima* do frame, com sua própria sombra suave e uma affordance de fechar — a profundidade comunica "isto está em cima daquilo", e não é um drop-shadow uniforme em todo painel.

### A versão genérica a EVITAR

- O **único painel escuro com uma caixa de `border border-white/10` de 1px completa** e `rounded-xl`, um `shadow-2xl` suave, flutuando no centro. Uma superfície, uma borda, uma sombra — o frame-padrão de IA.
- **Monoespaçada por toda parte** para a chave de issue, contagens, células de tabela, timestamps e números de métrica como um sabor "técnico". Banido. É datado e é o sinal entregue.
- Um **acento violeta/índigo em tudo** — linha de navegação ativa, toda pill de status, a métrica, o botão — em vez de racioná-lo a um único ponto.
- **Densidade média uniforme**: toda linha com a mesma altura, mesmo `px-4 py-3`, um peso de texto, rótulos de contraste igual — sem hierarquia de sinal, então nada é lido como "o app está no meio de uma tarefa".

### Alavancas de variedade (gire-as para que duas construções não combinem)

- **Frame claro vs. escuro.** Attio-branco (divisores de filete, muito ar) vs. Linear-quase-preto (painéis em camadas, realce inset). Escolha pelo Design DNA, não por reflexo-escuro.
- **Estratégia de borda.** (a) *Sem bordas* — separe por luminosidade de superfície + espaçamento; (b) *só divisores* — linhas de 1px entre linhas/tabs, sem caixa externa; (c) *realce superior inset* — o truque da borda-de-janela. Evite a caixa contornada completa.
- **Quantidade de painéis e enquadramento.** Um painel de conteúdo / 2 painéis (nav + conteúdo) / 3 painéis (nav + lista + trilho de detalhe). Mais painéis = mais "app real", menos marketing.
- **Densidade.** Confortável (linhas ≥44px, estilo Attio) vs. compacta (linhas de 28-32px, estilo Linear). Compacta é lida como ferramenta de poder; confortável como app de consumo.
- **Racionamento de acento e elevação.** Um ponto de acento vs. um estado ativo de preenchimento tingido; painéis planos vs. um card de overlay flutuante com sua própria sombra vs. glow da Basedash apenas na data viz.

### Esboço copiável (estilo Linear de 3 painéis, sem mono decorativa)

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

Repare nos movimentos de acabamento: três superfícies em luminosidades diferentes (`#0F1011`, `#0B0C0D`) em vez de uma caixa; um **realce superior inset** como a única "borda de frame"; contagens, chaves de issue e timestamps na grotesca do corpo com `tabular-nums` (zero mono); navegação ativa como um **preenchimento tingido**, não uma cor de acento; e o índigo racionado a um **único ponto de status** no trilho. Troque por um frame branco com divisores de filete (Attio) ou por um glow + grade de métricas com números grandes (Basedash) quando o Design DNA pedir — mesma arquitetura, mostradores diferentes.

---

## Tabelas de dados, ledgers e listas

Uma tabela é o componente mais "padronizável" de product UI — que é exatamente por que uma genérica grita IA. A correção não é mais chrome; é *menos*, aplicado com intenção. Tabelas de produto de verdade são grades silenciosas que deixam o dado carregar o peso visual.

### O que os melhores sites de verdade fazem

- **A Attio descarta a caixa externa por completo.** Não há `border` em volta da tabela — a separação vem de uma pilha de filetes horizontais tênues (`~1px` a aproximadamente `4–6%` de tinta) entre as linhas e *nada* nas bordas esquerda/direita. A tabela é lida como parte da página, não como um card pousado sobre ela. A linha de cabeçalho tem a mesma largura das linhas do corpo, destacada só por uma régua inferior ligeiramente mais forte, nunca por uma barra de fundo cinza preenchida.
- **As linhas são curtas e o tipo é pequeno.** A Attio roda células do corpo em ~13–14px com altura de linha em torno de 36–40px; a célula principal (nome do registro) é a única com ícone/avatar, e é `font-weight: 500`, enquanto toda outra célula é `400`. Densidade é a estética — você deve ver 10+ linhas sem rolar.
- **O Outerbase (escuro, estilo planilha) merece suas linhas de grade.** Como é uma data grid de verdade, ele *de fato* mostra filetes verticais e horizontais — mas com contraste muito baixo contra uma superfície escura *tingida* (`~#16181d`, nunca `#000`). Combina isso com uma coluna líder de checkbox, cabeçalhos ordenáveis com um pequeno chevron que só aparece no hover/ativo, e uma affordance `Add row` fixada na toolbar. Os números (`open / high / low`) são alinhados à direita e tabulares.
- **O hover é um tingimento, não uma borda.** Em todas elas o estado de hover da linha é uma leve lavagem de fundo (um realce de 4–8% da superfície ou do acento), nunca um contorno colorido e nunca uma sombra. A seleção é um tingimento ligeiramente mais forte da *mesma* matiz mais uma barra de acento de `2px` na borda líder (estilo Outerbase), não um sinal só de checkbox.
- **Números são cidadãos de coluna, não bloco de código.** Colunas financeiras/de métrica são alinhadas à direita, usam `font-variant-numeric: tabular-nums` na *grotesca do corpo*, frequentemente com um glifo de unidade/moeda discreto num peso mais leve. Nada de monoespaçada, jamais — o alinhamento vem dos números tabulares, não de uma face de máquina de escrever.
- **O status é um ponto silencioso ou uma pill de baixa saturação.** A tendência atual (Linear, Geist, Attio) pende para um pequeno ponto preenchido de `6px` + rótulo, em vez de um badge preenchido berrante. Quando uma pill é usada, ela é *suave*: fundo tingido a ~12% da matiz com texto na saturação cheia, `border-radius` modesto (6–8px), sem borda. Uma cor de acento por tabela no total — contenção.
- **O cabeçalho é sussurrante.** Os rótulos de coluna têm `12–13px`, frequentemente `font-weight: 500`, muitas vezes no foreground apagado (não tinta cheia), ocasionalmente com um fio de `letter-spacing` — mas **não** maiúsculas-espalhadas, o que hoje soa datado.

### A versão genérica a EVITAR

- Uma tabela totalmente encaixotada: `border border-white/10 rounded-xl` envolvendo tudo, com uma barra de cabeçalho `bg-white/5` preenchida e `divide-y divide-white/10` entre toda linha — a "gaiola de filete no painel escuro".
- Uma fonte monoespaçada em todo número, ID, timestamp ou valor com cara de código "para parecer técnico". Banido. Use tabular-nums na fonte do corpo no lugar.
- Uma pill de status berrante na coluna mais à direita (`bg-green-500/20 text-green-400 border border-green-500/30 rounded-full`) em *toda* linha, transformando a tabela numa fileira de luzes de Natal.
- Padding idêntico por toda parte (`px-4 py-3`) com um drop-shadow suave sob o card — plano, uniforme e instantaneamente reconhecível como template.

### Alavancas de variedade (gire-as para que duas construções não combinem)

1. **Estratégia de borda** — sem-borda-com-filetes (Attio), grade tênue completa (data grid do Outerbase), ou sombra-como-divisor onde as linhas repousam em tingimentos de superfície sutilmente alternados e a única linha é sob o cabeçalho. Escolha *uma* por construção.
2. **Densidade** — confortável (linhas de 44–48px, para um ledger curto) vs. compacta (32–36px, quando o ponto é mostrar volume). Defina altura de linha e tamanho de fonte juntos, não misture.
3. **Temperatura de superfície e elevação** — plano-na-página (sem card) vs. painel inset (a tabela fica num poço recuado, `bg` um passo mais *escuro* que a página, realce superior inset) vs. card elevado. Poços inset parecem atuais; cards elevados parecem 2021.
4. **Papel do acento** — acento na barra de seleção, OU numa única célula de sparkline/tendência, OU numa matiz de status — nunca os três. Decida o *único* lugar onde a cor é permitida.
5. **Enquadramento da coluna líder** — ícone+nome (cara de CRM/lista), checkbox+id (cara de data-grid), ou número-de-rank (cara de leaderboard/ledger). Essa escolha única muda toda a personalidade.

### Esboço copiável (ledger de filetes sem borda, escuro, números tabulares, sem mono)

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

Notas sobre o esboço: sem caixa envolvente, sem gaiola de `divide-y`, sem sombra de card — a estrutura é filetes + uma única régua de cabeçalho. Os números usam `tabular-nums` na grotesca do corpo (sem monoespaçada). A cor é racionada: pontos de status são as únicas matizes, ganhos usam um esmeralda dessaturado, e o único acento (`sky`) aparece *apenas* no tingimento e na barra de borda de `2px` da linha selecionada. Para fazer uma segunda tabela diferente, vire uma alavanca — por exemplo, mude para uma data grid densa de 32px *com* linhas verticais tênues e uma coluna líder de checkbox, ou inverta para uma superfície clara plana — em vez de reusar exatamente este visual.

---

## Gráficos e data-viz (linha, barra, funil, cohort, sparkline)

Gráficos são onde a UI padrão de IA se entrega mais rápido: um canvas encaixotado, quatro gridlines, um eixo x/y completo, uma linha de acento com glow, e um tooltip que ninguém estilizou. Times de produto de verdade tratam um gráfico como *tipografia com uma forma dentro* — o número é o herói, a linha é coadjuvante, as gridlines quase somem. Estude como as referências resolvem o mesmo trabalho de formas tão diferentes: o funil da Mixpanel é só barras lilás suaves + porcentagens empilhadas sem moldura; a spark de "Activation" da Steep é uma única linha fina cor de carvão com um ponto na ponta e um `46.2%` gigante embaixo; a Graphy vai no caminho oposto com barras 3D brilhantes e arredondadas; a PostHog fica plana e utilitária. Nenhuma delas parece o mesmo template.

### O que os melhores sites de verdade fazem

- **O número lidera, o gráfico apoia.** O card de ativação da Steep coloca uma figura grande `46.2%` diretamente *embaixo* de uma sparkline minúscula — a viz existe para dar uma forma ao número, não o contrário. Cards de KPI emparelham uma figura tabular grande com um pequeno delta com sinal (`↑ 5.5% vs last week`), onde o delta é o único elemento colorido do card.
- **Mate os eixos e a caixa.** Sparklines e gráficos de destaque saem com *nenhum* eixo y, sem borda de gráfico, e frequentemente sem rótulos de eixo x — só a linha e talvez uma linha de base tênue. O fragmento de gráfico da Steep tem zero gridlines. Quando um eixo é necessário, é 1px a ~8–10% de tinta, situado *sob* o plot, nunca um retângulo completo em volta.
- **Gridlines são a camada mais silenciosa ou ausente.** Se presentes, só horizontais, 1px, tracejadas ou sólidas em aproximadamente a opacidade de `border` (6–10% de tinta), e nunca verticais. A linha de dados é em força total; a grade é quase imperceptível. Hierarquia = linha ≫ eixo ≫ grade.
- **O preenchimento de área é um fade, não uma inundação.** Gráficos de linha usam um gradiente vertical sob a curva de ~14% de acento no topo a 0% na linha de base (Tremor/shadcn fazem exatamente isso). O traço é 1.5–2px; o preenchimento é um sussurro. Nada de bloco sólido de acento.
- **Funis são barras empilhadas + porcentagens empilhadas, sem andaime.** O funil da Mixpanel são barras horizontais em degraus, em lilás suave, com a conversão de cada passo `82.4% → 61.8% → 41.6%` posta logo abaixo, um total `Overall`, e conectores pontilhados tênues de queda entre passos — pousados sobre branco com uma sombra suave, não dentro de uma grade de gráfico.
- **Cohort/retenção = um heatmap tingido, não uma tabela de dígitos.** O *fundo* de cada célula carrega o valor (a saturação do acento codifica a magnitude), então o olho lê o gradiente antes de qualquer número. Os números são pequenos, tabulares e centrados; a cor faz o trabalho.
- **Um acento, contido; categorias via degraus neutros.** Uma única linha ou barra ganha o acento da marca. Gráficos multi-séries percorrem *tons de uma matiz* ou uma rampa neutra apagada — não um arco-íris. O coral da Steep, o lilás da Mixpanel: uma família.
- **Sparklines arredondam suas pontas e marcam o endpoint.** Um `stroke-linecap="round"`, um único ponto preenchido no último ponto (Steep), e a coisa toda do tamanho de uma palavra — ela vive dentro de um card ou ao lado de um número, nunca emoldurada.

### A versão genérica a EVITAR

- Um `<div>` com uma borda de filete de 1px, uma sombra suave, uma grade tracejada de 4 linhas, um eixo x **e** y completos, e uma linha índigo com glow em saturação cheia — o gráfico "de todo dashboard".
- Números e ticks de eixo postos em monoespaçada para uma cara de "dado". **Banido** — use a grotesca do corpo com `tabular-nums`.
- Um preenchimento de área de acento sólido (bloco plano de cor) sob a linha, mais uma pill de status flutuando no canto porque o painel pareceu vazio.
- Multi-séries arco-íris (índigo/verde/laranja/vermelho) onde cada série briga por atenção; pontos de legenda numa fileira de que ninguém precisa.

### Alavancas de variedade (gire-as para que duas construções difiram)

- **Proporção número/gráfico** — liderado-por-KPI (figura gigante, sparkline como guarnição, Steep) ↔ liderado-por-gráfico (o plot preenche o card, o número é uma legenda). Escolha um por superfície.
- **Estratégia de grade e eixo** — nenhuma (sparkline pura) ↔ só linha de base ↔ grade horizontal tênue ↔ eixo rotulado. Ir mais leve é lido como mais premium; ir mais cheio é lido como mais "ferramenta de analista" (PostHog).
- **Preenchimento e traço** — linha plana de 1px / sem preenchimento ↔ linha de 2px + fade em gradiente ↔ barras arredondadas brilhantes com glow suave (Graphy). Esse mostrador único oscila utilitário↔expressivo.
- **Codificação para categorias** — acento único + rampa neutra ↔ tons monocromáticos da matiz da marca ↔ células tingidas de heatmap (cohort). Nunca caia no padrão de um arco-íris categórico.
- **Enquadramento** — sem borda em superfície tingida ↔ só borda *superior* inset de 1px (estilo Linear, divisor não caixa) ↔ card flutuante com sombra suave (Mixpanel). O contêiner diz tanto quanto o gráfico.

### Esboço copiável — card de linha de KPI com fade em gradiente + heatmap de cohort

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

O card inteiro tem um acento (`#E07856`), figuras tabulares por toda parte via `font-feature-settings:'tnum'`, sem borda de gráfico, sem gridlines além de uma linha de base a 6% de tinta, um preenchimento em fade em vez de inundação, e uma grade de cohort onde a *cor* — não os dígitos — carrega a tendência. Para re-skin: descarte o preenchimento de área e vá para linha plana de 1px para uma leitura utilitária da PostHog, adicione um contêiner só-com-borda-superior-inset para uma leitura Linear, ou arredonde as barras e adicione um glow suave para uma leitura Graphy.

---

## Cards — pricing, stat, feature, product

Cards são onde o "painel padrão de IA" é mais visível: uma caixa, uma borda, uma pill, uma sombra suave, repetir. Os melhores times quase nunca entregam isso. Eles escolhem *uma* estratégia de superfície por página e comprometem-se com ela, depois carregam o sinal em espaçamento, peso e formatação de número — não em chrome.

### O que os melhores sites de verdade fazem

- **Linear: o card é uma "janela", não uma "caixa".** No canvas quase-preto (`#08090A`, nunca `#000`) os painéis de produto são lidos como uma superfície contínua única separada por um único **filete de 1px em `rgba(255,255,255,0.06–0.08)`**, frequentemente como uma *borda superior inset ou divisor* em vez de uma caixa completa de 4 lados. A elevação é um realce tênue de borda superior (`inset 0 1px 0 rgba(255,255,255,.04)`), não um drop shadow. O acento índigo aparece só como um **ponto de status** de 6–8px, nunca como preenchimento ou borda de card.
- **Stripe: claro, editorial, quase sem borda.** Cards de feature/stat ficam sobre branco com **nenhuma borda visível** — a separação vem de espaço em branco generoso e um título quase-preto (`#0A2540`) sobre um corpo ardósia apagado (`#425466`). Quando uma superfície é necessária, é um preenchimento `#F6F9FC` levemente tingido com raio ~`8px`, não um traço. A hierarquia dentro de um card longo é feita por *tinta de dois tons* (linha de promessa escura, linha de apoio em ardósia), exatamente como o H1 deles.
- **Vercel / Geist: minimalismo estrutural.** Cards são branco-sobre-branco (ou `#FAFAFA` elevado) com uma única **borda `1px` `#EAEAEA`** e raio apertado (`6–8px`). O movimento definidor é *a própria grade* — os cards se alinham a gridlines tênues visíveis e ticks de canto, então o layout é lido como engenheirado. Números e rótulos são a **grotesca do corpo com `tabular-nums`**, nunca uma face de código. CTAs dentro de cards são pills preto-sólido ou contorno-filete, alto contraste, pequenos.
- **Raycast: cards escuros que merecem sua elevação.** As superfícies são um fio mais claras que a página (`#0F0F12` sobre `#0A0A0C`), separadas por **degrau tonal, não traço**. Um único acento de marca (o vermelho deles) é racionado a um elemento por card — um tile de ícone ou um glow no hover — e o resto fica neutro. O raio de canto é generoso (`12–16px`) para parecer app.
- **Pricing especificamente:** o tier recomendado é distinguido por **uma** alavanca, não três. Pricing da classe Linear/Stripe promove um tier com um tingimento sutil ou uma borda ligeiramente mais forte — *não* borda + sombra + glow + scale-up + faixa tudo de uma vez. O preço é posto grande na grotesca com `tabular-nums` e um `/mo` alinhado à base em tinta apagada; os checks de feature são silenciosos (um glifo de check fino em acento-ou-apagado, nunca um círculo verde preenchido).
- **Acabamento de número por toda parte:** toda figura usa `font-variant-numeric: tabular-nums` para que colunas e preços empilhados se alinhem. Moeda, decimais e unidades são des-enfatizados (cor apagada, tamanho menor) para que a magnitude seja lida primeiro. Sem monoespaçada — a grotesca carrega o dado.

### A versão genérica a EVITAR

- O **"kit de painel escuro"**: `bg-neutral-900 + rounded-2xl + border border-white/10 + shadow-lg`, aplicado identicamente a todo tipo de card na página.
- Uma **pill de status em tudo** (chip rounded-full preenchido com ponto) usada como decoração em vez de transmitir estado real.
- **Monoespaçada para o número/preço/rótulo** para parecer "técnico" — banido. É lido como datado e padrão de IA.
- **Pistas de elevação empilhadas**: borda *e* sombra *e* glow *e* um tingimento, de modo que nada é de fato enfatizado e todo card grita igualmente.

### Alavancas de variedade (gire-as para que duas construções não combinem)

1. **Estratégia de superfície — escolha UMA por página:** (a) traço-de-filete (Vercel/Linear), (b) degrau-tonal / sem borda (Raycast), ou (c) sem-borda-no-espaço-em-branco (Stripe). Nunca misture as três.
2. **Meio de separação:** borda inset de 1px vs. uma única linha divisória vs. espaçamento puro vs. um tingimento de fundo de um passo. Mudar só isto re-skinia a grade inteira.
3. **Densidade:** editorial (padding de 28–32px, muito ar, Stripe) vs. compacta (padding de 16–20px, densa, product UI da Linear). Defina uma vez e mantenha.
4. **Racionamento de acento:** acento como um ponto de status de 6px · como um único tile de ícone · como o tingimento do tier recomendado · como um glow só no hover. Use exatamente um modo.
5. **Pareamento raio + elevação:** plano apertado de `6–8px` (engenheirado) vs. generoso de `12–16px` com um realce superior tênue (app). Raio e elevação devem concordar.

### Esboço copiável — trio de pricing, superfície de filete, acento como contenção

Superfície escura de neutro tingido, separação por borda inset de 1px + tingimento tonal de um passo no tier recomendado, acento (teal) racionado ao ponto, ao glifo de check e ao botão ativo. Todas as figuras usam `tabular-nums`. Nada de mono em lugar nenhum.

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

Por que não é lido como padrão de IA: a separação é um único `gap-px` sobre uma camada de linha tingida (um sistema de filete, sem caixas por card), o tier recomendado é promovido por **uma** alavanca (um tingimento de fundo de um passo mais o ponto de acento — sem pilha de sombra/glow/scale), o acento é racionado a três pontos precisos, e toda figura é a grotesca com `tabular-nums` para que `$0 / $24 / $96` se alinhem opticamente. Para re-skin para uma construção diferente, vire a estratégia de superfície (troque a camada de linha `gap-px` por sem-borda-no-espaço-em-branco, ou por um degrau-tonal sem borda) e a densidade (baixe o padding para `p-5`) — mesma marcação, um sistema de card visivelmente diferente.

---

## Feeds de atividade, logs, streams e timelines

Este componente é uma lista vertical de eventos ao longo do tempo: um feed de atividade, um audit log, um stream de deploy, uma thread de comentários, um trace de raciocínio. O modo de falha é tratar todo evento como um card totalmente bordeado. Ferramentas de verdade tratam o feed como uma *coluna silenciosa de texto* e gastam todo o orçamento de detalhe na borda esquerda (ícone/ponto/trilho) e na formatação de tempo.

### O que os melhores sites de verdade fazem

- **A linha não é uma caixa — ela pende de uma coluna à esquerda.** O trace de raciocínio "Root Cause" do Sentry dá a cada passo um pequeno glifo líder numa calha de ícone fixa e então apenas faz o texto correr; não há borda por linha, nem card por linha, nem sombra. O feed de comentários do Liveblocks faz o mesmo com uma calha de avatar. A lista é lida como uma superfície, não quinze painéis empilhados. A separação vem do line-height e da coluna de ícone, não de 15 caixas de filete.
- **Timestamps são des-enfatizados e geralmente relativos.** O Liveblocks mostra `now` e `5m ago` em cinza apagado no mesmo tamanho dos metadados, nunca em negrito, nunca colorido. Use tempo relativo para eventos recentes (`now`, `2m`, `1h`) e reserve timestamps absolutos (`14:02:31`) para logs de verdade — e quando você mostrar um horário de relógio, componha-o na grotesca do corpo com `tabular-nums`, apagado, para que a coluna fique alinhada verticalmente sem gritar.
- **Nível/severidade é um pequeno token de cor, não uma pill grande.** A tabela de log da Better Stack marca o nível com um pequeno ponto colorido ou uma única palavra de cor apagada (`ERROR` num vermelho dessaturado), inline, ~11–12px. Ela não envolve toda linha num badge de status preenchido. A cor é a *única* coisa berrante e tem 6px de largura. O Datadog igualmente usa cor puramente como codificação de dado (KPIs vermelho/laranja/verde), nunca como decoração.
- **A densidade é real e intencional.** A visão de log da Better Stack empacota linhas a ~28–32px de altura com texto de ~13px e tracking apertado — dezenas de linhas visíveis de uma vez. Um log que respira como um card de marketing está errado. Aperte o `leading`, baixe o padding vertical para `py-1.5`/`py-2`, e deixe o volume de linhas ser a textura.
- **Um conector implica sequência; um glifo implica tipo.** O Sentry roda linhas-guia horizontais tênues saindo de cada passo de raciocínio (e uma espinha vertical faria o mesmo trabalho numa timeline). Para uma *timeline*, desenhe um trilho vertical de 1px contínuo atrás da calha de ícone e deixe os pontos repousarem nele — a linha é a estrutura, então linhas individuais não precisam de bordas.
- **As superfícies são tingidas, o acento é racionado.** O painel do Sentry é um ameixa escuro quente (não `#000`); o passo ativo/importante ganha o único tratamento de acento (um link mais brilhante, um ponto preenchido) enquanto toda outra linha fica neutra. Um acento por tela, aplicado à coisa que importa (o erro, o passo atual, o item não lido).
- **Números e contagens usam figuras tabulares na face do corpo.** Contagens de reação, durações (`128ms`), tamanhos de byte, contagens de tentativa — todos grotesca + `tabular-nums`, nunca uma face monoespaçada. Eles se alinham na coluna por causa da variante numérica, não por causa de uma fonte de máquina de escrever.

### A versão genérica a EVITAR

- Todo evento envolto no seu próprio card `rounded-xl border border-white/10 bg-zinc-900 p-4 shadow-sm`, empilhado com `gap-4` — quinze painéis flutuantes idênticos em vez de uma coluna densa.
- Uma **pill** de status preenchida (`rounded-full bg-…/15 px-2 py-0.5`) em toda e cada linha para o nível/tipo, fazendo a severidade gritar em linhas que são rotineiras.
- Timestamps renderizados numa face **monoespaçada** (ou como um chip colorido em negrito) para parecer "técnico" — banido. É o sinal de log padrão de IA.
- Padding médio uniforme (`p-4`), `leading-relaxed` generoso, e um divisor de filete entre toda linha — o resultado respira como uma lista de blog, não um stream, e só ~6 eventos cabem na tela.

### Alavancas de variedade

Gire ao menos duas destas para que dois feeds não pareçam o mesmo template:

- **Pista de estrutura:** lista com calha de ícone (sem trilho) · espinha vertical única com pontos (timeline) · agrupado-por-dia com cabeçalhos de data sticky · tabela de log densa plana com colunas. Escolha uma por construção.
- **Densidade:** feed de atividade confortável (`py-3`, 14px, tempo relativo) vs. log forense (`py-1.5`, 13px, relógio `tabular-nums` absoluto, monocromático).
- **Estratégia de borda:** zero bordas por linha (separação por ritmo) · uma única borda superior inset por linha (estilo Linear, `border-t border-white/5`) · tingimento de linha alternado (`even:bg-white/[0.02]`) — nunca caixas completas.
- **Expressão de severidade:** ponto líder de 6px · uma palavra colorida apagada · uma borda de acento esquerda de 2px na linha · colorir só o ícone. Não combine mais de uma.
- **Formato de tempo e enquadramento:** relativo (`2m ago`) para social/atividade · relógio monotônico absoluto para logs · deltas de duração (`+340ms`) para traces. A escolha sinaliza que tipo de stream é este.

### Esboço copiável

Um feed de atividade de deploy / sistema: lista com calha de ícone, sem caixas por linha, uma espinha tênue, um acento no item ativo, superfície de neutro tingido, tempo relativo em figuras tabulares apagadas.

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

Notas sobre por que isto evita o padrão: não há cards ou divisores por linha — a **espinha** carrega a estrutura; a severidade é um ponto de 6px mais uma palavra apagada, não um badge preenchido; toda figura (`8.4s`, `3,182`, `12m`) é a face de corpo grotesca com `tabular-nums`, sem mono em lugar nenhum; a superfície é um `#16151c` quente em vez de preto puro; e exatamente uma linha merece o acento (o deploy ao vivo). Para re-rolar o visual, troque a espinha por linhas `even:bg-white/[0.02]`, mude o tempo relativo para um relógio `tabular-nums` absoluto, e aperte para `py-1.5` para uma cara de log forense.

---

## Navigation — headers, sidebars, tabs

### O que os melhores sites de verdade fazem

- **A top-nav de marketing é leve como pena, não uma "barra".** Vercel, Linear, Framer e Stripe todos rodam o logo + 5–6 itens de link + 1–2 ações do lado direito a ~13px, peso médio (500), numa tinta apagada (~70% da cor do corpo), com letter-spacing-0 generoso e gaps de ~24–28px. **Não há contêiner visível** — sem borda, sem preenchimento, sem sombra. A nav apenas flutua sobre o fundo da página. O único chrome é a pill de sign-up à direita (pill branca/preta na Vercel, Linear, Framer; o azul-de-marca sólido na Stripe). Contenção é o visual.
- **O botão pill é o elemento mais berrante, e é minúsculo.** Na Linear e Framer a ação principal de nav é uma pequena pill branca (~32px de altura, ~14–16px de padding horizontal, totalmente arredondada), e o *secundário* "Log in" é texto liso sem nenhuma borda. A Vercel entrega uma pill preta + uma pill ghost contornada "Log In". A hierarquia é pill > ghost > link de texto liso — nunca dois botões preenchidos.
- **Nav de sidebar in-product = linhas densas, planas e tingidas.** A sidebar de app da Linear empacota linhas a ~28–30px de altura, rótulo de ~13px, com um ícone líder de 16px e um gap de ~8px ícone-para-rótulo. **Não há bordas de linha nem divisores** — as seções (Workspace, Favorites) são separadas por um rótulo de seção em maiúsculas de 11px, cinza de baixo contraste, e só espaço em branco. A linha ativa é um **preenchimento tingido sutil** (alguns % de branco sobre o canvas escuro, raio de ~6px) — não uma barra de acento, não um fundo colorido. O hover é uma versão ainda mais tênue do mesmo preenchimento.
- **Divisores de cabeçalho são filetes inset ou sombras, não caixas completas.** A top bar in-app da Linear se separa do conteúdo com uma única borda inferior **inset** de 1px num tingimento quase imperceptível (algo como `rgba(255,255,255,0.06)`), parando nas bordas do conteúdo — é lida como uma costura, não uma moldura. Onde um divisor pareceria pesado, os melhores times trocam a linha de 1px por uma **sombra translúcida de 1px** para que a borda seja sentida, não desenhada.
- **Tabs são lideradas por sublinhado, baixo contraste, contagens tabulares.** O cabeçalho de issue da Linear mostra chrome de tab/breadcrumb onde o item ativo é tinta cheia e os itens inativos caem para ~50% de cinza; contagens como `02 / 145` ficam na grotesca do corpo com `tabular-nums`, nunca numa pill e nunca em mono. O marcador de tab ativa é um sublinhado de 2px da largura do *rótulo* (inset), não uma barra de largura completa.
- **O acento é reservado para estado, não para navegação.** O índigo da Linear nunca colore um item de nav — ele só aparece num ponto de status ou num chip "In Progress" dentro do conteúdo. A seleção de nav é comunicada por contraste de tinta + um preenchimento tingido neutro. A Stripe é a exceção que confirma a regra: o acento dela é um azul-de-marca de marketing só no CTA, enquanto os links de nav ficam quase-pretos.

### A versão genérica a EVITAR

- A sidebar **"painel escuro + caixa de filete de 1px"**: toda região de nav envolta em `border border-white/10 rounded-xl bg-zinc-900` com um `shadow-lg`. Sidebars de verdade *não têm borda nem sombra* — são superfícies planas definidas por tingimento e espaçamento.
- O **estado ativo de barra-de-acento**: uma borda esquerda colorida de 3px (geralmente índigo/violeta) mais um texto colorido e um tingimento de fundo colorido, tudo de uma vez. Os melhores times escolhem *um* sinal neutro (um preenchimento tênue) e deixam o contraste de tinta fazer o resto.
- **Pills para tudo**: contagens de nav, rótulos de tab e cabeçalhos de seção todos enfiados em pills de status bordeadas. Contagens pertencem inline com `tabular-nums`; seções pertencem como rótulos maiúsculos silenciosos.
- **Chrome de UI em mono**: eyebrows monoespaçadas, contagens de nav em mono, separadores de breadcrumb em mono "para parecer uma dev tool". Banido — use a grotesca com `tabular-nums` para qualquer figura.

### Alavancas de variedade (para que duas construções não pareçam idênticas)

1. **Estratégia de borda:** (a) nenhuma borda, seleção por preenchimento tingido (Linear); (b) uma única costura de filete inset só sob o cabeçalho; (c) sombra-como-divisor (sombra translúcida de 1px, zero linha desenhada). Escolha uma — nunca empilhe as três.
2. **Densidade:** confortável (~36px de linha, rótulos de 14px, cara de marketing) vs. densa (~28px de linha, rótulos de 13px, cara de app). Reduza pela metade ou dobre o padding da linha e todo o componente muda de caráter.
3. **Sinal de estado ativo:** bloco de preenchimento tingido · sublinhado inset de 2px · só contraste tinta-cheia-vs-apagado · ícone líder troca de linha para preenchido. Escolha exatamente um como primário.
4. **Enquadramento:** chrome flutuante sobre o bg da página (sem contêiner) vs. uma superfície de trilho tingido (`bg-white/[0.02]`) que é um tom fora do canvas sem borda. O trilho é lido como mais "app", o flutuante como mais "marketing".
5. **Disciplina de acento:** mantenha o acento totalmente fora da nav (seleção neutra) — *ou* permita-o em exatamente um elemento (um único ponto de status, ou a pill de CTA), nunca no texto do link e na linha ativa ao mesmo tempo.

### Esboço copiável (HTML + Tailwind)

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

Notas sobre o esboço: o canvas é um quase-preto tingido (`#0B0C0E`, não `#000`); a sidebar carrega **nenhuma borda e nenhuma sombra** — é um trilho plano `bg-white/[0.015]` com a seleção mostrada por um preenchimento tingido tênue. O cabeçalho é uma única costura de filete inset, as tabs usam um sublinhado inset de 2px, e toda figura (`12`, `02 / 145`, `8`) é a grotesca do corpo com `tabular-nums` — sem mono em lugar nenhum, sem acento na navegação.

---

## Superfícies de código, terminal e API

Isto cobre snippets de instalação, blocos de terminal, amostras de código, painéis de request/response e linhas de referência de API — os componentes que *contêm* mono, mas não devem *ser* estilizados por ele.

### O que os melhores sites de verdade fazem

- **O snippet é uma superfície tingida, não uma caixa preta.** No `bun.sh` o bloco de instalação fica num painel só alguns por cento mais claro que a página (um neutro estilo `#16161a` sobre uma página quase-preta), raio ~10-12px, com uma barra de chrome de verdade no topo carregando **tabs de SO** ("Linux & macOS" / "Windows") e um link "View install script". O código em si é uma linha silenciosa; o *frame* carrega a estrutura. Não se apoie numa borda de 1px para definir o bloco — o degrau de superfície faz isso.
- **O comando tem um glifo de prompt, e o glifo é apagado.** O `bun.sh` escreve `$ curl -fSSL https://bun.sh/install | bash` — o `$` é um neutro de baixo contraste, o comando é quase-branco, e esse único degrau de contraste é lido como "terminal" muito melhor que qualquer skin de verde-no-preto. O ícone de copiar fica no topo à direita, estilo ghost, ganhando contraste só no hover.
- **O acento é um único realce, nunca uma lavagem.** O painel de benchmark do `bun.sh` colore *apenas* a barra "Bun" de rosa; toda barra de concorrente é cinza. A tab de SO ativa ganha o mesmo sublinhado/preenchimento rosa. Um elemento é quente, todo o resto é neutro — é assim que uma superfície de produto sinaliza "esta é a resposta" sem gritar.
- **Números em UI adjacente a código são grotesca do corpo com figuras tabulares, alinhados à direita.** Os tempos de benchmark (`269.1 ms`, `494.9 ms`, `1,608 ms`, `2,137 ms`) e legendas de versão (`v1.3.14`) NÃO são mono — são a mesma sans que todo o resto, alinhadas à direita na coluna para que os pontos decimais empilhem. A unidade (`ms`) é destacada num peso apagado. Esta é a regra: dados perto de código ainda usam a grotesca + `tabular-nums`.
- **O chrome de docs/API é leve de filete e levantado por sombra, não encaixotado.** A janela de docs embutida do `readme.com` usa divisores tênues entre a árvore de sidebar, a toolbar (`Guides · Recipes · API Reference · Changelog`) e o conteúdo; a janela inteira é separada do hero escuro por uma **drop shadow suave + raio**, não por um contorno pesado. O campo de busca mostra um chip de dica `⌘K` inset à direita.
- **Semântica de método/status vem de pills tingidas, não de cor crua.** Linhas de API são lidas melhor com uma pequena tag de método em maiúsculas sobre um fundo *tingido* que combina com sua família de matiz (GET → tingimento teal/azul apagado, POST → tingimento verde apagado, DELETE → tingimento vermelho apagado), baixa saturação, texto escuro sobre tingimento claro. O caminho do endpoint é a grotesca, com só os segmentos `:id` apagados — nunca o caminho inteiro em mono-como-decoração.
- **Contenção da Vercel/Geist como o teto da elevação.** A Vercel mantém essas superfícies quase-planas e quase-monocromáticas; se você adiciona um glow, é um brilho tênue de borda superior, não um halo colorido. Na dúvida, mais plano e mais silencioso vence.

### A versão genérica a EVITAR

- A **caixa preta com o trio de pontos "semáforos do mac"** vermelho/amarelo/verde no canto — é o padrão de IA mais sobre-usado para "isto é código". Pule isso a menos que o design genuinamente queira uma metáfora de janela de SO; mesmo então, prefira *tabs* de SO (bun) a pontos decorativos.
- **Mono vazando do snippet** para o rótulo de nome de arquivo, os números de linha, o status "200 OK", o tooltip de copiar, ou as figuras de benchmark. Mono é permitido *só dentro do texto literal de código/terminal*. Todo o resto é a grotesca.
- **Syntax highlighting neon** (keywords magenta brilhante, strings lima) sobre `#000` puro. Blocos de código de produto de verdade usam uma paleta de token de neutro-tingido de baixo contraste — a maioria dos tokens perto do mesmo valor, um ou dois suavemente diferenciados.
- O tratamento de **retângulo de filete de 1px + sombra suave + uma pill de status** aplicado identicamente ao snippet, ao painel de response e à linha de API, para que os três pareçam o mesmo card vazio.

### Alavancas de variedade

Gire ao menos duas destas para que duas construções não rimem:

- **Enquadramento** — snippet nu rente (só um botão de copiar, sem chrome) vs. painel com tabs no topo (tabs de SO/linguagem) vs. janela de docs completa com sidebar. bun e readme ficam em extremos opostos deste mostrador.
- **Estratégia de borda** — só degrau de superfície (o tingimento define a borda), vs. filete inset único, vs. lift por sombra sem borda. Não combine as três.
- **Prompt e calha** — estilo de terminal com prompt `$`, vs. calha de fonte com numeração de linha, vs. sem calha nenhuma. Escolha uma identidade por bloco.
- **Papel do acento** — acento na tab ativa, OU no estado de cópia-com-sucesso, OU numa linha/barra realçada — não tudo de uma vez.
- **Densidade** — uma única linha de instalação de destaque (solta, padding generoso) vs. uma tabela de API densa multi-linha (linhas apertadas de 36-40px, divisores de filete). Combine a densidade a se a superfície é uma vitrine ou uma referência.

### Esboço copiável

Um painel de instalação com tabs no topo ao lado de uma leitura de benchmark — superfície tingida, glifo de prompt apagado, realce de acento único, figuras tabulares na grotesca (sem mono decorativa fora do snippet).

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

Para uma **linha de referência de API**, reuse a mesma superfície e troque o corpo: uma pill de método tingida em maiúsculas (`text-[11px] font-semibold tracking-wide` sobre `bg-emerald-400/10 text-emerald-300` para POST), o caminho na grotesca com os segmentos `:id` em `text-stone-500`, e uma figura de latência/versão `tabular-nums` alinhada à direita — nunca a linha inteira em mono.

---

## Formulários, inputs, busca e command palettes

Inputs são onde a product UI padrão de IA é mais obviamente falsa. Apps de verdade tratam o input como um *contêiner silencioso que ganha vida no foco* e tratam o command palette (⌘K) como uma superfície de primeira classe, não como uma caixa de busca com uma lupa. Estude os screenshots: o launcher do Raycast, o `⌘K` e a busca-em-painel da Linear, os campos de auth empilhados do Cal.com, o card de sign-in pixel-perfect do Clerk. Nenhum deles parece o genérico "painel escuro + pill + caixa de 1px" que a skill emite atualmente.

### O que os melhores sites de verdade fazem

- **O input em repouso é quase invisível; o foco faz o trabalho.** Linear e Raycast definem um campo em repouso numa superfície apenas levemente elevada (`raised` sobre `surface`, ~6-8% de realce de luminância) com uma borda de *filete* — às vezes nenhuma borda, só o preenchimento. Toda a expressão vive no **estado de foco**: a borda muda para um neutro mais claro ou um acento de baixa saturação e um anel suave de 2-3px aparece (`ring-2 ring-accent/15`, não um halo gordo com glow de 4px). Em repouso, sinal desligado; no foco, sinal ligado.
- **Busca ≠ uma caixa bordeada com uma lupa centrada.** O launcher do Raycast e o `⌘K` da Linear são *inputs sem borda* situados no topo de um painel flutuante, com o ícone alinhado à esquerda e pequeno (14-16px, `muted` não `ink`), placeholder em `faint`, e um keycap `⌘K` / `Esc` fixado à direita. O campo de busca e seus resultados são **uma superfície contínua separada por um divisor inset**, não dois cards empilhados. A linha de query manda no topo; os resultados fluem abaixo dela dentro da mesma casca arredondada.
- **Linhas de command-palette são densas, com ícones, e keyboard-first.** Cada linha tem ~36-40px de altura: um ícone líder de 16px, um rótulo a 13-14px médio, um grupo/breadcrumb opcional apagado à direita, e uma dica de teclado. A linha *ativa* é um preenchimento tingido de largura completa (`raised`/`accent-tint`) com cantos arredondados inset ~4px da borda do painel — a seleção é um bloco preenchido, nunca um sublinhado ou uma faixa de borda esquerda. Um pequeno rótulo de grupo ("Recent", "Navigation") numa legenda quase-maiúscula `faint` de 11-12px quebra a lista — composta na **grotesca do corpo, não em mono**.
- **Keycaps são chrome estilizado, não texto.** As dicas `⌘K`, `↵`, `Esc` são badges minúsculos de pill/caixa: ~18px de altura, preenchimento `raised`, borda de filete, glifo `muted` a 11px, compostos na **grotesca do corpo** com `tabular-nums`. São lidos como teclas físicas, que é a maior parte do sinal "isto é uma ferramenta de verdade".
- **Formulários de auth empilhados são apertados e liderados por rótulo (Cal.com / Clerk).** Cards de sign-in de verdade usam um rótulo de campo claro acima de cada input (13px médio, `muted`), gap vertical de ~10-12px rótulo-para-campo, ~14-16px entre campos, e inputs de largura completa com padding interno de 10-12px. O Cal.com lidera com um botão preto "Sign up with Google" depois um caminho "email" contornado e uma linha de reasseguro silenciosa `No credit card required` — o formulário é uma coluna curta e confiante, não um painel de vidro flutuante. O card do Clerk fica numa superfície off-white lisa com um único filete e uma sombra suave; a *contenção* é o polimento.
- **O acento é racionado a um momento.** A ação principal da Linear no painel é uma pill branca lisa; o índigo só aparece como um pequeno ponto de status. Num formulário, gaste o acento no *anel do campo focado* OU no botão de submit — raramente em ambos. Erros são uma borda vermelha dessaturada + uma linha de ajuda de 12px, não um campo inundado de vermelho.
- **Números e tokens inline ficam na face do corpo.** Quando um input mostra um valor, contagem ou uma dica `⌘K`, é a grotesca com `font-variant-numeric: tabular-nums`. A Linear mostra pill-tokens inline (`vehicle_state`) dentro de texto de corpo usando um chip elevado sutil — *não* uma fonte monoespaçada, só um fundo arredondado tingido.

### A versão genérica a EVITAR

- Uma caixa `#18181B` pura com uma borda uniforme de 1px `#3F3F46`, `rounded-lg`, um ícone de lupa cinza centrado, e `placeholder:Search...` — idêntica a todo outro campo na página.
- Uma face monoespaçada em placeholders, keycaps, rótulos, legendas, ou qualquer valor numérico (o datado sinal de "dev-tool"). **Mono é banido aqui** — keycaps e contagens vão na grotesca com `tabular-nums`.
- Um command palette construído como dois cards empilhados (um card de busca + um card de resultados separado) com uma drop shadow pesada, resultados como texto liso alinhado à esquerda, e a linha selecionada marcada por uma faixa de borda esquerda colorida.
- Um halo de acento com glow de 4px no foco (`ring-4 ring-accent`) e um acento índigo/violeta fazendo isso.

### Alavancas de variedade (gire-as para que duas construções difiram)

- **Estratégia de borda:** (a) filete em todos os lados em repouso, (b) *nenhuma* borda em repouso + só preenchimento, o foco revela um anel, (c) estilo Linear **borda superior inset única** ou campo-sublinhado com borda inferior, (d) divisor-como-estrutura (busca e resultados compartilham uma casca dividida por uma linha inset). Escolha uma por construção; não encaixote tudo sempre.
- **Densidade:** coluna de auth espaçosa (Cal.com, campos de ~44-48px, gaps de rótulo generosos) vs. palette densa (Raycast, linhas de 36px, texto de 13px, tracking apertado). Defina a altura de linha e o tamanho de fonte deliberadamente.
- **Elevação:** campo de superfície tingida plano (sem sombra) vs. uma sombra suave em camada na palette flutuante vs. um glow `accent` ambiente tênue atrás dela. Nunca empilhe uma borda *e* uma sombra pesada num input em repouso.
- **Posicionamento do acento:** só anel-focado / só botão-de-submit / só ponto-de-status — escolha onde o único momento saturado pousa.
- **Enquadramento da palette:** overlay de modal centrado com blur de backdrop, vs. inline-no-painel (ancorado sob uma toolbar), vs. launcher de tela cheia (Raycast). Frame diferente = página diferente.

### Esboço copiável — command palette (⌘K)

Uma casca flutuante: uma linha de query sem borda, um divisor inset, linhas densas keyboard-first, keycaps de verdade na face do corpo. Sem mono, sem halo gordo, acento só na linha ativa.

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

Fontes: [Raycast](https://www.raycast.com/), [Raycast design notes (awesome-design-md)](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/raycast/DESIGN.md), [Linear ⌘K integration](https://linear.app/integrations/raycast)

---

## Badges, pills, status, tags e avatares

Estes são os menores objetos de product UI, que é exatamente por que fazem ou quebram a leitura "real vs. padrão de IA". A régua é: um status é lido num único olhar, e o chrome em volta dele quase desaparece.

### O que os melhores sites de verdade fazem

- **Linear: o status é um ícone + texto liso, não uma pill encaixotada.** Na sidebar ("In Progress", "High", "jori", "Codex") não há borda, sem chip preenchido, sem retângulo arredondado. Um pequeno glifo colorido carrega o estado (um anel meio-preenchido para "In Progress", um ícone-de-barra colorido para prioridade) e o rótulo é só texto neutro de ~13px em peso normal. O orçamento de cor vive no *ícone*, nunca num fundo. Este é o movimento de maior alavancagem: **a maioria dos "status" não deveria ser pill nenhuma.**
- **Quando É um chip, o preenchimento é um tingimento, não um bloco saturado.** Chips de status de verdade usam uma lavagem de baixa opacidade do acento (mais ou menos 10-15% de alpha) com o texto na *força cheia* da mesma matiz — texto verde sobre uma lavagem verde tênue, âmbar sobre âmbar. Nada de badge saturado sólido com texto branco a menos que seja um alerta genuíno (erro/destrutivo). Sólido + texto-branco é a exceção berrante, não o padrão.
- **Um ponto líder de 6px faz o trabalho de uma borda inteira.** O chip "Issue tracking is dead" da Linear e a maioria dos indicadores "Live / Active / Degraded" prefixam o rótulo com um minúsculo ponto `currentColor`. O ponto é a única cor; a superfície e o texto ficam neutros. Isto é lido como mais silencioso e mais atual que uma pill totalmente tingida.
- **Avatares são quadrados arredondados para orgs/workspaces, círculos para pessoas.** O workspace switcher "Basepoint" da Attio usa um glifo de marca num quadrado arredondado de raio ~6px, não um círculo. Círculos sinalizam um humano; squircles sinalizam uma entidade/app/time. Misturá-los deliberadamente é um sinal de acabamento. Pilhas de avatares se sobrepõem em cerca de `-8px` com um anel de 2px na cor de fundo da *página* para abrir um gap, e um chip de overflow "+4" combina exatamente com o tamanho do avatar.
- **Tags são o objeto mais silencioso na tela.** Os rótulos da Attio e os "Performance", "iOS" da Linear são lidos como texto de baixo contraste com no máximo uma superfície tênue — sem borda, ~12-13px, foreground neutro apagado. Eles ficam *atrás* do dado na hierarquia visual, nunca competem com ele.
- **O raio de canto é pequeno e consistente, não `rounded-full` por toda parte.** Chips de status/tag ficam em torno de 5-7px de raio (combinando com botões/inputs), para que pareçam parte de um sistema. Reserve `rounded-full` para badges de contagem e indicadores de ponto. Tudo em formato de pill é um indício.
- **Números em chips usam figuras tabulares e é isso** — `font-variant-numeric: tabular-nums` na grotesca do corpo. Um "+12", um "3 open", uma contagem de versão: mesma tipografia da UI, só tabular. Sem monoespaçada em lugar nenhum.
- **Sentry: a severidade é codificada por uma borda de acento colorida, não por uma pill saturada.** As linhas "Root Cause" carregam o estado por um pequeno ícone líder e uma linha de progresso/acento verde em vez de um badge grosso. A cor é um sinal fino sobreposto a uma linha de resto neutra.

### A versão genérica a EVITAR

- A pill padrão escura `inline-flex items-center gap-1 rounded-full border border-white/10 bg-white/5 px-2.5 py-0.5 text-xs` — aplicada a *todo* status, tag e rótulo identicamente. Esta é a impressão digital do padrão de IA.
- Um ponto de status que é *sempre* `bg-green-500` (ou, pior, índigo/violeta) independentemente do significado, emparelhado com `text-xs uppercase tracking-wide` — o visual de falsa-empresa.
- Encaixotar coisas que deveriam ser sem borda: prioridade, assignee e categoria são texto + glifo em apps de verdade, não chips com bordas de filete e sombras suaves.
- `rounded-full` em literalmente tudo, preenchimentos sólidos saturados com texto branco para estados que não são de alerta, e foregrounds `#fff`/`#000` puros.

### Alavancas de variedade

Gire ao menos duas destas por construção para que duas telas não compartilhem uma impressão digital:

- **Estratégia de chrome:** ícone+texto sem borda (Linear) vs. chip de lavagem tingida (preenchimento de 10% de acento, texto com matiz combinada) vs. chip neutro com prefixo de ponto vs. sólido só-para-alertas. Escolha um como o estilo da casa para a tela.
- **Codificação de cor:** cor no *ícone/ponto* vs. cor no *preenchimento* vs. cor numa *borda/sublinhado de acento* (Sentry). Não misture as três numa tela.
- **Ritmo de raio:** raio uniforme pequeno (~6px, combina com inputs) vs. pills `rounded-full` de verdade — comprometa-se, não misture.
- **Linguagem de forma de avatar:** círculos-para-pessoas vs. squircles-para-entidades; iniciais em cor plana vs. glifo monocromático vs. foto; espessura de gap de anel nas pilhas.
- **Densidade:** rótulos inline densos (Attio, ~2px de padding vertical, sem borda) vs. chips standalone confortáveis (~4-6px de padding). Atrele isto à densidade da tabela/card ao redor.

### Esboço copiável

Uma linha de status usando a convenção *ícone+texto sem borda* para estado/assignee, um chip live com *prefixo de ponto*, uma tag silenciosa, e uma pilha de avatares de pessoas com um avatar de org em squircle. Neutros tingidos, sem mono, figuras tabulares.

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

Repare no que está *ausente*: sem pill de borda de filete em todo elemento, sem badges sólidos saturados, sem `uppercase tracking-wide`, sem monoespaçada. A cor aparece em exatamente um registro por objeto (ícone, ponto ou preenchimento), as figuras são tabulares, e avatares de humano vs. entidade usam formas diferentes — o tipo de variação que faz a construção ser lida como desenhada em vez de gerada.

---

## Chrome de browser/app/dispositivo, elevação e enquadramento

O enquadramento é onde "isto é um produto de verdade" se vende ou se perde. O frame é o proscênio em volta da sua UI — acerte a borda, o lift e o empilhamento e o screenshot é lido como um app capturado; erre e é lido como um `<div>` com uma borda. As quatro referências resolvem isso de quatro formas diferentes, e nenhuma delas é a caixa padrão de IA.

### O que os melhores sites de verdade fazem

- **A borda é um realce inset, não uma caixa.** O mock de app da Linear não tem uma borda de 1px circundando o painel inteiro. A borda superior é uma única linha ~1px *mais clara* (um realce superior inset, `box-shadow: inset 0 1px 0 rgba(255,255,255,.06)`), que é lida como um bisel físico pegando luz. A base e os lados se dissolvem numa grande sombra suave. O frame é sentido, não contornado.
- **Superfícies se separam por degraus de luminosidade, não por divisores.** Dentro da Linear a sidebar, a coluna principal e o trilho de detalhe são diferenciados por saltos de luminosidade de 2-4% num quase-preto tingido (`#0d0e11` → `#15161a` → `#1a1b20`), não por filetes. Painéis empilhados (o card de agente "Codex" flutuante) sobem mais um degrau *e* ganham sua própria sombra. Elevação = uma superfície mais brilhante + uma sombra mais suave/maior, em conjunto.
- **Chrome de janela de verdade, usado com parcimônia.** Cap e Arc/Dia renderizam chrome real: pontos de semáforo do macOS (círculos de 12px, ~8px de distância, vermelho/âmbar/verde apagado — não saturado), uma fileira de toolbar curta com chevrons de voltar/avançar, e um título centrado e silencioso ("Dia / New Chat", "Cap 2025-05-23 ... .cap"). O título é a grotesca do corpo a ~13px num foreground apagado, nunca mono. A altura do chrome é apertada (~36-40px).
- **Frames aninhados sinalizam profundidade.** O Cap é chrome-dentro-de-chrome: uma janela de app externa, depois um painel de preview *interno* com seus próprios mini controles, depois uma trilha de timeline. Cada painel interno tem um raio menor que o pai (externo ~14px, interno ~10px) e sua própria sombra sutil — arredondamento concêntrico é o sinal de que você está dentro de uma UI composta de verdade.
- **Raio externo generoso, flutuando numa página contrastante.** Arc e Cap usam ~12-14px no frame externo e deixam a janela inteira *flutuar* na página com uma grande sombra de baixa opacidade (`0 24px 60px -24px rgba(0,0,0,.4)`) mais um único filete. A Framer pula o chrome por completo — seus cards de template fazem um screenshot sangrar rente a uma borda arredondada de ~8px e se separam por gap + sombra, então o contraste (card claro sobre página preta) faz o enquadramento.
- **O acento aparece uma vez, na coisa viva.** A única cor do Cap é a seleção azul da timeline e o botão de play; todo o resto é neutro. O acento do Arc é a pill de sidebar selecionada. O frame e o chrome ficam neutros para que o acento marque *o que está ativo*, não a decoração.

### A versão genérica a EVITAR

- O "frame de screenshot" = uma caixa `rounded-xl border border-white/10` com uma única sombra uniforme, toda superfície dentro na mesma cor plana, separada por filetes `border-t border-white/10` por toda parte.
- Uma barra de browser falsa com três pontos `#ff5f56`/`#ffbd2e`/`#27c93f` puros e uma URL em mono no campo de endereço. (Pontos saturados + mono = sinal instantâneo de IA.)
- Mono para o título da janela, o nome de arquivo, os rótulos de tab, ou o texto de status no chrome.
- Um só nível de elevação: tudo fica no mesmo plano, então nada é lido como aninhado ou ativo — o visual de "sombra suave num card" sem lógica de camadas.

### Alavancas de variedade

- **Tipo de frame:** janela de SO de verdade (chrome de semáforo) vs. chrome de browser (voltar/avançar + título) vs. *sem chrome* — imagem sangrando rente a uma borda arredondada (Framer). Escolha um por construção; não caia sempre no padrão da barra de browser.
- **Estratégia de borda:** realce-superior-inset + sombra (Linear, sem borda) vs. filete + sombra de flutuação (Arc) vs. contraste puro, sem borda nenhuma (Framer claro-sobre-escuro). Estes parecem significativamente diferentes.
- **Modelo de elevação:** plano único / em camadas (2-3 degraus de luminosidade, raios concêntricos, sombras aninhadas) / flutuando-na-página (uma grande drop shadow). Em camadas é lido como o mais "real".
- **Escala de raio:** apertada (8px, denso/técnico) vs. generosa (14px, consumo/amigável), e se os painéis internos descem *de degrau* no raio.
- **Densidade de chrome:** mínima (só um título) vs. toolbar completa com ícones/controles. Combine-a ao produto — uma dev tool merece uma toolbar mais densa que um gravador de consumo.

### Esboço copiável

Uma janela de app flutuante com chrome do macOS real-mas-silencioso, superfícies em camadas (a sidebar desce de degrau, o painel de detalhe sobe), borda de realce-superior-inset, um filete neutro, acento usado só na linha ativa. Sem caixa-de-borda, sem mono, figuras tabulares.

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

Notas que evitam que vire genérico: o frame externo não tem **nenhuma borda completa** — é um `ring` quase invisível mais um realce-superior `inset` mais uma sombra de flutuação. As três superfícies interiores (`#0c0e11` sidebar, `#101216` chrome, `#13151a` main) são degraus de luminosidade distintos num quase-preto *tingido*, então a profundidade vem do valor, não de contornos. O único divisor é um único `divide-white/[0.05]` dentro da lista. O acento (`#3fae9b`) aparece exatamente uma vez, como a barra da linha ativa. Toda figura é `tabular-nums` na grotesca do corpo — zero mono.
