# Case 1: felles kjennetegn per forslag (smed, #1958) – forslagstype, aksjonærforslag, styrets anbefaling og historisk MOT-andel uten lekkasje

**Bruk:** `<split>/kjennetegn.csv` finnes for `data/`, `data_v3/`, `data_v3_val/` og `data_vif/`. Det er én rad per id i train ∪ test_input, og fila joines på `id`.
Lages på nytt med `python3 -I arbeid/hack/c1/kjennetegn/lag_kjennetegn.py arbeid/hack/c1/data_v3 ...` (tar 2 s for alle fire).
Lekkasjetesten kjøres med `python3 -I arbeid/hack/c1/kjennetegn/test_lekkasje.py`. Den bestod alle sjekker på alle fire splittene, se `kjennetegn/test_lekkasje.log`.

## Kolonner
- `forslagstype`: styrevalg, lonn, revisor, kapital, aksjonaer_miljo_sosial, aksjonaer_styring, annet. Den settes fra N-PX-kategorien og kilden, og teksten brukes når kategorien mangler.
- `undertype` (bare lønn): say_on_pay, fallskjerm (lønn knyttet til fusjon) og aksjeplan/frekvens.
- `fra_aksjonaer` (kilde SECURITY HOLDER) og `styret_anbefaler` (FOR/MOT, utledet fra kilden).
- `sel_*`, `seltype_*` og `fond_type_*`: `n_tidl`, `mot_andel_tidl`, `avvik_andel_tidl` og `siste_hist_dato`. De gjelder samme selskap (cusip), samme selskap og forslagstype, og forvalterens profil per forslagstype. Tallene regnes **bare fra train-rader med møtedato strengt før radens egen dato**. Test-rader ser derfor bare train, som ligger før grensedatoen. Train-rader ser bare fortiden og aldri sin egen stemme. Tom verdi betyr ingen historikk.

## Lekkasjetest (alle OK)
1. Id-ene er nøyaktig train + test_input.
2. fasit.csv åpnes aldri. Fila blir byte-lik når den bygges uten fasit.csv og når den bygges med stokket fasit.
3. test_input har ingen stemmekolonner. Nyeste historikkdato for test-rader ligger før grensen, for eksempel 2025-06-30 < 2025-07-01 i v3, og all historikk ligger strengt før radens egen dato.
4. Train-fasit ble stokket fra middato og utover. Ingen rad med dato ≤ middato endret seg, mens senere rader endret seg, så testen har kraft.
5. 300 tilfeldige rader ble regnet om med en naiv løkke og stemmer.

## MOT-andel per forslagstype i train
Vanguard, `data_vif` train (07.2023–06.2025, 70k forslag). "Avvik" betyr mot styret.

| type | n | MOT | avvik |
|---|---|---|---|
| styrevalg | 46 814 | 4,4 % | 4,4 % |
| lonn | 8 973 | 7,0 % | 7,0 % |
| revisor | 7 629 | 0,1 % | 0,1 % |
| kapital | 2 935 | 6,4 % | 6,5 % |
| annet | 1 993 | 10,7 % | 10,8 % |
| aksjonaer_miljo_sosial | 686 | 99,9 % | 0,1 % |
| aksjonaer_styring | 582 | 81,4 % | 18,6 % |

`data/` (v2, liten Vanguard-split) har samme mønster med lavere nivå: styrevalg 0,2 %, lønn 0,8 %, aksjonær-styring 10 % avvik og miljø/sosial 0 % avvik.
NBIM v3 train har bare say-on-pay og 9,1 % MOT. **Undertypen fallskjerm skiller seg ut: 28,6 % MOT i train (n=77) mot 8,6 % for vanlig say-on-pay.** Mønsteret holder utenfor utvalget: val 20,6 % (n=34) mot 8,8 %, og test 32,6 % (n=46) mot 9,5 %.

## Signal på holdout (fasit brukt bare til evaluering)
- v3 test: regelen `sel_avvik_andel_tidl > 0` gir F1 **0,383** og PR-AUC 0,283, mot en basisrate på 0,104. Det er nøyaktig dommerens gulv (#1966), så kolonnen reproduserer gulvet uavhengig.
- data_vif test: `seltype_avvik_andel_tidl` gir PR-AUC 0,127 mot en basisrate på 0,087. Hos Vanguard er historikken svak alene.
- `data/`: Splitten er strikt per selskap, så historikken dekker 0 % av test-radene. Der hjelper bare type og fondsprofil.

## Neste steg
Smed2 og smed3 kan legge til `undertype=fallskjerm` og `seltype_*` i v3-modellene. Fallskjerm alene er et ærlig regeltillegg til gulvet: MOT hvis historikken har MOT, eller hvis forslaget er fallskjerm. Det tillegget bør måles på val før det tas i bruk.

## Målt: gulv + fallskjerm (`arbeid/kandidater/smed_gulv_fallskjerm/train.py`)
Regelen er MOT hvis NBIM stemte MOT på selskapet før, eller hvis forslaget er fallskjerm. `p_avvik` er historikken glattet og løftet til fallskjerm-raten fra train.

| sett | gulv F1 / PR-AUC | gulv + fallskjerm F1 / PR-AUC | tavle |
|---|---|---|---|
| val 2025 (måler #1979) | 0,361 / 0,212 | **0,368 / 0,225** | #1005 |
| test 2026 (måler #1969) | 0,383 / 0,328 | **0,409 / 0,346** | #1004 |

Regelen er bedre på begge settene. Den har ingen frie parametre å tune, så val er ikke brukt til å velge noe. Gevinsten er liten på val (+0,007) og større på test (+0,026), der det er flere fallskjerm-saker (46 mot 34).
