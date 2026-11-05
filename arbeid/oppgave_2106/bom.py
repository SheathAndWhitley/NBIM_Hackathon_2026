import sys; sys.argv=[sys.argv[0]]
exec(open('arbeid/oppgave_2106/evaluer.py').read().split('if __name__')[0])
import pandas as pd
for år in (2025, 2026):
    D = kjor(år, 0, 12, 0, True); D['ok'] = D.sek == D.fasit
    print(år, D.groupby('type').ok.agg(['mean', 'count']).sort_values('count', ascending=False).to_string())
    print(D[~D.ok][['type', 'tekst', 'fasit', 'sek', 'nabo']].head(25).to_string())
