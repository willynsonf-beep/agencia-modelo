---
description: Cria um carrossel no padrão novo da agência (imagem real em toda tela, título curto, detalhes na legenda) sobre qualquer tema.
argument-hint: "[tema ou pauta]"
---
Crie um carrossel sobre: $ARGUMENTS

1. Leia a Regra nº 1 das artes no `CLAUDE.md`.
2. **roteirista/copywriter**: 5 a 8 telas (capa, telas `imagem`, opcional `lista`, `cta`), cada uma com título de até 8 palavras e no máximo 1 linha de apoio. Salve em `dados/carrosseis/<slug>.json`.
3. **pesquisador**: imagem real para cada tela (oficial, print real ou foto bruta do que está acontecendo; NUNCA foto do {{SEU_NOME}}, nem na tela de opinião ou de CTA). Preencha `imagens` com URL e crédito.
4. `python scripts/baixar_imagens.py <json>` e `python scripts/carrossel.py <json>`.
5. **copywriter**: legenda com os detalhes em `saida/<slug>/legenda.txt`.
6. **revisor** até APROVADO, depois mostre ao {{SEU_NOME}}.

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
