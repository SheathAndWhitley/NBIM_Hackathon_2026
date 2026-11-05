# Case 1: MOT-stemmene har nå et MOT-sitat og en egen grunn (#2009, smed3)

**Feilen:** sitatagenten (smed3_utf_sitat/agent.py) sier FOR i alle 1246 saker, og kjor_agent.py kopierte
sitatet rett inn. Alle 221 MOT-rader fikk derfor «generally will support» og «ingen varselsignal».

**Endringen** (liten og avgrenset, bare i `arbeid/hack/levering/kjor_agent.py`; smed #2000 jobber i samme fil):
- Ny funksjon `mot_sitat()` + konstanter øverst. Brukes bare når modellen sier MOT og sitatagenten fant et sitat
  (rader uten sitat rutes til menneske som før). Modell, grense, ruting og pred_maaler.csv er uendret.
- Punkt (ordrett setning fra punkter.json, kontrollert):
  - PIII Say on Pay ¶5 (styret må ta hensyn til lav støtte) når fondet stemte MOT i forrige sak i selskapet,
  - ¶4 (planstruktur) når viktigste grunn er aksjebasert lønn / CAP-andel / lang forslagstekst,
  - ¶3 (lønn/resultat-kobling) ellers,
  - PIII Additional executive pay matters ¶1 (golden parachutes, 2,99x-regelen) når forslaget gjelder fusjon/fallskjerm.
    Dette er utenfor ¶3–¶5 i bestillingen, men passer bedre for de 31 fusjonssakene.
- Grunn: de tre viktigste grunnene fra smed2s `forklaring.csv` (#2007), slått opp på id.
  Mangler forklaringen (andre inn-filer): «fondet (NBIM) stemte MOT styret i forrige sak i selskapet» regnet fra
  train.csv, ellers «policy åpner for MOT ved svak lønn/resultat-kobling; må vurderes av menneske».
- Ny kolonne til slutt: `uenig_med_sitatagent` (1 når sitatagent_anbefaling != anbefaling).

**Målt fra kald start (holdout 2026, `--ut /tmp/c1_2009`):**
- SCORE 0,474286 (F1 MOT), uendret. Hele systemet med 10 % ruting: F1 0,5723, også uendret.
- 221 MOT-rader: 0 med «ingen varselsignal» eller «generally will support». 0 standardgrunner (alle har forklaring.csv).
  Punkter: ¶5 92, ¶3 49, ¶4 49, fallskjerm ¶1 31. `uenig_med_sitatagent` = 1 på alle 221 MOT-rader, 0 på FOR.
- Reservevei testet (samme saker med nye id-er, så forklaring.csv ikke treffer): 221 MOT, 0 forbudte;
  94 med «stemte MOT i forrige sak», 127 med standardgrunnen.

**Svakheter (ærlig):** forklaring.csv er laget for holdout 2026; for andre inn-filer finnes bare historikk- eller
standardgrunnen. Punktvalget er regelbasert på viktigste kjennetegn, ikke validert mot hva Vanguard faktisk skrev.
Sitatagenten selv er ikke rettet: den sier fortsatt FOR overalt, som nå vises i den nye kolonnen.

Resultat: `arbeid/oppgave_2009/agent.csv`, `KJORING.txt`. Kommando:
`uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut`
