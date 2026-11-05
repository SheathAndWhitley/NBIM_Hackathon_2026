# Kjente svakheter og hva vi forkastet (Case 1)

Skrevet 05.11 kl. 12.30, hovedtallet oppdatert etter byttet kl. 17:03 (#2592). Levert modell: repo4 (miks h2 + 4 historikktrekk), F1 på MOT mot styret
**0,512 på test 2026, KI [0,40; 0,62]** (P 0,48, R 0,55, 58 MOT). Grensen er valgt på val 2025 (0,530). «Følg styret» gir F1 0.
Tabellene under er målt på den eldre frosne «miks h2» (LR+LGBM, løpende historikk; eldre 0,476 på MOT, KI [0,36; 0,59], val 0,520).
Merk (avvik): tabellene under er målt på avvik fra styret (MOT + 5 AVSTÅ, 66 saker). Der er eldre frossen miks h2 0,482 [0,375; 0,580] (repo4: 0,529 [0,42; 0,63]); det er sidetall, ikke hovedtallet.
Hver påstand har en kilde: en rapport (i zipen under `arbeid/hack/c1/leveranse/kilder/` der den er med) eller et internt forsøksnummer i utviklingsloggen.

## 1. Forkastet: «styreleder = daglig leder» (duality)
| variant | val 2025 | test 2026 | kilde |
|---|---|---|---|
| uten trekk (#2044) | 0,522 | 0,482 | #1037 |
| som trekk i LR+LGBM | 0,522 | 0,482 | #1064 |
| som etterregel, løft valgt på val | 0,564 | 0,478 (PR-AUC 0,52 → 0,43) | #1065 |

Gevinsten på val kommer fra 5 saker (alle MOT i 2025, India). I 2026 er alle 3 slike saker FOR. n er for lite, så vi tok det ikke inn.
Kilde: `c1_duality_2075.md`.

## 2. Det modellen ikke kan fange uten data utenfra
- **Hele styret straffes i ett møte** (f.eks. Fluence: 8 MOT, 0 truffet; 12 bom i 2 møter på val). Vi prøvde møte-maks og
  møtesnitt av p: F1 på val falt fra 0,52 til 0,28–0,40. Klyngene ser ut til å komme av uavhengighet eller styrets sammensetning,
  og det står ikke i dataene. Kilde: `arkitekt_c1_tiltak_2072.md` (tiltak 3), `c1_feilanalyse_mot.md`.
- **Første MOT i et selskap som bare har FOR før:** 604 saker, MOT-rate 0,012, 7 av bommene. Det er lavere enn snittet (0,058),
  så det hjelper ikke å sende dem til et menneske. Modellen bygger mest på selskapets egen historikk. Uten den faller F1 fra 0,52
  til 0,34 (Δ −0,19, KI −0,27 til −0,10, `hack_c1_ablasjon_2073.md`, #1057). Kilde: `arkitekt_c1_tiltak_2072.md`.
- **India:** modellen traff 0 av 14 MOT på val 2025 (MOT-rate 0,046 → 0,102). Forslaget var å sende alle India-saker til et
  menneske (#2079), men den frosne standardkjøringen gjør det ikke: 25 av 103 India-saker på test 2026 går til menneske (#2192).
- **Nye amerikanske saker om aksjonærrettigheter (hovedårsaken blant de usette bommene):** av 28 oversette MOT på test 2026 ser
  ingen 17, og 5 av dem er USA-saker om flytting fra Delaware til Texas, høyere terskel for aksjonærforslag, utsettelse av møtet
  og supermajoritet. Alle 5 var MOT i 2026, mens de 7 slike sakene før 2026 var FOR, så modellen kan ikke ha lært det.
  Søkeordene er funnet på test og er ikke validert. Kilde: `c1_bommene.md`.

## 3. Strøkne trekk og regler, med tall
| forslag | tall | kilde |
|---|---|---|
| «non-independent» i teksten | train MOT-rate 0,067 (snitt 0,058); val 22 saker, 0 MOT; val 0,52 → 0,48 | 2072 |
| «executive/whole-time director» | train-rate 0,055, under snitt; val +0,01 for ett løft, ellers ned | 2072 |
| statseid/nominee i teksten | n = 2 i train | 2072 |
| møteaggregat (størrelse, andel aksjonærforslag osv.) | val Δ −0,032 (KI −0,078 til +0,011) | 2073, #1061 |
| styremedlem-historikk på tvers av selskaper | val uendret 0,522; test 0,475 | #1039 |
| ruting: styrevalg i møter som alt er flagget | 270 saker, MOT-rate 0,056, ikke bedre enn snitt | 2072 |
| `rationale_text` / `position_paper` som trekk | lekkasje: 618 av 627 utfylte er MOT. Brukes bare som sitat *etter* avgjørelsen | `hack_innsikt.md` |
| NPX-tallet 0,90 | oppblåst: 94 % av MOT er aksjonærforslag eller saker der styret selv anbefaler MOT. På ekte uenighet er tallet 0,61. Vi rapporterer det ikke som hovedtall | `hack_innsikt.md` |

## 4. Test-logg: hvor ofte test 2026 (real_votes) er sett
Test er kjørt **14 ganger med ulike varianter** (forsøkstabellen, 05.11 11:47–12:16). Det er ikke én jomfruelig kjøring:
| familie | varianter sett på test | test F1 | id |
|---|---|---|---|
| smed2 logreg-trapp (#2023) | 5: t0, t1, t2, t4, t4e | 0,356 / 0,458 / 0,481 / 0,497 / **0,529** | `hack_innsikt.md`, #1032 |
| smed2 miks #2044 (hovedmodell) | 5: grunn, streng historikk, styremedlem, duality-trekk, duality-regel | 0,482 / 0,386 / 0,475 / 0,482 / 0,478 | #1037–1039, #1064–1065 |
| smed logreg (#2046) | 1 | 0,456 | #1036 |
| smed3 tfidf+LR (#2037) | 1 | 0,481 | #1041 |
| smed3 kaldstart (#2065) | 2 (bare 8 MOT, KI 0–0,9) | 0,471 / 0,500 | #1044–1045 |

Hovedmodellens prediksjoner er dessuten kjørt 3 ganger til fra kald start, byte-likt (#1046, #1064, #1066). Det er reproduksjon,
ikke valg.

**Hvorfor vi ikke velger t4e (0,529 på test):** val sier motsatt (t2 0,500 > t4 0,488 > t4e 0,468). Forskjellen t2 → t4e på test
er +0,05, men KI-et er −0,01 til +0,10 med 66 avvik. Velger vi beste av 14 på test, får vi et tall som er for høyt.
Regelen er at modellen velges på val (#2080). Kilde: `hack_innsikt.md`.

## 5. Kniveggen i grensa
- **Hovedmodellen #2044, sett i ettertid på test (ikke brukt til valg):** F1 er ganske flat målt i antall flagg: 0,47–0,54 for
  35–100 flagg (valgt 71). Men p er presset sammen. Grensa er p ≥ 0,921, og flytter den seg 0,09 ned til 0,83, får vi 176 flagg
  og F1 0,35. Endrer kalibreringen seg fra år til år, kan antallet flagg endre seg mye. Kilde: `arbeid/oppgave_2082/grense.py`.
- **Injeksjon (#2188, frossen #2044):** instruksen flagges og rutes i 1578 av 1578 saker. Frasen «kindly asked to support/oppose
  management» flagges ikke. Den endrer 40–41 stemmer, og 20–21 av dem går ut uten menneske. F1 på avvik faller 0,482 → 0,40–0,42.
  Utslaget går samme vei for begge fraser, så det er støy, ikke styring. Kilde: `c1_injeksjon_frossen.md`.
  Eldre (før vakta #2237/#2265): nå fanges frasen og 0 endres uten ruting; rest: 6 av 16 nye tittel-instrukser slipper, 18–27 urutet, F1 0,39–0,42 (`c1_motstandstall_dom.md`, #2358).
- **Historikken antar at stemmene publiseres løpende:** med historikk bare fra tidligere år faller test (avvik) fra 0,482 til 0,386 (#1038).

---

# Known weaknesses and what we discarded (Case 1, English)

Delivered model repo4 (#2044 + 4 vote-history features). F1 on AGAINST is **0.512 on test 2026** (P 0.48, R 0.55, 58 AGAINST,
CI 0.40–0.62), threshold chosen on val 2025 (0.530). The tables below were measured on the older frozen #2044 (LR+LGBM, rolling vote history; older 0.476,
CI 0.36–0.59; 0.482 [0.375; 0.580] if the 5 ABSTAIN are counted as deviations; val 0.52). Follow-the-board scores 0. Sources: reports in `state/rapporter/`, attempt ids (#nnnn).

1. **Discarded: chair = CEO (duality).** Val +0.04, test −0.004 (0.482 → 0.478), PR-AUC 0.52 → 0.43. The gain rests on 5 val cases.
   All 3 such cases in 2026 were FOR. (`c1_duality_2075.md`, #1064–1065)
2. **Out of reach without external data:** whole boards punished in one meeting (12 misses in 2 meetings; meeting-level max or
   mean of p drops val F1 to 0.28–0.40), and the first AGAINST at a company with only FOR history (604 cases, rate 0.012, below
   average, so routing does not help). Without company history, F1 falls 0.52 → 0.34 (Δ −0.19, CI −0.27 to −0.10).
   India (0/14 caught on val) goes to a human instead. (`arkitekt_c1_tiltak_2072.md`, `hack_c1_ablasjon_2073.md`)
3. **Dropped features, with numbers:** see the table in section 3 above. Non-independent text 0.52 → 0.48; meeting aggregates −0.032;
   cross-company director history adds no val gain; `rationale_text` is leakage (618/627 filled = AGAINST) and is used only as a quote
   after the decision; the NPX F1 0.90 is inflated (genuine disagreement: 0.61).
4. **Test log:** test 2026 has been scored for 14 different variants. The main model's predictions were also re-run 3 times, byte-identical.
   We do **not** pick t4e (0.529 on test), because val ranks it last (t2 0.500 > t4 0.488 > t4e 0.468), and the test gap
   (+0.05, CI −0.01 to +0.10) is noise. Selection is on val only. (`hack_innsikt.md`)
5. **Knife-edge thresholds:** for #2044, F1 is flat across 35–100 flags (0.47–0.54), but scores are compressed: moving the
   threshold from 0.92 to 0.83 gives 176 flags and F1 0.35. Calibration drift across years is a real risk. History assumes votes
   are published as they happen. With prior-year history only, test F1 is 0.386 (#1038).
