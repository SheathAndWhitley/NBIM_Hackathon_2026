# Case 1: én kommando kjører hele agenten (smed #1998)

**Kommando** (fra landsbymappen, ca. 12 s, også fra tom mappe):
`uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut <tom mappe> [--csv saker.csv | --sak '<json>']`
Standard inn er holdout 2026 (`hack/c1/data_v3/test_input.csv`). Finnes fasit.csv ved siden av, måles det med `hack/c1/maaler.py`.

## Hva den gjør (ingen kandidatkode er skrevet om)
- **Modell:** `train_v3.py` i variant `--lekkasjefri` (dommer #1988 b / #1997). Skriptet kaller `modell()` og `velg_grense()` derfra, og argumentene hentes fra parseren til train_v3 selv.
- **Grense og ruting låses på val 2025:** rå grense 0,1833 (kalibrert P 0,114), val-F1 0,429 i utvalget. Det er det samme tallet som dommer #1993. 10 %-båndet (strategi A i case1_ruting.md) er 0,332 logit rundt grensen. Saker med instruksjonslignende tekst rutes også.
- **Sitat:** smed3s `agent.py` kjøres uendret som egen prosess og gir punkt-id, ordrett sitat og grunn. Kilden er **Vanguards** policy, ikke NBIMs, og det står i kolonnen `sitat_kilde`. Sitatagentens egen stemme står i `sitatagent_anbefaling`, så konflikter synes.

## Ut: `agent.csv`
id, utsteder, moetedato, forslag, anbefaling, p_mot, til_menneske, rutingsgrunn, punkt, sitat, sitat_grunn, sitat_kilde, sitatagent_anbefaling, injeksjon_flagget, raa_score. I tillegg `pred_maaler.csv` (måler-format, rutet = konfidens 0,5) og `KJORING.txt` med tall og sha256 for hver kodefil.

## Holdout 2026 (1246 saker, 129 MOT), kald start
| | F1 / SCORE | presisjon | recall |
|---|---|---|---|
| alle saker | **0,474** | 0,376 | 0,643 |
| maskinens saker etter 10 %-ruting (n 1127) | | 0,427 | 0,658 |
Rutet: 119 saker (9,6 %), og 18 av dem er MOT. PR-AUC 0,455. Stemmene og P(MOT) er identiske med en direkte kjøring av `train_v3.py --lekkasjefri` (0 avvik av 1246). Enkeltsak-modus gir samme P som batchen.

## Forbehold
- Alle say-on-pay-saker får samme sitat, `PIII / Say on Pay / ¶6` («case by case»). Sitatet er ordrett, men det begrunner ikke en MOT-stemme. NBIM-sitater kommer fra speider #1977.
- `train_v3.py` og smed3s `agent.py` ble endret mens jeg jobbet. Skriptet bruker filene der de ligger, og sha-ene står i KJORING.txt. Etter modellfrysen kl. 16 må det kjøres på nytt.
