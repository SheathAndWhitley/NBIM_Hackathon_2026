# Case 1: blir agenten dårligere utover 2026? F1 på MOT per kvartal (smed2 #2369)
**Til JURY:** Vi ser ingen jevn forverring gjennom 2026 (K1 0,53, K2 0,52), men K3 er svak i begge år (2025: 0,14, 2026: 0,21), så agenten er svakest på møter utenom sesongen, og der er n så lite at vi ikke kan skille drift fra støy.

Frossen #2044 (`arbeid/oppgave_2103/full_{val,test}.csv`), huskeregel A (`arbeid/oppgave_2350/ki_A_*.csv`), MOT-regel som v3 `--score mot`. KI: klyngebootstrap per selskap, 2000 trekk, seed 0, bare når antall MOT ≥ 15. Data slutter i 2026 K3.
| Kvartal | n saker | MOT | Frossen F1 [95 % KI] | P / R | Huskeregel A F1 [KI] | P / R |
|---|---|---|---|---|---|---|
| 2025 K1 | 308 | 19 | 0,42 [0,16; 0,74] | 0,50 / 0,37 | 0,16 [0,07; 0,26] | 0,10 / 0,37 |
| 2025 K2 | 1257 | 54 | 0,65 [0,52; 0,77] | 0,70 / 0,61 | 0,29 [0,20; 0,41] | 0,20 / 0,54 |
| 2025 K3 | 235 | 20 | **0,14** [0,00; 0,29] | 0,22 / 0,10 | 0,23 [0,10; 0,38] | 0,17 / 0,35 |
| 2025 K4 | 109 | 6 | 0,60 (n for lite) | 0,75 / 0,50 | 0,44 (n for lite) | 0,67 / 0,33 |
| 2026 K1 | 270 | 8 | 0,53 (n for lite) | 0,45 / 0,62 | 0,26 (n for lite) | 0,16 / 0,75 |
| 2026 K2 | 1103 | 43 | 0,52 [0,37; 0,65] | 0,51 / 0,53 | 0,24 [0,14; 0,35] | 0,15 / 0,58 |
| 2026 K3 | 166 | 7 | **0,21** (n for lite) | 0,17 / 0,29 | 0,26 (n for lite) | 0,16 / 0,71 |
| hele 2025 / 2026 | 1909 / 1539 | 99 / 58 | 0,520 / 0,476 | | 0,254 / 0,243 | |

- Hovedsesongen (K2, 72 % av sakene og 74 % av MOT i 2026) bærer tallet. Fra K2 2025 til K2 2026 faller F1 fra 0,65 til 0,52. KI-ene overlapper, men det faller i samme retning som praksisskiftet. Vi kaller det et mulig fall, ikke et bevist.
- K3 i begge år: agenten bommer på de fleste MOT (recall 0,10 og 0,29), og der slår huskeregel A den i punktverdi. Det ser ut som sesong (få, uvanlige møter) heller enn drift gjennom 2026. Brukeren bør vite at agenten er svakest utenom sesongen.
- Ingen ny modell. Kjøring: `python3 -I arbeid/oppgave_2369/kvartal.py` (bare stdlib, noen sekunder). Utskrift: `arbeid/oppgave_2369/ut.txt`.
