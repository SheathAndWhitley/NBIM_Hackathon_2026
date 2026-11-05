"""#2283 KOPI av #2044 train.py + tiltak 1 (styrevalg-historikk forfaller, --t1). Bare val 2025, test 2026 kjøres IKKE.
MOT-modell på arrangørens real_votes (smed2 #2044). Predikerer stemmer MOT styret.
Bruk: uv run --project ../oppgave_2023 python train.py <real_votes.csv> [--variant lr|lgbm|miks]
- Bare hvitlistede kolonner (skrives ut). Forbudt: nbim_vote, nbim_vote_raw, rationale_text,
  rationale_section, funds_disagree, og position_paper (97,5 % MOT når satt = NBIMs egen begrunnelse).
- Historikk (tidligere MOT i selskapet / samme tekst) bruker bare etiketter fra år før året som
  predikeres: val 2025 ser <2025, test 2026 ser <2026. Ingen etiketter fra samme sesong.
- C og grense velges på val 2025 (trent <2025). Test 2026 kjøres én gang med valgt grense.
"""
import sys, re, argparse, json, pandas as pd, numpy as np, scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score, average_precision_score

FORBUDT = {'nbim_vote', 'nbim_vote_raw', 'rationale_text', 'rationale_section', 'funds_disagree', 'position_paper'}
KAT = ['proposal_type', 'proponent', 'mgmt_rec', 'mgmt_rec_raw', 'country', 'market']
TEKST = 'proposal_text'
HIST_NOKLER = ['company_id', 'proposal_text', 'meeting_date', 'year']  # historikk: bare eldre års etiketter
a = argparse.ArgumentParser(); a.add_argument('data'); a.add_argument('--variant', default='lr')
a.add_argument('--ut', default='pred_test.csv'); a.add_argument('--person', type=int, default=0); a.add_argument('--hist', type=int, default=1)
a.add_argument('--t1', type=int, default=0); a.add_argument('--tau', type=float, default=1.0); a.add_argument('--vaar', type=int, default=2025)
a = a.parse_args()
d = pd.read_csv(a.data, low_memory=False)
BRUKT = list(dict.fromkeys(KAT + [TEKST] + (HIST_NOKLER if a.hist else []) + ['item_no']))
assert not (set(BRUKT) & FORBUDT), set(BRUKT) & FORBUDT
print('FEATURES (kolonner lest av modellen):', sorted(set(BRUKT)))
print('FORBUDT og ikke brukt:', sorted(FORBUDT), '| snitt med brukt:', set(BRUKT) & FORBUDT)
y_all = d.against_board  # kun mål, aldri feature for samme rad
ok = ((d.injection_flag == 0) & y_all.notna()).values
X = d[BRUKT].copy()  # alt under leser bare X + etiketter fra tidligere år
norm = X[TEKST].fillna('').str.lower().map(lambda s: ' '.join(re.sub(r'[^a-z ]', ' ', s).split()))

DATO = pd.to_datetime(X.meeting_date)
STOPP = set('elect reelect re director directors as and audit committee member members outside independent non executive of the '
            'supervisory board reappoint appoint nomination compensation withdrawn resolution a for to designated company '
            'subsidiaries u s statutory alternate chairman chair deputy vice representative inside external internal '
            'remuneration risk dr mr ms mrs new candidate employee'.split())
def _navn(t):
    w = [x for x in t.split() if x not in STOPP and len(x) > 1]
    return ' '.join(sorted(w)) if len(w) >= 2 else None
# person = styremedlemmets navn (bare styrevalg); tom -> unik nøkkel uten historikk
person = pd.Series([(_navn(t) if pt == 'DIRECTOR_ELECTION' else None) for t, pt in zip(norm, X.proposal_type)], index=X.index)
person = person.where(person.notna(), '_' + X.index.astype(str))

# --- tiltak 1 (#2283): forfallende MOT-historikk på styrevalg. Bare etiketter og rationale_section fra år < radens år.
SEK = ['GVG 1.1', 'GVG 1.2', 'GVG 1.3', 'GVG 2.1', 'GVG 2.3', 'GVG 3.1', 'GVG 3.2']
_T1 = None
def t1_feats():
    global _T1
    if _T1 is not None: return _T1
    de = (X.proposal_type == 'DIRECTOR_ELECTION').values
    yr = X.year.values; comp = X.company_id.astype(str).values; pers = person.values
    sek = d.rationale_section.fillna('').values  # leses bare fra rader i år < radens år (historikk)
    yv_ = y_all.values
    # per (selskap, år): antall styrevalg, antall MOT, MOT per seksjon
    from collections import defaultdict
    cy = defaultdict(lambda: [0, 0, defaultdict(int)]); py = defaultdict(dict)
    for i in np.where(de & ok)[0]:
        c = cy[(comp[i], yr[i])]; c[0] += 1
        if yv_[i] == 1: c[1] += 1; c[2][sek[i]] += 1
        if not pers[i].startswith('_'): py[pers[i]][yr[i]] = max(py[pers[i]].get(yr[i], 0), int(yv_[i]))
    aarliste = defaultdict(list)
    for (c_, y_) in cy: aarliste[c_].append(y_)
    nf = 8 + len(SEK)
    F = np.zeros((len(X), nf))
    for i in np.where(de)[0]:
        Y = yr[i]; fl = sorted(a_ for a_ in aarliste[comp[i]] if a_ < Y)
        dec = 0.0; siste_mot = None; sek_dec = np.zeros(len(SEK))
        for a_ in fl:
            n, m, ss = cy[(comp[i], a_)]
            w = np.exp(-(Y - a_ - 1) / a.tau)
            dec += w * m / max(n, 1)
            if m: siste_mot = a_
            for k, s_ in enumerate(SEK): sek_dec[k] += w * ss.get(s_, 0) / max(n, 1)
        sist = fl[-1] if fl else None
        F[i, 0] = dec
        F[i, 1] = min(Y - siste_mot, 8) / 8 if siste_mot else 1.0           # år siden siste MOT (1 = aldri)
        F[i, 2] = (cy[(comp[i], sist)][1] / max(cy[(comp[i], sist)][0], 1)) if sist else 0  # MOT-andel siste sesong
        F[i, 3] = float(sist is not None and cy[(comp[i], sist)][1] == 0 and siste_mot is not None)  # MOT før, men alt FOR siste sesong
        ph = {k: v for k, v in py.get(pers[i], {}).items() if k < Y}
        if ph:
            ls = max(ph); F[i, 4] = 1; F[i, 5] = ph[ls]                      # personen sett, siste stemme MOT?
            pm = [k for k, v in ph.items() if v]; F[i, 6] = (min(Y - max(pm), 8) / 8) if pm else 1.0
            F[i, 7] = float(bool(pm) and ph[ls] == 0)                        # personen MOT før, FOR sist
        F[i, 8:] = sek_dec
    _T1 = [F[:, j] for j in range(nf)]
    return _T1

def hist_feats(til_aar):
    """For hver rad: MOT-statistikk i samme selskap, selskap+tekst og tekst.
    --hist 1: bare etiketter fra år < til_aar. --hist 2 (løpende): etiketter fra møter strengt før radens
    dato (NBIM publiserer stemmer løpende), men aldri fra år > til_aar."""
    lab = ok & (X.year <= til_aar if a.hist == 2 else X.year < til_aar).values
    yy = y_all.where(lab)
    out = []
    keys = [X.company_id.astype(str), X.company_id.astype(str) + '|' + norm, norm]
    if a.person: keys.append(person)
    for key in keys:
        if a.hist == 2:
            s0 = pd.DataFrame({'k': key, 'dt': DATO, 'y': yy})
            g = s0.dropna().groupby(['k', 'dt']).y.agg(['sum', 'count']).reset_index().sort_values('dt')
            g[['sum', 'count']] = g.groupby('k')[['sum', 'count']].cumsum().values
            q = s0[['k', 'dt']].reset_index().sort_values('dt')
            m = pd.merge_asof(q, g, on='dt', by='k', allow_exact_matches=False).set_index('index').sort_index()
            s = m['sum'].fillna(0).values; c = m['count'].fillna(0).values
        else:
            g = pd.DataFrame({'k': key, 'y': yy}).dropna().groupby('k').y.agg(['sum', 'count'])
            s = key.map(g['sum']).fillna(0).values; c = key.map(g['count']).fillna(0).values
        out += [np.log1p(c), (s + 0.05) / (c + 1), s > 0]
    if a.t1: out += t1_feats()
    return np.c_[tuple(out)].astype(float)

def matrise(fit, til_aar):
    kat = X[KAT].fillna('NA').astype(str)
    kat['tk'] = kat.proposal_type + '|' + kat.proponent + '|' + kat.mgmt_rec
    kat['item'] = np.minimum(X.item_no.fillna(0), 20).astype(int).astype(str)
    M = [OneHotEncoder(handle_unknown='ignore', min_frequency=5).fit(kat[fit]).transform(kat)]
    tv = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_features=50000, sublinear_tf=True).fit(norm[fit])
    M.append(tv.transform(norm))
    if a.hist: M.append(sp.csr_matrix(hist_feats(til_aar)))
    return sp.hstack(M).tocsr()

def lgbm_pred(Xm, tr, til_aar):
    import lightgbm as lgb
    kat = X[KAT].fillna('NA').astype('category')
    D = pd.concat([kat.reset_index(drop=True), pd.DataFrame(hist_feats(til_aar))], axis=1); D.columns = [str(c) for c in D.columns]
    m = lgb.LGBMClassifier(n_estimators=400, learning_rate=0.03, num_leaves=15, min_child_samples=20,
                           subsample=0.8, subsample_freq=1, colsample_bytree=0.8, is_unbalance=True, n_jobs=4, verbose=-1)
    m.fit(D[tr], y_all[tr].astype(int)); return m.predict_proba(D)[:, 1]

def pred(tr, til_aar, C):
    Xm = matrise(tr, til_aar)
    p = None
    if a.variant in ('lr', 'miks'):
        m = LogisticRegression(C=C, max_iter=4000, class_weight='balanced').fit(Xm[tr], y_all[tr].astype(int))
        p = m.predict_proba(Xm)[:, 1]
    if a.variant in ('lgbm', 'miks'):
        q = lgbm_pred(Xm, tr, til_aar)
        p = q if p is None else (pd.Series(p).rank(pct=True).values + pd.Series(q).rank(pct=True).values) / 2
    return p

def maal(y, s, t):
    yh = s >= t
    return dict(F1=round(f1_score(y, yh), 4), P=round(precision_score(y, yh, zero_division=0), 4),
                R=round(recall_score(y, yh), 4), n_pred_MOT=int(yh.sum()), n_MOT=int(y.sum()), n=len(y),
                PRAUC=round(average_precision_score(y, s), 4))

# 1) velg C og grense på val 2025 (trent på <2025, historikk <2025)
tr_v = ok & (X.year < a.vaar).values; va = ok & (X.year == a.vaar).values; yv = y_all[va].astype(int).values
best = (-1,)
for C in ([0.1, 0.3, 1, 3] if a.variant != 'lgbm' else [1]):
    p = pred(tr_v, a.vaar, C)
    for t in np.unique(np.quantile(p[va], np.linspace(0.80, 0.995, 80))):
        f = f1_score(yv, p[va] >= t)
        if f > best[0]: best = (f, C, t, p[va])
f, C, t, pv = best
print(f"VAL {a.vaar}: C={C} grense={t:.4f}", maal(yv, pv, t))
# grensen overføres som andel flagget (skalaen kan flytte seg når treningen vokser)
andel = (pv >= t).mean()
# 2) TEST 2026 KJØRES IKKE (#2283). Skriv val-prediksjoner i måler-format.
import csv
P = dict(zip(d.index[va], pv))
with open(a.ut, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['id', 'anbefaling', 'konfidens', 'p_avvik'])
    for j, r in d[d.year == a.vaar].iterrows():
        p_ = P.get(j)
        w.writerow([f"{int(r.meeting_id)}|{int(r.item_no)}", int(p_ >= t) if p_ is not None else 0, 0.9, round(float(p_), 5) if p_ is not None else 0.0])
de_va = (X.proposal_type[va] == 'DIRECTOR_ELECTION').values
print('STYREVALG val:', maal(yv[de_va], pv[de_va], t))
print('skrev', a.ut)
