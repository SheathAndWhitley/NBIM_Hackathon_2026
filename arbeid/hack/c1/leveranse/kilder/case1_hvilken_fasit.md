# Case 1: hvilken fasit teller, NPX-fila eller NBIMs API-stemmer? (speider sak 2052, 05.11)

**Anbefaling: Hovedtallet er F1 på MOT mot styret i real_votes (NBIMs egne stemmer). NPX-fila rapporteres som sekundærtall, med `against_board` rettet. «Aksjonærforslag=MOT = 0,645» må aldri stå som resultat, for det tallet bygger på en feil i fasiten.**

## Hva casen sier
- Case-PDF s. 1: «Evaluer mot **NBIM sine faktiske, publiserte stemmer**», og «94 % stemt med styret i 2025, baselinen som må slås … Verdien ligger i de 6 % der NBIM sier nei.»
- README for Case 1: «**Fasit: SEC Form N-PX**», men også at NBIMs database «har ingen åpen eksport, API-tilgang må søkes om. Ikke bygg noe som er avhengig av den.» Regler s. 3 sier det samme: databasen «kan ikke være kritisk sti».
- Arrangørens `baseline.py` teller MOT som `stemme ∈ {against, mot, withhold}`, altså stemmeretning og ikke avvik fra styret. Kick-off og hovedmålet definerer derimot MOT som **mot styret**. Juryen (NBIM) spør etter avvik fra styret.

**Tolkning:** Juryen evaluerer metode, ikke en skjult testfil. «Fasit brukt» (kriteriet) betyr NBIMs egne stemmer. Det er real_votes. NPX var arrangørens åpne reserve.

## Hvordan MOT er definert i de to filene (målt, uten injeksjonsrader)
| | real_votes (NBIM-API) | npx_votes (11:42 og 11:43 er byte-like) |
|---|---|---|
| against_board = 1 | stemme ≠ styret, AVSTÅ mot styrets FOR teller som avvik | samme formel, men på `mgmt_rec` |
| Avvik | 744 av 13 324 (5,6 %) | 1 936 av 49 006 (3,9 %) |
| Styret MOT eget forslag | 3 av 13 211 | **2 538 av 48 000** |
| Styret FOR aksjonærforslag | 29 av 150 | **1 122 av 1 210** |

**Feilen i NPX:** `mgmt_rec_raw` er nesten helt sikkert N-PX-feltet *for/mot ledelsen*, og ikke styrets anbefaling. Eksempel: «Re-elect Antoine de Saint-Affrique as Director» (Danones CEO) står med styret = MOT. Det betyr at:
- 1 770 ledelsesforslag der NBIM stemte MOT mot ledelsen er merket *ikke avvik* (falske FOR).
- 1 031 aksjonærforslag der NBIM stemte MOT, altså **med** styret, er merket *avvik*. Disse utgjør 58 % av alle NPX-avvik, og 48 % i 2026.
- Leser vi `mgmt_rec_raw=AGAINST` som «NBIM gikk mot ledelsen», blir avviksraten 5,2 %, noe som stemmer med casens 94 %/6 %. Da faller «aksjonærforslag=MOT» fra F1 0,645 til **0,071** på 2026, og fra 0,708 til 0,046 totalt. Det er på linje med 0 på real_votes.

## Hva det betyr for oss
1. Hovedtall: F1 på MOT mot styret i real_votes. Tidssplitten er train ≤2024, val 2025, test 2026, med 66 avvik i test. Bootstrap-intervallet blir bredt, og det skal vi si rett ut.
2. Sekundært: NPX med rettet etikett (`against_board = mgmt_rec_raw=="AGAINST"`) gir et større test-sett i flere land. Rapporteres med en fotnote om rettelsen.
3. AVSTÅ: begge filene teller AVSTÅ mot styrets FOR som avvik. Det beholder vi, og vi sier det i kravresponsen.
4. Modeller eller gulv som er trent eller valgt på dagens NPX-`against_board` (sak 2024, data_off) må sjekkes på nytt. Ellers har de lært «aksjonærforslag → MOT».

Usikkerhet: Feltbetydningen er utledet fra mønsteret i dataene. N-PX-dokumentasjonen er ikke sjekket. Mønsteret er likevel entydig: tusenvis av styrer skal ha stemt mot sine egne kandidater, mot bare 3 i NBIMs egne data.
Kode: kjørt inline med pandas på `arbeid/hack/CASE/*_votes.csv`. Tallene er reproduserbare med crosstab proponent × mgmt_rec_raw × nbim_vote.
