# #2054: «duplikat id» i Case 1-automålingen var feil format, ikke dobbeltnøkler

**Årsak.** `meeting_id|item_no` er unik i begge filene: real_votes har 13 757 rader og 13 757 unike nøkler, npx har 52 906 rader og 52 906 unike nøkler. Smedenes svarfiler (#1030–#1033) har formatet `rad,p` uten `id`-kolonne. `maaler_offisiell.py` leste derfor tom id på alle rader og stoppet på den andre.

**Rettelse (commit ef40284).**
- `arbeid/hack/c1/maaler_offisiell_v2.py` godtar `rad,p`: rad er radnummeret i datafila og oversettes til `meeting_id|item_no`. Avvik regnes når p >= 0,5, og p brukes til PR-AUC. Formatet `id,anbefaling` virker som før. Tom id og duplikat rad gir UGYLDIG med en klar melding.
- `tavle.py`: `forsok-vakt --id N` prøver nå på nytt også når en tidligere automåling feilet, og fjerner det gamle feilmerket. Før ble forsøket hoppet over for alltid.
- Den gamle `maaler_offisiell.py` står urørt (sha e8f70d3904). Bare dommeren kan sette måleren, og en endret fil ville ha brutt rundens måler.
- Test: `uv run python arbeid/hack/c1/test_maaler_v2.py` gir OK.

**Kontrollpunkt.** Forventet 0,481 (smed2s `maaler_ny.py`), fikk 0,481013 med v2 på test 2026: TP 38, FP 54, FN 28. Kjørt ende til ende på en kopi av tavle.db (`forsok-vakt --id 1032`) ble resultatet kilde=maaler med 0,481013.

**NB for dommeren (vindu).** Rundens måler måler `val` (2025). På val gir #1032 **0,664**, og #1033 gir 0,616, mot 0,529 meldt på test. Smedenes meldte tall er test 2026. Val-tallet er trolig optimistisk, fordi grensen er valgt på val. Akseptkravet «nær 0,481» holder bare med testvinduet. Hvilket vindu som er riktig, bestemmer dommeren, ikke jeg.

**#1030 og #1031** er svar på npx-fila. Med `--data real` feiler de riktig («rad 13757 finnes ikke»). De trenger en npx-måler hvis de skal telle.

**Til dommeren (oppgave lagt inn):** `tavle maaler --oppgave 2034 --kmd "python3 -I <repo>/arbeid/hack/c1/maaler_offisiell_v2.py {sti} val --data real" --aktiv --av dommer`, det samme for #2023, og deretter `tavle forsok-vakt --id 1032` og `--id 1033`.
