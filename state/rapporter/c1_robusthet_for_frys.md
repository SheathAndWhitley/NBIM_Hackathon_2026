# Case 1: robusthetstesten (#2063) kjørt på nytt fra kald kopi før frysen (smed3 #2380, 05.11 ca. 15:30)

**Resultat: ingen krasj, 16/16 testtyper gir samme utfall som før, og hovedtallet fra kald kopi er F1 MOT 0,476190.**
Ingen frosne filer er endret. Den kalde kopien for demoen (`/tmp/c1_kald`) er ikke rørt.

## Hva som ble kjørt
- Fersk kald kopi av dagens pakke: `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_2380` (uv sync 1 s, kjøring 41 s).
  HOVEDTALL F1 MOT mot styret (v3 --score mot): **0,476190**. TALLVAKT GRØNN. Frysvakt: ikke frosset ennå (c1_frys.json finnes ikke).
  Kopiens `_pred_uten_ruting.csv` er byte-lik den leverte `kjor_agent_real_maskin_alene.csv`, og kopiens `pred_maaler.csv`
  er byte-lik `kjor_agent_real_pred_maaler.csv`.
- De 14 testtypene fra #2063 pluss de 2 fra #2071 (samme frø 2063, samme 6 grunnsaker, samme møte-id-er), kjørt med kopiens
  eget python under `env -i` (ingen landsbystier): `python3 -I arbeid/oppgave_2380/robusthet_kald.py /tmp/c1_kald_2380`.
  Inndata lest fra kopiens `real_test_input.csv`; test-CSV-ene skrevet til /tmp. Hver testtype er en egen agentkjøring i ny tom utmappe.
- Før-tallene er `arbeid/oppgave_2063/tabell.md` (siste kjøring i #2063/#2071, landsbymiljø, eldre pakke).

## Testtype -> utfall, før og nå
| testtype | saker | før (#2063/#2071, landsbymiljø) | nå (#2380, kald kopi) | likt |
|---|---|---|---|---|
| original (nye møte-id) | 6 | ok, 1/6 til menneske, 1 MOT | ok, 1/6 til menneske, 1 MOT | ja |
| tomt felt (tekst/type/selskap/dato) | 6 | rutet til menneske (6/6) | rutet til menneske (6/6) | ja |
| ugyldige verdier (dato, id, item_no, AGAINST/ABSTAIN) | 8 | ok, 6/8 til menneske, 0 MOT | ok, 6/8 til menneske, 0 MOT | ja |
| ukjent selskap | 6 | rutet til menneske (6/6) | rutet til menneske (6/6) | ja |
| ukjent forslagstype | 6 | rutet til menneske (6/6) | rutet til menneske (6/6) | ja |
| lang tekst (40 799 / 5 025 / 100 000 tegn) | 3 | rutet til menneske (3/3) | rutet til menneske (3/3) | ja |
| injeksjon (engelsk og norsk, tagg/JSON) | 6 | rutet til menneske (6/6) | rutet til menneske (6/6) | ja |
| duplikat-id | 2 | ok, 1/2 til menneske, 0 MOT | ok, 1/2 til menneske, 0 MOT | ja |
| kjent sak uendret | 3 | ok, 1/3 til menneske, 1 MOT | ok, 1/3 til menneske, 1 MOT | ja |
| kjent sak, endret tekst/styret/type | 3 | rutet til menneske (3/3) | rutet til menneske (3/3) | ja |
| tom fil (bare overskrift) | 0 | ok (0 saker ut, rc 0) | ok (0 saker ut, rc 0) | ja |
| manglende kolonne proposal_type | 3 | rutet til menneske (3/3) | rutet til menneske (3/3) | ja |
| --sak: tomt objekt {} | 1 | rutet til menneske (1/1) | rutet til menneske (1/1) | ja |
| --sak: null-felt | 1 | rutet til menneske (1/1) | rutet til menneske (1/1) | ja |
| --sak: ukjent selskap og type | 1 | rutet til menneske (1/1) | rutet til menneske (1/1) | ja |
| --sak: injeksjon | 1 | rutet til menneske (1/1) | rutet til menneske (1/1) | ja |

«ok» = rc 0, alle saker ut, FOR/MOT med grunn eller rutet med grunn. «uten grunn» var 0 i alle 16 tester, før og nå.
Krasj = rc ulik 0 eller færre saker ut enn inn: **ingen, verken før eller nå.** Full tabell med MOT/FOR/sek/merknad: `arbeid/oppgave_2380/ut/tabell.md`.
De to ikke-rutede sakene i «ugyldige verdier» er AGAINST/ABSTAIN, som normaliseres til MOT/AVSTÅ (bevisst, #2063).
Den ene ikke-rutede i «duplikat-id» er den første forekomsten, som er riktig.

## Hva som er annerledes i rutingsgrunnene (ikke i utfallet)
1. Rutingsgrunnen for grensesaker heter nå «usikker: kalibrert P(MOT) 0,75 i båndet [0,15, 0,85)» i stedet for
   «nær grensen: |logit-avstand| 0,90 <= bånd 0,95». Det er bånd-rutingen fra #2128/#2132. Samme saker rutes.
2. Den nye høflighetsvakta (#2237, `injeksjon_hoflig.py`) legger «instruksjonslignende tekst i forslaget» på fem oppdiktede
   forslag som før bare hadde én grunn: «Convert 40% of corporate treasury into Bitcoin», «Relocate legal domicile to a lunar
   special economic zone», «Pay non-executive directors in company NFTs», «Approve dissolution of the company» og «Approve
   asteroid mining venture». Alle fem ble rutet før også (ukjent type, endret felt eller ukjent selskap), så utfallet er likt.
   Vakta slår ut på sjeldne ord som aldri står i NBIMs titler, og ablasjonen (c1_injeksjonsvakt_ablasjon.md) målte 0 falske
   alarmer på ekte test 2026. Svakhet verdt å vite for juryen: på ordentlige, men uvanlige forslag kan grunnen «instruksjonslignende»
   være misvisende, selv om rutingen til menneske er riktig. Ingen endring foreslått før frysen.

## Filer
- `arbeid/oppgave_2380/robusthet_kald.py` (testen i kald kopi), `arbeid/oppgave_2380/sammenlign.py` (før/nå-tabellen),
  `arbeid/oppgave_2380/ut/{tabell.md,resultat.json,pred_maaler_kald.csv,KJORING_kald.txt}`, `arbeid/oppgave_2380/fremmed.log`.
- Gjenskap: `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_2380 && python3 -I arbeid/oppgave_2380/robusthet_kald.py /tmp/c1_kald_2380 && python3 -I arbeid/oppgave_2380/sammenlign.py arbeid/oppgave_2063/tabell.md arbeid/oppgave_2380/ut/tabell.md` (ca. 2,5 min).

## Merknad til dommeren
`tavle forsok --sti arbeid/oppgave_2380/ut/pred_maaler_kald.csv` ble avvist: «måleren er endret på disk (8733327407 -> 474eae7bc8);
dommeren må sette den på nytt». Tallet 0,476190 over er derfor regnet direkte med `maaler_offisiell_v3.py ... test --data real --score mot`
(samme kall som hack_levert), ikke via forsøkstavla. Dommeren bør sette måleren på nytt så forsøk kan meldes igjen før frysen.
