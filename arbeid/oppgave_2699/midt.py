import csv, sys
val, test, ut = sys.argv[1:4]
V = list(csv.DictReader(open(val))); T = list(csv.DictReader(open(test)))
andel = sum(r["anbefaling"] == "1" for r in V) / len(V)
k_andel = round(andel * len(T)); k_raa = sum(r["anbefaling"] == "1" for r in T)
k = round((k_andel + k_raa) / 2)
orden = sorted(range(len(T)), key=lambda i: -float(T[i]["p_avvik"]))
flagg = set(orden[:k])
with open(ut, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "anbefaling", "p_avvik"])
    for i, r in enumerate(T): w.writerow([r["id"], 1 if i in flagg else 0, r["p_avvik"]])
print(f"{test}: k_raa={k_raa} k_andel={k_andel} k={k}")
