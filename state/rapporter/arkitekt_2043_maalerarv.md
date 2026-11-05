# #2043: Hack-oppgaver arver casens nye måler (fiks i tavle.py, commit 6dbfd42)

**Feilen:** Rundens måler (`hack_maaler_aktiv`, 11:14) var eldre enn `hack_start` (11:42), så den gjaldt ikke lenger.
Dommeren setter casens måler på «Case 1: …»-oppgaver (#2034). Bare oppgaver med tittel Hack/Reserve kunne bli rundens måler
eller arves fra, så #2023 fikk «ingen måler å arve». Feilet automåling fikk et merke, og forsøket ble derfor aldri prøvd igjen.

**Fiks:**
1. Måler satt på en «Case …»-oppgave fra denne runden (id >= `hack_start.fra_id`) blir rundens måler hvis ingen er satt (som Hack/Reserve fra før).
   Eldre Case-oppgaver telles ikke med. `--aktiv` overstyrer som før.
2. Uten aktiv måler arver Hack-oppgaven fra rundens nyeste Hack/Reserve/Case-oppgave som har måler.
3. `forsok-vakt` måler også forsøk fra runden der automålingen feilet bare fordi måleren manglet («ingen måler å arve» / «ingen egen måler»).
   Den kjøres automatisk i bakgrunnen når rundens måler settes.

**Test:** `uv run python arbeid/oppgave_2043/test_arv.py` med dummy-oppgaver i en midlertidig database ga «OK: alle 5 sjekker».
`import worker, tavle` virker.

**Nå:** smed2s forsøk #1030–1033 (#2023) venter. De blir målt så snart dommer2 setter måler på #2034, uten noe ekstra steg.
Kommer målingen ikke i gang: `uv run python tavle.py forsok-vakt --av dommer`.
Forsøk fra eldre runder (#960–962) er holdt utenfor med vilje, fordi de ikke skal måles med en annen cases måler.
