"""Dommer #2500: uavhengig F1 MOT mot styret (same regel som maaler_offisiell_v3) for et vilkårlig år. Måleren v3 har bare val=2025/test=2026."""
import csv, sys
REAL = "state/opplastet/20261105_114241_real_votes.csv"
aar = sys.argv[1]; svar = sys.argv[2]
S = {r["id"]: r for r in csv.DictReader(open(svar))}
tp = fp = fn = 0; atp = afp = afn = 0; n = 0; mangler = 0
for f in csv.DictReader(open(REAL, encoding="utf-8", newline="")):
    if f["year"] != aar or f["against_board"] == "": continue
    i = f"{f['meeting_id']}|{f['item_no']}"
    if i not in S: mangler += 1; continue
    n += 1; styret = f["mgmt_rec"] or "FOR"; avv = S[i]["anbefaling"].strip() == "1"
    mot = (("FOR" if styret == "MOT" else "MOT") if avv else styret) == "MOT"
    y = f["against_board"] == "1.0"; ym = f["nbim_vote"] == "MOT"
    xs = mot and styret != "MOT"; ys = ym and y
    tp += xs and ys; fp += xs and not ys; fn += (not xs) and ys
    atp += avv and y; afp += avv and not y; afn += (not avv) and y
f1 = lambda a, b, c: 2 * a / max(2 * a + b + c, 1)
print(f"{aar} {svar.split('/')[-1]}: n {n} mangler {mangler} | avvik F1 {f1(atp,afp,afn):.4f} (TP{atp} FP{afp} FN{afn}) | MOT mot styret F1 {f1(tp,fp,fn):.4f} (TP{tp} FP{fp} FN{fn}, {tp+fn} i fasit)")
