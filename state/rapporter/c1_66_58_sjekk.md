# Case 1: sjekk av 66 mot 58 MOT i pakka (#2156, dommer2)

**Dom: GODKJENT på akseptkravet.** 0 steder i pakka kaller 66 «MOT mot styret».

## Grep (README, BESLUTNINGSSTOTTE, JURYSVAR, EN_SIDE, KRAVRESPONS, c1_v1/kravrespons)
- Alle forekomster av 58 er «MOT mot styret» (hovedtallet, TP 30 FP 38 FN 28).
- Alle forekomster av 66 er «avvik», «avvik inkl. AVSTÅ» eller «ikke de 66 avvikene», og står som sidetall (0,4818).
- Regex for «66 MOT», «MOT … 66», «66 … mot styret»: bare to treff, begge riktige
  (KRAVRESPONS:56 og BESLUTNINGSSTOTTE:40, «58 MOT mot styret (66 avvik inkl. AVSTÅ)»).
- Måleren v3 bekrefter oppdelingen: 66 avvik = 58 MOT mot styret + 5 AVSTÅ + 3 andre avvik
  (BESLUTNINGSSTOTTE:5 er riktig). 71 avviksflagg = 68 MOT-mot-styret-flagg + 3 der styret sa MOT,
  så FP 38 på både avvik og MOT henger sammen.
- Reprodusert: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/hack/levering/kjor_agent_real_maskin_alene.csv test --data real --score mot`
  gir F1 0,4762, TP 30 FP 38 FN 28 (58 i fasit). Samme som pakka.

## Tallvakta: FEIL, men ikke på 66/58
`c1_tallvakt.py` sier 107 påstander stemmer, 22 avviker. **Alle 22 gjelder «til menneske»**, ingen gjelder F1 eller 66/58.
- Tallvakta leser standardloggen `levering/kjor_agent_real_test2026.txt`, som er fra kl. 12.29 med det gamle **10 %-båndet**
  (228 av 1578, 14,4 %). Pakka oppgir det nye kalibrerte båndet [0,15; 0,85) (#2132): 188 av 1578, 183 av 1539 (11,9 %).
  Loggen i pakka er altså utdatert, og `kjor_agent_real_test2026_LES.md` forklarer fortsatt 228/14,4 %.
- Min kjøring nå (13.03, `kjor_agent.py --ut /tmp/d2_2156`): agentens linje sier **222 av 1578 (14,1 %)**, mens måleren
  med ruting sier 183 av 1539 (11,9 %). `c1_real.py` ble endret 13.02 (smed, #2152, nye menneske-vakter), så 222 er
  trolig de nye vaktene. 188 kan ikke reproduseres akkurat nå fordi koden er i endring.

## Må gjøres (ikke min oppgave å rette)
1. Etter #2152: kjør agenten på nytt, legg ny `kjor_agent_real_test2026.txt` i levering, og oppdater «til menneske»-tallene
   (README:29/41/47, JURYSVAR:33/39, BESLUTNINGSSTOTTE:18/24/43, EN_SIDE:26, KRAVRESPONS:13, JURY_SPORSMAL:42) og `_LES.md`.
   Hører naturlig til #2155/#2158.
2. Kjør `uv run python arbeid/verktoy/c1_tallvakt.py` igjen etterpå; den skal gi OK uten `--kjoring`.
3. `c1_v1/kravrespons.md` sier 228 av 1578 (14,4 %, «standard 10 %»): gammel versjon, merk «eldre» eller fjern fra pakka.
