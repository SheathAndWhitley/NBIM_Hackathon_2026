# Case 1 (#2873): tre mønstre i NBIMs stemmeforklaringer, og om repo4 allerede fanger dem

Speider, 05.11 ca. 20:15. Kilder: NBIMs stemmeretningslinjer og stemmerapporter (URL-er per funn) og
`rationale_section`/`rationale_text` i dataene (`state/opplastet/20261105_114241_real_votes.csv`).
`rationale_section` er en GVG-paragraf (Global Voting Guidelines). Den er FORBUDT som trekk for samme
rad, men forklaringene fra *tidligere år* er historikk på linje med etikettene. Treff per tema er
regnet fra repo4 sine egne utdata (`arbeid/oppgave_2490/repo4_val.csv` = 2025 og `repo4_test.csv` = 2026),
slått sammen med fasiten på meeting_id|item_no. Alle MOT-rader telles her, også injeksjonsrader, så summen
for 2026 (66) er ikke 58 som i måleren. Bruk tallene som fordeling, ikke som F1.

## MOT per GVG-tema, 2019–2025 (678 MOT, 5,8 % av sakene)
| GVG | tema | MOT | trend 2020→2025 |
|---|---|---|---|
| 3.2 | ansvar: ansvarsfrihet og gjenvalg når styret ignorerer aksjonærer | 126 | 32 → 11, synker |
| 1.1/1.2/1.3 | uavhengighet, komiteer, CEO = styreleder | 164 | 13 → 44, øker |
| 3.3 | lønn (say-on-pay, opsjonsprogram) | 41 | 1 → 14, øker |
| 2.1 | tidsbruk (for mange verv) | 46 | 12 (2021) → 2 |
| 5.2 | for lite informasjon ("Other Business") | 35 | jevnt, rundt 6/år |
| tom | ingen forklaring | 123 | |

## Funn 1: Styreuavhengighet og CEO = styreleder (GVG 1.1–1.3) er det største hullet
- Kilde: retningslinjene 2023/2024/2025. Flertallet skal være uavhengige, og CEO og styreleder skal være to ulike personer.
  https://www.nbim.no/contentassets/cbee6983c7d044a6a6d2f286ed5fa3df/global-voting-guildeines_2025.pdf ,
  https://www.nbim.no/contentassets/34530895f32743a0a9528d6e55b73f6d/global_voting_guidelines_2024_uuweb.pdf
- Kilde: H1 2024 stemte NBIM mot CEO/styreleder i 311 amerikanske selskaper (ca. 20 % av dem), mest i USA og Sør-Korea.
  Uavhengighet var den største grunnen i H1 2025 (5,3 % av selskapene).
  https://www.nbim.no/en/responsible-investment/voting/voting-reviews/2024/our-voting-first-half-2024/web-report-our-voting-first-half-2024/ ,
  https://www.nbim.no/en/responsible-investment/voting/voting-reviews/2025/our-voting-first-half-2025/web-report-our-voting-first-half-2025/
- Data: repo4 traff 12 av 34 slike i 2025 og 9 av 13 i 2026, og bommet på 22 i 2025. Av de 27 bommene
  (1.1–1.3) i 2025 var USA 9 og India 8. Teksten er ofte bare «Elect Director <navn>», så tf-idf ser ingenting.
  **22 av 27 bom er i selskaper der NBIM hadde stemt MOT før, og 12 av 27 i selskaper der NBIM tidligere stemte MOT nettopp på grunn av uavhengighet.**
- Har repo4 det? Bare delvis. `prev_meeting_any_dev` og `prev_same_person` sier «avvik før», men ikke *hvorfor*.
  Tf-idf fanger «Non-Independent Non-Executive Director» i Asia, men ikke amerikanske navnevalg.
- **Trekk A (prioritet 1):** `hist_uavh_selskap` = antall/andel MOT med GVG 1.1–1.3 i samme selskap i tidligere år
  (merge_asof strengt før dato, som `hist_feats`), bare for DIRECTOR_ELECTION. En strukturell styresvakhet varer
  i flere år, mens et avvik på én enkeltsak gjør det ikke. Variant: `hist_ceo_chair_person` = personen fikk GVG 1.3-MOT før
  (gir CEO som også er styreleder hvert år).

## Funn 2: Ansvarsfrihet (GVG 3.2) har endret regime, så her trengs en vakt og ikke et trekk
- Kilde: retningslinjene sier at NBIM ikke gir ansvarsfrihet ved «reasonable doubt» om styrets handlinger, og 2023-utgaven
  lister dårlige resultater og risiko. https://www.nbim.no/contentassets/34530895f32743a0a9528d6e55b73f6d/global-voting-guidelines-2023.pdf
- Data: DISCHARGE MOT per år var 31, 31, 31, 20, **0, 1, 0, 0** (2019–2026). Altså var det slutt fra 2023. Tyskland står for 133 MOT
  totalt (27,8 % rate), mest herfra.
- Har repo4 det? Repo4 har ingen DISCHARGE blant falske positive i 2025–26, så modellen har lært bruddet (hist + år).
  **Konsekvens for natta:** regner noen tidsvekt eller treningsvindu, skal 2019–2022 ned for DISCHARGE. Trekk med «sakstype-rate
  over alle år» (som `hist_type_dev_rate` uten tidsvindu) bærer med seg det gamle regimet. Dette bør kontrolleres for tidsvekt-kandidaten (#2885).

## Funn 3: Lønn (GVG 3.3) øker, og bommene ligger i say-on-pay
- Kilde: en vesentlig del av lønna skal være aksjer låst i 5–10 år. NBIM stemmer mot uvanlig kostbare ordninger og mot rem.-komiteen
  når forrige lønnsforslag fikk lav støtte. https://www.nbim.no/contentassets/cbee6983c7d044a6a6d2f286ed5fa3df/global-voting-guildeines_2025.pdf
- Kilde: CEO-lønn var blant toppgrunnene for MOT i 2024. https://www.nbim.no/en/news-and-insights/reports/2024/responsible-investment-2024/web-report-responsible-investment-2024/
- Data: GVG 3.3 MOT per år var 1, 2, 6, 5, 13, 14 (2020–2025). Repo4 traff 7 av 14 i 2025 og 3 av 4 i 2026, men SAY_ON_PAY er også nest største
  kilde til falske positive (4 i 2025, 6 i 2026).
- Har repo4 det? Delvis. `prev_same_item` treffer når teksten er lik fra år til år (vanlig for say-on-pay). Det mangler en kobling fra lønn
  til direktørvalg: retningslinjen sier at rem.-komiteens medlemmer straffes etter lav lønnsstøtte. I proposal_text står
  ofte «Member of the Compensation/Remuneration Committee».
- **Trekk B (prioritet 2):** `rem_komite_x_lonnsmot` = direktørvalg med «compensation|remuneration committee» i teksten OG selskapet hadde
  say-on-pay-MOT i forrige år. Lite trekk (få rader), så forvent liten gevinst. Måles for seg.

## Andre ting (ikke prioritert)
- GVG 5.2 «Other Business» får alltid MOT (38/38), og repo4 tar 6 av 7 begge år. Det er dekket.
- MOT kommer i klynger: 428 av 678 MOT ligger i møter med 2 eller flere MOT. Det kan ikke bli et trekk uten å bruke etiketter fra samme møte,
  men det støtter regler som «flagg alle rem.-komitévalg i møtet når say-on-pay flagges» (etter regel, ikke etikett).
- Klima og bærekraft (GVG 5.3) er små: 21 MOT totalt, mest aksjonærforslag (SHP_SUSTAINABILITY 61 % MOT). Kategorien dekker dette allerede.

## Prioritert liste for smedene (regel i REGEL.md før måling, tre rullende år + 2023 som vakt)
1. Trekk A `hist_uavh_selskap` (+ variant per person for GVG 1.3), lagt til repo4-matrisen. Størst gap: 22 bom i 2025.
2. Kontroller at tidsvekt-kandidaten ikke vekter opp DISCHARGE-regimet fra før 2023 (sjekk FP på DISCHARGE i 2023 som vakt-år).
3. Trekk B `rem_komite_x_lonnsmot`. Lite, men tett koblet til retningslinjen.

Ingenting er målt med F1 ennå. Dette er en kartlegging, og tallene over er fordelinger av treff og bom i repo4 sine egne filer.

## Tillegg: skiller trekk A? (rå MOT-rate på direktørvalg, uten modell)
`arbeid/oppgave_2873/trekk_a_sjekk.py` (utdata i `trekk_a_sjekk.txt`). Selskapet er gruppert etter MOT i tidligere år:
| år | uavh-MOT før | annen MOT før | ingen MOT før |
|---|---|---|---|
| 2023 | 0,124 (19/153) | 0,042 (11/264) | 0,057 (25/447) |
| 2024 | 0,117 (31/265) | 0,036 (9/252) | 0,020 (8/404) |
| 2025 | 0,123 (32/261) | 0,082 (25/320) | 0,018 (6/338) |
| 2026 | 0,055 (13/235) | 0,051 (13/257) | 0,028 (7/252) |
*Hvorfor* NBIM avvek før, ikke bare *at* det avvek, gir 1,5–3 ganger høyere rate i 2023–2025. I 2026 er signalet svakt.
Raten er ikke F1, og repo4 har allerede «noen MOT før». Gevinsten må måles som trekk i matrisen etter bytteregelen.
