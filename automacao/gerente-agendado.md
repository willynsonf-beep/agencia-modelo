# Gerente com autonomia: tarefas agendadas

Duas tarefas do Claude Code fazem o Gustavo (Gerente) trabalhar sozinho, todo dia:

| Tarefa | Quando | O que faz |
|---|---|---|
| Gerente {{NOME_DA_AGENCIA}} · manhã | todo dia, 8h | Lê o ESTADO.md, monta a cobrança do dia, publica no mural da Vila e manda uma notificação ao {{SEU_NOME}} |
| Gerente {{NOME_DA_AGENCIA}} · noite | todo dia, 19h | Fecha o dia, pergunta "Gravou? Mandou o vídeo?", atualiza o mural e notifica o {{SEU_NOME}} |

Elas rodam com o app do Claude aberto. Se o app estiver fechado na hora, rodam quando ele abrir.
O Gerente nunca publica, programa, turbina, paga ou manda mensagem para ninguém, e não muda o ESTADO.md.

## Memória da equipe (desde 12/11)
Tudo o que o {{SEU_NOME}} fala com qualquer pessoa na Vila (chat e reunião) vira fato em `memoria/equipe` (campo `fatos`). As conversas ficam em `conversas/<id>`. O Gerente lê a memória antes de cobrar: o que o {{SEU_NOME}} disse que está resolvido não é cobrado de novo. O executor (a cada 30 min) passa os fatos novos para o ESTADO.md e o DECISOES.md.

## Mural da Vila
- Artifact: {{LINK_DA_VILA}}
- Documento: coleção `mural`, id `atual`
- Formato: `{"turno", "atualizadoEm", "resumo", "paraWill": [...], "equipe": {pesquisador, roteirista, copywriter, designer, editor, revisor}, "prazos": [{quando, oque, dono}]}`
- Na Vila: o Gustavo vai até o {{SEU_NOME}} para cobrar o primeiro item de `paraWill`, faz a daily às 9h e a ronda nas mesas às 10h30 e às 15h usando `equipe`. O botão "Ciente, Gustavo" grava `cienteEm`.

## Prompt usado pelas tarefas (turno da manhã; o da noite troca o passo 2 pelo fechamento do dia)
Você é o Gustavo, Gerente da agência {{SEU_ARROBA}}. Leia CLAUDE.md, memoria/ESTADO.md, memoria/DECISOES.md e .claude/skills/gerente/SKILL.md em {{PASTA_DA_AGENCIA}}. Monte a cobrança do turno (o que vai ao ar, o que o {{SEU_NOME}} precisa fazer com prazo exato, o que atrasou, o que cada pessoa entrega nos próximos 3 dias). Grave no mural com ArtifactData (get de mural/atual para pegar a version, depois set com if_version) no formato acima. Mande uma PushNotification de até 180 caracteres com a cobrança principal. Não altere arquivos, não marque nada como feito, nunca publique, programe, turbine, pague ou envie mensagem.

# Produção autônoma (criada em 11/11/2026)
| Tarefa | Quando | Passo a passo |
|---|---|---|
| Radar de tendências {{NOME_DA_AGENCIA}} | 8h, 11h, 14h, 17h e 20h | `.claude/skills/radar-tendencias/SKILL.md` |
| Produção autônoma {{NOME_DA_AGENCIA}} | 10h | `.claude/skills/producao-autonoma/SKILL.md` |
