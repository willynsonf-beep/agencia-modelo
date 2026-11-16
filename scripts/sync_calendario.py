"""Lê saida/calendario/semana-*.md e gera um JSON por dia para a coleção `calendario` da Vila.

Uso: python3 scripts/sync_calendario.py <pasta_saida>
Imprime a lista de writes (op set) para o ArtifactData batch.
Tipos: frase · carrossel · estatico · reels. Status: programado · aguardando · pronto · gravar · produzir.
"""
import glob, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAS = {'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'SAB', 'DOM'}
ANO = 2026


def tipo_de(t):
    u = t.split(' — ')[0].upper()
    if re.match(r'^\d+H\s+FRASE', u): return 'frase'
    if 'REELS' in u: return 'reels'
    if 'ESTÁTICO' in u or 'ESTATICO' in u or ', FEED' in u or ' FEED ' in u: return 'estatico'
    return 'carrossel'


def status_de(t):
    l = t.lower()
    if 'programado' in l: return 'programado'
    if 'aguardando aprovação' in l or 'aguardando aprovacao' in l: return 'aguardando'
    if 'roteiro pronto' in l or 'depende da gravação' in l: return 'gravar'
    if 'liberada' in l or 'arte pronta' in l or 'pronto' in l: return 'pronto'
    return 'produzir'


def tema_de(t):
    t = re.sub(r'^\d+h\s+', '', t)
    t = t.split(' — ')[0]
    t = re.sub(r'^(Frase( do dia)?|REELS|CARROSSEL|ESTÁTICO|EXTRA|NOTÍCIA|EDUCATIVO|HUMOR|CASE)[^:]*:\s*', '', t, flags=re.I)
    t = re.sub(r'^Frase\s+(FD-\d+\s*)?', '', t)
    t = re.sub(r'^(carrossel|Carrossel)\s+', '', t)
    t = re.sub(r',\s*(carrossel|feed|reels)$', '', t)
    return t.strip().strip('"').replace('"', '')


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    dias = {}
    arqs = sorted(glob.glob(os.path.join(RAIZ, 'saida', 'calendario', 'semana-*.md')), key=os.path.getmtime)
    for arq in arqs:  # o mais novo sobrescreve o dia
        atual = None
        for linha in open(arq, encoding='utf-8'):
            linha = linha.strip()
            m = re.match(r'^(\w{3})\s+(\d{1,2})/(\d{1,2})', linha)
            if m and m.group(1).upper() in DIAS:
                atual = f'{ANO}-{int(m.group(3)):02d}-{int(m.group(2)):02d}'
                dias[atual] = []
                continue
            if atual and re.match(r'^\d{1,2}h', linha):
                hora = linha.split()[0]
                dias[atual].append({'hora': hora, 'tipo': tipo_de(linha), 'tema': tema_de(linha)[:160], 'status': status_de(linha)})
    writes = []
    for d, itens in sorted(dias.items()):
        itens.sort(key=lambda x: int(x['hora'].rstrip('h')))
        p = os.path.join(out, f'cal-{d}.json')
        json.dump({'data': d, 'itens': itens}, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
        writes.append({'op': 'set', 'collection': 'calendario', 'doc_id': d, 'file_path': p})
    print(json.dumps(writes, ensure_ascii=False))


if __name__ == '__main__':
    main()
