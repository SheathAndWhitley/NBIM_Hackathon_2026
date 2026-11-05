# Case 1: demo.sh virker nå fra jury-zipen (#2442)

- pakk_jury.sh tar med `arbeid/hack/c1/vis_manussaker.py` og `arbeid/hack/c1/DEMO_MANUS.md`.
- demo.sh har fått zip-modus: mangler `fremmed.sh` (som i zipen), brukes pakkeroten selv som kald kopi.
  Er `sh KJOR.sh` ikke kjørt ennå: klar melding «DEMO STOPPET: kjør først sh KJOR.sh …», utgang 5.
  I repoet er oppførselen som før (fremmed.sh-veien er uendret).
- Ingen endring i modell, prediksjon eller frosne filer (demo.sh og pakk_jury.sh står ikke i c1_frys FILER).

Testet fra ny zip `/tmp/smed2_2442/jury_2442.zip` (104 filer, 1,0 MB), utpakket i en tom mappe:
1. `sh arbeid/hack/c1/leveranse/demo.sh` før KJOR.sh: DEMO STOPPET-meldingen, utgang 5.
2. `sh KJOR.sh`: FRYSVAKT GRØNN (15 filer), HOVEDTALL 0.476190, TALLVAKT GRØNN.
3. `sh arbeid/hack/c1/leveranse/demo.sh`: de tre manussakene (linje 276 / 89 / 15), «MANUS OK», så demo_vis.py, utgang 0.

Merk: zipen ble bygd før frysen (15:47), så sha256 er dagens filer; frysens zip må bygges på nytt etter kl. 16.
README nevner ikke demo.sh ennå (linje 72 sier demo ikke er med); den bør få én linje: «Demo: sh KJOR.sh, så sh arbeid/hack/c1/leveranse/demo.sh». Ikke endret av meg (README eies av andre oppgaver nå).

Merk commit acaaff7: tok også med JURY_README.md (+20/-1) som en annen agent alt hadde staget; innholdet er deres og urørt, bare commit-meldinga er min.
