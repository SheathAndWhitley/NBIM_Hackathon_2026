# Case 1: jurysvar og motstandstall i JURY.md godkjent etter én retting (dommer #2239)

05.11 kl. 13.40–13.50. Sjekket #2234 mot `case1_regelsjekk.md` punkt 1, 3 og 4. Tallene er talt på nytt fra kald kjøring
`/tmp/c1_kald/ut` (13:37, agent.csv + _data) med `arbeid/oppgave_2239/sjekk.py`, og måler v3
(sha 418a937e57) på `pred_maaler.csv`: TP 30, FP 38, FN 28, F1 0,476190, 183 av 1539 til menneske.

## Punkt for punkt
- **Pkt. 1, juryspørsmål 1–3:** besvart under egne overskrifter (`JURY.md:5`, `:11`, `:19`), og svarene er ærlige.
  Spm. 2 sier ja som sorteringshjelp og nei som automatisk stemme, med grunner. OK.
- **Pkt. 3, motstandstesten:** `JURY.md:15,37` og `BEGRENSNINGER.md:18` har de ekte tallene: 35–41 saker bytter stemme,
  20–21 uten ruting, F1 0,387–0,400. Tallene finnes i `c1_injeksjon_etter_2205.md:17-20`. «Ikke målt på den frosne» står ikke lenger noe sted. OK.
- **Pkt. 4, 188 av 1578:** 228 og 14,4 % er borte. 188 = 127 usikre + 60 ukjent selskap + 1 instruks (rutingsgrunn i agent.csv).
  183 av 1539 med fasit. Tallvakta er grønn: 153 påstander, 0 avvik. OK.

## Talt på nytt og funnet riktig
Accuracy 96,2 % / 95,7 %; avvik 66 = 58+5+3; aksjonærforslag=MOT F1 0,066 (2 av 58, `oppgave_2234/baseline_real_test.txt`);
21 treff og 38 FP rutet, 9 treff ikke rutet (alle riktige); 17 stille bom med maks P(MOT) 0,0896; alle 7 USA-MOT er stille bom;
18 aksjonærforslag av 1578; trening 11 785 saker 2019–2025 med 70–99 MOT per år; test 141 møter i 136 selskaper;
1504 FOR-standard-sitater; 0,365 / 0,415 / +0,11 [0,01; 0,22] (`c1_enkle_regler_og_hist1.md`); 0,375 / 99,4 % (`c1_robusthet_frossen.md`);
0,482 og 0,282 (`ERLIG_EVALUERING.md`); 18 av 18 og 8 av 20 (`c1_sitatkilder.md`); kjøretider (`c1_kjoretid.md`, avrundet).

## Avvik, rettet av meg
- `JURY.md:31` sa «styrevalg 28» blant styrets 56 egne forslag. Riktig er **26**: 28 inkluderer 2 styrevalg foreslått av
  aksjonærer (`c1_mot_sakstyper.md`, egen telling 26). Rettet til full fordeling 26+7+6+6+11 = 56, pluss en setning om de 2.
- `BEGRENSNINGER.md:3`: dobbel parentes slått sammen. Ingen tall endret.

**Dom: GODKJENT** etter rettingen. Kravet om én side (#2229) og måler-sha (#2238) ligger i egne oppgaver og er ikke sjekket her.
