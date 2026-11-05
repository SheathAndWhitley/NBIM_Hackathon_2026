# Case 1: tallvakta er eget steg i sluttsjekken (#2397, smed4, 05.11 ca. 15.24)

## Endring i `arbeid/hack/levering/sluttsjekk.sh`
- **Nytt steg 3 tallvakt**: kjører `c1_tallvakt.py` i den kalde kopien (MAAL) mot kopiens egen kjøring
  (`ut/pred_maaler.csv`, `ut/KJORING.txt`), under `env -i` med kopiens .venv. Rød gir:
  `SLUTTSJEKK RØD: TALLVAKT RØD (utgang 1): N tall i pakka avviker fra måleren, se AVVIK-linjene over (...3_tallvakt.txt). Rett teksten i landsbymappa og kjør sluttsjekken på nytt`, utgang 4, med AVVIK fil:linje skrevet rett over.
- Steg 2 (fremmed.sh) stopper ikke lenger med den vage «kaldstart fremmed.sh (utgang 1)» når bare tallvakta i fremmed.sh er rød; da tar steg 3 over med egen melding. Alle andre feil i steg 2 stopper som før.
- Mangler kopien .venv eller `ut/pred_maaler.csv`: rødt med egen melding. Grønn i steg 3 men rød i fremmed.sh: rødt («uforklart»).
- Tallsjekken heter nå steg 3b. Grønn sluttlinje nevner «tallvakt». Ingen frosne filer, målere eller tekster i pakka er rørt.

## Rød kjøring (bevisst feil i en speilkopi, ikke i leveransen)
Speil `/tmp/c1_rodtest_2397` (bare filene fremmed.sh trenger, 3,7 MB). I speilets `kravrespons.md:4` endret jeg «F1 på MOT 0,476» til «0,512».
Testfrysfil `/tmp/c1_rodtest_2397_frys.json` (C1_FRYS, siden frysen ikke er tatt før kl. 16).
```
>>> 3 tallvakt (kald kopi /tmp/c1_rodtest_2397_kald)
    AVVIK arbeid/hack/c1/leveranse/kravrespons.md:4: F1 0,512, måleren sier 0.4762
SLUTTSJEKK RØD: TALLVAKT RØD (utgang 1): 1 tall i pakka avviker fra måleren, se AVVIK-linjene over (...). Rett teksten i landsbymappa og kjør sluttsjekken på nytt (39 s)
```
Utgang 4. Full logg: `arbeid/oppgave_2397/c1_tallvakt_sluttsjekk_rod.log`.

## Grønn kjøring (ekte landsbymappe, git d51d58e + endringen)
`C1_FRYS=/tmp/c1_gronn_2397_frys.json C1_JURYZIP=/tmp/c1_2397_jury.zip bash arbeid/hack/levering/sluttsjekk.sh /tmp/c1_gronn_2397_kald`
```
>>> 3 tallvakt: F1 0.4762 P 0.4412 R 0.5172 TP 30 FP 38 FN 28 (58 MOT i fasit, 66 avvik); 18 filer, 167 påstander, 0 avviker; OK
>>> 4 kald kopi: 0.476190   kv hack_levert: 0.476190
>>> 6 ZIPTEST GRØNN: HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190
SLUTTSJEKK GRØNN: frysvakt, kaldstart, tallvakt, tallsjekk, jury-zip ok; HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen (197 s)
```
Utgang 0, 3 min 17 s. Full logg: `arbeid/oppgave_2397/c1_tallvakt_sluttsjekk_gronn.log`.

## Merk
- Kl. 19.30 kjøres sluttsjekken UTEN C1_FRYS (ekte frysfil fra kl. 16). Før kl. 16 er steg 1 rødt med vilje (`--krev`).
- Tallvakta kjøres nå to ganger (i fremmed.sh og i steg 3), ca. 2 s ekstra.
- **Disk, viktig før 19.30:** én full grønn sluttsjekk etterlot 3,2 GB i loggmappa `/tmp/c1_sluttsjekk_logg.XXXX` (bygg/, stage/, ziptest/ med .venv), pluss ca. 270 MB i MAAL.
  Disken falt til 0,5 GB ledig. Jeg har slettet mine. Den som kjører 19.30 bør ha minst 4 GB ledig og slette loggmappa etterpå (eller ta bort .venv-ene der).
