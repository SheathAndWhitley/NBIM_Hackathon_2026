# Case 1: kjøreplan for siste time 18:30–20:00 (#2515)

Én kommando gjør sluttsjekken: `bash arbeid/hack/levering/sluttsjekk.sh` (frysvakt → fremmed.sh kald
kopi → tallvakt → hovedtall mot kv hack_levert → pakk_jury.sh → test_jury_zip.sh → tekstavtrykk).
Siste linje: `SLUTTSJEKK GRØNN …` eller `SLUTTSJEKK RØD: <grunn>`. Hovedtall F1 MOT = 0,476190.

## Hull som tettes før 18:30 (smed2, med #2519)
sluttsjekk.sh legger zipen i en ny `mktemp`-mappe i /tmp hver gang. Da finnes ingen fast
«siste grønne zip». Etter hver GRØNN kjøring kopieres zipen hit:
```
D=state/levering/c1_gronn; mkdir -p $D; Z=<zip-sti fra SLUTTSJEKK GRØNN-linja>
T=$(date +%H%M); H=$(git rev-parse --short HEAD)
cp "$Z" $D/jurypakke_c1_${T}_${H}.zip && shasum -a 256 $D/jurypakke_c1_${T}_${H}.zip >> $D/SHA256.txt
ln -sf jurypakke_c1_${T}_${H}.zip $D/SISTE_GRONNE.zip
```
Bare dommeren flytter `SISTE_GRONNE.zip`. Ingen sletter noe i mappa.

## Tidslinje
| Kl. | Steg | Eier | Ferdig når |
|---|---|---|---|
| 18:00 | Tallvakt + frys_fasit etter siste tekstendringer (#2519) | smed2 | tallvakt 0 avvik, commit |
| 18:30 | Sluttsjekk nr. 1 fra ren HEAD (#1972) | dommer | GRØNN; zip kopiert til c1_gronn, SHA logget |
| 18:30–19:00 | Siste rettinger i jurytekster (bare dømte funn) | smed4/smed | commit + tallvakt 0 avvik |
| 18:45 | Generalprøve av demoen fra zipen, stoppeklokke (#2493) | smed3 | tid og avvik notert på tavla |
| **19:00** | **STOPP for endringer i jurytekster og kode.** Etter 19:00 committer bare dommeren, og bare for et RØDT funn | dommer | `git log` viser siste commit ≤ 19:00 |
| 19:00 | Sluttsjekk nr. 2 fra HEAD etter stoppen | dommer | GRØNN → kandidat i c1_gronn |
| 19:30 | Kaldstart-verifisering: `test_jury_zip.sh SISTE_GRONNE.zip` i tom mappe + SHA mot SHA256.txt | dommer2 (uavhengig av dommer) | ZIPTEST GRØNN, HOVEDTALL 0,476190, SHA lik |
| 19:45 | Endelig: `til-guden` med zip-sti, SHA256, git HEAD og hovedtall | dommer | melding sendt, #1972 done |
| 20:00 | Frist. Ingenting endres etter 19:45 | alle | — |

Speider (#2483, #2517) leser og melder funn som tavleoppgaver til dommeren; skriver ikke i pakka etter 19:00.
Ordfører holder tavla rolig: ingen nye Case 1-oppgaver etter 19:00 utenom tilbakefall.

## Hvis noe blir rødt
| Rødt | Når | Tiltak |
|---|---|---|
| Sluttsjekk 1 RØD | 18:30 | Eier av grunnen (se RØD-linja) retter, sluttsjekk på nytt. Frist for retting 19:00 |
| Sluttsjekk 2 RØD på tekst/tallvakt | 19:00–19:30 | `git revert` av commiten som brøt det (aldri reset), sluttsjekk igjen. Ikke rettet 19:25 → tilbakefall |
| Sluttsjekk 2 RØD på frysvakt/hovedtall | 19:00– | Modellfila er rørt: `git checkout <frys-commit> -- <fil>` fra c1_frys.json, sluttsjekk igjen |
| Kaldstart 19:30 RØD, eller SHA ulik | 19:30 | **Tilbakefall**: forrige linje i `c1_gronn/SHA256.txt` som har GRØNN-ziptest. Kjør `test_jury_zip.sh` på den (ca. 1–2 min), sjekk SHA, sett `SISTE_GRONNE.zip` dit |
| Ingen grønn zip i c1_gronn | 19:30 | Siste kjente: `/tmp/jurypakke_c1.zip` (15:45) må ziptestes før den brukes. Er også den rød: send guden den kalde kopien + ærlig RØD-melding, ikke pynt |
| Maskin/tid tom | 19:50 | Lever det som sist var grønt, med SHA. En sjekket eldre pakke slår en usjekket ny |

## Regler for siste time
1. Bare grønne zipper med SHA i SHA256.txt kan leveres.
2. Etter 19:00: ingen endringer i jurytekster, kode eller modell. Unntak bare for RØDT funn, og bare av dommeren.
3. Kaldstart 19:30 kjøres av en annen agent enn den som bygde zipen.
4. Den siste meldingen til guden har fire ting: zip-sti, SHA256, git HEAD, F1 MOT. Resten finnes i c1_sluttkontroll.md.
