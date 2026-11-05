# Case 1 #2146: tall_tabell og terskeltabell målt på MOT mot styret (58), ikke avvik (66)

**Gjort (ingen modellendring):**
- `arbeid/hack/c1/lag_tall_tabell.py` bruker nå `maaler_offisiell_v3.py --score mot` og leser linja «MOT mot styret». Bootstrap-KI-et regnes på samme mål, og punkt-F1 er kontrollert lik målerens for alle rader. PR-AUC er merket «(avvik)», for måleren har ingen MOT-sannsynlighet. Overskrifta sier «58 stemmer MOT mot styret; 66 avvik inkl. AVSTÅ er ikke hovedtallet».
- `arbeid/hack/c1/terskeltabell.py`: fasiten er MOT mot styret (nbim_vote MOT og against_board 1). Et flagg teller som MOT bare der styret ikke sier MOT, slik v3 gjør. Terskler og bånd er fortsatt låst på val.
- Begge .md-filene er generert på nytt.

**Kontroll:**
- `tall_tabell.md`, #2044: TEST F1 0,476, P 0,44, R 0,52, KI [0,37; 0,59], 68 flagget. Dette er likt hovedtallet (TP 30 FP 38 FN 28).
- `terskeltabell_ut.md`, 0 % til menneske: test P 0,441, R 0,517, F1 0,476 og val F1 0,520. Begge er like kravresponsen. MOT i fasit: 99 i val, 58 i test.
- `66` står nå bare som «avvik inkl. AVSTÅ … ikke hovedtallet».
- `c1_tallvakt.py` på de to filene gir 2 påstander, 0 avvik, OK. Vakta i fremmed.sh skanner bare levering/*.md og c1/leveranse/*.md, og de filene er ikke endret.

**Funn til ordføreren (ikke min fil, ikke rettet):** standardkjøringen av `c1_tallvakt.py` gir **22 avvik** i pakka. Alle gjelder andelen «til menneske»: tekstene sier 188 av 1578 (11,9 %) eller 183 av 1539, mens `kjor_agent_real_test2026.txt` nå sier 228 av 1578 (14,4 %) eller 223 av 1539 (14,5 %). Det gjelder BEGRENSNINGER, README (begge), BESLUTNINGSSTOTTE, EN_SIDE, JURYSVAR, JURY_SPORSMAL og KRAVRESPONS. Trolig skyldes det at det kalibrerte båndet (#2148) har endret agentens kjøring. Enten må tekstene rettes, eller så må kjøringen rulles tilbake før frys kl. 16.

Nye tabeller lages med `python3 -I arbeid/hack/c1/lag_tall_tabell.py` og `uv run --project arbeid/oppgave_2023 python arbeid/hack/c1/terskeltabell.py --ut arbeid/hack/c1/terskeltabell_ut.md`.
