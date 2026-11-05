# Case 1 (#2915): lekkasjetest for natt-kandidatene, GRØNN på frossen og v2+av

**Kommando til dommeren (natt-dom 02:00, #2874):**
```
uv run python arbeid/verktoy/c1_lekkasjetest.py --modell frossen        # eller --modell v2av
uv run python arbeid/verktoy/c1_lekkasjetest.py --aar 2023,2024,2025,2026 --kjor \
  'uv run --project {ROT} python <kandidat>/v2_rull.py {data} --ut v.csv --hist 2 --variant miks --testaar {T} --k {K} --repo prev_same_item,prev_same_person,prev_meeting_any_dev,hist_type_dev_rate > logg.txt 2>&1 && python3 -I {ROT}/arbeid/hack/levering/av_regel.py {data} v_test.csv {T} svar.csv'
```
`--kjor` er en kommandomal som kjøres i en tom mappe og skal legge igjen `svar.csv` (id,anbefaling,p_avvik) for år `{T}`.
Kandidaten **må** lese data fra `{data}`, ikke fra en hardkodet sti. Utgang 0 = alt GRØNN, 1 = RØD. Tid ca. 25 s (9 treninger i parallell).

## Hva testen gjør (svart boks, ingen kandidatkode importeres)
Etikettblokka = `against_board, nbim_vote, nbim_vote_raw, rationale_text, rationale_section, position_paper`, alltid byttet samlet per rad.
- **A, egen dag** (= «datoene flyttet en dag fram»): i teståret velges datoen D med flest saker (~100 rader). Alle rader med dato ≥ D
  får etikettblokka til en tilfeldig rad med *motsatt* etikett (FOR blir MOT med ekte MOT-forklaring). Radene på D kan da ikke
  lovlig se noe nytt. lekk = snitt av dp i retning ny etikett på D. GRØNN: lekk ≤ 0,01 og ≤ 1 flagg snudd mot ny etikett.
- **B, permutasjon**: etikettblokka stokkes innen hvert år, alle år. F1 (avvik fra styret, mot *ekte* etiketter) skal falle til
  tilfeldig nivå 2pq/(p+q). GRØNN: F1_perm ≤ tilfeldig + 0,05.
A fanger trekk som leser egen rad/eget møte/egen forklaring. B fanger lekk forbi blokka (hardkodet rådata, avledede kolonner).
B alene kan ikke fange en lekk *av* blokka (den lekker da den stokkede etiketten), derfor begge.

## Tall (frø 2915)
| kandidat | A lekk 2024 / 2025 / 2026 | flagg snudd | B F1avvik ekte → permutert (tilfeldig) 2024 / 2025 / 2026 | dom |
|---|---|---|---|---|
| frossen | −0,0064 / −0,0224 / −0,0002 | 0 / 0 / 0 | 0,541→0,027 (0,036) / 0,523→0,060 (0,084) / 0,529→0,082 (0,069) | GRØNN |
| v2av | −0,0035 / −0,0139 / −0,0001 | 0 / 0 / 0 | 0,568→0,049 (0,041) / 0,561→0,054 (0,065) / 0,556→0,067 (0,054) | GRØNN |
| kontroll_egen (leser egen against_board) | **+0,440 / +0,424 / +0,399** | 101 / 103 / 90 | GRØNN (ventet, se over) | **RØD** |
| kontroll_raadata (leser hardkodet rådata) | GRØNN (ventet) | 0 | **0,813→0,800 / 0,896→0,371 / 0,795→0,334** | **RØD** |

KP: forventet RØD på begge med vilje lekke kontroller, fikk RØD (`--modell kontroll_egen`, `--modell kontroll_raadata`).

## Forbehold
- F1 i B er på avvik (against_board), ikke hovedtallet «MOT mot styret» fra maaler_aar.py. Det er riktig mål for en lekkasjetest, ikke for byttedommen.
- Negativ lekk og støy (opptil 0,04 i 2025, der D er tidlig i mars) kommer av at miks-modellen rangerer p over *alle* rader, så
  endrede senere rader flytter rangen litt. Ingen flagg før D endret seg i frossen 2026/2025, 2 av 1355 i 2024.
- A tester én dato per år (den største). En lekk som bare slår ut på andre datoer, eller bare i treningsårene, fanges av B
  bare hvis den går forbi blokka. Vil dommeren ha mer: kjør med annet `--frø` (endrer byttene, ikke D).
- 2023 i `--aar` bruker k=32 for v2-kandidater (ikke låst på val for 2023).
Kode: `arbeid/verktoy/c1_lekkasjetest.py`, kontroll: `arbeid/verktoy/c1_lekk_kontroll.py`.
