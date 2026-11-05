# Case 1 #2159: tallvakta gir 0 avvik. Det var loggen som var gammel, ikke tekstene

**Funn:** De 22 avvikene kom av at `levering/kjor_agent_real_test2026.txt` var en lagret logg fra en kjøring med det **gamle ukalibrerte båndet**. Linje 3 sa «10 %-bånd 0.9459 logit», og loggen ga 228 av 1578 (14,4 %) til menneske. Dagens kode med kalibrert bånd (#2148, P(MOT) i [0,15; 0,85)) gir **188 av 1578 (11,9 %)** og 183 av 1539 med fasit (11,9 %). Det er de tallene tekstene allerede sier.

**Gjort (ingen modellendring, ingen tekst endret):**
- Kjørte agenten fra kald mappe to ganger (`kjor_agent.py --ut ...`). Begge ga byte-lik agent.csv, MOT 74 og SCORE 0.481752, det samme som den gamle loggen. Bare rutingen skilte.
- La agentens egen `KJORING.txt` (13:04:11) inn som `levering/kjor_agent_real_test2026.txt`. Den gamle loggen ligger i `arbeid/oppgave_2159/kjor_agent_real_test2026_GAMMEL_ukalibrert.txt`.
- `levering/kjor_agent_real_maskin_alene.csv` er byte-lik ny `_pred_uten_ruting.csv`.
- `menneske_tabell.py` på ny agent.csv gir samme tabell som README, JURYSVAR og BESLUTNINGSSTOTTE: standardrad 183 av 1539, 32 av 58 MOT, øvre grense F1 0,828 og gulv 0,269.

**Kontroll:** `python3 -I arbeid/verktoy/c1_tallvakt.py`: 13 filer, 129 påstander, 0 avvik, OK.

**NB:** Loggfila er ikke i git. Hvem som overskrev den med en gammel kjøring (12:38), er ukjent. Endrer #2152 rutingen, må #2158/#2162 lagre `KJORING.txt` på nytt og kjøre tallvakta.
