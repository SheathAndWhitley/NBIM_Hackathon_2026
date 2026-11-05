# Case 1: kontroll av modellfrysen kl. 16 (#2247)

Kjørt 05.11 kl. 16:03 av smed (automatisk, arbeid/oppgave_2247/kontroll.sh). Referanse: sha-ene i working tree rett etter den kalde kjøringen i #2243 (git 9012a58, arbeid/oppgave_2247/referanse_2243.json).

**Resultat: AVVIK:** sha ulik #2243: real_test_input.csv, maaler_offisiell_v2.py, maaler_offisiell_v3.py, punkter.jsonl, c1_real.py, injeksjon_hoflig.py, retningslinje_oppslag.py, pyproject.toml, uv.lock;

Frys tatt 2026-11-05T16:00:01, modell #2044 miks h2

| Fil | sha256 frosset | lik #2243 |
|---|---|---|
| arbeid/hack/c1/data_off/real_test_input.csv | 1e0e22f86bbf21ea | NEI (ref mangler) |
| arbeid/hack/c1/maaler_offisiell_v2.py | 1111f1afce04f906 | NEI (ref mangler) |
| arbeid/hack/c1/maaler_offisiell_v3.py | 418a937e57e52e56 | NEI (ref mangler) |
| arbeid/hack/c1/retningslinjer/punkter.jsonl | 089ddbddb839d9f3 | NEI (ref mangler) |
| arbeid/hack/levering/c1_real.py | 439b49f7483674e5 | NEI (ref 83fe0eb0de226944) |
| arbeid/hack/levering/injeksjon_hoflig.py | 51cd0698342cfd7b | NEI (ref 150b92e9993fb1a3) |
| arbeid/hack/levering/kjor_agent.py | dedc94062cf414e9 | ja |
| arbeid/hack/levering/kjor_agent_real_maskin_alene.csv | 22ac6717e1287c5a | ja |
| arbeid/hack/levering/retningslinje_oppslag.py | 0a45c013471bd0b1 | NEI (ref mangler) |
| arbeid/kandidater/smed2_c1_mot/pyproject.toml | 96fcf3b1c1089027 | NEI (ref mangler) |
| arbeid/kandidater/smed2_c1_mot/uv.lock | ed54fd6c8f92f347 | NEI (ref mangler) |
| arbeid/oppgave_2044/pred_miks_h2.csv | 40afcc3e2fec85b2 | ja |
| arbeid/oppgave_2044/train.py | 772fb71500e397cc | ja |
| arbeid/oppgave_2046/case1_mot.py | d403dd3c8f3b5876 | ja |
| arbeid/oppgave_2047/vern.py | 19c3629fa670ffd8 | ja |
| arbeid/oppgave_2103/full_test.csv | 69702192d3a4309e | ja |
| state/opplastet/20261105_114241_real_votes.csv | 71ba5135e7ba9d64 | ja |

| Sjekk | Resultat |
|---|---|
| c1_frys.py sjekk --krev | utgang 0: FRYSVAKT GRØNN: 17 filer like som ved frys 2026-11-05T16:00:01 |
| kaldstart.sh etter frys | utgang 0 |
| F1 MOT (måler v3 --score mot, sha 418a937e57) | 0.476190 (ventet 0.476190) |
| pred_maaler.csv sha256 | b113b545dd86b263bba78ea9ddb16f0580363d34e6718be66c1218025a783653 (ventet b113b545…3653) |

Siste linje fra kaldstart: `GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000 (grense 0.005) tid 58s`. Full logg: arbeid/oppgave_2247/kaldstart_etter_frys.log.
