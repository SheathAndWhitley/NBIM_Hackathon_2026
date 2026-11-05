# Case 1: India-bryteren er frys-kandidat. Den vinner 2024 og 2025, men på tynt grunnlag (#2307)

**Kort sagt:** Kopien med bryteren PÅ slår frossen #2044 på begge årene med samme seed og samme grense. Måler er v3 med `--score mot`.
Den formelle regelen er dermed oppfylt. Avgjørelsen er dommerens (#2297), og frossen agent står til dommeren har sagt ja.

| år | bryter AV (= frossen) | bryter PÅ | endring | snudde FOR→MOT | riktige | forsøk |
|---|---|---|---|---|---|---|
| val 2025 | 0,520231 | **0,561798** | +0,042 | 5 | 5 av 5 | #1164 |
| holdt-ut 2024 (trent på år < 2024) | 0,536313 | **0,544444** | +0,008 | 1 | 1 av 1 | #1165 |

## Forbehold (les før ja)
- **2025 er ikke et rent mål.** Regelen ble funnet på val 2025, så +0,042 er optimistisk.
- **2024 er det eneste ærlige beviset, og det bygger på én sak** (1886920|4). Det er for lite til å vise noe statistisk. Det betyr bare at regelen ikke tapte.
- **2024 er målt med v3 importert uendret.** Bare vindu-funksjonen er byttet til «år == 2024» (`maal_aar.py`), fordi v3 ikke har et eget 2024-vindu. Innpakningen gir nøyaktig samme tall som v3 direkte på 2025.
- **Regelen endrer bare `anbefaling`.** `konfidens` (0,9) og `p_avvik` (0,66–0,89) er uendret for de snudde sakene. Med terskel 0,6 går ingen av dem til et menneske (målt).
- Test 2026 er ikke kjørt (`--kun-val 1`). Ingen fil i den frosne mappa er endret.

## Sha256
- `arbeid/oppgave_2303/train.py` (kopien med bryter): b6ef58bdd43f7f3e779f3…
- `arbeid/oppgave_2044/train.py` (frossen, urørt): 772fb71500e397cc463d7…
- `arbeid/hack/levering/c1_real.py` (urørt): f0acb3c5aeddac50…
- v3-måler `arbeid/hack/c1/maaler_offisiell_v3.py`: 418a937e57e52e56e7d39…
- `val_frossen_2025.csv` = `val_av_2025.csv`: c1138c9d911d43274466c… (bryter AV gir byte-lik fil med frossen)
- `val_india_2025.csv`: 38ab16151434e5bfb7071…
- `val_av_2024.csv`: 992a0d45d6f9cbda45806…
- `val_india_2024.csv`: 5935b97914fcd327e6851…

## Kommandoer
```
bash arbeid/oppgave_2303/kjor.sh                       # ca. 3 min, lager alle fem val-filene
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2303/val_india_2025.csv val --data real --score mot
python3 -I arbeid/oppgave_2303/maal_aar.py arbeid/oppgave_2303/val_india_2024.csv 2024
```

## Hvis dommeren sier ja (før kl. 16): å bytte TRAIN og argv er IKKE nok
`c1_real.py` regner `mot = s >= t` selv, ut fra modellens score. Flaggene fra `flagg()` i train.py brukes aldri.
Endres bare TRAIN og argv, slik #2303 foreslo, får agenten nøyaktig de samme svarene som i dag.
En koblet kopi ligger i `arbeid/oppgave_2307/levering/`. Den har tre endrede linjer mot `arbeid/hack/levering/c1_real.py`:
- linje 35: `TRAIN` peker på `oppgave_2303/train.py`
- linje 85: argv får `"--india", "1"`
- linje 219: `mot = bool(s >= t or g["REGEL"][idx[rid(r)]])`

Kopien sammenlignet med frossen agent på test 2026-input (`--csv`, uten `--vindu`, se `arbeid/oppgave_2307/kjor.sh`, rundt 7 s), bare diff av svarene. Ingen fasit er lest:
- 1578 saker, **2 snudd FOR→MOT**: 2080562|4 og 2080562|6. Bare disse to radene er endret. Der endres anbefaling og mot_styret, og MOT-sakene får sitat, punkt og retningslinje. Ruting og p_mot er uendret.
- `p_mot` er uendret, 0,09 og 0,19. Agenten sier altså MOT, men oppgir lav P(MOT). Det er en synlig motsigelse i beslutningsstøtten.
  2080562|6 går til et menneske (båndet), 2080562|4 gjør ikke det. Bør regelen inn, bør regel-sakene få egen rutingsgrunn («India-regelen, ikke modellen»), eller alltid sendes til et menneske.
- Merk: train.py sin interne linje «TEST 2026 …» og loggens SCORE 0,4818 er like i begge kjøringene. De reflekterer ikke agentens endrede svar, og jeg har ikke brukt dem.

Etter en eventuell innkobling: c1_frys-sha må tas på nytt, og kaldstarten må kjøres. Jeg har ikke gjort noe av dette i frossen mappe.

## Min anbefaling
Den formelle regelen er oppfylt, men gevinsten er liten: én ærlig sak i 2024 og to saker i 2026. Den nye motsigelsen mellom p_mot og svaret svekker robustheten.
Med under 1,5 time til frys mener jeg det er tryggest å **la frossen agent stå** og nevne regelen i JURY.md som et testet funn. Dommeren avgjør.
