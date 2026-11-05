# Case 1: én kommando gjenskaper de tre testårstallene (#2727)

Kommando: `bash arbeid/oppgave_2727/testaar.sh` (trener frossen repo4 på nytt per testår, ca. 10 sek)
eller `bash arbeid/oppgave_2727/testaar.sh --rask` (måler bare de lagrede testfilene).
Skriptet kopierer abl_rull.py og maaler_aar.py (oppgave_2567) til en fersk tom mappe i /tmp, trener for
T = 2024/2025/2026 (C/grense valgt på T-1, trent på år < T), sjekker datavakta (sha256 71ba5135…) og måler
med `maaler_aar.py repo4_T_test.csv yT --data real --score mot`.

Resultat 18:20, begge modusene i kald kopi:
- 2024 F1 0,5057 (TP 44 FP 42 FN 44), 2025 0,5309 (TP 43 FP 20 FN 56), 2026 0,5120 (TP 32 FP 35 FN 26), snitt 0,5162.
- Likt med c1_dom_1815.md på 4 desimaler. 2026-fila er identisk (id, prediksjon) med oppgave_2490/repo4_test.csv.
- Frysvakt grønn (21 filer like som ved frys 17:18:18). Ingen frosne filer rørt.

Merk: stiene er absolutte til denne maskinen (<repo>) og bruker miljøet i arbeid/oppgave_2023.
Skriptet er ikke i jury-zipen eller GitHub-repoen ennå; skal det dit, må det kopieres med abl_rull.py og maaler_aar.py.

Linje til JURY.md (#2723):
> Testårstallene (F1 på MOT 0,5057 / 0,5309 / 0,5120, snitt 0,5162) gjenskapes med `bash arbeid/oppgave_2727/testaar.sh`: trener den frosne repo4-modellen på nytt for hvert testår 2024–2026 (valgt på året før, trent på eldre år) i en tom mappe og måler med den offisielle måleren, ca. 10 sekunder (`--rask` måler bare de lagrede svarfilene).
