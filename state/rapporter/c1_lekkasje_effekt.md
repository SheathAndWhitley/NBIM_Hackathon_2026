# Case 1 (#2744): hvor mye betyr samme-dags-lekkasjen for repo4s treff?

**Svar: nesten ingenting for selve lekkasjen, men modellvalget er følsomt.** Når repo4s fire historikktrekk regnes
bare fra møter med strengt tidligere dato, endres 0, 0 og 1 flagg på de berørte radene i testårene 2024, 2025 og 2026.
F1 på MOT flytter seg likevel −0,008 / −0,016 / +0,052 (snitt +0,009), fordi valideringsåret da velger en annen C og grense.

**Setning juryen kan lese:** Regnet med historikk bare fra strengt tidligere dato endres ett flagg på de 14 berørte
radene i 2026, og F1 på MOT over de tre testårene går fra 0,516 til 0,525 (−0,008, −0,016, +0,052 per år); forskjellen
skyldes at modellvalget på valideringsåret skifter, ikke at samme-dags-historikken ga treff. Frossen modell står (#265).

## Tabell (F1 på MOT mot styret, offisiell måler `maaler_aar.py --data real --score mot`)
| testår | F1 før (repo4, levert) | F1 etter (strengt tidligere dato) | differanse | flagg endret / berørte rader / endret på berørte |
|---|---|---|---|---|
| 2024 (val 2023) | 0,5057 | 0,4973 | −0,0084 | 18 / 13 / 0 |
| 2025 (val 2024) | 0,5309 | 0,5153 | −0,0156 | 7 / 23 / 0 |
| 2026 (val 2025) | 0,5120 | 0,5636 | +0,0516 | 15 / 14 / 1 |
| **snitt** | **0,5162** | **0,5254** | **+0,0092** | |

«Før» er gjenskapt fra kald mappe og treffer dom #2713 eksakt (0,5057/0,5309/0,5120). Etter-tallet er én kjøring per år,
samme oppsett (C/grense valgt på T−1, trent på år < T), bare trekkene endret.

## Hva som skjer
- Trekkene er nesten like (korrelasjon p før/etter 0,957 / 0,991 / 0,997). Snittet av prev_meeting_any_dev_ja går fra 0,305 til 0,334,
  fordi «siste møte» nå er siste dato (alle møter den dagen), ikke bare møtet med høyest meeting_id.
- Det som flytter F1 er modellvalget på valideringsåret: 2024 velger C=0,1 i stedet for 3; 2025 C=1 i stedet for 3;
  2026 samme C=3 men grense 0,9386 i stedet for 0,9232, så antall flagget faller fra 70 til 55 (presisjon 0,48 → 0,60).
- Lekkasjen selv: 0/0/1 endrede flagg på de berørte radene. Samme-dags-historikken var altså ikke det repo4 traff på.

## Vurdering mot #265
Etter-varianten gir snitt +0,009 over frossen (krav +0,02) og ett år −0,016 (grense −0,02). Den kvalifiserer ikke til bytte,
og dette er ærlighetstall, ikke en kandidat. Frossen modell og c1/leveranse er ikke rørt.

## Metode og kontroll
- `arbeid/oppgave_2744/strengt.py`: kopi av NBIM-repoets `add_history` der grupperingen er (meeting_date, company_id) i stedet for
  (meeting_date, meeting_id); etikettene oppdateres først etter alle selskapets møter samme dato. Ellers identisk.
- `arbeid/oppgave_2744/abl_strengt.py`: kopi av `c1/leveranse/verktoy/abl_rull.py` med `--strengt 1` som bytter `ballot.add_history`
  før `load_real()`. Leser leveransens ballot-kopi, skriver ingenting der.
- KP1: brute force fra #2731 mot den strenge varianten: 0 avvik på prev_same_item, prev_same_person, hist_type_dev_rate; 13 på
  prev_meeting_any_dev, alle fordi brute.py tar siste meeting_id på siste dato. KP2 med «siste dato»: **0 avvik på alle fire** (400 rader).
- Berørte rader: `arbeid/oppgave_2731/berorte_rader.csv` (177 rader, 33 møter).
- Kjør på nytt (ca. 20 sek): `cd arbeid/oppgave_2744/ut && bash ../kjor.sh`. Logger og måleutskrifter ligger i `arbeid/oppgave_2744/ut/`.
