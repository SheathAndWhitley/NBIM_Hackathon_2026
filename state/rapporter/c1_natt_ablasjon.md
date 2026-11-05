# Case 1: hvilke trekk bærer lederen? Drop-one-ablasjon på 2023-2026 (smed2, #2888)

Leder = #2701 (repo4 + av-regel), natt-måleren `arbeid/c1_natt/mal_kandidat.sh --torr` (F1 MOT mot styret). Ett ledd tatt ut om gangen,
alt annet likt (abl_rull.py miks, grense valgt på val T-1, av-regelen på etterpå). Kontrollkjøringen av hele lederen er bit-lik
frossen repo4 og gir nøyaktig 0,3736/0,5269/0,5375/0,5246. Forklaring, ikke byttekandidater. Kode og REGEL.md: `arbeid/oppgave_2888/`.

Endring i F1 MOT mot lederen (negativ = leddet hjelper):

| fjernet | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | F1 snitt |
|---|---|---|---|---|---|---|
| ingenting (leder) | 0 | 0 | 0 | 0 | 0 | 0,5297 |
| prev_same_item | -0,0122 | **-0,0686** | -0,0247 | +0,0226 | **-0,0236** | 0,5061 |
| historikken (--hist 0) | -0,0109 | **-0,0523** | -0,0282 | +0,0048 | **-0,0253** | 0,5044 |
| prev_same_person | +0,0021 | +0,0106 | -0,0250 | +0,0057 | -0,0029 | 0,5268 |
| prev_meeting_any_dev | -0,0090 | -0,0084 | +0,0014 | +0,0098 | +0,0009 | 0,5306 |
| hist_type_dev_rate | -0,0129 | +0,0073 | -0,0190 | +0,0271 | +0,0051 | 0,5348 |

## På vanlig norsk
- **prev_same_item** (stemte NBIM mot på samme sak sist): det tyngste repotrekket; uten det faller treffet 0,024 i snitt og 0,069 i 2024.
- **Historikken** (våre egne løpende avviksrater per selskap/forslagstype): like viktig; uten den faller treffet 0,025, mest i 2024 og 2025.
- **prev_same_person** (stemte NBIM mot samme styremedlem sist): liten og ustabil nytte; hjelper i 2025, ikke i de andre årene.
- **prev_meeting_any_dev** (avvek NBIM noe sted på selskapets forrige møte): bærer nesten ingenting når de andre er med; alle år innen ±0,01.
- **hist_type_dev_rate** (avviksrate for forslagstypen): gir ikke målbar nytte; uten det blir 2026 bedre og 2025 verre, netto støy.

## Ærlige forbehold
- Hvert tall er én kjøring. Svingninger på ±0,02-0,03 i ett år ses også for trekk som netto betyr null, så bare de to
  store fallene (prev_same_item og historikken) er sikre nok til å kalles bærende.
- 2026 går motsatt vei for nesten alle: å fjerne et ledd hjelper litt der. Lederens styrke er 2024-2025.
- «Uten hist_type_dev_rate» gir snitt 0,5348 (+0,0186 over frossen), men er valgt etter å ha sett testårene og bryter
  2025-vakta (-0,0123 mot leder). Det er ikke en kandidat, og skal ikke selges som en.

## Jurysetning
«Agenten bæres av to ting: om NBIM stemte mot på samme sak før, og våre egne løpende avviksrater per selskap; tar vi ut
en av dem, faller F1 på MOT fra 0,530 til 0,505. De tre andre repotrekkene flytter mindre enn tilfeldig år-til-år-støy.»
