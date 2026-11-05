"""#2086: bootstrap-95 %-KI for F1 på MOT (= against_board, rundens måler) for frysekandidaten og grunnlinjene.
Frysekandidat: kjor_agent.py standard (real_votes) = oppgave_2044/train.py --variant miks --hist 2, kjørt UENDRET
via runpy som i levering/c1_real.py. Grense og C velges i train.py på val 2025; test 2026 måles én gang.
Grunnlinjer: «følg styret» (F1 0) og presedensregelen «MOT hvis NBIM gikk mot styret i selskapet på et tidligere møte».
Bootstrap: B trekk (standard 2000), seed 0, trekk per selskap (company_id, klyngebootstrap) og per rad (info).
Ingen modellvalg skjer her. Kjør fra landsbymappen:
  uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2086/bootstrap_f1.py
"""
import contextlib, io, os, runpy, sys
import numpy as np, pandas as pd
ROT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REAL = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")
TRAIN = os.path.join(ROT, "arbeid/oppgave_2044/train.py")
B = int(os.environ.get("B", 2000))
sys.argv = [TRAIN, REAL, "--variant", "miks", "--hist", "2", "--ut", os.devnull]
logg = io.StringIO()
with contextlib.redirect_stdout(logg):
    g = runpy.run_path(TRAIN, run_name="__main__")
print("\n".join(l for l in logg.getvalue().splitlines() if l.startswith(("VAL", "TEST", "SCORE"))))
d, ok, t = g["d"], g["ok"], g["t"]
y_all = d.against_board
# presedens: MOT hvis selskapet har en sak med against_board=1 på et møte strengt før denne datoen (etikett kjent)
dato = pd.to_datetime(d.meeting_date)
s0 = pd.DataFrame({"k": d.company_id.astype(str), "dt": dato, "y": y_all.where(ok)}).reset_index()
gg = s0.dropna(subset=["y"]).groupby(["k", "dt"]).y.sum().reset_index().sort_values("dt")
gg["y"] = gg.groupby("k").y.cumsum()
q = s0[["index", "k", "dt"]].sort_values("dt")
m = pd.merge_asof(q, gg, on="dt", by="k", allow_exact_matches=False).set_index("index").sort_index()
presedens = (m.y.fillna(0).values > 0)
SETT = {"val 2025": (g["va"], g["pv"]), "test 2026": (g["te"], g["p"][g["te"]])}
f1 = lambda p, y: 2 * (p & y).sum() / max(p.sum() + y.sum(), 1)
ki = lambda v: np.percentile(v, [2.5, 97.5])
for navn, (maske, s) in SETT.items():
    y = y_all[maske].astype(int).values.astype(bool)
    kand = {"frysekandidat (miks h2)": s >= t, "presedensregel": presedens[maske], "følg styret": np.zeros(len(y), bool)}
    sel = d.company_id[maske].astype(str).values; us, inv = np.unique(sel, return_inverse=True)
    grp = [np.flatnonzero(inv == k) for k in range(len(us))]
    for modus in ("selskap", "rad"):
        rng = np.random.default_rng(0); bs = {k: np.empty(B) for k in kand}
        for b in range(B):
            idx = (np.concatenate([grp[k] for k in rng.integers(0, len(us), len(us))]) if modus == "selskap"
                   else rng.integers(0, len(y), len(y)))
            for k, p in kand.items(): bs[k][b] = f1(p[idx], y[idx])
        print(f"\n### {navn}: n {len(y)}, MOT {y.sum()}, selskaper {len(us)}, {B} trekk per {modus}, seed 0")
        print("| kandidat | F1 MOT | 95 % KI | P | R | flagget |\n|---|---|---|---|---|---|")
        for k, p in kand.items():
            lo, hi = ki(bs[k]); tp = (p & y).sum()
            print(f"| {k} | {f1(p, y):.3f} | [{lo:.3f}; {hi:.3f}] | {tp / max(p.sum(), 1):.3f} | {tp / y.sum():.3f} | {p.sum()} |")
        print("| forskjell, parvis (samme trekk) | ΔF1 | 95 % KI | andel trekk > 0 |\n|---|---|---|---|")
        for a_, b_ in [("frysekandidat (miks h2)", "presedensregel"), ("frysekandidat (miks h2)", "følg styret")]:
            dd = bs[a_] - bs[b_]; lo, hi = ki(dd)
            print(f"| {a_} − {b_} | {f1(kand[a_], y) - f1(kand[b_], y):+.3f} | [{lo:+.3f}; {hi:+.3f}] | {(dd > 0).mean():.3f} |")
