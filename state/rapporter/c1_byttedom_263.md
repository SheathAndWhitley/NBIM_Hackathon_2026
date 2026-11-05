# Case 1: byttedom (ordre #263, #2529): V1 STÅR. Beste kandidat V2 oppfyller ikke de forhåndsregistrerte kravene

**BESLUTNING: V1 STÅR.** Frossen #2044 (F1 MOT test 2026 0,476) blir hovedsvar. V2 (0,516) feiler krav 2 (KI-nedre mot frossen er −0,007, krysser null) og krav 3 (ikke i pakken, ingen etterfrys-kjøring). Hybriden fra det andre laget alene (0,545) feiler krav 1 (terskel og trekk valgt med 2025 i utvalget og 2026 synlig for forfatterne) og krav 3. Kravene står i `state/rapporter/c1_byttekrav_v2.md`, skrevet 16:16, før kandidatene ble dømt. Dom gitt 16:37, dommer.

## Hva dommeren målte selv (ikke smedens tall)
Alt kjørt fra egen kopi i `arbeid/oppgave_2529/` med `python3 -I`. V2-valget (`kombiner.py`) reprodusert: a=0,4074, b=0,091, t=0,919, og svarfilene for V1, V1p og V2 er byte-like smedens.

| svar | val 2025 F1 MOT (offisiell måler, 99 i fasit) | test 2026 F1 MOT (offisiell måler v3, 58 i fasit) | TP/FP/FN test | KI mot frossen (parret klyngebootstrap, 2000) |
|---|---|---|---|---|
| frossen #2044 (v1) | **0,520** | 0,476 | 30/38/28 | – |
| V2: hybrid sikker ja (h ≥ 0,407) / sikker nei (h < 0,091), vår p ≥ 0,919 i midten | 0,548 | 0,516 | 32/34/26 | +0,040 [**−0,007**; +0,095], B<A 5 % |
| hybrid alene (det andre lagets repo, vår splitt) | 0,525 (egen t_flag valgt der) | 0,545 | 30/22/28 | +0,069 [+0,007; +0,133], B<A 1 % |
| V2 mot hybrid alene | | | | −0,029 [−0,067; +0,010], B<A 93 % |

**0,520 eller 0,522 for frossen på val:** 0,520 er riktig (offisiell måler på `full_val.csv`, TP 45 FP 29 FN 54 = 0,5202). 0,522 har aldri vært et måleresultat for val; det nærmeste er terskelvarianten p ≥ 0,919 som gir 0,523 og p ≥ 0,923 som gir 0,529 i kombiner-definisjonen, men den frosne terskelen er den som ligger i svarfila, og den gir 0,520.

## Kravene, ett for ett

| # | Krav | V2 | Hybrid alene |
|---|---|---|---|
| 1 | Terskel og regel valgt på val 2025 alene, og v2 slår v1 på val | **JA med forbehold.** Argmax på val i koden, test rører ikke valget. Val 0,548 > 0,520. Forbehold: hybridens modellvalg (GBM etter PR-AUC) og t_flag 0,4074 er valgt på samme 2025, så komponenten er delvis i utvalget. Repoets trekk (personregex, presedens) er laget av forfattere som hadde 2026 synlig (repoets egen splitt tester på 2025–2026). | **NEI.** Val 0,525 er helt i utvalget. Trekkene er laget med 2026 synlig. |
| 2 | Test > 0,476 og KI-nedre > 0 | **NEI.** 0,516 > 0,476, men KI-nedre −0,007. | **JA.** KI-nedre +0,007. |
| 3 | Kald start grønn med v2 i pakken, frysvakt urørt, tallvakt 0 avvik | **NEI.** Ikke i pakken, ingen etterfrys-kjøring, ingen tallvakt. Frysvakt for v1 grønn (17 filer). | **NEI.** Samme. |
| 4 | Ferdig før 18:30 | Dom 16:37. Tiden holdt, men irrelevant når 2 og 3 mangler. | Samme. |

Alle fire må oppfylles. Ingen av kandidatene gjør det. **V1 står.**

## Forbeholdene som skal stå i jurysvaret uansett
- **Antall testblikk etter frys kl. 16:** minst 8 distinkte F1-tall for test 2026 er sett etter frys (0,485 #2485; 0,525 og 0,512 #2490; 0,516, 0,481 og 0,492 #2495; 0,545 hybrid alene #2464; 0,476 #2496 uten person). Med 58 positive og KI på omtrent ±0,10 vil den beste av 8 blikk ventes å ligge over sin sanne verdi. Det er grunnen til at et testtall alene ikke kan utløse bytte.
- **Hybridens t_flag og modellvalg er gjort på 2025**, samme år som V2 velger a, b og t på. Val-tallet 0,548 er derfor optimistisk, og avstanden til frossen på val (0,028) er mindre sikker enn den ser ut.
- **Repoet er laget med 2026 synlig.** Repoets egen splitt bruker 2025–2026 som test; forfatterne har hatt fasit for 2026 på skjermen mens trekk og regler ble laget. Vi kan ikke reparere det i dag. Alle tall for hybriden på test 2026 er derfor ikke rene prediksjoner i vår protokolls betydning.

## Svar til guden (ordre #263): hvorfor ikke bare «beste overall»?
1. **«Beste» er målt på test.** Vi har ingen uavhengig data igjen. Alle kandidatene over 0,476 ble funnet etter frys, med 2026-fasiten synlig. Hvis vi velger den med høyest testtall, er testtallet ikke lenger et estimat på hvor god agenten er, men et estimat på hvor heldige vi var i 8 trekk. Juryen vekter metode og ærlig evaluering 60 %. Et hovedtall som er valgt på test er det motsatte.
2. **Forskjellen er innenfor støyen.** V2 mot frossen: +0,040 med KI [−0,007; +0,095]. Vi kan ikke si at V2 er bedre. Hybriden alene er signifikant bedre (+0,069, KI-nedre +0,007), men den er det andre lagets modell, laget med 2026 synlig, og vi kan ikke verifisere den fra kald start i vår pakke før 18:30.
3. **Frysen er selve metodeargumentet.** Det som gjør 0,476 troverdig er at terskel, trekk og modell ble låst kl. 16 på val 2025, og at test 2026 ble målt én gang etterpå. Bytter vi nå, mister vi det eneste tallet i pakken juryen kan stole på, og får et som ser bedre ut men ikke er det.
4. **Riktig fremgangsmåte, og den vi følger:** frossen v1 er hovedtall. V2 og hybriden står i NESTE_VERSJON og JURY_SPORSMAL pkt 13 som «målt etter frys, ikke hovedtall», med tall, KI, antall testblikk og hvilket krav som manglet. Det viser juryen både at vi fant noe bedre, og at vi vet hvorfor vi ikke kan påstå det.

## Kommandoer
```
cd arbeid/oppgave_2529 && python3 -I kombiner.py && cd ../..
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2529/svar_V2_t2026.csv test --data real --score mot
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2529/svar_V2_val2025.csv val --data real --score mot
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2103/full_val.csv val --data real --score mot
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2529/svar_V2_t2026.csv test
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2464/svar_vaar_hybrid_t2026.csv test
```
