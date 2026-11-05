"""#2130: sjekk hvert NBIM GVG-punkt (og agentens sitater) mot ferskt hentet nbim.no og 2024-PDF.
Bruk: python3 -I sjekk_kilder.py <gvg.html> <gvg2024.txt> <punkter.jsonl> <agent.csv>"""
import sys, re, html, json, csv, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', html.unescape(s))
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('\xad', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
h = open(sys.argv[1], encoding='utf-8').read()
# overskrifter i rekkefølge, for å vise hvilket offisielt (under)punkt hvert avsnitt står under
web_blokker = []
cur = []
for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>|<(p|li)[^>]*>(.*?)</\3>', h, re.S):
    if m.group(1):
        cur = [norm(re.sub('<[^>]+>', '', m.group(2)))]
    else:
        web_blokker.append((norm(re.sub('<[^>]+>', '', m.group(4))), cur[0] if cur else ''))
web = norm(re.sub('<[^>]+>', ' ', h))
pdf = norm(open(sys.argv[2], encoding='utf-8').read())
pdf_nh = re.sub(r'(\w)- (\w)', r'\1\2', pdf)
pkt = {}
for l in open(sys.argv[3], encoding='utf-8'):
    d = json.loads(l)
    if re.match(r'NBIM \d', d['id']):
        pkt[d['id']] = d
brukt = {}
for r in csv.DictReader(open(sys.argv[4], encoding='utf-8')):
    brukt.setdefault(r['retningslinje_id'], set()).add(r['retningslinje_sitat'])
ut = []
for pid, d in pkt.items():
    t = norm(d['tekst'])
    i_web = t in web
    i_pdf = t in pdf or t in pdf_nh
    under = next((u for b, u in web_blokker if t in b), '')
    ag = brukt.get(pid)
    ag_lik = None if ag is None else all(norm(s) == t for s in ag)
    ut.append(dict(id=pid, web=i_web, pdf=i_pdf, under=under, avsnitt=d.get('avsnitt',''), agent_n=len(ag) if ag else 0, agent_lik=ag_lik, tekst=d['tekst']))
ukjent = [k for k in brukt if k not in pkt]
json.dump(dict(punkter=ut, ukjente_id=ukjent), open('resultat.json', 'w'), ensure_ascii=False, indent=1)
print('GVG-punkter', len(ut), 'ordrett på nbim.no i dag', sum(x['web'] for x in ut), 'ordrett i PDF 2024', sum(x['pdf'] for x in ut))
print('agent-id ukjente', ukjent)
for x in ut:
    if x['agent_n'] or not x['web']:
        print(x['id'], 'web', x['web'], 'pdf', x['pdf'], 'agentlik', x['agent_lik'], '|', x['avsnitt'][:50], '|', x['tekst'][:90])
