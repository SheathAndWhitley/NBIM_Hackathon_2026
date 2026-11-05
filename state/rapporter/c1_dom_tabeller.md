# Case 1: dom over tabellene om menneskets arbeid (#2377) og bortvalgte forsøk (#2378)

Dommer, 05.11 kl. 15:12. Hver rad under er kjørt på nytt av meg fra fila i kildekolonnen, med måleren som står oppgitt. Frossen fil: `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv`, v3 `--score mot` gir 0,476190 (TP 30 FP 38 FN 28) som før.

## Tabell 2: bortvalgte forsøk (`c1_valgt_bort.md`, speider) — GODKJENT

| Rad i tabellen | Påstand | Kjørt på nytt | Stemmer |
|---|---|---|---|
| t4e +NPX (#1033) | v2 avvik test 0,529, val 0,468 | `maaler_offisiell_v2.py arbeid/oppgave_2023/m_real_t4e.csv test --data real` = 0,529412; tavle #1033 (9d81a418dd) 0,529412, vinkel «val 0,468» | ja |
| Uten sakstype (#1109) | v3 mot test 0,500 | `maaler_offisiell_v3.py arbeid/oppgave_2103/utentype_test.csv test --data real --score mot` = 0,500000 (TP 29 FP 29 FN 29) | ja |
| India-regelen (#1164/#1165) | val 2025 0,562 (0,520), 2024 0,544 (0,536) | v3 val på `arbeid/oppgave_2303/val_india_2025.csv` = 0,561798; `maal_aar.py val_india_2024.csv 2024` = 0,544444; `val_av_2024.csv` = 0,536313 | ja |
| Nyeste historikk A+B (#2363) | v3 mot test 0,500, FP 35 | v3 mot på `arbeid/oppgave_2363/svar_test_AB.csv` = 0,500000 (TP 31 FP 35 FN 27) | ja |
| Ablasjon full / h1 (v2) | val 0,522 / test 0,386 | v2 val `oppgave_2089/full_val.csv` = 0,521739; v2 test `hist1_test.csv` = 0,385965; tavle #1094–#1103 stemmer rad for rad | ja |
| Huskeregel A | v3 mot test 0,243 | v3 mot på `arbeid/oppgave_2350/regel_A_test.csv` = 0,243243 | ja |

Avvik: ingen. To merknader, ikke feil:
- #1033-fila gir **0,5366** (TP 33 FP 32 FN 25) på v3 `--score mot`. Tabellen oppgir ærlig at raden bare er v2-målt; den som limer inn i ERLIG_EVALUERING.md kan legge til v3-tallet, for juryen vil spørre. Konklusjonen (valgt bort på val) endres ikke.
- I raden nyeste historikk står frossen val 2025 som 0,522, i India-raden 0,520. Begge er riktige: 0,520 er frossen fil, 0,522 er variant 0 trent på nytt i #2363 (`c1_beslutning_nyeste_historikk.md` pkt. 3). Bør få en fotnote ved innliming.

## Tabell 1: menneskets arbeid (`c1_mennesket_arbeid.md`, smed2) — GODKJENT

| Rad i tabellen | Påstand | Kjørt på nytt | Stemmer |
|---|---|---|---|
| standard [0,15; 0,85) | 183 av 1539 (11,9), MOT 9 / 32 / 17, falske 0 / 38, F1 0,476, øvre 0,828, gulv 0,269 | Egen utregning på `arbeid/oppgave_2241/agent_med_vakt.csv` (frossen agent, tidligere dømt #2263) med `menneske_tabell.py`: 183 (11,9 %), 32 av 58, øvre TP 41 FP 0 FN 17 = 0,828, gulv 0,269; auto MOT TP = 41 − 32 = 9, auto FOR FN 17 | ja |
| smalt [0,25; 0,75) | 120 av 1539 (7,8), 12 / 23 / 23, 5 / 33, 0,714, 0,320 | Kjørt fra kald kopi i egen mappe: `sh arbeid/hack/levering/fremmed.sh /tmp/d2379_smal --baand 0.25,0.75`, så `arbeidsmengde.py` og `menneske_tabell.py` på `/tmp/d2379_smal/ut`: 120 (7,8), 12 / 23 (18 flagget) / 23, 5 / 33, 0,714, 0,320 | ja |
| maskin alene i alle rader | 0,476190 (30/38/28), `_pred_uten_ruting.csv` byte-lik frossen | v3 mot på min `_pred_uten_ruting.csv` = 0,476190; `cmp` mot `levering/kjor_agent_real_maskin_alene.csv` = byte-lik | ja |

Avvik: ingen. Merknader:
- Tallvakta i `fremmed.sh` går RØD ved ikke-standard bånd (README sier 11,9 %, kjøringen 7,8 %). Det er ventet og riktig: pakka beskriver standardbåndet. Ingen fil i pakka er endret.
- Ingen av radene velger båndet på nytt. Standard er låst på val 2025 (#2128), og tabellen sier selv at de to siste kolonnene er grenser, ikke resultater. Det er riktig lest.

## Dom
- `c1_valgt_bort.md`: **GODKJENT**. 6 rader kjørt på nytt, alle stemmer. Legg til v3-tallet 0,537 for #1033 ved innliming i ERLIG_EVALUERING.md (#1975).
- `c1_mennesket_arbeid.md`: **GODKJENT**. 2 av 4 rader kjørt på nytt (standard og smalt), begge stemmer, maskin alene byte-lik frossen fil.
Begge kan brukes i jurysvar og ERLIG_EVALUERING.md etter frysen kl. 16. Midlertidig mappe `/tmp/d2379_smal` er slettet.
