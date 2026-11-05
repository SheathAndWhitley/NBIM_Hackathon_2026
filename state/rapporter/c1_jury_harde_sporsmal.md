# Case 1 (#2674): tre harde juryspørsmål om svakheter som ikke har svar ennå, med svar på 2 linjer

Lest: `c1/SVAKHETER.md` og `c1/leveranse/JURY_SPORSMAL.md` (sp. 1–23). De tre spørsmålene under er ikke besvart der.
KP: forventet repo4 test 2026 TP 32 av 58 MOT (`kilder/c1_repo4_tall_2592.md`). Fikk 32 av 58 med `arbeid/oppgave_2674/klynger.py` (OK).

## A. Lekkasje: «De fire repo4-trekkene er designet av hybridforfatterne, som hadde 2025–26 som sin test. Er 2025 da et friskt år?»
Nei, bare 2024 er helt friskt for trekk-designet: der er repo4 +0,051 over frossen, men KI [−0,065; +0,160] krysser null, og kontrollåret 2023 gir +0,005.
Gevinsten fra byttet er derfor sannsynlig, ikke bevist. Det vi står på, er rangeringen og regelen fra før måling, ikke 2025-tallet.
Kilder: sp. 13 («2025–26»), sp. 19, `ERLIG_EVALUERING.md` § 7 (per år-KI, 2023-kontroll).

## B. Få MOT: «58 MOT er få. Står de i noen få selskaper, slik at det reelle utvalget er mye mindre?»
Nei: de 58 MOT ligger i 43 selskaper og 44 møter, og ingen har mer enn 3; de 32 treffene ligger i 26 selskaper.
Derfor er KI per selskap [0,40; 0,62] nesten likt KI per rad [0,397; 0,616], men bredden ±0,11 er fortsatt det ærlige tallet.
Kilder: `arbeid/oppgave_2674/klynger.py` (ny, målt 17:5x på `oppgave_2612/kjor/pakke_repo4_test.csv`, byte-lik pakkas), `kilder/c1_repo4_tall_2592.md`.

## C. Terskel: «På val er F1 flat (0,510–0,530 over 0,90–0,95), men på test spenner den 0,500–0,579. Er 0,512 bare flaks med grensa?»
Delvis: val skiller ikke grensene, så valget i båndet er nesten tilfeldig, og på test flytter grensa alene F1 fra 0,500 til 0,579.
Vi valgte 0,9232 fordi den var høyest på val og melder 0,512; 0,95 (0,579 på test) ville vært å velge på test.
Kilde: terskeltabellen for repo4 i `kilder/c1_repo4_tall_2592.md` (rader 0,90 / 0,9232 / 0,95).

## Funn under lesingen (til smed før 19:00, ikke rørt av meg)
- **Sp. 15 har tall fra feil modell.** Teksten sier grensa 0,9232 (repo4), men «F1 fra 0,373 til 0,532 over 0,85–0,97» er den frosne #2044s tabell (grense 0,9188, `kilder/TREFFSIKKERHET.md:74-79`). For repo4 er spennet 0,373–0,579 (`kilder/c1_repo4_tall_2592.md`). Rett til: «fra 0,373 til 0,579 over grensene 0,85–0,97, og 0,95 ville vunnet på test».
- Svar C forutsetter at sp. 15 er rettet, ellers motsier de hverandre.

## Til smeden
Lim inn A–C som sp. 24–26 før «## Hull vi kjenner» i `leveranse/JURY_SPORSMAL.md` hvis dommeren godkjenner. Hvert svar har `<!-- tallvakt: ignorer: ... -->` behov for A og C (per år-tall og terskelrader, ikke hovedtall).
