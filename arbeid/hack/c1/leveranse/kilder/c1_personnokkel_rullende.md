# Case 1: personnøkkelen (+0,049 i sak 2490) holder ikke på tidligere år (sak 2496, ikke hovedtall)

_Kopi av `state/rapporter/c1_personnokkel_rullende.md` (#2505). Koden det vises til (`arbeid/oppgave_2496/`, `arbeid/oppgave_2503/`) ligger i landsbyen, ikke i zipen; tallene er ikke hovedtall._

**Spørsmål:** Gir `prev_same_person` fra teamets parallelle hybridløsning (ikke fra NBIM) som ekstra trekk i frossen #2044-modell (miks, hist 2) gevinst også før 2026?

**Oppsett:** `arbeid/oppgave_2496/abl_rull.py` = `oppgave_2490/abl.py` med `--testaar T`. C og terskel velges på T−1
(trent på år < T−1), deretter trent på år < T og testet én gang på T. Samme kode med T=2026 gir byte-identisk
`full_test.csv` som sak 2490 (sjekket med cmp). F1 MOT er målt med en kopi av `maaler_offisiell_v3.py --score mot`
der vinduet er et årstall (`maaler_aar.py`; gir 0,476190 / 0,525424 på 2026, likt originalen). KI er parret
klyngebootstrap per selskap, 2000 trekk, seed 0 (`diff_ki_aar.py` = `oppgave_2103/diff_ki.py` med årstall som vindu).

| Testår (val-år) | Variant | F1 MOT | P | R | Person − uten, 95 % KI | Ulike pred. |
|---|---|---|---|---|---|---|
| 2024 (val 2023) | uten | 0,4545 | 0,682 | 0,341 | | |
| 2024 (val 2023) | + person | 0,4179 | 0,609 | 0,318 | **−0,037** [−0,133; +0,058] | 28 |
| 2025 (val 2024) | uten | 0,5143 | 0,592 | 0,455 | | |
| 2025 (val 2024) | + person | 0,5155 | 0,526 | 0,505 | **+0,001** [−0,042; +0,050] | 25 |
| 2026 (val 2025) | uten (= frossen) | 0,4762 | 0,441 | 0,517 | | |
| 2026 (val 2025) | + person | 0,5254 | 0,517 | 0,534 | **+0,049** [+0,016; +0,090] | 14 |

Snitt over tre år: uten 0,482, med person 0,486 (+0,005).

**Dom:** Gevinsten er ikke stabil. Den finnes bare i 2026: −0,037 i 2024 og +0,001 i 2025, begge med KI som
dekker null. I 2026 kom gevinsten fra presisjon. I 2025 bytter varianten presisjon mot recall (terskelen som ble valgt
på 2024 flagger 107 mot 84). I 2024 taper den på begge. Personnøkkelen skal derfor ikke inn som forbedring.
+0,049 på 2026 er mest sannsynlig støy, og testen var allerede sett. Frys og leveranse er urørt.

**Forbehold:** Val 2023 er svak (val-F1 ca. 0,39) og gir en støyete terskel for 2024. Treningsdata før 2023 er
mindre. Ett mulig unntak er at trekket hjelper når historikken er lang, men tre år er for lite til å vise det.

Kjør på nytt: `cd arbeid/oppgave_2496 && bash kjor.sh`, så `python3 -I arbeid/oppgave_2496/maaler_aar.py
arbeid/oppgave_2496/<variant>_<år>_test.csv y<år> --data real --score mot` og
`python3 -I arbeid/oppgave_2496/diff_ki_aar.py <full> <person> <år>`.
