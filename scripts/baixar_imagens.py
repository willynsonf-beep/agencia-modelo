"""Baixa as imagens oficiais listadas no JSON do carrossel (campo "imagens").
Uso: python scripts/baixar_imagens.py dados/carrosseis/novidades-ig.json

Cada item: {"arquivo": "fotos/x.png", "url": "https://...", "credito": "Imagem: divulgação Instagram"}
Se "url" estiver vazio, o Pesquisador precisa achar uma imagem OFICIAL (newsroom da marca,
about.fb.com, about.instagram.com, ou a imagem de divulgação usada pela imprensa) e preencher.
Nunca foto de celebridade. Nunca imagem de banco genérico se existir a oficial.
"""
import os, sys, json, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

c = json.load(open(sys.argv[1], encoding='utf-8'))
falta = []
for it in c.get('imagens', []):
    destino = os.path.join(RAIZ, it['arquivo'])
    if os.path.exists(destino):
        print('ok (já existe)', it['arquivo']); continue
    if not it.get('url'):
        falta.append(it['arquivo']); continue
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    req = urllib.request.Request(it['url'], headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r, open(destino, 'wb') as f:
        f.write(r.read())
    print('baixada', it['arquivo'])
if falta:
    print('\nSEM URL (achar imagem oficial e preencher no JSON):', *falta, sep='\n  ')
