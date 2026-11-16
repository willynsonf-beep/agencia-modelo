---
description: Edita um vídeo bruto do {{SEU_NOME}} em reel pronto (legenda sincronizada, cortes, destaques, áudio -14 LUFS), sem texto sobre o rosto.
argument-hint: "[arquivo do vídeo em videos/] [roteiro ou tema opcional]"
---
Edite o reel a partir de: $ARGUMENTS

Use o subagente **editor** e siga o fluxo descrito nele e as regras de vídeo do `CLAUDE.md`.
Se houver roteiro em `dados/roteiros/`, use-o para escolher o gancho e as palavras de destaque, mas **o que vale é a fala real**.
No fim, chame o subagente **revisor** e mostre ao {{SEU_NOME}} 3 quadros (gancho, destaque e CTA) e pergunte: "Aprova ou quer ajustar alguma parte?"

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
