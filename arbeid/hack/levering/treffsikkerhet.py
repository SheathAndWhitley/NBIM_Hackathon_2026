"""2x2-tabell for MOT mot styret (#2175), regnet med samme regler som maaler_offisiell_v3.py (importert, ikke kopiert).
Bruk: python3 -I treffsikkerhet.py SVAR.csv [--terskel 0.6]   (vindu test, data real)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "c1"))
import maaler_offisiell_v3 as M

def tell(S, fas, filt=lambda k: True):
    t = {"TP": 0, "FP": 0, "FN": 0, "TN": 0}
    for i, f in fas.items():
        if f["against_board"] == "": continue
        s = S[i]; styret = f["mgmt_rec"] or "FOR"; a = (s.get("anbefaling") or "").strip().upper()
        if a in ("0", "1"): a = ("FOR" if styret == "MOT" else "MOT") if a == "1" else styret
        k = float(s.get("konfidens") or 1.0)
        if not filt(k): continue
        x = a == "MOT" and styret != "MOT"; y = f["nbim_vote"] == "MOT" and f["against_board"] == "1.0"
        t[("T" if x == y else "F") + ("P" if x else "N")] += 1
    return t

def skriv(navn, t):
    n = sum(t.values()); P, R, _ = M.prf(t["TP"], t["FP"], t["FN"])
    print(f"[{navn}] n {n}: TP {t['TP']} FP {t['FP']} FN {t['FN']} TN {t['TN']}")
    print(f"  accuracy {(t['TP']+t['TN'])/n:.4f}  recall MOT {R:.4f}  presisjon MOT {P:.4f}  "
          f"riktig på FOR/ikke-MOT (TN/(TN+FP)) {t['TN']/max(t['TN']+t['FP'],1):.4f}  "
          f"følg styret ville hatt accuracy {(t['TN']+t['FP'])/n:.4f}")

if __name__ == "__main__":
    a = sys.argv[1:]; ter = 0.6
    if "--terskel" in a: j = a.index("--terskel"); ter = float(a[j + 1]); del a[j:j + 2]
    fas = {M.rid(r): r for r in M.les("real") if M.vindu_av(r, "real") == "test"}
    S = M.les_svar(a[0], "real")
    skriv("alle saker", tell(S, fas))
    skriv(f"maskinen avgjør selv (konfidens >= {ter})", tell(S, fas, lambda k: k >= ter))
    skriv(f"går til menneske (konfidens < {ter})", tell(S, fas, lambda k: k < ter))
