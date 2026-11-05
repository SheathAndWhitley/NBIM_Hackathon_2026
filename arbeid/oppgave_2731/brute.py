"""#2731: brute force-sjekk av repo4s fire historikktrekk (ballot.add_history) på 400 tilfeldige rader.
For hver rad regnes trekket på nytt fra bunnen, bare fra merkede rader i samme selskap med møtedato
STRENGT før radens møtedato. Avvik = repoets verdi != brute force-verdi. Leser rådata, skriver ingenting frosset."""
import sys, pathlib, hashlib, numpy as np, pandas as pd
D = sys.argv[1]
print('sha256 rådata:', hashlib.sha256(open(D, 'rb').read()).hexdigest()[:8])
R = pathlib.Path("arbeid/hack/CASE/20261105_155545_NBIM_Hackathon_2026-main_1__ut/NBIM_Hackathon_2026-main")
sys.path.insert(0, str(R / "src")); from stemmeagent import ballot
ballot.REAL_FILE = pathlib.Path(D); B = ballot.load_real()
base = B.loc[B.labelled & (B.split == 'train'), 'y'].mean()
L = B[B.labelled]
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 2731)
idx = rng.choice(len(B), 400, replace=False)
avvik = {k: 0 for k in ('prev_same_item', 'prev_same_person', 'prev_meeting_any_dev', 'hist_type_dev_rate')}
ikke_tom = dict.fromkeys(avvik, 0); samme_dag = 0; eks = []
def lik(a, b): return (np.isnan(a) and np.isnan(b)) or (not np.isnan(a) and not np.isnan(b) and abs(a - b) < 1e-9)
for i in idx:
    r = B.iloc[i]; c = r.company_id
    P = L[(L.company_id == c) & (L.meeting_date < r.meeting_date)].sort_values(['meeting_date', 'meeting_id', 'item_no'])
    if ((L.company_id == c) & (L.meeting_date == r.meeting_date) & (L.meeting_id != r.meeting_id)).any(): samme_dag += 1
    q = P[P.item_key == r.item_key]; v = {'prev_same_item': float(q.y.iloc[-1]) if len(q) else np.nan}
    pk = r.person_key if isinstance(r.person_key, str) else None
    q = P[P.person_key == pk] if pk else P.iloc[:0]; v['prev_same_person'] = float(q.y.iloc[-1]) if len(q) else np.nan
    if len(P):
        lm = P[P.meeting_id == P.meeting_id.iloc[-1]]; v['prev_meeting_any_dev'] = float(lm.y.max())
    else: v['prev_meeting_any_dev'] = np.nan
    q = P[P.proposal_type == r.proposal_type]; v['hist_type_dev_rate'] = (q.y.sum() + 5 * base) / (len(q) + 5)
    for k in avvik:
        if not np.isnan(v[k]) and k != 'hist_type_dev_rate': ikke_tom[k] += 1
        if k == 'hist_type_dev_rate' and len(q): ikke_tom[k] += 1
        if not lik(float(r[k]), v[k]):
            avvik[k] += 1; eks.append((i, k, r[k], v[k], str(r.meeting_date)[:10], r.year))
print('rader:', len(idx), '| år i utvalget:', B.iloc[idx].year.value_counts().sort_index().to_dict())
print('avvik per trekk:', avvik, '| sum', sum(avvik.values()))
print('rader der trekket har historikk (ikke tomt/bare prior):', ikke_tom)
print('rader der samme selskap har annet møte SAMME dato:', samme_dag)
for e in eks[:15]: print('AVVIK', e)
