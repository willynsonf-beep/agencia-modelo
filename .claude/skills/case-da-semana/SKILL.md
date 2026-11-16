---
description: Monta o Case da semana (segunda às 11h): pesquisa um case real, escreve as 5 telas e a legenda, e gera os PNGs.
argument-hint: "[marca ou tema opcional]"
---
Monte a próxima edição do Case da semana. Pista do {{SEU_NOME}}: $ARGUMENTS

1. Leia `CLAUDE.md` e o `dados/case.json` atual (a próxima edição é o número seguinte).
2. Subagente **pesquisador**: 3 opções de case dos últimos 30 dias, cada uma com fonte, data, o negócio por trás e se existe foto oficial de divulgação. Se o {{SEU_NOME}} deu uma pista, priorize ela.
3. Mostre as 3 opções ao {{SEU_NOME}} e espere ele escolher (se ele disse "escolhe você", escolha a de lógica de negócio mais clara).
4. Peça ao {{SEU_NOME}} a foto oficial de divulgação (ou baixe do newsroom da marca, se permitido) e salve em `fotos/`. **Nunca foto de celebridade.**
5. Subagente **copywriter**: preencha um novo `dados/case.json` (guarde o anterior em `dados/arquivo/`) e escreva a legenda em `saida/case-<edição>/legenda.txt`.
6. `python scripts/case.py dados/case.json`.
7. Subagente **revisor**: checa as 5 telas e a legenda. Corrija até aprovar.
8. Entregue: "Case #<edição> pronto. Manda `saida/case-<edição>/png` e a legenda no chat da sede para programar segunda às 11h."

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
