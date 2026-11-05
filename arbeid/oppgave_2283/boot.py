"""Parvis klyngebootstrap (møter) av F1-differanse t1 - grunnlinje. Bruk: python boot.py <år> <grunn.csv> <t1.csv>"""
import sys, numpy as np, pandas as pd
aar, fa, fb = int(sys.argv[1]), sys.argv[2], sys.argv[3]
d = pd.read_csv('state/opplastet/20261105_114241_real_votes.csv', low_memory=False)
d = d[(d.year == aar) & (d.injection_flag == 0) & d.against_board.notna()]
d['id'] = d.meeting_id.astype(int).astype(str) + '|' + d.item_no.astype(int).astype(str)
A = pd.read_csv(fa).set_index('id').anbefaling; B = pd.read_csv(fb).set_index('id').anbefaling
y = d.against_board.astype(int).values; a = d.id.map(A).values; b = d.id.map(B).values; m = d.meeting_id.values
def f1(y, p): tp = (y & p).sum(); return 2 * tp / max(2 * tp + (p & ~y.astype(bool)).sum() + (y.astype(bool) & ~p.astype(bool)).sum(), 1)
y = y.astype(bool); a = a.astype(bool); b = b.astype(bool)
def F(yy, pp): tp = (yy & pp).sum(); return 2 * tp / (2 * tp + (pp & ~yy).sum() + (yy & ~pp).sum())
print('grunn', round(F(y, a), 4), 't1', round(F(y, b), 4), 'diff', round(F(y, b) - F(y, a), 4))
u = np.unique(m); idx = {k: np.where(m == k)[0] for k in u}; r = np.random.default_rng(0); D = []
for _ in range(2000):
    s = np.concatenate([idx[k] for k in r.choice(u, len(u))]); D.append(F(y[s], b[s]) - F(y[s], a[s]))
D = np.array(D); print('95 % KI diff', np.round(np.quantile(D, [.025, .975]), 3), 'P(diff>0)', round((D > 0).mean(), 3))
