# Case 1 speider (#1948): retningslinjer klare til sitering, gulv/tak for MOT-stemmer, Case 2 uten AAER-CSV

## 1. Retningslinjene ligger i `arbeid/hack/c1/retningslinjer/` (637 nummererte punkter)
| Fil | Punkter | Siter som | Kilde |
|---|---|---|---|
| `vanguard_us_2026.md` | 132 | `VG26 1.4.1` | https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vpm/vpm-proxy-voting-policy-us.pdf |
| `vanguard_us_2025.md` | 109 | `VG25 ...` | Vanguard SAI på EDGAR (smed3s tekstkopi), effektiv feb. 2025 |
| `nbim_global_voting_guidelines.md` | 140 | `NBIM 3.1.4` | https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ |
| `nbim_posisjonsnotater.md` | 256 | `NBIM-PP3 5` | https://www.nbim.no/en/responsible-investment/position-papers/ (12 notater) |

- Alt står også i `punkter.jsonl` (`id`, `pilar`, `avsnitt`, `tekst`), klart for BM25. `README.md` har et kart fra forslagstype til punkt.
  Eksempler: overboarded → VG26 1.4.1/1.4.2, oppmøte < 75 % → 1.5.1, Say on Pay → 3.0.9-3.0.19, revisor → 2.5.1, miljø/sosialt → 2.4.x.
- Datasettet er Vanguard, derfor Vanguard og ikke BlackRock. blackrock.com svarer med feilside til skript, og BlackRocks CIK 1364742 har ingen stemmer.
- **Vanguard-versjon per møtedato:** Vanguard delte stewardship i VPM og VCM fra 12.01.2026. VPM- og VCM-policyen er ordrett like (sjekket med diff). Bruk VG25 for møter før 12.01.2026 og VG26 etter.
- 2026-teksten «may recommend» erstatter «will vote». Policyen er altså mykere enn før. Det er greit å si til juryen når praksis spriker fra policy.
- NBIM: «Our starting point when deciding how to vote is to support the board» (NBIM 0.0.3). Det gjør «følg styret» til policyens egen nullhypotese.
- Lages på nytt med `python3 -I arbeid/speider/c1ret/lag_retningslinjer.py`.

## 2. Gulv og tak for å forutsi MOT-stemmer
**Gulv (våre egne målinger):**
- Mål A, MOT/AGAINST: «følg utledet styre» gir F1 0,839 på dommerens måler bdad4444d1. Høyt, fordi aksjonærforslag er nesten alltid MOT. smed3 har 0,860.
- Mål B, avvik fra styret (hovedtallet i måler v2): «følg styret» har recall 0 per definisjon. Regelen «aksjonærforslag eller direktør med tidligere MOT» ga F1 0,153 (tavla #971). tfidf på forslagsteksten ga PR-AUC 0,062 mot 0,045 for tilfeldig. Teksten bærer nesten ingen informasjon.

**Tak:**
- 12,2 % av de unike forslagene fikk blandet stemme innen Vanguard selv (hack_speider.md). Ingen modell kan treffe dem perfekt.
- Regimeskifte: samme serie stemte 0,4 % mot ledelsen i 2024-25 og 4,8 % i 2025-26. Trening på fjoråret overføres dårlig.
- Litteraturen har ingen publisert presisjon/recall for å forutsi fondsstemmer fra N-PX. Det er en åpning for oss: vi kan si at dette ikke er gjort før med tidssplitt.

**Hva som forklarer MOT i litteraturen (kandidater til kjennetegn):**
- **ISS-anbefaling:** Malenko og Shen (RFS 2016) bruker en terskelregel hos ISS. En negativ ISS-anbefaling gir 25 prosentpoeng lavere støtte til Say on Pay. ISS-anbefalinger koster penger, og vi har dem ikke. Erstatning: de målbare reglene ISS og Vanguard bruker (verv, oppmøte, uavhengighet) hentet fra DEF 14A.
- **Indeksfond følger rådgiver mest:** Iliev og Lowry (RFS 2015) fant at ca. 25 % av fondene stemmer med ISS på nesten alt. Passive fond følger ISS omtrent tre ganger så ofte som aktive ved omstridte direktørvalg. Vanguard indeks er derfor forutsigbar fra regler.
- **Lav dimensjon:** Bubb og Catan («The Party Structure of Mutual Funds», RFS 2022) viser at to dimensjoner forklarer det meste av fondsstemmene, og at de følger rådgiverens anbefalinger. Historikken til utsteder og direktør er derfor et sterkt signal. Det stemmer med vårt funn: 26 % MOT mot 4,6 %.
- **Lekkasjefelle:** møteresultatet (f.eks. en Say on Pay som falt) er kjent først etter møtet. Det skal aldri brukes som kjennetegn.

**Konsekvens for Smeden:** de største gevinstene ligger i kjennetegn fra innkallingen (DEF 14A): antall styreverv, oppmøte under 75 % og uavhengighet i komiteer. Hver av dem svarer direkte til et VG26-punkt, så sitatet kommer på kjøpet.

## 3. Case 2 uten arrangørens AAER-CSV
**Én linje: gjennomførbar på 15 min. 696 AAER (08.2017-10.2026) skrapet fra SEC, 165 unike selskaper koblet til CIK med navnematch (171 av 236 selskapsnavn), 55 av dem i vårt FSDS-panel. Hvilket regnskapsår som var feil står bare i selve utgivelsen. Det må leses (LLM, 1-3 t), ellers lekker tid.**
- Skript: `arbeid/speider/c2aaer/kobl.py`, resultat `arbeid/speider/c2aaer_raa/aaer_cik.csv`. Navnematchen er ikke kontrollert for falske treff.
- Liste: https://www.sec.gov/enforcement-litigation/accounting-auditing-enforcement-releases (100 per side, `?page=N`). CIK-oppslag: https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
- Valget av Case 1 står seg. Grunnen er fasitårene, ikke at listen mangler.

## Kilder
- Vanguard VPM 2026: https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vpm/vpm-proxy-voting-policy-us.pdf
- Vanguard VCM 2026: https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vcm/vcm-proxy-voting-policy-us.pdf
- Endringer 2026 (Vanguard/BlackRock): https://www.cooley.com/news/insight/2026/2026-01-22-key-updates-in-blackrocks-and-vanguards-2026-us-proxy-voting-guidelines
- NBIM retningslinjer: https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ og PDF 2024: https://nbim.no/contentassets/01a7ee19b5d84a73a67a365e76a0fb01/global-voting-guidelines2024.pdf
- NBIM posisjonsnotater: https://www.nbim.no/en/responsible-investment/position-papers/
- Malenko og Shen 2016, RFS 29(12): https://econpapers.repec.org/RePEc:oup:rfinst:v:29:y:2016:i:12:p:3394-3427
- Iliev og Lowry 2015, RFS 28(2): https://econpapers.repec.org/RePEc:oup:rfinst:v:28:y:2015:i:2:p:446-485
- Bubb og Catan: https://www.ecgi.global/sites/default/files/working_papers/documents/bubbcatanfinal.pdf
- Effektstørrelsene i litteraturen er hentet fra sammendrag. Fulltekst er ikke lest i dag.
