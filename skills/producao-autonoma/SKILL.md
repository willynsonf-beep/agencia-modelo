---
description: Produção autônoma do {{SEU_ARROBA}}. Escolhe a melhor pauta do radar e produz o carrossel completo (texto, imagens oficiais, artes, legenda e revisão), coloca na fila de aprovação da Vila e, depois do OK do {{SEU_NOME}}, programa no Instagram.
---
A equipe trabalha sozinha; o {{SEU_NOME}} só aprova. Pasta da agência: {{PASTA_DA_AGENCIA}}. Vila (artifact): {{LINK_DA_VILA}}.
Carregue com ToolSearch, num só pedido: "select:ArtifactData,Artifact,PushNotification".

## 0. Ler a fila
Leia CLAUDE.md, memoria/ESTADO.md, memoria/DECISOES.md e memoria/PAUTAS.md (data e hora em America/Sao_Paulo).
ArtifactData action "list" em collection "aprovacoes". Cada documento tem status "aguardando", "ajuste" ou "aprovado".
- **"aprovado" sem programado: true** → vá ao passo 9 com ele.
- **"ajuste"** → refaça esse item primeiro (passos 3 a 8, mesmo slug, versao + 1), seguindo o campo "comentario" do {{SEU_NOME}}. Não produza item novo hoje. Ao terminar, marque na coleção "alteracoes" o documento desse pedido (slug igual, status "pedida") como status "feita", com feitoEm, por ("designer" etc.), oQueMudou (1–2 frases, o que trocou em qual tela) e telas (as URLs novas). Se não existir documento, crie um já como "feita".
- Se houver **2 ou mais "aguardando"**, não produza nada novo: mande PushNotification "2 carrosséis esperam sua aprovação na Vila." e pare.

## 1. Escolher a pauta
Em memoria/PAUTAS.md, pegue a pauta de formato carrossel com maior nota e status "ideia" que não repete tema do calendário (ESTADO.md) nem dos últimos 30 dias. **Cota da Meta:** se a semana (seg–dom) já tem 1 peça sobre Meta/Instagram/Meta Ads, pule toda pauta da Meta e pegue marca, pesquisa de mercado ou mundo do social. Se não houver nenhuma com nota 7 ou mais, rode antes o passo a passo de .claude/skills/radar-tendencias/SKILL.md e escolha de novo. Marque a pauta como "em produção".
Slug: aaaa-mm-dd-palavra-chave (minúsculas, sem acento).

## 2. Data sugerida
Escolha um dia nos próximos 7 dias sem outro post de feed no mesmo horário, às 12h ou às 18h (o público é mais ativo das 11h às 23h). Nunca use segunda 11h (Case da semana) nem 7h (Frase do dia).

## 3. Texto (papel da Clara, .claude/agents/copywriter.md)
Escreva dados/carrosseis/<slug>.json no formato de dados/carrosseis/novidades-ig.json: capa → telas "imagem" (uma por ideia, de 3 a 5) → "lista" com o que fazer → "cta". Título curto com destaque, no máximo ~20 palavras por tela, fonte e data em toda tela com dado.

## 4. Imagens (papel da Pietra e do Diego)
Só imagem oficial de divulgação (newsroom da marca, imprensa com crédito) ou foto bruta real; nunca repetir imagem de outro post; nunca celebridade; crédito em toda tela. Preencha "imagens" no JSON e rode `python3 scripts/baixar_imagens.py dados/carrosseis/<slug>.json`. Abra cada imagem com Read e confirme que é do assunto certo.

## 5. Arte (Diego)
`python3 scripts/carrossel.py dados/carrosseis/<slug>.json` → saida/<slug>/png/. Abra cada PNG com Read.

## 6. Legenda (Clara)
saida/<slug>/legenda.txt no formato de legenda do CLAUDE.md (gancho, corpo curto, CTA, 3 a 5 hashtags de nicho). Detalhes e números vão aqui.

## 7. Revisão (Renata, checklist de .claude/agents/revisor.md)
Corrija e gere de novo até APROVADO, no máximo 3 voltas. Se não aprovar em 3 voltas, não envie: marque a pauta como "ideia" de novo, anote o motivo em PAUTAS.md e pare.

## 8. Enviar para aprovação
1. Artifact action "read" com o url da Vila (obrigatório antes de enviar arquivos).
2. Artifact publish com url = a Vila, asset: true e file_paths = os PNGs de saida/<slug>/png/ em ordem (caminhos absolutos). Guarde as urls devolvidas, na mesma ordem.
3. ArtifactData action "set" em collection "aprovacoes", doc_id "<slug>" (para um item em ajuste, leia antes com "get" e use if_version), data:
   {"slug", "tema", "formato": "carrossel", "porque": "<1 frase: por que agora e para quem>", "fontes": [{"veiculo", "data", "url"}], "telas": [urls], "legenda": "<texto completo>", "sugestaoData": "<ex.: qui 19/11 12h>", "sugestaoISO": "<ISO com -03:00>", "status": "aguardando", "criadoEm": "<ISO UTC>", "revisao": "APROVADO", "versao": 1}
4. memoria/ESTADO.md: na seção "## Produção autônoma" (crie antes de "## Sessões de gravação" se não existir; tabela Data sugerida | Peça | Formato | Status) adicione ou atualize a linha com status "Aguardando aprovação". memoria/PAUTAS.md: status "aguardando aprovação".
5. PushNotification: "Carrossel pronto para aprovar: <tema>. Abra a Vila."

## 9. Programar o que o {{SEU_NOME}} aprovou
Só itens com status "aprovado" (o {{SEU_NOME}} clicou "Aprovar e programar" na Vila: isso é o OK dele). Siga .claude/skills/programar/SKILL.md pelo Chrome (ferramentas mcp__claude-in-chrome__*): só Instagram, desmarcar a página {{PAGINA_FACEBOOK}}, data e hora de sugestaoISO (se já passou, o próximo horário livre às 12h ou 18h), legenda do documento, PNGs de saida/<slug>/png/ em ordem, nunca turbinar ("Talvez mais tarde"), nunca "Publicar agora".
Depois: ArtifactData "update" (com if_version) {"programado": true, "programadoPara": "<texto>"}; ESTADO.md status "Programado"; PAUTAS.md status "usado".
Se o Chrome não estiver conectado, o login pedir senha ou algo der errado: não insista; ArtifactData "update" {"programado": false, "erro": "<motivo curto>"} e PushNotification "Aprovado, mas não consegui programar <tema>: <motivo>."

## Regras
- Produza só para preencher dia sem carrossel/estático nos próximos 15 dias do calendário (saida/calendario/); com os 15 dias completos, não produza. Custo zero: nunca turbinar ou pagar nada. Só Instagram.
- Nunca publicar na hora e nunca programar algo sem status "aprovado".
- Nunca mexer em Case da semana, Frase do dia ou nos reels do {{SEU_NOME}}.
- Dado de mercado sempre com veículo e data; sem fonte, fora.

## Registrar na pasta Materiais da Vila (obrigatório ao terminar)
Toda peça pronta vai para a coleção `materiais` da Vila ({{LINK_DA_VILA}}), para o {{SEU_NOME}} ver por pasta:
1. Suba os PNGs: Artifact action "read" no URL (uma vez na sessão) e depois publish com `url`, `asset: true` e `file_paths` (até 25 por chamada). Guarde as URLs `/_blob/...`.
2. ArtifactData "set" (ou "update" com if_version se já existir) em collection "materiais", doc_id = slug, data: {pasta: "carrosseis"|"posts"|"frases"|"cases"|"reels"|"roteiros", titulo, slug, status: "aguardando"|"aprovado"|"programado"|"postado"|"pronto"|"rascunho", data (ex.: "ter 17/11 18h"), dataISO, telas: [urls], legenda, roteiro (texto, para roteiros), fontes, criadoPor (pesquisador|roteirista|copywriter|designer|editor|revisor|gerente), local (pasta no computador), criadoEm}.
3. Quando programar ou postar, atualize o `status` e a `data` do mesmo documento.
