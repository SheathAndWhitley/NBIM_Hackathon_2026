# Case 1: tre nye vinkler for natta (arkitekt, #2868, ordre #281)

Utgangspunkt: frossen repo4 = `arbeid/oppgave_2567/abl_rull.py --variant miks --hist 2 --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate`, snitt 0,5162 (0,5057/0,5309/0,5120). Ingen av vinklene under er av-regel, ensemble eller terskelflytting. Disse er lukket og står utenfor: duality (#2075), møtestruktur, land×type og «ny for selskapet» (#2248), overboarding (#1964), p-klumping per møte (#2067) og NPX-trening (#2081).
**KP:** jeg kjørte en kopi av abl_rull.py med testår 2025. Forventet val 0,5561 og intern test 0,5233 (repo4_2025.log). Fikk 0,5561 og 0,5233, altså samme tall. Prøvene under er kjørt på samme måte, men bare på ett testår (2025, med val 2024). De er ikke en måling etter bytteregelen.

| # | vinkel | til | kontrolltall | prøve, val 2024 / intern test 2025 |
|---|---|---|---|---|
| 1 | Begrunnelses-historikk: hvilken GVG-seksjon de tidligere MOT-stemmene i selskapet hadde | **smed** | styrevalg etter MOT med GVG 1–3: 10–14 % MOT. Etter GVG 4–6: 1,3–3 % (n=2 130 rader fra 2022) | ikke bygd (dataprøve bare) |
| 2 | Tekst inn i LGBM-halvdelen (SVD av tf-idf) | **smed3** | LGBM ser i dag 0 tekstkolonner (abl_rull.py:98) | 0,5561→0,5619 (+0,006) / 0,5233→0,5373 (+0,014) |
| 3 | Tidsvekt på treningsrader (nyere år teller mer) | reserve | — | tv 0,8: +0,017 / −0,001; tv 0,65: +0,021 / −0,015 |

## Vinkel 1 → smed: hvilken GVG-seksjon de tidligere MOT-stemmene hadde
**Hva endres:** i dag teller historikken alle tidligere MOT i selskapet likt (`s>0`, rate). Men `rationale_section` på **tidligere møter** sier *hvorfor* NBIM stemte MOT. Den er offentlig sammen med stemmen. FORBUDT.md forbyr den bare for samme sak, og historikk fra møter før datoen er lov. Nytt trekk per rad: for hver GVG-hovedseksjon 1–6, antall tidligere MOT i selskapet med den seksjonen (log1p), løpende med `merge_asof`, `allow_exact_matches=False`, akkurat som `hist_feats`. Altså 6 kolonner.
**Hvorfor +0,02 er mulig:** tallene (2022–2026, alle rader med fasit, `arbeid/oppgave_2868`, se kommandoen nederst):
| sakstype | forrige MOT var GVG… | MOT-rate | n |
|---|---|---|---|
| DIRECTOR_ELECTION | 1 / 2 / 3 | 0,102 / 0,121 / 0,140 | 891 / 372 / 286 |
| DIRECTOR_ELECTION | 4 / 5 / 6 | 0,013 / 0,030 / 0,031 | 155 / 302 / 64 |
| DIRECTOR_ELECTION | ingen MOT før | 0,029 | 1 903 |
| SAY_ON_PAY | 3 / ingen | 0,291 / 0,070 | 55 / 114 |
| AUDITOR | 5 / ingen | 0,167 / 0,009 | 54 / 331 |
| DISCHARGE | 3 / ingen | 0,082 / 0,011 | 243 / 94 |

Et selskap med MOT på vedtekter (GVG 4) eller revisor (GVG 5) får i dag samme historikkløft på styrevalg som et selskap med MOT på uavhengighet. Etter disse tallene er det løftet falskt. Styrevalg står for 26 av 38 falske MOT på test (#2272), og der er presisjonen 0,37. Vinkelen treffer akkurat det. `hist_type_dev_rate` dekker bare samme sakstype, ikke koblingen på tvers (GVG 3 → say-on-pay 29 %).
**Hvor koden røres:** kopi av `arbeid/oppgave_2567/abl_rull.py` til ny oppgavemappe. Legg til 6 kolonner i `hist_feats` (l. 46–74, ny nøkkel = company_id, y = MOT med seksjon k), og de går da automatisk inn i både LR og LGBM. `rationale_section` leses bare i den løpende historikken og aldri for raden selv. Kjør gjerne `sjekk_lekkasje.py` (arbeid/hack/c1). Leveranse: `svar_*_t{2023..2026}.csv` til dommer2s natt-måler (#2867). REGEL.md skrives før måling.
**Risiko:** seksjonen finnes nesten bare fra 2023 («fra 2023 har nesten alle MOT begrunnelse», FORBUDT.md). Før det blir kolonnene for det meste 0, så gevinsten kommer helst i 2024–2026. Vaktåret 2023 er trolig nøytralt.

## Vinkel 2 → smed3: tekst inn i LGBM-halvdelen
**Hva endres:** miks = rang-snitt av LR (tf-idf + kategorier + historikk) og LGBM (kategorier + historikk). LGBM ser ikke forslagsteksten i det hele tatt. Legg til TruncatedSVD(48) av samme tf-idf, tilpasset bare på treningsradene, som 48 kolonner i LGBM. Ingen ny modell og ingen ny blanding, bare flere trekk inn i den eksisterende halvdelen.
**Hvorfor +0,02 er mulig:** prøven over gir +0,014 på intern test 2025 og +0,006 på val. Teksten bærer det LGBM nå mangler: «Chairman and Managing Director», flytting til Texas og aksjeplaner (bommene i #2067/#2272). Trærne kan da kombinere tekst med historikk, noe LR bare gjør additivt.
**Hvor koden røres:** ferdig prototype i `arbeid/oppgave_2868/svd_rull.py`. Den har 4 nye linjer i `lgbm_pred` (l. 95ff.) og er ellers lik abl_rull.py. smed3 kjører 2023/2024/2025/2026 og prøver eventuelt 32/64 komponenter. Komponenttallet velges på val, ikke på test.
**Risiko:** én prøve på ett år. +0,014 kan være støy (KI på snitt er ±0,04, ki_snitt.txt).

## Vinkel 3 (reserve): tidsvekt på treningsrader
**Hva:** `sample_weight = tv^(år_før_test − år)` i både LR og LGBM. Prototype: `arbeid/oppgave_2868/tv_rull.py --tv`.
**Tall:** val 2024 går opp (+0,017 og +0,021), men intern test 2025 står eller faller (−0,001 og −0,015). Val-gevinsten blir ikke med til test, fordi MOT-raten per år er stabil (0,052/0,054/0,043 i 2024–2026) og driften ikke er stor nok. **Ikke start på denne før vinkel 1 og 2 er målt.** Hvis den startes, skal den kombineres med vinkel 1 (seksjonene kom først fra 2023, så nyere år bør da veie mer).

## Trukket vinkel (#156)
Trekket ga topologi/bandit, termodynamikk/symmetri og finans/«gradient på en glatt erstatning». Den mest lovende var finans: tren direkte på en glatt F1 i stedet for logloss. Jeg forkastet den uten prototype: den endrer bare rangeringen nær grensen, og det ligner terskelflytting, som oppgaven utelukker. Kostanslag: om lag 1 time smedtid for en egen gradientløkke, uten noe tall som tyder på gevinst.

## Kommandoer
```
cd arbeid/oppgave_2868; D=<repo>/state/opplastet/20261105_114241_real_votes.csv
uv run --project ../oppgave_2023 python svd_rull.py $D --ut svd.csv --hist 2 --variant miks --testaar 2025 --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate
uv run --project ../oppgave_2023 python tv_rull.py $D --ut tv_0.8.csv --hist 2 --variant miks --testaar 2025 --tv 0.8 --repo (samme)
```
Seksjonstabellen: `uv run --project ../oppgave_2023 python seksjon.py` ( merge_asof på siste MOT-møte per selskap (modal seksjon), år ≥ 2022).
