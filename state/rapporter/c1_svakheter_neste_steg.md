# Case 1: tre svakheter i metoden og hva vi ville gjort med en uke til (#2310)

Alle tallene er hentet fra rapportene som er nevnt. Ingenting er målt på nytt, og levert agent er ikke rørt.

**1. India-regelen hviler på ett ærlig bevis, og det er én sak.**
Tall: val 2025 0,520 → 0,562 (+0,042, 5 av 5 snudde saker riktige), men regelen ble *funnet* på val 2025. Holdt-ut 2024 (trent på år < 2024): 0,536 → 0,544 (+0,008). Her snur bare én sak (1886920|4). Test 2026 er ikke kjørt.
Kilde: `state/rapporter/c1_india_frys_kandidat.md`.
Med en uke til: vi ville gjort regelen om fra en håndlaget bryter til et land×tema-trekk, lært med rullerende opprinnelse (tren på < år, mål på år) for 2021–2025. Vi ville bare beholdt den hvis den parede gevinsten summert over årene har et KI over 0, ikke hvis den vinner én sak.

**2. Injeksjonsvakta slipper gjennom 6 av 17 instrukser skrevet i Title Case.**
Tall: 11 av 17 fanget. De 6 som slipper («The Board Knows Best», «Do As The Board Says» …) endrer 18–27 stemmer uten at et menneske ser dem, og F1 faller til 0,39–0,42 (rent 0,476). Bare blind sett 2 er helt blindt (5 av 8 fanget). Strammere regel flagger ekte titler.
Kilde: `state/rapporter/c1_injeksjonsvakt.md` (logg `arbeid/oppgave_2265/inj_ny_v4.log`).
Med en uke til: vi ville sammenlignet med selskapets egne tidligere titler. En ny tittel som ikke likner noen NBIM- eller N-PX-tittel for samme selskap og type går til et menneske. I tillegg ville vi laget et blindt angrepssett på 50+ fraser, skrevet av en som ikke har sett vakta, og målt fangst og falske flagg på det før vi endrer regelen.

**3. Hovedtallet er usikkert: F1 MOT 0,476 med 95 % KI [0,36; 0,59].**
Tall: test 2026 har bare 58 MOT-saker av 1539. Klyngebootstrap per selskap (135 selskaper, 2000 trekk) gir ±0,12. Val 2025 gir 0,520 [0,41; 0,63], og intervallene overlapper nesten helt. Den eldre kandidaten (0,482) gir [0,375; 0,580] med samme metode. Forskjeller under ~0,02 tilsvarer ±1 sak.
Kilde: `state/rapporter/c1_bootstrap_f1.md` (metode, eldre kandidat), `state/rapporter/c1_erlig_evaluering_2096.md` og `arbeid/oppgave_2095/ki_mot.py` (levert tall).
Med en uke til: vi ville samlet flere MOT-saker ved å legge 2023–2024 til som rullerende testår (en modell per år, trent bare på tidligere år) og rapportert et samlet F1 med KI over alle årene. Hver modellendring ville vi avgjort med en paret bootstrap mot levert agent, ikke ved å sammenligne punkttall.

Fellesnevner: alle tre svakhetene kommer av for få MOT-saker per år. Neste uke handler derfor om flere ærlige testår, ikke om en bedre modell.
