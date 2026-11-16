"""Case da semana — carrossel de 5 telas a partir de um JSON.

Uso:  python scripts/case.py dados/case.json
Saída: saida/case-<edicao>/CS<edicao>-0N.html e .../png/*.png

Estrutura fixa (não mude a ordem):
  1 Capa       pergunta + foto oficial de divulgação + subtítulo
  2 O que fizeram
  3 O que ninguém te contou   (o negócio por trás, com citação real)
  4 Como aplicar no cliente pequeno (3 passos)
  5 CTA        frase de fechamento + faixa rasgada + chamadas
Campos com destaque usam três partes: antes / destaque / depois.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marca import B, W, L, RAIZ, pagina, chip_perfil, data_uri, renderizar

NUM = 'font-family: Inter, sans-serif; font-weight: 800; letter-spacing: -0.04em'
TOT = 5
TORN = '\n.torn{clip-path:polygon(0 8%,4% 0,9% 6%,15% 1%,22% 7%,30% 0,38% 6%,46% 1%,55% 7%,63% 0,71% 6%,80% 1%,88% 7%,95% 0,100% 5%,100% 94%,94% 100%,86% 94%,78% 100%,70% 94%,61% 100%,52% 94%,43% 100%,35% 94%,26% 100%,18% 94%,10% 100%,4% 95%,0 100%)}'


def marca_txt(p, cor_txt=B):
    return f'{p.get("antes","")}<span style="background: {L}; color: {cor_txt}; padding: 0 14px">{p["destaque"]}</span>{p.get("depois","")}'


def frame(c, n, dark, content, fonte='', last=False):
    bg, fg = (B, W) if dark else (W, B)
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px; background: {bg}; color: {fg}; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 40px">
<div style="display: flex; justify-content: space-between; align-items: center; font-weight: 800; font-size: 26px">
<span>{{SEU_ARROBA}}</span>
<span style="{NUM}; background: {L}; color: {B}; padding: 6px 18px; font-size: 34px">{n}/{TOT}</span>
</div>
{content}
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; justify-content: space-between; font-size: 22px; font-weight: 600"><span>{fonte}</span><span>{{SEU_NOME}} · {{SEU_METODO}}</span></div>
<div style="display: flex; justify-content: space-between; font-size: 22px; font-weight: 400; border-top: 2px solid {fg}; padding-top: 16px"><span>Case da semana</span><span style="font-weight: 800">Edição #{c['edicao']}</span><span>{'{{SEU_ARROBA}}' if last else 'Arraste para o lado →'}</span></div>
</div>
</div>'''


def tag(txt):
    return f'<span style="align-self: flex-start; margin-top: auto; background: {L}; color: {B}; font-weight: 800; font-size: 26px; padding: 8px 20px; border-radius: 40px">{txt}</span>'


def foto(c, h, chave='foto'):
    return f'<img src="{data_uri(c.get(chave) or c["foto"])}" alt="{c.get("foto_alt","")}" style="width: 920px; height: {h}px; object-fit: cover; border-radius: 28px; display: block">'


def paragrafos(lista, tam, gap=16):
    ps = ''.join(f'<p style="margin: 0">{p}</p>' for p in lista)
    return f'<div style="display: flex; flex-direction: column; gap: {gap}px; font-size: {tam}px; line-height: 1.35">{ps}</div>'


def passos(lista):
    out = []
    for i, (t, d) in enumerate(lista, 1):
        out.append(f'''<div style="display: flex; gap: 32px; align-items: flex-start; border-top: 4px solid {B}; padding-top: 28px">
<span style="{NUM}; font-size: 69px; line-height: 1; min-width: 96px">{i:02d}</span>
<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 42px; font-weight: 800; line-height: 1.15">{t}</span><span style="font-size: 31px; line-height: 1.35; text-wrap: pretty">{d}</span></div>
</div>''')
    return '<div style="display: flex; flex-direction: column; gap: 28px">' + ''.join(out) + '</div>'


def telas(c):
    cp, s2, s3, s4, s5 = c['capa'], c['tela2'], c['tela3'], c['tela4'], c['tela5']
    t = {}
    t[1] = pagina('Capa', f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px 80px; background: {W}; color: {B}; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 40px">
<div style="display: flex; justify-content: space-between; font-size: 22px; font-weight: 400"><span>Case da semana</span><span style="font-weight: 800">Edição #{c['edicao']}</span><span>{c['data']}</span></div>
<div style="margin-top: auto; display: flex; align-items: center; gap: 16px">{chip_perfil(B)}<span style="font-size: 24px; font-weight: 600">Olhar de estrategista · {{SEU_ARROBA}}</span></div>
<h1 style="margin: 0; {NUM}; font-size: 92px; line-height: 1.08">{marca_txt(cp['titulo'])}</h1>
{foto(c, 470)}
<p style="margin: 0; font-size: 36px; font-weight: 300; line-height: 1.3">{cp['sub']} <strong style="font-weight: 800">{cp['sub_forte']}</strong></p>
<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; font-size: 22px; font-weight: 400; border-top: 2px solid {B}; padding-top: 16px">
<span>{c['credito_foto']}</span>
<span style="display: flex; align-items: center; gap: 14px; font-weight: 800; font-size: 26px">Arraste para o lado <span style="width: 44px; height: 44px; border-radius: 50%; background: {B}; color: {L}; display: flex; align-items: center; justify-content: center">→</span></span>
</div>
</div>''')
    t[2] = pagina('O que fizeram', frame(c, 2, False, tag(s2['tag']) +
        f'<h2 style="margin: 0; {NUM}; font-size: 72px; line-height: 1">{s2["titulo"]}</h2>' + foto(c, 330, 'foto2') +
        paragrafos(s2['paragrafos'], 31), fonte=s2['fonte']))
    cit = ''
    if s3.get('citacao'):
        cit = f'''<div style="border: 3px solid {W}; padding: 32px 36px; display: flex; flex-direction: column; gap: 10px">
<span style="font-size: 40px; font-weight: 300; line-height: 1.2">“{s3['citacao']}”</span>
<span style="font-size: 24px; font-weight: 600; color: {L}">{s3['autor']}</span></div>'''
    t[3] = pagina('O que ninguém te contou', frame(c, 3, True, tag(s3['tag']) +
        f'<h2 style="margin: 0; {NUM}; font-size: 92px; line-height: 1">{marca_txt(s3["titulo"])}</h2>' +
        paragrafos(s3['paragrafos'], 36, 18) + cit, fonte=s3['fonte']))
    t[4] = pagina('Como aplicar', frame(c, 4, False, tag(s4['tag']) +
        f'<h2 style="margin: 0; {NUM}; font-size: 76px; line-height: 1">{s4["titulo"]}</h2>' + passos(s4['passos']),
        fonte=s4.get('fonte', 'Exemplos ilustrativos')))
    t[5] = pagina('CTA', frame(c, 5, False,
        f'<h2 style="margin: auto 0 0; {NUM}; font-size: 112px; line-height: 1">{s5["frase"]}</h2>' +
        f'<div class="torn" style="background: {B}; color: {W}; padding: 76px 80px 64px; margin: 0 -80px"><p style="margin: 0; {NUM}; font-size: 72px; line-height: 1">{marca_txt(s5["faixa"])}</p></div>' +
        paragrafos(s5['paragrafos'], 36, 20), last=True), TORN)
    return t


def main():
    c = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, 'dados', 'case.json'), encoding='utf-8'))
    pasta = os.path.join(RAIZ, 'saida', 'case-' + c['edicao'])
    os.makedirs(pasta, exist_ok=True)
    htmls = []
    for n, html in telas(c).items():
        h = os.path.join(pasta, f'CS{c["edicao"]}-0{n}.html')
        open(h, 'w', encoding='utf-8').write(html)
        htmls.append(h)
    for png in renderizar(htmls, os.path.join(pasta, 'png')):
        print(png)


if __name__ == '__main__':
    main()
