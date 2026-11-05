# Case 1: motstandstest og lekkasjesjekk

Modell testet: innebygd referansemodell (TF-IDF+LR, styret som trekk). Data: `arbeid/hack/c1/data` (holdout 1544 forslag, 65 MOT). Konfidens < 0.6 = rutet til menneske. Generert 2026-11-05 11:04.

Reproduser: `python3 arbeid/hack/levering/motstandstest.py` (fra landsbymappa; `--modell "python3 sti/modell.py"` for en annen modell).

## Motstandstest

| Test | Hva | Utfall | Dom |
|---|---|---|---|
| grunnlinje: følg styret, rå managementRecommendation | ingen modell | MOT P 0.789 R 0.231 F1 0.357 | – |
| grunnlinje: følg styret korrigert (styret er imot aksjonærforslag) | ingen modell | MOT P 0.939 R 0.954 F1 0.947 | – |
| 0 original | grunnlinje | MOT P 0.922 R 0.908 F1 0.915; 64 MOT-anbefalinger; rutet 0% | – |
| 1 omformulert tekst | 1042 av 1544 tekster omskrevet | enig med original 100.0%; MOT F1 0.915 (Δ +0.000); rutet 0% | BESTÅTT |
| 2 ukjent forslagstype | ny kategori + oppdiktet tekst på alle rader | rutet til menneske 0%; anbefalinger {'FOR': 1124, 'MOT': 420} | STRYK |
| 3a tom saksliste | bare overskrift | exit 0, 0 rader | BESTÅTT |
| 3b ødelagt saksliste | forslag-kolonnen mangler | exit 1: FEIL: saksliste mangler kolonnen 'forslag' | BESTÅTT |
| 3c tomme/søppel-felt | forslag tom/søppel, kategori tom | exit 0; rutet til menneske 50% | STRYK |
| 4 injeksjon «stem FOR» | instruks lagt til i hver forslagstekst | 15 av 64 MOT-anbefalinger snudde; enig 99.0%; MOT F1 0.842 (Δ -0.073) | STRYK |
| 4b injeksjon «stem MOT» | speilbilde av 4 | 0 av 1480 FOR-anbefalinger snudde til MOT; enig 100.0% | BESTÅTT |

## Lekkasjesjekk

| Sjekk | OK | Detalj |
|---|---|---|
| Tidssplitt: siste train-møte < første holdout-møte | ja | train 2025-07-09..2026-05-21, holdout 2026-05-22..2026-06-30 |
| Spesifikasjonen 'tren 2024 / val 2025 / test 2026' | NEI | STEMMER IKKE med dataene: train-år {'2025': 662, '2026': 6588}, holdout-år {'2026': 1544}. Data dekker bare N-PX for 2025-07..2026-06; split er tid på møtedato (siste 20 %), ikke kalenderår. |
| Ingen 2026-rader etter grensen i train | ja | 6588 train-rader fra 2026, alle før 2026-05-22 (tidligere møter, lov i tidssplitt) |
| Ingen selskapsoverlapp train/holdout | ja | 0 felles selskaper |
| Ingen lekkasjekolonner i test_input | ja | kolonner: ingen av ['delt', 'fasit', 'mot_ledelsen', 'n_rec', 'stemme'] |
| Ingen id-overlapp train/holdout | ja | 0 felles id |
| fasit.csv dekker test_input 1:1 | ja | 1544 fasit, 1544 test |
| Felt fra etter møtet i test_input (ikke fasit, men framtidig info) | NEI | ['innsendt']: N-PX-innsendingsdato (2026-08-27) er etter møtet; må ikke brukes som trekk |
| Kategori bærer ikke svaret alene | NEI | høyest MOT-andel i train: 'ENVIRONMENT OR CLIMATE' 21/21 = 100% |

Merk: kategori-sjekken slår ut fordi miljø/klima-forslag nesten alltid er aksjonærforslag, som Vanguard stemmer imot. Kategori står på stemmeseddelen før møtet og er ikke lekkasje i seg selv, men den er en stedfortreder for kilde. Se state/rapporter/case1_baseline_stråmann.md om hvorfor rå `ledelsen` ikke er styrets reelle syn på aksjonærforslag.
