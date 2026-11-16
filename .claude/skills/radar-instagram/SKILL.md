---
description: Radar semanal das novidades do Instagram para social medias — pesquisa, escolhe as 3 a 5 mais importantes e gera o carrossel com imagens oficiais e pouco texto. Rodar toda semana sem esperar o {{SEU_NOME}} pedir.
argument-hint: "[período opcional, ex.: últimos 15 dias]"
---
Monte o carrossel "Novidades do Instagram". Período: $ARGUMENTS (se vazio, últimos 15 dias).

1. Se `dados/carrosseis/novidades-ig.json` ainda não virou post (pergunte ou veja `saida/`), comece por ele: vá direto ao passo 4.
2. Subagente **pesquisador**: novidades do Instagram, do Edits e da Meta no período, com fonte e data (TechCrunch, Social Media Today, The Verge, Tecnoblog, Olhar Digital, Omelete, newsroom oficial). Priorize o que muda o trabalho do social media (formatos, alcance, edição, monetização, regras). Descarte boato sem fonte.
3. Escolha 3 a 5 notícias. Para cada uma, ache a **imagem oficial** e escreva o JSON em `dados/carrosseis/novidades-ig-<ddmm>.json` no formato do `novidades-ig.json`: capa → uma tela `imagem` por notícia → `lista` "O que fazer esta semana" → `cta`. Título curto com destaque + 1 linha por tela.
4. `python scripts/baixar_imagens.py <json>`. Se alguma imagem não tiver URL, procure (WebSearch/WebFetch) a imagem oficial e preencha. Abra cada imagem baixada e confirme que é da notícia certa.
5. `python scripts/carrossel.py <json>`.
6. Subagente **copywriter**: legenda em `saida/<slug>/legenda.txt` (aqui entram os detalhes e números).
7. Subagente **revisor**. Corrija até APROVADO.
8. Mostre ao {{SEU_NOME}} as telas e a legenda e diga: "Pronto. Programo para quando?"

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
