"""95 %-intervall for recall og presisjon på MOT mot styret (#2185): bootstrap over sakene, fast frø.
Samme regler som treffsikkerhet.py (importert) og maaler_offisiell_v3.py. Trekker 1539 saker med tilbakelegging,
regner P og R for alle saker og for båndet konfidens >= terskel i hvert trekk, og gir 2,5- og 97,5-persentilen.
Clopper-Pearson (eksakt binomial) vises ved siden av: bootstrap blir degenerert når en andel er 0 eller 100 %.
Bruk: python3 -I treffsikkerhet_ki.py SVAR.csv [--trekk 2000] [--fro 2185] [--terskel 0.6]"""
import os, random, sys
from statistics import NormalDist
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import treffsikkerhet as T
M = T.M


def saker(S, fas):
    """Én rad per sak med fasit: (agenten sier MOT, fasit MOT, konfidens). Samme regel som T.tell."""
    ut = []
    for i, f in fas.items():
        if f["against_board"] == "": continue
        s = S[i]; styret = f["mgmt_rec"] or "FOR"; a = (s.get("anbefaling") or "").strip().upper()
        if a in ("0", "1"): a = ("FOR" if styret == "MOT" else "MOT") if a == "1" else styret
        ut.append((a == "MOT" and styret != "MOT", f["nbim_vote"] == "MOT" and f["against_board"] == "1.0",
                   float(s.get("konfidens") or 1.0)))
    return ut


def pr(rader):
    tp = sum(x and y for x, y in rader); fp = sum(x and not y for x, y in rader); fn = sum(y and not x for x, y in rader)
    return (tp / (tp + fp) if tp + fp else None), (tp / (tp + fn) if tp + fn else None), tp, fp, fn


def beta_ppf(q, a, b):  # invers av regularisert ufullstendig beta ved halvering (ingen scipy i -I)
    from math import lgamma, exp, log
    def cdf(x, n=4000):  # Simpson på tettheten
        if x <= 0: return 0.0
        if x >= 1: return 1.0
        c = lgamma(a + b) - lgamma(a) - lgamma(b); h = x / n; s = 0.0
        for k in range(n + 1):
            t = max(k * h, 1e-300); w = 1 if k in (0, n) else (4 if k % 2 else 2)
            s += w * exp(c + (a - 1) * log(t) + (b - 1) * log(max(1 - t, 1e-300)))
        return s * h / 3
    lo, hi = 0.0, 1.0
    for _ in range(50):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if cdf(m) < q else (lo, m)
    return (lo + hi) / 2


def clopper(k, n):
    lo = 0.0 if k == 0 else beta_ppf(0.025, k, n - k + 1)
    hi = 1.0 if k == n else beta_ppf(0.975, k + 1, n - k)
    return lo, hi


def pst(v): return "–" if v is None else f"{100 * v:.1f}".replace(".", ",")


def main(a):
    trekk, fro, ter = 2000, 2185, 0.6
    for flagg in ("--trekk", "--fro", "--terskel"):
        if flagg in a:
            j = a.index(flagg); v = a[j + 1]; del a[j:j + 2]
            if flagg == "--trekk": trekk = int(v)
            elif flagg == "--fro": fro = int(v)
            else: ter = float(v)
    fas = {M.rid(r): r for r in M.les("real") if M.vindu_av(r, "real") == "test"}
    S = M.les_svar(a[0], "real")
    R = saker(S, fas)
    t = T.tell(S, fas)  # kontroll: samme 2x2 som treffsikkerhet.py
    assert (sum(x and y for x, y, _ in R), sum(x and not y for x, y, _ in R)) == (t["TP"], t["FP"]), "avvik mot T.tell"
    deler = {"alle saker": lambda k: True, f"konfidens >= {ter}": lambda k: k >= ter}
    rng = random.Random(fro); n = len(R)
    boot = {d: ([], []) for d in deler}
    for _ in range(trekk):
        u = [R[rng.randrange(n)] for _ in range(n)]
        for d, f in deler.items():
            p, r, *_ = pr([(x, y) for x, y, k in u if f(k)])
            if p is not None: boot[d][0].append(p)
            if r is not None: boot[d][1].append(r)
    def kvant(v, q): v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))]
    print(f"Bootstrap {trekk} trekk, frø {fro}, {n} saker med fasit (test 2026, real)")
    for d, f in deler.items():
        p, r, tp, fp, fn = pr([(x, y) for x, y, k in R if f(k)])
        nd = sum(1 for *_, k in R if f(k))
        bp, br = boot[d]
        cp, cr = clopper(tp, tp + fp), clopper(tp, tp + fn)
        print(f"[{d}] n {nd}: TP {tp} FP {fp} FN {fn}")
        print(f"  presisjon {pst(p)} %  bootstrap 95 % {pst(kvant(bp, .025))}–{pst(kvant(bp, .975))} %"
              f"  Clopper-Pearson {pst(cp[0])}–{pst(cp[1])} %  (gyldige trekk {len(bp)})")
        print(f"  recall    {pst(r)} %  bootstrap 95 % {pst(kvant(br, .025))}–{pst(kvant(br, .975))} %"
              f"  Clopper-Pearson {pst(cr[0])}–{pst(cr[1])} %  (gyldige trekk {len(br)})")


if __name__ == "__main__":
    main(sys.argv[1:])
