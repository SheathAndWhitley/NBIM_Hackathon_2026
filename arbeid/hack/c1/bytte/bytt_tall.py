"""#2572 bytte steg 4: hovedtallet frossen #2044 -> repo4 i pakkas tekster. Uten --skriv: viser bare treff per fil.
Hopper over linjer om den gamle modellen (frossen, #2044, V1, 2024, 2025, tallvakt: ignorer). Alt annet fanges av tallvakta.
KI, TN/accuracy og modellnavnet («miks h2») må rettes for hånd (BYTTEPLAN.md steg 4)."""
import glob, re, sys
# #2577: test-tallene på 1539 saker med fasit først (183 -> 161, 11,9 % -> 10,5 %), så de avrundede P/R-formene
FOR = [(re.compile(r"183 av 1539 \(11,9 %\)"), "161 av 1539 (10,5 %)"), (re.compile(r"183 av (de )?1539"), r"161 av \g<1>1539"),
       (re.compile(r"(1539[^%]{0,40}?)11,9 %"), r"\g<1>10,5 %"),
       (re.compile(r"\bP 0,44\b(?!\d)"), "P 0,48"), (re.compile(r"\bR 0,52\b(?!\d)"), "R 0,55"), (re.compile(r"30/38/28"), "32/35/26")]
BYTT = [("TP 30 FP 38 FN 28", "TP 32 FP 35 FN 26"), ("0.4762", "0.5120"), ("0,4762", "0,5120"), ("0,476", "0,512"),
        ("0.476", "0.512"), ("P 0.4412", "P 0.4776"), ("R 0.5172", "R 0.5517"), ("0,441", "0,478"), ("0,517", "0,552"),
        ("188 av 1578", "164 av 1578"), ("11,9 %", "10,4 %")]
HOPP = re.compile(r"frossen|#2044|\bV1\b|2024|2025|tallvakt: ignorer", re.I)
skriv = "--skriv" in sys.argv; tot = 0
for f in sorted(glob.glob("arbeid/hack/levering/*.md") + glob.glob("arbeid/hack/c1/leveranse/*.md")):
    ut, n = [], 0
    for l in open(f).read().split("\n"):
        if not HOPP.search(l):
            for r, b in FOR:
                l, k = r.subn(b, l); n += k
            for a, b in BYTT:
                n += l.count(a); l = l.replace(a, b)
        elif "--rester" in sys.argv and re.search(r"0,476|0,44\b|0,52\b|183 av 1539|188 av 1578|11,9 %|30 FP 38", l):
            print(f"  FOR HÅND {f}: {l[:160]}")
        ut.append(l)
    if n:
        tot += n; print(f"{n:4d}  {f}")
        if skriv: open(f, "w").write("\n".join(ut))
print(f"{tot} erstatninger {'skrevet' if skriv else '(tørt)'}")
