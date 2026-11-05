# Case 1: hvorfor ble stemmeagenten ikke bedre etter frysen? (svar på ordre #261)

Kort svar: vi fant ting som *ser* bedre ut på test 2026, men ingen av dem er bevist bedre, og alle ble
funnet etter at testen var sett. Å bytte da ville vært å jukse med vår egen måling. Ingen nye målinger her;
hvert tall har kildesti (N = `arbeid/hack/c1/leveranse/NESTE_VERSJON.md`, T = `arbeid/hack/c1/leveranse/TREFFSIKKERHET.md`).

## 1. Det vi har (frossen kl. 16)
- F1 på MOT, test 2026: **0,476** (TP 30, FP 38, FN 28). Kilde: N:4-5.
- F1 på MOT, val 2025: **0,520** (TP 45, FP 29, FN 54). Kilde: N:5.
- «Følg styret» gir F1 MOT **0,000** (finner 0 av 58 MOT). Kilde: T:20, T:100. <!-- tallvakt: ignorer (baseline, ikke hovedtall) -->

## 2. Det vi prøvde etter frysen (test 2026, ikke hovedtall, 95 % KI for forskjellen mot frossen)
| Forsøk | F1 MOT | Mot frossen 0,476 | Kilde |
|---|---|---|---|
| NBIM-repoets presedensregel alene | 0,515 | +0,039 [−0,051; +0,126] | N:58-59, kilder/c1_nbim_repo_sammenligning.md:10 |
| NBIM-repoets hybrid på vår splitt | 0,545 | +0,069 [+0,007; +0,133] | N:59-60, kilder/c1_nbim_repo_sammenligning.md:13 |
| Vår hybrid (repoets sikre ja/nei + vår modell i midten) | 0,516 | +0,040 [−0,007; +0,095] | N:92-93 |
| Personnøkkel som trekk, 2026 | 0,525 | +0,049 [+0,016; +0,090] | N:76, kilder/c1_personnokkel_rullende.md |
| Personnøkkel, 2024 / 2025 | 0,418 / 0,516 | −0,037 [−0,133; +0,058] / +0,001 [−0,042; +0,050] | N:84-85, kilder/c1_personnokkel_rullende.md |

Les tabellen slik: tre av fem intervaller dekker null, altså kan gevinsten være null. Personnøkkelen
hjelper bare i 2026, året vi allerede hadde sett, og ikke i 2024 eller 2025 (N:85). Bare NBIM-hybriden
ligger helt over null, og den nedre kanten er +0,007, nesten null.

## 3. Hvorfor vi ikke byttet
- **Valgregelen:** alt velges på val, aldri på test (N:6). Alle tallene over er målt på test etter frysen.
  Velger vi det beste av flere testforsøk, blåser vi opp tallet. Det har skjedd før: t4e så best ut på test
  (0,529) men tapte på val, 0,468 mot 0,522 (N:100-101).
- **Frysen kl. 16** (mission.md:8): modellen var låst før disse forsøkene, og ombygging med nye
  lekkasjesjekker rakk vi ikke før frysen (N:36).
- **Støyen:** test har bare 58 MOT (T:100), og bootstrap-intervallet på F1 er ca. ±0,1 (N:33).
  Forskjeller på +0,04 er da innenfor det tilfeldige.
- **NBIM-repoets egen test (2025-26) inneholder 2026**, så utformingen kan være valgt med 2026 synlig (N:71).

## 4. Hva det betyr
Vi leverer 0,476 som er ærlig målt. Det vi lærte står som neste versjon: presedens først, vår rangering
etterpå, men først når det vinner på rullerende val over flere år (N:51-72, tiltak 2 og 4).
