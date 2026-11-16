---
name: producao-autonoma
description: A equipe escolhe a melhor pauta, produz o carrossel completo, manda para aprovação na Vila e programa o que o {{SEU_NOME}} aprovou.
---

Trabalhe na pasta {{PASTA_DA_AGENCIA}} (agência {{SEU_ARROBA}} do {{SEU_NOME}}). Escreva sempre em português do Brasil.

Leia o arquivo {{PASTA_DA_AGENCIA}}/.claude/skills/producao-autonoma/SKILL.md e siga todos os passos dele, do início ao fim. Em resumo:
0. Ler a fila de aprovação da Vila {{NOME_DA_AGENCIA}} (artifact {{LINK_DA_VILA}}, coleção "aprovacoes") com ArtifactData: programar o que o {{SEU_NOME}} aprovou, refazer o que ele pediu para ajustar, e não produzir nada novo se já houver 2 carrosséis esperando aprovação.
1 a 7. Escolher a pauta de maior nota em memoria/PAUTAS.md, escrever o carrossel, baixar imagens oficiais, gerar os PNGs com scripts/carrossel.py, escrever a legenda e revisar com o checklist da revisora até APROVADO (use os manuais em .claude/agents/ e as regras do CLAUDE.md).
8. Enviar para aprovação: Artifact read da Vila, upload dos PNGs como assets (Artifact publish com url, asset: true, file_paths), documento em "aprovacoes" com status "aguardando", linha em memoria/ESTADO.md (seção "Produção autônoma") e PushNotification ao {{SEU_NOME}}.
9. Programar no Meta Business Suite pelo Chrome só o que tem status "aprovado": só Instagram, desmarcar a página {{PAGINA_FACEBOOK}}, nunca turbinar, nunca publicar na hora.

Regras: produza só para preencher dia vazio dos próximos 15 dias no calendário (saida/calendario/); se os 15 dias estiverem completos, não produza nada; custo zero; nunca programar sem status "aprovado"; nunca mexer em Case da semana, Frase do dia ou reels do {{SEU_NOME}}; todo dado com veículo e data. Se algo der errado, pare, registre o motivo e avise o {{SEU_NOME}} com PushNotification.