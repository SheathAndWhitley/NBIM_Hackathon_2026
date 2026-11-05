# Case 1: hvor agenten bommer på MOT, én tabell (#2576, til ERLIG_EVALUERING)

Frossen agent (#2044) på tre rullende testår 2024+2025+2026 samlet. Det er bare tall som ble målt i #2569
(`arbeid/oppgave_2569/rader.csv`), telt med `python3 -I arbeid/oppgave_2576/tabell.py`.
«MOT» = sanne stemmer mot styret. «Fant» = de av dem agenten flagget (TP). «Falske» = flagg der NBIM stemte FOR (FP).
Radene overlapper (en sak kan høre til flere typer). Tallene i parentes er 2024/2025/2026.

| Type sak | MOT | Fant | Falske | Eksempel |
|---|---|---|---|---|
| **Alle saker** | 245 (88/99/58) | 105 (30/45/30) | 83 (14/31/38) | – |
| NBIM har stemt MOT på samme tekst i selskapet før | 125 (47/47/31) | **93** (26/41/26) | 58 (12/24/22) | Arbonia AG: 4 av 5 funnet i 2024, 4 av 4 i 2025 |
| Ny MOT (første gang på denne teksten) | 120 (41/52/27) | **12** (4/4/4) | 25 (2/7/16) | Fluence Energy 2025: 8 MOT, ingen funnet |
| – av dem styrevalg | 75 (25/36/14) | 8 (3/2/3) | 18 (2/5/11) | Nickel Industries 2024 (4), GFL Environmental 2025 (4) |
| Møte med minst 2 sanne MOT | 120 (43/52/25) | 44 (13/17/14) | 11 (1/4/6) | Lepu Medical 2024: 6 av 7 bommet, alle i samme møte |
| – av dem i fremvoksende markeder (EM) | 51 (22/16/13) | 18 (4/5/9) | 3 (0/1/2) | LOTTE Chemical 2024 (3), Telecom Egypt 2024 (3) |
| Say-on-pay (lønnsavstemning) | 27 (12/12/3) | 12 (1/8/3) | 13 (1/4/8) | Bommer på «Advisory Vote … Named Executive Officers» (6 ganger). Colruyt 2026 gir 2 falske |
| Revisor | 15 (2/6/7) | 7 (2/2/3) | 0 | S.F. Holding: PwC Zhong Tian, bommet i både 2025 og 2026 |
| «Other business» (fullmakt til ukjente saker) | 17 (5/6/6) | **17** | 0 | Mobimo, Arbonia: alle 17 i testårene var MOT, og agenten tok alle |

**Les slik:** agenten finner MOT når NBIM har sagt MOT til samme sak før (93 av 125). Nye MOT finner den nesten
aldri (12 av 120). Falske flagg kommer mest fra gamle MOT-er som NBIM har sluttet med (58 av 83), og de
øker fra år til år (12/24/22). Det er dette mennesket i løkka må se på: en ny sak uten historikk
ser «trygg» ut for agenten selv om den ikke er det.

Kandidattrekket fra #2569 («siste stemme på samme tekst var FOR → ikke MOT») går rett på den
falske-raden. Det er målt bare som kandidat etter frysen. Byttedommen kl. 18 (#2570) avgjør om det tas med,
og tabellen over gjelder den frosne agenten.
