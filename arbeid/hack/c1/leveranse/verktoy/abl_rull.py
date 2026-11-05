"""#2733: flyttbar kopi av oppgave_2567/abl_rull.py (bare ballot-importen endret: relativ sti).
#2496: rullende kopi av oppgave_2490/abl.py, --testaar T: C/grense velges på T-1 (trent <T-1), test T (trent <T).
#2490: kopi av oppgave_2103/abl.py (= frossen #2044) + --repo: NBIM-repoets historikktrekk (ballot.add_history).
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
a.add_argument('--ut', default='pred_test.csv'); a.add_argument('--person', type=int, default=0); a.add_argument('--hist', type=int, default=1); a.add_argument('--utentype', type=int, default=0); a.add_argument('--repo', default=''); a.add_argument('--testaar', type=int, default=2026)
a = a.parse_args(); TA = a.testaar; VA = TA - 1
if a.utentype: KAT = [k for k in KAT if k != 'proposal_type']  # ablasjon: uten sakstype
d = pd.read_csv(a.data, low_memory=False)
BRUKT = list(dict.fromkeys(KAT + (['proposal_type'] if a.person else []) + [TEKST] + (HIST_NOKLER if a.hist else []) + ['item_no']))
assert not (set(BRUKT) & FORBUDT), set(BRUKT) & FORBUDT
print('FEATURES (kolonner lest av modellen):', sorted(set(BRUKT)))
print('FORBUDT og ikke brukt:', sorted(FORBUDT), '| snitt med brukt:', set(BRUKT) & FORBUDT)
y_all = d.against_board  # kun mål, aldri feature for samme rad
ok = ((d.injection_flag == 0) & y_all.notna()).values
X = d[BRUKT].copy()  # alt under leser bare X + etiketter fra tidligere år
norm = X[TEKST].fillna('').str.lower().map(lambda s: ' '.join(re.sub(r'[^a-z ]', ' ', s).split()))

DATO = pd.to_datetime(d.meeting_date)
STOPP = set('elect reelect re director directors as and audit committee member members outside independent non executive of the '
            'supervisory board reappoint appoint nomination compensation withdrawn resolution a for to designated company '
            'subsidiaries u s statutory alternate chairman chair deputy vice representative inside external internal '
            'remuneration risk dr mr ms mrs new candidate employee'.split())
def _navn(t):
    w = [x for x in t.split() if x not in STOPP and len(x) > 1]
    return ' '.join(sorted(w)) if len(w) >= 2 else None
# person = styremedlemmets navn (bare styrevalg); tom -> unik nøkkel uten historikk
person = pd.Series([(_navn(t) if pt == 'DIRECTOR_ELECTION' else None) for t, pt in zip(norm, d.proposal_type)], index=X.index)
person = person.where(person.notna(), '_' + X.index.astype(str))
def hist_feats(til_aar):
    """For hver rad: MOT-statistikk i samme selskap, selskap+tekst og tekst.
    --hist 1: bare etiketter fra år < til_aar. --hist 2 (løpende): etiketter fra møter strengt før radens
    dato (NBIM publiserer stemmer løpende), men aldri fra år > til_aar."""
    lab = ok & (d.year <= til_aar if a.hist == 2 else d.year < til_aar).values
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
    return np.c_[tuple(out)].astype(float)

REPO_TREKK = None
if a.repo:  # repoets trekk, løpende: bare etiketter fra tidligere møter (oppdatert etter hele møtet)
    import pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from stemmeagent import ballot  # #2733: kopi av NBIM-repoets ballot.py ved siden av
    ballot.REAL_FILE = pathlib.Path(a.data); B = ballot.load_real()
    assert len(B) == len(d) and (B.meeting_id.values == d.meeting_id.values).all()
    kol = []
    for k in a.repo.split(','):
        if k in ('prev_same', 'prev_same_item', 'prev_same_person', 'prev_meeting_any_dev'):
            kol += [(B[k] == 1).astype(float).rename(k + '_ja'), (B[k] == 0).astype(float).rename(k + '_nei')]
        else: kol.append(B[k].astype(float).fillna(0))
    REPO_TREKK = pd.concat(kol, axis=1).values
    print('REPO-TREKK:', a.repo, REPO_TREKK.shape, 'snitt', REPO_TREKK.mean(0).round(4))

def matrise(fit, til_aar):
    kat = X[KAT].fillna('NA').astype(str)
    kat['tk'] = (kat.proposal_type + '|' if 'proposal_type' in kat else '') + kat.proponent + '|' + kat.mgmt_rec
    kat['item'] = np.minimum(X.item_no.fillna(0), 20).astype(int).astype(str)
    M = [OneHotEncoder(handle_unknown='ignore', min_frequency=5).fit(kat[fit]).transform(kat)]
    tv = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_features=50000, sublinear_tf=True).fit(norm[fit])
    M.append(tv.transform(norm))
    if a.hist: M.append(sp.csr_matrix(hist_feats(til_aar)))
    if REPO_TREKK is not None: M.append(sp.csr_matrix(REPO_TREKK))
    return sp.hstack(M).tocsr()

def lgbm_pred(Xm, tr, til_aar):
    import lightgbm as lgb
    kat = X[KAT].fillna('NA').astype('category')
    D = pd.concat([kat.reset_index(drop=True)] + ([pd.DataFrame(hist_feats(til_aar))] if a.hist else []) + ([pd.DataFrame(REPO_TREKK, columns=[f'r{i}' for i in range(REPO_TREKK.shape[1])])] if REPO_TREKK is not None else []), axis=1); D.columns = [str(c) for c in D.columns]
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

# 1) velg C og grense på val VA (trent på <VA, historikk <VA)
tr_v = ok & (d.year < VA).values; va = ok & (d.year == VA).values; yv = y_all[va].astype(int).values
best = (-1,); pv_all = None
for C in ([0.1, 0.3, 1, 3] if a.variant != 'lgbm' else [1]):
    p = pred(tr_v, VA, C)
    for t in np.unique(np.quantile(p[va], np.linspace(0.80, 0.995, 80))):
        f = f1_score(yv, p[va] >= t)
        if f > best[0]: best = (f, C, t, p[va]); pv_all = p.copy()
f, C, t, pv = best
print(f"VAL {VA}: C={C} grense={t:.4f}", maal(yv, pv, t))
# grensen overføres som andel flagget (skalaen kan flytte seg når treningen vokser)
andel = (pv >= t).mean()
# 2) tren på <TA, historikk <TA, test TA én gang
tr = ok & (d.year < TA).values; te = ok & (d.year == TA).values; yt = y_all[te].astype(int).values
p = pred(tr, TA, C)
print(f"TEST {TA} (rå grense fra val {t:.4f}):", maal(yt, p[te], t))
t2 = np.quantile(p[te], 1 - andel)
print(f"TEST {TA} (samme andel flagget som val {andel:.4f}, merk: bruker test-fordeling uten etiketter):", maal(yt, p[te], t2))
pd.DataFrame({'rad': d.index[te], 'p': p[te], 'mot_pred': (p[te] >= t).astype(int), 'y': yt}).to_csv(a.ut, index=False)
def skriv(fil, aar, pp, tt):
    m = (d.year == aar).values; ids = pd.read_csv(a.data, dtype=str, usecols=['meeting_id', 'item_no'])
    pd.DataFrame({'id': ids.meeting_id[m] + '|' + ids.item_no[m], 'anbefaling': (pp[m] >= tt).astype(int), 'p_avvik': pp[m]}).to_csv(fil, index=False)
skriv(a.ut.replace('.csv', '_val.csv'), VA, pv_all, t); skriv(a.ut.replace('.csv', '_test.csv'), TA, p, t)
print('SCORE', maal(yt, p[te], t)['F1'])
