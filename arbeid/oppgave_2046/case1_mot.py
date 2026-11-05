"""Case 1, oppgave #2046 (smed): systemet flagger stemmer MOT styret; hovedtall F1 på MOT, mot 'følg styret' (F1 0).

Én kommando:  uv run python arbeid/oppgave_2046/case1_mot.py
Protokoll (låst før test ble sett):
  - Tidssplitt på møtedato. real_votes: møteår. npx: arrangørens split_year (sesonggrense på møtedato).
    Tren <=2024, velg alt (C, segmentvalg, terskel) på val 2025, test 2026 kjøres én gang, ingen refit.
  - Forbudte kolonner brukes aldri: rationale_text, rationale_section, position_paper, nbim_vote*, funds_disagree.
    n_funds brukes heller ikke (uavklart). injection_flag==1 holdes utenfor trening og måling.
  - Features: forslagstype, forslagsstiller, styrets anbefaling, land, marked, tfidf på forslagstekst,
    selskapets MOT-historikk og samme tekst i samme selskap, bare fra møter med strengt tidligere dato,
    og møtestruktur (antall punkter, antall aksjonærforslag i møtet).
  - Logreg uten klassevekt (sannsynligheter brukes til ruting). Terskel = maks F1 på val 2025.
  - Segmentvalg på val: aksjonærforslag der styret er imot tas enten med regelen (-> MOT) eller med modellen.
  - Ruting: forventet feil (1-p om flagget MOT, p om FOR). Grensen settes på val 2025 slik at 5 % / 10 %
    av val-sakene går til menneske, og samme grense brukes uendret på test (antallet på test blir det det blir).
    Vi rapporterer maskinen alene (ingen ruting), antall rutede og MOT blant dem, maskinen på de ikke-rutede,
    og systemet med antakelsen at mennesket stemmer som NBIM (orakel, øvre grense, sagt rett ut).
"""
import re, sys, json, numpy as np, pandas as pd, scipy.sparse as sp
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score

ROT = Path(__file__).resolve().parents[2]
FILER = {'real_votes': ROT / 'arbeid/hack/CASE/20261105_114241_real_votes.csv',
         'npx': ROT / 'arbeid/hack/CASE/20261105_114301_npx_votes.csv'}
FORBUDT = {'rationale_text', 'rationale_section', 'position_paper', 'nbim_vote', 'nbim_vote_raw', 'funds_disagree', 'n_funds'}
UT = Path(__file__).resolve().parent
BARE_VAL = '--bare-val' in sys.argv


def last(navn):
    d = pd.read_csv(FILER[navn], low_memory=False)
    d['dt'] = pd.to_datetime(d.meeting_date)
    d['aar'] = d.split_year if 'split_year' in d else d.dt.dt.year
    d['lab'] = (d.injection_flag == 0) & d.against_board.notna()
    d['y'] = d.against_board.fillna(0).astype(int)
    d['sh_mot'] = (d.proponent == 'Shareholder') & (d.mgmt_rec == 'MOT')
    return d


def historikk(d, nokkel):
    """MOT-sum og antall for nøkkelen fra møter med strengt tidligere dato (bare merkede rader)."""
    s = pd.DataFrame({'k': nokkel, 'dt': d.dt, 'y': d.y.where(d.lab)})
    g = s.dropna(subset=['y']).groupby(['k', 'dt']).y.agg(['sum', 'count']).reset_index()
    g = g.sort_values('dt')
    g[['cs', 'cc']] = g.groupby('k')[['sum', 'count']].cumsum().values
    q = s[['k', 'dt']].reset_index().sort_values('dt')
    m = pd.merge_asof(q, g[['k', 'dt', 'cs', 'cc']], on='dt', by='k', allow_exact_matches=False)
    m = m.set_index('index').sort_index()[['cs', 'cc']].fillna(0)
    return m.cs.values, m.cc.values


def features(d, fit):
    kat = d[['proposal_type', 'proponent', 'mgmt_rec', 'country', 'market']].fillna('NA').astype(str)
    kat['tk'] = kat.proposal_type + '|' + kat.proponent + '|' + kat.mgmt_rec
    kat['lt'] = kat.country + '|' + kat.proposal_type
    oh = OneHotEncoder(handle_unknown='ignore', min_frequency=5).fit(kat[fit])
    tekst = d.proposal_text.fillna('')
    tv = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_features=50000, sublinear_tf=True).fit(tekst[fit])
    norm = tekst.str.lower().map(lambda x: ' '.join(re.sub(r'[^a-z ]', ' ', x).split()))
    cs, cc = historikk(d, d.company_id.astype(str))
    ts, tc = historikk(d, d.company_id.astype(str) + '|' + norm)
    mote = d.groupby('meeting_id').proposal_text.transform('size').values
    mote_sh = d.groupby('meeting_id').proponent.transform(lambda s: (s == 'Shareholder').sum()).values
    num = np.c_[np.log1p(cc), (cs + 0.05) / (cc + 1), cs > 0, ts > 0, (tc > 0) & (ts == 0), ts / (tc + 1),
                np.log1p(mote), np.log1p(mote_sh)]
    return sp.hstack([oh.transform(kat), tv.transform(tekst), sp.csr_matrix(num.astype(float))]).tocsr()


def mal(y, yh):
    return dict(n=int(len(y)), MOT=int(y.sum()), treff=float((y == yh).mean()), flagget=int(yh.sum()),
                P=float(precision_score(y, yh, zero_division=0)), R=float(recall_score(y, yh, zero_division=0)),
                F1=float(f1_score(y, yh, zero_division=0)))


def system(p, t, sh_mot, regel_sh):
    yh = (p >= t).astype(int)
    if regel_sh: yh = np.where(sh_mot, 1, yh)
    feil = np.where(yh == 1, 1 - p, p)
    if regel_sh: feil = np.where(sh_mot, 1 - p, feil)
    return yh, feil


def rut(y, yh, feil, grense):
    r = feil >= grense
    yh = yh.copy(); yh[r] = y[r]
    return yh, r


def kjor(navn):
    d = last(navn)
    BRUKT = {'proposal_type', 'proponent', 'mgmt_rec', 'country', 'market', 'proposal_text', 'company_id', 'meeting_id',
             'meeting_date', 'split_year', 'against_board', 'injection_flag'}  # against_board bare som mål og fortidshistorikk
    assert not (FORBUDT & BRUKT) and not any(c.startswith(('nbim_vote', 'rationale_')) for c in BRUKT)
    tr = (d.lab & (d.aar <= 2024)).values; va = (d.lab & (d.aar == 2025)).values; te = (d.lab & (d.aar == 2026)).values
    X = features(d, tr); y = d.y.values; sh = d.sh_mot.values
    best = None
    for C in [0.1, 0.3, 1, 3, 10]:
        p = LogisticRegression(C=C, max_iter=4000).fit(X[tr], y[tr]).predict_proba(X)[:, 1]
        for regel in [False, True]:
            for t in np.arange(0.01, 0.9, 0.01):
                yh, _ = system(p[va], t, sh[va], regel)
                f = f1_score(y[va], yh)
                if best is None or f > best[0]: best = (f, C, round(float(t), 2), regel, p)
    f, C, t, regel, p = best
    valg = dict(C=C, terskel=t, regel_for_sh_mot=regel, val_F1=round(f, 4))
    _, fv = system(p[va], t, sh[va], regel)
    grenser = {0: np.inf, 0.05: np.quantile(fv, 0.95), 0.10: np.quantile(fv, 0.90)}
    valg['rutegrense_5'] = round(float(grenser[0.05]), 4); valg['rutegrense_10'] = round(float(grenser[0.10]), 4)
    res = {'valg': valg, 'val': {}, 'test': {}}
    for nm, m in [('val', va)] + ([] if BARE_VAL else [('test', te)]):
        yy = y[m]; seg = d.proponent.values[m]
        r = res[nm]
        r['folg_styret'] = mal(yy, np.zeros_like(yy))
        r['regel_sh_mot'] = mal(yy, sh[m].astype(int))
        r['regel_alle_sh'] = mal(yy, (seg == 'Shareholder').astype(int))
        yh, feil = system(p[m], t, sh[m], regel)
        r['maskin_alene'] = mal(yy, yh)
        for a in [0, 0.05, 0.10]:
            g = grenser[a]
            yr, ruta = rut(yy, yh, feil, g)
            r[f'system_rut{int(a*100)}'] = mal(yy, yr)
            r[f'system_rut{int(a*100)}'].update(grense=float(g), rutet=int(ruta.sum()), rutet_andel=float(ruta.mean()),
                                                 MOT_blant_rutet=int(yy[ruta].sum()))
            r[f'maskin_ikke_rutet{int(a*100)}'] = mal(yy[~ruta], yh[~ruta])
            rng = np.random.default_rng(0); bs = []
            for _ in range(1000):
                i = rng.integers(0, len(yy), len(yy)); bs.append(((yr[i] == yy[i]).mean() - (yy[i] == 0).mean(), f1_score(yy[i], yr[i])))
            bs = np.array(bs); r[f'system_rut{int(a*100)}']['ki95_treff_gevinst'] = [float(x) for x in np.percentile(bs[:, 0], [2.5, 97.5])]
            r[f'system_rut{int(a*100)}']['ki95_F1'] = [float(x) for x in np.percentile(bs[:, 1], [2.5, 97.5])]
            for s in ['Management', 'Shareholder']:
                r[f'system_rut{int(a*100)}_{s}'] = mal(yy[seg == s], yr[seg == s])
        for s in ['Management', 'Shareholder']:
            r[f'folg_styret_{s}'] = mal(yy[seg == s], np.zeros((seg == s).sum(), int))
    if not BARE_VAL: pd.DataFrame({'rad': d.index[te], 'p': p[te], 'flagg': system(p[te], t, sh[te], regel)[0]}).to_csv(UT / f'pred_{navn}_2026.csv', index=False)
    return res


if __name__ == '__main__':
    alle = {n: kjor(n) for n in FILER}
    if not BARE_VAL: (UT / 'resultat.json').write_text(json.dumps(alle, indent=1, ensure_ascii=False))
    for n, r in alle.items():
        print(f"\n== {n}  valg på val 2025: {r['valg']}")
        for nm in r['val'] and (['val'] if BARE_VAL else ['val', 'test']):
            for k, v in r[nm].items():
                print(f"{nm:4} {k:32} n {v['n']:6} MOT {v['MOT']:4} treff {v['treff']:.4f}  flagget {v['flagget']:4}  P {v['P']:.3f} R {v['R']:.3f} F1 {v['F1']:.3f}" + (f"  rutet {v['rutet']} (MOT {v['MOT_blant_rutet']})" if 'rutet' in v else '') + (f"  KI95 gevinst {v['ki95_treff_gevinst'][0]:+.4f}..{v['ki95_treff_gevinst'][1]:+.4f} F1 {v['ki95_F1'][0]:.3f}..{v['ki95_F1'][1]:.3f}" if 'ki95_F1' in v else ''))
