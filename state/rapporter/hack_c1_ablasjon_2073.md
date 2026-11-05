# Case 1: ablasjon av ledermodellen (smed2 #2044), hvilke trekk bærer F1 på MOT (smed3 #2073)

**Oppsett.** Modellen er #2044 (`arbeid/oppgave_2044/train.py`, miks LR+LGBM, `--hist 2` løpende historikk), den som `levering/c1_real.py` kjører i agenten. Logikken er kopiert uendret til `arbeid/oppgave_2073/abl.py`, og én trekkgruppe tas ut om gangen. Treningen bruker real_votes år <2025 og målingen **val 2025** (1909 saker, 103 MOT, MOT = `against_board`). C og grense velges på nytt for hver variant, slik train.py gjør. **Test 2026 er ikke kjørt.** F1, P og R kommer fra den offisielle måleren (`maaler_offisiell_v2.py SVAR val --data real`) og stemmer på alle fire desimaler med skriptets eget tall. Usikkerheten er en parvis bootstrap over val-sakene (2000 trekk, grensene holdt fast).

| variant | F1 MOT | P | R | flagget | PR-AUC | ΔF1 mot full [95 %-KI] | forsøk |
|---|---|---|---|---|---|---|---|
| **full (lederen)** | **0.522** | 0.593 | 0.466 | 81 | 0.473 | (KI på F1: [0.431, 0.606]) | #1056 |
| uten historikk | 0.337 | 0.258 | 0.485 | 194 | 0.273 | **−0.185 [−0.268, −0.096]** | #1057 |
| uten tekst (tfidf) | 0.506 | 0.620 | 0.427 | 71 | 0.421 | −0.016 [−0.061, +0.025] | #1058 |
| uten sakstype (type, forslagsstiller, styrets anbef., item_no) | 0.506 | 0.620 | 0.427 | 71 | 0.427 | −0.016 [−0.059, +0.023] | #1059 |
| uten land (country, market) | 0.492 | 0.579 | 0.427 | 76 | 0.432 | −0.030 [−0.072, +0.011] | #1060 |
| + møteaggregat (finnes ikke i lederen, lagt TIL) | 0.489 | 0.541 | 0.447 | 85 | 0.428 | −0.032 [−0.078, +0.011] | #1061 |
| bare historikk | 0.482 | 0.635 | 0.388 | 63 | 0.358 | −0.039 [−0.096, +0.015] | #1062 |
| bare sakstype | 0.155 | 0.096 | 0.408 | 440 | 0.146 | −0.366 [−0.446, −0.284] | #1063 |

**Funn.**
1. **Historikken bærer modellen.** Det er MOT-andelen NBIM tidligere har hatt i samme selskap, i samme selskap+tekst og på samme tekst, bare fra møter før saken. Tas den ut, faller F1 med 0,185, og KI-et ligger klart under null. Alene gir den 0,48 av 0,52.
2. **Tekst, sakstype og land gir hver for seg 0,02 til 0,03.** Ingen av bidragene er signifikante på val. Gruppene overlapper (sakstype finnes også i tekst og historikk), så de erstatter hverandre. Samlet løfter de PR-AUC fra 0,36 til 0,47, og det er der de synes.
3. **Møteaggregat finnes ikke i lederen.** Jeg testet det som tillegg: størrelse, andel aksjonærforslag, styrevalg og lønnssaker per møte, og plassering i møtet. Det gir −0,032 [−0,078, +0,011] og bør ikke legges til.
4. Uten historikk flagger modellen 194 saker og presisjonen faller til 0,26. Den vet da hvilke *typer* saker NBIM stemmer mot, men ikke *hvilke selskaper*.

**Forbehold (ærlig).**
- Grensen velges på selve val-settet, så alle tallene er optimistiske i like stor grad. Sammenligningen mellom variantene er rettferdig, men nivået er ikke et test-tall. Lederens test 2026 er 0,482.
- «Uten tekst» fjerner bare tfidf. Normalisert tekst er fortsatt nøkkel i to av de tre historikktrekkene.
- Historikk med `--hist 2` bruker etiketter fra tidligere møter *samme år*. Det forutsetter at NBIM publiserer stemmene løpende. Med streng historikk (bare tidligere år) fikk smed2 0,386 på test.
- 103 MOT i val gir brede KI. Bare historikk og «bare sakstype» skiller seg sikkert fra full.

**Til jurysvaret (metode):** «Ablasjon på val 2025: uten selskapets egen stemmehistorikk faller F1 på MOT fra 0,52 til 0,34 (Δ −0,19, 95 %-KI [−0,27, −0,10]). Tekst, sakstype og land gir hver 0,02 til 0,03, og ingen av dem er signifikante.»

Reproduser: `cd arbeid/oppgave_2073 && uv run --project ../oppgave_2023 python abl.py <real_votes.csv> --uten historikk --ut pred_uten_historikk.csv`, så `python3 -I ../hack/c1/maaler_offisiell_v2.py pred_uten_historikk.csv val --data real`. Bootstrap: `uv run --project ../oppgave_2023 python boot.py`.

Merk: rundens måler på tavla er UGYLDIG («måleren er endret på disk 8733327407 -> 474eae7bc8»). Forsøkene er derfor meldt med `--score` fra maaler_offisiell_v2 og `--sti`. Dommeren må sette måleren på nytt.
