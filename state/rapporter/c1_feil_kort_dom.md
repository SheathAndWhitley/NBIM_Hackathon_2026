# Case 1: dom over tallene i feilkortet (#2729, kontroll av #2725)

Regnet på nytt av dommeren med eget skript (`python3 -I arbeid/oppgave_2729/kontroll.py`, bare stdlib, bruker ikke feil_per_gruppe-modulen). Kilder: rådata `state/opplastet/20261105_114241_real_votes.csv` (sha 71ba5135…), prediksjoner `arbeid/oppgave_2490/repo4_test.csv`, ruting `arbeid/oppgave_2592/agent.csv`. Regler som måler v3 --score mot: fasit = nbim_vote MOT og against_board 1; agentens MOT = avvik der styret ikke sier MOT. Kald kjøring (agent.csv, mot_styret) og repo4_test.csv er enige om alle 1578 rader (0 uenige).

Én linje per tall:

- TP/FP/FN 32/35/26: OK (32/35/26)
- F1 0,512: OK (0,512; P 0,478, R 0,552)
- 161 til menneske av 1539 (10,5 %): OK (161/1539 = 10,5 %)
- 58 MOT i fasit 2026: OK
- 23 av 35 falske flagg på styrevalg: OK (styrevalg FP 23)
- 11 av 26 oversette på styrevalg: OK (styrevalg FN 11)
- styrevalg F1 0,47: OK (0,469)
- «annet» F1 0,58 og 6 falske flagg: OK (0,578; FP 6)
- 32 av 35 falske flagg gikk til menneske: OK
- 8 av 26 oversette gikk til menneske: OK
- 18 av 26 misser uten varsel: OK (26 − 8 = 18)
- 7 misser uten varsel på styrevalg, 9 på «annet»: OK (11 − 4 = 7; 13 − 4 = 9; resten: lønn 1, aksjonærforslag 1)
- lønn 4 MOT, aksjonærforslag 2 MOT: OK
- F1 2024 0,506 og 2025 0,531 (fra #2718): OK mot `arbeid/oppgave_2567/benk.txt` (repo4: 0,5057 og 0,5309)
- 58–99 MOT-stemmer per år: OK (58, 88, 99)
- 95 % KI 2026 [0,40; 0,62]: OK (klyngebootstrap over møter, frø 2272: 0,396–0,624; frø 1: 0,393–0,621)

Avvik: ingen. Alle 16 tall i `state/rapporter/c1_feil_kort.md` er bekreftet. Smed2 (#2723) kan bruke feilkortet som det står.
