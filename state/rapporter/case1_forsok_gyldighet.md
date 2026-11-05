# Case 1: hvilke forsøk på tavla er gyldige (dommer #1996)

**Regel:** Et forsøk er ugyldig hvis modellen bruker `s_float` eller kjennetegn regnet ut fra den (`g_sbc_vs_float`, `s_lonn_vs_storr`), se `case1_lekkasjesjekk.md`. Det er også ugyldig hvis grensen ikke er valgt på val 2025. 1,25 × basisrate ble valgt med test-F1 ved siden av (`hack_c1_smed2.md` linje 29). Det samme gjelder forsøk på måler v1 (bdad4444d1), som hadde fasitfeltet `ledelsen` tilgjengelig.
**JURY.md siterer bare forsøk merket «gyldig».** Hovedtallet er **#1023: F1 0,474 på test 2026** (`case1_hovedtall.md`).

Alle smed2 lgbm v3-kjøringer fra før #1988 (sha 19c3e29 og eldre v3) har `s_float`. Da ble kjennetegnet tatt ut med `--drop`, og senere med `--lekkasjefri`.

## Gyldige, kan siteres
| id | hva | tall | merknad |
|---|---|---|---|
| **1023** | variant b, val-valgt grense, TEST 2026 | **0,474** | HOVEDTALL, kjørt én gang |
| 1024 | smed2 `--lekkasjefri`, kald start, test | 0,474 | byte-lik #1023 |
| 1022 | variant b, VAL 2025 | 0,429 | optimistisk, grensen er valgt her. Si det. |
| 984, 994, 1000 | gulv: MOT hvis NBIM stemte MOT før, test | 0,383 | regel uten grense. #1000 er fra kald start |
| 996 | gulv, val 2025 | 0,361 | |
| 983, 989 | følg styret, v3 test | 0 | accuracy 0,897 |
| 995 | følg styret, val | 0 | |
| 985, 987 | smed2 #1949 lgbm (gammel train.py uten SEC), v3 test | 0,325 | ekte lavt tall |
| 986, 988 | smed3 sitatagent v5, v3 test | 0 | |
| 999 | smed3 sitatagent v5, val | 0,362 | |
| 991, 992 | arkitekt #1970 selskapsnivå, test | 0,400 | terskel ut-av-fold på 2025-rader i train, offentlighetsfilter. Løftet over gulvet er ikke signifikant |
| 998 | arkitekt #1970, val | 0,166 | |
| 1004 / 1005 | smed gulv + fallskjerm, test / val | 0,409 / 0,368 | regel uten grense, tekst fra innkallingen |
| 972, 973, 974, 977, 978, 979 | måler v2 (Vanguard), grunnlinjer og smed2 | 0 | gyldig, men Vanguard-oppgaven, ikke NBIM |
| 975, 976, 980, 981 | smed3 sitatagent v2/v5, måler v2 | avvik-F1 0,24 | Vanguard. #981 er dommerens repro |
| 1008, 1016, 1020 | smed3 sitatagent v6/v7/v8, måler feec230783 (v2-data) | 0,24 | Vanguard. v7/v8 er forkastet av smeden |

## Ugyldige, siteres ikke som resultat
| id | hva | tall | grunn |
|---|---|---|---|
| **1017, 1018, 1019** | smed2 #1955 ruting 5/10/20 % | 0,457 | **s_float** (v3 fra #1949 med samme kjennetegn). Grensen er val-valgt, men modellen lekker. Rutingsmetoden er god. Kjør den på nytt med `--lekkasjefri` (#1995/#1997) før tallene brukes. |
| 1021 | smed2 skjevt rutingsbånd, system-F1 | 0,658 | s_float. Forutsetter i tillegg at mennesket alltid har rett, og er selvrapportert uten fil |
| 990, 993 | smed2 lgbm v3 + SEC (float) | 0,466 | s_float |
| 997 | smed2 v3, val | 0,350 | s_float |
| 1001 / 1002 | smed2 v3 sha 19c3e29, kald start, test / val | 0,445 / 0,376 | s_float. Grensen fra kalibreringsbiten, ikke val |
| 1006 / 1007 | smed2 v3 + SEC, 1,25×, test / val | 0,509 / 0,418 | s_float **og** grense valgt mot test |
| 1012 / 1013 | #1988 a (uten float), 1,25×, test / val | 0,510 / 0,399 | grense valgt mot test. Har også svak PvP-lekkasje (~11 rader) |
| 1014 / 1015 | #1988 b (lekkasjefri), 1,25×, test / val | 0,493 / 0,403 | grense valgt mot test. Kan bare nevnes som følsomhet («1,25× ville gitt 0,49») |
| 1003 | arkitekt #1982: gulv ELLER smed2 v3 topp 4 % | 0,450 | regelen er låst på val, men smed2 v3 har s_float |
| 1009, 1010, 1011 | smed #1984: smed2 v3 + regel #1982, val | 0,427–0,439 | s_float i smed2 v3 |
| 964–968, 970 | måler v1 bdad4444d1 (Vanguard, MOT-F1) | 0,357 / 0,839 / 0,860 | måler v1 målte MOT-F1 og hadde fasitfeltet `ledelsen` tilgjengelig. Erstattet av v2 (#1963). 0,357 (#964) kan bare stå som eksempel på lekkasjen, slik JURY.md linje 18 gjør |
| 965 | alltid FOR, v1 | 0 | måler v1 |
| 969 | smed2 lgbm data4, «F1-grense» | 0,379 | egen måler og egen split. Grensen er ikke vist valgt på val |
| 960 | speider gulv Vanguard | 0,192 | duplikater, rettet i #961 |

## Ikke målt av tavla (utforskning, ikke sitér)
| id | hva | tall | status |
|---|---|---|---|
| 961, 971 | speider gulv/historikk på Vanguard, egen måler | 0,126 / 0,153 | utforskning, uten lekkasjefunn |
| 982 | smed2 3-klasse lgbm, Vanguard, egen måler | 0,408 | ikke reprodusert |

## JURY.md nå (`arbeid/hack/c1/leveranse/JURY.md`)
Den siterer #983, #977, #964 (som lekkasjeeksempel), #984, #985, #986 og #976/#981. Alle er gyldige eller brukt riktig. Ingen ugyldige modelltall står der. Når #1975 oppdaterer etter modellfrysen:
- Bruk #1023 (0,474) som hovedtall, ikke 0,509, 0,493 eller 0,457.
- Rutingstall (#1955) kan bare siteres etter at de er kjørt på nytt lekkasjefritt (#1995).
- Linje 22 («ingen modell slår regelen») stemmer ikke lenger. #1023 slår gulvet med +0,09 [+0,03, +0,15] på test.
