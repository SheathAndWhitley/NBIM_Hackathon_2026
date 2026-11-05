"""#2103: parret klyngebootstrap (selskap, 2000 trekk, seed 0) av F1 MOT mot styret, uten sakstype minus full. Samme regel som ki_mot.py/v3."""
import csv, sys, random
A, B, vindu = sys.argv[1], sys.argv[2], sys.argv[3]
REAL = "state/opplastet/20261105_114241_real_votes.csv"
SA = {r["id"]: r for r in csv.DictReader(open(A))}; SB = {r["id"]: r for r in csv.DictReader(open(B))}
def mot(S, i, st):
    avv = S[i]["anbefaling"].strip() == "1"; a = ("FOR" if st == "MOT" else "MOT") if avv else st
    return a == "MOT" and st != "MOT"
g = {}
for f in csv.DictReader(open(REAL)):
    yr = int(f["meeting_date"][:4])
    if (vindu == "test" and yr != 2026) or (vindu == "val" and yr != 2025) or f["against_board"] == "": continue
    i = f"{f['meeting_id']}|{f['item_no']}"
    if i not in SA: continue
    st = f["mgmt_rec"] or "FOR"; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
    g.setdefault(f["company_id"], []).append((mot(SA, i, st), mot(SB, i, st), y))
def f1(rs, k):
    tp = sum(r[k] and r[2] for r in rs); fp = sum(r[k] and not r[2] for r in rs); fn = sum(r[2] and not r[k] for r in rs)
    return 2 * tp / max(2 * tp + fp + fn, 1)
alle = [r for v in g.values() for r in v]; ks = list(g); rng = random.Random(0); ds = []
for _ in range(2000):
    rs = [r for k in (rng.choice(ks) for _ in ks) for r in g[k]]; ds.append(f1(rs, 1) - f1(rs, 0))
ds.sort(); d = f1(alle, 1) - f1(alle, 0)
print(f"{vindu}: B-A {d:+.4f}, 95 % KI [{ds[49]:+.3f}; {ds[1949]:+.3f}], andel trekk B<A {sum(x < 0 for x in ds)/len(ds):.2f}, ulike prediksjoner {sum(r[0]!=r[1] for r in alle)}")
