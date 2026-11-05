# Case 1: hovedtallet 0,476 i hele tall (sak 2467)

Testen 2026 har 58 stemmer der NBIM stemte MOT mot styret. Slik går det:

| Svar | Funnet (treff) | Bommet | Falske alarmer | F1 MOT |
|---|---|---|---|---|
| Agenten (hovedtallet) | 30 av 58 | 28 | 38 | 0,476 |
| Følg styret | 0 av 58 | 58 | 0 | 0,000 |
| Gjenta forrige stemme (samme selskap og tekst fikk MOT før) | 25 av 58 | 33 | 54 | 0,365 |

Med ord: agenten finner 30 av de 58 stemmene mot styret. Den slår alarm 68 ganger, og 30 av dem er riktige (44 %).
«Gjenta forrige stemme» finner 25, men slår alarm 79 ganger og bommer på 54 av dem.

Kommando (fra rotmappa): `.venv/bin/python -I arbeid/oppgave_2467/hele_tall.py`
Skriptet kjører måleren `arbeid/hack/c1/maaler_offisiell_v3.py <svar> test --data real --score mot` og leser linja «MOT mot styret».
Svarfiler: `arbeid/hack/levering/kjor_agent_real_pred_maaler.csv` (svarfila bak hovedtallet i pakka), `arbeid/hack/c1/data_off/real_test_folg_styret.csv`, `arbeid/oppgave_2134/regel_b2_test.csv` (regel b2 fra sak 2134).
Pakka er ikke rørt.
