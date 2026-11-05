# Case 1 (#2773): siste kontroll, GitHub-repoen mot endelig pakke (dommer, 05.11 19:11)

**GODKJENT: GitHub origin/main (499ae0c, ren startcommit) og endelig pakke (jurypakke_c1_1902_cbae393.zip, sha256 e6dae498…7818) sier de samme tallene: F1 MOT 0,512 (0.512000), tre testår 0,5057 / 0,5309 / 0,5120, snitt 0,5162, 95 % KI [0,400; 0,621], presisjon 0,478, recall 0,552, TP 32 FP 35 FN 26.**

## Slik ble det sjekket (`arbeid/oppgave_2773/kontroll.sh`)
- `git fetch origin`, `git archive origin/main` til tom mappe; zipen pakket ut i egen tom mappe. Ingen fasit lest, ingen hemmeligheter berørt.
- 157 filer har samme sti i begge. 147 er byte for byte like (all modell- og målerkode, KJOR.sh, leveranse-dokumentene).
- 10 er ulike, og alle er bare stier: `<repo>` skrevet som `<repo>` eller `.` i GitHub
  (JURY_README.md, TREFFSIKKERHET.md x2, c1_tallvakt.py, menneske_tabell.py, usette.py, to dommerrapporter) og
  FROSNE_SHA256.txt uten de fem filene som holdes ute av GitHub. Ingen tall endret.
- Bare i pakka: arrangørens `state/opplastet/20261105_114241_real_votes.csv`, `data_off/real_*_input.csv`, `pred_miks_h2.csv`
  og smed2-kandidatens pyproject/uv.lock. `find -iname "*votes*.csv"` i GitHub: tomt.
- GitHub-fryslista stemmer med GitHub-filene (`shasum -c`: 0 avvik).
- GitHub README.md (= GITHUB_README_UTKAST.md i pakka) nevner hvert av hovedtallene over; pakkas JURY.md og KANDIDATER.md nevner de samme. Ingen F1-påstand med andre tall i README/LAGET/DATA på GitHub.

## Forbehold
Kontrollen er kjørt 19:11, ikke 19:45, fordi oppgaven kom nå. Blir origin/main eller ENDELIG_PAKKE.zip byttet før 20:00,
kjøres `bash arbeid/oppgave_2773/kontroll.sh` på nytt (ett minutt). Oppfølging ligger på tavla for dommer kl. 19:45.

## Kontroll 19:45 (#2822, dommer)
**AVVIK, men kjent og forklart:** `ENDELIG_PAKKE.zip` peker fortsatt på 1902-zipen (sha e6dae498…7818, uendret). origin/main har gått fra 499ae0c til 4f148d1 (synk 19:08/19:12/19:16, skanning 0 funn).
- 12 ULIK-filer, 10 av dem bare stier som før (`<repo>` -> `<repo>`/`.`), pluss toppnivå-README (GitHub-README og zip-README er ulike med hensikt; GitHub-README nevner alle hovedtallene, ingen avvikende F1-påstand).
- 2 innholdsendringer, ikke stier: `arbeid/hack/c1/leveranse/README.md` linje 14 og `kravrespons.md` linje 10. GitHub sier «repo4 uten samme-sesong-historikk gir 0,396 (arkitektens måling, ikke reprodusert av kontrollagent)»; 1902-zipen sier «for repo4 er golvet ikke målt». Det er 0,396-rettelsen etter dom #2668 (`c1_repo4_golv_rettet.md`), feid med i landsby-commit 4ed8a9c 19:15. GitHub er altså ærligere enn 1902-zipen. Ingen hovedtall endret, ingen kode endret.
- `SISTE_GRONNE.zip` -> jurypakke_c1_1918_9f41d82.zip (sha 84aefb46…2f73) er byte-lik GitHub på begge filene, og dommer2 kaldstartet 1918 GRØNN kl. 19:40 (#2860).
- Arrangørrader i GitHub: tomt. Hemmelighetsskanning: 0 funn.

**Anbefaling:** sluttkvitteringen (#2828) oppgir 1918-zipen som endelig pakke, så zip og GitHub sier det samme. Flyttes ikke her; det er #2828 sin jobb.
