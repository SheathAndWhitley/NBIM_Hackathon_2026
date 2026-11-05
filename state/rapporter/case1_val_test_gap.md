# Case 1 (#1990): hvorfor lederen er svakere på 2025 (F1 0,42) enn på 2026 (0,51), og hvilket tall som gjelder for neste sesong

**Konklusjon for juryen:** Omtrent 0,07 av gapet på 0,09 skyldes oppsettet, ikke året. Val 2025 har bare ett års NBIM-historikk å lære av og slå opp i. Test 2026 har to. Vi trente den samme modellen på 2026 med bare ett års historikk (N-PX 2025), og da faller den fra 0,509 til **0,439**. Det er bare 0,021 over val (0,418), og den resten er støy. Neste sesong (2027) får minst like mye historikk som test. Derfor er test-oppsettet det riktige for neste sesong, men 0,509 er litt for høyt fordi grenseregelen ble valgt med test i sikte. **Forventet F1 neste sesong: ca. 0,48, med usikkerhet ±0,07 (omtrent 0,41–0,55).** Følg styret gir 0. Gulvregelen gir ca. 0,38.

## 1. Basisrate MOT per år
| N-PX-år (møter) | forslag | MOT | andel |
|---|---|---|---|
| 2024 (07.23–06.24) | 1631 | 149 | 9,1 % |
| 2025 (07.24–06.25) = val | 1506 | 136 | 9,0 % |
| 2026 (07.25–06.26) = test | 1246 | 129 | 10,4 % |

2026 har 1,4 prosentpoeng flere MOT. Den forskjellen er ikke signifikant (to-andelstest z ≈ 1,2, p ≈ 0,2). En litt høyere basisrate løfter F1 litt av seg selv, så dette er en liten del av det året «forklarer».

## 2. Historikk per rad (det som forklarer mesteparten)
| | val 2025 | test 2026 (i dag) | test 2026, bare ett års historikk |
|---|---|---|---|
| treningsrader | 1631 | 3137 | 1506 |
| rader med NBIM-historikk på selskapet | 92,1 % | 91,3 % | 90,4 % |
| snitt antall tidligere NBIM-stemmer | 0,93 | **1,77** | 0,91 |
| rader med ≥ 2 tidligere stemmer | 0,7 % | **85,6 %** | 1,0 % |
| P(MOT \| tidligere MOT) | 0,387 (46/119) | 0,348 (55/158) | 0,436 (44/101) |
| P(MOT \| bare tidligere FOR) | 0,058 | 0,056 | 0,064 |
| andel av MOT-sakene som hadde MOT før (gulvets recall-tak) | 0,338 | **0,426** | 0,341 |
| Vanguard say-on-pay innsendt før møtet | 89,6 %, snitt 1,02 stemmer | 92,7 %, snitt 1,98 | som test |
| **gulvregelen F1** | 0,361 | 0,383 | 0,383 |
| **smed2 lederen F1** (gjenskapt nøyaktig) | **0,418** | **0,509** | **0,439** |

Slik leses tabellen:
- Med to år bak seg har 43 % av MOT-sakene en tidligere MOT på samme selskap. Med ett år er det 34 %, både i 2025 og 2026. Modellen bruker antall, andel og siste stemme, så den får mer ut av ekstra historikk enn gulvregelen gjør. Gulvregelen spør bare «MOT noen gang før?» og ligger på 0,383 uansett.
- Parvis bootstrap på 2026 (trekk per selskap, 1000 trekk, seed 0): to års historikk minus ett år gir **+0,071, KI [+0,009; +0,135]**, og 99 % av trekkene er over 0. Effekten er altså ekte, men bred.
- Med lik historikk er 2026 bare 0,021 over 2025 (0,439 mot 0,418). Det er godt innenfor KI-bredden på ±0,07 per år fra #1986.
- Forbehold: ett års historikk betyr også halvparten så mye treningsdata. De to effektene kan ikke skilles i dette oppsettet. Vanguard-historikken var ikke kuttet i ettårskjøringen, så Vanguard-dybden (1,02 mot 1,98 stemmer) ligger i restgapet på 0,021.

## 3. NBIMs retningslinjer mellom årene
Vi finner ingen dokumentert endring i NBIMs lønnspolicy mellom sesongene 2025 og 2026. Speiderens kopi (#1948) har bare én dato innenfor vinduet: notatet om bærekraftsrapportering (NBIM-PP4) ble oppdatert 3. september 2024. Det er ikke lønn, og det kom før begge sesongene. Lønnsnotatet (NBIM-PP3, CEO remuneration) har ingen dato i kopien vår. Vi har ikke versjonerte utgaver av NBIMs globale stemmeretningslinjer per år, så en endring kan ikke utelukkes. Dataene tyder heller ikke på et skifte: P(MOT | tidligere FOR) er 5,8 % mot 6,4 %, og MOT-andelen i juni er 13 % mot 14 %. **Retningslinjene forklarer ikke gapet, så langt vi kan måle.**

## 4. Bootstrap-intervallene (#1986)
Hvert års F1 har et 95 %-KI på ca. ±0,07. Det kommer av at vi bare har 129–136 MOT-saker. Val [0,344; 0,488] og test [0,435; 0,580] overlapper. To uavhengige år kan dermed lett skille 0,09 av ren støy. Det strukturelle funnet over (+0,071 fra historikk, målt parvis) forklarer likevel det meste av gapet uten å trenge støy.

## 5. Hvilket tall er forventet for neste sesong, og hvorfor
- **Ikke 0,42.** Val er et ettårsoppsett, og slik blir aldri drift: i 2027 har modellen tre års historikk.
- **Ikke 0,51 rått heller.** Grenseregelen (1,25 × basisrate) og SEC-kjennetegnene ble valgt etter test-ablasjonen (smed2s egen rapport). 2026 hadde dessuten litt høyere basisrate (+1,4 pp).
- **Anslag ≈ 0,48 (± 0,07):** 0,509 minus årseffekten med lik historikk (0,021) og litt for valg med test i sikte. Tallet er et anslag, ikke en måling. Den eneste rene målingen er test 2026 med alle valg frosset før kjøring.
- Den åpne lekkasjesjekken (#1988) kan senke alle tallene over. Kommer den med lavere tall, skal anslaget flyttes like mye ned.
- Til juryen: «0,42 på 2025 og 0,51 på 2026. Det meste av forskjellen kommer av at 2026 har to års historikk og 2025 bare ett. Med samme historikk gir 2026 0,44. For neste sesong venter vi rundt 0,48 ± 0,07.»

## Kjør fra kald start (< 2 min)
    python3 -I arbeid/oppgave_1990/gap.py          # tabell 1-2 (basisrate, historikk, gulv)
    cd arbeid/kandidater/smed2_c1_mot && uv run python train_v3.py --data ../../oppgave_1990/data_1aar --ut ../../oppgave_1990/pred_1aar.csv
    python3 -I arbeid/hack/c1/maaler.py arbeid/oppgave_1990/pred_1aar.csv --fasit arbeid/hack/c1/data_v3/fasit.csv   # 0,438662
    python3 -I arbeid/oppgave_1990/boot.py         # +0,071 [+0,009; +0,135]
`data_1aar/` = data_v3 med train filtrert til npx_aar 2025. smed2s kode er ikke endret.

Tilfeldig vinkel: ingen trukket. Dette er en ren måle- og forklaringsoppgave.
