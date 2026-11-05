# Case 1 #2792: tallvakt og tallsjekk på tekststopp-zipen (forhåndskjøring, zipen fantes ikke ennå)

Kl. 18:52 finnes ingen #2549-zip. #2549 starter 19:00, og tidsboksen min (10 min) går ut før det.
Nyeste zip er `state/levering/c1_gronn/jurypakke_c1_1827_0e3b14b.zip` (fra før README-rettingen 9d5c855).

## Hva er sjekket nå
- Tallvakt på landsbyen (HEAD 9d5c855): `32 filer, 197 påstander om hovedtallet stemmer, 0 avviker`, F1 MOT 0,5120 (TP 32, FP 35, FN 26). OK.
- Samme skript mot 18:27-zipen (forrige økt): tallvakt 0 avvik, alle fem README-punktene NEI (ventet, zipen er eldre enn rettingen).

## De fem README-punktene (#2785) i kilden GITHUB_README_UTKAST.md (landsbyen, 9d5c855)
| Punkt | Kilde nå | 18:27-zip | Tekststopp-zip |
|---|---|---|---|
| 1 ett hovedtall, snitt merket «ikke hovedtall» | JA | NEI | ikke sjekket |
| 2 regelen skrevet før byttet | JA | NEI | ikke sjekket |
| 3 2044 merket forrige modell | JA | NEI | ikke sjekket |
| 4 arbeidsmapper forklart | JA | NEI | ikke sjekket |
| 5 39 saker uten styreanbefaling | JA | NEI | ikke sjekket |

## Når zipen finnes (etter 19:00)
    sh arbeid/oppgave_2792/sjekk_zip.sh state/levering/c1_gronn/<ny zip>
Skriptet pakker ut i /tmp, kjører tallvakt og tallsjekk mot den utpakkede roten og grepper de fem punktene.
Alle fem må stå JA i både GITHUB_README_UTKAST.md og README.md i zipen. Tar 1 minutt. Dette bør kjøres
som egen oppgave ca. 19:05, før dommer2 dømmer #2668.
