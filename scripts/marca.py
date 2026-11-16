"""Identidade visual do {{SEU_ARROBA}} e renderizador de PNG.
Tudo que gera arte importa daqui. Não crie cores ou fontes fora deste arquivo."""
import os, sys, base64, mimetypes

B, W, L, D = '#0131CB', '#FFFFFF', '#B9FC01', '#8EA3EA'   # azul, branco, lima, azul apagado
NUM = 'font-family: Inter, sans-serif; letter-spacing: -0.045em'
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTO_PERFIL = os.path.join(RAIZ, 'assets', 'perfil.jpg')


def data_uri(caminho):
    """Embute a imagem no HTML para o PNG sair igual em qualquer máquina."""
    if not os.path.isabs(caminho):
        caminho = os.path.join(RAIZ, caminho)
    tipo = mimetypes.guess_type(caminho)[0] or 'image/jpeg'
    with open(caminho, 'rb') as f:
        return f'data:{tipo};base64,' + base64.b64encode(f.read()).decode()


def chip_perfil(anel, tamanho=64):
    """Foto de perfil do {{SEU_NOME}}, SÓ pequena no selo (substitui o antigo 'WF'). Nunca usar grande (ordem do {{SEU_NOME}}, 12/11)."""
    return (f'<img src="{data_uri(FOTO_PERFIL)}" alt="{{SEU_NOME}}" style="width: {tamanho}px; '
            f'height: {tamanho}px; border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 3px {anel}; display: block">')


def pagina(titulo, corpo, css_extra=''):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{titulo}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
body{{margin:0}}
h1,h2,p{{text-wrap:balance}}{css_extra}
</style>
</head>
<body>
{corpo}
</body>
</html>
'''


def renderizar(htmls, pasta_png):
    """Gera um PNG 1080x1350 para cada HTML (qualidade 2x para o Instagram não borrar)."""
    from playwright.sync_api import sync_playwright
    os.makedirs(pasta_png, exist_ok=True)
    saidas = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        for h in htmls:
            pg.goto('file://' + os.path.abspath(h))
            pg.wait_for_load_state('networkidle')
            pg.evaluate('document.fonts.ready')
            png = os.path.join(pasta_png, os.path.splitext(os.path.basename(h))[0] + '.png')
            pg.screenshot(path=png, clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1350})
            saidas.append(png)
        nav.close()
    return saidas
