"""#2732: parret klyngebootstrap (2000 trekk, seed 0) av F1 MOT mot styret, B minus A, test 2026.
Samme regel som oppgave_2103/diff_ki.py, men klyngenøkkel kan velges: selskap (som før) eller møte."""
import csv, sys, random
A, B, kl = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "selskap")
REAL = "state/opplastet/20261105_114241_real_votes.csv"
SA = {r["id"]: r for r in csv.DictReader(open(A))}; SB = {r["id"]: r for r in csv.DictReader(open(B))}
def mot(S, i, st):
    avv = S[i]["anbefaling"].strip() == "1"; a = ("FOR" if st == "MOT" else "MOT") if avv else st
    return a == "MOT" and st != "MOT"
g = {}
for f in csv.DictReader(open(REAL)):
    if int(f["meeting_date"][:4]) != 2026 or f["against_board"] == "": continue
    i = f"{f['meeting_id']}|{f['item_no']}"
    if i not in SA or i not in SB: continue
    st = f["mgmt_rec"] or "FOR"; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
    g.setdefault(f["company_id"] if kl == "selskap" else f["meeting_id"], []).append((mot(SA, i, st), mot(SB, i, st), y))
def f1(rs, k):
    tp = sum(r[k] and r[2] for r in rs); fp = sum(r[k] and not r[2] for r in rs); fn = sum(r[2] and not r[k] for r in rs)
    return 2 * tp / max(2 * tp + fp + fn, 1)
alle = [r for v in g.values() for r in v]; ks = list(g); rng = random.Random(0); ds = []
for _ in range(2000):
    rs = [r for k in (rng.choice(ks) for _ in ks) for r in g[k]]; ds.append(f1(rs, 1) - f1(rs, 0))
ds.sort(); d = f1(alle, 1) - f1(alle, 0)
print(f"klynge={kl} n={len(alle)} klynger={len(ks)} F1 A={f1(alle,0):.4f} B={f1(alle,1):.4f} B-A {d:+.4f}, 95 % KI [{ds[49]:+.3f}; {ds[1949]:+.3f}], andel trekk B<A {sum(x < 0 for x in ds)/len(ds):.3f}")
