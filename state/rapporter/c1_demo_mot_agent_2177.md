# Case 1: demo-utskriftene mot agenten etter menneske-vaktene (#2177, smed, 05.11 kl. 13.10–13.25)

Kjørt: `bash arbeid/hack/c1/demo_saker_2026.sh /tmp/smed_2177`, `bash arbeid/hack/c1/demo_mangler_styret.sh`,
`sh arbeid/hack/levering/fremmed.sh /tmp/smed_2177_kald` + demo_vis.py i kald kopi.

**fremmed.sh GRØNN:** HOVEDTALL F1 MOT 0.476190 (TP 30, FP 38, FN 28 av 58), 183 av 1539 til menneske (11,9 %), tallvakt 136/136.

## Eksempler i DEMO_MANUS.md (arbeid/hack/c1/DEMO_MANUS.md)
| Sak | Svar | Rå score | Ruting/grunn | Sitat | Status |
|---|---|---|---|---|---|
| 1 Hainan Jinpan 2056685\|7 | FOR = | 0,912 = | manus: «nær grensen, logit 0,09, bånd 0,95». Agent: usikker, P(MOT) 0,19 i [0,15, 0,85) | – | **avvek, rettet** |
| 2 Arbonia 2041102\|2 | FOR = | 0,262 = | nei = | – | stemmer |
| 3 Eximbank 2039527\|11 | FOR = | 0,636 = | manus: nei. Agent: **ja**, ukjent selskap | – | **avvek, rettet** |
| 4 Nomad 2084542\|6 | FOR = | 0,451 = | nei = | NBIM-begrunnelse = | stemmer |
| 5 Klarna 2089598\|12 | FOR = | 0,257 = | manus: nei. Agent: **ja**, ukjent selskap | NBIM-begrunnelse = | **avvek, rettet** |
| 6 TV TOKYO 2089132\|3 | MOT = | 0,970 = | manus: «ikke sendt». Agent: **ja**, usikker P(MOT) 0,52 | GVG 1.1, ordrett likt manus | **avvek, rettet** |
| 7 Arbonia uten mgmt_rec | FOR = | 0,0075 = | 0 / 1 med samme grunn som i manus | – | stemmer |

Også rettet i manuset: «MOT-score er en rangering»-punktet (agenten viser nå kalibrert P(MOT), rå 0,91 = 19 %),
antallet til menneske 176 (11,2 %) → 183 av 1539 (11,9 %), `--til-menneske 10 %` → `--baand [0,15, 0,85)`,
TP/FP/FN 30/38/28 fylt inn. Trekket står: seed 17 er fortsatt første seed som holder kravet med ny ruting.
Kopi av manuset før retting: /tmp/smed_2177_DEMO_MANUS_for.md.

## Andre utskrifter
- `c1/leveranse/demo_utskrift.txt` (juryens demo, 12:57): **stemmer**, identisk med demo_vis.py på dagens kalde kopi.
- `levering/demo/` (Streamlit-app): stub + Vanguard N-PX, merket INTERN; viser ikke agenten. Ikke endret.
- `levering/KJORING_til_menneske_10.txt` og `_15.txt` (11:47): **utdatert, ikke rettet.** Gammel modus
  (1246 saker, logit-bånd `--til-menneske`, SCORE 0.474286), ikke dagens standard (real_votes, kalibrert bånd).
  Ingen fil i pakka peker på dem. Forslag: flytt til en `gammel/`-mappe eller lag dem på nytt med `--til-menneske 10/15`
  før pakken fryses (eier bestemmer).
- Merk: demo_saker_2026.sh printer `SCORE 0.4818` (avvik-tallet, 66). Hovedtallet er F1 MOT 0,476 (58); manuset bruker 0,476.
