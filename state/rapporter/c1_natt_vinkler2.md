# Case 1: to nye vinkler for natta, med prøvetall (arkitekt, #2884)

Grunnlaget er frossen repo4 (`oppgave_2567/abl_rull.py`, miks, hist 2, repo4-trekk). Prototypen ligger i `arbeid/oppgave_2884/rr.py`. Den er en kopi med tre flagg: `--refit N`, `--strat kol` og `--decay hl`.
**KP:** jeg ventet base 2025 = 0,5233 (repo4_2025.log, #2868) og fikk 0,5233.
NB: tallene er SCORE, altså F1 på against_board med rå grense fra val, uten av-regel. De er derfor ikke natt-målerens tall, og base er 0,3628 / 0,5408 / 0,5233 / 0,5294. Dette er prøver og ikke målinger etter bytteregelen.
Alle fire testår er kjørt (val = året før), også vaktåret 2023. Hver kjøring tar ca. 15 s.

| vinkel | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | verst |
|---|---|---|---|---|---|---|
| base (frossen repo4) | 0,3628 | 0,5408 | 0,5233 | 0,5294 | 0,5312 | |
| **A: månedlig re-trening, grense fra vanlig val** | 0,3721 | 0,5392 | 0,5116 | 0,5649 | **0,5386 (+0,007)** | −0,012 (2025) |
| A: kvartalsvis, grense fra vanlig val | 0,3662 | 0,5427 | 0,5233 | 0,5441 | 0,5367 (+0,006) | 0 |
| A: månedlig, grense fra re-trent val | 0,3687 | 0,5612 | 0,5000 | 0,5854 | 0,5489 (+0,018) | **−0,023 (2025)** |
| B: egen grense per marked (DM/EM) | 0,3585 | 0,5333 | 0,5176 | 0,4966 | 0,5158 (−0,015) | −0,033 |
| C: nylighetsvektet MOT-rate (halveringstid 1 år) | 0,3347 | 0,5486 | 0,4973 | 0,5224 | 0,5228 (−0,008) | −0,028 |

PR-AUC på test, base mot A månedlig: 0,290→0,309, 0,564→0,593, 0,500→0,493, 0,537→0,559. Rangeringen blir altså bedre 3 av 4 år. Det er ikke bare grensen som flytter seg.

## Vinkel A → smed: løpende re-trening innen året (nytt spor, sporsjekk «refit/månedlig»: ingen treff)
**Hva endres:** i dag trenes modellen én gang på år < T og brukes på hele år T. Historikktrekkene er allerede løpende (hist 2), men vektene er ikke det. NBIM publiserer stemmene løpende, så i stedet trenes LR og LGBM på nytt hver måned, på alle møter strengt før månedens start. Det er samme regel for hva som er lov som hist 2 bruker allerede. C og grense velges som før på vanlig val.
**Hvorfor:** feilgruppe 3/4 (Kinder Morgan) og selskaper som bytter mening i løpet av sesongen. De første møtene i året lærer modellen om resten. I 2026 gir det +0,036.
**Hvor koden røres:** `refit_pred()` i `arbeid/oppgave_2884/rr.py`, ca. 12 linjer. Den kaller `pred(trb, aar, C)` per måned. Ingenting annet endres. Kjør: `uv run --project ../oppgave_2023 python rr.py $D --ut x.csv --hist 2 --variant miks --testaar T --repo $R --refit 1`. Svarfila skal bruke grensen `MED_BASEGRENSE`, altså t0, ikke den re-trente.
**Risiko:** +0,007 er under kravet +0,02 og innenfor støyen (KI ±0,04). Velger man grensen på re-trent val, blir snittet +0,018, men 2025 faller 0,023, så den varianten er forbudt etter regelen. Re-treningen er en innpakning rundt modellen og står utenom trekkene. Derfor kan den stables med vinkel 2 (SVD) og med av-regelen uten at noe kolliderer. Det er det eneste realistiske løpet mot +0,02. **Anbefaling:** skriv REGEL.md for «leder + refit 1 + grense t0» og mål med natt-måleren. Faller vinkel 2 positivt ut, mål også «vinkel 2 + refit 1».

## Vinkel B: egen grense per marked: LUKK
**Hva:** grensen velges per marked (DM/EM) på val, koordinatvis, i stedet for én årsvis grense. Utgangspunktet var at DM står for 80 % av FP og EM for 47 % av FN.
**Tall:** −0,015 i snitt og −0,033 i 2026. Val-F1 går opp alle år (for eksempel 0,556→0,575 i 2024), men test faller alle år. Med ca. 30–70 MOT per segment er grensen per segment bare overtilpasning. Ikke bygg den. Det taler også mot andre oppdelte grenser (per land eller type).

## Vinkel C: nylighetsvektet historikk (feature-versjonen av smed2s regimeskifte): LUKK ved hl = 1
**Hva:** for selskap og for selskap|type: MOT-rate med eksponentiell nedvekting (halveringstid 1 år), vekt og differansen mot den langsiktige raten, som 5 kolonner (`--decay 1`).
**Tall:** −0,008 i snitt, og vaktåret 2023 faller 0,028. Bare 2024 går opp (+0,008, VW-året). Resultatet bekrefter smed2s +0,005 med regelversjonen: regimeskiftet er for sjeldent til å bære +0,02, og ellers lager trekket støy.

## Trukket vinkel (#156)
Trekket ga 1) DP over grense, 2) aktuarfag / populasjon og kryssing, 3) militær logistikk / grådig med angring. Den mest lovende var aktuarfag: erfaringsprising, altså at premien justeres løpende etter skadene. Det er i praksis vinkel A, og der ble den testet: +0,007. Bühlmann-troverdighet på selskapsraten finnes allerede som (s+0,05)/(c+1) i hist_feats. Kostanslaget for en egen k per sakstype er 20 min, med forventet gevinst under 0,005, som ikke er bygget. 1) og 3) er grensejustering, som B nettopp har vist taper.

## Gjenskap
`cd arbeid/oppgave_2884; D=../../state/opplastet/20261105_114241_real_votes.csv; R=prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate`, med `--refit 1|3`, `--strat market` eller `--decay 1`. Loggene er `base_T.log`, `refit1_T.log`, `refit3b_T.log` og `decay1_T.log`.
