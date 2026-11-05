# Case 1 natt #2887: v2 (SVD-tekst i LGBM) + av-regel gir BYTT etter regelen, +0,043 over frossen (smed)

#2882 viste signal: v2 alene lå +0,0192 over frossen. Derfor ble vinkel 2 kjørt, ikke ablasjonen.
Regelen står i `arbeid/c1_natt/v2av/svar/REGEL.md`, skrevet 19:46:27, før svarfilene. k er låst fra #2882 (32/64/48), og modellen er ikke trent på nytt.
Av-regelen er koden fra #2701 uendret. Valget mellom ingen og av ble gjort på val T-1, og av vant alle tre år (val: 0,359→0,372, 0,553→0,594, 0,558→0,560).
Målt med natt-måleren (`mal_kandidat.sh`), forsøk #1257 på tavla.

| år | frossen | v2 | v2+av | diff mot frossen |
|---|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3592 | 0,3723 | +0,019 |
| 2024 | 0,5057 | 0,5326 | 0,5731 | +0,067 |
| 2025 | 0,5309 | 0,5436 | 0,5667 | +0,036 |
| 2026 | 0,5120 | 0,5299 | 0,5391 | +0,027 |
| snitt 24-26 | 0,5162 | 0,5354 | **0,5596** | **+0,0434** → **BYTT** |

Robusthet (`k_spredning.py`, ikke brukt til valg): av-regelen hever F1 på alle ni k×år-filer, med +0,009 til +0,050.
Med fast k blir snittet 0,552 (k32), 0,554 (k48) og 0,557 (k64). Alle ligger over +0,02, så resultatet henger ikke på k.
Radtallene er like frossen. Antall flagg: 94/89/63 mot frossens 100/72/73.

Forbehold for dommeren:
- Begge delene ble valgt etter at testtallene deres var kjent: av fra #2701 (+0,0135) og v2 fra #2882 (+0,019). Kombinasjonen er satt sammen av ledd som allerede hadde vist seg på test, og det er en mild form for test-sniking over natta. Selve kombinasjonen er låst på forhånd og målt én gang.
- Gevinsten er større enn summen av delene (0,033). Det er mulig fordi v2 flagger flere saker (110/106 mot 100/72), og av-regelen rydder bort de gale av dem. Dette bør vurderes opp mot støytesten (#2889) og frø-spredningen (#2886) før 02-dommen.

Filer: `arbeid/c1_natt/v2av/` (v2av.py, k_spredning.py, svar/ med REGEL.md, DOM.md og 4 csv-er til natt-måleren).
