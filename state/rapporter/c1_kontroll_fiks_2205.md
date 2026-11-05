# Case 1: kontroll av at robusthetsfiksen (#2205) ikke endret prediksjonene (dommer #2211)

**Dom: GODKJENT.** Prediksjonene er uendret. Fiksen påvirker bare rare inndata.

Kjørt 05.11 kl. 13.24 fra landsbymappen.

| sjekk | kommando | resultat |
|---|---|---|
| kald kopi, test 2026 | `sh arbeid/hack/levering/fremmed.sh /tmp/kontroll_2211` | rc 0, 34 s. HOVEDTALL F1 MOT **0.476190** (TP 30 FP 38 FN 28, P 0,4412 R 0,5172), 188/1578 til menneske |
| sha256 prediksjonsfila | `shasum -a 256 /tmp/kontroll_2211/ut/pred_maaler.csv` | **b113b545…3653**, lik den frosne. `cmp` mot `kjor_agent_real_pred_maaler.csv`: byte-lik |
| endringen | `diff /tmp/c1_real_for_2205.py arbeid/hack/levering/c1_real.py` | 3 linjer: ny `GYLDIG` og `anbefaling = TIL MENNESKE` når styrets verdi ikke er FOR/MOT/AVSTÅ. Ingen modell- eller terskelkode er rørt |
| frysvakt | `c1_frys.py sjekk` (ekte frys) og test-frys `C1_FRYS=/tmp/frys_2211.json` + `sjekk` | ekte frys finnes ikke ennå (rc 0, som ventet). Test-frys: «FRYSVAKT GRØNN: 9 filer», **0 avvik** |
| tallvakt | `python3 -I arbeid/verktoy/c1_tallvakt.py` (og inne i fremmed.sh) | 14 filer, 144 påstander, **0 avvik**, OK |

Mtime på de 8 andre frosne filene er 11.42–12.49, altså før #2205. Bare `c1_real.py` (13.21) er endret. Den kommer med i den ekte frysen kl. 16 slik den er nå.

**Merk om tallet 0,4818 i smed3s rapport:** det er v2-målerens «avvik»-F1 (TP 33 FP 38 FN 33 over 66 avvik, der avstå er med). Hovedtallet er v3 `--score mot` = 0,476. Begge tall er de samme som før fiksen. Det er ingen motsigelse, men rapporten #2205 sier feilaktig at 0,476 «ikke er gjenskapt». Det er gjenskapt her.

**Ikke testet her:** fremmed.sh kopierer ikke `pred_miks_h2.csv`, `full_test.csv` og `kjor_agent_real_maskin_alene.csv`. Derfor gir `sjekk --rot <kald kopi>` «MANGLER» på dem. Det er ventet: frysvakta sjekker kilden før kopiering.
