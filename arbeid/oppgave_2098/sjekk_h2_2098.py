import sys, numpy as np, pandas as pd
src = open('abl.py').read().split('\n')
sys.argv = ['abl.py', 'rv.csv', '--hist', '2']
exec('\n'.join(src[:65]))
H = hist_feats(2026)
rng = np.random.default_rng(0)
idx = rng.choice(np.where(d.year.values >= 2025)[0], 400, replace=False)
keys = [X.company_id.astype(str), X.company_id.astype(str) + '|' + norm, norm]
lab = ok & (d.year <= 2026).values
feil = 0; samme_mote = 0
for i in idx:
    for j, key in enumerate(keys):
        m = lab & (key.values == key.values[i]) & (DATO.values < DATO.values[i])
        c = m.sum(); s = y_all[m].sum()
        if not (np.isclose(H[i, 3*j], np.log1p(c)) and np.isclose(H[i, 3*j+1], (s+.05)/(c+1))): feil += 1
        mm = lab & (key.values == key.values[i]) & (d.meeting_id.values == d.meeting_id.values[i])
        # bidrar noen rad fra samme møte? da må den ha dato < radens dato (umulig)
        samme_mote += (m & mm).sum()
print('rader sjekket', len(idx), 'avvik mot brute force:', feil, 'etiketter fra samme møte brukt:', samme_mote)
