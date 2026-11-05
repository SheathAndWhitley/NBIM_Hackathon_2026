# Case 1: flyttbar testårskommando for juryen (#2733)

Kommando (fra pakkas rot, både jury-zipen og GitHub-repoen):

    bash arbeid/hack/c1/leveranse/verktoy/testaar.sh          # trener frossen repo4 på nytt per testår
    bash arbeid/hack/c1/leveranse/verktoy/testaar.sh --rask   # måler bare de lagrede svarfilene

Resultat fra fersk kald kopi (/tmp/c1_kald2733.YF2A: bare rotens pyproject.toml/uv.lock, datafila og verktoy/), begge modusene:
- 2024 F1 0,5057 (TP 44 FP 42 FN 44), 2025 0,5309 (TP 43 FP 20 FN 56), 2026 0,5120 (TP 32 FP 35 FN 26), snitt 0,5162.
- Likt med dom #2713 på 4 desimaler. Ca. 50 sek med fersk `uv`-miljø, ellers ca. 10 sek.

Hva som er endret mot arbeid/oppgave_2727/testaar.sh:
- Ingen absolutte stier. Roten finnes fra skriptets plass (5 nivåer opp). Data: `state/opplastet/20261105_114241_real_votes.csv`
  under roten, eller `C1_DATA=<sti>` (GitHub-repoen har ikke datafila, se DATA.md). Datavakta (sha256 71ba5135) står.
- Miljø: `uv run --project <rot>` = kandidatens pyproject.toml/uv.lock (samme som zipen), ikke oppgave_2023.
- abl_rull.py: bare ballot-importen endret (leser `verktoy/stemmeagent/`, byte-lik kopi av arbeid/hack/levering/stemmeagent).
  maaler_aar.py: bare FILER-stiene (relative + C1_DATA). Resten byte-likt med oppgave_2567 (diff i commit).
- Trening som feiler stopper skriptet (før: ble ikke fanget).

Filer (alle nye, i `arbeid/hack/c1/leveranse/verktoy/`, 224 KB):
testaar.sh, abl_rull.py, maaler_aar.py, stemmeagent/{__init__,ballot,config}.py, lagret/repo4_{2024,2025,2026}_test.csv.

For smed (#2549, tekststopp-zipen): **ingenting ekstra å ta med**. pakk_jury.sh linje 32 kopierer hele `arbeid/hack/c1/leveranse/`,
og rotens pyproject.toml/uv.lock + state/opplastet/…real_votes.csv er allerede i zipen. github_synk.sh har også hele
`arbeid/hack/c1/leveranse` på hvitlista. Merk: frys_diff mot frys_fasit_1600.sha256 vil vise disse 9 filene som NY (ikke endret).

Frosne filer: ingen rørt. Frysvakt GRØNN (21 filer). Ingen ~ i verktoy/.

Linje til JURY.md (erstatter #2727-linja):
> Testårstallene (F1 på MOT 0,5057 / 0,5309 / 0,5120, snitt 0,5162) gjenskapes med `bash arbeid/hack/c1/leveranse/verktoy/testaar.sh`: trener den frosne repo4-modellen på nytt for hvert testår 2024–2026 (valgt på året før, trent på eldre år) og måler med den offisielle måleren (`--rask` måler bare de lagrede svarfilene).

## Uavhengig sjekk smed3 (#2737, 05.11 kl. 18)
GRØNN: fersk kald kopi i /tmp/c1_kald2737.QR34 (bare pyproject.toml, uv.lock, datafila og verktoy/, 12 filer) ga 0,5057 / 0,5309 / 0,5120 (snitt 0,5162) i både `--rask` (0,3 s) og full trening (36 s med ferskt uv-miljø), TP/FP/FN likt med fasit; `grep -r /Users verktoy/` = 0. Eneste /Users-spor var en uv-advarsel om skallets VIRTUAL_ENV, som uv ignorerte (kopiens eget .venv ble brukt).
