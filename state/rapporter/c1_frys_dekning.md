# Case 1: låser frysen alle filer agenten bruker? (#2337, arkitekt)
Metode: kjor_agent.py fra kald kopi (fremmed.sh, /tmp/frys2337) og fra landsbymappen under audit-hook (open, import, subprocess): arbeid/oppgave_2337/spor.py, lister i lest_land.tsv / lest_kald.tsv.
| lest fil | i FILER før | nå |
|---|---|---|
| levering/kjor_agent.py, c1_real.py, injeksjon_hoflig.py, oppgave_2044/train.py, real_votes.csv | ja | ja |
| levering/retningslinje_oppslag.py (sitat) | NEI | ja |
| hack/c1/retningslinjer/punkter.jsonl (sitat) | NEI | ja |
| hack/c1/data_off/real_test_input.csv (inn-sakene) | NEI | ja |
| hack/c1/maaler_offisiell_v2.py (subprocess, SCORE) / v3 (hovedtall i fremmed.sh) | NEI | ja |
| kandidater/smed2_c1_mot/pyproject.toml + uv.lock (pakkeversjoner i kald kopi) | NEI | ja |
Ikke lest av agenten, men står i FILER (harmløst): pred_miks_h2.csv, full_test.csv, kjor_agent_real_maskin_alene.csv, vern.py, case1_mot.py. c1_forslagsstiller.py er et analyseskript, ikke agent: ikke lagt til.
Endring: bare FILER-lista i arbeid/verktoy/c1_frys.py, 10 -> 17 filer. Frysen er ikke tatt ennå, så LaunchAgent kl. 16 bruker den nye lista.
Prøve: C1_FRYS=/tmp/c1_frys_2337.json frys + sjekk GRØNN (17 filer); sluttsjekk.sh GRØNN, HOVEDTALL F1 MOT 0.476190 = kv hack_levert (39 s). state/c1_frys.json ikke rørt (finnes ikke).
