"""#2084: terskeltabell for beslutningsstøtte på modellen som fryses (#1046 = smed2 #2044 miks h2, dommer #2080).
Modellen kjøres UENDRET via c1_real.kjor_modell (samme kall som agenten). Alt velges på val 2025 (trent <2025):
  - terskel t: MOT når p >= t. Tre terskler: val-F1-optimal (agentens), høy recall (minste t med val-R >= 0,70),
    høy presisjon (største t med val-P >= 0,60 og minst 10 flagg).
  - usikker-sone: saken går til menneske når |logit(p) - logit(t)| <= bånd; båndet er kvantilen som ruter r % av val.
Test 2026 (modell trent <2026, rå t og bånd fra val) regnes én gang for alle rader i samme kjøring; ingen valg gjøres på test.
#2146: fasit er MOT mot styret (nbim_vote MOT og against_board 1, ordre #231, som maaler_offisiell_v3 --score mot);
  et flagg blir MOT bare der styret ikke sier MOT (som v3). Terskel og bånd er fortsatt valgt på modellens avvik-p.
Kolonner: P/R MOT = agentens egne MOT-flagg utenfor sonen mot alle MOT; «fanget» = (MOT-flagg riktig + MOT i sonen)/alle MOT
(øvre grense: forutsetter at mennesket avgjør sonen riktig); «leses» = sone + MOT-flagg utenfor sonen, per 100 saker.
Kjør fra landsbymappen:  uv run --project arbeid/oppgave_2023 python arbeid/hack/c1/terskeltabell.py [--ut fil.md]
"""
import argparse, os, sys
import numpy as np

HER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HER, "../levering"))
import c1_real  # noqa: E402

ANDELER = [0, 5, 10, 15, 20, 30]


def rad(y, p, t, band, kan):
    lg = c1_real.lg
    sone = np.abs(lg(p) - lg(t)) <= band
    flagg = (p >= t) & ~sone & kan
    tp = (flagg & y).sum(); n = len(y); ny = y.sum()
    P = tp / max(flagg.sum(), 1); R = tp / max(ny, 1)
    F1 = 2 * tp / max(flagg.sum() + ny, 1)
    fanget = (tp + (sone & y).sum()) / max(ny, 1)
    return dict(sone=100 * sone.mean(), P=P, R=R, F1=F1, fanget=fanget, leses=100 * (sone.sum() + flagg.sum()) / n,
                mot_i_sone=int((sone & y).sum()), oversett=int((~sone & ~flagg & y).sum()))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data", default=c1_real.REAL); ap.add_argument("--ut", default=None)
    a = ap.parse_args()
    logg = []
    g = c1_real.kjor_modell(a.data, logg)
    pv, yv, t0, C = np.asarray(g["pv"], float), np.asarray(g["yv"]).astype(bool), float(g["t"]), g["C"]
    pt, yt = np.asarray(g["p"])[g["te"]].astype(float), np.asarray(g["yt"]).astype(bool)
    d = g["d"]; nv_ = d["nbim_vote"].astype(str).eq("MOT").values; kan_ = ~d["mgmt_rec"].astype(str).eq("MOT").values
    yav, yat = yv, yt  # avvik (inkl. AVSTÅ), bare til overskrifta
    yv, yt = yv & nv_[g["va"]], yt & nv_[g["te"]]  # MOT mot styret
    kv, kt = kan_[g["va"]], kan_[g["te"]]
    # terskler, valgt bare på val
    kand = np.unique(pv)
    R = np.array([((pv >= t) & kv & yv).sum() / yv.sum() for t in kand])
    P = np.array([((pv >= t) & kv & yv).sum() / max(((pv >= t) & kv).sum(), 1) for t in kand])
    nfl = np.array([((pv >= t) & kv).sum() for t in kand])
    terskler = {"val-F1-optimal (agentens)": t0,
                "middels recall (val R>=0,60)": float(kand[R >= 0.60].max()),
                "høy recall (val R>=0,70)": float(kand[R >= 0.70].max()),
                "høy presisjon (val P>=0,70)": float(kand[(P >= 0.70) & (nfl >= 10)].min())}
    L = [f"# Terskeltabell Case 1 (#2084): modell #1046 (smed2 #2044 miks h2), C={C}",
         "", f"Val 2025: n={len(yv)}, MOT mot styret={yv.sum()} ({100 * yv.mean():.1f} %). Test 2026: n={len(yt)}, MOT mot styret={yt.sum()} "
         f"({100 * yt.mean():.1f} %). Fasit og P/R/F1 er MOT mot styret som `maaler_offisiell_v3.py --score mot` (#2146); "
         f"avvik inkl. AVSTÅ ({yav.sum()} val, {yat.sum()} test) er ikke hovedtallet. "
         f"Terskel og bånd låst på val; test regnet én gang i samme kjøring.", ""]
    for navn, t in terskler.items():
        L += [f"## Terskel {navn}: p >= {t:.4f}", "",
              "| til menneske (låst på val) | bånd logit | val: sone % | val P MOT | val R MOT | val F1 | val fanget | val leses/100 "
              "| test: sone % | test P MOT | test R MOT | test F1 | test fanget | test leses/100 | test MOT oversett |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        lgd = np.abs(c1_real.lg(pv) - c1_real.lg(t))
        for r in ANDELER:
            band = float(np.quantile(lgd, r / 100)) if r > 0 else -1.0
            v, s = rad(yv, pv, t, band, kv), rad(yt, pt, t, band, kt)
            L.append(f"| {r} % | {max(band, 0):.3f} | {v['sone']:.1f} | {v['P']:.3f} | {v['R']:.3f} | {v['F1']:.3f} | "
                     f"{v['fanget']:.3f} | {v['leses']:.1f} | {s['sone']:.1f} | {s['P']:.3f} | {s['R']:.3f} | {s['F1']:.3f} | "
                     f"{s['fanget']:.3f} | {s['leses']:.1f} | {s['oversett']} av {yt.sum()} |")
        L.append("")
    tekst = "\n".join(L)
    print(tekst)
    if a.ut:
        open(a.ut, "w", encoding="utf-8").write(tekst + "\n")


if __name__ == "__main__":
    main()
