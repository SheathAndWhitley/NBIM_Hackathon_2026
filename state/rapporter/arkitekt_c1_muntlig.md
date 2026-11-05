# Case 1: 3-minutters muntlig manus for juryen (#2632)

Filer: `arbeid/hack/c1/leveranse/MUNTLIG.md` (BYTT) og `arbeid/hack/c1/reserve_staar/MUNTLIG.md` (STÅR).
424 ord, cirka 3 min ved 140 ord/min. Fem bolker: problem, metode (tre rullende testår og byttegrensen fastsatt på forhånd), ærlig tall, forbehold og ruting til menneske.
Diff mellom utgavene: tittelen, tallavsnittet (dom + F1 + TP + KI) og rutingslinja. Alt annet er likt. Variantlinjene er merket med `<!-- VARIANT -->`.

Tallene er sjekket mot kilden (KP):
| tall i manus | kilde | BYTT | STÅR |
|---|---|---|---|
| F1 MOT test 2026 | README.md:8 / reserve_staar/README.md:8 | 0,512 | 0,476 |
| TP av 58 | README.md:9 | 32 | 30 |
| KI | README.md:8 | [0,40; 0,62] | [0,36; 0,59] |
| til menneske | README.md:10 | 164/1578, 10,4 % | 188/1578, 11,9 % |
| 1539 saker med fasit, 58 MOT | README.md:8 | ja | ja |
| følg styret 96 %, F1 0 | README.md:29 (96,2 %) | ja | ja |
| regel +0,02 / −0,02, tre år | ERLIG_EVALUERING § 7 | ja | ja |
| 12 kandidater, 11 falt | § 7 benk A (6) + benk B (6) | ja | ja |
| 2024 +0,051, 2025 +0,017, snitt +0,034 | § 7 forbeholdet | ja | ja |
| KI snitt [−0,005; +0,078] | README.md:12 | ja | ja |
| bånd [0,15; 0,85) | README.md:5 | ja | ja |

STÅR-dommen bruker samme ordlyd som reserve_staar/README.md:12 («besto regelen, men pakken … ble ikke grønn i tide»).
