# Case 1: plan B for demoen kl. 20 hvis live-kjøringa svikter (#2321, arkitekt, 05.11 14.35)

**Kort sagt:** Plan B er reserven fra #2191: ferdige utskrifter som vises med `cat`, uten nett, Python eller agent.
**Viktig funn:** reserven er nå **utdatert**. `reserve/SHA.txt` (laget 13.18) har kjor_agent.py `638d5fea…8b17`,
men fila er nå `dedc9406…87e2` (endret 13.28), og c1_real.py er endret 14.32. Reserven må lages på nytt etter frys
kl. 16 (punkt 3 under). Før det kan den ikke vises som «samme modell».

## Hvilket tall gjelder (frysbeslutningen)
- **Standard: F1 MOT 0,476190** (TP 30, FP 38, FN 28; v3 `--score mot`, test 2026). Dette er det leverte tallet i
  `tavle.py levert` (forsøk 1046, `kjor_agent_real_maskin_alene.csv`). Det står hvis dommeren (#2297) ikke sier ja
  til India-bryteren før kl. 16, og det er det smed2 råder til (`c1_india_paret.md`: 2024-beviset er én sak, perm p = 1,0).
- **India-tallet gjelder bare hvis** dommeren sier ja i #2297 **og** #2312 er gjort før frys **og** `tavle.py levert`
  er satt på nytt. Det finnes **ikke noe India-tall for test 2026 ennå** (bare val: 2025 0,562, 2024 0,544, som ikke
  kan sammenlignes med 0,476). Si aldri «0,56» i demoen som testtall.
- Regel for kl. 19.30: **tallet på scenen er det `uv run python tavle.py levert` viser, og det må stå i
  `reserve/3_fremmed_kald_kopi.txt` på linja `HOVEDTALL`.** Avviker de: bruk tallet fra måleren, ikke fra manus.

## Hva som vises hvis live svikter (alle stier fra landsbymappa)
| Steg i demoen | Live | Plan B (bare `cat`) |
|---|---|---|
| Sak 1–6 (manus, seed 17 + sitatsak) | `bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_demo2026` | `sh arbeid/hack/levering/demo/reserve/vis_reserve.sh 1` |
| Sak 7: styret mangler | `bash arbeid/hack/c1/demo_mangler_styret.sh /tmp/c1_demo_m` | `… vis_reserve.sh 2` |
| Kald kopi + hovedtall + tallvakt | `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald` (ca. 40 s) | `… vis_reserve.sh 3` |
| 3 saker med NBIM-sitat | `arbeid/hack/c1/leveranse/demo.sh` | `… vis_reserve.sh 4` |
| Rådata hvis juryen spør | – | `arbeid/hack/levering/demo/reserve/csv/test2026_agent.csv`, `demo5_agent.csv` |
| Siste nødutgang (maskin død) | – | `arbeid/hack/c1/leveranse/demo_utskrift.txt` og `reserve/*.txt` er ren tekst i pakka |

Feiltabellen (uv uten nett, PATH, feil mappe, krasj, frysvakt rød) står i `arbeid/hack/levering/demo/RESERVE.md`. Ikke dupliser.
Si høyt: «dette er en lagret kjøring fra i dag kl. HH.MM, samme frosne modell» (tida står øverst i hver utskrift).

**Tekstutdrag fra reserven slik den er nå (13.18, før frys, skal byttes):**
```
HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190
TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring
Kjøring: til menneske 188 av 1578 inn (11.9%), 183 av 1539 med fasit (11.9%)
FRYSVAKT: ikke frosset ennå   <- må bli grønn etter ny kjøring
```

**Sha256 nå (14.35), til sammenligning ved 19.30:**
- `arbeid/hack/levering/kjor_agent.py` dedc94062cf414e9038ec6094edce272dcb8c6d15a36629f8bc49226eeac87e2 (≠ reserve 638d5fea…)
- `arbeid/hack/levering/c1_real.py` 439b49f7483674e55456e89bafa7eb2fdf2f9dbea9d31dfc500e6656e434f378
- `arbeid/hack/levering/kjor_agent_real_maskin_alene.csv` 22ac6717e1287c5ae1cc8b53471823dbcfa9e04fdda97b474ba1e9af0cbc788f
- `arbeid/oppgave_2103/full_test.csv` 69702192d3a4309ef5b41c6779a24d5c943489244557e030f027dadad3de8dfc
- `reserve/3_fremmed_kald_kopi.txt` 8503737bc705e3bb65c0aa41ade3ef188c912f05a49a88b98c031e7af7e749f4 (gammel)
Fasit for frosne filer etter kl. 16 er `state/c1_frys.json` (skrives av LaunchAgent `no.landsby.c1frys`), ikke denne lista.

## Sjekkliste for dommeren kl. 19.30 (8 punkter, fra `<repo>`)
1. **Frysvakt:** `python3 -I arbeid/verktoy/c1_frys.py sjekk --krev` → utgang 0. Rød: stopp, ikke demo live; bruk punkt 3-reserven bare hvis den er laget etter frys.
2. **Levert tall:** `uv run python tavle.py levert` → noter tallet (0,476190 med mindre India ble tatt inn, se over).
3. **Reserven er fra etter frys:** `head -3 arbeid/hack/levering/demo/reserve/SHA.txt` → tid etter 16.00, kjor_agent.py-sha lik den i `state/c1_frys.json`, ingen «ikke frosset». Hvis ikke: `sh arbeid/hack/levering/demo/reserve/lag_reserve.sh` (ca. 1 min), sjekk på nytt.
4. **Tallet i reserven = levert tall:** `grep HOVEDTALL arbeid/hack/levering/demo/reserve/3_fremmed_kald_kopi.txt` og `grep "TALLVAKT GRØNN" …/3_fremmed_kald_kopi.txt` → begge treffer, tall som i punkt 2.
5. **Reserven vises uten miljø:** `env -i PATH=/usr/bin:/bin sh arbeid/hack/levering/demo/reserve/vis_reserve.sh > /tmp/pb.txt; echo $?` → 0 og 4 `RESERVE:`-linjer (`grep -c RESERVE: /tmp/pb.txt` = 4).
6. **Live-veien går offline:** `export PATH=/opt/homebrew/bin:$PATH; UV_OFFLINE=1 bash arbeid/hack/c1/demo_saker_2026.sh /tmp/c1_pb_live > /tmp/pb_live.txt 2>&1; echo $?` → 0, under 30 s, og sak-id-ene lik `reserve/1_saker_2026.txt` (`diff <(grep '^==' /tmp/pb_live.txt) <(grep '^==' arbeid/hack/levering/demo/reserve/1_saker_2026.txt)` tomt).
7. **Manus og jury sier samme tall:** `grep -n -E "0[,.]47|0[,.]56|0[,.]54" arbeid/hack/c1/DEMO_MANUS.md arbeid/hack/c1/leveranse/JURY.md` → bare tallet fra punkt 2 brukes som testtall; val-tall (0,52/0,56) er merket val.
8. **Kopi utenfor maskina-avhengighet:** `cp -R arbeid/hack/levering/demo/reserve /tmp/planB_kopi && ls /tmp/planB_kopi/*.txt` → 4 filer; åpnes med hvilken som helst teksteditor hvis terminalen dør.

Ett punkt rødt i 1–5: demoen kjøres fra reserven, ikke live. Rødt i 6: start live-skriptet i bakgrunnen ved 0:00
(står i RESERVE.md), og bytt til `vis_reserve.sh 1` hvis det ikke er ferdig ved 0:40.

## Det jeg ikke gjorde
- Kjørte ikke `lag_reserve.sh` nå: den overskriver #2191-reserven, og agenten er ikke frosset. Riktig tid er etter 16.00
  (helst etter #2297/#2312, så India-valget er med). Eier: #1975 (speider) eller dommeren i punkt 3.
- Rørte ingen agent-, modell- eller målerfil.

## Akseptkrav sjekket (14.36)
`ls` på alle 22 stier i planen: alle finnes (unntatt `state/c1_frys.json`, som LaunchAgent skriver kl. 16).
Punkt 5 prøvd nå: `env -i … vis_reserve.sh` exit 0, 4 `RESERVE:`-linjer.
