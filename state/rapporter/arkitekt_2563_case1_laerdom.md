# Case 1: tre ting vi gjorde feil (arkitekt #2563)

Kilde: `state/tavle.db`, Case 1-oppgaver #2000–#2810 (kost, sek, tidspunkt).
F1 MOT flyttet seg én gang: 0,476 → 0,512 (byttet til repo4 #2592, 17:01–17:21).

| Mønster | Oppgaver | Kost | Agentmin | Flyttet F1/juryteksten? |
|---|---|---|---|---|
| Rette og sjekke håndskrevne tall | 115 | $110 | 435 | Nei, holdt bare tekst lik måleren |
| Modellvalg før flerårsbenk (vinneren målt 16:12, lagt i «neste versjon») | 18 av 296 oppgaver kl. 13–16 var modellarbeid | – | – | Gevinsten +0,036 kom 4 t for sent |
| STÅR-reserve (full ekstra tekstutgave) | 19 | $25 | 73 | Nei, aldri brukt (#2603) |

Til sammenligning: alt modellarbeid etter #2000 var 33 oppgaver og $20.

Regler med oppgave-id står i `arbeid/handbok/hack_laerdom_case1.md`, under «Runde 2»:
1. Tall i tekst settes inn fra måleren, aldri for hånd (#2104, #2159, #2347, #2358, #2659, #2665, #2671, #2685).
2. Flerårsbenk og alle kandidater, også andres repo, måles før modellvalg (#2080, #2464, #2490, #2567).
3. Ingen reserveutgave av tekstene. Tilbakerulling er git-sha og skript (#2631, #2640, #2654, #2681, #2697, #2603).

Forslag til mekanisme: `tallmal.py`. Måleren skriver `tall.json`, og zip og synk rendrer `*.md.mal`.
Tallvakta gir RØDT for løse tall i maler. Kost: ca. 1–2 smedøkter. Bør bygges før dag 1 av Name that LLM.

Merk: temaene er sortert etter nøkkelord i titlene. Det er grovt, og noen oppgaver kan ha havnet i feil gruppe.
