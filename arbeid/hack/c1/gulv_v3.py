"""Dommerens gulv v3 (#1966): MOT hvis NBIM stemte MOT på samme selskaps say-on-pay i train (tidligere år).
p_avvik = andel MOT-stemmer på selskapet i train (glattet), 0.09 for ukjente. Bruk: gulv_v3.py DATAMAPPE UT.csv"""
import csv, sys
from collections import defaultdict
d, ut = sys.argv[1], sys.argv[2]
h = defaultdict(lambda: [0, 0])
for r in csv.DictReader(open(f"{d}/train.csv", encoding="utf-8")):
    h[r["cusip"]][0] += r["avvik"] == "1"; h[r["cusip"]][1] += 1
basis = sum(v[0] for v in h.values()) / sum(v[1] for v in h.values())
with open(ut, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "anbefaling", "konfidens", "p_avvik"])
    for r in csv.DictReader(open(f"{d}/test_input.csv", encoding="utf-8")):
        m, n = h.get(r["cusip"], (0, 0))
        p = (m + basis) / (n + 1)
        a = "MOT" if m > 0 else "FOR"
        w.writerow([r["id"], a, round(max(p, 1 - p), 4), round(p, 4)])
