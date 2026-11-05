# Case 1: én zip juryen kan pakke ut og kjøre alene (#2346)

**Bygg (fra landsbymappen):** `sh arbeid/hack/levering/pakk_jury.sh` -> `/tmp/jurypakke_c1.zip` (1,1 MB, ca. 94 filer, 37 s).
Kan kjøres på nytt når som helst, også etter frysen kl. 16. Ingen frosne filer endres; alt kopieres.

## Hva skriptet gjør
1. Kjører `fremmed.sh` i `/tmp/jurybygg_c1` (frysvakt, kald kjøring, tallvakt). Ikke TALLVAKT GRØNN = ingen zip.
   Zipen slettes først, så en feilet bygging etterlater aldri en gammel pakke.
2. Tar fillista fra den kalde kopien og kopierer de samme filene fra kilden, pluss alle frosne filer i
   `c1_frys.py` (også `pred_miks_h2.csv`, `full_test.csv`, `kjor_agent_real_maskin_alene.csv`), hele `c1/leveranse/`
   (kravrespons, JURY, README, `kilder/`), og i roten `README.md` (= `levering/JURY_README.md`) og `KJOR.sh` (= `levering/jury_kjor.sh`).
3. Målerne v2/v3 hadde `<repo>/…` hardkodet; i zipen er datastien `os.path.join(HER, "../../../…")`. Regnestykket er uendret.
4. `FROSNE_SHA256.txt`: sha256 for de 15 frosne filene som er kopiert uendret. Finnes `state/c1_frys.json` (etter kl. 16),
   må hver sha være lik frysens, ellers stopp. `KJOR.sh` sjekker fila først (FRYSVAKT GRØNN/RØD).

## Zip-README, ord for ord: `unzip jurypakke_c1.zip`, `cd c1_stemmeagent`, `sh KJOR.sh`
Test 14:55, tom mappe `/tmp/jurytest2346`, `env -i HOME=/tmp/juryhome2346` (tom uv-buffer), systemets python3,
og `sandbox-exec` med `(deny file-read* file-write* (subpath "<repo>"))` (kontrollert: `cat mission.md` nektes):

| steg | resultat |
|---|---|
| `sh KJOR.sh` | utgang 0, 78 s med nedlasting. FRYSVAKT GRØNN (15 filer), **HOVEDTALL 0.476190**, **TALLVAKT GRØNN** |
| `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh` | TP 30 FP 38 FN 28 TN 1443 STEMMER, sha256 LIK (b113b545…) |
| ordet «landsby» i hele kjøreloggen | 0 treff |
| endret `pred_miks_h2.csv` i utpakket kopi | KJOR.sh stopper: FRYSVAKT RØD |
| prøvefrys (`C1_FRYS=/tmp/provefrys2346.json`) | «sha256 i pakka = frysfila», zip bygget |
| prøvefrys med én feil sha | bygget stopper (fremmed.sh FRYSVAKT RØD), ingen zip igjen |

8 tekstfiler i pakka nevner `~` (rapporter i `kilder/`, demo_utskrift, tallvaktas standard-rot som overstyres med `--rot`).
Kjøringen leser dem ikke; sandkassen beviser det.

## Åpent
- **Løst ca. 15:08:** TALLVAKT RØD 14:56–15:08 i landsbymappen (ikke fra zipen): ny tekst «565 av 569 MOT-stemmer» i
  `c1/leveranse/kravrespons.md:10` og `ERLIG_EVALUERING.md:68` leses av tallvakta som antall MOT i test (58).
  Varslet på tavla; teksten ble rettet. Imens nektet pakk_jury.sh å bygge, med vilje.
- **Ny bygging etter rettingen:** 95 filer, `test_zip.sh` -> FRYSVAKT GRØNN, HOVEDTALL 0.476190, TALLVAKT GRØNN, STEMMER, sha LIK, **ZIPTEST GRØNN**.
- Sidefunn: sjekk_treffsikkerhet sier accuracy agent 95,7 % / følg styret 96,2 % (n 1539); dashbordet sier 95,39 / 95,71 %. Bør #2347/dommer2 se på.
- Ikke committet: arbeid/ er git-ignorert. Filene ligger på disk: `arbeid/hack/levering/{pakk_jury.sh,jury_kjor.sh,JURY_README.md}`.
- Kl. 19.30 (#1972): `sh arbeid/hack/levering/pakk_jury.sh && sh arbeid/oppgave_2346/test_zip.sh` (aksepttesten over i sandkasse, skriver ZIPTEST GRØNN).

## Zipen er nå steg 5 og 6 i sluttsjekken (#2349)
`bash arbeid/hack/levering/sluttsjekk.sh` gjør nå til slutt:
- **5 jury-zip:** `pakk_jury.sh` -> `/tmp/jurypakke_c1.zip` (annen sti med `C1_JURYZIP=`). Bygge- og stage-mappe ligger i sluttsjekkens loggmappe, så den kolliderer ikke med andre som kjører pakk_jury.sh samtidig (`C1_JURYBYGG`/`C1_JURYSTAGE`, standard uendret).
- **6 ziptest:** ny `arbeid/hack/levering/test_jury_zip.sh ZIP [TESTMAPPE]` (aksepttesten fra `oppgave_2346/test_zip.sh`, flyttet hit). Tom mappe, `env -i` med tom HOME, sandbox-exec som nekter landsbymappen. Krever FRYSVAKT GRØNN, TALLVAKT GRØNN, STEMMER, ingen «landsby» i loggen.
- Sluttsjekken krever i tillegg at HOVEDTALL fra zipen = HOVEDTALL fra kald kopi (= kv hack_levert). Ellers `SLUTTSJEKK RØD`.

**Test 15:11–15:15 (prøvefrys `C1_FRYS=/tmp/provefrys2349.json`, siden ekte frys kommer kl. 16):**
`SLUTTSJEKK GRØNN: frysvakt, kaldstart, tallsjekk, jury-zip ok; HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen (1.0M, 96 filer)` på **242 s** (4 min 2 s) totalt.
Rød-test: zip med én linje lagt til `pred_miks_h2.csv` -> `FRYSVAKT RØD` i KJOR.sh -> `ZIPTEST RØD`, utgang 1.

Kl. 19.30 (#1972): bare `bash arbeid/hack/levering/sluttsjekk.sh`. Regn med ca. 4–5 min. Zipen til juryen er da `/tmp/jurypakke_c1.zip`.
Ingen frosne filer endret (endret: sluttsjekk.sh, pakk_jury.sh, ny test_jury_zip.sh; ingen av dem er i c1_frys.py).
