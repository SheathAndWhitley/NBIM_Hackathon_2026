# Case 1: lim-inn-fanen i demoen kjører nå den ekte agenten (#2335)

**Hva:** `arbeid/hack/levering/demo/ekte_agent.py` (ny) skriver de innlimte sakene (real_votes-format) til en CSV og
kjører `arbeid/hack/levering/kjor_agent.py --csv` som egen prosess i agentens låste miljø
(`uv run --frozen --project arbeid/kandidater/smed2_c1_mot`, eller `DEMO_AGENT_PYTHON`). Dette er samme kall som
demo.sh/fremmed.sh, bare med --csv. `app.py`: fanen «Lim inn saker (ekte agent)» viser anbefaling, P(MOT), ruting med
grunn, NBIM-retningslinje og tidligere NBIM-begrunnelse. Møte-fanen heter nå «Eldre N-PX-møte (forenklet stubb)» og
peker til demo.sh. README og topptekst er rettet.

**Akseptkrav:**
- Samme svar som demo.sh: demo.sh sine tre saker (2084790|5, 2097662|16, 2097662|18) er kjørt i fanen, både med
  Streamlit AppTest (klikk på Anbefal) og fra kommandolinja. Alle 19 felt i agent.csv er **identiske** med den kalde
  kopien fra demo.sh (/tmp/c1_demo_kald/ut/agent.csv, 14:43). Bevis: `arbeid/oppgave_2335/apptest_svar.json`,
  `fane_svar.jsonl`, `tre_saker.csv`.
- Frysvakta: `c1_frys.py sjekk` gir utgang 0 (frysen er ikke tatt ennå, den kommer kl. 16). Ingen av de 17 filene i
  FILER er endret etter 14:45. Jeg har bare endret filer i `levering/demo/`, og ingen av dem står i frysvaktas liste.

**Begrensning:** fanen krever saker med feltene meeting_id, item_no, company_id, meeting_date, proposal_text,
proposal_type og proponent. Fri tekst uten disse feltene avvises med en tydelig feilmelding (agenten trenger
selskapshistorikk). En kjøring tar ca. 5 s.
