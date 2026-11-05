# F1-MOT på test 2026 for #2044 (miks h2) som funksjon av antall flagg. Bare til å beskrive følsomhet, ikke til valg.
import csv, sys
f = sys.argv[1] if len(sys.argv) > 1 else 'arbeid/oppgave_2044/pred_miks_h2.csv'
d = sorted([(float(x['p']), int(x['y'])) for x in csv.DictReader(open(f)) if x['y'] != ''], reverse=True)
n_mot = sum(y for _, y in d)
for k in [35, 45, 55, 60, 65, 71, 80, 90, 100, 115, 140, 176]:
    tp = sum(y for _, y in d[:k]); print(f'flagg {k:3d} p>={d[k-1][0]:.3f} F1 {2*tp/(k+n_mot):.3f}')
