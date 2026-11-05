# Case 1: reserveplan for demoen, vist fra kald kopi (#2191, smed, 05.11 13.16–13.25)

**Levert:** `arbeid/hack/levering/demo/RESERVE.md` (feiltabell + kommandoer) og `arbeid/hack/levering/demo/reserve/`:
- `lag_reserve.sh`: kjører begge manus-skriptene, fremmed.sh (kald kopi) og demo_vis.py, lagrer utskrift + csv + SHA.txt (64 s).
  Skriver ikke over `c1/leveranse/demo_utskrift.txt`.
- `vis_reserve.sh [1-4]`: viser lagret utskrift med «RESERVE … laget <tid>» øverst. Bare `sh` og `cat`.
- 4 utskrifter (117 linjer), `csv/` med agentens svar for demosakene og hele test 2026.

**Akseptkrav, vist fra kald kopi:** reservemappa kopiert inn i fremmed.sh-mappa `/tmp/c1_res_kald`, kjørt med
`env -i PATH=/usr/bin:/bin sh /tmp/c1_res_kald/reserve/vis_reserve.sh` fra /tmp: exit 0, 0,02 s, 122 linjer, alle 4 deler.
Innhold: HOVEDTALL F1 MOT 0,476190 (TP 30 FP 38 FN 28), TALLVAKT GRØNN (139 påstander, 0 avvik), til menneske 183/1539.
Sak 1–6 er byte-lik med #2184-kjøringen (seed 17, samme 6 saker).

**Tregeste steg:** fremmed.sh-kjøringen i kald kopi, 37 s (agenten i ny .venv), mot 5,6 s i landsbymappen.
Ikke rettet i kode: fremmed.sh er frysvakt og verifiseringsvei for #1972, og en endring nå er større risiko enn 30 s.
Fiks i manus i stedet: start skriptet i bakgrunnen ved 0:00 (står i RESERVE.md).

**Modell/prediksjoner ikke rørt.** kjor_agent.py sha 638d5fea…8b17; frysvakta var ikke satt ennå (13.18).
**Må gjøres etter frys kl. 16 (#1975):** kjør `lag_reserve.sh` på nytt, ellers er reserven fra før frys.
