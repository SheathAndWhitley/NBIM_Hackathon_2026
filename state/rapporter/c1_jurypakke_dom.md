# Case 1: dom over jury-zipen prøvd som jurymedlem (#2348, dommer2, 05.11 kl. 15.15)

**Dom: GODKJENT.** Zipen fra #2346 (`/tmp/jurypakke_c1.zip`, 1,1 MB, 95 filer) gir riktig hovedtall fra en tom mappe
uten tilgang til landsbymappa. Fire avvik under er ikke blokkerende, men ett av dem (punkt 1) bør rettes før frysen kl. 16
fordi det står i kravrespons.md.

## Hva jeg gjorde (README i zipen, ord for ord)
Tom mappe `/tmp/jurydom2348`, tom HOME (`/tmp/juryhome2348`, tom uv-buffer), og `sandbox-exec` som nekter all lesing
og skriving under `<repo>` (kontrollert: `cat mission.md` gir «Operation not permitted»).

| steg | resultat |
|---|---|
| `unzip`, `cd c1_stemmeagent`, `sh KJOR.sh` | utgang 0, 56 s. FRYSVAKT GRØNN (15 filer), **HOVEDTALL 0.476190**, **TALLVAKT GRØNN** (18 filer, 165 påstander, 0 avvik) |
| steg 4, `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh` | **TP 30 FP 38 FN 28 TN 1443: STEMMER**, F1 0,4762, sha256 ny prediksjon = frossen (b113b545…) LIK |
| ordet «landsby» i kjøreloggen | 0 treff |
| `~` i kode (.py/.sh/.toml) | bare `c1_tallvakt.py:22` som standardverdi, overstyrt av `--rot` i KJOR.sh. 7 tekstfiler til (kilder/, demo_utskrift, JURY_README) nevner stien; kjøringen leser dem ikke (sandkassen beviser det) |
| måler v3 mot kilden | eneste diff er datastien (relativ til fila), regnestykket uendret |
| kravrespons, JURY, kilder | `arbeid/hack/c1/leveranse/{kravrespons,JURY,README,BEGRENSNINGER,ERLIG_EVALUERING}.md` og `kilder/` (41 filer) ligger med. Alle stier de nevner finnes i zipen, unntatt `npx_votes.csv` og `arkiv/gammel_data/`, som README selv sier ikke er med |
| ny tom HOME, `uv sync --frozen` uten sandkasse | laster ned 1,5 GB til uv-bufferen, fullfører |

## Avvik (ingen stopper godkjenning)
1. **`leveranse/README.md` og `kravrespons.md` sier «ett kall reproduserer: `bash arbeid/hack/c1/leveranse/kjor.sh`».** I zipen feiler
   det straks: `fremmed.sh: No such file or directory` (`levering/fremmed.sh` og `hack/maaler.sh` er ikke med). Et jurymedlem som
   leser kravresponsen før rot-README får en feil. Rett teksten (zip: `sh KJOR.sh`; repo: `kjor.sh`) eller legg de to filene i zipen. Samme for `demo.sh`
   (trenger fremmed.sh og `vis_manussaker.py`).
2. **Den gamle dokumentlaget `arbeid/hack/levering/*.md`** (KRAVRESPONS, JURYSVAR, JURY_SPORSMAL, BESLUTNINGSSTOTTE, README, EN_SIDE, SLIDE)
   peker på 17 `state/rapporter/`-filer og 4 arbeidsfiler som ikke er i zipen. Fire av rapportene ligger i `kilder/` under samme navn.
   Hoveddokumentene i `c1/leveranse/` er rene.
3. **1,5 GB pakker for en sklearn+LightGBM-modell.** Rot-`pyproject.toml`/`uv.lock` er landsbyens hele miljø (torch, catboost, xgboost,
   interpret, pytabkit, claude-agent-sdk). README sier «ca. 1 min»; på vanlig nett er 1,5 GB flere minutter. `arbeid/kandidater/smed2_c1_mot/`
   har et lite låst miljø som alt er i zipen og kunne vært roten. Ikke endre før frys uten ny ZIPTEST.
4. Kosmetisk: KJOR.sh skrev «tid: uv sync 0 s» i min kjøring selv om miljøet ble bygget i samme kjøring.

## Diskvarsel
Rota har **2,7 GB ledig** (15:14). `/tmp/jurytest_zip` (2,9 GB, smed #2346), `/tmp/jury2328` (0,9 GB) og 10+ `/tmp/c1_*`-kopier à 0,4 GB
ligger igjen. Hver jury-/kaldstart-test trenger 1,5 GB; sluttsjekken 19:30 kan feile på full disk. Eierne bør rydde egne kopier. Mine egne
(`/tmp/jurydom2348b`, `/tmp/juryhome2348b`, .venv i `/tmp/jurydom2348`) er slettet; logg ligger i `/tmp/jurydom2348/kjor.log`.
