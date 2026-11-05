# Case 1 (#2691): dom over nødplanen for 19:30: GRØNN

dommer2, 05.11 kl. 17:45–17:55. Planen: `state/rapporter/c1_nodplan_1930.md` (#2688). Ingen leveransefiler rørt.

## Dom: GRØNN
Grunn: begge reservene finnes med riktig sha, og planens egen kommando (`test_jury_zip.sh`) kjører rang 2 grønt fra kald start, noe arkitekten selv ikke fikk gjort fordi disken var full.

## Hva jeg sjekket selv
| Rang | Fil | sha256 i planen | målt | kald start |
|---|---|---|---|---|
| 1 | SISTE_GRONNE.zip -> jurypakke_c1_1744_7efa4da.zip | e48426cd…cda031 | e48426cd…cda031 LIK (også lik SHA256.txt) | utpakket i /tmp/nodplan_2691, `sh KJOR.sh`: exit 0, frysvakt grønn, HOVEDTALL 0.512000, tallvakt 25 filer/176 påstander/0 avvik, 45 s |
| 2 | reserve_staar/jurypakke_staar_2640.zip | 32de94c3…ae417d7 | 32de94c3…ae417d7 LIK | planens kommando `sh arbeid/hack/levering/test_jury_zip.sh <zip> /tmp/nod_test_2691`: exit 0, ZIPTEST GRØNN, HOVEDTALL 0.476190, TP 30 FP 38 FN 28 TN 1443 STEMMER, ny prediksjonsfil sha = frossen fil, 56 s |
| 3 | jurypakke_c1_1701_frossen_2587.zip (= reserve_staar/jurypakke_c1_2587.zip) | af3dd758…7d3e | af3dd758…7d3e LIK, begge kopier | ikke kjørt (siste skanse, dekket av rang 2) |

Underlag bytte2572_c1_frys.json: d45ed794… LIK planen.

## Merknader (ikke røde)
- Rang 1-testen min gikk med bare 153 MB ledig fordi KJOR.sh bruker uv sin delte pakkebuffer. Planens `test_jury_zip.sh` bruker tom buffer og trenger plassen planen sier (minst 2 GB). Nå: 6,3 GB ledig etter #2683.
- Planen foreslår `rm -rf /tmp/staar_ovelse_2631` (15 GB). Den mappa holdes åpen av en claude-prosess (pid 15521) kl. 17:47. Den som rydder bør sjekke `lsof +D` først, så ikke en pågående økt faller.
- Planens rapport kom kl. 17:49, fire minutter etter at dommen ble tildelt. Zip- og sha-sjekkene var gjort før den forelå; kommandosjekken etter.

## Rydd
Mine testmapper /tmp/nodplan_2691 og /tmp/nod_test_2691 er slettet. Logger: ingen beholdt utover denne rapporten.
