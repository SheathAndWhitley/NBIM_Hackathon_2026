"""Lekkasjetest for kjennetegn.csv (smed, #1958). Exit 0 = alle sjekker bestått.

1. id-er i kjennetegn = train ∪ test_input, ingen ekstra, ingen mangler.
2. fasit.csv brukes ikke: kjøring uten fasit.csv og med stokket fasit.csv gir byte-lik fil.
3. Holdout-stemmer kan ikke påvirke noe: test_input har ingen stemmekolonner, og all historikk
   (siste_hist_dato) ligger strengt før radens egen dato og før grensedatoen for test.
4. Tidsperturbasjon: stokk train-fasit for møter >= dato d. Kjennetegn for rader med dato <= d er uendret.
5. Brute force: 300 tilfeldige rader regnes på nytt med en naiv løkke og må stemme.
"""
import shutil, subprocess, sys, tempfile, hashlib
from pathlib import Path
import numpy as np
import pandas as pd

HER = Path(__file__).resolve().parent
LAG = HER / "lag_kjennetegn.py"
SPLITS = [HER.parent / s for s in ("data", "data_v3", "data_v3_val", "data_vif")]


def kjor(split):
    subprocess.run([sys.executable, "-I", str(LAG), str(split)], check=True, capture_output=True)
    return (split / "kjennetegn.csv").read_bytes()


def kopi(split, tmp, uten_fasit=False, stokk_fasit=False):
    d = Path(tmp) / split.name
    d.mkdir()
    for f in ("train.csv", "test_input.csv"):
        shutil.copy(split / f, d / f)
    if not uten_fasit and (split / "fasit.csv").exists():
        fa = pd.read_csv(split / "fasit.csv")
        if stokk_fasit:
            for c in fa.columns[1:]:
                fa[c] = np.random.default_rng(1).permutation(fa[c].values)
        fa.to_csv(d / "fasit.csv", index=False)
    return d


feil = 0
def sjekk(ok, tekst):
    global feil
    print(("OK   " if ok else "FEIL ") + tekst)
    feil += not ok


for split in SPLITS:
    print(f"== {split.name}")
    k = pd.read_csv(split / "kjennetegn.csv", dtype=str)
    tr = pd.read_csv(split / "train.csv", dtype=str, low_memory=False)
    te = pd.read_csv(split / "test_input.csv", dtype=str, low_memory=False)
    sjekk(set(k.id) == set(tr.id) | set(te.id) and len(k) == len(tr) + len(te), f"1 id-er matcher ({len(tr)} train + {len(te)} test)")
    lekk = [c for c in ("fasit", "avvik", "stemme", "mgmt_felt_LEKKER", "mot_ledelsen", "mot") if c in te.columns]
    sjekk(not lekk, f"3 test_input uten stemmekolonner {lekk}")
    orig = (split / "kjennetegn.csv").read_bytes()
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        a = kjor(kopi(split, t1, uten_fasit=True))
        b = kjor(kopi(split, t2, stokk_fasit=True))
    sjekk(a == orig and b == orig, "2 byte-lik uten fasit.csv og med stokket fasit.csv")
    grense = te.moetedato.min()
    hist = [c for c in k.columns if c.endswith("_siste_hist_dato")]
    verst = max((k[c].dropna().max() if k[c].notna().any() else "") for c in hist)
    tk = k[k.sett == "test"]
    tmax = max((tk[c].dropna().max() if tk[c].notna().any() else "") for c in hist)
    sjekk(tmax < grense, f"3 test-rader: nyeste historikk {tmax} < grense {grense}")
    strengt = all((k[c].isna() | (k[c] < k.moetedato)).all() for c in hist)
    sjekk(strengt, f"3 all historikk strengt før radens egen dato (nyeste brukt totalt {verst})")
    # 4 tidsperturbasjon
    d = sorted(tr.moetedato.unique())[len(tr.moetedato.unique()) // 2]
    with tempfile.TemporaryDirectory() as t3:
        dd = kopi(split, t3, uten_fasit=True)
        trp = tr.copy()
        sen = trp.moetedato >= d
        rng = np.random.default_rng(7)
        trp.loc[sen, "fasit"] = rng.choice(["FOR", "MOT"], sen.sum())
        trp.loc[sen, "avvik"] = rng.choice(["0", "1"], sen.sum())
        trp.to_csv(dd / "train.csv", index=False)
        kjor(dd)
        kp = pd.read_csv(dd / "kjennetegn.csv", dtype=str)
    tidlig = k.moetedato <= d
    lik = k[tidlig].reset_index(drop=True).equals(kp[tidlig].reset_index(drop=True))
    endret = not k[~tidlig].reset_index(drop=True).equals(kp[~tidlig].reset_index(drop=True))
    sjekk(lik, f"4 stokket train-fasit fra {d}: rader <= {d} uendret ({tidlig.sum()} rader)")
    sjekk(endret, "4 kontroll: senere rader endres faktisk (testen har kraft)")
    # 5 brute force
    trn = tr[tr.fasit.isin(["FOR", "MOT", "AVSTÅ"])].copy()
    trn["selskap"] = trn.cusip.fillna(trn.utsteder)
    kk = k.set_index("id")
    rng = np.random.default_rng(3)
    ok = True
    for i in rng.choice(len(k), min(300, len(k)), replace=False):
        r = k.iloc[i]
        h = trn[(trn.selskap == r.selskap) & (trn.moetedato < r.moetedato)]
        n = len(h)
        if int(r.sel_n_tidl) != n:
            ok = False; break
        if n and abs(float(r.sel_mot_andel_tidl) - (h.fasit == "MOT").mean()) > 1e-3:
            ok = False; break
    sjekk(ok, "5 300 tilfeldige rader stemmer med naiv omregning av sel_mot_andel_tidl")

print("ALLE BESTÅTT" if not feil else f"{feil} FEIL")
sys.exit(1 if feil else 0)
