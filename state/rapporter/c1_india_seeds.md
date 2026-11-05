# Case 1 #2320: holder India-gevinsten med andre seed? Ja, men seed kan ikke teste den

Kopi av #2303 (= frossen #2044 + `--india`) i `arbeid/oppgave_2320/`, eneste tillegg `--seed` (LGBM random_state)
og `--val-ut-av` (AV-fil fra samme modell og samme grense som PÅ). Trent <2024, grense valgt på 2024 som i #2303.
Måler v3 `--score mot` via `maal_aar.py` (v3 importert uendret). Standard-seed gir nøyaktig #2303-tallene
(AV 0,536313, PÅ 0,544444), så kopien er tro. Levert mappe er ikke rørt. Test 2026 er ikke kjørt.
Kjør: `bash arbeid/oppgave_2320/kjor.sh` (7 s), tall i `tabell.txt`.

| år | seed | AV | PÅ | endring | saker snudd |
|---|---|---|---|---|---|
| 2024 (holdt ut) | std | 0,5363 | 0,5444 | +0,0081 | 1 |
| 2024 | 1 | 0,5263 | 0,5359 | +0,0096 | 1 |
| 2024 | 2 | 0,5285 | 0,5361 | +0,0076 | 1 |
| 2024 | 3 | 0,5175 | 0,5278 | +0,0103 | 1 |
| 2024 | 4 | 0,5475 | 0,5556 | +0,0081 | 1 |
| 2024 | 5 | 0,5181 | 0,5258 | +0,0076 | 1 |
| 2025 (regel funnet her) | std | 0,5202 | 0,5618 | +0,0416 | 5 |
| 2025 | 1 | 0,5238 | 0,5665 | +0,0427 | 5 |
| 2025 | 2 | 0,5114 | 0,5525 | +0,0411 | 5 |
| 2025 | 3 | 0,5143 | 0,5556 | +0,0413 | 5 |
| 2025 | 4 | 0,5119 | 0,5549 | +0,0430 | 5 |
| 2025 | 5 | 0,5172 | 0,5587 | +0,0414 | 5 |

Seed 1-5: 2024 endring snitt +0,0086 (min +0,0076), AV-spenn mellom seed 0,030 (sd 0,012).
2025 endring snitt +0,0419, alle 5 snudde saker er riktige (TP 45 -> 50, FP uendret).

**Ærlig:** Gevinsten er positiv for alle 5 seed begge år, men det sier lite. Regelen er deterministisk og
snur de samme sakene uansett seed (1 i 2024, 5 i 2025), saker modellen aldri fanger selv. Seed endrer bare
nevneren, ikke om regelen treffer. 2024-beviset er fortsatt én enkelt sak (+1 TP), og seed-støyen i
grunnmodellen (spenn 0,030) er omtrent 3-4 ganger så stor som India-gevinsten på 2024. Seed-testen avviser
altså ikke regelen, men styrker heller ikke 2024-beviset. Avgjørelsen hviler på den parede testen (#2311) og dommeren.
