# Case 1 (#2906): trekkliste fra NBIMs stemmeforklaringer, uten lekkasje

Speider, 05.11 ca. 20:10. Bygger på #2873 (`c1_natt_nbim_monstre.md`). Råtall: `arbeid/oppgave_2906/sjekk.py` → `sjekk.txt`
(bare injection_flag==0, historikk = år < testår). Dette er rå MOT-rater per gruppe, **ikke F1**. Gevinst avgjøres i måleren etter REGEL.md.

## Lekkasjeregel for alle trekkene (les først)
- `rationale_section` er satt **bare på MOT-rader** (0 FOR-rader har den). Den er altså etiketten delt opp etter grunn.
  Samme rad og samme møte: forbudt. Tidligere møter: lov, på linje med `hist_feats`.
- Er informasjonen der FØR stemmedatoen? Ja for tidligere møter: NBIM publiserer stemme og begrunnelse løpende (før/ved møtet),
  så en forklaring fra et møte med dato strengt før radens dato er offentlig. Samme dato: nei (`allow_exact_matches=False`).
- Bygg som `hist_feats` med `--hist 2` (det repo4/kjor.sh bruker): `merge_asof` på dato, strengt før, aldri år > til_aar.
  Gjelder også treningsrader, så en rad aldri ser sin egen forklaring.
- 2019 har ingen forklaringer (0 %), så trekkene er 0 før 2020. Det er riktig, ikke en feil.
- Nøkkel for person: samme `_navn()` som `person` i `abl.py` (bare DIRECTOR_ELECTION).

## Trekkene, rangert
| # | trekk | gjelder | retning | før dato? | rå MOT-rate 2023 / 2024 / 2025 / 2026 (treff/n) | sammenlign |
|---|---|---|---|---|---|---|
| 1 | `pers_uavh_mot_for`: personen fikk MOT med GVG 1.1–1.3 før | DIRECTOR_ELECTION | MOT | ja | 0,71 (10/14) / 0,63 (15/24) / 0,67 (16/24) / 0,41 (7/17) | person med MOT av annen grunn: 0,44 / 0,21 / 0,25 / 0,27 |
| 2 | `selsk_uavh_mot_for`: selskapet hadde MOT med GVG 1.1–1.3 før (antall, log1p) | DIRECTOR_ELECTION | MOT | ja | 0,12 (19/153) / 0,12 (31/265) / 0,12 (32/261) / 0,06 (13/235) | basis direktørvalg 0,064 / 0,053 / 0,070 / 0,045 |
| 3 | `selsk_lonn_mot_for`: selskapet hadde MOT med GVG 3.3 før | SAY_ON_PAY (og EQUITY_PLAN) | MOT | ja | 0,30 (3/10) / 0,25 (3/12) / 0,42 (8/19) / 0,18 (3/17) | say-on-pay-MOT før av annen grunn: 0/7, 1/7, 0/5, 0/5; uten noe: 0,02 / 0,12 / 0,06 / 0,00 |
| 4 | `rem_komite_x_lonnsmot`: tekst har «compensation/remuneration committee» OG selskapet hadde SAY_ON_PAY-MOT året før | DIRECTOR_ELECTION | MOT | ja (året før) | 3/3 / 3/3 / 3/3 / 1/3 | rem-komité uten lønns-MOT: 0/6, 0/6, 0/6, 3/9 |
| 5 | `pers_tidsbruk_mot_for`: personen fikk MOT med GVG 2.1 (for mange verv) før | DIRECTOR_ELECTION | MOT, men svekkes | ja | 0,54 (7/13) / 0,36 (4/11) / 0,17 (2/12) / 0,14 (1/7) | synkende, se merknad |
| 6 | (vakt, ikke trekk) DISCHARGE-historikk GVG 3.2 | DISCHARGE | FOR (null MOT fra 2023) | ja | 0/86, 0/57, 0/74, 0/58 med 3.2-MOT før | basis 0/122, 1/96, 0/114, 0/88 |

Merknader:
- **1 er det beste**: grunnen til MOT betyr noe utover «MOT før». Det er stabilt i alle fire år, også 2026 og vakt-året 2023.
  Overlapper mye med `prev_same_person` (som sier *at*, ikke *hvorfor*). Lag det som et ekstra ja-flagg, ikke en erstatning.
- **2** gir dobbel basisrate 2023–25, men nesten ingenting i 2026. Det treffer bredt (≈250 rader/år) med lav presisjon,
  så forvent mest nytte i LGBM-delen av miksen. Mål 1 alene først, så 1+2.
- **3** skiller skarpt: say-on-pay-MOT før *uten* GVG 3.3 gir 1 av 24 MOT. Det kan også dempe de falske positive på SAY_ON_PAY
  som #2873 fant (4 i 2025, 6 i 2026), fordi `prev_same_item` ikke skiller grunnene.
- **4** har bare 3 rader per år. Det kan ikke flytte F1 merkbart, og 2026 er 1/3. Mål det bare som pakke sammen med 3.
- **5** taper kraft hvert år (NBIM har strammet antall verv, så alle er nå justert). Høy risiko for at den bare passer til 2023.
  Ta den med bare hvis vakt-året 2023 *og* 2026 ikke faller.
- **6** er ikke et trekk. Det er en kontroll: ingen kandidat skal gi flere FP på DISCHARGE i 2023–2026 enn frossen.
  Et trekk «3.2-MOT før» vil lære det gamle regimet (2019–22) og bør derfor ikke bygges.

## Byggeoppskrift for smed (#2907)
1. I `abl.py` (kopi i egen oppgave), ved siden av `hist_feats`: lag `yy_s = y_all.where(lab & d.rationale_section.isin(S))` per gruppe S,
   og kjør samme `merge_asof`-løkke med nøkkel person (1, 5) eller company_id (2, 3). Gi `(s > 0)` og `log1p(s)` som kolonner.
   Les `rationale_section` bare inne i denne funksjonen og bare for rader med `lab`. Legg den i en egen `HIST_GRUNN`-liste i
   kolonneutskriften, så assert-en mot FORBUDT fortsatt gir mening og juryen ser hvorfor den leses.
2. Lekkasjetest før måling: sett `rationale_section = NaN` for alle rader med år ≥ til_aar og kjør på nytt. Prediksjonene på teståret skal være
   byte-like. Er de ikke det, lekker trekket.
3. Kandidater, i denne rekkefølgen: K1 = v2+av + {1}; K2 = K1 + {2}; K3 = K2 + {3, 4}. Trekk 5 bare hvis K3 står.
4. Regel i REGEL.md før måling (#265/#281): snitt +0,02 over frossen på tre rullende testår, intet år inkludert 2023 under -0,02. Dommer avgjør.

Ærlig forbehold: n er lite (trekk 1: 14–24 rader per år). Rå rater sier at signalet finnes og ikke lekker, men ikke at F1 stiger.
Trekk 1 og `prev_same_person` overlapper, så reell gevinst kan bli nær null.
