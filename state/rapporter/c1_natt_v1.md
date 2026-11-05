# Case 1 natt, vinkel 1 (GVG-seksjon i MOT-historikken): STÅR, to forsøk (smed, #2869)

Vinkelen kom fra arkitekten (c1_natt_vinkler.md). Kode i `arbeid/c1_natt/v1/` og `arbeid/c1_natt/v1b/`. Begge er kopier av frossen `oppgave_2567/abl_rull.py`, og frosne filer er ikke rørt. REGEL.md ble skrevet før hver måling, og måleren sjekker det med mtime. Dommen kommer fra `mal_kandidat.sh` og gjelder F1 MOT mot frossen repo4. Grensen og C er valgt på val-året.

| år | frossen | v1 (6 kol) | v1b (+30 kryss) |
|---|---|---|---|
| 2023 (vakt) | 0,3535 | 0,3434 (−0,010) | 0,4218 (+0,068) |
| 2024 | 0,5057 | 0,4973 (−0,008) | 0,4247 (−0,081) |
| 2025 | 0,5309 | 0,5244 (−0,007) | 0,5190 (−0,012) |
| 2026 | 0,5120 | 0,5487 (+0,037) | 0,4925 (−0,020) |
| snitt 24-26 | 0,5162 | **0,5235 (+0,007)** | 0,4787 (−0,038) |
| dom | | STÅR (krav +0,02) | STÅR |

Tavla: forsøk #1242 (v1) og #1244 (v1b).

- **v1:** 6 kolonner, log1p av antall tidligere MOT i selskapet per GVG-hovedseksjon. De er løpende med merge_asof og allow_exact_matches=False, med samme etikettgrense som hist_feats. Gevinsten kommer bare i 2026. To av tre år og vakt-året går litt ned, så +0,007 ligger innenfor støyen (KI ±0,04).
- **v1b:** v1 pluss seksjon × radens sakstype. Den skulle fange koblingen på tvers, for eksempel at GVG 3 løfter say-on-pay. Den overtilpasser: val-F1 går opp (2023-val 0,433 mot 0,371), mens test faller kraftig. Krysscellene er for små, n≈50–300 per celle over fem år.
- **Lekkasje:** `sjekk_lekkasje.py kode` flagger v1_rull.py:70 (rationale_section). Feltet leses bare gjennom `yy`, som er maskert til etiketter fra møter strengt før radens dato. Radens egen seksjon brukes aldri. Dommeren bør likevel lese linja.
- **Tolkning:** «forrige MOT-seksjon» bærer signal i rå rater (arkitektens tabell). Men modellen fanger mesteparten allerede gjennom hist_type_dev_rate og prev_same_item. Det som er igjen er for tynt til +0,02.
- **Neste:** ikke flere varianter av vinkel 1. v1 kan eventuelt være et ledd hvis vinkel 2 (SVD-tekst i LGBM) blir målt positiv og man vil stable. Det er ny regel og ny måling, og forventet gevinst er liten.
