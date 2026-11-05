"""#1986: bootstrap-KI (95 %, 1000 trekk, trekk per selskap = cusip) for F1 på avvik/MOT (= maaler.py SCORE; i v3 er styret alltid FOR).
Kandidater: gulv, smed2 v3 frosset (sha 19c3e29, tavla 0,4658), val-regelen #1982 (gulv ELLER topp 4 % p_avvik, persentil av settet selv),
og smed2 nyeste (kandidatmappa 11:25, ikke frosset, bare til info). Inndata er frosne kopier i usikkerhet_inn/ (SHA256.txt).
Kjør fra landsbymappen: uv run python arbeid/hack/c1/usikkerhet.py   (seed 0, deterministisk; B=1000 kan endres med miljøvariabel B)"""
import csv, hashlib, os
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); INN = os.path.join(D, "usikkerhet_inn")
SETT = {"val 2025": ("data_v3_val/fasit.csv", "val"), "test 2026": ("data_v3/fasit.csv", "test")}
B, Q = int(os.environ.get("B", 1000)), 0.04
les = lambda f: {r["id"]: r for r in csv.DictReader(open(f, encoding="utf-8"))}
f1 = lambda p, y: 2 * (p & y).sum() / max(p.sum() + y.sum(), 1)
ki = lambda v: np.percentile(v, [2.5, 97.5])
sha = {l.split()[1].split("/")[-1]: l.split()[0] for l in open(os.path.join(INN, "SHA256.txt"))}
for f, s in sha.items():
    assert hashlib.sha256(open(os.path.join(INN, f), "rb").read()).hexdigest().startswith(s), f"{f} er endret siden frysing"
for navn, (ff, suf) in SETT.items():
    F = les(os.path.join(D, ff)); ids = list(F)
    P = {k: les(os.path.join(INN, f"{k}_{suf}.csv")) for k in ["gulv", "smed2_v3", "smed2_nyeste_1125"]}
    for k, p in P.items(): assert all(i in p for i in ids), f"{k}_{suf}: mangler id-er"
    y = np.array([F[i]["avvik"] == "1" for i in ids])
    avv = lambda p: np.array([p[i]["anbefaling"].strip().upper() != F[i]["styret"].strip().upper() for i in ids])
    pm = np.array([float(P["smed2_v3"][i]["p_avvik"]) for i in ids])
    kand = {"gulv": avv(P["gulv"]), "smed2 v3 (frosset)": avv(P["smed2_v3"])}
    kand["val-regel #1982"] = kand["gulv"] | (pm >= np.quantile(pm, 1 - Q))
    kand["smed2 nyeste 11:25 (info)"] = avv(P["smed2_nyeste_1125"])
    sel = np.array([F[i]["cusip"] for i in ids]); us, inv = np.unique(sel, return_inverse=True)
    grupper = [np.flatnonzero(inv == k) for k in range(len(us))]
    rng = np.random.default_rng(0); bs = {k: [] for k in kand}
    for _ in range(B):
        idx = np.concatenate([grupper[k] for k in rng.integers(0, len(us), len(us))])
        for k, p in kand.items(): bs[k].append(f1(p[idx], y[idx]))
    bs = {k: np.array(v) for k, v in bs.items()}
    print(f"\n### {navn}: n {len(y)}, avvik/MOT {y.sum()}, selskaper {len(us)}, {B} trekk per selskap")
    print("| kandidat | F1 | 95 % KI | flagget |\n|---|---|---|---|")
    for k, p in kand.items():
        lo, hi = ki(bs[k]); print(f"| {k} | {f1(p, y):.3f} | [{lo:.3f}; {hi:.3f}] | {p.sum()} |")
    print("| forskjell (parvis, samme trekk) | ΔF1 | 95 % KI | andel trekk > 0 |\n|---|---|---|---|")
    for a, b in [("smed2 v3 (frosset)", "gulv"), ("val-regel #1982", "gulv"), ("val-regel #1982", "smed2 v3 (frosset)"), ("smed2 nyeste 11:25 (info)", "gulv")]:
        d = bs[a] - bs[b]; lo, hi = ki(d)
        print(f"| {a} − {b} | {f1(kand[a], y) - f1(kand[b], y):+.3f} | [{lo:+.3f}; {hi:+.3f}] | {(d > 0).mean():.2f} |")
