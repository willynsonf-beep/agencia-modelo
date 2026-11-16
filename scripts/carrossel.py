"""Carrossel com IMAGEM EM TODA TELA e pouco texto (padrão novo da agência).

Uso:  python scripts/carrossel.py dados/carrosseis/novidades-ig.json
      (antes, rode  python scripts/baixar_imagens.py <mesmo json>  para baixar as fotos)
Saída: saida/<slug>/png/<slug>-0N.png

Regra de ouro: a imagem para o dedo, o título faz ler. Máximo ~20 palavras por tela.
Tipos de tela no JSON:
  capa     imagem grande + título curto
  imagem   imagem em cima (60% da tela) + etiqueta + título + 1 linha
  lista    até 3 itens curtíssimos (máx. 6 palavras cada)
  cta      imagem real (obrigatória, NUNCA foto do {{SEU_NOME}}) + frase final + chamada

REGRA DO WILL (12/11): foto do {{SEU_NOME}} só pequena, no selo {{SEU_ARROBA}}. Nunca foto grande dele em tela nenhuma.
Títulos aceitam destaque: {"antes": "...", "destaque": "...", "depois": "..."} ou texto simples.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marca import B, W, L, RAIZ, pagina, chip_perfil, data_uri, renderizar, FOTO_PERFIL

NUM = 'font-family: Inter, sans-serif; font-weight: 800; letter-spacing: -0.04em'


def titulo(t, cor_mk=B):
    if isinstance(t, str):
        return t
    return (f'{t.get("antes","")}<span style="background: {L}; color: {cor_mk}; padding: 0 12px; '
            f'-webkit-box-decoration-break: clone; box-decoration-break: clone">{t["destaque"]}</span>{t.get("depois","")}')


def img(caminho, w, h, pos='center', raio=0):
    if 'will-perfil' in caminho:
        sys.exit('ERRO: foto do {{SEU_NOME}} grande é proibida. Use print real, foto do que está acontecendo ou imagem oficial.')
    full = caminho if os.path.isabs(caminho) else os.path.join(RAIZ, caminho)
    if os.path.exists(full):
        return f'<img src="{data_uri(full)}" alt="" style="width: {w}px; height: {h}px; object-fit: cover; object-position: {pos}; border-radius: {raio}px; display: block">'
    return f'<div style="width: {w}px; height: {h}px; border-radius: {raio}px; background: repeating-linear-gradient(45deg,{L} 0 20px,{W} 20px 40px); display: flex; align-items: center; justify-content: center; color: {B}; font: 800 32px Inter">FALTA A IMAGEM: {os.path.basename(caminho)}</div>'


def topo(n, tot, cor, chip):
    return f'''<div style="position: absolute; top: 48px; left: 80px; right: 80px; display: flex; justify-content: space-between; align-items: center; z-index: 2">
<div style="display: flex; align-items: center; gap: 14px; background: {W}; color: {B}; padding: 6px 20px 6px 6px; border-radius: 40px">{chip_perfil(B, 48)}<span style="font-weight: 800; font-size: 24px">{{SEU_ARROBA}}</span></div>
{'' if tot == 1 else f'<span style="{NUM}; background: {L}; color: {B}; padding: 6px 18px; font-size: 32px">{n}/{tot}</span>'}
</div>'''


def rodape(c, cor, fonte, last):
    return f'''<div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; gap: 24px; font-size: 22px; color: {cor}; border-top: 2px solid {cor}; padding-top: 16px">
<span>{fonte}</span><span style="font-weight: 800; white-space: nowrap">{'{{SEU_ARROBA}}' if last else 'Arraste →'}</span></div>'''


def tela_capa(c, t, n, tot):
    return f'''<div style="position: relative; width: 1080px; height: 1350px; background: {B}; color: {W}; font-family: Inter, sans-serif; overflow: hidden">
{img(t['imagem'], 1080, 790, t.get('foco','top'))}
{topo(n, tot, W, L)}
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 560px; box-sizing: border-box; padding: 48px 80px 48px; background: {B}; display: flex; flex-direction: column; gap: 22px">
<span style="align-self: flex-start; background: {L}; color: {B}; font-weight: 800; font-size: 26px; padding: 8px 20px; border-radius: 40px">{t.get('etiqueta', c['serie'])}</span>
<h1 style="margin: 0; {NUM}; font-size: 80px; line-height: 1.1; text-wrap: balance">{titulo(t['titulo'])}</h1>
{rodape(c, W, t.get('credito',''), tot == 1)}
</div>
</div>'''


def tela_imagem(c, t, n, tot, last):
    dark = t.get('fundo', 'branco') == 'azul'
    bg, fg = (B, W) if dark else (W, B)
    return f'''<div style="position: relative; width: 1080px; height: 1350px; background: {bg}; color: {fg}; font-family: Inter, sans-serif; overflow: hidden; display: flex; flex-direction: column">
{img(t['imagem'], 1080, 840, t.get('foco','center'))}
{topo(n, tot, fg, L)}
<div style="flex: 1; box-sizing: border-box; padding: 48px 80px 56px; display: flex; flex-direction: column; gap: 20px">
<span style="align-self: flex-start; background: {L}; color: {B}; font-weight: 800; font-size: 24px; padding: 6px 18px; border-radius: 40px">{t['etiqueta']}</span>
<h2 style="margin: 0; {NUM}; font-size: 84px; line-height: 1.1; text-wrap: balance">{titulo(t['titulo'])}</h2>
{f'<p style="margin: 0; font-size: 36px; line-height: 1.3; text-wrap: balance">{t["linha"]}</p>' if t.get('linha') else ''}
{rodape(c, fg, t.get('fonte',''), last)}
</div>
</div>'''


def tela_lista(c, t, n, tot, last):
    itens = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; border-top: 4px solid {B}; padding-top: 26px">
<span style="{NUM}; font-size: 72px; line-height: 1; min-width: 100px">{i:02d}</span><span style="font-size: 48px; font-weight: 800; line-height: 1.12; text-wrap: balance">{x}</span></div>'''
                    for i, x in enumerate(t['itens'], 1))
    foto = img(t['imagem'], 920, 440, t.get('foco', 'center'), 28) if t.get('imagem') else ''
    return f'''<div style="position: relative; width: 1080px; height: 1350px; box-sizing: border-box; padding: 150px 80px 56px; background: {W}; color: {B}; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 36px">
{topo(n, tot, B, L)}
{foto}
<h2 style="margin: 0; {NUM}; font-size: 72px; line-height: 1.04">{titulo(t['titulo'])}</h2>
<div style="display: flex; flex-direction: column; gap: 26px">{itens}</div>
{rodape(c, B, t.get('fonte',''), last)}
</div>'''


def tela_cta(c, t, n, tot):
    foto = t.get('imagem')
    if not foto or 'will-perfil' in foto:
        sys.exit('ERRO: tela cta precisa de imagem real (foto do {{SEU_NOME}} grande é proibida).')
    return f'''<div style="position: relative; width: 1080px; height: 1350px; background: {B}; color: {W}; font-family: Inter, sans-serif; overflow: hidden; display: flex; flex-direction: column">
{img(foto, 1080, 720, t.get('foco','center 25%'))}
{topo(n, tot, W, L)}
<div style="flex: 1; box-sizing: border-box; padding: 56px 80px 56px; display: flex; flex-direction: column; gap: 24px">
<h2 style="margin: 0; {NUM}; font-size: 84px; line-height: 1.1; text-wrap: balance">{titulo(t['titulo'])}</h2>
<p style="margin: 0; font-size: 36px; line-height: 1.3">{t['linha']}</p>
{rodape(c, W, t.get('credito', '{{SEU_METODO}}'), True)}
</div>
</div>'''


def checar_repeticao(c):
    """Ordem do {{SEU_NOME}} (15/11): imagem nunca se repete — nem entre telas do mesmo post, nem de outro post."""
    import glob
    minhas = [t['imagem'] for t in c['telas'] if t.get('imagem')]
    dup = {i for i in minhas if minhas.count(i) > 1}
    if dup:
        sys.exit(f'ERRO: imagem repetida dentro do mesmo carrossel: {sorted(dup)}. Cada tela leva uma imagem diferente.')
    usadas = {}
    for f in glob.glob(os.path.join(RAIZ, 'dados', 'carrosseis', '*.json')):
        try:
            o = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(o, dict) or o.get('slug') == c['slug']:
            continue
        for t in o.get('telas', []):
            if t.get('imagem'):
                usadas.setdefault(t['imagem'], o.get('slug'))
    rep = [f'{i} (já usada em {usadas[i]})' for i in minhas if i in usadas]
    if rep:
        sys.exit('ERRO: imagem já usada em outro post. Busque imagem nova:\n  ' + '\n  '.join(rep))


def main():
    arq = sys.argv[1]
    c = json.load(open(arq, encoding='utf-8'))
    checar_repeticao(c)
    tot = len(c['telas'])
    pasta = os.path.join(RAIZ, 'saida', c['slug'])
    os.makedirs(pasta, exist_ok=True)
    hs = []
    for n, t in enumerate(c['telas'], 1):
        last = n == tot
        f = {'capa': lambda: tela_capa(c, t, n, tot), 'imagem': lambda: tela_imagem(c, t, n, tot, last),
             'lista': lambda: tela_lista(c, t, n, tot, last), 'cta': lambda: tela_cta(c, t, n, tot)}[t['tipo']]
        h = os.path.join(pasta, f'{c["slug"]}-0{n}.html')
        open(h, 'w', encoding='utf-8').write(pagina(f'{c["slug"]} {n}', f()))
        hs.append(h)
    for p in renderizar(hs, os.path.join(pasta, 'png')):
        print(p)


if __name__ == '__main__':
    main()
