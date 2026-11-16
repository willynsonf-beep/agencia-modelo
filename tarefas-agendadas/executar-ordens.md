---
name: executar-ordens
description: Pega as ordens que o {{SEU_NOME}} deu na Vila {{NOME_DA_AGENCIA}}, executa de verdade e devolve o resultado lá.
---

Trabalhe na pasta {{PASTA_DA_AGENCIA}} (agência {{SEU_ARROBA}} do {{SEU_NOME}}). Escreva sempre em português do Brasil.

Leia o arquivo {{PASTA_DA_AGENCIA}}/.claude/skills/executar-ordens/SKILL.md e siga os passos dele.

PASSO 1 — CHECAGEM RÁPIDA (economiza token). Carregue com ToolSearch "select:ArtifactData,Artifact,PushNotification". Na Vila {{NOME_DA_AGENCIA}} (artifact {{LINK_DA_VILA}}):
a) list "ordens" → tem alguma com status "nova"?
b) list "alteracoes" → tem alguma com status "pedida"?
c) list "aprovacoes" → tem alguma com status "aprovado" e programado diferente de true?
d) get "memoria"/"equipe" → tem fato com `em` mais novo que `processadoAte`?
e) Entregas do calendário (15 dias à frente): leia a tabela "Pendências com prazo" de memoria/ESTADO.md. Tem item com dono "Equipe" (ou nome de alguém da equipe) vencendo nos próximos 15 dias ou já vencido, que ainda não está pronto? E no calendário da semana (os arquivos de semana em {{PASTA_DA_AGENCIA}}/saida/calendario/), tem post dos próximos 15 dias marcado "a produzir" ou "a fazer" que não dependa de gravação do {{SEU_NOME}}?
Se nada disso existir, pare na hora, sem notificar.

PASSO 2 — EXECUTE, nesta ordem:
1. Entregas do calendário vencendo (passo e) — sempre 15 dias à frente. Faça até 3 peças por rodada, da data mais próxima para a mais longe. Se os calendários cobrirem menos de 15 dias a partir de hoje, crie o arquivo da semana seguinte em saida/calendario/ (frase 7h + carrossel ou estático + reels por dia, com o mix de pautas do CLAUDE.md e temas de memoria/PESQUISAS.md e memoria/PAUTAS.md). Frases do dia: gere com /frases-da-semana e grave em aprovacoes já com status "aprovado" (o {{SEU_NOME}} liberou as frases sem aprovação), para o passo 4 programar. faça de verdade como o responsável (roteiros com o manual .claude/agents/roteirista.md salvos em dados/roteiros/; Case com /case-da-semana; frases com /frases-da-semana; post "a produzir" do calendário com /carrossel, enviado para aprovacoes com a sugestaoData do calendário, e marque "pronto, aguardando aprovação" no arquivo do calendário). Registre cada entrega na coleção "materiais" da Vila (pasta certa; roteiro com o texto no campo `roteiro`) e marque a pendência como feita no ESTADO.md.
2. Ordens "nova": marque "andamento", execute como o responsável (manuais em .claude/agents/, skills em .claude/skills/), devolva "feito" com resultado curto, "pergunta" com uma pergunta só, ou "erro".
3. Alterações "pedida": refaça a peça, atualize aprovacoes/materiais e marque a alteração "feita" com oQueMudou e telas.
4. Aprovações "aprovado" sem programado: ANTES, grave programando:true com if_version (se falhar por versão, outra rodada já está programando: pule). Confira em Conteúdo › Programados se o post já existe, para nunca duplicar. (Reels: formato "reels" sobe o MP4 do campo local da coleção materiais, em saida/reels/, como Reels, com a legenda do documento; capa = primeiro quadro.) Programe já no Meta Business Suite pelo Claude in Chrome seguindo .claude/skills/programar/SKILL.md (só Instagram, desmarcar {{PAGINA_FACEBOOK}}, nunca turbinar, "Talvez mais tarde"), na sugestaoData. Depois grave programado:true e programadoPara. Se o Chrome não estiver conectado, grave em aprovacoes {erro: "Chrome desconectado: abra o Chrome com a extensão Claude ligada"} e siga.
5. Memória nova: passe para ESTADO.md/DECISOES.md, tire do mural o que já foi resolvido e grave só {processadoAte} em memoria/equipe (update com if_version; nunca reescreva `fatos`).

PASSO 2b — ABA CALENDÁRIO DA VILA (sempre que algo mudou no passo 2): atualize o status da linha no arquivo de semana em saida/calendario/ (programado, aguardando aprovação, pronto, roteiro pronto ou a produzir) e rode `python3 {{PASTA_DA_AGENCIA}}/scripts/sync_calendario.py <pasta temporária>`. Ele imprime a lista de writes: mande tudo num único ArtifactData "batch" (se der erro de versão, faça get do dia e use if_version). Também quando o {{SEU_NOME}} aprovar algo na Vila, marque "aguardando aprovação" → "aprovado" e, depois de programar, "programado".

PASSO 3 — Uma única PushNotification curta com o que ficou pronto ou o que precisa do {{SEU_NOME}}.

Regras: ordem é para executar, não para discutir. Respostas curtas e sem repetir o que o {{SEU_NOME}} já sabe (memoria/JEITO-DO-DONO.md). Custo zero; nunca turbinar; nunca publicar na hora; programar só o que o {{SEU_NOME}} aprovou. Nunca foto grande do {{SEU_NOME}} nas artes.
