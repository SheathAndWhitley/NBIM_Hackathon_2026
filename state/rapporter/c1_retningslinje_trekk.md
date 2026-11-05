# Case 1: NBIM/Vanguard-retningslinjer som trekk i repo4 (smed3, #2876)

**Svar: gir lite.** Rå repo4+retn: snitt 0,5223 mot frossen repo4 0,5162 (+0,006). Under bytteregelens +0,02. Frossen står.
Gjennom #2703s midt+av gir samme p_avvik 0,5478 mot midt+av 0,5261 (+0,022), men 2023-vakta faller med 0,0203
(regelen sier intet år under -0,02), og en kontroll med stokkede trekk flytter enkeltår like mye. Dommer avgjør, min
anbefaling er nei.

## Formen
637 siterbare punkter (`arbeid/hack/c1/retningslinjer/punkter.jsonl`). 141 sier eksplisitt «stem mot / støtter ikke»
(regex på teksten: vote against, will not support, oppose, withhold ...). Per forslag 12 tette trekk, ingen etiketter:
tfidf-cosinus (1-2-gram, engelske stoppord) til nærmeste MOT-punkt og nærmeste punkt overhodet, differansen, maks
likhet til MOT-punkter per tema (lønn 15 punkter, styreuavhengighet/-sammensetning 67, klima/rapportering 18,
kapital/aksjonærrettigheter 38), nøkkelordtellinger per tema, og grov id for nærmeste MOT-punkt.
Hektet på repo4 (oppgave_2567/abl_rull.py: logreg tfidf+kategorier ⊕ LightGBM, 4 repotrekk, --hist 2) som ekstra
kolonner, samme sted som repotrekkene. Modell og valgregler uendret. REGEL.md skrevet før måling (sa 13 kolonner, det ble 12;
trekksettet er ikke endret etter første kjøring).

## Tall (maaler_aar --score mot, F1 på MOT mot styret, ett forsøk per år)
| | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | mot grunnlinje |
|---|---|---|---|---|---|---|
| repo4 frossen | 0,3350 | 0,5057 | 0,5309 | 0,5120 | 0,5162 | |
| **repo4+retn rå** | 0,3231 | 0,5233 | 0,5233 | 0,5203 | **0,5223** | +0,006, år: -0,012 / +0,018 / -0,008 / +0,008 |
| repo4 midt+av (#2703) | 0,3536 | 0,5083 | 0,5276 | 0,5424 | 0,5261 | |
| **repo4+retn midt+av** | 0,3333 | 0,5506 | 0,5549 | 0,5378 | **0,5478** | +0,022, år: **-0,020** / +0,042 / +0,027 / -0,005 |
| kontroll: 12 stokkede kolonner, rå | 0,3118 | 0,4819 | 0,5093 | 0,5614 | 0,5175 | +0,001, år: -0,023 / -0,024 / -0,022 / +0,049 |
| kontroll, midt+av | 0,3537 | 0,4884 | 0,5150 | 0,5766 | 0,5266 | +0,001, år: 0 / -0,020 / -0,013 / +0,034 |

Kontrollen (samme 12 kolonner med radene stokket, altså ingen informasjon) viser at enkeltår flytter seg ±0,02–0,05 bare av
at LightGBM får nye kolonner å splitte på. Snittet over tre år er stabilt (±0,001). Gevinsten +0,022 på midt+av er altså
større enn kontrollen, men den kjøpes av to år og gis tilbake i 2026 og 2023.

## Hvorfor lite
Forslagstekstene er korte (maks 253 tegn) og sier *hva* saken er, ikke *hvorfor* NBIM skulle stemme mot. Likheten til
retningslinjene fanger tema, og tema har modellen alt gjennom proposal_type og tfidf på teksten. Det som utløser MOT
(CEO i for mange styrer, lønn uten prestasjonskrav, manglende uavhengighet) står ikke i forslagsteksten, så retningslinjen
kan ikke matches mot det. Trekket ville trengt selskapsdata (styresammensetning, lønnsdata) for å bite.

## Filer
- Kode: `arbeid/hack/varianter/smed3_utf_retn/` (abl_retn.py = abl_rull.py + `--retn`, retn_trekk.py, kjor.sh, maal.py, REGEL.md, KORT.md)
- Prediksjoner: `retn_<år>_{val,test}.csv`, offisielle svarfiler `ut_retn_{raa,midt,midt+av}_<år>.csv`, kontroll `ut_perm_*`
- Logger: `retn_<år>.log`, `perm_<år>.log`
