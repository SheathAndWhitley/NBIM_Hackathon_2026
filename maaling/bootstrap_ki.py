"""95 % konfidensintervall for F1 på MOT mot styret: klyngebootstrap over selskaper (2000 trekk, seed 0), samme
fasitregel som maaling/maaler.py. Bare standardbiblioteket.
Bruk (fra repo-roten, etter sh KJOR.sh):  python3 -I maaling/bootstrap_ki.py [SVAR.csv] [test|val]
Standard er agentens svar på test 2026 (ut/pred_maaler.csv).
"""
import csv, os, random, sys

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
svar = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROT, "ut/pred_maaler.csv")
vindu = sys.argv[2] if len(sys.argv) > 2 else "test"
REAL = os.path.join(ROT, "data/real_votes.csv")
S = {r["id"]: r for r in csv.DictReader(open(svar))}
rows = []
for f in csv.DictReader(open(REAL, encoding="utf-8")):
    yr = int(f["meeting_date"][:4])
    if (vindu == "test" and yr != 2026) or (vindu == "val" and yr != 2025): continue
    if f["against_board"] == "": continue
    i = f"{f['meeting_id']}|{f['item_no']}"
    if i not in S: continue
    st = f["mgmt_rec"] or "FOR"; avv = S[i]["anbefaling"].strip() == "1"
    a = ("FOR" if st == "MOT" else "MOT") if avv else st
    x = a == "MOT" and st != "MOT"; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
    rows.append((f["company_id"], x, y))


def f1(rs):
    tp = sum(x and y for _, x, y in rs); fp = sum(x and not y for _, x, y in rs); fn = sum(y and not x for _, x, y in rs)
    return 2 * tp / max(2 * tp + fp + fn, 1), tp, fp, fn


g = {}
for r in rows: g.setdefault(r[0], []).append(r)
ks = list(g); rng = random.Random(0); bs = []
for _ in range(2000):
    rs = [r for k in (rng.choice(ks) for _ in ks) for r in g[k]]; bs.append(f1(rs)[0])
bs.sort(); F, tp, fp, fn = f1(rows)
print(f"{vindu}: n {len(rows)}, selskaper {len(ks)}, F1 MOT mot styret {F:.4f} (TP {tp} FP {fp} FN {fn}), 95 % KI [{bs[49]:.3f}; {bs[1949]:.3f}]")
