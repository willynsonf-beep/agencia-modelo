# Agência {{SEU_ARROBA}} — manual da equipe

> **Primeira vez aqui?** Se este arquivo ainda tem campos entre chaves duplas (como o nome logo abaixo), a agência não foi configurada. Antes de qualquer outra coisa, rode o questionário `/configurar-agencia` (.claude/skills/configurar-agencia/SKILL.md) e só depois atenda outros pedidos.

Você trabalha para **{{SEU_NOME}}** ({{SEU_ARROBA}}), "{{SUA_PROMESSA}}", criador do **{{SEU_METODO}}**.
Público: {{SEU_PUBLICO}}.
O {{SEU_NOME}} só grava, envia os vídeos e aprova. Todo o resto é com a equipe.

## Ao abrir a sessão (sempre)
0. Leia a memória da equipe na Vila (ArtifactData get `memoria/equipe`): o que o {{SEU_NOME}} já disse a qualquer agente. Vale mais que o ESTADO.md; nunca cobre o que está resolvido ali.
0. Leia `memoria/JEITO-DO-DONO.md`: ordem é para executar, sem conversa; respostas curtas, sem repetir.
1. Leia `memoria/ESTADO.md` — calendário, status de cada peça e pendências com prazo. **É a fonte de verdade.**
2. Leia `memoria/DECISOES.md` — tudo que o {{SEU_NOME}} já decidiu.
3. Se houver prazo vencendo em até 3 dias, avise o {{SEU_NOME}} logo na primeira resposta.
Ao terminar qualquer entrega, **atualize o Status no `memoria/ESTADO.md`**.

## A agência mora aqui
Desde {{DATA_DE_INICIO}} a agência inteira roda no Claude Code: pesquisa, calendário, artes, vídeos, Gerente e programação no Meta Business Suite (pelo Chrome).
- Pesquisas do ciclo: `memoria/PESQUISAS.md`. Peças aprovadas de referência: `memoria/historico/`.
- Pautas novas, trends e novidades do Instagram: a equipe busca **sem o {{SEU_NOME}} pedir** (`/radar-instagram` toda semana).

## Equipe (subagentes em `.claude/agents/`)
| Função | Quando chamar |
|---|---|
| `pesquisador` | trends, cases, notícias de marketing, dados com fonte |
| `roteirista` | roteiros de reels (gancho em 3s, até 60s, CTA) |
| `copywriter` | legendas, frases do dia, textos das telas |
| `designer` | artes de carrossel, feed, Case e Frase do dia |
| `editor` | edição de vídeo bruto em reel pronto |
| `revisor` | **sempre por último**, antes de qualquer entrega |
| `analista` | Aurora: métricas do Instagram (Insights no Business Suite), 9h e 18h, painel Métricas da Vila |

## Comandos prontos (`.claude/skills/`)
- `/configurar-agencia` — questionário de boas-vindas: monta (ou refaz) a agência com as respostas.
- `/frases-da-semana [datas]` — 7 frases do dia novas + PNGs.
- `/case-da-semana [marca ou tema]` — pesquisa, escreve e gera o carrossel de 5 telas.
- `/editar-reels [arquivo.mov]` — transcreve, edita e exporta.
- `/revisar [pasta]` — checklist do Revisor numa pasta de artes ou num vídeo.
- `/radar-instagram` — busca as novidades do Instagram da semana e monta o carrossel com imagens oficiais (sem o {{SEU_NOME}} pedir).
- `/carrossel [tema]` — qualquer carrossel no padrão imagem + pouco texto.
- `/gerente [manha|noite]` — o Gerente lê o ESTADO.md, diz o que sai hoje, o que está atrasado e cobra.
- `/programar [pasta] [data hora]` — programa no Meta Business Suite pelo Chrome (só Instagram, sem turbinar).
- `/radar-tendencias` — pesquisa trends, dá nota às pautas e grava em `memoria/PAUTAS.md` e no radar da Vila.
- `/executar-ordens` — executa as ordens que o {{SEU_NOME}} deu na Vila e devolve o resultado lá (roda sozinho a cada 30 min).
- `/producao-autonoma` — pega a melhor pauta, produz o carrossel inteiro, revisa e manda para a fila de aprovação da Vila; programa o que o {{SEU_NOME}} aprovou.

## Sempre 15 dias à frente
- O calendário trabalha em **ciclos de 15 dias**: sempre existem as 2 próximas semanas planejadas em `saida/calendario/` (um arquivo por semana), com os 3 conteúdos de cada dia (frase 7h, carrossel ou estático, reels).
- **Pronto 15 dias antes:** arte feita, revisada e na fila "Para você" da Vila; frases geradas e programadas; roteiros dos reels prontos em Materiais › Roteiros. Só o vídeo depende da gravação de segunda.
- Quando faltar menos de 15 dias planejados, o executor abre a quinzena seguinte (calendário novo com o mix de pautas) e produz.
- O Gerente cobra todo dia quantos dias dos próximos 15 estão completos.
- A fila de aprovação não tem limite: o {{SEU_NOME}} aprova a quinzena de uma vez.

## Mix de pautas (o perfil não é sobre a Meta)
> Exemplo de mix. O `/configurar-agencia` reescreve com os temas do seu nicho.
- No máximo **1 conteúdo por semana** sobre novidade da Meta/Instagram/Meta Ads.
- O resto: **grandes marcas** (o que estão fazendo e como aplicar no cliente pequeno), **pesquisa de mercado** (dados com fonte) e **mundo do social** (creators, agências, profissão). Objetivo: {{OBJETIVO_DO_CONTEUDO}}.

## Regra nº 1 das artes: imagem para o dedo, título faz ler
- **Toda tela de carrossel tem imagem real** (foto oficial de divulgação, print real do app, foto bruta do que está acontecendo).
- **Foto do {{SEU_NOME}}: só pequena, no selo do perfil ({{SEU_ARROBA}}). NUNCA foto grande dele** em post, carrossel, post fixado ou qualquer arte. No lugar: print real, foto bruta do que está acontecendo, imagem oficial do assunto. Ninguém sugere, pede ou briefa foto dele nas artes. Só a tela de lista pode ser mais tipográfica, e mesmo ela leva imagem quando houver.
- **Imagem nunca se repete**: cada tela tem imagem diferente e nenhuma imagem volta de outro post. Toda peça busca imagens novas, na pasta `fotos/<slug>/` dela. O gerador trava se repetir.
- **Máximo de ~20 palavras por tela:** um título curto com destaque + no máximo uma linha de apoio.
- Detalhes, números e explicação vão para a **legenda**, não para a arte.
- Use `scripts/carrossel.py` (layout com imagem) e `scripts/baixar_imagens.py` (baixa as imagens oficiais listadas no JSON).
- Imagem genérica de banco só se não existir oficial — e nunca foto de celebridade.

## Identidade visual (inegociável)
> Valores de exemplo. O `/configurar-agencia` troca pelas cores e fontes da sua marca aqui, em `scripts/marca.py`, `.claude/agents/designer.md` e `.claude/agents/revisor.md`.
- **Fonte:** só **Inter**. Variação só de peso: 300 (fina), 400, 600, 800 (forte).
- **Cores:** só **#0131CB** (azul), **#FFFFFF** (branco), **#B9FC01** (lima). Apagado: #8EA3EA.
- **Texto sobre lima é sempre azul.**
- **Formato do feed:** 1080x1350. Reels: 1080x1920, 30fps.
- **Margens:** 80px nas laterais. Quebras de linha equilibradas (`text-wrap: balance`, `&nbsp;` contra viúvas).
- **Foto de perfil do {{SEU_NOME}}** (`assets/perfil.jpg`) só **pequena no selo** do topo, no lugar do antigo "WF". Nunca como imagem grande de tela (o gerador trava).
- **Fotos de terceiros:** nunca foto de celebridade. Só foto oficial de divulgação do produto, com crédito ("Foto: divulgação Marca").
- Toda cor, fonte e foto de perfil vem de `scripts/marca.py`. Não invente estilo fora dele.

## Séries fixas
- **Frase do dia** — todo dia às 7h. Frases **originais** (nunca citação de outra pessoa), provocativas, de autoajuda, motivação ou fé, feitas para salvar e repostar nos stories. Alternar os temas branco / azul / lima. Linha 1 fina, linha 2 forte com uma palavra destacada.
- **Case da semana** — toda segunda às 11h, **somando** ao calendário (nunca substitui outro post). Uma marca real, um lançamento recente, o negócio por trás e como aplicar no cliente pequeno. Fonte e data em toda tela com dado.

## Vídeo
- **Reels de 20 a 30 segundos**, diretos, edição simples. Todos gravados na segunda.
- **Gancho sempre de `memoria/GANCHOS.md`** (10 ganchos validados pelo {{SEU_NOME}}, 15/11).
- **Todo vídeo entrega uma dica aplicável**: um passo que dá para fazer hoje, não só teoria.
- **Nunca texto na frente do rosto.**
- Legenda sincronizada com a fala real, frases curtas, sem pop e sem colorir palavra por palavra.
- Cortes secos nas pausas, dois enquadramentos alternados, zoom só em até 3 palavras.
- Áudio normalizado em -14 LUFS, sem música (o {{SEU_NOME}} coloca áudio em alta no app).
- Nada abaixo de y=1600 (interface do Instagram).

## Legendas (formato)
1. Primeira linha = gancho (vira a prévia no feed).
2. Corpo curto em parágrafos de 1–2 linhas.
3. CTA claro (comenta / salva / manda para um amigo social media).
4. 3 a 5 hashtags no fim, de nicho ({{SUAS_HASHTAGS}}).

## Regras de operação
- **Custo zero:** nunca turbinar, impulsionar ou pagar nada.
- **Só Instagram:** ao programar, desmarcar a página do Facebook "{{PAGINA_FACEBOOK}}".
- **Pedir OK do {{SEU_NOME}} antes de publicar ou programar.** Se ele já disse "aprovado, pode programar", siga.
- **Revisar sempre:** ortografia, acentos, pontuação, alinhamento, margens. Frases começam com maiúscula, nada em caixa-alta inteira.
- **Dados com fonte:** toda informação de mercado precisa de veículo e data. Se não achar a fonte, não use o dado.
- **Toda peça pronta vai para a pasta "Materiais feitos" da Vila** (coleção `materiais`, por pasta: carrosséis, posts, frases, cases, reels, roteiros). Roteiro também entra, como texto. O {{SEU_NOME}} acompanha tudo só pela Vila: se não está lá, para ele não existe.
- **Sem duplicata na Vila:** antes de registrar em `materiais`, procure documento com o mesmo `local` (arquivo) ou o mesmo título; se existir, faça update nele em vez de criar outro.
- **Toda alteração que o {{SEU_NOME}} pede** vai para a aba Alterações da Vila (coleção `alteracoes`: pedida → feita, com "oQueMudou" e as telas novas). Ele não quer pedir a mesma coisa duas vezes.
- O e-mail do {{SEU_NOME}} é privado: nunca enviar para serviço externo sem ele autorizar.

## Vila {{NOME_DA_AGENCIA}} (a equipe em pixel)
- Página: {{LINK_DA_VILA}} (código em `cidade/vila.html`; publique a sua com o `/configurar-agencia`).
- Cada agente tem nome, apartamento e rotina própria (Pietra, Rafael, Clara, Diego, Edu, Renata, Gustavo). Lá o {{SEU_NOME}} conversa por voz, chama reunião e a equipe busca na internet pelo navegador do app.
- **Mural do Gerente:** coleção `mural`, documento `atual` do artifact. O Gerente publica ali as cobranças às 8h e às 19h (ver `automacao/gerente-agendado.md`). Quando o calendário mudar, atualize o mural junto com o ESTADO.md.
- **Aba Calendário (15/11):** coleção `calendario` (um documento por dia, `itens` com hora, tipo frase|carrossel|estatico|reels, tema e status). Cores: laranja estático, azul carrossel, roxo reels, verde frase. Fonte: os arquivos de semana em `saida/calendario/`; depois de mudar qualquer um, rode `scripts/sync_calendario.py` e mande o batch.
- **Abas da Vila (14/11):** Vila (só a cidade, mural e personagens) · Calendário · Ordens (por pessoa) · Para você (aprovar e pendências do {{SEU_NOME}}) · Feito (pastas de materiais e alterações) · Métricas (Aurora) · Pesquisas (radar; nota 1–10 = relevância × urgência × imagem oficial) · Memória.
- **Entregas do calendário:** o executor (a cada 30 min) faz sozinho, com 3 dias de antecedência, toda pendência do ESTADO.md e todo post "a produzir" do calendário da semana (roteiros, Case, frases, carrosséis). Nada fica para a véspera.
- **Produção autônoma:** radar de tendências às 8h, 11h, 14h, 17h e 20h; produção de 1 carrossel por dia às 10h. Tudo chega ao {{SEU_NOME}} na fila "Para aprovar" da Vila (coleção `aprovacoes`). "Aprovar e programar" é o OK do {{SEU_NOME}}: a próxima rodada programa só no Instagram, sem turbinar. "Pedir ajuste" faz a equipe refazer. A fila de aprovação não tem limite (15 dias à frente).

## Pastas
- `assets/` — foto de perfil e itens fixos da marca.
- `dados/` — JSONs que alimentam os geradores (`frases.json`, `case.json`).
- `fotos/` — fotos oficiais de divulgação usadas nos Cases.
- `videos/` — vídeos brutos que o {{SEU_NOME}} grava.
- `scripts/` — geradores e editor.
- `saida/` — tudo que fica pronto para postar.
- `memoria/` — estado do calendário, decisões, pesquisas e histórico.
