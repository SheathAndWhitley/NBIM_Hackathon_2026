"""#2592: entydige rester etter bytt_tall.py (KI, val, TN/accuracy, b2-diff, TP/FP/FN-tekst). Tall i arbeid/oppgave_2592/nye_tall.md.
Hopper over linjer som sier frossen/frosne/#2044 alene (de gjelder gammel modell). Kjør: python3 -I hand_tall.py [--skriv]"""
import glob, re, sys
FILER = sorted(glob.glob("arbeid/hack/levering/*.md") + glob.glob("arbeid/hack/c1/leveranse/*.md"))
R = [("[0,36; 0,59]", "[0,40; 0,62]"), ("0,36–0,59", "0,40–0,62"), ("[0,37; 0,59]", "[0,40; 0,62]"),
     ("[0,359; 0,590]", "[0,400; 0,621]"), ("+0,11 [0,01; 0,22]", "+0,15 [0,04; 0,25]"),
     ("0,520 [0,41; 0,63]", "0,530 [0,42; 0,64]"), ("95,7 %", "96,0 %"), ("1473 av 1539", "1478 av 1539"),
     ("TN 1443", "TN 1446"), ("TP 30, FP 38, FN 28", "TP 32, FP 35, FN 26"), ("TP 30 FP 38 FN 28", "TP 32 FP 35 FN 26"),
     ("30 av 58", "32 av 58"), ("overser 28", "overser 26"), ("38 av 68 MOT-flagg", "35 av 67 MOT-flagg"),
     ("30 av 68", "32 av 67"), ("Av 68 MOT-flagg er 38 falske", "Av 67 MOT-flagg er 35 falske"),
     ("38 falske", "35 falske"), ("38 feilflagg", "35 feilflagg"), ("bytter 38 riktige", "bytter 35 riktige"),
     ("P 0,44, R 0,52", "P 0,48, R 0,55"), ("P 0,441, R 0,517", "P 0,478, R 0,552"),
     ("**51,7 %**", "**55,2 %**"), ("**44,1 %**", "**47,8 %**"), ("0,5 poeng lavere", "0,2 poeng lavere"),
     ("val 2025 (0,520)", "val 2025 (0,530)"), ("over (0,520)", "over (0,530)"), ("målet (0,520)", "målet (0,530)"),
     ("val (0,520)", "val (0,530)"), ("og 0,520 på val 2025", "og 0,530 på val 2025"), ("188 av 1578", "164 av 1578"),
     ("11,9 %", "10,4 %"), ("17 MOT ser ingen", "18 MOT ser ingen"), ("finner 30 (", "finner 32 (")]
HOPP = re.compile(r"frossen|frosne|bommene|c1_bommene|eldre|tallvakt: ignorer", re.I)
skriv = "--skriv" in sys.argv; tot = 0
for f in FILER:
    L = open(f, encoding="utf-8").read().split("\n"); n = 0
    for i, l in enumerate(L):
        if HOPP.search(l): continue
        ny = l
        for a, b in R: ny = ny.replace(a, b)
        if ny != l: n += 1; L[i] = ny; print(f"{f}:{i+1}") if not skriv else None
    if n and skriv: open(f, "w", encoding="utf-8").write("\n".join(L))
    if n: print(f"{n:3d} linjer {f}"); tot += n
print(tot, "linjer", "skrevet" if skriv else "(tørt)")
