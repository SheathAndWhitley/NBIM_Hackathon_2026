"""#2731: forklar avvikene. (a) samme 400 rader, men 'tidligere' = (dato, meeting_id) leksikografisk før, som repoet.
(b) hele datasettet: hvor mange rader (og test 2024-2026) får trekk fra et annet møte SAMME dato."""
import sys, pathlib, numpy as np, pandas as pd
D = sys.argv[1]
R = pathlib.Path("arbeid/hack/CASE/20261105_155545_NBIM_Hackathon_2026-main_1__ut/NBIM_Hackathon_2026-main")
sys.path.insert(0, str(R / "src")); from stemmeagent import ballot
ballot.REAL_FILE = pathlib.Path(D); B = ballot.load_real()
base = B.loc[B.labelled & (B.split == 'train'), 'y'].mean(); L = B[B.labelled]
idx = np.random.default_rng(2731).choice(len(B), 400, replace=False)
K = ('prev_same_item', 'prev_same_person', 'prev_meeting_any_dev', 'hist_type_dev_rate')
def lik(a, b): return (np.isnan(a) and np.isnan(b)) or (not np.isnan(a) and not np.isnan(b) and abs(a - b) < 1e-9)
av = dict.fromkeys(K, 0); av_strikt_samme = 0
for i in idx:
    r = B.iloc[i]; c = r.company_id; S = L[L.company_id == c]
    P = S[(S.meeting_date < r.meeting_date) | ((S.meeting_date == r.meeting_date) & (S.meeting_id < r.meeting_id))].sort_values(['meeting_date', 'meeting_id', 'item_no'])
    q = P[P.item_key == r.item_key]; v = {'prev_same_item': float(q.y.iloc[-1]) if len(q) else np.nan}
    pk = r.person_key if isinstance(r.person_key, str) else None
    q = P[P.person_key == pk] if pk else P.iloc[:0]; v['prev_same_person'] = float(q.y.iloc[-1]) if len(q) else np.nan
    v['prev_meeting_any_dev'] = float(P[P.meeting_id == P.meeting_id.iloc[-1]].y.max()) if len(P) else np.nan
    q = P[P.proposal_type == r.proposal_type]; v['hist_type_dev_rate'] = (q.y.sum() + 5 * base) / (len(q) + 5)
    for k in K:
        if not lik(float(r[k]), v[k]): av[k] += 1
print('(a) avvik med repoets rekkefølge (dato, meeting_id):', av, 'sum', sum(av.values()))
# (b) hele datasettet: rader med et merket møte i samme selskap, samme dato, lavere meeting_id
m = L.groupby(['company_id', 'meeting_date']).meeting_id.min().rename('min_mid')
X = B.join(m, on=['company_id', 'meeting_date'])
berort = X.min_mid.notna() & (X.meeting_id > X.min_mid)
print('(b) rader som kan få trekk fra annet møte samme dato:', int(berort.sum()), 'av', len(B))
print('    per år:', X[berort].year.value_counts().sort_index().to_dict())
print('    møter berørt:', X[berort].meeting_id.nunique(), '| MOT blant berørte (merket):', int(X[berort & X.labelled].y.sum()), 'av', int((berort & X.labelled).sum()))
X[berort][['row_id', 'meeting_id', 'company_id', 'meeting_date', 'year', 'y']].to_csv('berorte_rader.csv', index=False)
