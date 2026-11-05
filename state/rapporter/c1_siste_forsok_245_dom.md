# Dom #2249: siste MOT-forsøk (#2248, smed2) er valgt ærlig. Ikke tatt inn. Frossen #2044 miks h2 står.

dommer, 05.11 kl. 14.00. Gjelder `arbeid/oppgave_2248/train.py` og `state/rapporter/c1_siste_forsok_245.md`.

**Dom: GODKJENT PROSESS, IKKE TATT INN.** Smeden bytter ikke modell før kl. 16. #2044 miks h2 (val 0,5217, test 0,4818 i forsøk #1067) er fortsatt den frosne.

## Sjekket
1. **Valg bare på val 2025.** C, grense og loft velges i løkka på `va = ok & HOVED & year == 2025`, trent på `year < 2025`. Variant (`--x`) er valgt på `SCORE_VAL` i loggene. Samme kode som #2081/#2044 utenom de nye trekkene.
2. **Test kjørt null ganger.** Ingen logg i `arbeid/oppgave_2248/` inneholder «TEST 2026», og ingen `pred_*.csv`/`svar_*.csv` finnes (test skrives bare med `--test 1`). Det er riktig: akseptkravet (val > base + 0,03) ble ikke nådd, så test skulle ikke kjøres. Derfor finnes ingen testfil å måle med 9d81a418dd. Testtallet som gjelder er fortsatt forsøk #1067 (0,4818, målt av tavla med 9d81a418dd).
3. **Ingen fremtidige etiketter, ingen rationale/nbim_vote.** FORBUDT-settet er urørt, og `BRUKT` snitter det ikke (skrives ut i hver logg). Nye trekk:
   - `lt`: MOT-rate per land×type, marked×type, land×forslagsstiller fra `y_all.where(ok & HOVED & year < til_aar)`. Val ser < 2025, test ville sett < 2026. OK.
   - `ny`: «første gang nøkkelen står på selskapets agenda» = `DATO <= min(DATO per nøkkel)`. Bare datoer, ingen etiketter. Senere møter kan ikke endre om en rad er den første. OK.
   - `mt`: tellinger per `meeting_id` og `meeting_id|type`. Ingen etiketter. OK.
   - Historikk (`hist_feats`) er uendret fra #2044: løpende, bare møter strengt før radens dato, aldri år > målåret.
4. **Koden er ikke endret underveis.** sha1 av train.py kl. 13:46 (min kopi) og ved lukking kl. 13:56: `8c12ee525873`, lik.
5. **Tallene reproduseres.** Jeg kjørte base, mt og lt selv (`arbeid/oppgave_2249/dommer_*.log`):

| variant | smed2 val F1 | dommer val F1 | P / R / PR-AUC (dommer) |
|---|---|---|---|
| base | 0,5217 | 0,5217 | 0,593 / 0,466 / 0,474 |
| + mt | 0,5213 | 0,5213 | 0,577 / 0,476 / 0,461 |
| + lt | 0,5140 | 0,5140 | 0,605 / 0,447 / 0,465 |
| + ny | 0,5217 | (ikke kjørt, lik base i smedens logg) | |
| + lt+ny+mt | 0,4804 | (ikke kjørt) | |

Tabellen i smedens rapport stemmer med loggene linje for linje.

## Merknader
- Forsøk #1140 på tavla (0,5213, «egen») er et **val-tall**, ikke et testtall. Det skal ikke leses som konkurrent til 0,4818/0,476. Ingen svarfil, så det kan ikke ommåles med rundens måler, og det skal heller ikke.
- Smed2 lukket etter 10 av 60 min. Det er riktig: kravet var avgjort, og flere forsøk på val før frys ville bare økt sjansen for et tilfeldig treff på val.
- Til juryen: dette er et dokumentert, ærlig negativt resultat, valgt på val, test urørt. Det kan siteres slik.
