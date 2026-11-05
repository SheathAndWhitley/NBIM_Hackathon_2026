# Case 1: lim-inn-fanen gir samme svar som kjor_agent fra kommandolinja (#2344, uavhengig sjekk av #2335)

**Svar: ja.** For 10 saker er anbefaling, P(MOT), til menneske og rutingsgrunn like i fanen og på kommandolinja.
Alle 19 felt er identiske når fanen og kommandolinja får de samme sakene. 0 avvik.

**Slik:** Streamlit AppTest på `arbeid/hack/levering/demo/app.py`. Jeg limte teksten inn i fanen «Lim inn saker (ekte agent)»,
klikket på Anbefal og leste `session_state["ekte"]`. Det ga 10 rader, ingen feilmelding, og tabellen viste 10 rader.
Kommandolinja er `kjor_agent.py` i det låste miljøet (`smed2_c1_mot`) på tre måter: hele test 2026 (standard),
`--csv` med de samme 10 sakene, og `--sak` for hver av de rare sakene alene. De rare sakene ble også kjørt alene i fanen.
De 8 testsakene er trukket med seed 2344: 2 MOT, 2 til menneske, 2 FOR, 1 med injeksjon og 1 der styret ikke anbefaler FOR.
De 2 rare er tom forslagstekst og et oppdiktet selskap (company_id 999999999, Norge, type REMUNERATION).

| sak | CLI-svar (kilde) | P(MOT) CLI | fane-svar | P(MOT) fane | til menneske CLI/fane | rutingsgrunn (fane) |
|---|---|---|---|---|---|---|
| 2084790\|4 | MOT (hele test) | 1.0 | MOT | 1.0 | 0/0 | |
| 2068788\|4 | MOT (hele test) | 1.0 | MOT | 1.0 | 0/0 | |
| 2040176\|5 | MOT (hele test) | 0.5217 | MOT | 0.5217 | 1/1 | usikker: P(MOT) i båndet [0,15, 0,85) |
| 2035238\|3 | FOR (hele test) | 0.0896 | FOR | 0.0896 | 1/1 | ukjent selskap |
| 2071193\|6 | FOR (hele test) | 0.0455 | FOR | 0.0455 | 0/0 | |
| 2064275\|7 | FOR (hele test) | 0.0 | FOR | 0.0 | 0/0 | |
| 2094542\|10 | FOR (hele test) | 0.0455 | FOR | 0.0455 | 1/1 | instruksjonslignende tekst |
| 2040922\|1 | FOR (hele test) | 0.0372 | FOR | 0.0372 | 0/0 | |
| 9900001\|1 (tom tekst) | FOR (--sak) | tom | FOR | tom | 1/1 | kan ikke vurderes: mangler felt: proposal_text |
| 9900002\|1 (ukjent selskap) | FOR (--sak) | 0.0455 | FOR | 0.0455 | 1/1 | ukjent forslagstype; ukjent selskap; ukjent land/marked |

**Felt for felt (19 felt per sak):**
- Fanen med 10 saker mot `kjor_agent --csv` med de samme 10 sakene: 0 avvik.
- Fanen alene mot `--sak` alene, for hver av de to rare sakene: 0 avvik.
- Fanen mot kjøringen på hele test: anbefaling, P(MOT), ruting og sitat er like. Bare `raa_score` avviker, i 4 av 8 saker,
  med høyst 0,00003 (for eksempel 0,84857 mot 0,84854). Det ligger ikke i fanen. Kommandolinja med bare de 8 testsakene
  gir 0 avvik mot hele test, så avviket kommer av at den oppdiktede saken er med i samme kjøring.
  - Årsak: `arbeid/oppgave_2044/train.py:92` regner `raa_score` som et rangsnitt (`rank(pct=True)`) over alle rader. Det er
    historikken pluss nye saker uten etikett. En ny sak i kjøringen flytter derfor prosentrangen til alle andre saker litt,
    omtrent 1/13 757. I disse 10 sakene endret ikke det P(MOT) med 4 desimaler, og ingen beslutning endret seg.
  - Risiko: en sak som ligger nøyaktig på grensa kan i prinsippet få et annet svar når den kjøres sammen med nye saker,
    i fanen eller på kommandolinja. Agentfilene er ikke endret. Dette er et tema for jurysvaret om robusthet, ikke en feil i fanen.

**Annet:** Fanen bruker 5 s per kjøring. Saken med tom tekst får anbefalingen FOR (følger styret) og går til menneske,
som den skal. Kjøringene la én linje per sak i demoens `logg/` (12 linjer), slik fanen alltid gjør.

**Bevis:** `arbeid/oppgave_2344/` har `ti_saker.csv`, `fane_*.json` (fra AppTest), `cli_*/agent.csv` og `sammenligning.md`.
Kjør på nytt med `fane_apptest.py` og `sammenlign.py` (kommandoene står øverst i hvert skript).
