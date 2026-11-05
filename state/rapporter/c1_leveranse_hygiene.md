# Case 1: hygiene i leveransen før frysen (#2422, dommer2, 05.11 kl. 15.40)

Sjekket `arbeid/hack/c1/leveranse/` og jury-zipen fra `pakk_jury.sh` (/tmp/jurypakke_c1.zip kl. 15.30, 119 filer)
for __pycache__, .DS_Store, logger, absolutte stier og hemmeligheter.

## Funnet og fjernet
- `arbeid/hack/c1/leveranse/__pycache__/` (demo_vis og sporlogg, .pyc for 3.12). Slettet. Var git-ignorert og
  allerede utenfor zipen, men lå i mappa.
- `pakk_jury.sh`: begge find-kommandoene (byggemappa og leveranse/) ekskluderer nå også `.DS_Store` og `*.pyc`.
  Før var bare `__pycache__/` ekskludert i byggemappa. `sh -n` og `bash -n` ok.

## Sjekket, ingenting å fjerne
- .DS_Store: ingen, verken i arbeid/hack eller zipen.
- Logger/.venv/.git/.pytest_cache i zipen: ingen. `leveranse/ut/` og `home/` holdes ute av pakkinga.
- Hemmeligheter (api-key, token, password, sk-, AKIA, Bearer, KAGGLE, ANTHROPIC): ingen treff. Eneste treff på
  «secret» er ordet «Secretary» i NBIM-dataene.

## Meldt (ikke rørt, utenfor «bare søppel»)
1. `~` i 8 tekstfiler i zipen. Kjørestien leser ingen av dem, og README i zipen (linje 44) sier det alt:
   - `arbeid/verktoy/c1_tallvakt.py:22` `ROT = "<repo>"`: standardverdi, overstyres med `--rot`
     (sluttsjekk og KJOR.sh gjør det). Ufarlig, men ser rart ut for juryen som leser koden.
   - `arbeid/hack/levering/TREFFSIKKERHET.md:92` og `leveranse/kilder/TREFFSIKKERHET.md:92`: `cd <repo>/arbeid/hack/c1`
     i en oppskrift. Burde vært relativ.
   - `leveranse/demo_utskrift.txt:4`: FRYSVAKT-linja med full sti (utskrift, lages på nytt etter frysen av #2325/#1975).
   - `leveranse/kilder/dommer_ablasjon_v2.md`, `dommer_2090_streng_mot.md`: kommandoer fra dommerrapporter.
   - `README.md` og `levering/JURY_README.md`: nevner stien bare for å forklare den.
2. `leveranse/spor_npx/utkast_1100/` (eldre README og kravrespons fra kl. 11) og `spor_npx/run.sh|rapport.py|sporlogg.py`
   ligger i zipen. LESMEG.md merker dem som eldre utkast. Ikke søppel, men to README-versjoner i samme pakke kan forvirre.
   Forslag: ta utkast_1100/ ut av pakka (ikke frosset, krever bare `-not -path "*/utkast_1100/*"` i pakk_jury.sh) hvis
   speider/arkitekt er enig; jeg lot den stå fordi oppgaven sa bare søppel.
3. `leveranse/demo_utskrift.txt` er en kjøreutskrift (7,7 kB) som endrer seg ved hver demo. Den er ment som bevis,
   ikke søppel, men må regenereres etter frysen så FRYSVAKT-linja stemmer.

## Sluttsjekk etterpå
`C1_FRYS=/tmp/provefrys2422.json C1_JURYZIP=/tmp/jurypakke_c1_2422.zip bash arbeid/hack/levering/sluttsjekk.sh /tmp/c1_sluttsjekk_2422`
(egen prøvefrys, egne mapper, ingen kollisjon med smed4 #2423):
**SLUTTSJEKK GRØNN**, HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen, 224 s. Ny zip: 119 filer, 0 treff på
__pycache__/.DS_Store/.pyc. Prøvefrys, kald kopi, zip og loggmappe (ca. 3 GB) er slettet etterpå; `state/c1_frys.json` urørt.
