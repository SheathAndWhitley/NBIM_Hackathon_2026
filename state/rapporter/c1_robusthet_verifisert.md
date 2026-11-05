# Case 1: verifisering av robusthet / hovedtall i JURYSVAR og README (#2110, dommer2)

**Robusthetstesten (#2101) er ikke verifisert:** #2101 (smed3) sto claimed (40 %) kl. 12:36. Derfor ble reservesjekken kjørt: har JURYSVAR og README bare 0,476 som hovedtall etter #2104?

## Dom
**GODKJENT for pakkefilene, AVVIK for to gamle filer som fortsatt ligger i leveransen.**

| Fil | Hovedtall | Dom |
|---|---|---|
| `arbeid/hack/levering/JURYSVAR.md` (12:34) | 0,476 [0,36; 0,59], l. 5. 0,4818 merket som sidetall (l. 7), 0,474 merket N-PX (l. 8) | GODKJENT |
| `arbeid/hack/levering/README.md` | 0,476 (l. 3), 0,4818 sidetall (l. 6), 0,474 «ikke hovedtallet» (l. 31–32) | GODKJENT |
| `arbeid/hack/c1/leveranse/README.md` (12:30) | 0,476 (l. 7), 0,482 sidetall (l. 9), l. 31 forklarer SCORE 0,4818 vs 0,4762 | GODKJENT |
| `arbeid/hack/c1/JURYSVAR.md` (12:08, #2066) | **0,482 som hovedtall** (l. 21, 23, 39, 40), «66 MOT» (l. 6, 25; 66 er avvik, MOT er 58) | **AVVIK** |
| `arbeid/hack/c1/leveranse/jury_svar.md` (11:00) | utkast med TODO, før real_votes. KRAVRESPONS rad 27 peker hit | **AVVIK** |

Også sjekket uten funn: BEGRENSNINGER, ERLIG_EVALUERING (0,482 tydelig merket som avvik-ablasjon), c1/leveranse/kravrespons, levering/METODE, BESLUTNINGSSTOTTE, KRAVRESPONS. Alle har 0,476 som hovedtall og 0,482 som merket sidetall.

## Risiko
En jurymedlem som åpner `c1/JURYSVAR.md` leser «vår modell gir 0,482» og «66 MOT». Det motsier hovedtallet. `c1_ruting_verifisert.md` siterer fortsatt c1/JURYSVAR.md l. 42.

## Tiltak
- Ny oppgave: fjern/arkiver `c1/JURYSVAR.md` og `c1/leveranse/jury_svar.md` fra pakken (eller oppdater til 0,476/58 MOT), og la KRAVRESPONS rad 27 bare peke til `levering/JURYSVAR.md`.
- Robusthetstesten (#2101) må verifiseres når den lukkes; den er ikke dekket her.
