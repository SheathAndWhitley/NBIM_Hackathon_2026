# Case 1: robusthetstallene i ERLIG_EVALUERING.md § 5 kjørt på nytt med én kommando (smed3 #2395, 05.11 kl. 15.25)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

**Resultat: alle tall i § 5 kom ut likt fra en ny kald kopi. Én kommando gir alle: `sh arbeid/oppgave_2395/reprod.sh` (2 min 36 s, fra roten av repoet).**
Kommandoen lager en fersk kald kopi i `/tmp/c1_kald_2395` med `fremmed.sh`, kjører de 16 feiltestene med kopiens eget python under `env -i`,
sammenligner med før-tabellen fra #2063/#2071 og teller forslagene som har fått den nye rutingsgrunnen. Full utskrift: `arbeid/oppgave_2395/reprod_utskrift.txt`.
Ingen frosne filer er rørt. Demokopien `/tmp/c1_kald` er ikke rørt. #2380 sine utdata (`arbeid/oppgave_2380/ut/`) er ikke overskrevet; de nye ligger i `arbeid/oppgave_2395/ut/`.

| tall i § 5 | kommando (fra roten av repoet) | fikk |
|---|---|---|
| hovedtall F1 0,476 på MOT mot styret (0,476190) | `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_2395` (steg 1 i reprod.sh), linja `HOVEDTALL` | 0.476190, P 0,4412 R 0,5172, TP 30 FP 38 FN 28, TALLVAKT GRØNN | <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 --> <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
| kald kopis svarfil byte-lik den leverte | `cmp /tmp/c1_kald_2395/ut/_pred_uten_ruting.csv arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` og `cmp .../pred_maaler.csv arbeid/hack/levering/kjor_agent_real_pred_maaler.csv` (steg 2) | begge byte-like (cmp stille, rc 0) |
| 16 feiltester, ingen krasj | `python3 -I arbeid/oppgave_2380/robusthet_kald.py /tmp/c1_kald_2395 arbeid/oppgave_2395/ut` (steg 3) | 16 rader, krasj = nei i alle, 0 «uten grunn» i alle |
| 16 av 16 testtyper likt utfall som 04.11 (til menneske, MOT, krasj, uten grunn) | `python3 -I arbeid/oppgave_2380/sammenlign.py arbeid/oppgave_2063/tabell.md arbeid/oppgave_2395/ut/tabell.md` (steg 4) | «16/16 testtyper byte-likt i krasj/MOT/menneske/uten grunn. KRASJ NÅ: ingen» |
| like mange saker til menneske og like mange MOT per testtype | samme som over, kolonnene «til menneske» og «MOT» i `arbeid/oppgave_2395/ut/tabell.md` mot `arbeid/oppgave_2380/ut/tabell.md` | identiske i alle 16 rader (6/6, 6/8, 6/6, 6/6, 3/3, 6/6, 1/2, 1/3, 3/3, 0, 3/3, 1/1 ×4; MOT 1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0) |
| grensesaker heter «usikker: kalibrert P(MOT) i båndet [0,15, 0,85)», ikke «nær grensen» | `grep -o "usikker: kalibrert P(MOT) [0-9.]* i båndet" arbeid/oppgave_2395/ut/tabell.md \| sort -u` (steg 6); «nær grensen» finnes bare i før-tabellen `arbeid/oppgave_2063/tabell.md` | 2 varianter (P 0,52 og 0,75); 0 treff på «nær grensen» i ny tabell |
| fem oppdiktede forslag har fått grunnen «instruksjonslignende tekst i forslaget», alle rutet til menneske før også | `python3 -I arbeid/oppgave_2395/fem_nye.py` (steg 5; før = `arbeid/oppgave_2063/ut/resultat.json`, nå = `arbeid/oppgave_2395/ut/resultat.json`) | «før 3, nå 8, ANTALL NYE 5»: Bitcoin-kasse, månedomisil, NFT-lønn, oppløsning, asteroidegruve; alle `til_menneske=1` før og nå; ingen mistet grunnen |

## Det som ikke sto rett i tabellen før
Tallet «fem» i § 5 var lest ut av to tabeller for hånd i #2380. Nå er det en kommando (`fem_nye.py`), og den gir samme fem. De tre andre
sakene som har grunnen i dag (AI-sjef, og to lange tekster som begynner med «The Board recommends shareholders approve»), hadde den også i #2063.
Totalt 8 saker utenfor injeksjonstestene har grunnen nå; § 5 sier «fem» fordi det er de nye. Det står nå eksplisitt i § 5 («3 før mot 8 nå»).

## Endringer gjort
- `arbeid/oppgave_2380/robusthet_kald.py`: valgfri utmappe som andre argument (ellers skrev kjøringen over #2380 sine utdata). Testlogikken er uendret.
- Nytt: `arbeid/oppgave_2395/reprod.sh` (én kommando), `arbeid/oppgave_2395/fem_nye.py`, `arbeid/oppgave_2395/ut/` (tabell.md, resultat.json, sammenlign.md, fremmed.log, robusthet.log), `reprod_utskrift.txt`.
- `ERLIG_EVALUERING.md` § 5: én setning med kommandoen og hva den skriver ut.

## Forbehold
- Kjøretid for `fremmed.sh` var 77 s denne gangen (41 s i #2380); maskinen hadde andre kjøringer samtidig. Tallene er like.
- Kommandoen forutsetter repoet (`arbeid/oppgave_2063/`, `arbeid/oppgave_2380/`, `arbeid/oppgave_2395/`). Jurypakkelista (#2333) tar med hele `arbeid/hack/c1/leveranse` (så denne fila og § 5 følger med), men ikke de tre oppgavemappene med skriptene. Fra jury-zipen alene kan § 5 derfor ikke kjøres på nytt; det er pakkerens valg om de tre mappene skal med (ca. 20 små filer).
- Forsøkstavla avviste `tavle forsok --sti arbeid/oppgave_2395/ut/pred_maaler_kald.csv` med «måleren er endret på disk (8733327407 -> 474eae7bc8); dommeren må sette den på nytt», samme som i #2380. Tallet 0,476190 over er derfor fra `fremmed.sh` sitt eget v3-kall, ikke fra forsøkstavla. Dommeren må kjøre `tavle maaler --oppgave 2395 --kmd ...` før kalde kontrollmålinger kan meldes der.

## Kontrollkjøring nr. 2 (økt 2, 05.11 kl. 15.29, `sh arbeid/oppgave_2395/reprod.sh /tmp/c1_kald_2395 arbeid/oppgave_2395/ut2`)
Samme kommando kjørt en gang til mot ny utmappe `ut2/`: HOVEDTALL 0,476190, TALLVAKT GRØNN, begge svarfiler byte-like, sammenlign.md byte-lik første kjøring (16/16), <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
8 saker med grunnen «instruksjonslignende» utenfor injeksjonstestene (de samme fem nye). `diff ut/tabell.md ut2/tabell.md` viser avvik bare i kolonnen for kjøretid i sekunder
(4,3–5,8 s), alle tellingene (saker, til menneske, MOT, krasj, uten grunn) og rutingsgrunnene er identiske. Tallene i § 5 er dermed bekreftet fra kald kopi to ganger.
