"""#2885 diagnose 2 (ikke kandidat, bruker testens flaggtall): samme antall flagg som tv=1.0 (90/68/70 etter av) -> skiller rangering fra grense."""
import csv, subprocess, os, sys
sys.argv = ["x", "diag"]; exec(open("velg_tv.py").read().split('print("| T |')[0])
MAAL = {2024: 90, 2025: 68, 2026: 70}
print("| tv | 2024 | 2025 | 2026 | snitt | (flagg låst til tv=1.0 sitt antall etter av) |")
for tv in TVS:
    r = []
    for T in (2024, 2025, 2026):
        rows = list(csv.DictReader(open(f"{U}/tv{tv}_{T}_test.csv")))
        ps = sorted((float(x["p_avvik"]) for x in rows), reverse=True)
        # finn grense slik at antall flagg ETTER av = MAAL (søk nedover)
        lo = 0
        for k in range(MAAL[T], len(ps)):
            t = ps[k - 1]; tmp = f"{U}/diag/tmp.csv"
            with open(tmp, "w") as o:
                o.write("id,anbefaling,p_avvik\n")
                for x in rows: o.write(f"{x['id']},{int(float(x['p_avvik']) >= t)},{x['p_avvik']}\n")
            f = f"{U}/diag/rang_tv{tv}_{T}.csv"; av(tmp, T, f)
            n = sum(x["anbefaling"] == "1" for x in csv.DictReader(open(f)))
            if n >= MAAL[T]: break
        r.append((mål(f, T), n))
    print(f"| {tv} | " + " | ".join(f"{s:.4f} ({n})" for s, n in r) + f" | {sum(s for s,_ in r)/3:.4f} |", flush=True)
