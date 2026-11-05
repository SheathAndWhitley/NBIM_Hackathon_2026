# Speider #2399: disk ryddet og recall ved fast budsjett til menneske (Case 1)

## Disk (ordre #252)
Slettet bare egne rådata i arbeid/speider: hack_data/fsds (12 SEC-zipper, 1,2 GB, kan lastes ned på nytt),
ovelse_c/raw/pkg og solutions.zip (1,9 GB, gammel øvelse) og gbmtest/.venv (0,4 GB). Ingen kode utenfor
arbeid/speider viser til disse stiene (sjekket med grep). Case 1-filene i hack_data står urørt.
arbeid/speider gikk fra 4,9 til 1,2 GB, og disken fra 0,4 til 7,5 GB ledig (andre ryddet samtidig).

## Recall ved budsjett (#1939 ba om dette tallet, det manglet)
Prediksjoner: arbeid/oppgave_2044/pred_miks_h2.csv, test 2026, N=1539, 66 MOT (4,3 %).
Kode: arbeid/oppgave_2399/recall_k.py, tall: recall_k.txt. Tavla: forsøk #1179.

| k til menneske | MOT funnet | recall | presisjon | tilfeldig recall |
|---|---|---|---|---|
| 25 | 21 | 0,32 | 0,84 | 0,02 |
| 50 | 30 | 0,45 | 0,60 | 0,03 |
| 71 (levert terskel) | 33 | 0,50 | 0,46 | 0,05 |
| 100 | 39 | 0,59 | 0,39 | 0,06 |
| 150 | 42 | 0,64 | 0,28 | 0,10 |
| 300 | 48 | 0,73 | 0,16 | 0,19 |

«Følg styret» flagger ingenting og har recall 0 ved alle budsjetter.
Det ærlige forbeholdet: F1 0,517 ved k=50 er valgt i etterkant på test. Det er ikke et nytt hovedtall.
Hovedtallet står som før (0,476 for levert, 0,482 for denne fila). <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->

## Forslag til JURY.md / demo (#1975)
Én linje for beslutningsstøtte: «Leser analytikeren de 25 øverste av 1539 saker, er 21 av dem MOT
(84 %). Det fanger en tredjedel av alle MOT-stemmene. Tilfeldig utvalg ville funnet 1.»
Bør måles på nytt på den frosne kjor_agent-utgangen etter kl. 16 før det siteres.
