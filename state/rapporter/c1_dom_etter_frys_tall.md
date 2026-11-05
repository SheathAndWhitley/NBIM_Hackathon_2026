# Dom #2500: smedenes tall etter frys (#2495 hybrid+rangering, #2496 personnøkkel rullende)

Frossen 0,476 står til 20:00. Ingenting her endrer leveransen. Frysvakt: 17 filer uendret siden 16:00.

## Dom per tall

| sak | tall i rapport/NESTE_VERSJON | mitt tall | dom |
|---|---|---|---|
| #2495 V2 (hybrid sikker ja/nei, vår p ≥ 0,919 i midten), test 2026 | F1 MOT 0,516 (TP 32 FP 34 FN 26) | `maaler_offisiell_v3.py ... test --data real --score mot` → SCORE 0,516129, TP 32 FP 34 FN 26 | **stemmer** |
| #2496 personnøkkel rullende, test 2025 | 0,516 mot 0,514 uten (+0,001) | måleren vindu val: 0,5155 mot 0,5143 | **stemmer** |
| #2496 personnøkkel rullende, test 2024 | 0,418 mot 0,455 uten (−0,037) | eget skript `arbeid/oppgave_2500/mot_aar.py` (samme regel som måleren, måleren kjenner ikke 2024): 0,4179 mot 0,4545 | **stemmer** |
| kontroll: frossen #2044 test 2026 | 0,476 | måleren 0,476190, skriptet 0,4762 | stemmer |

Skriptet gir samme TP/FP/FN som måleren på 2025 og 2026, så 2024-tallene er sammenlignbare.
Smedens egne logger i `arbeid/oppgave_2496/*.log` oppgir avvik-F1 (SCORE 0,5098 / 0,4706 / 0,5134 / 0,5048).
Det er en annen metrikk enn hovedtallet. I NESTE_VERSJON.md står MOT-mot-styret-tallene, og de er riktige.

## Merking
Begge er merket «ikke hovedtall» i `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` (linje 83 personnøkkel rullende, linje 88 hybrid+rangering, i arbeidstreet, ikke committet ennå). Akseptkravet er oppfylt.

## Hva tallene sier
- Personnøkkelen (+0,049 i 2026) er et 2026-funn: −0,037 i 2024, +0,001 i 2025. Smedens konklusjon «holder ikke» er riktig.
- Hybrid + vår rangering: 0,516 er +0,040 over frossen med KI over 0, og −0,029 under hybriden alene. Ikke et bytte.
- Ingen protokollbrudd funnet: a, b, t og C er valgt på året før testen; test er brukt én gang.

Kommandoer:
```
uv run python arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2495/svar_V2_t2026.csv test --data real --score mot
uv run python arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2496/person_2025_test.csv val --data real --score mot
uv run python arbeid/oppgave_2500/mot_aar.py 2024 arbeid/oppgave_2496/person_2024_test.csv
```
