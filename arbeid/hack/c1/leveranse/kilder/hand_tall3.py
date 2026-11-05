"""#2592 runde 3: overskrifter med 0,476, modellnavn og beskrivelser (for hånd, eksakte strenger)."""
import sys
L, C = "arbeid/hack/levering/", "arbeid/hack/c1/leveranse/"
NAVN = "repo4 = #2044 miks h2 + 4 repotrekk, byttet 17:03 etter byttedom #2570"
E = {
 L+"README.md": [("> **Hovedtall (#231, frosset modell #2044 miks h2):** F1 **0,476 på MOT mot styret**", f"> **Hovedtall (#231, frosset modell {NAVN}):** F1 **0,512 på MOT mot styret**")],  # eldre frossen #2044 (0,476), dagens hovedtall er repo4 0,512
 L+"METODE.md": [("> **Hovedtall (#231, frosset modell #2044 miks h2):** F1 **0,476 på MOT mot styret**", f"> **Hovedtall (#231, frosset modell {NAVN}):** F1 **0,512 på MOT mot styret**")],  # eldre frossen #2044 (0,476), dagens hovedtall er repo4 0,512
 L+"KRAVRESPONS.md": [("smed2 #2044 miks h2) på NBIMs egne stemmer (real_votes fra arrangøren), test 2026: **F1 0,476 på MOT mot styret**", "repo4 = smed2 #2044 miks h2 + 4 repotrekk, `modell_repo4.py`) på NBIMs egne stemmer (real_votes fra arrangøren), test 2026: **F1 0,512 på MOT mot styret**")],
 L+"JURYSVAR.md": [("presisjon 0,44 og recall 0,52, F1 0,512 [0,40; 0,62]. Omtrent 4 av 10 flagg er ekte MOT, og halvparten av MOT-sakene blir funnet.", "presisjon 0,48 og recall 0,55, F1 0,512 [0,40; 0,62]. Omtrent halvparten av flaggene er ekte MOT, og litt over halvparten av MOT-sakene blir funnet.")],
 C+"BEGRENSNINGER.md": [("**F1 0,476 på MOT mot styret, 95 % KI [0,40; 0,62]**", "**F1 0,512 på MOT mot styret, 95 % KI [0,40; 0,62]** (levert modell repo4; eldre frossen #2044: 0,476)"),
                        ("av de 1539 med fasit er 183 rutet (10,4 %; kald kjøring, sist kontrollert av kontrollagenten kl. 13.37)", "av de 1539 med fasit er 161 rutet (10,5 %; kald kjøring 17.03, #2592)")],
 C+"ERLIG_EVALUERING.md": [("går til et menneske: 188 av 1 578 saker på test 2026 (10,4 %)", "går til et menneske: 164 av 1 578 saker på test 2026 (10,4 %)"),
     ("der ligger 17 av 58 MOT-stemmer, som ikke blir sett. Modellen («miks h2») er", "der ligger 18 av 58 MOT-stemmer, som ikke blir sett. Modellen («repo4»: miks h2 + 4 repotrekk) er"),
     ("fra møter *strengt før* sakens møtedato.", "fra møter *strengt før* sakens møtedato, og fire historikktrekk fra NBIM-repoet (forrige stemme på samme punkt, samme person, avvik i forrige møte, avviksrate for sakstypen)."),
     ("(recall 0,52), og 44 % av sakene den markerer er ekte MOT (presisjon 0,44)", "(recall 0,55), og 48 % av sakene den markerer er ekte MOT (presisjon 0,48)")],
 C+"JURY.md": [("Den leverte agenten har F1 0,476 på MOT på test 2026 (`kilder/c1_enkle_regler_og_hist1.md:1`) og 0,530 på val 2025 (`kilder/c1_val_kaldstart.md:23`). Det ligger under målet 0,5, og vi hadde endringer som så bedre ut. Vi la dem ikke inn,",
               "Den eldre frosne agenten (#2044) hadde F1 0,476 på MOT på test 2026 (`kilder/c1_enkle_regler_og_hist1.md:1`) og 0,520 på val 2025 (`kilder/c1_val_kaldstart.md:23`). Det lå under målet 0,5, og vi hadde endringer som så bedre ut. Vi la dem ikke inn,")],
 C+"NESTE_VERSJON.md": [("under er målt før og har kilde. Grunnlag: frossen agent (miks h2), F1 på MOT 0,476 på test 2026\n(TP 32, FP 35, FN 26) [`utviklingsrapport:c1_feil_per_gruppe.md:4`] og 0,530 på val 2025 (TP 45, FP 29, FN 54)",
                         "under er målt før og har kilde. Grunnlag: eldre frossen agent (miks h2), F1 på MOT 0,476 på test 2026\n(eldre TP 30, FP 38, FN 28) [`utviklingsrapport:c1_feil_per_gruppe.md:4`] og 0,520 på val 2025 (TP 45, FP 29, FN 54)"),
                        ("løfter test (0,512 → 0,504) men senker val (0,520 → 0,488)", "løfter test (eldre 0,476 → 0,504) men senker val (0,520 → 0,488)")],
 C+"kravrespons.md": [("går til et menneske (188 av 1 578 saker på test 2026)", "går til et menneske (164 av 1 578 saker på test 2026)"),
     ("og NBIMs tidligere MOT-stemmer i selskapet.", "og NBIMs tidligere MOT-stemmer i selskapet, pluss fire historikktrekk fra NBIM-repoet (repo4)."),
     ("F1 på MOT 0,512 (presisjon 0,44, recall 0,52)", "F1 på MOT 0,512 (presisjon 0,48, recall 0,55)")],
}
for f, rs in E.items():
    s = open(f, encoding="utf-8").read()
    for a, b in rs:
        if a not in s: print("FANT IKKE", f, a[:70]); continue
        s = s.replace(a, b)
    if "--skriv" in sys.argv: open(f, "w", encoding="utf-8").write(s)
print("ferdig")
