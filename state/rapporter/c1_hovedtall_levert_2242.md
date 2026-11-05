# Case 1: dashbordets hovedtall er nå den leverte agenten (#2242)

**Før:** `server._maltall_live()` valgte høyeste forsøk på rundens måler (v2 avvik-F1, sha 9d81a418dd):
forsøk #1033 (smed2 t4e +NPX, valgt bort på val), 0,529412, acc 95,84 %.

**Nå:** ny kv-nøkkel `hack_levert` = {sti, kmd, navn, forsok, maaler}. Er den satt, blir hovedtallet
den filen målt med sin egen måler (SCORE-linja), og accuracy regnes fra samme kjøring.
Beste forsøk vises fortsatt, men bare som en grå linje: «beste forsøk #1033 0,529 på rundens måler, ikke levert».

Satt til (av arkitekt):
- sti `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` (forsøk #1046, frossen #2044 miks h2)
- kmd `python3 -I .../maaler_offisiell_v3.py {sti} test --data real --score mot` (v3 sha 418a937e57)

**KP:** forventet 0,476190 / 95,39 % / 95,71 % (dommer #2220). Fikk `_maltall_live()` 0,47619, acc 95,39 %,
følg styret 95,71 %. Samme tall fra live-dashbordet på :7682 (`/api/state`) etter omstart.

**Bytte senere** (f.eks. etter modellfrys hvis fila endrer seg):
`uv run python tavle.py levert --sti <fil> --kmd "<måler {sti}>" --navn "..." --forsok <id> --maaler "..." --av dommer`
Uten `--sti` viser den gjeldende verdi. Fila mellomlagres på mtime, så en ny fil måles automatisk.

Endret: server.py (`_levert`, `_maltall_live`), tavle.py (kommando `levert`), dashboard/index.html (tekst).
Testinstansen på :7799 (startet 10:35, ikke gudens) er ikke startet på nytt.
