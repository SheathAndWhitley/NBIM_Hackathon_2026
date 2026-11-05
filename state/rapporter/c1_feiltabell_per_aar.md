# Case 1: feiltabell per testår for den leverte modellen repo4 (F1 0,512), #2718

Ingen ny trening. Kilde: rullende kjøringer i `arbeid/oppgave_2567/benk.txt` (måler v3, MOT mot styret); 2026 er den leverte kjøringen (`oppgave_2490/repo4_test.csv`, kald kjøring #2592). Val = året før, trening = årene før det.

| testår | MOT i fasit | flagget MOT | riktige (TP) | falske (FP) | oversett (FN) | presisjon | recall | F1 | til menneske |
|---|---|---|---|---|---|---|---|---|---|
| 2024 | 88 | 86 | 44 | 42 | 44 | 0,51 | 0,50 | 0,506 | ikke målt |
| 2025 | 99 | 63 | 43 | 20 | 56 | 0,68 | 0,43 | 0,531 | ikke målt |
| 2026 (levert) | 58 | 67 | 32 | 35 | 26 | 0,48 | 0,55 | 0,512 | 161 av 1539 med fasit (10,5 %) |

- Snitt F1 0,516, spenn 0,506–0,531. Hvert år har bare 58–99 MOT-stemmer, så ett treff mer eller mindre flytter F1 med ca. 0,01; 95 % KI for 2026 er [0,40; 0,62]. Forskjellen mellom årene er innenfor støyen.
- Presisjon og recall bytter plass mellom år (2025: få flagg, høy presisjon; 2024/2026: flere flagg, lavere presisjon). Grensen er satt på val-året og treffer ikke like godt hvert år.
- «Til menneske» finnes bare for 2026: agenten med ruting (bånd [0,15; 0,85) + vakter) ble bare kjørt på teståret. For 2024/2025 finnes bare modellscorer, og vi dikter ikke opp et rutingstall.
- Følg styret gir F1 0 alle år (0 flagg).
