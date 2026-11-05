# Case 1: jury-zipen ryddet (#2587, ordre #266 hull 4+5)

Ny zip: `/tmp/jurypakke_c1_2587.zip` (137 filer). ZIPTEST GRØNN (FRYSVAKT GRØNN 15 filer, HOVEDTALL 0.476190,
TALLVAKT GRØNN, TP 30 FP 38 FN 28 STEMMER, prediksjonsfil LIK frossen). Tallvakt i repoet: 19 filer, 173 påstander, 0 avvik.

## Endret
- (a) Rot-README (`levering/JURY_README.md`): første linje peker til `c1/leveranse/README.md` («Datakilder», «AI-verktøy»)
  for kilder, kreditering og AI-bruk. Unzip-steget er nå `unzip jurypakke_c1*.zip`, fordi den lagrede grønne zipen heter
  `jurypakke_c1_<HHMM>_<commit>.zip`. Fjernet «(#2417, #2421)».
- (b) `pakk_jury.sh`: `levering/KRAVRESPONS.md` og `levering/EN_SIDE.md` filtreres ut (0 i ny zip). fremmed.sh er urørt
  (tallvakta globber, tåler at de mangler). `levering/README.md:24` sier nå at de ikke er med i zipen.
- (c) `JURY_SPORSMAL.md:69`: ikke lenger «JURY.md sier låst på val» (JURY.md:40 sier nå selv at båndet er valgt på test).
  `SVAKHETER.md:3`: «oppdateres etter frys i #1975» og «smed2 #2044» ut; sier at modell og hovedtall er de samme etter frysen.
- (d) Interne navn: `landsbyrapport:` -> `utviklingsrapport:` i NESTE_VERSJON.md og JURY_SPORSMAL.md (ikke linje 15);
  LESMEG.md forklarer begge formene. Saksnumre og agentnavn ut av kommentarene i `leveranse/demo.sh` og `leveranse/kjor.sh`,
  også i demo-linja «# renset utskrift» (demo_utskrift.txt har den gamle linja til #2577 kjører demoen på nytt).

## Telling utenfor kilder/ (`arbeid/oppgave_2587/tell_interne.sh`)
| zip | smed/dommer/landsby | #NNNN |
|---|---|---|
| før: siste grønne (`SISTE_GRONNE.zip`) | 115 | 402 |
| etter: `jurypakke_c1_2587.zip` | 82 | 328 |

## Ikke rørt, med grunn
- Frosne .py (c1_real.py, kjor_agent.py, train.py, målerne): sha256 er låst.
- ERLIG_EVALUERING (smed3), JURY_SPORSMAL:15 (#2574), kravrespons.md (#2586) og JURY.md (andres endring ligger staget).
- `README.md:55` (`smed2_c1_mot` er en ekte sti) og «dommer» i AI-avsnittet (forklart som kontrollagent).
- Resten ligger i `levering/*.md` (eldre lag, mange #-pekere som kilder) og SVAKHETER.md (37 #-pekere er kildene).
  Forslag: ta også `levering/JURY_SPORSMAL.md` (merket UTDATERT) ut av zipen.

## Commit og byttedom
- Endringene over ligger i commit 4fe23fe. Den har meldingen til #2577, fordi en annen agent committet mens filene mine var staget.
  Innholdet er mitt (pakk_jury.sh, JURY_README.md, levering/README.md, JURY_SPORSMAL.md, NESTE_VERSJON.md, demo.sh, kjor.sh,
  LESMEG.md, SVAKHETER.md, tell_interne.sh og denne rapporten).
- Byttedommen (d5b3672) sier BYTT til repo4. Zipen over er bygget med frossen modell (0.476190). Rettingene i pakk_jury.sh og
  README gjelder også for neste zip; kjør `sh arbeid/oppgave_2587/tell_interne.sh <ny zip>` for å telle på nytt.
