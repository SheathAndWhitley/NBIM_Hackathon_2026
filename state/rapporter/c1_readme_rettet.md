# Case 1: README-uklarhetene fra #2416 rettet i jury-README (#2430)

Fil: `arbeid/hack/levering/JURY_README.md` (blir rot-README.md i zipen via pakk_jury.sh linje 29). Commit `445e428`. Bare tekst.

- **(1)** Ny setning: linja `IKKE HOVEDTALL` er en sjekk med test-fordelingen, ikke resultatet.
- **(2)** Egne saker: id-ene må være heltall + heltallseksemplet fra #2416. Eksemplet krever `--ut` (obligatorisk argument; manglet i rapportens versjon), lagt til `--ut ut_egen`. Kjørt nå: p_mot 0.5217, til_menneske=1, retningslinje NBIM 5.3.1.
- **(4)** «1,5 GB» var feil: #2417 (`c1_tom_cache.md`) testet tom uv-cache og tom Python: ~230 MB pakker + ~70 MB Python, 3–4 s uv sync, samme hovedtall. README sier nå det. «python3 (3.10+)» fjernet: pyproject krever >=3.13, og uv henter Python selv.
- Ingen andre «1,5 GB» i leveranse/ eller levering/*.md.

**Tallvakt:** `c1_tallvakt.py` GRØNN, 18 filer, 168 påstander stemmer, 0 avvik, utgang 0.

## Diff
```diff
--- /tmp/JURY_README_for2430.md	2026-11-05 15:38:29
+++ arbeid/hack/levering/JURY_README.md	2026-11-05 15:38:09
@@ -5,9 +5,10 @@
 på test 2026 (NBIMs egne stemmer fra arrangøren): **0.476190**. «Følg styret» har F1 0 på MOT.
 
 ## Det du trenger
-macOS eller Linux med `python3` (3.10+) og [uv](https://docs.astral.sh/uv/)
-(`curl -LsSf https://astral.sh/uv/install.sh | sh`). Første kjøring laster ned låste pakker: ca. 1,5 GB (hele utviklingsmiljøet er låst med, også pakker agenten ikke bruker),
-så regn med fra ett til noen minutter avhengig av nettet. Selve kjøringen tar under ett minutt.
+macOS eller Linux med [uv](https://docs.astral.sh/uv/)
+(`curl -LsSf https://astral.sh/uv/install.sh | sh`). Første kjøring trenger nett én gang og laster ned ca. 230 MB låste pakker
+(pluss ca. 70 MB Python hvis uv ikke finner Python 3.13+; uv henter den selv). Testet fra tom uv-cache og uten Python i #2417:
+3–4 sekunder på vår linje, samme hovedtall; en tregere linje bruker lengre tid. Selve kjøringen tar under ett minutt.
 
 ## Kjør (ord for ord)
 1. `unzip jurypakke_c1.zip`
@@ -21,6 +22,7 @@
     TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring
 
 `SCORE`-linjene midt i utskriften er avvik fra styret inkludert AVSTÅ (sidetall, 0.481752), ikke hovedtallet.
+Linja som starter med `IKKE HOVEDTALL` er en sjekk med test-fordelingen, ikke resultatet.
 Agentens svar ligger i `ut/` (`agent.csv` med anbefaling, sitat og til_menneske per sak).
 
 4. Uavhengig telling (valgfritt, etter steg 3): `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/c1_sjekk`
@@ -30,6 +32,12 @@
 ## Egne saker
     .venv/bin/python arbeid/hack/levering/kjor_agent.py --help
 
+`meeting_id`, `item_no` og `company_id` må være heltall (ellers går saken til menneske som «kan ikke vurderes»). Eksempel:
+
+    .venv/bin/python arbeid/hack/levering/kjor_agent.py --sak '{"meeting_id":9000001,"item_no":3,"company_id":537900,"meeting_date":"2026-05-01","proposal_text":"Shareholder Proposal Regarding Report on Climate Lobbying","proposal_type":"SHAREHOLDER","proponent":"Shareholder","mgmt_rec":"AGAINST","country":"United States","market":"DM"}' --ut ut_egen
+
+gir (i `ut_egen/agent.csv`) P(MOT) 0,52, sendes til menneske, retningslinje NBIM 5.3.1 sitert.
+
 ## Hva som er hva
 | fil | innhold |
 |---|---|
```
