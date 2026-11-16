"""Frase do dia — gera as artes da semana a partir de um JSON.

Uso:  python scripts/frases.py dados/frases.json
Saída: saida/frases/<id>.html e saida/frases/png/<id>.png

Cada frase tem duas linhas:
  fina      → 1ª linha, peso leve (300)
  antes     → começo da 2ª linha, peso forte (800)
  destaque  → palavra marcada (fundo de destaque)
  depois    → resto da 2ª linha
  tema      → "branco", "azul" ou "lima" (alterne os três na semana)
Use &nbsp; entre palavras que não podem quebrar (ex.: "qualquer&nbsp;preço.").
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marca import B, W, L, NUM, RAIZ, pagina, chip_perfil, renderizar

TEMAS = {  # fundo, texto, marcador fundo, marcador texto, anel da foto
    'branco': (W, B, L, B, B),
    'azul':   (B, W, L, B, L),
    'lima':   (L, B, B, W, B),   # em fundo lima o texto é sempre azul
}


def arte(f):
    bg, fg, mk_bg, mk_fg, anel = TEMAS[f['tema']]
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px; background: {bg}; color: {fg}; font-family: Inter, sans-serif; display: flex; flex-direction: column">
<div style="display: flex; align-items: center; gap: 16px">
{chip_perfil(anel)}
<span style="font-size: 26px; font-weight: 600">{{SEU_ARROBA}}</span>
</div>
<h1 style="margin: auto 0; {NUM}; font-size: 112px; line-height: 1.14; font-weight: 300">{f['fina']}<br><span style="font-weight: 800">{f.get('antes','')}<span style="background: {mk_bg}; color: {mk_fg}; padding: 0 14px; -webkit-box-decoration-break: clone; box-decoration-break: clone">{f['destaque']}</span>{f.get('depois','')}</span></h1>
<div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: 400; border-top: 2px solid {fg}; padding-top: 20px">
<span style="font-weight: 800">Frase do dia</span><span>Salva e reposta ↗</span><span>{{SEU_METODO}}</span>
</div>
</div>'''


def main():
    dados = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, 'dados', 'frases.json'), encoding='utf-8'))
    pasta = os.path.join(RAIZ, 'saida', 'frases')
    os.makedirs(pasta, exist_ok=True)
    htmls = []
    for f in dados['frases']:
        h = os.path.join(pasta, f['id'] + '.html')
        open(h, 'w', encoding='utf-8').write(pagina('Frase do dia ' + f['id'], arte(f)))
        htmls.append(h)
    for png in renderizar(htmls, os.path.join(pasta, 'png')):
        print(png)


if __name__ == '__main__':
    main()
