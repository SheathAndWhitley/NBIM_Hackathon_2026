# Case 1: dommer2 kjører agenten selv og teller treffsikkerheten (#2207, ordre #241)

**Svar til guden:** en ekstern dommer som kjører programmet nå, får **95,7 % accuracy, ikke 97 %**.
Følg styret får 96,2 %. Hovedtallet, F1 på MOT, blir **0,476**. Tallet er nøyaktig det samme som i TREFFSIKKERHET.md.
De 98,75 % som står i pakka gjelder bare de 1356 sakene som *ikke* går til menneske. Det er ikke tallet for hele testen.

## Slik kjørte jeg
- Fulgte README som en fremmed: `sh arbeid/hack/levering/fremmed.sh /tmp/d2207_a` og så `/tmp/d2207_b`, hver i en tom mappe.
  NB: å kopiere bare `arbeid/hack/levering` er ikke nok. Agenten trenger modell og data utenfor mappa. `fremmed.sh` kopierer de filene (README sier det).
- Kjøringen bruker `env -i` og eget `.venv` (uv sync --frozen, 0 s fra cache). Agenten brukte 40 s og 36 s.
- Talte selv med eget skript, bare stdlib: `python3 -I arbeid/oppgave_2207/tell.py <agent.csv> state/opplastet/20261105_114241_real_votes.csv`.
  Det leser fasit direkte (år 2026, positiv = `nbim_vote == MOT` og `against_board == 1`) og bruker ikke måleren.

## Resultat (test 2026, 1578 saker inn, 1539 med fasit)

| mål | min telling | TREFFSIKKERHET.md | stemmer? |
|---|---:|---:|---|
| 2x2 | TP 30 FP 38 FN 28 TN 1443 | TP 30 FP 38 FN 28 TN 1443 | ja |
| accuracy agent | 95,71 % | 95,7 % | ja |
| accuracy følg styret | 96,23 % | 96,2 % | ja |
| recall MOT | 0,517 | 51,7 % | ja |
| presisjon MOT | 0,441 | 44,1 % | ja |
| **F1 MOT** | **0,4762** | 0,476 | ja |
| til menneske | 188 av 1578 (11,9 %), 183 av 1539 med fasit | 188 / 183 | ja |

**Definisjonsfelle (ikke feil, men bør vite om den):** kolonnen `mot_styret` i agent.csv har 74 enere. 3 av dem er saker der
styret sier MOT og agenten sier FOR (aksjonærforslag). Fasit er der også «NBIM stemte FOR, mot styret», så agenten har rett om avviket.
Men de 3 er ikke MOT-stemmer. Teller en dommer `mot_styret == 1` som positiv mot klassen «MOT-stemme», får hen
TP 30 FP 41, P 0,423, F1 **0,465** og accuracy 95,5 %. Hovedtallet 0,476 bruker «agenten anbefaler MOT mot et styre som sier FOR». Det er riktig for klassen,
men README/TREFFSIKKERHET bør si én setning om hvilken kolonne som skal telles. (Kjør tell.py med argument `kolonne` for å se varianten.)

## Nett/API og determinisme
- **Ingen nett eller API i agenten.** Grep i alle kopierte .py fant ingen requests/urllib/http/socket/anthropic/openai og ingen URL-er.
  Det eneste som kan gå mot nett er `uv sync --frozen`, og bare hvis uv-cachen mangler pakkene. Her tok det 0 s, altså fra cache.
  Det finnes ingen LLM-kall. «Med en API nå» gir altså samme tall: programmet er lokalt og frossent.
- **Deterministisk:** to kalde kjøringer ga byte-like filer.
  agent.csv sha256 `f0444a47…f17f7`, pred_maaler.csv `b113b545…3653`, _pred_uten_ruting.csv `22ac6717…c788f` (like i a og b).

## Funn utenom tallene
- Kjøring b endte med **utgang 1 (TALLVAKT RØD)**, men modell og svar var like. Grunnen er at `JURY_SPORSMAL.md:16` ble redigert mellom kjøringene
  (ny linje «…finne 30 ekte MOT-stemmer»). Tallvakta leser 30 som «antall MOT» mot målerens 58. Det er falsk alarm på tekst, men en fremmed ser
  «Pakka er IKKE verifisert». Linja må omformuleres eller merkes `tallvakt: ignorer` før den endelige verifiseringen kl. 19.30.
