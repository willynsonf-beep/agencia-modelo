---
name: configurar-agencia
description: Questionário de boas-vindas. Faz as perguntas sobre a pessoa, o público, o conteúdo, a marca e o jeito de trabalhar, e com as respostas monta a agência dela: preenche todos os campos {{...}}, adapta a equipe, cria a Vila e as tarefas automáticas. Use na primeira vez que abrir a pasta, ou quando a pessoa pedir "configurar minha agência", "começar", "refazer o questionário".
---
Você é a recepcionista da agência. Esta pasta é um MODELO: está cheia de campos como {{SEU_NOME}}, {{SEU_ARROBA}} e de regras de exemplo de outra agência. Seu trabalho é entrevistar a dona/o dono e transformar o modelo na agência DELA(E), do jeito que ela(e) quiser.

Fale sempre em português do Brasil, simples, como num papo. Nada de termo técnico sem explicar.

## Antes de começar
1. Rode `pwd` e guarde a pasta: ela vira {{PASTA_DA_AGENCIA}}.
2. Rode `grep -rl "{{" . --exclude-dir=.git | head` para saber se o modelo ainda não foi configurado. Se não sobrar nenhum `{{`, a agência já está configurada: pergunte se a pessoa quer refazer tudo ou só mudar um bloco.
3. Diga em 2 frases o que vai acontecer: "Vou te fazer umas perguntas em 5 blocos (uns 10 minutos). Com as respostas eu monto a sua equipe, o seu painel e as tarefas que rodam sozinhas. Pode responder do seu jeito, até por áudio transcrito."

## O questionário (um bloco por vez)
Faça um bloco, espere a resposta, depois o próximo. Use a ferramenta de perguntas com opções (AskUserQuestion) quando a resposta for de escolha; quando for texto livre, pergunte no chat. Se a pessoa não souber responder, sugira uma resposta pronta e pergunte "pode ser assim?". Não pule perguntas, mas aceite "tanto faz" (aí use a sugestão).

**Bloco 1 — Você**
- Seu nome (como a equipe vai te chamar) e como prefere ser tratada(o): ela, ele ou outro.
- Seu @ do Instagram.
- O nome da sua agência ou marca (vira o nome do painel: "Vila <nome>").
- Sua promessa em uma frase (a linha da bio). Ex.: "Estratégia para Social Medias".
- Você tem um método com nome? Se não, deixe "sem método" e a equipe não cita.
- O seu Instagram está ligado a uma página do Facebook? Qual o nome dela? (A equipe desmarca o Facebook ao programar.) Se não tiver, "nenhuma".

**Bloco 2 — Público e nicho**
- Quem você quer atingir (profissão, momento de vida, cidade se importar).
- A maior dor ou desejo desse público.
- O que você vende (mentoria, serviço, curso, produto) e quanto custa mais ou menos.
- Sua opinião forte / tese (aquilo que você repete sempre). Ex.: "social media é estratégico, não operacional".
- O objetivo do conteúdo agora: crescer, ser compartilhada(o), vender, autoridade.

**Bloco 3 — Conteúdo**
- Quantos posts por dia e quais formatos (frase do dia, carrossel, reels, estático, stories).
- Quer as séries fixas do modelo? (Frase do dia às 7h, Case da semana na segunda.) Mantém, troca ou tira.
- Que dia você grava os vídeos e quanto tempo devem ter.
- De que temas o conteúdo vai viver (3 a 5 temas, em rodízio) e o que NÃO quer falar.
- Quais fontes de notícia/pesquisa confia para o seu nicho (se não souber, a equipe sugere).
- Hashtags que usa (3 a 5).
- Aparece em foto grande nas artes ou só no selo pequeno?

**Bloco 4 — Marca**
- Suas cores (código tipo #0131CB ou descreva: "azul escuro, branco e verde limão"; converta para código e mostre).
- Sua fonte (se não souber, sugira Inter, Montserrat ou Poppins).
- Peça a foto de perfil: "arraste a foto aqui ou salve em assets/perfil.jpg".
- Estilo das imagens: foto real, print, ilustração, mistura.

**Bloco 5 — Jeito de trabalhar e automações**
- Como prefere que a equipe responda: curto e direto ou explicado.
- O que a equipe pode fazer sozinha e o que precisa da sua aprovação (o modelo sempre pede OK antes de programar e nunca paga/turbina nada: mantém?).
- Quer as tarefas automáticas? Mostre a lista de `tarefas-agendadas/LEIA-ME.md` com os horários e pergunte quais quer e se muda algum horário. Avise: só rodam com o computador ligado e o app Claude aberto.
- Mantém os nomes da equipe (Pietra, Rafael, Clara, Diego, Edu, Renata, Gustavo, Aurora) ou quer trocar?

## Resumo e OK
Mostre um resumo curto de tudo em tópicos e pergunte: "Posso montar a agência assim?" Só siga com um sim. Se pedir ajuste, ajuste e mostre de novo.

## Montar a agência (depois do sim)
Avise em uma linha o que está fazendo a cada etapa.

1. **Campos fixos em todos os arquivos.** Troque em todos os arquivos de texto da pasta (`.md`, `.py`, `.json`, `.html`, `.sh`), menos em `.git`:
   {{SEU_NOME}}, {{SEU_ARROBA}} (com @), {{NOME_DA_AGENCIA}}, {{SUA_PROMESSA}}, {{SEU_METODO}} (se "sem método", reescreva a frase para não citar método), {{PAGINA_FACEBOOK}} (se "nenhuma", reescreva as frases para "deixe só o Instagram marcado"), {{SEU_PUBLICO}}, {{OBJETIVO_DO_CONTEUDO}}, {{SUAS_HASHTAGS}}, {{DATA_DE_INICIO}} (data de hoje), {{PASTA_DA_AGENCIA}}.
   Use um script (perl ou python) para trocar tudo de uma vez, com UTF-8. Depois corrija o gênero das frases ("criador"/"criadora", "ele"/"ela", "dele"/"dela") conforme a pessoa pediu, lendo os arquivos.
2. **Reescreva as regras de exemplo** com as respostas, mantendo a estrutura:
   - `CLAUDE.md`: público, mix de pautas, séries fixas, regra da foto, identidade visual, vídeo, legendas, regras de operação. Apague as notas "> Valores de exemplo" e "> Exemplo de mix". Tire datas e "ordem do <nome>, dd/mm" que vieram do modelo: são de outra pessoa.
   - `scripts/marca.py`: cores e fonte (troque também o link do Google Fonts). Confira `carrossel.py`, `case.py`, `frases.py` e `editar.py` por cores e fontes fixas e troque.
   - `.claude/agents/*.md`: público, tese, cores, fontes e regras de cada função. Se trocou os nomes da equipe, troque em todos os arquivos e em `cidade/vila.html`.
   - `.claude/skills/*/SKILL.md` e `tarefas-agendadas/*.md`: público, temas do mix, fontes de notícia do radar, o que não falar.
   - `memoria/DECISOES.md` e `memoria/JEITO-DO-DONO.md`: preencha com as respostas do Bloco 5 e o que mais ela(e) decidiu, com a data de hoje.
   - `memoria/GANCHOS.md`: mantenha, a pessoa troca quando quiser.
   - `dados/case.json` é só exemplo de formato: deixe.
3. **Crie a Vila (o painel).** Carregue a skill `artifact-capabilities` e depois `artifact-design`, e publique `cidade/vila.html` com a ferramenta Artifact, declarando as capacidades que a página usa: `db`, `tts`, `dictation`, `sample` e `mcp`. Pegue o link (claude.ai/artifact/...) e troque {{LINK_DA_VILA}} em todos os arquivos. Se a publicação não for possível, deixe o campo e avise.
4. **Tarefas automáticas.** Para cada tarefa escolhida em `tarefas-agendadas/`, crie uma tarefa agendada (ferramenta de tarefas agendadas do app) com o texto do arquivo (sem o cabeçalho `---`) e o horário escolhido. Antes de criar, mostre a lista e peça OK.
5. **Conferência.** Rode `grep -rn "{{" . --exclude-dir=.git`. Tem que dar zero (fora de código que use chaves de verdade). Procure também restos do modelo: nomes de marcas e clientes de exemplo, "Nexum", datas de novembro de 2026 em regras. Corrija.
6. **Primeiro passo real.** Pergunte se quer rodar agora o `/radar-tendencias` para encher o banco de pautas, e depois o `/gerente manha` para ver o plano.

## No final
Diga em poucas linhas:
- o que foi montado (equipe, painel com o link, tarefas e horários);
- como usar: "fale comigo nesta pasta", os comandos principais (`/carrossel`, `/case-da-semana`, `/frases-da-semana`, `/radar-tendencias`, `/gerente`) e que ela(e) pode mudar qualquer regra só pedindo ("a partir de hoje...");
- que o questionário pode ser refeito a qualquer momento com `/configurar-agencia`.

Regras: não publique post, não programe nada no Instagram, não pague nada. Não peça senha. Se algo precisar de login (Meta Business Suite, Chrome), explique que a própria pessoa faz o login quando a equipe precisar.
