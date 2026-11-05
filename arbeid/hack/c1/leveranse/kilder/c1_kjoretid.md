# Case 1: kjøretid og minne for stemmeagenten (smed sak 2213)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

Målt 05.11 kl. 13.24 på Mac mini M4, 16 GB, git 4533b7d. Agenten er den frosne miksen miks h2, med `kjor_agent.py` som står nå. Modellen er ikke endret.

| Måling | Tid | Maks minne (RSS) |
|---|---|---|
| Hele `kaldstart.sh` (kopi, uv sync, agent, måler) | 52,2 s | 229 MB |
| ...av dette kopi av leveransen | 6 s | |
| ...av dette `uv sync --frozen` (ny .venv) | 38 s | |
| ...av dette agenten på test 2026 (1578 saker) | 8 s | |
| Agenten alene på test 2026, varm .venv | 4,8 s (ca. 3 ms per sak) | 226 MB |
| Én sak med `--sak`, n = 20 tilfeldige (seed 1) | median 4,35 s, min 4,21, maks 4,95 | 216–220 MB |

- Kaldstarten ble GRØNN: F1 MOT 0,476190 = REF, med samme tall som før. <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
- Alle 20 enkeltkall gikk uten feil (exit 0).
- En enkeltsak tar like lang tid som hele sesongen, fordi agenten trener modellen på nytt fra historikken ved hvert kall. Rådet i drift er derfor å kjøre saker samlet med `--csv`.
- Minnet er høyst 2 % av 16 GB, så det er god margin.
- Hele `kaldstart.sh` målte 229 MB med `/usr/bin/time -l`. Det er det største barneprosessen brukte, ikke summen av alle prosessene.

Rådata: `<arbeidsmappe>/oppgave_2213/kald.log`, `tider.txt` (exit, sekunder, RSS i byte per sak), `saker.jsonl`.
Lagt inn som pkt. 8 i `arbeid/hack/c1/leveranse/BEGRENSNINGER.md`.

Reproduser: `BEHOLD=1 /usr/bin/time -l bash arbeid/hack/c1/kaldstart.sh`, og deretter i tmp-mappa `/usr/bin/time -l <.venv>/bin/python arbeid/hack/levering/kjor_agent.py --sak '<json>' --ut <mappe>`.
