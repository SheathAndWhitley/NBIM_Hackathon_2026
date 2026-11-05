# Case 1: hvor bommer maskinen? Feil per sakstype på test 2026 (smed2 #2031)

Bare måling, ingen trening. Frosset agent fra kald kjøring 11:43 (`fremmed.sh`, 10 % til menneske, F1 0,474,
byte-lik standardkjøringen i #2029). Test 2026: 1246 saker, 129 MOT. Bom = tapt MOT (fasit MOT, agenten sier FOR)
+ falsk MOT (fasit FOR, agenten sier MOT). Agentens svar telles også for rutede saker (maskinen alene).
Totalt 184 bom: 46 tapte og 138 falske.

**Kategori og kilde deler ikke noe her:** alle 1246 testsakene er `SECTION 14A SAY-ON-PAY VOTES` fra `ISSUER`
med styret FOR (data_v3). Derfor deler jeg også på undertype, selskapets stemmehistorikk hos NBIM og ruting.
Arrangørens rettede NPX-data (flere kategorier, aksjonærforslag) er ikke med; der må tabellen lages på nytt.

| Gruppe | Saker | MOT | Flagg | Tapte MOT | Falske MOT | Bom (andel av gruppa) | Andel av alle bom | R | P |
|---|---|---|---|---|---|---|---|---|---|
| **Alle** | 1246 | 129 | 221 | 46 | 138 | 184 (14,8 %) | 100 % | 0,64 | 0,38 |
| Kategori say-on-pay / kilde ISSUER | 1246 | 129 | 221 | 46 | 138 | 184 (14,8 %) | 100 % | 0,64 | 0,38 |
| Undertype: vanlig say-on-pay | 1200 | 114 | 190 | 41 | 117 | 158 (13,2 %) | 86 % | 0,64 | 0,38 |
| Undertype: fallskjerm (golden parachute) | 46 | 15 | 31 | 5 | 21 | 26 (56,5 %) | 14 % | 0,67 | 0,32 |
| Historikk: nytt selskap | 109 | 19 | 30 | 7 | 18 | 25 (22,9 %) | 14 % | 0,63 | 0,40 |
| Historikk: tidligere bare FOR | 979 | 55 | 73 | **39** | 57 | 96 (9,8 %) | 52 % | **0,29** | 0,22 |
| Historikk: tidligere MOT | 158 | 55 | 118 | 0 | **63** | 63 (39,9 %) | 34 % | 1,00 | 0,47 |
| Ikke rutet | 1127 | 111 | 171 | 38 | 98 | 136 (12,1 %) | 74 % | 0,66 | 0,43 |
| Rutet til menneske | 119 | 18 | 50 | 8 | 40 | 48 (40,3 %) | 26 % | 0,56 | 0,20 |

Etter maskinens p_mot: under 0,1 er 811 saker med 30 tapte MOT (alle vanlig say-on-pay, ingen med MOT-historikk).
Mellom 0,3 og 0,5 holder bare 42 av 112 flagg (P 0,38). Over 0,7 holder 28 av 35 (P 0,80).
Ruting fungerer som tenkt: 9,6 % av sakene står for 26 % av bommene, og presisjonen der er 0,20.

**Hvor forvalteren ikke bør stole på maskinen:**
1. Selskaper der NBIM tidligere har stemt MOT: maskinen gjentar i praksis fjorårets MOT (118 flagg på 158 saker),
   men bare 55 av 158 ble MOT igjen. Et MOT-flagg her er et minne, ikke et funn, og må sjekkes mot årets lønnsplan.
2. Selskaper der NBIM alltid har stemt FOR: her ligger 39 av 46 tapte MOT. Maskinen ser nesten ingen nye MOT
   (R 0,29), så et FOR her betyr «ingen historikk sier noe», ikke «trygt».
3. Fallskjerm-avstemninger ved oppkjøp: 26 av 46 saker bommer (57 %), mest falske MOT. Disse bør alltid til menneske.
   Det samme gjelder flagg med p_mot under 0,5, der under 4 av 10 holder.

Tallene er fra ett testår og små grupper (fallskjerm 46 saker, 15 MOT), så andelene har stor usikkerhet.

Kjør på nytt: `uv run --with tabulate python -I arbeid/oppgave_2031/feil_per_type.py` (alle tabeller i
`arbeid/oppgave_2031/tabeller.md`, agentfila kopiert til `arbeid/oppgave_2031/agent_fremmed_1143.csv`).
