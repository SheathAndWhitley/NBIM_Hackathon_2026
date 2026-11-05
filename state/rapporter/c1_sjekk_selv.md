# Case 1: ett skript lar en dommer sjekke treffsikkerheten selv (smed2 #2206, ordre #241)

Svaret til guden: kjøres programmet nå, får det **accuracy 95,7 %**. Det er ikke 97 %, og det er heller ikke
tallet som teller. Følg styret får 96,2 % accuracy og finner null stemmer mot styret. Hovedtallet er **F1 0,476 på MOT**
(recall 51,7 %, presisjon 44,1 %).

Kommando (fra landsbymappen eller roten av en kald kopi fra `fremmed.sh`):

    sh arbeid/hack/levering/sjekk_treffsikkerhet.sh [UTMAPPE]

Skriptet gjør dette:
- kjører `kjor_agent.py` på hele test 2026 fra rådata og skriver ny prediksjonsfil til /tmp
- teller 2x2 selv, rett mot fasit i real_votes (`nbim_vote`, `against_board`), uten å bruke måleren eller pakkas tellekode
- sammenligner sha256 av ny `pred_maaler.csv` med den frosne `b113b545…3653`

Utgangskoder: 0 = stemmer, 3 = annen 2x2, 5 = annen sha, 2 = agenten feilet.

Kjøringer 05.11 ca. 13.25 (utgang 0 begge ganger):

| | landsbymappen | kald kopi (`fremmed.sh /tmp/fremmed_2206`, `env -i`) |
|---|---|---|
| 2x2 | TP 30 FP 38 FN 28 TN 1443 | TP 30 FP 38 FN 28 TN 1443 |
| accuracy agent / følg styret | 0,9571 / 0,9623 | samme |
| MOT recall / presisjon / F1 | 0,5172 / 0,4412 / 0,4762 | samme |
| til menneske | 188 av 1578 inn, 183 av 1539 med fasit | samme |
| sha256 mot frossen | LIK | LIK |
| tid | 10 s | 6 s (+49 s for selve kopien og uv sync) |

Avvik underveis, forklart: første versjon telte agentens `mot_styret` (avvik i begge retninger) og fikk FP 41 / TN 1440.
De tre ekstra sakene (2045311|16, 2066391|14, 2086078|6) er aksjonærforslag der styret sier MOT, og der både agenten
og NBIM stemte FOR. Det er avvik i FOR-retning, og etter fasitdefinisjonen er det ikke «MOT mot styret». Skriptet bruker
nå samme definisjon som fasit (agenten sier MOT der styret ikke sier MOT) og får 30/38/28/1443.

Endringer: ny `arbeid/hack/levering/sjekk_treffsikkerhet.sh`, `fremmed.sh` kopierer den nå med, og README har fått
avsnittet «Sjekk tallene selv». Ingen modellendring.

Funn utenfor oppgaven: tallvakta melder nå 3 avvik i `arbeid/hack/c1/leveranse/JURY.md:15` (228 til menneske / 14,4 % /
P 0,69, mens måleren sier 188 / 11,9 % / 0,4412). Linja ble endret av noen andre etter kald kopi 13.24. Jeg har ikke rørt den.
