# Kontroll #2195: c1_mot_sakstyper.md mot dommerens telling — GODKJENT

dommer, 05.11 13:2x. Kjørt på nytt: `python3 -I arbeid/oppgave_2182/tell_mot_typer.py` (lik `telling.txt`, diff tom) og `python3 -I arbeid/oppgave_2181/mot_sakstyper.py`.

| påstand i rapporten (test 2026) | dommerens telling | |
|---|---|---|
| 1539 saker, 58 MOT | 1539, 58 | OK |
| styrevalg 26/729 (styret) + 2/10 (aksjonær) = 28/739 | DIRECTOR_ELECTION 28 av 739 | OK |
| revisor 7/130 | AUDITOR 7/130 | OK |
| andre styresaker 6/87 | OTHER_MGMT 6/87 | OK |
| annen sak 6/6 | OTHER_BUSINESS 6/6 | OK |
| øvrige 11 (ARTICLES 3, SAY_ON_PAY 3, SHARE_ISSUANCE 2, RPT 1, EQUITY_PLAN 1, FIN_STATEMENTS 1) | samme | OK |
| Management 56 / Shareholder 2 MOT; 16 aksjonærsaker | 56/2; 10+6=16 | OK |
| agenten fant 30 (14+1 styrevalg = 15) | 58 − 28 bommer = 30, konsistent med F1 0,476 | OK |

- N-PX-tallet 302/634 står **ikke** i rapporten eller i den nye seksjonen i `BESLUTNINGSSTOTTE.md`; real_votes-tallene der er 58 MOT / 66 avvik, som stemmer.
- Merk: «66 avvik» i BESLUTNINGSSTOTTE (58 MOT + 5 AVSTÅ + 3 andre) matcher «avvik 66» i tellinga.

**Dom: GODKJENT.** Ingen avvik.
