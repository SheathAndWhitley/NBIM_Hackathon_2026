# Case 1 (#2747): jurylesing av de endrede linjene, zip 17:44 → 18:27

Diff: `jurypakke_c1_1744_7efa4da.zip` mot `jurypakke_c1_1827_0e3b14b.zip` (= SISTE_GRONNE). 44 filer endret, 282 +/- linjer,
nye filer: `KANDIDATER.md`, `kilder/c1_differanser_repo4.md`, `kilder/c1_lekkasje_effekt.md`, `kilder/c1_lekkasje_repo4.md`, `verktoy/` (testaar.sh m.m.).
Kildefilene i `kilder/` har stort sett bare fått merket «eldre frossen modell #2044» med tallvakt-kommentar. Måletall er ikke endret (lest; OK).

## Tallene i bestillingen
| påstand i endrede linjer | kilde | dom |
|---|---|---|
| repo4 mot huskeregelen +0,27 [+0,16; +0,36] (JURY_SPORSMAL, ERLIG) | c1_differanser_repo4.md:12 | OK |
| repo4 mot regel b2 (0,365) +0,15 [+0,04; +0,25] | c1_differanser_repo4.md:13 | OK |
| «15 avvik på 400 rader» (sp. 24) | c1_lekkasje_repo4.md:3 (15 avvik, 11 rader) | OK |
| «1 flagg på de 14 berørte radene i 2026», snitt 0,516 → 0,525 (sp. 24, KANDIDATER) | c1_lekkasje_effekt.md:7–17 (15/14/1; 0,5162 → 0,5254) | OK |
| «atten måter … den beste ga +0,014», krav +0,02 (JURY, ERLIG §7) | KANDIDATER.md:35 (18 målinger, beste #2701 +0,0135) | OK (avrundet riktig) |
| testaar.sh-sluttlinje 0.5057 / 0.5309 / 0.5120 / snitt 0.5162 (JURY, leveranse/README) | KANDIDATER.md:41, c1_lekkasje_effekt.md; testaar.sh finnes i zipen | OK |

## Andre endrede linjer
| fil:linje (ny zip) | endring | dom |
|---|---|---|
| README.md:39–40 | MOT-grense p_mot ≥ 0,232, rå 0,923 (var 0,191/0,919) | OK: stemmer med repo4-loggen `levering/kjor_agent_real_test2026.txt:3` (rå 0.92321, kalibrert 0.232) |
| leveranse/JURY_SPORSMAL.md sp. 15 (overskrift) | «Grensa (0,919 for repo4, 0,9232 for eldre frossen)» | **FEIL**: byttet om. Repo4 = 0,9232 (logg), eldre frossen #2044 = 0,9188 (hand_tall2.py:39). Rett: «0,923 for repo4, 0,919 for eldre frossen» |
| leveranse/README.md:24 | «MOT allerede ved kalibrert P(MOT) ca. 0,19 … grensen (rå 0,919 for repo4)» | **FEIL**: motsier README.md:39–40 i samme zip. Rett: «ca. 0,23 … (rå 0,923 for repo4)» |
| JURY.md ordliste, sp. 20/22/23/24, KANDIDATER-regel | én bytteregel (snitt +0,02 over 3 år, intet år −0,02) | OK, likt i JURY, ERLIG §7, MUNTLIG og KANDIDATER |
| JURY.md: 32 av 58, 26 oversett, 18 usett; 161 av 1539 (10,5 %), 11/29/18, 3/32 | | OK mot c1_repo4_tall_2592 / leveranse/README (TP 32 FP 35 FN 26) |
| JURY.md pkt. 8, MUNTLIG: 164 av 1578 (10,4 %), 161 med fasit | | OK, intern samstemmighet |
| ERLIG/README: avvik-F1 0,529 [0,42; 0,63]; maskin alene 0,478/0,552/0,512 | | OK mot loggen (TEST 2026 avvik F1 0.5294) |
| ERLIG og leveranse/README: «val ligger på 0,530» | | OK i praksis (2025-året 0,5309); merk at loggens val-F1 på avvik er 0,5251. Ikke rødt |
| DEMO_MANUS_5min_tilfeldige.md:1 | merket ELDRE, skal ikke leses høyt (den har fortsatt 0,919 og 19 %) | OK, siden den er merket |
| DEMO_MANUS.md / demo_utskrift.txt: Lundbeck p_mot 0.2321 | | OK, og konsistent med ny grense 0,232 (rett over grensen) |
| kilder/*: «Eldre tall»-boks + tallvakt-kommentarer | | OK, ingen måletall endret |

## Til smed (før tekststopp 19:00)
To FEIL, begge er bare tekst, i `arbeid/hack/c1/leveranse/`:
1. `JURY_SPORSMAL.md` sp. 15: bytt til «0,923 for repo4, 0,919 for eldre frossen».
2. `README.md:24`: «ca. 0,19» → «ca. 0,23», «rå 0,919 for repo4» → «rå 0,923 for repo4».
Ingen andre røde funn i de endrede linjene.
