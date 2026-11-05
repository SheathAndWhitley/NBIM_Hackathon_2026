# Case 1: måler v3 på NBIMs egne N-PX-stemmer (dommer, #1966): 129 avvik i testsettet, gulvet er F1 0,38

**Til smedene (én linje):** `python3 -I arbeid/hack/c1/maaler.py PRED.csv --fasit arbeid/hack/c1/data_v3/fasit.csv`. Det er rundens aktive måler, **maaler-sha 823c9610fe**. Tren på `data_v3/train.csv`, prediker `data_v3/test_input.csv`. Tuning skjer på `data_v3_val/` (tren 2024, valider 2025), ikke på test.

## Hva v3 er
- Kilde: `arbeid/arkitekt/hack1942/nbim_votes.csv` (Norges Bank N-PX, CIK 1374170, 4857 rader). Bygges med `python3 -I arbeid/hack/c1/lag_v3.py`, samme skjema som v2, så `run.sh` og `train.py` går uendret.
- Tidssplitt per N-PX-år: tren 2024 (møter 07.2023–06.2024), valider 2025, test 2026 (07.2025–06.2026). Splitten asserter at alle treningsmøter ligger før testmøtene. Det er ingen selskapssplitt. Fjorårets stemme er offentlig når en ny stemme skal avgis, og 1121 av 1225 testselskaper finnes i train.
- **Lekkasje:** `managementRecommendation` betyr «med/mot ledelsen» også hos NBIM. 411 say-on-pay-rader har AGAINST/AGAINST, og styret anbefaler aldri mot sin egen lønnspakke. Feltet er fasiten og leses aldri. Styret utledes som FOR, fordi say-on-pay er selskapets eget forslag (kilde ISSUER).
- Data: N-PX fra NBIM inneholder **bare say-on-pay**, altså ingen styrevalg og ingen aksjonærforslag. Frekvensstemmene (ONE YEAR 436, THREE 30, TWO 1) holdes utenfor, fordi styrets frekvensanbefaling ikke kan utledes uten lekk-feltet.
- Enhet = forslag (cusip, dato, tekst). Duplikater er slått sammen: 4383 unike forslag.

| sett | forslag | avvik (MOT) | følg styret acc |
|---|---|---|---|
| train 2024 | 1631 | 149 (9,1 %) | 0,909 |
| val 2025 | 1506 | 136 (9,0 %) | 0,910 |
| **test 2026** | **1246** | **129 (10,4 %)** | **0,897** |

**Kontroll mot casens tall (ca. 93–94 %): stemmer IKKE.** «Følg styret» gir 91,0 % på 2025 (91,6 % med frekvensstemmene, regnet med lekk-feltet bare til denne kontrollen) og 89,7 / 90,5 % på 2026. Arkitektens 113/1621 for 2025 lar seg ikke reprodusere: CSV-en har 136 AGAINST av 1621. Casens tall gjelder trolig alle NBIM-stemmer globalt, mens N-PX bare dekker amerikansk say-on-pay, der NBIM er strengere. Uansett er accuracy fella: 90 % er det samme som null funn.

## Målt på v3 test 2026 (avvik = MOT, hovedtall)
| kandidat | P | R | F1 (SCORE) | PR-AUC | acc | tavle | val 2025 F1 |
|---|---|---|---|---|---|---|---|
| følg utledet styre (FOR) | 0 | 0 | 0,000 | 0,104 (= basisrate) | 0,897 | #983 | 0,000 |
| **dommer-gulv: MOT hvis NBIM stemte MOT på selskapet før** (`gulv_v3.py`) | 0,348 | 0,426 | **0,383** | **0,328** | 0,858 | #984 | 0,361 |
| smed2 #1949 lgbm (uendret kode) | 0,269 | 0,411 | 0,325 | 0,262 | 0,823 | #985 | 0,190 |
| smed3 #1950 sitatagent v5 (uendret kode) | 0 | 0 | 0,000 | 0,107 | 0,897 | #986 | 0,362 |

Kandidatene ble kjørt på kopier: `arbeid/kandidater/dommer_v3_smed2kopi`, `arbeid/hack/varianter/dommer_v3_smed3kopi`. Smedenes egne mapper er ikke rørt. Prediksjonene ligger i `arbeid/hack/c1/ut_v3/`.

## Dom
- Ingen kandidat slår gulvet. Det ærlige nivået å slå er **F1 0,383 / PR-AUC 0,328**, og det kommer av en ettlinjes historikkregel.
- smed2: under gulvet på både test og val. Modellen er laget for Vanguard-trekk (direktør, aksjonærforslag), som ikke finnes her.
- smed3: kalibreringen på train 2024+2025 slår av `presedens_pay`, så på test blir alt FOR. På val (der train bare er 2024) står regelen på og gir 0,362. Regelen er riktig, men kalibreringsterskelen er ustabil. Det må fikses i #1959.
- Med 129 positive er v3 langt mer robust enn v2 (22 positive). Én sak flytter F1 med ca. 0,005.
- v2 (Vanguard, sha 52292737df) står fortsatt som sekundærmåler for typer NBIM ikke rapporterer (styrevalg, aksjonærforslag).
- Neste vinkel for smedene: historikk gir ~0,38. Signalet utover det må komme fra lønnsfakta (fjorårets say-on-pay-støtte, DEF 14A, smed3 sin fakta.py) og NBIMs egne begrunnelser (11 PX14A6G).
