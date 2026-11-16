---
description: Cria as 7 Frases do dia da próxima semana (post das 7h) e gera os PNGs prontos para programar.
argument-hint: "[datas, ex.: 19 a 25/11]"
---
Crie as Frases do dia para: $ARGUMENTS (se vazio, os 7 dias seguintes à última semana em `dados/frases.json`).

1. Leia `CLAUDE.md` e o `dados/frases.json` atual para **não repetir** frases nem palavras de destaque.
2. Peça ao subagente **copywriter** 7 frases originais (mix: 2 provocação sobre valor/cobrança, 2 autoajuda, 2 motivação, 1 fé), no formato do JSON, alternando os temas branco / azul / lima. Ids no padrão `FD-MMDD` (ex.: FD-1119).
3. Salve em `dados/frases.json` (guarde a semana anterior em `dados/arquivo/frases-<semana>.json`).
4. Rode `python scripts/frases.py dados/frases.json`.
5. Peça ao subagente **revisor** para checar os 7 PNGs em `saida/frases/png/`. Corrija até ele aprovar.
6. Mostre ao {{SEU_NOME}} a lista das 7 frases com a data de cada uma e diga: "Prontas. Manda a pasta `saida/frases/png` no chat da sede para programar às 7h."

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
