"""Baseline 'stem alltid som styret' på votes.csv, med MOT-presisjon/recall.

Bruk: python baseline_styret.py data/votes.csv [--split 2026-01-01]
To mål:
  A) MOT = stemmen er AGAINST/WITHHOLD (som baseline.py i startpakken).
     Baseline predikerer MOT når styret anbefaler AGAINST.
  B) AVVIK = stemmen avviker fra styrets anbefaling (mot_ledelsen=1).
  Styret = utledet kolonne 'styret' (fra lag_tabell.py), ALDRI mgmt_felt_LEKKER.
  Standard: bare hovedposter (hoved=1), dvs. fondets egen stemme.
     'Følg styret' predikerer aldri avvik -> recall 0 per definisjon.
Tall både per post (fond x forslag) og per unikt forslag (cusip, dato, tekst; flertall over fond).
"""
import argparse, csv
from collections import Counter, defaultdict

MOT = {"AGAINST", "WITHHOLD"}


def pr(pred, fakt):
    tp = sum(p and f for p, f in zip(pred, fakt)); fp = sum(p and not f for p, f in zip(pred, fakt))
    fn = sum(f and not p for p, f in zip(pred, fakt))
    P = tp / (tp + fp) if tp + fp else 0.0; R = tp / (tp + fn) if tp + fn else 0.0
    F = 2 * P * R / (P + R) if P + R else 0.0
    return P, R, F, tp, fp, fn


def rapport(navn, rader):
    n = len(rader)
    if not n:
        return
    motA = [r["mot"] == "1" for r in rader]
    predA = [r["styret"] == "AGAINST" for r in rader]
    avv = [r["mot_ledelsen"] == "1" for r in rader]
    P, R, F, tp, fp, fn = pr(predA, motA)
    print(f"{navn}: n={n}  andel MOT={sum(motA)/n:.1%}  andel avvik fra styret={sum(avv)/n:.1%}")
    print(f"   A) MOT, følg styret: presisjon {P:.1%}  recall {R:.1%}  F1 {F:.3f}  (tp {tp}, fp {fp}, fn {fn})")
    P2, R2, F2, *_ = pr([True] * n, motA)
    print(f"   A) MOT, alltid MOT (gulv): presisjon {P2:.1%}  recall {R2:.1%}  F1 {F2:.3f}")
    print(f"   B) avvik, følg styret: presisjon 0  recall 0  (predikerer aldri avvik); andel avvik {sum(avv)/n:.1%}")


def unike(rader):
    g = defaultdict(list)
    for r in rader:
        g[(r["cusip"], r["moetedato"], r["forslag"])].append(r)
    ut, uenige = [], 0
    for k, rs in g.items():
        c = Counter(r["stemme"] for r in rs)
        if len(c) > 1:
            uenige += 1
        rr = dict(rs[0]); rr["stemme"] = c.most_common(1)[0][0]
        rr["mot"] = str(int(rr["stemme"] in MOT))
        rr["mot_ledelsen"] = Counter(r["mot_ledelsen"] for r in rs).most_common(1)[0][0]
        ut.append(rr)
    return ut, uenige


if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("csv"); p.add_argument("--split", default="2026-01-01")
    a = p.parse_args()
    alle = [r for r in csv.DictReader(open(a.csv, encoding="utf-8")) if r["stemme"]]
    rader = [r for r in alle if r.get("hoved", "1") == "1"]  # unik-filer: alle
    print(f"Poster: {len(alle)}, hovedposter: {len(rader)}")
    print("Stemmer:", Counter(r["stemme"] for r in rader).most_common(8))
    print("Styret (utledet):", Counter(r["styret"] for r in rader).most_common(8))
    print("År (møtedato):", sorted(Counter(r["moetedato"][:4] for r in rader).items()))
    rapport("ALLE hovedposter (fond x forslag)", rader)
    u, uenige = unike(rader)
    print(f"Unike forslag: {len(u)}  (fond uenige seg imellom på {uenige} = {uenige/len(u):.1%})")
    rapport("ALLE unike", u)
    rapport(f"TEST unike (møtedato >= {a.split})", [r for r in u if r["moetedato"] >= a.split])
    rapport(f"TRENING unike (< {a.split})", [r for r in u if r["moetedato"] < a.split])
    for kilde in ("ISSUER", "SHAREHOLDER"):
        rapport(f"unike, kilde={kilde}", [r for r in u if r["kilde"] == kilde])
