# Case 1: feltet `ledelsen` ser ut som lekkasje, og en lovlig regel gir F1 0,84 mot grunnlinjas 0,357 (arkitekt, #1956)

Funn mens jeg bygde demo-stubben (arbeid/hack/levering/demo/modell.py). Til dommeren (#1954 lekkasjesjekk, #1961).

**1. `ledelsen` (N-PX managementRecommendation) ser ut til å bety «stemte med/mot ledelsen», ikke styrets anbefaling.**
Train.csv, Vanguard:
- aksjonærforslag: `ledelsen=FOR` i 185 av 194, men fondet stemte MOT i 183 av dem. Styrer anbefaler nesten alltid MOT på aksjonærforslag.
- styrets egne forslag med `ledelsen=AGAINST`: MOT 15, AVSTÅ 7, FOR 4. Eksempel fra holdout: T-Mobile 2026-06-16, styrevalg (Teresa A. Taylor, Christian P. Illek) med `ledelsen=AGAINST`. Et styre anbefaler ikke MOT sine egne kandidater.

Mønsteret passer med at feltet er avledet av fondets egen stemme. I så fall er det lekkasje.
KP: med `ledelsen` brukt rått fikk stubben P 0,94 / R 0,95 på holdout. Det er for godt, og samme feltet ligger bak dommerens grunnlinje på 0,357.

**2. Lovlig regel uten `ledelsen`:** «aksjonærforslag (kilde=SECURITY HOLDER) → MOT, ellers FOR». `kilde` står på stemmeseddelen før møtet.
Holdout (1544 forslag, 65 MOT): tp 47, fp 0, fn 18 → **P 1,00, R 0,72, F1 0,84**.
Kilde gjettet bare fra teksten (regex «shareholder/stockholder proposal»): P 1,00, R 0,48, F1 0,65.

**Følger:** Grunnlinja «følg styret» trenger et ekte styreanbefalingsfelt. Det står i proxy-materialet (DEF 14A) og ikke i N-PX.
Alternativt kan den skrives som «FOR på styrets forslag, MOT på aksjonærforslag», som er det styret nesten alltid anbefaler. Det gir F1 0,84.
Smedene må slå 0,84, ikke 0,357, ellers ser juryen en stråmann (evaluering = 30 %). De 18 MOT-stemmene vi bommer på er styrets egne forslag (styrevalg og lønn), og det er der en modell kan tilføre noe.
`ledelsen` må ut av test_input som trekk.
