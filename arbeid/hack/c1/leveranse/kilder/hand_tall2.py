"""#2592 runde 2: ruting/menneske-tall og avvik-sidetall for repo4 (menneske_tabell.py, usette.py, ki_avvik.py på arbeid/oppgave_2592/agent.csv).
Ingen hopp-regel: strengene under er valgt så de bare finnes i setninger om levert modell. Kjør: python3 -I hand_tall2.py [--skriv]"""
import glob, re, sys
FILER = sorted(glob.glob("arbeid/hack/levering/*.md") + glob.glob("arbeid/hack/c1/leveranse/*.md"))
RAD_B = "| bare båndet: kalibrert P(MOT) i [0,15; 0,85) | 99 av 1539 (6,4 %) | 25 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,92 / R 0,62 / F1 0,742 (TP 36 FP 3 FN 22) | P 0,79 / R 0,19 / F1 0,306 |"
RAD_S = "| **standard** (bånd + ukjent selskap/type, injeksjon, datafeil, MOT uten sitat) | 161 av 1539 (10,5 %) | 29 av 58 | P 0,48 / R 0,55 / F1 0,512 (TP 32 FP 35 FN 26) | P 0,93 / R 0,69 / F1 0,792 (TP 40 FP 3 FN 18) | P 0,79 / R 0,19 / F1 0,306 |"
R = [("frossen modell #2044, faktisk standardkjøring (#2132,", "levert modell repo4 (#2044 miks h2 + 4 repotrekk), faktisk standardkjøring (#2592,"),
     ("Inn 1578 saker, 188 (11,9 %) til menneske; av de 1539 med fasit 183 (11,9 %)", "Inn 1578 saker, 164 (10,4 %) til menneske; av de 1539 med fasit 161 (10,5 %)"),
     ("menneske_tabell.py arbeid/oppgave_2132/agent.csv", "menneske_tabell.py arbeid/oppgave_2592/agent.csv"),
     ("Alle 35 falske MOT-flagg havner hos mennesket; de 17 MOT ingen ser har lav P(MOT)", "32 av 35 falske MOT-flagg havner hos mennesket (3 er MOT-flagg utenfor sonen, som forvalteren også leser); de 18 MOT ingen ser har lav P(MOT)"),
     ("**12,5 av 100 saker**: 11,9 i sonen (183 saker) og 0,6 MOT-flagg utenfor sonen (9 saker, alle ekte MOT)", "**11,4 av 100 saker**: 10,5 i sonen (161 saker) og 0,9 MOT-flagg utenfor sonen (14 saker, 11 ekte og 3 falske MOT)"),
     ("**inntil 71 % av MOT-stemmene funnet** (41 av 58), mot 52 % for maskinen alene", "**inntil 69 % av MOT-stemmene funnet** (40 av 58), mot 55 % for maskinen alene"),
     ("blir det 16 %.", "blir det 19 %."), ("**17 av 58 MOT (1,1 per 100) ser ingen.**", "**18 av 58 MOT (1,2 per 100) ser ingen.**"),
     ("rundt 62 per 1539 saker (183 × 20 min + 9 × 10 min)", "rundt 56 per 1539 saker (161 × 20 min + 14 × 10 min)"),
     ("(p ≥ 0,919)", "(p ≥ 0,923)"), ("122 saker i båndet, 183 i alt (10,4 %,", "99 saker i båndet, 161 i alt (10,5 %,"),
     ("havnet alle 35 falske flagg i sonen, der forvalteren avgjør selv. Utenfor sonen var alle 9 flagg ekte.", "havnet 32 av 35 falske flagg i sonen, der forvalteren avgjør selv. Utenfor sonen var 11 av 14 flagg ekte og 3 falske (den frosne modellen hadde 0 falske der)."),
     ("(1,1 per 100, 17 av 58 MOT på test)", "(1,2 per 100, 18 av 58 MOT på test)"),
     ("på test 2026 var 5 av de 17 usette", "på test 2026 (analysen er gjort på den frosne modellen; repo4 har 18 usette, 7 av dem i USA som før) var 5 av de 17 usette"),
     ("og der ligger 32 av 58 MOT og alle 35 falske flagg. Gjør mennesket dem riktig, blir F1 0,828", "og der ligger 29 av 58 MOT og 32 av 35 falske flagg. Gjør mennesket dem riktig, blir F1 0,792"),
     ("Følger mennesket bare styret, blir det 0,269.", "Følger mennesket bare styret, blir det 0,306."),
     ("inntil 71 % av MOT funnet (41 av 58), mot 52 % for maskinen alene (F1 0,828 mot 0,512)", "inntil 69 % av MOT funnet (40 av 58), mot 55 % for maskinen alene (F1 0,792 mot 0,512)"),
     ("71 % er en øvre grense", "69 % er en øvre grense"), ("17 av 58 MOT ser ingen", "18 av 58 MOT ser ingen"),
     ("| 32 av 58 (alle 35 falske MOT-flagg er også her) |", "| 29 av 58 (32 av 35 falske MOT-flagg er også her) |"),
     ("| 41 av 58, F1 0,828 hvis mennesket avgjør riktig (øvre grense); 0,269 hvis", "| 40 av 58, F1 0,792 hvis mennesket avgjør riktig (øvre grense); 0,306 hvis"),
     ("| 17 av 58 (P(MOT) under 0,15", "| 18 av 58 (P(MOT) under 0,15"), ("Lesetid ca. 62 timer", "Lesetid ca. 56 timer"),
     ("**Ærlig begrensning.** 17 av 58 MOT-stemmer", "**Ærlig begrensning.** 18 av 58 MOT-stemmer"), ("Få MOT-stemmer gir bredt KI; 17 av 58", "Få MOT-stemmer gir bredt KI; 18 av 58"),
     ("**Standard [0,15; 0,85)** | **183 (11,9 per 100)** | **9 / 32 / 17** | **0 / 38** |", "**Standard [0,15; 0,85)** | **183 (11,9 per 100)** | **9 / 32 / 17** | **0 / 38** |\n| *Standard, levert repo4 (#2592)* | *161 (10,5 per 100)* | *11 / 29 / 18* | *3 / 32* |"),
     ("de 17 bommene med P(MOT) ≤ 0,09 ser ingen. 7 av 17 er i USA", "de 18 bommene med P(MOT) ≤ 0,11 ser ingen (repo4; 17 med frossen). 7 av 18 er i USA"),
     ("**17 av de 28 bommene ser ingen.** De får P(MOT) ≤ 0,09 og rutes ikke til menneske. De andre 11 havner hos et menneske", "**18 av de 26 bommene ser ingen.** De får P(MOT) ≤ 0,11 og rutes ikke til menneske. De andre 8 havner hos et menneske (repo4, #2592; bomme-analysen i kilden er gjort på frossen modell, 17 av 28)"),
     ("finner 32. Den betaler 35 falske flagg for det, og alle 38 går til et menneske.", "finner 32. Den betaler 35 falske flagg for det, og 32 av dem går til et menneske."),
     ("Rutingen til menneske er 127 usikre med kalibrert\nP(MOT) i [0,15; 0,85), 60 ukjent selskap og 1 instruks; av de 1539 med fasit er 183 rutet (10,5 %), målt fra kald kopi 05.11 kl. 12.54.", "Rutingen til menneske er 101 usikre med kalibrert\nP(MOT) i [0,15; 0,85), 61 ukjent selskap og 1 instruks (+1 annen vakt); av de 1539 med fasit er 161 rutet (10,5 %), målt fra kald kjøring 05.11 kl. 17.03 (#2592)."),
     ("Agenten sier 188 til menneske (av 1578 inn), måleren 183", "Agenten sier 164 til menneske (av 1578 inn), måleren 161"),
     ("0,482 [0,375; 0,580]", "0,529 [0,42; 0,63] (frossen 0,482)"), ("avvik inkl. 5 AVSTÅ (66 saker) gir 0,4818", "avvik inkl. 5 AVSTÅ (66 saker) gir 0,5294"),
     ("> *Avvik:* 0,4818 er avvik fra styret", "> *Avvik:* 0,5294 er avvik fra styret"),
     ("0,4818 (TP 33 FP 38 FN 33, 66 avvik), KI [0,375; 0,580] (#2086)", "0,5294 (TP 36 FP 34 FN 30, 66 avvik), KI [0,42; 0,63] (#2592, `oppgave_2592/ki_avvik.py`; frossen 0,4818)"),
     ("0,4818 (avvik fra styret inkl. 5 AVSTÅ, 66 saker, KI [0,375; 0,580], #2086)", "0,5294 (avvik fra styret inkl. 5 AVSTÅ, 66 saker, KI [0,42; 0,63], #2592)"),
     ("0,4818 (avvik fra styret, 66 saker: 58 MOT, 5 AVSTÅ, 3 andre, KI [0,375; 0,580], #2086)", "0,5294 (avvik fra styret, 66 saker: 58 MOT, 5 AVSTÅ, 3 andre, KI [0,42; 0,63], #2592)"),
     ("F1 0,4818 er avvik fra styret (66 avvik", "F1 0,5294 er avvik fra styret (66 avvik"),
     ("rå grense 0,9188 (val-F1 0,522 på avvik, `c1_agent_real_2053.md`)", "rå grense 0,9232 for repo4 (val-F1 0,525 på avvik, `kjor_agent_real_test2026.txt`; frossen hadde 0,9188)"),
     ("**Grensen 0,9188:**", "**Grensen 0,9232:**")]
skriv = "--skriv" in sys.argv; tot = 0
for f in FILER:
    s0 = s = open(f, encoding="utf-8").read()
    L = s.split("\n")
    L = [RAD_B if l.startswith("| bare båndet: kalibrert P(MOT)") else RAD_S if l.startswith("| **standard** (bånd + ukjent") else l for l in L]
    s = "\n".join(L)
    for a, b in R: s = s.replace(a, b)
    s = re.sub(r"0,9188(?!\d)", "0,9232", s) if "levering/" in f or "JURY_SPORSMAL" in f else s
    if s != s0:
        n = sum(x != y for x, y in zip(s0.split("\n"), s.split("\n"))); tot += n; print(f"{n:3d} {f}")
        if skriv: open(f, "w", encoding="utf-8").write(s)
print(tot, "skrevet" if skriv else "(tørt)")
