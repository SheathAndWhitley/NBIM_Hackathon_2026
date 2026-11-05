# Case 1: de 17 tallene uten kilde er funnet eller rettet (#2276, dommer, 05.11 14:20)

Tallsjekken kl. 14:08 (`state/rapporter/c1_tallsjekk.md`) fant 17 tall i pakka uten kilde. Da jeg startet stod 9 igjen (andre hadde lagt til kilder for 0,269 m.fl. i mellomtida). Jeg har regnet hvert av dem ut på nytt fra prediksjonsfilene og datafila, bare med stdlib. Modell og prediksjoner er ikke rørt.

**Resultat:** `python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke` gir nå **IKKE FUNNET 0** (2143 tall i 16 filer). Ett tall i pakka var feil og er rettet: avvik i train i `levering/METODE.md` stod som 574, datafila gir **575**.

## Kilden som ble laget
`arbeid/hack/c1/lag_tall_kilder.py` skriver `arbeid/hack/c1/tall_kilder_ut.txt` (kilde B for tallsjekken). Kjøretid ca. 40 s (bootstrap). Innhold og hva det dekker:

| del | kilde | tall i pakka | reprodusert |
|---|---|---|---|
| 1 menneske_tabell.py på oppgave_2132/agent.csv | TP/FP/FN per rutingsoppsett | F1 0,779 (TP 37 FP 0 FN 21), 0,294, 0,828, 0,269 (TP 9 FP 0 FN 49) | eksakt |
| 2 diff_ki.py (#2103), klyngebootstrap per selskap, seed 0, 2000 trekk, mot «følg styret» | oppgave_2134/*_test.csv | KI i JURY.md: [0,359; 0,590], [0,252; 0,492], [0,203; 0,378], [0,072; 0,124], [0,301; 0,533], punkt 0,476/0,365/0,287/0,097/0,415 | eksakt |
| 3 tellinger per splitt | real_votes, rader med against_board satt | train 9876 / 504 / **575**, val 1909 / 99 / 103, test 1539 / 58 / 66 | 574 var feil |
| 4 aritmetikk båndet konfidens ≥ 0,6 | TP 9 FP 0 FN 17 TN 1330 | accuracy 98,75 %, følg styret 98,1 %; Clopper-Pearson 9/26 = 17,2–55,7 %, 30/58 = 38,2–65,0 %, 30/68 = 32,1–56,7 % | eksakt |
| 5 terskelrader | p_avvik i oppgave_2103/full_{val,test}.csv | hele tabellen TREFFSIKKERHET.md:70–77 (0,70–0,97), bl.a. test P 0,189 ved 0,80 (41/217), val P 0,735 og test P 0,742 ved 0,97 | eksakt, alle 14 rader |
| 6 treffsikkerhet_ki.py (#2185, frø 2185) | oppgave_2132/agent.csv | bootstrap recall 39,1–65,2 %, presisjon 32,8–56,2 % | eksakt |
| 7 øvre grenser i NESTE_VERSJON.md (ny fil 14:15) | oppgitte TP/FP/FN | 0,578, 0,601, 0,537, 0,634 | eksakt |

## De 17 enkeltvis
- **0,779 og 0,269** (BESLUTNINGSSTOTTE, JURYSVAR, README, EN_SIDE, 7 steder): F1 for «maskin + menneske» og «gulv» i rutingstabellen. 2·37/(2·37+0+21) = 0,7789 og 2·9/(2·9+0+49) = 0,2687. Del 1.
- **0,252** (JURY.md:45): nedre KI-grense for regel b2. Del 2, eksakt med seed 0.
- **9876, 504, 574** (METODE.md:15): 9876 saker med fasit og 504 MOT mot styret stemmer. Avvik (against_board = 1) i train er 575, ikke 574. Rettet i teksten. Kontrollert både med `year`-kolonnen og møtedatoens år, og med og uten injeksjonsfilter: 575 alle veier.
- **571** (BESLUTNINGSSTOTTE.md:46) og **367** (JURY_SPORSMAL.md:61): var allerede funnet i kilde B da jeg startet (noen la inn kilde mellom 14:08 og 14:11). Ikke etterprøvd av meg.
- **98,75 %** (TREFFSIKKERHET.md:31): (9+1330)/1356. Del 4.
- **55,7 %** (TREFFSIKKERHET.md:45): Clopper-Pearson øvre grense for 9/26. Del 4.
- **0,189** (TREFFSIKKERHET.md:72): test-presisjon ved terskel 0,80 = 41/217. Del 5.

## Stikkprøve av «avledet»-tallene
De 14 som var merket «avledet A» (kan være tilfeldig brøk) er sjekket: 1443 er TN, 2185 og 2115 er frø/oppgavenummer, 65,2 % / 0,735 / 0,742 er nå reprodusert (del 5–6). 0,845 (ERLIG_EVALUERING.md:59, historikkregel) står i teksten uttrykkelig som tall fra et gammelt skript, med det nye tallet 0,097 ved siden av. Lar den stå.

## Merknad til tallsjekken (arkitekt, #2271)
`50,63` i NESTE_VERSJON.md:37 er ikke et tall, men linjehenvisningen i «[`c1_feil_stabilitet.md:50,63`]». KODE-regexen tar `\S+\.md` før backtick-alternativet når linja begynner med «[», og lar «:50,63» stå. Den ble likevel «funnet B» ved tilfeldighet. Liten regex-ordensfeil, ikke rettet av meg.

## Kommandoer
```
python3 -I arbeid/hack/c1/lag_tall_kilder.py          # skriver tall_kilder_ut.txt (ca. 40 s)
python3 -I arbeid/verktoy/c1_tallsjekk.py --bare-ikke  # skal gi IKKE FUNNET 0
```
