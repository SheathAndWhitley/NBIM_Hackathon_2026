"""Lekkasje- og tidsserietest for den leverte modellen (arbeid/hack/levering/modell_repo4.py), ca. 2 minutter.

Modellen kjøres UENDRET på endrede kopier av NBIMs stemmer, og svarene sammenlignes med en kjøring på originalen.
I tillegg regnes modellens rå sannsynligheter (logistisk regresjon og LightGBM) for testkjøringen på nytt med
skriptets egne funksjoner og valgt C, så ekte lekkasje skilles fra rangeringen på tvers av saker.
Bare 2026-etiketter endres i T2, T3 og T5, så testmodellen (trent på 2019-2025) er den samme; bare historikk kan endres.

  T0 uendret kopi              kontroll: alt identisk
  T1 fasitkolonner tømt        nbim_vote, nbim_vote_raw, rationale_* og position_paper blankes: alt identisk
  T2 framtidige etiketter      2026-etiketter fra 1. mai snus: saker før 1. mai får samme rå sannsynlighet og flagg
  T3a egen etikett, samme dag  alle etiketter på én 2026-dato snus: sakene den dagen får samme rå sannsynlighet
  T3b to møter samme dag       første møte snus: KJENT LEKKASJE, skriver hvor mange saker i det andre møtet som endres
  T4 stokkede etiketter        etikettene stokkes innen hvert år: F1 på MOT 2026 faller til sjansenivå (mot ekte fasit)
  T5 terskel uten 2026-fasit   alle 2026-etiketter fjernes: valideringsåret 2025 velger samme C og terskel

Bruk (fra repo-roten, etter sh KJOR.sh):  .venv_kjor/bin/python -B arbeid/hack/c1/lekkasjetest.py
"""
import contextlib
import io
import os
import shutil
import sys
import tempfile

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

ROT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.."))
MODELL = os.path.join(ROT, "arbeid/hack/levering/modell_repo4.py")
ORIG = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")
MAALER = os.path.join(ROT, "arbeid/hack/c1/leveranse/verktoy/maaler_aar.py")
REPO = "prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate"
if not os.path.exists(ORIG):
    sys.exit("mangler state/opplastet/...real_votes.csv: kjør sh KJOR.sh først")
UT = tempfile.mkdtemp(prefix="lekkasjetest_")

R = pd.read_csv(ORIG, dtype=str, keep_default_na=False)  # originalen som tekst; kopiene endrer bare valgte celler
ID = (R.meeting_id + "|" + R.item_no).values
AAR = R.year.astype(int).values
DATO = R.meeting_date.values
MERKET = (R.against_board != "").values
STYRET = R.mgmt_rec.replace("", "FOR").values
YS = ((R.nbim_vote == "MOT") & (R.against_board == "1.0")).values  # fasit «MOT mot styret» (som v3 --score mot)
T26 = (AAR == 2026) & MERKET & (R.injection_flag != "1").values
VA = (AAR == 2025) & MERKET


def kjor(datafil, bare_val=False):
    """Kjører modell_repo4.py uendret i en egen ordbok. bare_val: testdelen får feile (tomt testår i T5)."""
    g = {"__name__": "lekkasjetest", "__file__": MODELL}
    gammel = sys.argv
    sys.argv = [MODELL, datafil, "--variant", "miks", "--hist", "2", "--repo", REPO, "--ut", os.devnull]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                exec(compile(open(MODELL, encoding="utf-8").read(), MODELL, "exec"), g)
            except ValueError:
                if not bare_val:
                    raise
                return dict(C=g["C"], t=float(g["t"]), pv=np.asarray(g["pv_all"], float))
            tr = g["tr"]
            Xm = g["matrise"](tr, 2026)
            lr = LogisticRegression(C=g["C"], max_iter=4000, class_weight="balanced").fit(Xm[tr], g["y_all"][tr].astype(int))
            p_lr = lr.predict_proba(Xm)[:, 1]
            q = g["lgbm_pred"](Xm, tr, 2026)
    finally:
        sys.argv = gammel
    return dict(C=g["C"], t=float(g["t"]), p=np.asarray(g["p"], float), pv=np.asarray(g["pv_all"], float), p_lr=p_lr, q=q)


def f1_mot(p, t, maske=T26):
    xs = (p >= t) & (STYRET != "MOT")
    tp = int((xs & YS & maske).sum()); fp = int((xs & ~YS & maske).sum()); fn = int((~xs & YS & maske).sum())
    return round(2 * tp / (2 * tp + fp + fn), 4), tp, fp, fn


def kopi(navn, endre):
    X = R.copy(); endre(X); sti = os.path.join(UT, f"{navn}.csv"); X.to_csv(sti, index=False); return sti


def snu(X, maske):
    ab = X.against_board.copy()
    X.loc[maske & (ab == "1.0").values, "against_board"] = "0.0"
    X.loc[maske & (ab == "0.0").values, "against_board"] = "1.0"


def sammenlign(B, K, m):
    raa = max(float(np.max(np.abs(B["p_lr"][m] - K["p_lr"][m]))), float(np.max(np.abs(B["q"][m] - K["q"][m])))) if m.any() else 0.0
    return dict(rader=int(m.sum()), maks_diff_raa=raa, rangscore_endret=int((B["p"][m] != K["p"][m]).sum()),
                flagg_snudd=int(((B["p"][m] >= B["t"]) != (K["p"][m] >= K["t"])).sum()),
                C_og_val_lik=B["C"] == K["C"] and np.array_equal(B["pv"], K["pv"]))


rader = []
def rad(test, ok, tekst):
    utfall = "KJENT LEKKASJE" if ok is None else ("BESTÅTT" if bool(ok) else "IKKE BESTÅTT")
    rader.append((test, utfall, tekst))
    print(f"{test}: {utfall}  {tekst}", flush=True)

print("Grunnkjøring på originalen ...", flush=True)
B = kjor(ORIG)
f, tp, fp, fn = f1_mot(B["p"], B["t"])
print(f"  C={B['C']} terskel={B['t']:.5f}  F1 MOT 2026 {f} (TP {tp} FP {fp} FN {fn}); Mac gir 0,512, Linux 0,520", flush=True)

s = sammenlign(B, kjor(kopi("t0", lambda X: None)), T26)
rad("T0 uendret kopi", s["maks_diff_raa"] == 0 and s["rangscore_endret"] == 0 and s["C_og_val_lik"], f"{s}")

def t1(X):
    for k in ("nbim_vote", "nbim_vote_raw", "rationale_text", "rationale_section", "position_paper"): X[k] = ""
s = sammenlign(B, kjor(kopi("t1", t1)), np.ones(len(R), bool))
rad("T1 fasitkolonner tømt", s["maks_diff_raa"] == 0 and s["rangscore_endret"] == 0 and s["C_og_val_lik"], f"{s}")

D = "2026-05-01"
K = kjor(kopi("t2", lambda X: snu(X, (AAR == 2026) & (DATO >= D))))
s = sammenlign(B, K, T26 & (DATO < D))
rad(f"T2 etiketter fra {D} snudd", s["maks_diff_raa"] == 0 and s["flagg_snudd"] == 0,
    f"{s} (rangscoren kan flytte seg litt fordi scoren er en rang over alle saker; det som teller er rå sannsynlighet og flagg)")

par = R.groupby(["company_id", "meeting_date"]).meeting_id.nunique()
par = par[par > 1].reset_index()
D0 = next(d for d in pd.Series(DATO[T26]).value_counts().index if d not in set(par.meeting_date))
dag = T26 & (DATO == D0)
s = sammenlign(B, kjor(kopi("t3a", lambda X: snu(X, (AAR == 2026) & (DATO == D0)))), dag)
rad(f"T3a alle etiketter {D0} snudd", s["maks_diff_raa"] == 0, f"{s}")

forste, andre = np.zeros(len(R), bool), np.zeros(len(R), bool)
for c, dt in zip(par.company_id, par.meeting_date):
    if not dt.startswith("2026"):
        continue
    m = (R.company_id == c).values & (DATO == dt)
    ids = sorted(R.meeting_id[m].astype(int).unique())
    forste |= m & (R.meeting_id.astype(int).values == ids[0])
    andre |= m & (R.meeting_id.astype(int).values != ids[0])
K = kjor(kopi("t3b", lambda X: snu(X, forste)))
s = sammenlign(B, K, andre & T26)
endret = int(((B["p_lr"] != K["p_lr"]) | (B["q"] != K["q"]))[andre & T26].sum())
rad("T3b to møter samme dag", None if endret else True,
    f"{endret} av {s['rader']} saker i det andre møtet får endret sannsynlighet, {s['flagg_snudd']} flagg snur "
    "(historikktrekkene fra ballot.py regner møtet med lavest meeting_id som tidligere)")

rng = np.random.default_rng(0)
def t4(X):
    for aar in np.unique(AAR):
        m = np.where((AAR == aar) & MERKET)[0]
        X.loc[X.index[m], "against_board"] = X.against_board.values[rng.permutation(m)]
K = kjor(kopi("t4", t4))
f4 = f1_mot(K["p"], K["t"])
rad("T4 etiketter stokket innen år", f4[0] < 0.15, f"F1 MOT 2026 mot ekte fasit {f4[0]} (TP {f4[1]} FP {f4[2]} FN {f4[3]}), ekte etiketter gir {f}")

K = kjor(kopi("t5", lambda X: X.__setitem__("against_board", X.against_board.where(AAR != 2026, ""))), bare_val=True)
f5 = f1_mot(B["p"], K["t"])
rad("T5 terskel uten 2026-fasit", K["C"] == B["C"] and f5 == (f, tp, fp, fn),
    f"C {K['C']} (grunnkjøring {B['C']}), terskel {K['t']:.6f} ({B['t']:.6f}); F1 2026 med denne terskelen {f5[0]}")

print("\nOppsummering:")
for test, utfall, _ in rader:
    print(f"  {utfall:15s} {test}")
shutil.rmtree(UT, ignore_errors=True)  # kopiene av dataene slettes igjen
