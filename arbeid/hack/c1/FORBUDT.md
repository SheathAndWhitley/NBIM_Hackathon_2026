# Case 1: forbudte kolonner (aldri input for samme sak) — dommer2 #2055

Disse kolonnene er fasit eller skrevet ETTER stemmen. Brukes de som feature, er tallet ugyldig.

| kolonne | hvorfor forbudt | målt |
|---|---|---|
| nbim_vote, nbim_vote_raw | er stemmen | — |
| against_board | er fasiten | bare som y på TRAIN |
| rationale_text | NBIMs begrunnelse etter stemmen | real: fylt i 618 av 744 MOT, 9 av 12 580 FOR |
| rationale_section | samme | real: 618 MOT, 0 FOR |
| position_paper | samme | real: 358 MOT, 9 FOR |
| funds_disagree | utfall av fondenes stemmer | npx: 4 rader =1 |
| n_funds | antall NBIM-fond som rapporterte stemmen i N-PX, kjent først etter møtet; MOT-andel 3 % (1 fond) → 26 % (4 fond) | npx |
| injection_flag | arrangørens merke for plantede instrukser; rader med 1 er motstandstesten (vindu inj), ikke data | npx: 141 rader |
| split_year | bare til å dele, ikke feature | npx |

Lov som input: proposal_text, proponent, proposal_type, mgmt_rec(_raw), company/ticker/country/market, meeting_date, item_no, year.
Historikk (selskapets tidligere MOT-rate o.l.) er lov bare fra møter FØR datoen.

**Hvorfor dette er de «94 %»:** fra 2023 har nesten alle MOT begrunnelse. Regelen «begrunnelse finnes = MOT»
gir på real 2026: 63 riktige, 2 falske, 3 bommet, F1 ≈ 0,95. Hvert tall over ~0,6 skal sjekkes mot dette.

**Sitat, ikke feature (#2037):** begrunnelser fra TIDLIGERE år kan siteres som NBIMs policy
(«i 2024 stemte NBIM mot … fordi …»). Aldri begrunnelsen til samme sak eller samme år som scores.

## Sjekken
```
cd arbeid/hack/c1
python3 -I sjekk_lekkasje.py svar SVAR.csv --data real --vindu test   # 1=AVVIST, 2=MISTANKE, 0=OK
python3 -I sjekk_lekkasje.py kode ../../oppgave_NNNN                  # linjer som nevner forbudte kolonner
```
- Svarfil med forbudt kolonne: AVVIST.
- Jaccard ≥ 0,75 mellom predikerte avvik og rader med begrunnelse: MISTANKE (lekk-regelen gir 1,00, smed2s 2046-modell 0,26).
- Kodelinjer som nevner forbudte kolonner listes; merk lovlig bruk med `# lov: <grunn>`.
- Måleren `maaler_offisiell_v2.py lag` skriver allerede `data_off/*_input.csv` uten LEKK-kolonnene: les dem, ikke rådata.
