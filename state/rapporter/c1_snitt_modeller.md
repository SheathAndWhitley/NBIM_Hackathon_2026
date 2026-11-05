# Case 1 #2568: snitt av frossen + person + hybrid. Byttregelen er ikke oppfylt, frossen står

**Svar:** et snitt av sannsynlighetene med like vekter jevner ikke ut svingningen. Det taper 0,047 i 2024 og ender 0,002 under frossen i snitt. Frossen #2044 står, og tallet går i NESTE_VERSJON.

## Oppsett (fastsatt før måling, ingen vekttuning)
- Frossen og person (`prev_same_person`): prediksjonsfilene fra #2503 (`arbeid/oppgave_2503/{full,person}_T_{val,test}.csv`).
- Hybrid: `ballot_model.fit_select`, trent til og med T-2, valgt og kalibrert på T-1 (som `oppgave_2531/rull.py`). P = 1 ved presedens, ellers kalibrert p.
- snitt3 = (frossen + person + hybrid) / 3. Én terskel valgt på val (T-1), og test T kjøres én gang.
- Måler: F1 på MOT mot styret (fasit nbim_vote MOT og against_board 1). KI: `diff_ki_aar.py`, parret klyngebootstrap på selskap, 2000 trekk.
- KP: frossen fra fil gir 0,4545/0,5143/0,4762, som forventet. Hybrid 2024 gir 0,4072, likt #2531.

## Tall (test T, val = T-1)
| variant | 2024 | 2025 | 2026 | snitt | mot frossen |
|---|---|---|---|---|---|
| frossen #2044 | 0,4545 (P 0,68 R 0,34) | 0,5143 (P 0,59 R 0,45) | 0,4762 (P 0,44 R 0,52) | 0,4817 | – |
| **snitt3** | 0,4072 (P 0,43 R 0,39) | 0,5204 (P 0,53 R 0,52) | 0,5113 (P 0,45 R 0,59) | **0,4796** | −0,002 |
| KI snitt3 − frossen | −0,047 [−0,173; +0,092] | +0,006 [−0,058; +0,070] | +0,035 [−0,019; +0,097] | | |
| person alene | 0,4179 | 0,5155 | 0,5124 | 0,4819 | +0,000 |
| hybrid alene | 0,4072 | 0,5060 | 0,5455 | 0,4862 | +0,005 |

Byttregelen: snittet må være minst +0,02 over frossen, og intet år må være mer enn 0,02 dårligere. snitt3 gir −0,002 i snitt og −0,047 i 2024, så den faller på begge kravene.

## Hvorfor snittet ikke demper svingningen
Hybridens isotone kalibrering er tilpasset på selve val-året. På val ser den derfor bedre ut enn den er, og terskelen havner der bare hybridens presedenssaker blir flagget. I 2024 er snitt3 og hybrid alene helt like (val 0,4138, test 0,4072, tp34 fp45). Snittet arver altså hybridens tap i stedet for å dempe det. En rettferdig sammenslåing krever en hybrid kalibrert utenfor val-året, for eksempel på T-2. Det er en ny kandidat og må måles på nytt.

## Bivarianter (to-modell-snitt, ikke kandidater, bare til NESTE_VERSJON)
Disse to er sett etter at snitt3 var målt, og regnes derfor ikke som kandidater (flere sammenligninger):
- frossen + person: 0,5083/0,5055/0,4697, snitt 0,4945 (+0,013). 2024 +0,054 [−0,062; +0,165], 2025 −0,009, 2026 −0,007. Oppfyller ingen av årskravene, men under +0,02 i snitt.
- frossen + hybrid: 0,4072/0,5319/0,5000, snitt 0,4797. Samme tap i 2024.

## Anbefaling
Ikke bytt. For NESTE_VERSJON: kalibrer hybriden på T-2, ikke på val-året. Mål deretter frossen + person (+ hybrid) på nytt med samme byttregel, og fastsett varianten før målingen.

Kode: `arbeid/oppgave_2568/snitt.py` (logg `snitt.log`, KI i `ki.log`, svarfiler `svar_*_T.csv`). Forsøk #1202 på tavla.
