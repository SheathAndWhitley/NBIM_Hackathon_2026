"""Lager STÅR-reserveutgaven (#2598) av README.md og kravrespons.md fra BYTT-utgaven i c1/leveranse/.

Bruk (fra landsbymappen):  uv run python -I arbeid/oppgave_2598/lag_staar.py [--sjekk]
Skriver til arbeid/hack/c1/reserve_staar/. Rører aldri leveranse/ eller levering/.
Hver erstatning må finnes nøyaktig én gang i BYTT-teksten, ellers stopper skriptet (så en endret BYTT-tekst ikke gir en stille feil).
Frosne tall er fra git 5442ccd (README) og acdd689 (kravrespons), dvs. tekstene før bytt_tall.py.
"""
import pathlib, sys

ROT = pathlib.Path(__file__).resolve().parents[2]
KILDE = ROT / "arbeid/hack/c1/leveranse"
MAAL = ROT / "arbeid/hack/c1/reserve_staar"
VILKAR = ("og kontrollagenten (en egen agent som ikke målte kandidatene) dømte BYTT kl. 17:02 på vilkår om at hele pakken "
          "med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45.")
STAAR = VILKAR + (" Kandidaten besto regelen, men pakken med repo4 var ikke reprodusert fra kald start før fristen, "
                  "så den frosne agenten står med 0,476")
# #2640: jury-rettelsene (#2637) ligger i reglene under (1b, 3a, 4a, 4h, 5a, 5c, 5e), så de overlever ombygging.
README = [
    ("F1 **0,512 på MOT mot styret**, 95 % KI [0,40; 0,62]", "F1 **0,476 på MOT mot styret**, 95 % KI [0,36; 0,59]"),
    ("P 0,48, R 0,55 (TP 32 FP 35 FN 26). Følg styret har", "P 0,44, R 0,52 (TP 30 FP 38 FN 28). Følg styret har"),
    ("Grensen er valgt på val 2025 (0,530); 2026 ble brukt til å finne repo4, så 2026 er ikke et friskt testår (rutingsbåndet", "Valgt på val 2025 (0,520), kjørt én gang på test (rutingsbåndet"),  # BYTT-form etter #2723
    ("Til menneske: 164 av 1578 saker inn (10,4 %)", "Til menneske: 188 av 1578 saker inn (11,9 %)"),
    ("(rutingsbåndet er valgt ut fra test og sjekket på val); repo4 (frossen modell + fire historikktrekk) ble deretter byttet inn etter regelen på tre testår (2024–2026).",
     "(rutingsbåndet er valgt ut fra test og sjekket på val)."),  # BYTT-form etter #2653 (#2681): byttesetningen strykes i STÅR
    # 1a (BYTT) -> 1b (STÅR)
    ("> Vi leverer repo4 (frossen modell + fire historikktrekk), ikke V2. V2 er en tidligere variant (0,516 på test), men den ble målt på test etter frysen uten en regel satt før måling, "
     "og avstanden til V1 (en eldre variant, ikke den frosne) er innenfor støyen (+0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19.",
     "> Vi leverer den frosne agenten med vilje. V1 og V2 er eldre varianter, ikke den frosne (V1-raden i `ERLIG_EVALUERING.md` § 7 er derfor et annet tall "
     "enn «frossen»). V2 gir 0,516 på test, men ble målt på test etter frysen og er innenfor støyen (V2 − V1 +0,040, KI [−0,007; +0,095]); se `JURY_SPORSMAL.md` sp. 19."),
    # 4b (BYTT) -> 4a (STÅR)
    (VILKAR + " Det gjorde den (se `ERLIG_EVALUERING.md` § 7)", STAAR + " (se `ERLIG_EVALUERING.md` § 7)"),
    # 3c (BYTT) -> 3a (STÅR)
    ("> **Om de andre tallene i pakken:** V2 0,516, NBIM-hybrid 0,545 og 0,529 er målt på test etter frysen uten en regel satt på forhånd, og står bare som sidetall. "
     "Repo4 er levert fordi den besto regelen satt før måling (snitt over 2024–2026, avgjort av 2024 og 2025, som ble målt etter at regelen var skrevet), ikke fordi 0,512 er høyest. "
     "Alle kandidater målt etter byttet står i `KANDIDATER.md`; ingen nådde +0,02.",  # BYTT-form etter #2723
     "> **Hvorfor vi leverer et lavere tall enn flere andre i pakken:** alle høyere tall (V2 0,516, NBIM-hybrid 0,545, 0,529, repo4 0,512) er enten målt på test "
     "etter frysen uten en regel satt på forhånd, eller faller under den frosne på 2024. Repo4 er det eneste som besto regelen, og den ble ikke levert fordi den "
     "ikke var reprodusert fra kald start før fristen."),
    # #2723: forbehold, grense og løpende stemmer tilbake til eldre frossen-form
    ("> **Største forbehold:** en del av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong; for den eldre frosne modellen var det ca. 0,06, for repo4 er golvet ikke målt.",
     "> **Største forbehold:** omtrent 0,06 av F1 kommer fra NBIMs egne tidligere stemmer i samme sesong."),
    ("grensen (rå 0,919 for repo4) er valgt for F1 på val", "grensen (rå 0,9232) er valgt for F1 på val"),
    ("Hvorfor MOT allerede ved kalibrert P(MOT) ca. 0,19:", "Hvorfor MOT allerede ved lav kalibrert P(MOT):"),
    # 5d (BYTT) -> 5c (STÅR)
    ("Uten den historikken er F1 0,415 [0,30; 0,53] (målt på den frosne modellen), bare", "Uten den historikken er F1 0,415 [0,30; 0,53], bare"),
    ("`c1/tall_tabell.md` gir [0,40; 0,62].", "`c1/tall_tabell.md` gir [0,37; 0,59]."),
    ("3 andre) 0,529 [0,42; 0,63] (frossen 0,482). Rutingen til menneske er 101 usikre",
     "3 andre) 0,482 [0,375; 0,580]. Rutingen til menneske er 127 usikre"),
    ("61 ukjent selskap og 1 instruks (+1 annen vakt); av de 1539 med fasit er 161 rutet (10,5 %), målt fra kald kjøring 05.11 kl. 17.03 (#2592).",
     "60 ukjent selskap og 1 instruks; av de 1539 med fasit er 183 rutet (11,9 %), målt fra kald kopi 05.11 kl. 12.54."),
    ("TP 32 FP 35 FN 26 TN 1446, F1 MOT 0,512, accuracy 96,0 %", "TP 30 FP 38 FN 28 TN 1443, F1 MOT 0,476, accuracy 95,7 %"),
    # 5f (BYTT) -> 5e (STÅR)
    ("**Les bare linja `MOT mot styret … F1 0.5120`; det er hovedtallet.** Linja `SCORE 0.529412` er IKKE hovedtallet:",
     "**Les bare linja `MOT mot styret … F1 0.4762`; det er hovedtallet.** Linja `SCORE 0.481752` er IKKE hovedtallet:"),
    ("  avvik: TP 36 FP 34 FN 30  P 0.5143  R 0.5455  F1 0.5294  PR-AUC 0.5368", "  avvik: TP 33 FP 38 FN 33  P 0.4648  R 0.5000  F1 0.4818  PR-AUC 0.5245"),
    ("MOT mot styret: TP 32 FP 35 FN 26  P 0.4776  R 0.5517  F1 0.5120", "MOT mot styret: TP 30 FP 38 FN 28  P 0.4412  R 0.5172  F1 0.4762"),
    ("\nSCORE 0.529412\n", "\nSCORE 0.481752\n"),
    ("**Hovedtallet (F1 0,512 på MOT mot styret):**", "**Hovedtallet (F1 0,476 på MOT mot styret):**"),
    # 4h
    ("modellen (internt kalt repo4: den frosne «miks h2» pluss fire historikktrekk)", "den frosne modellen (internt kalt «miks h2»)"),
]
KRAV_VILKAR = "og kontrollagenten dømte BYTT kl. 17:02 på vilkår om at pakken kjørte feilfritt fra kald start, og det gjorde den"  # BYTT-formen etter #2653 (#2681)
# #2654: STÅR uten internspråk («grønn») og med repo4 forklart første gang
KRAV_STAAR = "og kontrollagenten dømte BYTT kl. 17:02 på vilkår om at hele pakken med repo4 kjørte feilfritt fra kald start, med samme tall, innen 18:45. Kandidaten besto regelen, men pakken med repo4 var ikke reprodusert fra kald start før fristen, så den frosne agenten står med 0,476"
KRAV = [
    ("til et menneske (164 av 1 578 saker på test 2026)", "til et menneske (188 av 1 578 saker på test 2026)"),
    ("NBIMs tidligere MOT-stemmer i selskapet, pluss fire historikktrekk (forrige stemme på samme punkt og person, avvik i forrige møte, avviksrate for sakstypen); internt kalt repo4. På test 2026 finner den 32 av 58 stemmer mot styret: F1 på MOT 0,512 (presisjon 0,48, recall 0,55)",
     "NBIMs tidligere MOT-stemmer i selskapet. På test 2026 finner den 30 av 58 stemmer mot styret: F1 på MOT 0,476 (presisjon 0,44, recall 0,52)"),
    (KRAV_VILKAR + ".", KRAV_STAAR + "."),
    ("(2024–2026): repo4 (frossen modell + fire historikktrekk) ga snitt", "(2024–2026): repo4 (frossen + fire historikktrekk) ga snitt"),  # #2654, BYTT-form etter #2653
    ("Grensen er valgt på 2025; 2026 ble brukt til å finne repo4, så 2026 er ikke et friskt testår. 95 %-intervall [0,40; 0,62]", "Modell og grense er valgt på 2025 og kjørt én gang på 2026, med 95 %-intervall [0,36; 0,59]"),  # BYTT-form etter #2723
    ("For den eldre frosne modellen kom ca. 0,06 av F1 fra NBIMs stemmer tidligere i samme sesong (uten dem 0,415); for repo4 er golvet ikke målt.",
     "Omtrent 0,06 av F1 kommer fra NBIMs stemmer tidligere i samme sesong (uten dem 0,415)."),  # #2723  # BYTT-form etter #2653 (#2681)
    ("og 0,512 ligger like over målet vårt på 0,5", "og 0,476 ligger under målet vårt på 0,5"),  # BYTT-form etter #2653 (#2681)
]
BYTT_SPOR = ["0,512", "0.5120", "0.5294", "0.529412", "TP 36", "164 av", "10,4 %", "P 0,48", "R 0,55", "presisjon 0,48", "32 av 58", "TP 32", "1446", "96,0", "0,40; 0,62",
             "0,529", "101 usikre", "61 ukjent", "161 rutet", "17.03", "0,530", "pluss fire historikktrekk", "Det gjorde den", "Vi leverer repo4"]

def lag(navn, regler):
    s = (KILDE / navn).read_text()
    for gammel, ny in regler:
        n = s.count(gammel)
        if n != 1:
            sys.exit(f"{navn}: fant {n} treff (skal være 1) for: {gammel[:70]}")
        s = s.replace(gammel, ny)
    # repo4-dommens egne tall og sidetall (0,5120, 0,529) skal stå i linjer merket tallvakt-ignorer; sjekk bare utenfor dem
    uten_dom = "\n".join(l for l in s.splitlines() if "tallvakt: ignorer" not in l)
    rest = [sp for sp in BYTT_SPOR if sp in uten_dom]
    if rest:
        sys.exit(f"{navn}: BYTT-tall igjen utenfor dom-linjene: {rest}")
    return s

if __name__ == "__main__":
    ut = {"README.md": lag("README.md", README), "kravrespons.md": lag("kravrespons.md", KRAV)}
    if "--sjekk" in sys.argv:
        for navn, s in ut.items():
            print(f"{navn}: {'LIK' if (MAAL / navn).exists() and (MAAL / navn).read_text() == s else 'ULIK/MANGLER'}")
    else:
        MAAL.mkdir(exist_ok=True)
        for navn, s in ut.items():
            (MAAL / navn).write_text(s); print(f"skrev {MAAL / navn}")
