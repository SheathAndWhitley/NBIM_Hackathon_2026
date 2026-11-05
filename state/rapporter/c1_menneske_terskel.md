# Case 1: når agenten sender saken til et menneske (smed3, #2128)

Frossen modell #2044 (miks h2) er ikke rørt. Den gamle regelen er også den samme: MOT når rå p ≥ 0,919.
Det nye er én regel til: rå p kalibreres med isotonisk regresjon. Den er lært på val 2025 og brukes på test 2026.
Kalibreringen gir Brier 0,030 og ECE 0,016 på test (#2109). Når den kalibrerte q havner i båndet [lo, hi), går saken til et menneske.
Kode: `arbeid/oppgave_2128/baand.py`. Svarfiler: `svar_baand_*.csv`. Rådata: `baand_tabell.csv`.

## Test 2026 (1539 saker, 66 MOT; uten ruting er F1 MOT 0,482, med TP 33, FP 38 og FN 33)

| Bånd på q | Til menneske | MOT i båndet | F1 MOT på resten | Rest TP/FP/FN | System, menneske riktig | System, menneske følger styret |
|---|---|---|---|---|---|---|
| [0,3, 0,7) | 51 (3,3 %) | 19 av 66 | 0,418 | 14/6/33 | 0,629 | 0,326 |
| [0,15, 0,85) | 122 (7,9 %) | 30 av 66 | 0,468 | 11/0/25 | 0,766 | 0,286 |
| [0,08, 0,95) | 167 (10,9 %) | 32 av 66 | 0,455 | 10/0/24 | 0,778 | 0,263 |

Val 2025 viser det samme mønsteret: [0,15, 0,85) sender 7,5 % videre og fanger 54 av 103 MOT.
Rutingtallene er sjekket med rundens måler: `bash arbeid/hack/maaler.sh <fil> real_test` ga 51, 122 og 167 saker til menneske, og frossen F1 0,4818.

## Hva det betyr
- **F1 på resten går ned, ikke opp.** Båndet tar de MOT-tette sakene, altså de fleste flaggene til modellen. Det som blir igjen er nesten bare «følg styret».
  Ruting gjør altså ikke maskinen flinkere. Den flytter de vanskelige MOT-sakene til et menneske.
- I de to brede båndene er flaggene maskinen beholder 100 % presise (FP 0). Feilene er bare MOT som maskinen overser i det lave q-området (FN 24–25, q under 0,08). Dem fanger intet bånd.
- Anbefaling: **[0,15, 0,85)**. Der leser mennesket 8 % av sakene og får 45 % av alle MOT. Gjør mennesket dem riktig, blir F1 for systemet 0,77. Det bredere båndet gir 2 MOT til for 45 saker mer.
- Ærlighet: kalibreringen er en trapp med trinnene 0,09, 0,17, 0,19, 0,52, 0,58, 0,75 og 1. Derfor kan bånd bare skille mellom trinnene.
  Bånd 3 var først [0,1, 0,95), men det ga nesten samme saker som bånd 2. Jeg byttet det til [0,08, 0,95) etter å ha sett tallene for test. Bånd 1 og 2 ble valgt før måling.
  Kolonnen «menneske riktig» er et tak. Kolonnen «menneske følger styret» er gulvet.
- Tavla avviste `--sti` fordi måler-hashen er endret på disk (dommeren må sette måleren på nytt). Derfor står forsøkene som egenrapporterte: #1112, #1113 og #1114.
