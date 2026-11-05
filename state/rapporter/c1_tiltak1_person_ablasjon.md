# Tiltak 1-ablasjon: bare samme-person-trekkene (4–7) gir +0,007 på val 2025 og −0,018 på 2024. Ikke bygg inn.

Oppgave #2296 (smed3). Test 2026, frossen #2044 og miks h2 er ikke rørt. Ingen test-2026-prediksjon er laget.
Kode: `arbeid/oppgave_2296/train_t1p.py` = kopi av `arbeid/oppgave_2283/train_t1.py` + `--trekk` (komma-liste over
hvilke av de 15 tiltak-1-kolonnene som beholdes). Samme miks, `--hist 2`, τ=1, samme C-rutenett og grensevalg på val.

Kolonne 4–7 = samme person (navnenøkkel fra #2044): sett før, siste stemme MOT, år siden siste MOT, «MOT før, FOR sist».
Komplementet (0–3 + 8–14) = selskapets forfalte MOT-andel på styrevalg og MOT per rationale_section fra tidligere år.

## Tall (val 2025: måler v3 `--score mot`; 2024: intern F1 fra boot.py; grunnlinje = arkitektens t1=0-kjøring)

| oppsett | val 2025 F1 MOT (v3) | diff 2025 (boot, KI 95 %, P>0) | 2024 F1 | diff 2024 (boot, KI 95 %, P>0) |
|---|---:|---:|---:|---:|
| grunnlinje (t1=0) | 0,520231 | – | 0,5672 | – |
| alle 15 trekk, τ=1 (#2283) | 0,550898 | +0,026 [−0,013, 0,070] 0,89 | 0,5524 | −0,015 [−0,043, 0,017] 0,19 |
| **bare person 4–7, τ=1** | **0,527607** | +0,007 [−0,031, 0,045] 0,65 | **0,5489** | −0,018 [−0,083, 0,041] 0,27 |
| komplement (0–3, 8–14), τ=1 | 0,512500 | −0,016 [−0,095, 0,061] 0,39 | 0,5572 | −0,010 [−0,048, 0,030] 0,30 |

Styrevalg val 2025, bare person: P 0,63, R 0,43, TP 27 (grunnlinje P 0,56, TP 28). På 2024 velger modellen en lav
grense (168 flagget mot 98 MOT, P 0,43), altså ustabil kalibrering.

## Funn
- Kravet «bedre begge år» er ikke nådd for noen delmengde. Person-trekkene alene gir nesten ingenting på 2025 og
  samme tap på 2024 som hele settet.
- Gevinsten på 2025 (+0,031) ligger i kombinasjonen, ikke i én av delene: person alene +0,007, komplement alene −0,016.
  Det styrker arkitektens lesning: gevinsten følger året, ikke mekanismen.
- Ingen variant av tiltak 1 har P(bedre) over 0,3 på 2024. Sporet bør lukkes med dette tallet.

## Kommandoer
```
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2296/train_t1p.py \
  state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 --t1 1 --tau 1 --trekk 4,5,6,7 --vaar 2025 --ut val_p_tau1.csv
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2296/val_p_tau1.csv val --data real --score mot
uv run --project arbeid/kandidater/smed2_c1_mot python -I arbeid/oppgave_2283/boot.py 2024 \
  arbeid/oppgave_2283/v2024_t10_tau1.csv arbeid/oppgave_2296/v2024_p_tau1.csv
```
Filer: `arbeid/oppgave_2296/{val,v2024}_{p,k}_tau1.csv`, `log*`, `boot*`.
