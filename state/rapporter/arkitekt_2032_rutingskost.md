# Arkitekt #2032: kostnad ved å rute 5–20 % av Case 1-sakene til menneske

## Hva koster det å sende flere saker til et menneske? (#2032)
Regnet med dommerens låste rutingsverdier fra #2017 (grense 0,1833 og bredder låst på val 2025), kjørt på **test 2026: 1246 forslag, 129 ekte MOT**. Som et år ser 2025 likt ut (1506 forslag, 136 MOT). «Ekstra MOT fanget» er sammenlignet med ingen ruting (83 av 129). **Timer per år** bygger på en antagelse vi ikke har målt: **20 min per rutet sak** (forvalteren avgjør saken uten agentens svar) og **10 min per MOT-flagg** (lese flagg og sitat, bekrefte eller avvise). Formel: timer = rutet × 20/60 + flagg × 10/60.

**Symmetrisk ruting** (sakene nærmest grensa går til menneske):

| til menneske | rutede saker 2026 (2025) | MOT-flagg å bekrefte | saker lest i alt | MOT fanget av 129 | **ekstra MOT fanget** | **timer per år** | timer per ekstra MOT |
|---|---|---|---|---|---|---|---|
| 0 % | 0 (0) | 221 | 221 | 83 (64 %) | – | 37 | – |
| 5 % | 56 (76) | 195 | 251 | 87 (67 %) | **+4** | 51 | 3,6 |
| **10 %** | 119 (151) | 171 | 290 | 91 (71 %) | **+8** | **68** | 3,9 |
| 15 % | 188 (226) | 144 | 332 | 94 (73 %) | **+11** | 87 | 4,5 |
| 20 % | 270 (302) | 116 | 386 | 95 (74 %) | **+12** | 109 | 6,0 |

**Skjev ruting** (#2017, c låst for best treffprosent, båndet ligger over grensa):

| til menneske | rutede saker 2026 (2025) | MOT-flagg å bekrefte | MOT fanget av 129 | **ekstra MOT fanget** | timer per år |
|---|---|---|---|---|---|
| 5 % | 70 (76) | 151 | 83 | **0** | 49 |
| 10 % | 122 (151) | 99 | 83 | **0** | 57 |
| 15 % | 201 (226) | 24 | 85 | +2 | 71 |
| 20 % | 262 (302) | 25 | 91 | +8 | 92 |

**Det viktigste:** skjev ruting opp til 10 % fanger **ingen** flere MOT-stemmer. Den sender sakene som alt var flagget MOT til menneske og fjerner falske flagg (138 → 44). Treffprosenten stiger (92,8 % i #2017), men det er samme 83 MOT-stemmer som før. Val 2025 viser det samme: 0 ekstra ved skjev 5 og 10 %, men +2/+9/+14/+18 ved symmetrisk 5/10/15/20 %.

**Anbefaling:** Bruk **symmetrisk 10 %**: ca. 120 saker i året til menneske, **8 flere MOT-stemmer fanget** (91 i stedet for 83 av 129), ca. **31 timer mer** analytikertid i året enn uten ruting (68 mot 37 t), altså rundt 4 timer per ekstra fanget MOT. Har analytikeren tid, gir 15 % tre MOT til for 19 timer til. Over 15 % blir det dyrt: 20 % gir bare én MOT mer for 22 timer. Velg skjev ruting bare hvis målet er færre falske flagg og høy treffprosent, ikke flere fangede MOT.

**Forbehold:** (1) Tallene er fra dataene **før** arrangørens rettede filer kl. 11:42 og må kjøres på nytt på dem (`arbeid/oppgave_2032/kost.py`). (2) Vi antar at mennesket avgjør rutede saker riktig, så «fanget» er en øvre grense. (3) Med 129 MOT-saker er +4 og +8 usikre: på val 2025 ga symmetrisk 5 % bare +2. (4) Minutter per sak er en antagelse. Med 30 min per rutet sak blir symmetrisk 10 % 88 t i året i stedet for 68 t.

Kode: arbeid/oppgave_2032/kost.py, utskrift kost.txt.
