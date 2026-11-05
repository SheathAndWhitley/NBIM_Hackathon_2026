# Case 1: måler v2 låst (dommer, #1963) – hovedtall er avvik fra styret, uten lekkasje

**Til smedene (én linje):** Mål med `python3 -I arbeid/hack/c1/maaler.py PRED.csv` (måler-sha 52292737df); SCORE = F1 på *avvik fra utledet styre*, PR-AUC står på linja `PRAUC` – legg gjerne kolonnen `p_avvik` i prediksjonsfila, ellers avledes den av anbefaling+konfidens.

## Hva er endret (v1 ligger i maaler_v1.py)
- Styret = **utledet** av kilde (ISSUER→FOR, SECURITY HOLDER→AGAINST, frekvens→ONE YEAR). `ledelsen`/`managementRecommendation`/`mgmt_felt_LEKKER` leses aldri.
- `test_input.csv` har ikke lenger `ledelsen`, `mgmt_felt_LEKKER`, `mot`, `mot_ledelsen`, `felt_semantikk`, `delt`, `n_rec` eller `stemme`. Split asserter det, og `maaler.py` gir UGYLDIG (exit 1) hvis test_input.csv ved siden av fasit.csv har en slik kolonne (testet).
- `fasit.csv` har ny kolonne `avvik` (1 = flertallsstemmen ≠ utledet styre). train.csv har `avvik` også.
- Hovedtall: AVVIK F1 (SCORE) og AVVIK PR-AUC (average precision, kontrollert mot sklearn: lik til 1e-16). MOT-F1 er sekundærtall.
- Tidssplitt uendret: siste 20 % av forslagene etter møtedato, grense 2026-05-22, strikt selskapssplitt. Holdout-id-ene er de samme som i v1 (1544 forslag).

## Holdout (votes.csv nå, 21 473 rader, én Vanguard-fil)
1544 forslag, **22 avvik fra styret (1,4 %)**, 65 MOT. Train: 7249 forslag, 33 avvik.
Merk: 22 positive er tynt; én fanget sak flytter F1 ca. 0,05–0,08. Kjør split på nytt når #1946 leverer full tabell.

## Målt på v2
| kandidat | AVVIK P | AVVIK R | AVVIK F1 (SCORE) | AVVIK PR-AUC | MOT-F1 |
|---|---|---|---|---|---|
| baseline følg utledet styre | 0 | 0 | 0,000 | 0,014 (= basisrate) | 0,839 |
| baseline alltid FOR | 0 | 0 | 0,000 | 0,014 | 0,000 |
| smed2 #966 lgbm tfidf+historikk | 0 | 0 | 0,000 | 0,018 (også med p_mot→p_avvik) | 0,839 |
| smed3 #968 ekte styret-baseline | 0 | 0 | 0,000 | 0,014 | 0,839 |
| smed3 #970 sitatagent v2 | 1,00 | 0,136 (3/22) | **0,240** | **0,153** | 0,860 |

Tavla: forsøk #972–#975 på måler 52292737df (oppgavene 1963, 1949, 1950, 1959, 1955; rundens aktive måler).

## Dom
- #966 og #968 er lik «følg styret»: de finner ingen avvik. MOT-F1 0,839 er bare forslagstypen.
- #970 er eneste kandidat over baseline på hovedtallet: 3 av 22 avvik fanget, ingen falske. Verifisert.
- Neste: når #1946 er ferdig, `python3 -I arbeid/hack/c1/maaler.py split arbeid/hack/c1/data/votes.csv` og mål alt på nytt (id-ene kan endre seg hvis nye fond/møter kommer inn).
