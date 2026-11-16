# Sua agência 24h com o Claude

Esta pasta é uma agência de conteúdo inteira que roda dentro do app Claude: pesquisadora de trends, roteirista, copywriter, designer, editor de vídeo, revisora, gerente e analista de métricas. Você só grava, aprova e dá ordens. A equipe faz o resto.

É **sua**: pode mudar tudo do jeito que quiser.

## Do que você precisa
- Conta no Claude com plano pago (Pro ou Max): https://claude.ai
- O **app Claude para computador** (Mac ou Windows): https://claude.ai/download
- Python 3 instalado (para gerar as artes e editar vídeo). O Claude te ajuda a instalar: é só pedir.
- Opcional: o app Claude no celular, para acompanhar e aprovar de qualquer lugar.

## Começar (uma vez só)
1. **Pegue a sua cópia.** No GitHub, clique em **"Use this template" → "Create a new repository"**. Dê um nome (ex.: `minha-agencia`) e deixe **Private**. Essa cópia é só sua.
2. **Baixe para o computador.** Na sua cópia, clique em **Code → Download ZIP** e descompacte numa pasta fácil (ex.: Documentos/minha-agencia). Quem já usa git pode clonar.
3. **Abra no Claude.** No app Claude, vá na aba **Code**, escolha **abrir pasta** e selecione a pasta da agência.
4. **Faça o questionário.** Escreva: `/configurar-agencia`
   O Claude faz perguntas em 5 blocos (você, público, conteúdo, marca e jeito de trabalhar) e monta tudo com as suas respostas: a equipe, o seu painel (a Vila) e as tarefas que rodam sozinhas.
5. Pronto. A partir daí, é só conversar com a equipe nessa pasta.

## Como usar no dia a dia
- Peça do seu jeito: "faz um carrossel sobre X", "quais pautas boas tem hoje?", "edita o vídeo que salvei em videos/".
- Comandos prontos:
  - `/carrossel [tema]`: carrossel completo com imagens
  - `/case-da-semana [marca]`: case de uma marca real em 5 telas
  - `/frases-da-semana`: 7 frases do dia
  - `/editar-reels [arquivo]`: transcreve, corta e legenda o vídeo
  - `/radar-tendencias`: busca trends e dá nota às pautas
  - `/gerente manha`: o que sai hoje e o que está atrasado
  - `/revisar [pasta]`: revisão antes de postar
  - `/programar`: programa no Meta Business Suite (só com o seu OK)
- **Mudar uma regra:** é só falar. "A partir de hoje, nada de emoji nas legendas." A equipe anota em `memoria/DECISOES.md` e segue.
- **Refazer a configuração:** `/configurar-agencia` de novo.

## Onde fica cada coisa
| Pasta / arquivo | O que é |
|---|---|
| `CLAUDE.md` | O manual da equipe (as regras da sua agência) |
| `.claude/agents/` | Cada pessoa da equipe e o que ela faz |
| `.claude/skills/` | Os comandos prontos (`/carrossel` etc.) |
| `memoria/` | Calendário (`ESTADO.md`), decisões, pautas, pesquisas, ganchos |
| `tarefas-agendadas/` | Textos das tarefas automáticas e horários (veja o LEIA-ME de lá) |
| `cidade/vila.html` | O painel da Vila (a equipe em pixel, aprovações, calendário) |
| `scripts/` | Geradores de arte e editor de vídeo |
| `assets/` | Sua foto de perfil (`perfil.jpg`) |
| `fotos/`, `videos/`, `saida/` | Imagens baixadas, vídeos brutos e o que fica pronto |

## Bom saber
- **"24h" de verdade:** as tarefas automáticas só rodam com o **computador ligado e o app Claude aberto**. No celular você acompanha e aprova pela Vila.
- **Nada sai sem você:** a equipe pede seu OK antes de programar e **nunca** turbina nem paga nada.
- **Senhas:** a equipe nunca pede. Quando precisar do Meta Business Suite, você faz o login no navegador.
- **Uso do plano:** cada tarefa automática consome do seu plano do Claude. Comece com poucas.
