# Case 1: tallvakt og sitatkontroll etter juryrettingene (#2170, dommer2, 05.11 kl. 13.25)

**Dom: TALLVAKT GRØNN, 0 sitatfeil.** Alle fem tallene oppgaven nevner stemmer med en godkjent rapport eller med en kald kjøring.
#2167 og #2168 var ferdige før kontrollen.

## Tallvakta
- Kald kopi `sh arbeid/hack/levering/fremmed.sh /tmp/d2_2170`: utgang 0, F1 MOT 0,476190, TP 30 FP 38 FN 28, 188/1578 og 183/1539 til menneske. TALLVAKT GRØNN.
- I landsbyen (README endret kl. 13.11, etter kopien) ga vakta først 2 avvik på `levering/README.md:10`: «recall 51,7 %, presisjon 44,1 %».
  Tallene var **riktige**. Vakta leste prosent som brøk (51,7 mot 0,5172). **Rettet i `arbeid/verktoy/c1_tallvakt.py`**: «P/R/recall/presisjon x %» sammenlignes nå med 100·måletallet.
  Negativtest: «recall 51,8 %» gir 1 avvik. Etter rettingen: `14 filer, 139 påstander stemmer, 0 avviker`, utgang 0. (README sier nå R 0,517, P 0,441.)

## De fem tallene
| Tall | Hvor i pakka | Kilde | Dom |
|---|---|---|---|
| b2 0,365 [0,25; 0,49] (P 0,317 R 0,431) | EN_SIDE:23, JURYSVAR:23, JURY_SPORSMAL:77, kravrespons:14, JURY:11 | `c1_enkle_regler_og_hist1.md:13` | stemmer |
| 0,415 [0,30; 0,53] (P 0,458 R 0,379) | EN_SIDE:48, BESLUTNINGSSTOTTE:61, JURY_SPORSMAL:31, BEGRENSNINGER:10-11, ERLIG_EVALUERING:29, kravrespons:15, JURY:15 | samme rapport `:14`, målt #1123 | stemmer |
| +0,11 [0,01; 0,22] mot b2 | JURY:17, kravrespons:21, JURY_SPORSMAL:77 | samme rapport `:13`, `:36` | stemmer |
| 17 av 58 MOT ingen ser | EN_SIDE:5,40, BESLUTNINGSSTOTTE:10,33,69 | regnet selv fra kald `agent.csv` + fasit: av 58 MOT er 17 FOR og ikke til menneske (21 MOT i sonen, 9 MOT utenfor, 11 FOR i sonen) | stemmer |
| 15 av 20 avgjørende sitat | EN_SIDE:8, kravrespons:4 | `c1_sitat_verifisert.md` (#2115): 15/20, 4 delvis, 1 feil | stemmer |

Andre nye tall fra rettingene, regnet fra kald kjøring: accuracy 95,7 % (1473/1539) mot følg styret 96,2 % (1481/1539), 58/1539 = 3,8 %,
12,5 av 100 lest (183 i sonen + 9 MOT-flagg utenfor, alle 9 ekte MOT), 1,1 per 100 (17/1539), «88 %» uten flagg = 1347/1539 = 87,5 %. Alle stemmer.

## Sitatkontrollen
`python3 -I arbeid/oppgave_2166/alle_sitat.py /tmp/d2_2170/ut/agent.csv`: 1578 rader, alle med sitat, 74 MOT, 0 MOT uten sitat.
15 unike sitater, alle ordrett på NBIMs nettside og i PDF-en. Nummerkontrollen (`nummer.py`) stemmer for alle 15.

## Merk
Modellfrys kl. 16 og #1975 kan endre tallene igjen. Kjør `python3 -I arbeid/verktoy/c1_tallvakt.py` etter hver endring i pakka.
