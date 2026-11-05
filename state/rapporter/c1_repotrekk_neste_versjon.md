# Case 1, neste versjon: NBIM-repoets historikktrekk i vår modell (#2490, smed)

Bare dokumentasjon for NESTE_VERSJON.md. Ingen endring i levering/ eller frosne filer.

**Kode:** `arbeid/oppgave_2490/abl.py` (kopi av `oppgave_2103/abl.py` = frossen #2044, miks LR+LGBM, løpende historikk h2) + bryter `--repo`. Den legger til repoets egne trekk fra `ballot.add_history` (uendret repokode) som ja/nei-indikatorer: `prev_same_person` (forrige stemme på samme direktørnavn i samme selskap), `prev_same_item` (samme sakstekst uten tall), `prev_meeting_any_dev` (noe avvik på selskapets forrige møte) og `hist_type_dev_rate`. Kjøring: `cd arbeid/oppgave_2490 && bash kjor.sh` (ca. 10 s).
**Protokoll:** C og terskel valgt på val 2025 (trent <2025), test 2026 én gang. Valgregel: høyest val-F1. To varianter kjørt i samme batch, så begge testtallene ble sett samtidig. Valget står likevel på val (se tabell). `full` gjenskaper #2044 (test 0,476190, identisk).
**Måler:** `arbeid/hack/c1/maaler_offisiell_v3.py <svar> test --data real --score mot` (58 MOT i fasit). KI: `oppgave_2103/diff_ki.py`, parret klyngebootstrap per selskap, 2000 trekk, B minus frossen.

| variant | val 2025 F1 MOT | test F1 MOT | P | R | flagget | B−#2044, 95 % KI |
|---|---|---|---|---|---|---|
| frossen #2044 | 0,520 | 0,476 | 0,441 | 0,517 | 68 | – |
| **+ prev_same_person (valgt på val)** | **0,536** | **0,525** | 0,517 | 0,534 | 60 | **+0,049 [+0,016; +0,090]**, B<A 0 % |
| + alle fire repotrekk | 0,530 | 0,512 | 0,478 | 0,552 | 67 | +0,036 [−0,008; +0,085], B<A 5 % |

Funn:
1. **Det nye signalet er personnøkkelen.** Vi har allerede selskap-, selskap+tekst- og tekst-historikk. Repoets direktørnavn-nøkkel fanger gjenvalg der teksten endrer seg (komité, tittel), og det har vi ikke. Bare to kolonner gir +0,049 på test, med KI helt over 0. Det skjer via presisjon (0,44 → 0,52): 8 færre falske MOT og én sann MOT til.
2. **Flere repotrekk hjelper ikke mer.** `prev_same_item` og `prev_meeting_any_dev` overlapper med våre egne historikktrekk. Med alle fire blir val litt lavere og test lavere enn bare person, og KI-et krysser 0.
3. **Mot #2485 (presedensregel oppå frossen):** 0,485 der, 0,525 her. Signalet virker bedre som trekk inne i modellen enn som en overstyring etter modellen. Det forklarer en stor del av repoets 0,545 (hybrid), men ikke hele.

Ærlige forbehold:
- 58 MOT i test: én sak er ca. ±0,01. KI-et er parret og ligger over 0, men det kommer fra 14 ulike prediksjoner.
- Repoets historikk oppdateres per (dato, møte). To møter i samme selskap samme dag kan i prinsippet se hverandre. Vår h2 bruker strengt tidligere dato. Effekten er antakelig liten, men den er ikke målt.
- Løpende historikk forutsetter at NBIM publiserer stemmene før neste møte (gjelder fra 2021, `c1_nbim_publisering.md`), samme som for frossen h2.
- Personregexen og navnefjerningen er laget av repoets forfattere med 2026 synlig. Vi har ikke valgt noe på test, men selve trekkdesignet er ikke rent ut-av-utvalg.

**Anbefaling for NESTE_VERSJON:** test nr. 1 = «#2044 + prev_same_person som trekk» (0,525 [KI-diff +0,016; +0,090]). Kombinasjonen med presedens-ELLER er ikke testet, og den må velges på val før den rører test. Ingen bytte nå: modellen er frosset.

Svarfiler: `arbeid/oppgave_2490/{full,person,repo4}_{val,test}.csv`, logger `*.log`.
