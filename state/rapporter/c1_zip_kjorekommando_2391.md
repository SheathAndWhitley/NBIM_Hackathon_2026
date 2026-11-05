# Case 1: kjørekommandoen i zipens README og kravrespons er rettet (#2391, smed2, 05.11)

Avvik 1 i dom #2348: `c1/leveranse/README.md` og `kravrespons.md` sa «ett kall: `bash arbeid/hack/c1/leveranse/kjor.sh`».
Den kommandoen feiler i zipen fordi `levering/fremmed.sh` og `hack/maaler.sh` ikke er med.

## Endret (bare tekst, ingen tall og ingen frosne filer)
- `README.md` linje 12: «… i jury-zipen er det `sh KJOR.sh` fra mappa `c1_stemmeagent/`.»
- `README.md` etter kodeblokka: ny avsnitt **I jury-zipen**: kjør `sh KJOR.sh`; `kjor.sh` og `demo.sh` virker bare i repoet
  (fremmed.sh og hack/maaler.sh er ikke med i zipen).
- `kravrespons.md` linje 7: «med ett kall: i jury-zipen `sh KJOR.sh` fra mappa `c1_stemmeagent/`, i repoet
  `bash arbeid/hack/c1/leveranse/kjor.sh` fra rotmappa. Begge måler også …»

Valgte tekst framfor å legge fremmed.sh og maaler.sh i zipen: fremmed.sh leser landsbystier, og pakkelista er godkjent som den er.

## Disk
Slettet `/tmp/jurytest_zip` (2,9 GB, fra #2346; test_jury_zip.sh lager den på nytt). Rota gikk fra 2,1 til 3,8 GB ledig.

## Ny zip og test
Første ombygging (15.16) stoppet på **TALLVAKT RØD**: `ERLIG_EVALUERING.md:41` står «F1 0,476190», men måleren skriver 0.4762.
Det er en linje smed3 la til i #2386 mens hen fortsatt jobbet i fila, så jeg rørte den ikke.
NB: pakk_jury.sh sletter den gamle zipen før den bygger, så etter 15.16 fantes det ingen `/tmp/jurypakke_c1.zip` før neste grønne bygging.
