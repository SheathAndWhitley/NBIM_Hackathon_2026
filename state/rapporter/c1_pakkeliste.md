# Case 1: alle filer den låste pakka må ha (dommer #2333, 05.11 kl. 14.47)

Input til #1972 (endelig pakke kl. 18.30). Maskinlesbar liste: `arbeid/oppgave_2333/pakkeliste.txt` (én sti per linje,
relativt til rotmappa; mapper tas med rekursivt uten `__pycache__`, `.venv`, `logg/`).
**Viktig:** `arbeid/` og `state/` er gitignorert i landsbyen, så pakka må lages fra disk, ikke fra git.

## Bevis (kl. 14.45)
Pakka bygd fra lista i tom mappe `/tmp/c1_pakketest` (8,0 MB, 146 filer, står igjen til #1972) og README-kallet
`bash arbeid/hack/c1/leveranse/kjor.sh` kjørt der: utgang 0 på 28 s, TALLVAKT GRØNN (17 filer, 166 påstander, 0 avvik),
`MOT mot styret: TP 30 FP 38 FN 28 F1 0.4762`, SCORE 0.481752. Ingen interne stier (`~`) i utskriften.
Frysvakta mot en midlertidig frysfil (`/tmp/c1_2333_frys.json`, ikke `state/`) er GRØNN med `--rot /tmp/c1_pakketest`:
alle 10 frosne filer ligger i pakka. Ingen frosne filer er rørt.

## Fil for fil

### A. Juryens dokumenter, `arbeid/hack/c1/leveranse/` (hele mappa uten `__pycache__`)
| fil | beviser | finnes |
|---|---|---|
| `kravrespons.md` | kravresponsen på én side (regelverkets mal, 438 ord) | ja |
| `JURY.md` | svar på de tre offisielle juryspørsmålene | ja |
| `README.md` | ett kall, sha256 på data, kilder med URL, AI-bruk, kreditering (B §5) | ja |
| `JURY_SPORSMAL.md`, `BEGRENSNINGER.md`, `ERLIG_EVALUERING.md`, `NESTE_VERSJON.md` | ærlig evaluering, erklærte begrensninger, «én uke til» | ja |
| `kjor.sh` | README-kallet (kald kopi via fremmed.sh + måler v3) | ja |
| `demo.sh`, `demo_vis.py`, `demo_utskrift.txt` | demoen: ekte agent, 3 saker seed 0, lagret utskrift | ja |
| `kilder/` (33 filer) | kopier av måle- og kontrollrapportene JURY/BEGRENSNINGER peker til, så pakka står alene | ja |
| `spor_npx/` | den gamle N-PX-grunnlinja (SPOR=npx), kreditering av startpakke-kode | ja |

### B. Juryens dokumenter og agenten, `arbeid/hack/levering/`
| fil | beviser | finnes |
|---|---|---|
| `README.md` | kjør fra ren kopi, tabell til menneske, robusthet, svartid, rare saker | ja |
| `SLIDE.md` | 1 slide med funn og avgrensning (krav 22, speider #2332) | ja (14.44) |
| `JURYSVAR.md`, `METODE.md`, `BESLUTNINGSSTOTTE.md`, `TREFFSIKKERHET.md`, `EN_SIDE.md`, `JURY_SPORSMAL.md`, `KRAVRESPONS.md` | metode, tidssplitt, lekkasje, beslutningsstøtte, 2x2, hvorfor ikke accuracy | ja |
| `kjor_agent_real_test2026_LES.md`, `kjor_agent_real_test2026.txt` | målerutskrift for hovedtallet | ja |
| `kjor_agent.py`, `c1_real.py`, `injeksjon_hoflig.py`, `retningslinje_oppslag.py` | agenten (frosne: de tre første) | ja |
| `fremmed.sh` | kald kopi under `env -i`, frysvakt, tallvakt, HOVEDTALL | ja |
| `sjekk_treffsikkerhet.sh`, `treffsikkerhet.py`, `treffsikkerhet_ki.py` | «sjekk tallene selv» uten måleren | ja |
| `sluttsjekk.sh` | intern sluttsjekk (#2330), ufarlig å ha med | ja |
| `kjor_agent_real_maskin_alene.csv` | den leverte svarfila (kv hack_levert, frossen) | ja |
| `kjor_agent_real_pred_maaler.csv` | svar med ruting | ja |
| `motstandstest.py`, `motstand_ut/` (2,7 MB) | motstandstesten og rådataene (krav 11) | ja |
| `c1_forslagsstiller.py/.txt` | opptelling forslagsstiller | ja |
| `demo/` uten `.venv` og `logg/` | `RESERVE.md` + `reserve/` (lagrede utskrifter, plan B); `app.py` er merket INTERN i `demo/README.md` | ja |
| ikke med: `c1_v1/`, `arkiv/`, `kjor_agent_pred_maaler.csv` | gammel v1 og N-PX-æra, refereres ikke av jurydokumentene | – |

### C. Kode og data utenfor de to mappene som kallene trenger
| fil | trengs av | finnes |
|---|---|---|
| `arbeid/oppgave_2044/train.py` (frossen) | modellen, kjøres med runpy fra c1_real.py | ja |
| `arbeid/oppgave_2047/vern.py`, `arbeid/oppgave_2046/case1_mot.py` (frosne) | vern og MOT-definisjon | ja |
| `arbeid/oppgave_2044/pred_miks_h2.csv`, `arbeid/oppgave_2103/full_test.csv` (frosne) | kreves av frysvakta: mangler de, stopper fremmed.sh med utgang 4 etter kl. 16 | ja |
| `state/opplastet/20261105_114241_real_votes.csv` (frossen, 2,6 MB) | trening, fasit, sha-sjekk i c1_real.py | ja |
| `arbeid/hack/c1/data_off/real_test_input.csv` | agentens input test 2026 | ja |
| `arbeid/hack/c1/retningslinjer/` (punkter.jsonl + GVG-kopiene) | sitatlaget | ja |
| `arbeid/hack/c1/maaler_offisiell_v2.py`, `maaler_offisiell_v3.py` | målerne (stien pekes om av fremmed.sh:34) | ja |
| `arbeid/hack/maaler.sh`, `arbeid/hack/c1/maaler_nbim.py` | kjor.sh siste steg «rundens måler» | ja, men se avvik 2 |
| `arbeid/kandidater/smed2_c1_mot/pyproject.toml`, `uv.lock` | låst miljø (`uv sync --frozen`) | ja |
| `arbeid/verktoy/c1_frys.py`, `c1_tallvakt.py`, `c1_tallsjekk.py` | fremmed.sh:13-18 (mangler train.py eller c1_frys.py: «FEIL STED» utgang 6, rotsjekk #2339 kl. 14.47; frysvakt utgang 4), :31 (mangler c1_tallvakt.py: `cp` feiler under `set -e`), :53 (bare varsel) | ja |
| `state/c1_frys.json` | frysbeviset; **finnes ikke før kl. 16**, må legges til i #1972 | nei (ventet) |
| `arbeid/hack/c1/tall_tabell.md`, `menneske_tabell.py`, `DEMO_MANUS.md`, `kaldstart.sh`, `sluttkontroll.sh`, `demo_saker_2026.sh`, `demo_mangler_styret.sh`, `demo_trekk_2026.py`, `sitatvakt.py`, `arbeid/hack/CASE/demo_saker.md` | refereres fra README/JURY/DEMO_MANUS/RESERVE | ja |
| `arbeid/oppgave_2267/maaling.txt`, `arbeid/hack/c1/terskeltabell_ut.md`, `MAALER_LES.md`, `tall_kilder_ut.txt` (24 kB) | tallsjekk kilde A; uten dem sier tallsjekk 524 «ikke funnet» inne i pakka (varsel i fremmed.sh, RØDT i sluttsjekk.sh `--feil`) | ja |

## Tar kaldstart.sh og fremmed.sh med begge mappene?
- **fremmed.sh: delvis.** Linje 31 (versjonen fra kl. 14.47, etter rotsjekken #2339) kopierer `arbeid/hack/levering/*.md` og `arbeid/hack/c1/leveranse/*.md`, altså bare
  toppnivå-md fra begge mapper, til tallvakta. Ikke `kilder/`, `spor_npx/`, `demo.sh`, `kjor.sh`, `demo_utskrift.txt`, `demo/`.
  Det er riktig for formålet (kald kjøring + tallvakt), men fremmed.sh er ikke et pakkeskript.
- **kaldstart.sh: nei.** Linje 36–45 kopierer bare kode og data (`hack/c1/*.py`, `hack/c1/demo_*.sh`, agentfilene,
  real_votes). Ingen `.md` fra noen av mappene. Også det er riktig for formålet (måle fra kald start), ikke pakking.
- **Det finnes ikke noe pakkeskript.** #1972 sier «zip arbeid/hack/c1/leveranse»; det er for lite: `kjor.sh` kaller
  `levering/fremmed.sh`, som trenger alt i tabell C med samme relative stier fra rotmappa. Zip-en må lages fra
  `pakkeliste.txt` (eller tilsvarende) med rot = repoets rot.

## Avvik å rette før 18.30 (ikke frosne filer)
1. **`state/c1_frys.json` kommer kl. 16** og må inn i pakka sammen med de 10 frosne filene (alle er i lista). Uten json
   sier frysvakta «ikke frosset ennå» (utgang 0), så pakka kjører, men beviset mangler.
2. **`arbeid/hack/maaler.sh:6` og `arbeid/hack/c1/maaler_nbim.py:17-18` hardkoder `<repo>/`**
   (`maaler_nbim.py` peker på `arbeid/hack/CASE/..._real_votes.csv`). Siste steg i `kjor.sh` («rundens måler») virker her
   bare fordi landsbymappa finnes på maskinen. På juryens maskin gir det «No such file» og `kjor.sh` utgang ≠ 0 under
   `pipefail`, etter at hovedtallet er skrevet. Fiks: `kjor.sh` dropper rundens måler (v3 er hovedtallet), eller
   `maaler.sh` bruker `$(dirname "$0")` og `maaler_nbim.py` får `--data`-sti relativt. `kjor.sh` er ikke frossen.
3. `arbeid/hack/c1/sitatvakt.py:16` og `menneske_tabell.py:7-8` hardkoder også landsbystien. Bare «gjenskapes med», ikke i
   README-kallet. Nevn det i README eller rett til relativ sti.
4. `levering/KRAVRESPONS.md` peker på `c1/data_v3/fasit.csv` (finnes ikke, N-PX-æra) og på `state/rapporter/...` og
   `arbeid/hack/c1/arkiv/...` som ikke er i pakka. Fila er intern (README sier kravresponsen er `c1/leveranse/kravrespons.md`);
   enten dropp den fra pakka eller merk den intern øverst. Samme gjelder «gjenskapes med»-stiene til `arbeid/oppgave_2xxx/`
   i `levering/README.md` og `BESLUTNINGSSTOTTE.md`: de peker ut av pakka (kopiene i `kilder/` dekker rapportene, ikke skriptene).
