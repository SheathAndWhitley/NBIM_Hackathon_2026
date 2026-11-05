# Case 1: stemmer p_mot? Kalibreringstabell på test 2026 (smed2 #2015)

**Kort:** Ja, innenfor støyen. Når agenten sier p_mot rundt 0,4–0,6, er det MOT i omtrent like stor andel av sakene. Ingen gruppe bommer utenfor sitt 95 %-intervall. Ingen trening; bare måling.

**Hva er målt:** `kjor_agent.py` (variant b, frosset kode) kjørt fra kald start 05.11 kl. 11.4x på holdout 2026, 1246 saker, 129 MOT (10,4 %). Samme kjøring gir SCORE 0,474286 som før, så det er samme agent. p_mot er den isotoniske P(MOT) agenten skriver i `agent.csv`. Intervallet er 95 % klyngebootstrap på selskap (2000 trekk), fordi saker i samme selskap henger sammen.

| p_mot | saker | snitt p_mot | andel MOT i fasit | 95 % intervall | agenten sier MOT | til menneske |
|---|---|---|---|---|---|---|
| 0,00–0,05 | 704 | 0,024 | 0,028 (20) | 0,017–0,041 | 0 | 0 |
| 0,05–0,10 | 107 | 0,072 | 0,093 (10) | 0,041–0,148 | 0 | 0 |
| 0,10–0,20 | 286 | 0,108 | 0,101 (29) | 0,068–0,139 | 72 | 119 |
| 0,20–0,40 | 59 | 0,367 | 0,322 (19) | 0,203–0,444 | 59 | 0 |
| 0,40–1,00 | 90 | 0,615 | 0,567 (51) | 0,456–0,667 | 90 | 0 |

Kontroll med fem like store grupper (kvintiler): ECE 0,010. Brier 0,070 mot 0,093 for å gi alle saker 10,4 % (lavere er bedre).

**Tre ting forvalteren må vite:**
1. **Den grove skalaen stemmer, men den er grov.** Isotonisk kalibrering gir trappetrinn: bare 37 ulike verdier. 166 saker har nøyaktig p_mot 0,114, og 117 har 0,100. Innenfor et trinn skiller p_mot ikke sakene; det er rå score som avgjør MOT/FOR og ruting.
2. **Grensen for MOT ligger på p_mot ≈ 0,114.** Et MOT-flagg betyr altså ikke "trolig MOT", men "klart mer sannsynlig enn vanlig" (vanlig er 10 %). Per bunke på test 2026:
   - MOT, ikke rutet: 171 saker, snitt p_mot 0,465, ekte MOT 42,7 %.
   - MOT, rutet til menneske: 50 saker, alle p_mot 0,114, ekte MOT 20,0 %.
   - FOR, rutet til menneske: 69 saker, alle p_mot 0,114, ekte MOT 11,6 %.
   - FOR, ikke rutet: 956 saker, snitt p_mot 0,042, ekte MOT 4,0 %.
3. **Intervallene er brede over 0,2.** Bare 149 saker og 70 MOT ligger der. "0,6" kan like gjerne være 0,45 eller 0,67.

**Begrensning:** ett år (2026) og en modell. Kalibreringen er lært på historikken før 2026; skifter NBIM praksis, sklir den. Følg med på andelen avviste flagg (BESLUTNINGSSTOTTE, "Tilbakefall").

**Kjør på nytt:** `uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/x` og deretter `arbeid/kandidater/smed2_c1_mot/.venv/bin/python -I arbeid/oppgave_2015/kalib.py /tmp/x/agent.csv arbeid/hack/c1/data_v3`. Utdata: `arbeid/oppgave_2015/kalib.txt`, `agent_test2026.csv`.
