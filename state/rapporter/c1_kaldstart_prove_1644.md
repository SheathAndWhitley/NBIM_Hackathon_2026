# Case 1: generalprøve av kaldstarten på 16:44-zipen (dommer #2555, 05.11 kl. 16:49–16:51)

**Grønn.** Zipen `jurypakke_c1_1644_bf0d3f8.zip` kjører fra tom mappe med tom HOME og gir F1 MOT 0.476190, likt tavla. Ingen filer i leveransen er endret.

## Kommando
```
sh arbeid/hack/levering/test_jury_zip.sh state/levering/c1_gronn/jurypakke_c1_1644_bf0d3f8.zip /tmp/jurytest_2555
```
Skriptet gjør det et jurymedlem gjør: tom mappe, `env -i` med tom HOME (ingen uv-buffer), sandbox-exec som nekter lesing i landsbymappen, `unzip`, `cd c1_stemmeagent`, `sh KJOR.sh`, så `sjekk_treffsikkerhet.sh`.

## Resultat
| Sjekk | Forventet | Målt | |
|---|---|---|---|
| SHA256 på zipen | ec8e04b8…85d4 (SHA256.txt) | ec8e04b8cfb555ab8d018454f7dc3ef87754b85c1674e90bdee7a2f983af85d4 | LIK |
| FRYSVAKT | 15 frosne filer uendret | 15 like sha256 | GRØNN |
| HOVEDTALL F1 MOT (v3 --score mot) | 0.476190 | 0.476190 (P 0.4412, R 0.5172, TP 30 FP 38 FN 28 TN 1443) | LIK |
| TALLVAKT | 169 påstander om hovedtallet | 169 stemmer, 0 avvik | GRØNN |
| Prediksjonsfil | frossen b113b545…3653 | ny fil samme sha256 | LIK |
| Tidssplitt | modell på data t.o.m. 2024, grense låst på val 2025, kjørt én gang på test 2026 (1539 med fasit, 58 MOT) | loggen: «låst på val 2025 … C 3, rå grense 0.91885», «TEST 2026 … n 1539, n_MOT 66 avvik» | stemmer med tavla (forsøk #2503: 2026 = 0.4762) |
| Loggen nevner «landsby» | nei | nei | GRØNN |

**Tid brukt:** 62 s vegg-til-vegg (uv sync 3 s fra tom buffer med nett, kjøring 52 s, sjekk 6 s). README lover 29–52 s for kjøringen; stemmer.

## Observasjoner (ingen rød, ingen endring i leveransen)
1. Utpakkinga får en tom mappe `c1_stemmeagent/home`. Den lages av KJOR.sh:17 (`mkdir -p home`) som HOME for `env -i`, så det er med vilje og ufarlig.
2. v2-målerblokken skriver fortsatt `streng MOT: TP 0 FP 0 FN 0 … F1 0.0000` før HOVEDTALL. Kjent fra prøvekaldstarten kl. 13 (#2180, pkt. 4) og forklart i README/`c1_streng_mot.md`; hovedtallet er v3-linja.
3. 16:44-zipen er bygd på bf0d3f8. Siden er tre tekstcommits lagt til (83f152c, 5442ccd, c928a62) og 16:47-zipen (`jurypakke_c1_1647_83f152c.zip`, 1e0260d3…) finnes. Den endelige pakka kl. 19:30 (#1972) blir en nyere zip med egen SHA; e-postutkastet har derfor TODO på filnavn og SHA.

## E-postutkast
`state/rapporter/epost_utkast_hackathon.md` er oppdatert til skjelett med de tallene som er frosne (holdout 2026, 1539 saker, 58 MOT, F1 0,476, P 0,44, R 0,52, kommando `sh KJOR.sh`). Filnavn og SHA256 på zipen står som TODO og fylles i #1972. Guden fyller gruppenavn og navn.
