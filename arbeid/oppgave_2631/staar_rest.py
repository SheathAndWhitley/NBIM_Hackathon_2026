"""#2631: STÅR-resten. Tekster som verken zip 2587 (tilbake_fra_zip.sh) eller reserve_staar/ dekker, får BYTT-tallene
reversert til frossen (omvendt bytt_tall.py + de håndrettede formene fra BYTTEPLAN steg 2).
Standardfiler: levering/KRAVRESPONS.md, EN_SIDE.md (usporet, ikke i zipen), GITHUB_README_UTKAST.md (laget etter zipen).
Bruk: python3 -I arbeid/oppgave_2631/staar_rest.py [--rot ROT] [--skriv] [fil ...]   Uten --skriv: tørt.
Linjer om frossen/#2044/2024/2025/tallvakt: ignorer hoppes over for de mekaniske parene; de eksplisitte formene (KI,
sidetall, HOVEDTALL-utskrift, accuracy) byttes uansett. Tallvakta avgjør til slutt."""
import os, re, sys
a = sys.argv[1:]; rot = "."; skriv = False; filer = []
while a:
    x = a.pop(0)
    if x == "--rot": rot = a.pop(0)
    elif x == "--skriv": skriv = True
    else: filer.append(x)
filer = filer or ["arbeid/hack/levering/KRAVRESPONS.md", "arbeid/hack/levering/EN_SIDE.md", "arbeid/hack/levering/GITHUB_README_UTKAST.md"]
EKSPLISITT = [("repo4 = smed2 #2044 miks h2 + 4 repotrekk, `modell_repo4.py`) på NBIMs egne stemmer (real_votes fra arrangøren), test 2026: **F1 0,512 på MOT mot styret**",
               "smed2 #2044 miks h2) på NBIMs egne stemmer (real_votes fra arrangøren), test 2026: **F1 0,476 på MOT mot styret**"),
              ("0,529 [0,42; 0,63] (frossen 0,482)", "0,482 [0,375; 0,580]"), ("[0,40; 0,62]", "[0,36; 0,59]"),
              ("0.512000", "0.476190"), ("Accuracy **96,0 %**", "Accuracy **95,7 %**"), ("TN 1446", "TN 1443")]
FOR = [(re.compile(r"161 av 1539 \(10,5 %\)"), "183 av 1539 (11,9 %)"), (re.compile(r"161 av (de )?1539"), r"183 av \g<1>1539"),
       (re.compile(r"(1539[^%]{0,40}?)10,5 %"), r"\g<1>11,9 %"),
       (re.compile(r"\bP 0,48\b(?!\d)"), "P 0,44"), (re.compile(r"\bR 0,55\b(?!\d)"), "R 0,52"), (re.compile(r"32/35/26"), "30/38/28")]
BYTT = [("TP 32 FP 35 FN 26", "TP 30 FP 38 FN 28"), ("TP 32, FP 35, FN 26", "TP 30, FP 38, FN 28"), ("0.5120", "0.4762"), ("0,5120", "0,4762"),
        ("0,512", "0,476"), ("0.512", "0.476"), ("P 0.4776", "P 0.4412"), ("R 0.5517", "R 0.5172"), ("0,478", "0,441"), ("0,552", "0,517"),
        ("164 av 1578", "188 av 1578"), ("10,4 %", "11,9 %"), ("32 av 58", "30 av 58")]
HOPP = re.compile(r"frossen|#2044|\bV1\b|2024|2025|tallvakt: ignorer", re.I)
tot = 0
for f in filer:
    p = os.path.join(rot, f)
    if not os.path.exists(p): print(f"mangler {f}"); continue
    ut, n = [], 0
    for l in open(p).read().split("\n"):
        for g, ny in EKSPLISITT:
            n += l.count(g); l = l.replace(g, ny)
        if not HOPP.search(l):
            for r, b in FOR:
                l, k = r.subn(b, l); n += k
            for g, ny in BYTT:
                n += l.count(g); l = l.replace(g, ny)
        ut.append(l)
    tot += n; print(f"{n:4d}  {f}")
    if skriv and n: open(p, "w").write("\n".join(ut))
print(f"{tot} erstatninger {'skrevet' if skriv else '(tørt)'}")
