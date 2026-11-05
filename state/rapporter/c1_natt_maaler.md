# Case 1: natt-måler med 2023 som vakt-år, én kommando (dommer2 #2867, ordre #281)

Kommando: `arbeid/c1_natt/mal_kandidat.sh SVARMAPPE [--vinkel TEKST] [--oppgave ID] [--av NAVN] [--torr]`

Svarmappa må ha `REGEL.md` (skrevet FØR svarfilene: mtime sjekkes, tom fil avvises) og nøyaktig én csv per år
som matcher `*2023*.csv`, `*2024*.csv`, `*2025*.csv`, `*2026*.csv` (format id,anbefaling[,p_avvik]).
2023-fila er val-året for T=2024 (modell trent på <2023), samme konvensjon som frossen `oppgave_2575/repo4_2024_val.csv`.

Skriptet måler kandidat og frossen repo4 på alle fire år med den offisielle måleren (`oppgave_2567/maaler_aar.py --score mot`,
F1 MOT mot styret), stopper med exit 3 om frossen ikke lenger gir de pinnede tallene 0,5057/0,5309/0,5120, og dømmer:
**BYTT** bare når snitt 2024-26 er minst +0,02 over frossen OG intet år (2023 medregnet) er under -0,02. Ellers **STÅR**.
Dommen med tabell skrives til `SVARMAPPE/DOM.md`, og forsøket føres på tavla med `tavle.py forsok --vinduer y2023..y2026`
(score = kandidatens snitt 2024-26, notat med dom og differanser; automåling slås av fordi dette er dommerens måling).

## Frossen repo4 per år (referanse)
| år | F1 MOT | merknad |
|---|---|---|
| 2023 | 0,3535 | vakt-år, val for T=2024 (grense valgt der), ikke hovedtall |
| 2024 | 0,5057 | |
| 2025 | 0,5309 | |
| 2026 | 0,5120 | |
| snitt 2024-26 | 0,5162 | |

## Akseptansetest: #2701-filene («av»-regelen) → STÅR
Mappe `arbeid/c1_natt/test_2701/` (REGEL.md skrevet først, så filene kopiert fra oppgave_2701).
2023 +0,0201, 2024 +0,0212, 2025 +0,0066, 2026 +0,0126, snitt +0,0135 < +0,02 → **STÅR**. Likt c1_2701_repo4_siste_regel.md.
Forsøk #1238 på tavla (oppgave 2867). Røde tilfeller testet: REGEL.md mangler → UGYLDIG exit 2; REGEL.md rørt etter filene → UGYLDIG exit 2.

## Slik bruker smedene den i natt
1. `mkdir arbeid/oppgave_<id>/svar && skriv REGEL.md der` (hva kandidaten er, ingen valg på test).
2. Lag de fire filene (2023 fra T=2024-val-kjøringen, 2024/25/26 test).
3. `arbeid/c1_natt/mal_kandidat.sh arbeid/oppgave_<id>/svar --vinkel "<kort navn>" --oppgave <id> --av <deg>`.
Dommeren leser DOM.md; BYTT gjelder først når en dommer har kjørt kommandoen selv på samme mappe.
