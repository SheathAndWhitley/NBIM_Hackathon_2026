# Case 1: hvor sikkert er hovedtallet? Bootstrap med 5 frø (smed2 #2001)

**Svar: lederen får F1 0,474 [0,409, 0,536] på test 2026, og regelen "MOT hvis NBIM stemte MOT før" får 0,383 [0,309, 0,458]. Intervallene overlapper litt (0,409–0,458). Forskjellen er likevel sikker: +0,090 [+0,037, +0,145], og den er under null i 0 av 1000 trekk.**

## Metode
- Leder: `train_v3.py --lekkasjefri` (variant b), med grensen valgt på val 2025 og trent på 2024+2025, så kjørt én gang på test 2026. Ingen grense er valgt på test.
- 5 frø: nytt flagg `--seed-start` (standard 0, gir byte-lik `oppgave_1993/b_test_g.csv`). Hvert frøsett (0, 100, 200, 300, 400 × 5 LGBM-modeller) velger sin egen grense på val.
- Bootstrap: 1000 trekk med selskap (cusip) som klynge. 1246 saker, 129 MOT og 1225 selskap. Regelen og modellen måles på de samme trekkene, så forskjellen er parret.

## Tall (test 2026, F1 på MOT)
| Frøsett | Val-grense | Punkt | Bootstrap 95 % | Leder − regel |
|---|---|---|---|---|
| 0 (= hovedtallet) | 0,1833 | **0,474** | [0,409, 0,536] | +0,090 [+0,037, +0,145] |
| 100 | 0,2040 | 0,491 | [0,421, 0,554] | +0,107 [+0,052, +0,165] |
| 200 | 0,1909 | 0,473 | [0,401, 0,540] | +0,092 [+0,037, +0,145] |
| 300 | 0,1845 | 0,470 | [0,406, 0,531] | +0,087 [+0,029, +0,148] |
| 400 | 0,1938 | 0,485 | [0,416, 0,550] | +0,102 [+0,045, +0,163] |
| snitt av 5, felles trekk | – | 0,479 | [0,410, 0,543] | +0,095 [+0,045, +0,153] |
| regel (NBIM MOT før) | – | 0,383 | [0,308, 0,454] | – |

## Hva det betyr
- Frøet flytter test-F1 med 0,469–0,491 (spenn 0,02). Det er mye mindre enn utvalgsstøyen (intervallbredde ca. 0,13). Hovedtallet 0,474 med frø 0 ligger i den nedre delen av frøspennet, så det er ikke et heldig frø.
- De to intervallene overlapper. Det er likevel ikke den riktige testen, fordi begge måles på de samme sakene. Den parrede forskjellen har nedre grense +0,03 til +0,05 for alle 5 frø. Modellen slår regelen.
- Målet 0,5 ligger inne i intervallet, men punktet er under. Vi kan ikke påstå at modellen er over 0,5.
- Samsvarer med dommer #1993 (2000 trekk, ett frø): 0,474 [0,404, 0,538], og forskjellen +0,090 [+0,034, +0,147].

## Til juryen (forslag)
"F1 0,47 (95 % [0,41, 0,54]) mot regelens 0,38 [0,31, 0,45]. Gevinsten er +0,09 [+0,04, +0,15] målt parret. Fem modellfrø gir 0,47–0,49."

Filer: `arbeid/oppgave_2001/` (`boot2001.py`, `boot2001.txt`, `pred_s*.csv`, `train_v3_for_2001.py` = versjonen før flagget). Kommando: `cd arbeid/kandidater/smed2_c1_mot && uv run python train_v3.py --lekkasjefri --seed-start 100 --ut x.csv`, deretter `python3 -I arbeid/oppgave_2001/boot2001.py`.
