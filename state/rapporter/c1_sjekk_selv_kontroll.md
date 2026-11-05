# Case 1: dommer2 kjører sjekk_treffsikkerhet.sh fra kald kopi (#2208)

**Dom: GODKJENT.** Skriptet til smed2 (#2206) gir de samme tallene som min egen telling fra #2207, og sha-en matcher den frosne fila.

## Slik kjørte jeg (bare README)
1. `sh arbeid/hack/levering/fremmed.sh /tmp/d2208` lagde en tom kopi med egen `.venv` (uv sync --frozen).
2. Fra roten av kopien, uten arvet miljø:
   `cd /tmp/d2208 && env -i HOME=/tmp/d2208/home PATH=/usr/bin:/bin LANG=C.UTF-8 sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/d2208_ut`
3. Utgang 0, agenten brukte 6 s. Loggen nevner ikke landsbymappen, og skriptet brukte kopiens `.venv` og kopiens real_votes.
4. Kontroll: `shasum -a 256` på den nye fila og `python3 -I arbeid/oppgave_2207/tell.py /tmp/d2208_ut/agent.csv <real_votes>` (mitt eget telleskript).

| mål | skriptet (kald kopi) | min telling #2207 | min telling på ny fil |
|---|---|---|---|
| 2x2 | TP 30 FP 38 FN 28 TN 1443 | samme | samme |
| accuracy agent / følg styret | 0,9571 / 0,9623 | samme | samme |
| MOT recall / presisjon / F1 | 0,5172 / 0,4412 / **0,4762** | samme | samme |
| til menneske | 188 av 1578, 183 av 1539 med fasit | samme | samme |
| sha256 pred_maaler.csv | LIK `b113b545…3653` | lik den i landsbymappen | – |

Akseptkravene er oppfylt: tallene er like, det trengs ingen forkunnskap utover README-avsnittet «Sjekk tallene selv» (pluss fremmed.sh for å lage kopien), og sha-en matcher.

## Merknader (ikke del av dommen over skriptet)
- **`fremmed.sh` avslutter med utgang 1 (TALLVAKT RØD)** på grunn av `arbeid/hack/c1/leveranse/JURY.md:15`: der står 228 / 14,4 % / P 0,69, mens målt er 188 / 11,9 % / 0,4412. Det samme funnet meldte smed2. En fremmed dommer ser «Pakka er IKKE verifisert» før hen kommer til sjekk-skriptet. Linja må rettes eller merkes «eldre» før frysen kl. 16. Det er ikke en feil i skriptet.
- Skriptets fallback når `.venv` mangler peker på `arbeid/kandidater/smed2_c1_mot`, og den mappa finnes ikke i kopien. Fallbacken slår derfor bare til i landsbymappen. I kopien fra fremmed.sh finnes `.venv` alltid, så dette er ufarlig.
