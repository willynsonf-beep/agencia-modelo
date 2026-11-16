---
description: Executa as ordens que o {{SEU_NOME}} deu na Vila (coleção "ordens"): cada ordem vira entrega de verdade (arte, roteiro, pesquisa, legenda, revisão), com resultado de volta na Vila e aviso curto ao {{SEU_NOME}}.
---
Pasta da agência: {{PASTA_DA_AGENCIA}}. Vila: {{LINK_DA_VILA}}.
Carregue as ferramentas com ToolSearch num pedido só: "select:ArtifactData,Artifact,PushNotification".

## 0. Ver se há trabalho (barato)
ArtifactData action "list" em collection "ordens". Separe as que têm status "nova". Faça também "list" em collection "alteracoes" (status "pedida") e "get" em collection "memoria", doc_id "equipe" (fatos com `em` mais novo que o campo `processadoAte`). **Se não houver nenhuma das três coisas, pare aqui sem fazer mais nada** (não leia arquivos, não notifique).

## 1. Antes de executar
Leia memoria/JEITO-DO-DONO.md, CLAUDE.md, memoria/ESTADO.md e o manual do responsável em .claude/agents/<para>.md (gerente: .claude/skills/gerente/SKILL.md).
Para cada ordem nova, da mais antiga para a mais nova (no máximo 3 por rodada):
- ArtifactData "update" com if_version: {"status": "andamento", "atualizadoEm": "<ISO>"}.
- Se o documento tiver "resposta", é a resposta do {{SEU_NOME}} a uma pergunta anterior: use-a.

## 2. Executar como o responsável ("para")
- **designer** (arte, carrossel, post de feed, capa): siga .claude/skills/carrossel/SKILL.md (imagem oficial, Inter, cores da marca, revisão da Renata). Gere os PNGs em saida/<slug>/png/. Se for para postar, também crie a entrada na fila de aprovação como no passo 8 de .claude/skills/producao-autonoma/SKILL.md.
- **roteirista**: roteiro no formato do manual em dados/roteiros/<slug>.md.
- **copywriter**: legenda, frases ou texto em saida/<slug>/ (ou dados/frases.json para Frase do dia).
- **pesquisador**: pesquisa com WebSearch e WebFetch; toda informação com veículo, data e link; salve em memoria/PESQUISAS.md e, se virar pauta, em memoria/PAUTAS.md.
- **revisor**: checklist de .claude/agents/revisor.md sobre o arquivo citado.
- **editor**: só se houver vídeo em videos/; senão, pergunte (passo 3).
- **gerente**: atualize o mural (coleção "mural", doc "atual") ou o ESTADO.md conforme a ordem.
Se a ordem pedir publicar ou programar: só com o OK explícito do {{SEU_NOME}} no próprio pedido, e seguindo .claude/skills/programar/SKILL.md (só Instagram, nunca turbinar).

## 3. Devolver na Vila (ArtifactData "update" com if_version)
- Pronto: {"status": "feito", "resultado": "<1 ou 2 frases: o que foi feito e onde está>", "atualizadoEm": "<ISO>"} e, se houver imagens, envie os PNGs como assets (Artifact action "read" na Vila; depois Artifact publish com url, asset: true, file_paths) e grave as urls em "telas". Links úteis em "links".
- Faltou algo essencial: {"status": "pergunta", "pergunta": "<uma pergunta só, com a sua sugestão>", "atualizadoEm": "<ISO>"}.
- Deu erro: {"status": "erro", "resultado": "<motivo curto>"}.
Atualize memoria/ESTADO.md se a entrega mexe no calendário.

## 4. Avisar e aprender
- Uma PushNotification por rodada, só se algo ficou pronto ou precisa do {{SEU_NOME}}: "Diego: arte X pronta, está na Vila." (até 180 caracteres).
- Se a ordem revelou algo novo sobre o jeito do {{SEU_NOME}} (preferência, forma de pedir, algo que ele odeia), acrescente uma linha datada em memoria/JEITO-DO-DONO.md, seção "Aprendizados", e grave o arquivo inteiro no documento "perfil"/"will" da Vila com ArtifactData ("get" para pegar a version; depois "set" com {"texto": "<conteúdo do arquivo>", "atualizadoEm": "<ISO>"}).

## Regras
Custo zero. Nunca publicar na hora. Não discutir a ordem: executar. Respostas ao {{SEU_NOME}} curtas e sem repetir o que ele já sabe.

## Alterações pedidas (rodar junto, toda vez)
- ArtifactData "list" em collection "alteracoes". Se houver documento com status "pedida", ele vem ANTES das ordens: marque "fazendo", refaça a peça (slug no campo "slug", JSON em `dados/carrosseis/<slug>.json`), gere os PNGs, revise, suba as telas novas (asset), atualize `aprovacoes/<slug>` (telas, versao+1, status "aguardando") e marque a alteração "feita" com feitoEm, por, oQueMudou e telas.
- Se nenhuma ordem "nova" e nenhuma alteração "pedida": pare na hora.
- Regra fixa: nunca foto grande do {{SEU_NOME}} (ver `memoria/JEITO-DO-DONO.md`).

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.

## Memória nova (rodar junto, toda vez)
- Para cada fato da memória mais novo que `processadoAte`: se muda o calendário ou o status de uma peça (gravou, mandou vídeo, aprovou, cancelou, mudou data, já resolveu algo), atualize `memoria/ESTADO.md`. Se é decisão ou preferência duradoura, acrescente em `memoria/DECISOES.md` (com data). Se o fato resolve uma pendência do mural, tire do mural (`mural/atual`, campos paraWill/equipe, com if_version).
- No fim, ArtifactData "update" em memoria/equipe só com {processadoAte: "<em do último fato processado>"} e if_version. Nunca apague nem reescreva `fatos`.
