# Case 1 #2707: «av» + fyll frigjorte flagg – dårligere enn «av» alene, frossen står

Regel skrevet før måling (arbeid/oppgave_2707/REGEL.md): repo4 + «av» (#2701). Flaggene som «av» fjerner, fylles opp igjen med neste sak etter p_avvik (antall flagg holdes likt).
Offisiell måler oppgave_2567/maaler_aar.py --score mot.

| | 2024 | 2025 | 2026 | snitt |
|---|---|---|---|---|
| repo4 (frossen) | 0,5057 | 0,5309 | 0,5120 | 0,5162 |
| av alene (#2701) | 0,5269 | 0,5375 | 0,5246 | 0,5297 |
| av+fyll | 0,4972 | 0,5342 | 0,5280 | 0,5198 |

Fylte flagg: 10, 4 og 3. Gevinsten fra «av» kommer av at agenten flagger færre saker (høyere presisjon). Fyller man på igjen, forsvinner gevinsten, og 2024 blir dårligere enn frossen.
Etter #265 er snittet +0,004 og 2024 er -0,009. **Frossen står.** Lærdom: bruk «av» uten å fylle på.
Kode: `uv run --project arbeid/oppgave_2023 python arbeid/oppgave_2707/av_fyll.py`
