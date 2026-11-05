"""#2193: P, R og F1 på MOT mot styret for 7 terskler, på val 2025 og test 2026, maskin alene (ingen sone).
Viser juryen at terskelen er valgt på val (S2 i JURY_SPORSMAL): agentens t er val-F1-optimal, og den valgte raden
er ikke den beste på test. Modellen kjøres UENDRET via c1_real.kjor_modell (samme kall som agenten og terskeltabell.py).
Fasit og flagg som maaler_offisiell_v3.py --score mot: MOT når p >= t og styret ikke sier MOT; fasit nbim MOT og avvik.
Kjør fra landsbymappen:  uv run --project arbeid/oppgave_2023 python arbeid/hack/c1/terskel_val_test.py
"""
import os, sys
import numpy as np

HER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HER, "../levering"))
import c1_real  # noqa: E402

TERSKLER = [0.70, 0.80, 0.85, 0.90, None, 0.95, 0.97]  # None = agentens val-F1-optimale terskel


def prf(y, p, t, kan):
    fl = (p >= t) & kan; tp = int((fl & y).sum())
    return tp / max(fl.sum(), 1), tp / max(y.sum(), 1), 2 * tp / max(fl.sum() + y.sum(), 1), tp, int(fl.sum()) - tp


def main():
    g = c1_real.kjor_modell(c1_real.REAL, [])
    pv, t0 = np.asarray(g["pv"], float), float(g["t"])
    pt = np.asarray(g["p"])[g["te"]].astype(float)
    d = g["d"]; nv = d["nbim_vote"].astype(str).eq("MOT").values; kan = ~d["mgmt_rec"].astype(str).eq("MOT").values
    yv = np.asarray(g["yv"]).astype(bool) & nv[g["va"]]; yt = np.asarray(g["yt"]).astype(bool) & nv[g["te"]]
    kv, kt = kan[g["va"]], kan[g["te"]]
    rader = [(t if t is not None else t0, t is None) for t in TERSKLER]
    fv = [prf(yv, pv, t, kv)[2] for t, _ in rader]; ft = [prf(yt, pt, t, kt)[2] for t, _ in rader]
    print(f"Val 2025: n={len(yv)}, {yv.sum()} MOT mot styret. Test 2026: n={len(yt)}, {yt.sum()} MOT mot styret.\n")
    print("| terskel p >= | val P | val R | val F1 | test P | test R | test F1 | test TP/FP |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|")
    for i, (t, valgt) in enumerate(rader):
        P, R, F, _, _ = prf(yv, pv, t, kv); Pt, Rt, Ft, tp, fp = prf(yt, pt, t, kt)
        b = lambda x, beste: f"**{x:.3f}**" if beste else f"{x:.3f}"
        navn = f"**{t:.4f} (valgt)**" if valgt else f"{t:.2f}"
        print(f"| {navn} | {P:.3f} | {R:.3f} | {b(F, F == max(fv))} | {Pt:.3f} | {Rt:.3f} | {b(Ft, Ft == max(ft))} | {tp}/{fp} |")
    print(f"\nValgt t = {t0:.4f} er den val-F1-optimale (c1_real.kjor_modell). Fet F1 = beste i kolonnen blant radene.")


if __name__ == "__main__":
    main()
