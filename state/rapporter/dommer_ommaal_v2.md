# Dommer #2085: selvrapporterte Case 1-forsøk målt på nytt på måler v2

Målere: test 2026 = rundens måler #2034 `maaler_offisiell_v2.py {sti} test --data real` (9d81a418dd).
Val 2025 = ny egen måler på #2073 `... val --data real` (882009b35e). Ablasjonene er val-filer og skal ikke på test.

**Hvorfor de sto UGYLDIG:** #2073 og #2075 hadde ingen egen måler og falt tilbake til den GLOBALE måleren.
Den er fortsatt Name that LLM-måleren (8733327407). `forsok-ommaal` fant dem ikke heller, fordi den bare ser på
oppgaver med tittel «Hack…/Reserve…», ikke «Case 1…». Jeg målte dem med et eget skript
(`arbeid/oppgave_2085/ommaal*.py`), som skriver nye maaler-rader og [ommålt-merker på samme måte som tavla.

## Målt (alle reproduserer det som ble selvrapportert)
| gammel | ny | hva | før | målt |
|---|---|---|---|---|
| 1066 | 1069 | speider #2077, kjor_agent maskin alene, test | 0.4818 | 0.481752 |
| 1064 | 1070 | smed3 duality-trekk i miks h2, test | 0.4818 | 0.481752 (5 av 1578 prediksjoner ulike fra #1046, samme F1) |
| 1065 | 1071 | smed3 duality etterregel p+0,5, test | 0.4783 | 0.478261 |
| 1068 | 1085 | smed3 #2081 valgt base, test | 0.4818 | 0.481752 |
| 1044 | 1083 | smed3 utf kaldstart selskapsblind, test | 0.4706 | 0.470588 |
| 1045 | 1084 | smed3 utf kaldstart + historikktrekk, test | 0.5 | 0.500000 |
| 1041 | 1086 | smed3 utf tfidf+LR + sitat, test | 0.4805 | 0.480519 |
| 1047 | – | kaldstart-ruting, test | UGYLDIG | 0.481752 |
| 1053–1063, 1048–1052 | 1072–1082 m.fl. | ablasjon #2044, val 2025 | UGYLDIG/selvr. | full 0.5217, uten_historikk 0.3367, uten_sakstype 0.5057, uten_tekst 0.5057, uten_land 0.4916, med_mote 0.4894, bare_historikk 0.4819, bare_sakstype 0.1547 |

Ablasjonen står: historikken bærer modellen (uten den 0,52 → 0,34). Sakstype og tekst kan fjernes på val uten tap.

## Ærlig avvist (kan ikke måles)
- #1037, #1038, #1039 (smed2 #2044 rad,p-filer): 39 av 1578 test-id mangler, så måleren gir nan. Den samme modellen er målt
  komplett via kjor_agent (#1067/#1069: 0.481752), så hovedtallet står. Selvrapporterte 0.386 og 0.4748 er ikke verifisert.
- #1029, #1040: gammelt format (hash-id, 1247 rader), ikke real_votes. Hører til forrige datasett.
- #1036: resultat.json, ikke svarfil. #1035, #1043: ingen fil lagret (#1043 sier at prediksjonene er uendret fra #2037, som er målt 0.480519).

## Merk
- #1045 (0.500 på test) er høyere enn hovedtallet 0.4818, men er valgt på val. Test må ikke brukes til å velge den nå.
- Tre selvrapporterte forsøk fra før rundestart (11:42) står fortsatt på tavla (NY npx med duplikat-id, kjor_agent v3 0.474286).
  De er fra eldre data og ligger utenfor denne runden.
- Rettet: forsøkstavla viste UGYLDIG-rader selv etter at de var ommålt (commit i tavle.py).
- Anbefaling til arkitekten: «Case 1»-oppgaver bør arve rundens måler (eller den globale måleren byttes til Case 1 til kl. 20).
  Ellers lander hvert nytt forsøk uten egen måler som UGYLDIG mot NTL-måleren. `forsok-ommaal` bør også ta med «Case%».
