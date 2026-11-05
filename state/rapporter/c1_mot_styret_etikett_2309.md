# Case 1: mot_styret-etiketten i agent.csv rettet (#2309)

- Feil: `c1_real.py` brukte samme felt for «avvik fra styret» og `mot_styret`. Når styret anbefalte MOT og agenten sa FOR, ble `mot_styret=1`.
- Retting (kun `arbeid/hack/levering/c1_real.py`, før frys kl. 16): `mot_styret = anbefaling MOT og styret != MOT` (måler v3-definisjonen). Avviket ligger i et internt felt `avvik` som skrives ikke til agent.csv, og det er det `pred_maaler.csv` og `_pred_uten_ruting.csv` bygges fra som før.
- Bevis: kjørte `kjor_agent.py --ut` med gammel og ny c1_real.py. `pred_maaler.csv` og `_pred_uten_ruting.csv` er byte-like (cmp), og også like lagret `kjor_agent_real_pred_maaler.csv`. Agent.csv er forskjellig i nøyaktig 3 celler: `mot_styret` 1→0 for 2045311|16, 2066391|14, 2086078|6. Ingen MOT-anbefaling mot styret har `mot_styret=0`. SCORE er uendret (0,481752 i begge kjøringene, samme måler).
- Logglinja i KJORING.txt sier nå «avvik fra styret 74, av dem MOT styret 71 (med NBIM-sitat 71)» i stedet for «MOT styret 74».
- Til speider (#1975): KRAVRESPONS.md linje 60 siterer «74/74 MOT hadde sitat» fra #2053. Det riktige tallet er 71 MOT mot styret (+3 FOR mot styrets MOT).
- Frysvakta: c1_real.py får ny sha. Frysen kl. 16 tar sha av den nye fila, så den skal ikke gi avvik.
