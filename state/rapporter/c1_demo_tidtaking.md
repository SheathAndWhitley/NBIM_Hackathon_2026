# Case 1: tidtaking av demo-manuset og forslag til kutt (#2415, 05.11 kl. 15.33)

Manus: `arbeid/hack/c1/DEMO_MANUS.md`. Kjørt: `sh arbeid/hack/c1/leveranse/demo.sh /tmp/c1_tid2415 --ny` (kald) og samme uten `--ny` (gjenbruk).
Utskrift og tider: `arbeid/oppgave_2415/` (kald.txt, kald_tid.txt, varm_tid.txt). `demo_utskrift.txt` er satt tilbake til slik den var.
Taletid: ord i «…» per del (Skjerm- og «Ærlig hvis spurt»-linjer tatt ut), regnet i 145 ord/min (manusets tempo) og 125 ord/min (realistisk med engelske sitater).

## Målt maskintid
| Steg | Målt | Manus sier |
|---|---|---|
| `demo.sh --ny` (fremmed.sh kald kopi + visning) | **71 s** (agenten alene 48 s), load ~3 | «42 s» |
| `demo.sh` som gjenbruker kopien | 0,22 s | – |
| `vis_manussaker.py` | 0,02 s | 0,02 s |

Resultat lik manus: F1 MOT 0,476190, `MANUS OK` (linje 276/89/15), TALLVAKT GRØNN. FRYSVAKT: «ikke frosset ennå» (ventet før 16).

## Tid per del (tale)
| Del | Manus-vindu | Ord | 145/min | 125/min | Ber om |
|---|---|---|---|---|---|
| Måltallet | 0:35 | 90 | 37 s | 43 s | metode |
| Treff Mobimo | 0:35 | 67 (18 eng.) | 28 s | 32 s | beslutningsstøtte |
| Bom LOTTE | 0:45 | 94 (13 eng.) | 39 s | 45 s | ærlig evaluering |
| Til menneske Kura Sushi | 0:40 | 71 (21 eng.) | 29 s | 34 s | beslutningsstøtte |
| Avslutning | 0:15 | 19 | 8 s | 9 s | (svak) |
| **Totalt** | 2:50 | **341** | **2:21** | **2:44** | |

Med ca. 5 s skjermbytte per sak (3 stk.) blir total **2:36–2:59**. Ordtallet i manusets hode (404) stemmer ikke med min telling (341); tida holder likevel under 3 min, men med lite slakk i lavt tempo.

## Funn
1. **Tidslinja brekker ved 0:35.** Manus starter `fremmed.sh` ved 0:00 og viser Mobimo fra den kalde kopien ved 0:35, men kopien er klar først ved ~1:11 (målt med landsbyen i gang). Mobimo-skjermen finnes ikke når den skal vises.
2. **Robusthet (40 % av vurderingen) sies ikke høyt i det hele tatt.** Ingen av de 341 ordene nevner feiltestene, injeksjonsvakta eller ukjent selskap. Tallene finnes i `ERLIG_EVALUERING.md` § 5 (16 av 16 testtyper uten krasj fra kald kopi) og under «Motstandstest» (6 av 16 nye tittel-instrukser slipper fortsatt forbi).
3. **«Tre saker til» (demo_vis.py, seed 0) gir ingen poeng i 3 min.** Sak 2 og 3 er samme selskap (Colruyt), samme P(MOT) 52 %, samme sitat; sak 3 heter «MOT bom», men gikk til menneske, så den viser ikke en stille feil. Den overlapper Kura Sushi.
4. **Mobimo-skjermen viser et retningslinjesitat som ikke passer** (NBIM 5.2.1 om årsrapporten). Manus har det bare som «Ærlig hvis spurt», men juryen ser det på skjermen.
5. Avslutningen (8 s) gjentar «kald start» og bruker ikke tida på noe juryen vekter.

## Konkrete kutt og flyttinger (prioritert; tekstendring går via #1975 etter 16)
1. **Flytt kald kjøring før demoen starter** (kjør `fremmed.sh /tmp/fremmed` 2 min før, eller bruk reserven fra #2325). Ved 0:00 vises `demo.sh` i gjenbruksmodus (0,22 s) med hovedtallet øverst. I avslutningen: «kjørt fra kald start for to minutter siden, 71 sekunder» i stedet for å late som den går live. Ingen tale må vente på maskinen.
2. **Bytt avslutningen mot én robusthetssetning** (~25 ord, +10 s): «Robusthet: 16 feiltester fra kald kopi, også injeksjon og ukjent selskap, ingen krasj, uklare saker går til menneske. Men 6 av 16 nye injeksjonsfraser slipper fortsatt gjennom.» Det siste er ærlig og teller på 60 %-delen.
3. **Kutt i Måltallet** (~20 ord, −8 s): «Å alltid følge styret gir høy treffprosent, men» kan bli «Følg styret treffer 96 %, men finner null MOT». Behold «første av hver type, ikke de peneste».
4. **Kutt i LOTTE** (~12 ord, −5 s): «fordi aksjonærene skal få stemme over endringer i vedtektene» kan ut; behold 17 stille / 11 til menneske / 38 falske MOT til menneske, det er det sterkeste ærlighetspoenget.
5. **Mobimo: si mismatchen selv** (+8 ord): «Retningslinjen i raden passer dårlig, det er begrunnelsen som bærer.» Den står på skjermen, bedre at vi sier det enn at juryen finner det.
6. **Ikke scroll til «Tre saker til»** i demoen; behold dem som reserve til spørsmål.

Netto etter 2–5: ca. 341 − 20 − 12 + 25 + 8 ≈ 342 ord, samme taletid (2:21–2:44), men robusthet og den kjente svakheten er med, og ingen ventetid på maskinen.
