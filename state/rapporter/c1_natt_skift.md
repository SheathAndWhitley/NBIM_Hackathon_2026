# Case 1 natt (#2881): regimeskifte-regel mot feilgruppe 2 (VW ansvarsfrihet, FP), dom STÅR

**Gruppa:** feilgruppe 2 i c1_feilanalyse_natt.md, den største som gjenstår etter #2871. Volkswagen DISCHARGE 2022-23 står for 61 FP (33,5 % av FP). NBIM gikk fra MOT til FOR, men modellen henger igjen på de gamle årene.
**Regel** (`arbeid/oppgave_2881/svar/REGEL.md`, skrevet før svarfilene): fjern et MOT-flagg når siste tidligere år for (selskap, forslagstype) hadde MOT-andel ≤ 0,30 over ≥ 5 saker, og andelen har falt ≥ 0,30 fra snittet over årene før. Bare år før radens år brukes. K, R og D er valgt på val-filene (platå, intet val-år under frossen).

| år | frossen | skift | diff | av + skift (#2881b) | diff |
|---|---|---|---|---|---|
| 2023 (vakt*) | 0,3535 | 0,4277 | +0,0741 | 0,4371 | +0,0836 |
| 2024 | 0,5057 | 0,5057 | +0,0000 | 0,5269 | +0,0212 |
| 2025 | 0,5309 | 0,5375 | +0,0066 | 0,5443 | +0,0134 |
| 2026 | 0,5120 | 0,5203 | +0,0083 | 0,5333 | +0,0213 |
| snitt 2024-26 | 0,5162 | 0,5212 | **+0,0050** | 0,5349 | **+0,0187** |

*2023-fila (repo4_2024_val) var med da parametrene ble valgt. +0,07 der er derfor ikke et ærlig tall, bare et tegn på at regelen treffer VW.
Begge er **STÅR** etter natt-måleren. Tavla: #1245 (skift alene) og #1247 (av + skift). DOM.md ligger i `svar/` og `svar_av/`.

**Hvorfor den virker lite på test:** regelen slår til der et selskap har skiftet kurs fra ett år til det neste. I praksis er det VW 2023, og der rydder den 39 flagg. I 2024-26 har modellen alt lært skiftet (0 flagg fjernet i 2024, 2 i 2025 og 2 i 2026), men de få den fjerner er riktige. Regelen gjør aldri et år dårligere. Oppå «av» (#2701) legger den seg nesten rent til, fordi de to fjerner ulike flagg: +0,0135 blir +0,0187, like under kravet på +0,02.
**Ingen videre tuning på test:** jeg prøvde én variant oppå «av» med uendrede parametre. Flere varianter nå ville vært å velge på testårene.
**Neste forslag:** kandidat «av + skift + avstå-regel» (gruppe 5, +0,012 på val, koster 0 TP), med REGEL.md skrevet før måling. Den kan nå +0,02 ærlig, men det må dommeren bekrefte.
**Gjenskap:** `cd arbeid/oppgave_2881 && python3 -I skift.py` (val-søk), `python3 -I lag.py` / `python3 -I lag_av.py`, deretter `bash ../c1_natt/mal_kandidat.sh svar` / `svar_av`.
