# Case 1: hva de 28 bommene har felles (sak 2192)

smed2, 05.11. Test 2026, 58 MOT mot styret (samme definisjon som måler v3 `--score mot`). Frossen agent miks h2 maskin alene: TP 30, FP 38 (måleren; 41 flagg utenfor MOT når AVSTÅ og andre avvik telles med), **FN 28**. Ruting fra standardkjøringen sak 2132 (`<arbeidsmappe>/oppgave_2132/agent.csv`). Modellen er ikke rørt.

Kommando (bare stdlib): `python3 -I <arbeidsmappe>/oppgave_2192/bommene.py` (full utskrift i `<arbeidsmappe>/oppgave_2192/bommene.txt`).

## Tabell: de 28 bommene
| gruppe | bom (FN) | funnet (TP) | MOT i alt | funnet-andel |
|---|---|---|---|---|
| styrevalg | 13 | 15 | 28 | 54 % |
| andre styresaker (OTHER_MGMT) | 5 | 1 | 6 | 17 % |
| revisor | 4 | 3 | 7 | 43 % |
| vedtekter | 2 | 1 | 3 | 33 % |
| aksjeemisjon | 2 | 0 | 2 | 0 % |
| aksjeprogram / regnskap | 1 / 1 | 0 / 0 | 1 / 1 | 0 % |
| forslag fra styret / fra aksjonær | 27 / 1 | 29 / 1 | 56 / 2 | 52 % / 50 % |
| **USA** | **7** | **0** | **7** | **0 %** |
| Japan / Kina / India | 3 / 3 / 3 | 4 / 0 / 1 | 7 / 3 / 4 | 57 / 0 / 25 % |
| DM / EM | 15 / 13 | 14 / 16 | 29 / 29 | 48 / 55 % |
| Texas Capital Bancshares | 3 | 0 | 3 | 0 % |
| LOTTE Chemical, S.F. Holding, Klarna, Nomad Foods | 2 hver | 0, 0, 0, 1 | | |
| selskap med MOT før 2026 / aldri MOT før / nytt i data | 20 / 4 / 4 | 28 / 0 / 2 | 48 / 4 / 6 | 58 / 0 / 33 % |
| eneste MOT i møtet | 17 | 0 | 17 | 0 % |

## Hvor bommene havner
- 11 av 28 går til menneske i standardkjøringen (7 i båndet, 3 ukjent selskap, 1 injeksjonsvakt). **17 ser ingen**, alle med kalibrert P(MOT) ≤ 0,09.
- De 17 usette: 8 styrevalg, 4 andre styresaker, 2 vedtekter, 1 aksjeprogram, 1 revisor, 1 regnskap. **7 av 17 er i USA.**
- **Hovedårsak blant de usette: nye amerikanske saker om aksjonærrettigheter.** 5 saker i 2026: flytting fra Delaware til Texas (Dell, Texas Capital), høyere terskel for aksjonærforslag og utsettelse av møtet (Texas Capital), supermajoritet for vedtektsendring (CrowdStrike). **Alle 5 er MOT, agenten flagget 0 og sendte 0 til menneske.** Før 2026 finnes 7 slike saker i dataene, 0 MOT. Modellen lærer av fortida, og der stemte NBIM aldri mot dette. Det er en ny praksis i 2026 som ikke står i treningsdataene.
- Resten er spredt: 17 av 28 er eneste MOT i møtet (agenten finner MOT best når hele møtet er omstridt), og selskaper uten MOT før 2026 treffes aldri (0 av 4).
- Terskelen er streng: 15 av 28 har rå skår ≥ 0,6 (flagg fra 0,919), men å senke den koster mye lesing: 483 ikke-flaggede saker har skår ≥ 0,6, og bare 17 av dem er MOT.

## Ærlig forbehold
Søkeordene for aksjonærrettighets-saker (`state of incorporation|reincorporat|supermajority|threshold to submit|adjourn meeting`) er funnet ved å lese bommene på test. Regelen er derfor ikke validert og skal ikke inn i modellen. Den er et råd om hva et menneske bør se på, ikke et målt resultat. n = 5.

## Avvik funnet i pakka
`SVAKHETER.md` § 2 sa «alle India-saker går til et menneske (sak 2079)». I standardkjøringen sak 2132 går 25 av 103 India-saker til menneske, og én India-bom (Varroc, regnskap) er usett. Setningen er rettet til det som faktisk skjer.

## Lagt inn
- `arbeid/hack/c1/SVAKHETER.md` § 2: ny punkt om aksjonærrettigheter i USA, India-setningen rettet.
- `arbeid/hack/levering/BESLUTNINGSSTOTTE.md` «Når agenten tar feil»: hvilke saker et menneske bør se ekstra på.
