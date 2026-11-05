# Case 1: kan vi stole på P(MOT)? Kalibrering av frossen #2044 miks h2 (smed3 #2109)

**Svar: nei, ikke som prosent.** p_mot som agenten viser (c1_real.py, `p_mot`/`raa_score`) er et
**rangsnitt** (snitt av rangprosentilen til logreg og LightGBM, train.py linje 92), ikke en sannsynlighet.
Den er nesten jevnt fordelt på [0,1] mens bare 4–5 % av sakene er MOT.

Kjørt: `arbeid/oppgave_2109/kal.py` (train.py uendret, `--variant miks --hist 2`, samme C=3 og grense 0,9188).
Ingen ny trening av modellen, ingen terskelendring.

| | n | MOT | basisrate | snitt p | Brier | ECE (10 like brede bøtter) |
|---|---|---|---|---|---|---|
| val 2025, rå p | 1909 | 103 | 0,054 | 0,456 | 0,244 | **0,402** |
| test 2026, rå p | 1539 | 66 | 0,043 | 0,484 | 0,278 | **0,441** |
| test 2026, isotonisk tilpasset på val 2025 | 1539 | 66 | 0,043 | 0,059 | 0,031 | 0,016 |
| test 2026, konstant = val-basisrate 0,054 | 1539 | 66 | 0,043 | 0,054 | 0,041 | 0,011 |

Rå p har dårligere Brier enn å si 5,4 % på alle saker. Det er like ille på val som på test,
så det kommer ikke av drift. Det kommer av skalaen.

Reliabilitet, test 2026, rå p (val 2025 i parentes):

| bøtte | n | snitt p | faktisk MOT-andel |
|---|---|---|---|
| 0,0–0,5 | 826 (1098) | ~0,27 | 0,012 (0,011) |
| 0,5–0,8 | 490 (550) | ~0,65 | 0,020 (0,042) |
| 0,8–0,9 | 135 (165) | 0,847 | 0,059 (0,115) |
| 0,9–1,0 | 88 (96) | 0,954 | 0,432 (0,510) |

Det som teller for brukeren er MOT-flaggene (p ≥ 0,919): snitt p **0,965**, faktisk MOT **0,465** på test
(0,593 på val). Og like over grensen (0,919–0,95) er bare 2 av 18 MOT på test (11 %, val 50 %).
Rangeringen er god (PR-AUC 0,52), men tallet er ikke en sannsynlighet.

Isotonisk kartlegging tilpasset på val 2025 (monoton, så flagg og F1 endres ikke) gir på test:
p ≈ 0,99 → 11 av 11 MOT, ≈ 0,75 → 3/6, ≈ 0,53 → 19/51, ≈ 0,19 → 8/64, ≈ 0,025 → 25/1406.
Snitt kalibrert P(MOT) på MOT-flaggene er 0,61. Det betyr omtrent «litt bedre enn myntkast», ikke «sikker».

Rundens måler (`maaler.sh svar_iso.csv real_test`, frossen modell, isotonisk p_avvik og konfidens):
F1 MOT 0,4818 (TP 33, FP 38, FN 33), som før. PR-AUC faller 0,525 → 0,489 fordi isotonisk lager
likeverdier. Forsøk #1111 står **selvrapportert**: tavla avviste `--sti` fordi måleren er endret på disk
(sha 8733327407 → 474eae7bc8). Dommeren må sette måleren på nytt.

**Ordene i svaret må tones ned.** Rå p_mot over 0,9 må ikke vises eller leses som «sikker» eller «96 %».
Et MOT-flagg er riktig i 47 % av tilfellene på test 2026 (59 % på val). Den kalibrerte P(MOT) på
flaggene er ca. 0,6. Riktige ord: «mulig MOT, les begrunnelsen». Bare p ≥ 0,95 (rå) bør kalles «sannsynlig MOT» (58 % på test, 63 % på val).
BESLUTNINGSSTOTTE.md sier allerede «bruk som rekkefølge, ikke prosent». Det stemmer og bør stå.
**METODE.md linje 58 («isotonisk … ECE på test 0,025») gjelder den gamle #1997-modellen, ikke agenten som
leveres nå.** Den linja må rettes eller merkes, ellers påstår vi kalibrering vi ikke har.

Billig tiltak etter frysen (gjelder bare visningen, ikke flagget): vis `iso(p)` fra val 2025 ved siden av rangen,
ECE 0,016 på test. Det er guden og ordføreren som avgjør om det er lov etter kl. 16.

Filer: `arbeid/oppgave_2109/{kal.py, svar.py, kal_resultat.json, val_pred.csv, test_pred.csv, svar_iso.csv}`.

## #2132 (smed3): kalibrert P(MOT) og «send til menneske» er nå i agenten og demoen

- `c1_real.py`: `p_mot` er nå **kalibrert P(MOT)**. Den er isotonisk tilpasset på modellens val 2025-score (trent <2025) og brukt på inn-sakene.
  `raa_score` er fortsatt rangsnittet. Modellen, grensen 0,9188 og MOT-flagget er de samme som før (frys kl. 16).
- `til_menneske` brukes nå som standard når kalibrert P(MOT) er i **[0,15, 0,85)** (valgt i #2128), pluss de gamle grunnene: injeksjon, ukjent selskap eller type, datafeil og MOT uten sitat.
  Den gamle logit-regelen finnes fortsatt med `--til-menneske PROSENT`. Båndet kan endres med `--baand LO,HI`.
- `pred_maaler.csv` har fortsatt rå score som `p_avvik`, så PR-AUC (0,5245) ikke får likeverdier.
- Kjørt fra kald kopi (`sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_2132_demo`): demoen viser P(MOT) i prosent og «SEND TIL MENNESKE: JA/nei» for 3 trukne saker.
  Sak 2 er nå «usikker, sendt til menneske», og den er trukket blant de 122 sakene i båndet.
- Måler v3 `--score mot`, test 2026: **F1 MOT 0,4762** (TP 30, FP 38, FN 28). Det er uendret fra før endringen, både med og uten ruting.
  Til menneske: 183 av 1539 saker (11,9 %). 122 av dem er i båndet, og resten har de andre grunnene. Før var tallet 223.
- Kalibrering i kald kopi, test: snitt q 0,059 mot basisrate 0,043, Brier 0,0305.
  Ærlig svakhet: trinnet q ≈ 0,52 (41 saker) var MOT i bare 29 % av sakene på test. q ≈ 0,58 (9 saker) var MOT i 78 %.
  Midten av skalaen er altså grov, men den ligger inne i båndet og går til menneske.
- Med båndet havner alle 38 falske MOT på test 2026 hos et menneske. Derfor trekkes demo-sak 3 («MOT bom») nå uansett ruting.
- Filer: `arbeid/oppgave_2132/agent.csv` (svarfila), `pred_maaler.csv` og `KJORING.txt`.

## #2148 (dommer2): målt på rundens måler, stemmer med frossen #2044

- Måler for oppgaven: `python3 -I arbeid/hack/c1/maaler_offisiell_v3.py {sti} test --data real --score mot`, sha **de049083d9** (samme som #2123 kald kopi).
- `tavle forsok --sti arbeid/oppgave_2132/agent.csv` → forsøk **#1121, 0,47619, målt** (ikke selvrapportert). MOT mot styret: TP 30 FP 38 FN 28 (58 MOT i fasit), P 0,441 R 0,517.
- Alle 1578 anbefalinger i smed3s `agent.csv` er identiske med `arbeid/oppgave_2123/agent_kald.csv` (frossen #2044 miks h2). Agenten og hovedtallet bruker samme modell. **Ingen avvik i F1.**
- Merknad, ikke avvik: på `agent.csv` gir måleren PR-AUC 0,29 (den leser kalibrert `p_mot` med likeverdier), mot 0,52 på `pred_maaler.csv` (rå score). Den viser også «0 til menneske», fordi `agent.csv` har `til_menneske`, ikke `konfidens`. PR-AUC og rutingsandel skal derfor siteres fra `pred_maaler.csv`/KJORING.txt (0,5245; 183 = 11,9 %), ikke fra denne målingen.
- Den globale måleren står på sha 8733327407 (Name that LLM), og det er grunnen til at smedenes `--sti` blir avvist. Case 1-forsøk må ha egen måler per oppgave.
