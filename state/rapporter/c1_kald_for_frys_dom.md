# Dom: kald kjøring Case 1 før modellfrys, målt på nytt av dommer2 (#2250)

Dato 2026-11-05 13:55. Gjelder smeds runde 2 i #2243 (kaldstart 13:49, fremmed.sh 13:50, etter #2237 høflighetsvakt).
Resultat: **GRØNN, ingen avvik.** Smeds tall 0,476190 er reprodusert av dommeren med landsbyens egen måler.

## Hva jeg gjorde
- Kjørte selv `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py <fil> test --data real --score mot` på begge svarfilene
  (`_pred_uten_ruting.csv` og `pred_maaler.csv`) i begge kopiene: `/tmp/c1_kald.oChD4r` (kaldstart.sh) og `/tmp/fremmed_2243` (fremmed.sh).
- Sammenlignet sha256 på alle kildefiler i kopiene mot landsbyens filer nå (det frysvakta `c1_frys.py` låser kl. 16).
- Sammenlignet anbefaling per id mot den frosne `arbeid/oppgave_2103/full_test.csv` (hovedtallet 0,476).

## Måling (dommerens egen kjøring, måler v3 sha 418a937e57, data real_votes sha 71ba5135e7ba)
| fil | kopi | TP | FP | FN | P | R | F1 MOT mot styret |
|---|---|---|---|---|---|---|---|
| _pred_uten_ruting.csv | kaldstart | 30 | 38 | 28 | 0,4412 | 0,5172 | 0,476190 |
| pred_maaler.csv | kaldstart | 30 | 38 | 28 | 0,4412 | 0,5172 | 0,476190 |
| _pred_uten_ruting.csv | fremmed | 30 | 38 | 28 | 0,4412 | 0,5172 | 0,476190 |
| pred_maaler.csv | fremmed | 30 | 38 | 28 | 0,4412 | 0,5172 | 0,476190 |

58 MOT i fasit, 66 avvik fra styret, 1539 vurderte rader test 2026. Streng MOT (inkl. avstå-saker) F1 0,5241, ikke hovedtall.

## Sha-er (kopi = landsby, byte-likt i begge kopier)
| fil | sha256[:12] |
|---|---|
| arbeid/oppgave_2044/train.py | 772fb71500e3 |
| arbeid/oppgave_2044/pred_miks_h2.csv | 40afcc3e2fec |
| arbeid/oppgave_2103/full_test.csv | 69702192d3a4 |
| arbeid/hack/levering/kjor_agent.py | dedc94062cf4 |
| arbeid/hack/levering/c1_real.py | 83fe0eb0de22 |
| arbeid/hack/levering/injeksjon_hoflig.py (etter #2237) | 150b92e9993f |
| arbeid/hack/levering/kjor_agent_real_maskin_alene.csv | 22ac6717e128 |
| arbeid/oppgave_2047/vern.py | 19c3629fa670 |
| arbeid/oppgave_2046/case1_mot.py | d403dd3c8f3b |
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba |
| arbeid/hack/c1/data_off/real_test_input.csv | 1e0e22f86bbf |
| arbeid/hack/c1/maaler_offisiell_v3.py | 418a937e57e5 |

Utdata fra kopiene: `_pred_uten_ruting.csv` 22ac6717e128 (= maskin-alene-fila i pakka), `pred_maaler.csv` b113b545dd86 (= sha i README),
`agent.csv` f0444a47ee0f. Kaldstart- og fremmed-kopien er byte-like på begge svarfiler.
Måleren i fremmed-kopien avviker fra landsbyens bare i de to hardkodede datastiene (sed i fremmed.sh), regnestykket er likt.

## Mot den frosne modellen (#2103 full_test.csv)
1578 felles id-er, **0 ulike anbefalinger** (både med ruting og maskin alene). Fila er ikke byte-lik fordi full_test.csv mangler
kolonnen konfidens og har uavrundet p_avvik; største p_avvik-forskjell er 5e-6 (avrunding til 5 desimaler). Ingen stemmebytter.

## Frysvakta
`state/c1_frys.json` finnes ikke ennå (LaunchAgent fryser kl. 16). Sha-tabellen over er dermed øyeblikksbildet frysen skal låse.
#2247 (smed, etter kl. 16) sammenligner `c1_frys.py status` mot denne tabellen. Avvik der er rødt flagg.

## Referanse
#2248 (siste MOT-forsøk) var fortsatt bare 10 % og ikke godkjent (#2249 pågår) ved dom. Referansen er derfor uendret: 0,476190 (#2090).
Godkjennes #2248 senere, må ny kald kjøring måles på nytt mot den nye modellen før frys kl. 16.

## Dom
Smeds påstand i #2243 holder i alle ledd: F1 MOT 0,476190, sha-er like, 188 til menneske (11,9 %), 1 injeksjon. Ingen rødt flagg.
