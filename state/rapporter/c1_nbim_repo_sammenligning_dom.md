# Dom #2465: sammenligningen med det opplastede NBIM-repoet (#2464) er gjenskapt, GODKJENT

Kjørt av dommer 2026-11-05 16:05–16:14, egen kopi av koden i `arbeid/oppgave_2465/` (samme `kjor_nbim.py`, `python -I`, begge splitter), svarfiler målt med `arbeid/hack/c1/maaler_offisiell_v3.py <svar> test --data real --score mot`. Datafila: sha256 71ba51… lik i `state/opplastet/` og i repoets `ny_data/real_votes.csv`.

## Tallene (test 2026, F1 MOT mot styret, 58 i fasit)

| rad i rapporten | smed4 | dommer | avvik |
|---|---|---|---|
| frossen #2044 (`oppgave_2103/full_test.csv`, sha 697021… = frys_fasit_1600) | 0,476190 | 0,476190 | 0 |
| deres persistence | 0,514851 | 0,514851 | 0 |
| deres modell alene, deres splitt | 0,464646 | 0,464646 | 0 |
| deres hybrid, deres splitt | 0,522523 | 0,522523 | 0 |
| deres hybrid, vår splitt | 0,545455 | 0,545455 | 0 |

P, R, flagget, avvik-F1 og PR-AUC i tabellen stemmer også. Repoets egne tall på 2025-26 (hybrid avvik-F1 0,518, persistence 0,491) kom ut likt. KI med `oppgave_2103/diff_ki.py`: hybrid vår splitt +0,069 [+0,007; +0,133], B<A 1 %; persistence +0,039 [−0,051; +0,126]. Alt innenfor kravet (≤ 0,001; faktisk 0).

## Splitter
Alle rader i tabellen er målt på samme vindu (test 2026) med samme måler og samme fasit. De eneste 2025-26-tallene er merket som repoets egne gjenskapte tall og er avvik inkludert AVSTÅ. Rapporten blander ikke splitter. Forskjellen i treningsdata (≤2023 mot ≤2024) er merket per rad.

## To presiseringer
- Presedensregelen er «samme direktør hvis kjent, ellers samme sakstekst» (`prev_same_person.fillna(prev_same_item)`), ikke «sak eller direktør». Og «avvek» teller alle avvik, også AVSTÅ. Ingen tallendring, men ordlyden bør være presis om den brukes.
- Modell alene på vår splitt (GBM valgt) gir 0,538, høyere enn hybrid på deres splitt. Står ikke i tabellen; ikke feil, bare utelatt.

## Bør noe inn i JURYSVAR?
Ja, én setning i ærlig evaluering (tekst, ingen modellendring): JURYSVAR sier i dag at den sterkeste enkle regelen vi har målt gir 0,365 og at modellen slår den med +0,11. NBIMs egen presedensregel i det opplastede repoet gir 0,515 på vår måler, +0,04 over vår modell, innenfor støyen [−0,05; +0,13], mens vår rangering fortsatt er best (PR-AUC 0,525 mot 0,318). Utelates det, står jurysvaret med en påstand juryen selv kan motbevise fra sitt eget repo.

Tavleforsøk #1187-1189 står som selvrapportert; `forsok-vakt` gir ingen utskrift for dem. Tallene er verifisert her.
