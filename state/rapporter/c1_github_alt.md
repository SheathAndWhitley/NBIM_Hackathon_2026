# Case 1: alt Case 1-arbeid lagt inn i GitHub-repoen nbim (#2762, ordre #277)

- Filantall i repoen: **før 161, etter 957** (HEAD 5deae34 = origin/main etter git ls-remote) (git ls-files). Skanning: **0 funn** (synkens mønstre + portvakt c1_hemmelig_skann.sh fra #2605).
- Frosne filer: `shasum -a 256 -c FROSNE_SHA256.txt` gir 0 avvik både i repoen og i landsbyen.
- Hvordan: `arbeid/verktoy/github_synk.sh` (10-min-synken) har fått en ALT-liste i tillegg til hvitlista, laget av ny `arbeid/verktoy/c1_github_alt.py`: alle filer under arbeid/hack/c1 og arbeid/hack/levering, state/rapporter/c1_*.md, case1_*.md og andre rapporter som nevner Case 1/stemmeagent/NBIM. Siden synken speiler med rsync --delete, MÅTTE dette inn i synken; ellers hadde neste synk slettet det igjen.
- Filer fra ALT-lista som skanneren flagger, tas automatisk ut av stagen og skannes på nytt. Flagg i den gamle hvitlista stopper fortsatt synken som før.
- .gitignore i repoen: `ut/` og `home/` er nå forankret til roten (`/ut/`, `/home/`), så ut-mapper lenger nede kommer med. DATA.md har fått et avsnitt om rådataene vi selv lastet ned og hvordan de hentes på nytt.

## Utelatt, og hvorfor

Ingen fil var over 50 MB etter at mappene under var tatt ut. pred_miks_h2 ligger ikke i repoen (0 treff i git ls-files).

```
arbeid/hack/c1/__pycache__/	Python-cache
arbeid/hack/c1/data_off/	arrangørens casedata (hentes fra casepakken, se DATA.md)
arbeid/hack/c1/arkiv/gammel_data/	nedlastet N-PX-rådata fra SEC (hentes på nytt med hent_npx.py/hent_votes.py, se DATA.md)
arbeid/hack/c1/test/votes.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, stemme)
arbeid/hack/c1/test/test_input.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag)
arbeid/hack/c1/test/train.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne fasit, forslag, stemme)
arbeid/hack/c1/test/fasit.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne fasit)
arbeid/hack/c1/kilder/nbim_begrunnelser_saypay.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne fasit, nbim_stemme_side)
arbeid/hack/c1/kilder/nbim_begrunnelser.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, nbim_stemme)
arbeid/hack/c1/ut_v3/smed2_pred_val.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag)
arbeid/hack/c1/ut_v3/smed2_pred.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag)
arbeid/hack/c1/bytte/stemmeagent/__pycache__/	Python-cache
arbeid/hack/c1/leveranse/spor_npx/utkast_1100/	utkast holdt utenfor også før (#2666-synken)
arbeid/hack/c1/leveranse/kilder/__pycache__/	Python-cache
arbeid/hack/c1/leveranse/verktoy/stemmeagent/__pycache__/	Python-cache
arbeid/hack/levering/__pycache__/	Python-cache
arbeid/hack/levering/demo/__pycache__/	Python-cache
arbeid/hack/levering/demo/.venv/	virtuelt miljø (lages av uv fra pyproject.toml/uv.lock)
arbeid/hack/levering/demo/reserve/csv/test2026_agent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne proposal_text)
arbeid/hack/levering/demo/reserve/csv/demo5_agent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne proposal_text)
arbeid/hack/levering/demo/reserve/csv/sitat_agent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne proposal_text)
arbeid/hack/levering/demo/reserve/csv/mangler_styret_agent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne proposal_text)
arbeid/hack/levering/demo/data/moter_2026.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne faktisk_npx, forslag)
arbeid/hack/levering/motstand_ut/test_uten_forslag.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_inj_mot.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_tomme_felt.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_ukjent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_inj_for.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_tom.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/motstand_ut/test_omformulert.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne forslag, forvalter, forvalter_cik)
arbeid/hack/levering/c1_v1/ut/agent.csv	csv med fasit eller arrangørens/NBIMs rådata (kolonne proposal_text)
arbeid/hack/levering/stemmeagent/__pycache__/	Python-cache
```

Flagget av hemmelighetsskanningen og derfor utelatt (44 filer: e-post i SEC User-Agent i hent_*.py, arrangørens e-post, ~/-stier og rapporter som siterer nøkkelmønstre i sine sjekklister):

```
arbeid/hack/c1/hent_nbim.py
arbeid/hack/c1/hent_npx.py
arbeid/hack/c1/hent_votes.py
state/rapporter/arkitekt_2610_laget.md
state/rapporter/arkitekt_2767_start_her_boks.md
state/rapporter/arkitekt_2776_readme_https.md
state/rapporter/arkitekt_jurylesning_1855.md
state/rapporter/c1_2613_hemmelighetssjekk_i_synk.md
state/rapporter/c1_dom_2770.md
state/rapporter/c1_dom_github_trygg.md
state/rapporter/c1_dom_github_vs_zip.md
state/rapporter/c1_ekstern_lesning_1840.md
state/rapporter/c1_formelle_krav_sjekk.md
state/rapporter/c1_frysvakt_klar.md
state/rapporter/c1_github_fremmedtest.md
state/rapporter/c1_github_fremmedtest2.md
state/rapporter/c1_github_kald_klon.md
state/rapporter/c1_github_lesning.md
state/rapporter/c1_github_retting_2770.md
state/rapporter/c1_github_sikkerhet.md
state/rapporter/c1_klone_sjekk.md
state/rapporter/c1_laget_md_github_2615.md
state/rapporter/c1_lekkasje_steder.md
state/rapporter/c1_lekkasje_tallsjekk.md
state/rapporter/c1_lenkesjekk.md
state/rapporter/c1_metode_mot_logg.md
state/rapporter/c1_offline_etter_pyproject.md
state/rapporter/c1_push_historikk_sjekk.md
state/rapporter/c1_repo_fremmedlesing.md
state/rapporter/c1_repo_kald.md
state/rapporter/c1_repo_sjekk.md
state/rapporter/c1_repo_skann_historikk.md
state/rapporter/c1_repo_squash.md
state/rapporter/c1_repo_synk_sjekk.md
state/rapporter/c1_reserveplan.md
state/rapporter/c1_synk_sjekk_2628.md
state/rapporter/disk_rydding_1800.md
state/rapporter/diskrydding_2751.md
state/rapporter/dom_disk_rydding.md
state/rapporter/epost_utkast_hackathon.md
state/rapporter/github_repo_269.md
state/rapporter/github_repo_dom.md
state/rapporter/github_synk.md
state/rapporter/maskinendringer.md
```

Holdes også utenfor av lagets egen `arbeid/hack/levering/.gitignore` (demo/logg/): 13 json/jsonl demologger.
