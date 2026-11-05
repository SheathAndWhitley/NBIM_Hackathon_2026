# Case 1: V2 (#2495) rullet til 2024: taper mot frossen-oppsettet (sak 2531, ikke hovedtall)

**Spørsmål:** Er V2 (repoets hybrid avgjør sikre ja/nei, vår p avgjør midten) bedre enn frossen-oppsettet også i et annet år enn 2026?

**Oppsett:** `arbeid/oppgave_2531/rull.py` er `oppgave_2495/hent_hybrid.py` + `kombiner.py`, flyttet ett år tilbake.
Repoets hybrid er trent på årene til og med 2022, og den har valgt modell og t_flag på 2023. a, b og t er valgt på
2023 med samme gitter som #2495. Vår p_avvik er frossen-oppsettet rullet til 2024 fra #2496 (`full_2024_val/test.csv`,
trent på år før 2023/2024). Testen på 2024 er kjørt én gang. F1 MOT er målt uavhengig med `oppgave_2500/mot_aar.py`.
KI er parret klyngebootstrap per selskap (`oppgave_2496/diff_ki_aar.py`).

| Testår 2024 (val 2023) | Valg på 2023 | Val-F1 2023 | F1 MOT 2024 | TP/FP/FN | V2 − frossen, 95 % KI |
|---|---|---|---|---|---|
| Frossen-oppsett (dom #2500, uten person) | egen terskel | ca. 0,39 | **0,4545** | 30/14/58 | |
| V2 hybrid ja/nei + vår p i midten | a=0,625 b=0,269 t=0,96 | 0,4138 | **0,4072** | 34/45/54 | **−0,047** [−0,173; +0,092], 57 ulike pred. |
| V1 hybridflagg ELLER p≥t | t=0,979 | 0,4138 | 0,4048 | 34/46/54 | |
| V1p presedens ELLER p≥t | t=0,962 | 0,4052 | 0,4023 | 35/51/53 | |
| Hybrid alene (gbm structured only, t_flag 0,625) | | 0,4138 | 0,4072 | 34/45/54 | |

**Funn:** I 2024 er V2 0,047 dårligere enn frossen-oppsettet. KI dekker null, og V2 taper i 72 % av
bootstrap-trekkene. På 2023 valgte gitteret t=0,96, så vår p bidrar nesten ikke, og V2 blir i praksis lik hybriden
alene (samme F1 og nesten samme flagg). Hybriden flagger mange flere saker (79 mot 44), men bare 4 flere av dem
er riktige. Presisjonen faller fra 0,68 til 0,43.

**Sammen med 2026:** På 2026 fikk V2 0,516 og frossen 0,476 (+0,040 [−0,007; +0,095], dom #2529; rettet 16:50, sto først feil som 0,4923, som er en annen variant). I 2024 er forskjellen −0,047. Gevinsten
følger altså ikke med til et annet år, og dette er ikke grunnlag for å bytte. V2 hører hjemme under NESTE_VERSJON, og
der bare hvis flere år viser gevinst.

**Forbehold:** Val 2023 er svak for begge oppsett. Hybriden valgte her en annen modell («gbm structured only») enn i
2025-oppsettet. Det er bare ett ekstra år. 2025 er ikke kjørt.
Leveranse og frosne filer er ikke rørt.

Kjør på nytt: `cd arbeid/oppgave_2531 && uv run python rull.py`, deretter
`python3 -I arbeid/oppgave_2500/mot_aar.py 2024 arbeid/oppgave_2531/svar_V2_t2024.csv`.
