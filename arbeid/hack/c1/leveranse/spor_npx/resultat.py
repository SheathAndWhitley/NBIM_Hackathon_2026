"""Skriver ut/RESULTAT.md fra målerens utskrift + bootstrap-KI for F1 (dommer2, sak 1971). Bare stdlib.
Bruk: python3 -I leveranse/resultat.py --ut ut --fasit data_v3/fasit.csv --navn "modellnavn"
KI: 2000 trekk med tilbakelegging av hele møtedager (cusip+dato), seed 1971. Avvik klynger per møte."""
import argparse, csv, os, random, re
from collections import defaultdict


def tall(sti):
    t = open(sti, encoding="utf-8").read()
    m = re.search(r"AVVIK \(hovedtall\) presisjon ([\d.]+)\s+recall ([\d.]+)\s+F1 ([\d.]+)\s+\(tp (\d+) fp (\d+) fn (\d+)", t)
    return dict(p=float(m[1]), r=float(m[2]), f1=float(m[3]), tp=int(m[4]), fp=int(m[5]), fn=int(m[6]),
                prauc=float(re.search(r"^PRAUC ([\d.]+)", t, re.M)[1]),
                score=re.search(r"^SCORE ([\d.]+)", t, re.M)[1],
                rutet=re.search(r"rutet til menneske \(konfidens < [\d.]+\): (\d+) = ([\d.]+)%", t).groups())


def ki(pred, fasit):
    anb = {r["id"]: r["anbefaling"].strip().upper() for r in csv.DictReader(open(pred, encoding="utf-8"))}
    grupper = defaultdict(list)
    for r in csv.DictReader(open(fasit, encoding="utf-8")):
        grupper[(r["cusip"], r["moetedato"])].append((anb.get(r["id"], "FOR") != "FOR", r["avvik"] == "1"))
    g = list(grupper.values()); rnd = random.Random(1971); f1 = []
    for _ in range(2000):
        tp = fp = fn = 0
        for x in (g[rnd.randrange(len(g))] for _ in g):
            for p, y in x: tp += p and y; fp += p and not y; fn += y and not p
        f1.append(2 * tp / (2 * tp + fp + fn) if tp else 0.0)
    f1.sort(); return f1[50], f1[1949]


a = argparse.ArgumentParser(); a.add_argument("--ut"); a.add_argument("--fasit"); a.add_argument("--navn")
a = a.parse_args()
b, m = tall(os.path.join(a.ut, "maal_baseline.txt")), tall(os.path.join(a.ut, "maal_modell.txt"))
lo, hi = ki(os.path.join(a.ut, "pred.csv"), a.fasit)
info = open(os.path.join(os.path.dirname(a.fasit), "split_info.txt"), encoding="utf-8").read().splitlines()
rad = lambda n, x, k="": f"| {n} | {x['p']:.3f} | {x['r']:.3f} | **{x['f1']:.3f}** {k}| {x['prauc']:.3f} | {x['tp']}/{x['tp'] + x['fn']} | {x['rutet'][1]} % |"
md = ["# Case 1: resultat på NBIMs egne stemmer, holdout N-PX 2026", "",
      "Målvariabel: avvik fra styret (NBIM stemte MOT styrets anbefaling). Tall fra `maaler.py`.", "",
      "| kandidat | presisjon | recall | F1 (95 % KI) | PR-AUC | funnet | rutet til menneske |",
      "|---|---|---|---|---|---|---|",
      rad("følg styret (baseline)", b), rad(a.navn, m, f"({lo:.3f}-{hi:.3f}) "), "",
      *[f"- {x}" for x in info],
      "- KI: bootstrap over hele møter (2000 trekk, seed 1971)."]
ms = os.path.join(a.ut, "motstand.json")
if os.path.exists(ms):
    import json; j = json.load(open(ms, encoding="utf-8"))
    md.append(f"- Motstandstest: «{j['injeksjon']}» lagt inn i alle {j['forslag']} forslagstekster: "
              f"{j['mot_som_snudde_til_for']} av {j['mot_original']} MOT-anbefalinger snudde, {j['endret_totalt']} endret totalt.")
open(os.path.join(a.ut, "RESULTAT.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print("\n".join(md[4:7]))
print(f"SCORE {m['score']}")
