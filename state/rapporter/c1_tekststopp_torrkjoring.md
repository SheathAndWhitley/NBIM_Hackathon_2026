# Case 1: tørrkjøring av tekststopp-zipen (#2800, smed, 05.11 ca. 18:57)

## Forhåndssjekk 18:59 (#2809, smed)
- git status: 0 ukommitterte Case 1-filer (grep c1/case1/stemme tom), HEAD cbae393 (18:58).
- Frysvakt GRØNN: 21 filer like som ved frys 2026-11-05T17:18:18.
- Tavla: ingen åpne Case 1-endringer fra andre smeder; claimed er bare lesende kontroller (#2756 smed4 GitHub-klone, #2799 smed3 dårlig inndata, #1972 dommer kald start).

## Ukommitterte Case 1-filer før zipen (#2805, smed, 18:59)
`git status` 18:58: 17 endrede filer, bare **2 hører til Case 1**, begge committet nå:
- `state/rapporter/c1_sluttsjekk_1800.md` (sluttsjekk #2538 16:47, HEAD 83f152c, erstatter 16:44-teksten)
- `state/rapporter/c1_v2_rullende_2024.md` (retting: V2 2026 = 0,516, ikke 0,4923, dom #2529)
Ingen av dem er frosne filer eller under `arbeid/hack/` (zip-innholdet). Ikke Case 1, latt urørt: LOGG.md, gemma_dev_agent, oppgave_1450/1476/1481/1495/1806/1815/1823 (øvelse 56), generalprove_tomgang, leaderboard, maskinendringer, ovelse_56_arxiv_klynger, `.schema hendelser`, kaggle_benchmarks_reference.md. Ingen push.


**Funn som stopper #2549: ingen.** Ett forbehold: `sluttsjekk.sh` steg 8 (lagre_gronn.sh) skriver til `state/levering/c1_gronn/` og flytter `SISTE_GRONNE.zip`. Derfor kjørte jeg ikke hele sluttsjekken i tørrkjøringen, bare zip-stegene (5 og 6) til en kladdemappe. I #2549 kl. 19 kjøres hele `bash arbeid/hack/levering/sluttsjekk.sh`.

- HEAD 388aa31, arbeidstreet rent under `arbeid/hack/`.
- Frysvakt før og etter: GRØNN, 21 filer like som ved frysen 17:18:18.
- `sh arbeid/hack/levering/pakk_jury.sh /tmp/c1_torr_2800/jury.zip`: utgang 0, 1,1 MB, 163 filer (merk: 9 tekstfiler nevner ~, men kjørestien leser dem ikke, samme som før).
- `sh arbeid/hack/levering/test_jury_zip.sh`: utgang 0, `ZIPTEST GRØNN: HOVEDTALL F1 MOT 0.512000` (TP 32, FP 35, FN 26), prediksjonsfila er lik den frosne.
- sha256 kladdezip: 0b4d909ca8f3f374f978352d8eb122704686fe7db15aa6d3d9a078a0df015f7b (bare en kladd, ikke levering).

## Filer som er endret siden forrige grønne zip (jurypakke_c1_1827_0e3b14b.zip)
Bare tekst, ingen kode og ingen prediksjoner:
1. arbeid/hack/c1/leveranse/BEGRENSNINGER.md
2. arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md
3. arbeid/hack/c1/leveranse/JURY_SPORSMAL.md
4. arbeid/hack/levering/GITHUB_README_UTKAST.md (README-rettingen #2791)
5. arbeid/hack/levering/JURY_SPORSMAL.md
6. arbeid/hack/levering/LAGET.md (lages av pakk_jury.sh ved hver bygging, ikke i git-diffen)

Ingen filer er lagt til eller fjernet (diff -rq: 6 linjer, alle «differ»).
