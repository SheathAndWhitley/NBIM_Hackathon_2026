# Case 1 (#2669): usikkerheten rundt 0,512 i én setning

**Setningen** (nå i `leveranse/JURY.md` pkt. 2 og `leveranse/ERLIG_EVALUERING.md` § 3):
> 0,512 hviler på bare 58 MOT-stemmer (TP 32, FP 35, FN 26), så 95 % KI er [0,40; 0,62], de tre testårene gir 0,506–0,531, og gevinsten over den eldre frosne 0,476 er +0,036 [−0,008; +0,085]; tallet er altså like over målet 0,5, innenfor støy.

Kilder:
- KI [0,400; 0,621]: klyngebootstrap per selskap, 2000 trekk, `kilder/oppgave_2095_ki_mot.py`, tall i `kilder/c1_repo4_tall_2592.md:3` (bootstrap over rader: [0,397; 0,616])
- år: 2024 0,506 / 2025 0,531 / 2026 0,512, `ERLIG_EVALUERING.md` § 7 benk A
- repo4 − frossen: +0,036 [−0,008; +0,085], `kilder/c1_repo4_tall_2592.md:5`

Rettet feil: JURY.md pkt. 2 hadde fortsatt KI-et til den gamle modellen, [0,36; 0,59], og sa «punktestimatet er under» målet. Begge deler gjaldt 0,476. Val-tallet der er nå repo4 sitt (0,530 [0,417; 0,638]).

KP: forventet TP32 FP35 FN26 og F1 0,5120, fikk F1 0.5120 TP 32 FP 35 FN 26 (tallvakt). Tallvakt etterpå: 31 filer, 196 påstander, 0 avvik, OK.
