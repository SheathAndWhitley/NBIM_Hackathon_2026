# Case 1: går usikre saker til et menneske? Sjekk av frossen #2044 på test 2026 (#2293, smed3)

Kjørt 05.11 14:20 med frossen agent (frysvakt OK, modell urørt): `kjor_agent.py --ut arbeid/oppgave_2293/ut`.
Regnestykket «MOT mot styret» er gjenskapt fra maaler_offisiell_v3.py og gir 0,476190 på alle 1539, likt hovedtallet.
Skript: `arbeid/oppgave_2293/sjekk_ruting.py arbeid/oppgave_2293/ut/agent.csv`.

## Svar på akseptkravet
| | saker | rutet til menneske | med begrunnelse |
|---|---|---|---|
| usikkerhetsbåndet, kalibrert P(MOT) i [0,15, 0,85) | 127 | 127 (100 %) | 127, alle «usikker: kalibrert P(MOT) x i båndet» |
| rutet av andre grunner, utenfor båndet | 61 | 61 | 70 «ukjent selskap», 1 «instruksjonslignende tekst» (noen har flere grunner) |
| rutet totalt | 188 av 1578 (11,9 %) | | 0 rutet uten begrunnelse |

F1 på MOT mot styret (måler v3-regel, bare rader med fasit):
| delmengde | n | TP | FP | FN | P | R | F1 MOT |
|---|---|---|---|---|---|---|---|
| alle (hovedtallet) | 1539 | 30 | 38 | 28 | 0,441 | 0,517 | **0,476** |
| ikke-rutede, maskinen svarer alene | 1356 | 9 | 0 | 17 | 1,000 | 0,346 | **0,514** |
| i båndet (det mennesket får) | 122 | 20 | 38 | 7 | 0,345 | 0,741 | 0,471 |

## Funn
- Rutingen virker som beskrevet: alle 127 i båndet går til menneske, hver med begrunnelse. Ingen sak er rutet uten grunn.
- Maskinen alene gjør null falske MOT: alle 38 falske MOT ligger i båndet og havner hos mennesket. Det er bra beslutningsstøtte.
- Svakheten er på den andre siden: 17 av 26 ekte MOT blant de ikke-rutede sier agenten trygt FOR på. Alle 17 har P(MOT) under 0,09
  (0,0 til 0,0896), så å senke bånd-grensen til 0,10 fanger ingen av dem (0 saker ligger i [0,10, 0,15)). De bommene er
  modellens, ikke rutingens.
- Båndet fanger 20 av 27 ekte MOT der det er fasit, men med 38 falske per 20 ekte: mennesket må lese 122 saker for å finne 20.
- Rå grense 0,919 tilsvarer kalibrert 0,191, så 63 av 74 MOT-flagg ligger i båndet. Bare 10 MOT-flagg sendes ut uten menneske,
  og 9 av dem er riktige (1 er mot et styre som selv sa MOT, teller ikke som MOT mot styret).

## For juryen (én setning)
Av 1578 saker svarer maskinen alene på 1390 med null falske MOT (F1 MOT 0,514, presisjon 1,0); 188 går til menneske med
skriftlig grunn, og alle 127 i usikkerhetsbåndet er blant dem. Det agenten ikke klarer, er 17 ekte MOT den er trygt feil på.
