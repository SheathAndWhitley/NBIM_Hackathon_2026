# Case 1: forsøk vi målte, men valgte bort, og hvorfor (#2378)

Speider, 05.11 kl. 15.20. Alle tall er hentet fra rapportene eller tavleforsøkene i kildekolonnen, ingen fra hukommelsen.
Levert agent er frossen #2044 miks h2. Valgregelen hele veien: en endring kommer bare inn hvis den vinner på **val** (2025, og fra #2297 også holdt-ut 2024). Test 2026 brukes aldri til å velge.

**To målere, ikke bland dem.** v3 `--score mot` (sha 418a937e57, 58 MOT på test 2026) er pakkas hovedtall. Eldre forsøk er målt med v2 avvik-F1 (9d81a418dd / 882009b35e, 66 avvik på test, 103 på val). Samme frosne modell gir **v3: val 0,520, test 0,476** og **v2: val 0,522, test 0,482** (`c1_huskeregel_dom.md`, `c1_ablasjon_v2.md`, `c1_injeksjonsvakt_ablasjon_dom.md`).

## Kandidater som var bedre på test, men ikke inn

| Forsøk | Måler | Val (frossen) | Test 2026 (frossen) | Hvorfor valgt bort | Kilde |
|---|---|---|---|---|---|
| t4e +samme-tekst-historikk +NPX (tavle #1033, smed2) | v2 avvik | 0,468 (0,522) | **0,529** (0,482) | Tapte på val med 0,054. Høyeste testtall vi har sett, men valg på test er ikke lov. Var en tid dashbordets hovedtall ved en feil, rettet i #2242. | `c1_datasjekk_242.md` l. 105–106, `c1_hovedtall_levert_2242.md`, `c1_juryspm.md` l. 12 |
| Uten sakstype (tavle #1109, #2103) | v3 mot | 0,509 (0,520) | **0,500** (0,476) | Full modell er best på val. 0,500 er bare sett på test, KI [0,38; 0,61]. Bekreftet fra kald kopi av dommer2 (#2107). | `c1_lekkasje_v3.md` l. 11–18, `c1_verifisert_lekkasje.md` |
| India-regelen (tavle #1164/#1165, #2307) | v3 mot | val 2025 0,562 (0,520); holdt-ut 2024 0,544 (0,536) | ikke målt mot fasit (2 saker ville snudd) | Kravet oppfylt bare på papiret: 2025 er året regelen ble funnet (p ≈ 0,06, optimistisk), 2024 er én sak (p = 1,0). De 2 snudde 2026-sakene ville fått MOT med P(MOT) 0,09 og 0,19, en motsigelse i beslutningsstøtten. Dom #2297: ikke inn. | `c1_beslutning_india.md`, `c1_india_frys_kandidat.md`, `c1_india_paret.md` |
| Nyeste historikk A+B (tavle #1174/#1175, #2363) | v3 mot | val 2025 0,543 (0,522); holdt-ut 2024 0,551 (0,510) | **0,500** (0,476), FP 35 mot 38 | Paret bootstrap dekker null begge val-år: 2025 +0,021 [−0,021; +0,067], 2024 +0,028 [−0,020; +0,075]. PR-AUC ned (0,509 mot 0,525), USA fortsatt 9 falske MOT, Kina opp fra 2 til 7. Dom #2366: ikke inn. | `c1_beslutning_nyeste_historikk.md`, `c1_nyeste_historikk.md`, `c1_lekkasje_2363.md` |
| Nyeste historikk A alene (#2363) | v3 mot | ikke valgt på val (A+B vant) | 0,512 | Å bytte til A etter å ha sett test ville vært valg på test. | `c1_beslutning_nyeste_historikk.md` pkt. 7 |

## Kandidater som ikke nådde kravet på val (test ikke kjørt)

Kravet var val F1 > 0,5217 + 0,03 = 0,552 (`c1_siste_forsok_245.md`, #2248, v2-oppsett, val n=1909, 103 MOT).

| Forsøk | Val 2025 F1 | PR-AUC | Hvorfor valgt bort | Kilde |
|---|---|---|---|---|
| + lt (glattet MOT-rate land×type) | 0,514 | 0,465 | Under base | `c1_siste_forsok_245.md` |
| + ny (ny for selskapet) | 0,5217 | 0,474 | Lik base, ingen gevinst | samme |
| + mt (møtestruktur) | 0,5213 | 0,461 | Under base | samme |
| + lt + ny + mt | 0,480 | 0,463 | Under base | samme |

## Ablasjoner: deler vi beholdt fordi de bærer modellen

Hver variant velger C og grense på val 2025, test kjørt én gang. Måler v2 avvik (`c1_ablasjon_v2.md`, #2089, tavle #1094–#1103).

| Variant | Val 2025 F1 | Test 2026 F1 | Lesning |
|---|---|---|---|
| Full (levert) | 0,522 | 0,482 | Referanse |
| Uten sakstype | 0,511 | 0,504 | Nesten overflødig, forskjell under ±1 sak; se v3-raden over |
| Historikk bare fra tidligere år (h1) | 0,448 | 0,386 | Løpende historikk gir +0,07 på val. h1 er det ærlige tallet hvis NBIMs stemmer ikke er kjent løpende |
| Uten historikk | 0,337 | 0,282 | Historikken er hoveddelen (−0,19 på val) |
| Uten LightGBM | 0,485 | 0,470 | LGBM gir +0,04 på val, mest via presisjon |
| Injeksjonsvakt av / på (#2241) | – | 0,476 (v3) begge, byte-like filer | Vakta koster ingenting, 0 falske alarmer; beholdt (`c1_injeksjonsvakt_ablasjon_dom.md`, tavle #1142/#1143) |

## Grunnlinjer (aldri kandidater, bare målestokk)

| Regel | Val 2025 F1 (v3) | Test 2026 F1 (v3) | Kilde |
|---|---|---|---|
| Huskeregel A: MOT der NBIM stemte MOT sist i samme selskap og sakstype | 0,254 | 0,243 | `c1_huskeregel_dom.md` (tavle #1172) |
| Huskeregel B: samme selskap, alle saker | 0,162 | 0,125 | samme (tavle #1173) |

## Til ERLIG_EVALUERING.md (#1975)
Vi har sett tre testtall som er høyere enn det leverte (0,529, 0,500, 0,500) og valgt bort alle, fordi ingen vant tydelig på val. Det leverte tallet 0,476 er altså ikke plukket som beste av mange på test. Forbehold: t4e (#1033) og ablasjonene er bare målt med v2-måleren, ikke v3.
