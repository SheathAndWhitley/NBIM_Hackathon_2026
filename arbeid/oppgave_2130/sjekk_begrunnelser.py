"""#2130: NBIMs tidligere begrunnelser (agent.csv kolonne sitat/punkt) mot ferskt nbim.no og PDF 2024, setning for setning.
Bruk: python3 -I sjekk_begrunnelser.py <gvg.html> <gvg2024.txt> <agent.csv>"""
import sys, re, html, csv, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', html.unescape(s)).replace('’', "'").replace('‘', "'").replace('\xad', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
h = open(sys.argv[1], encoding='utf-8').read()
# avsnitt med offisiell nummerering prinsipp.delpunkt fra overskriftene
p = d = 0; blokk = []
for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>|<(p|li)[^>]*>(.*?)</\3>', h, re.S):
    if m.group(1):
        t = re.sub('<[^>]+>', '', m.group(2)).strip(); n = re.match(r'(\d+)\.', t)
        if n and m.group(1) in ('h2', 'h3'): p, d = int(n.group(1)), 0
        elif n: d = int(n.group(1))
    else:
        blokk.append((norm(re.sub('<[^>]+>', ' ', m.group(4))), f'{p}.{d}'))
pdf = norm(open(sys.argv[2], encoding='utf-8').read()); pdf = re.sub(r'(\w)- (\w)', r'\1\2', pdf)
sett = {}
for r in csv.DictReader(open(sys.argv[3], encoding='utf-8')):
    if r['sitat']: sett.setdefault((r['punkt'], r['sitat']), []).append(r['sitat_kilde'])
print('| punkt | setninger på nbim.no | i PDF 2024 | nettsidens punkt | stemmer | eksempel-kilde |')
for (pk, s), k in sorted(sett.items()):
    setn = [x for x in re.split(r'(?<=[.!?])\s+', norm(s)) if len(x) > 15]
    funn = [next((nr for b, nr in blokk if x in b), None) for x in setn]
    ok = sum(f is not None for f in funn); ip = sum(x in pdf for x in setn)
    nr = sorted({f for f in funn if f})
    stem = 'stemmer' if ok == len(setn) and nr == [pk.replace('GVG ', '')] else 'AVVIKER'
    print(f'| {pk} | {ok}/{len(setn)} | {ip}/{len(setn)} | {",".join(nr)} | {stem} | {k[0][:70]} ({len(k)} rader) |')
    if stem == 'AVVIKER': print('  ', s[:300])
