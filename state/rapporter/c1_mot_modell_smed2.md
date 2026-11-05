# Case 1: modell som finner stemmene MOT styret på arrangørens real_votes (smed2, #2044)

**Valgt modell:** logreg (tfidf på forslagstekst + kategorier) og LightGBM (kategorier + historikk), snitt av rangene.
Historikken er løpende: MOT-andel i samme selskap, samme selskap+tekst og samme tekst, bare fra møter **før** møtedatoen.
Grensen og C er valgt på val 2025 (trent på <2025). Test 2026 er kjørt én gang.

| real_votes test 2026 (1539 rader, 66 MOT) | F1 | Presisjon | Recall | Predikert MOT |
|---|---|---|---|---|
| Følg styret (ikke lov) | 0 | – | 0 | 0 |
| **Miks, løpende historikk (valgt)** | **0,482** | 0,465 | 0,500 | 71 |
| Miks, streng historikk (bare tidligere år) | 0,386 | 0,458 | 0,333 | 48 |
| Logreg alene, løpende historikk | 0,470 | 0,390 | 0,591 | 100 |
| + styremedlem-historikk (nullfunn, ikke valgt) | 0,475 | 0,452 | 0,500 | 73 |

- Val 2025 for valgt modell: F1 0,522 (P 0,59, R 0,47). PR-AUC test 0,52. Bootstrap 95 % for test-F1: 0,37–0,58 (bare 66 MOT, så tallet er usikkert).
- Modellen fanger mer enn aksjonærforslag: 29 av 58 MOT der styret selv foreslår og anbefaler FOR blir truffet. Styrevalg: 15 av 33 truffet, 41 flagget.
- Løpende historikk forutsetter at NBIMs tidligere stemmer i samme sesong er kjent. Det stemmer i praksis, fordi NBIM publiserer stemmene løpende. Den strenge varianten (0,386) er gulvet uten den antakelsen.

**Features (bevis, skrives ut av train.py, og en assert stopper kjøringen ved overlapp):**
kolonner lest: company_id, country, item_no, market, meeting_date, mgmt_rec, mgmt_rec_raw, proponent, proposal_text, proposal_type, year.
against_board brukes bare som mål og som historikk fra tidligere møter.
Forbudt og ikke brukt: nbim_vote, nbim_vote_raw, rationale_text, rationale_section, funds_disagree, **position_paper**.

**Ny lekkasje funnet:** `position_paper` er satt i 367 rader, og 97,5 % av dem er MOT (mot 3 % ellers). Det er NBIMs egen begrunnelse og må på forbudslista (til lekkasjevakt #2040).

Kjør (ca. 1 min):
`cd arbeid/oppgave_2044 && uv run --project ../oppgave_2023 python train.py ../../state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --ut pred_miks_h2.csv`
Forsøk på tavla: #1037 (valgt), #1038 (streng), og person-varianten (nullfunn).
