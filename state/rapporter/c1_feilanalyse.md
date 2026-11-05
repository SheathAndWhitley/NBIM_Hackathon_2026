# Case 1 feilanalyse: hvilke MOT-stemmer den frosne modellen bommer på (test 2026, #2097)

Modell: frossen #2044 miks h2, grense 0,9188 (valgt på val). Ingen modellendring.
Svar: `arbeid/oppgave_2087/svar_test.csv`. Fasit: real_votes (MOT mot styret = nbim_vote MOT og against_board 1, som måler v3).
Ett kall: `.venv/bin/python arbeid/oppgave_2097/feilanalyse.py` (under 1 s). Full liste over hver bom: `state/rapporter/c1_feilanalyse_tabeller.md`.

**TP 30, FP 38, FN 28, F1 MOT 0,476** (P 0,44, R 0,52) på 1539 vurderte rader. Samme tall som `dommer_2090_streng_mot.md`.

## Bommene fordelt
| sakstype | TP | FP (falsk MOT) | FN (glemt MOT) |
|---|---|---|---|
| Styrevalg (DIRECTOR_ELECTION) | 15 | 26 | 13 |
| Lønn (SAY_ON_PAY) | 3 | 8 | 0 |
| Annet fra styret (OTHER_MGMT) | 1 | 1 | 5 |
| Revisor (AUDITOR) | 3 | 0 | 4 |
| Vedtekter (ARTICLES) | 1 | 1 | 2 |
| Aksjeutstedelse | 0 | 0 | 2 |
| Andre 6 typer | 7 | 2 | 2 |
| **sum** | **30** | **38** | **28** |

| land | TP | FP | FN |
|---|---|---|---|
| USA | 0 | 9 | 7 |
| India | 1 | 6 | 3 |
| Japan | 4 | 3 | 3 |
| Belgia | 2 | 6 | 0 |
| Kina | 0 | 2 | 3 |
| Indonesia | 6 | 1 | 1 |
| Sveits | 4 | 3 | 0 |
| 14 andre land | 13 | 8 | 11 |
| **sum** | **30** | **38** | **28** |

| hadde selskapet MOT før? | TP | FP | FN |
|---|---|---|---|
| ja, tidligere i 2026 | 0 | 0 | 0 |
| bare i tidligere år | 28 | 37 | 20 |
| nei, aldri | 2 | 1 | 8 |
| **sum** | **30** | **38** | **28** |

## Hva tabellene sier
- **Modellen lener seg på historikk.** 65 av 68 MOT-predikasjoner gjelder selskaper med MOT i et tidligere år. Av de 10 MOT-ene hos selskaper uten MOT-historikk fant den bare 2. Ingen selskap i test hadde MOT tidligere i 2026: de fleste har bare ett møte i året, så sesongen gir ingen hjelp.
- **Styrevalg er både styrken og hovedkilden til feil**: 26 av 38 falske MOT. Mange er amerikanske styreledere som også er toppsjef (Dueser, Swift, Kemper, Jordan, Michael Dell). Der stemte NBIM MOT før, men FOR i 2026.
- **USA gir null treff**: 0 TP, 9 FP, 7 FN. Det er det svakeste landet.
- **Glemte MOT ligger ofte like under grensen**: 8 av 28 FN har p mellom 0,85 og 0,918. 10 FN har p under 0,5. Det er nye temaer modellen ikke har sett.

## Tre typiske bommer
1. **FP, First Financial Bankshares, «Elect Director F. Scott Dueser» (USA, p 0,988):** selskapet og den samme personen har fått MOT før, så modellen er nesten sikker. NBIM stemte likevel FOR i 2026. Historikken veier tyngre enn det som er nytt i år.
2. **FN, Texas Capital Bancshares, «Change State of Incorporation from Delaware to Texas» (USA, p 0,199):** NBIM stemte MOT fordi aksjonærenes rettigheter svekkes (rationale: «basic right of shareholders»). Det samme gjaldt Dell. Flytting fra Delaware til Texas er et nytt tema i 2025–26 som sakstypen OTHER_MGMT ikke fanger.
3. **FN, S.F. Holding, «Approve PricewaterhouseCoopers … as auditors» (Kina, p 0,901, to møter):** NBIM stemte MOT på grunn av revisorens uavhengighet. Modellen var nær, men under grensen 0,918. Det er en grensesak som bør sendes til et menneske og ikke avgjøres automatisk.

## Hva det betyr for juryen og ruting (ingen modellendring)
- Saker med p mellom omtrent 0,85 og grensen inneholder 8 av 28 glemte MOT. Det støtter at båndet «send til menneske» ligger rett under grensen.
- Styrevalg i USA der MOT-signalet bare kommer fra tidligere år, og nye temaer om rettigheter (flytting av selskapets hjemstat, vedtektsendringer), er kjente svakheter. De bør stå ærlig i JURY.md.
