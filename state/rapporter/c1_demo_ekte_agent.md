# Case 1: demoen kjører nå den ekte agenten (H5 tettet, smed #2093)

**Ett kall:** `sh arbeid/hack/c1/leveranse/demo.sh` (ca. 35 s). Lager en kald kopi med `levering/fremmed.sh` (env -i, låste pakker),
kjører `kjor_agent.py` (standard real_votes, frosset modell #2044 miks h2) på hele test 2026, og viser tre saker.
Utskrift: `arbeid/hack/c1/leveranse/demo_utskrift.txt`. Ingen N-PX i utskriften (grep: 0 treff).

- Tall i kopien: F1 MOT **0,4818** (TP 33, FP 38, FN 33, P 0,465, R 0,500), 66 MOT av 1539. Samme som hovedtallet.
- Sakene trekkes med seed 0 blant alle saker i kategorien, sortert på id, ikke håndplukket:
  1. MOT funnet med sitat (24 slike): PT Solusi Sinergi Digital, revisor, Indonesia. Agent MOT 0,99, NBIM Against.
  2. Rutet til menneske (223 slike): Klarna, revisor EY. Grunn: ukjent selskap. NBIM For.
  3. FOR (1265 slike): Red Star Macalline, styrehonorar. NBIM For.
- Ærlig merknad: sitatet i sak 1 er NBIMs egen begrunnelse fra samme selskap i 2025. Det er riktig etter reglene
  (alltid tidligere år, aldri feature), men juryen kan lese det som at agenten «kopierer fjoråret».
- Ruting er 14,5 %, ikke 10 %: båndet ruter 10 % på val, i tillegg kommer ukjent selskap, injeksjon og datafeil.
- Stubben (`levering/demo/`, Streamlit, N-PX) står, men README sier nå øverst at den ikke er juryens demo.
- Ikke rørt: `c1/DEMO_MANUS.md` (speider #1975) bruker `demo_saker_2026.sh` med 5+1 saker. Speider bør velge ett av de to
  skriptene i manus; `demo.sh` er det eneste som går fra kald kopi.
- Avhenger av `fremmed.sh` (smed3 #2094 jobber med den). Brekker den, brekker demoen; demo.sh skriver da loggen.
