# Case 1: skript som lager demo-reserven på nytt og sjekker den mot frysen (#2322, arkitekt, 05.11 14.42)

**Sti:** reserven ligger i `arbeid/hack/levering/demo/reserve/`, ikke i `arbeid/hack/reserve/` som oppgaven sa
(den mappa er noe annet, gammel måler). Jeg utvidet `lag_reserve.sh` der den alt lå. Gammel versjon fra #2191: `lag_reserve_2191.sh`.

## Kommandoen dommeren kjører etter kl. 16 (fra landsbymappa, ca. 1 min 10 s)
```
sh arbeid/hack/levering/demo/reserve/lag_reserve.sh; echo "utgang $?"
```
- **Utgang 0, `RESERVE GRØNN`:** ny reserve på plass, gammel flyttet til `/tmp/c1_reserve_forrige_<tid>`. `SHA.txt` har tid, frystid,
  sha256 + `LIK FRYS` for kjor_agent.py, c1_real.py, kjor_agent_real_maskin_alene.csv, full_test.csv, pred_miks_h2.csv,
  sha av kald kopis agent.csv, `FRYSVAKT GRØNN` og `HOVEDTALL`-linja.
- **Utgang 4, `RESERVE STOPP: …`:** gammel reserve er urørt. Grunnen står på linja: frysvakta ikke grønn før kjøring (ikke frosset
  eller fil endret), fremmed.sh stoppet (4 = frysvakt rød i kald kopi), sha-avvik, frysvakta ble rød under kjøringen,
  eller HOVEDTALL / TALLVAKT GRØNN mangler i utskrift 3. Halvferdig ny reserve ligger i `reserve.ny/` til feilsøking.

## Hva skriptet gjør
1. `c1_frys.py sjekk --krev` før kjøring. Ikke grønn: stopp med 4 før noe kjøres.
2. Samme fire utskrifter som #2191 (demo_saker_2026.sh, demo_mangler_styret.sh, fremmed.sh kald kopi, demo_vis.py) + csv-ene,
   men inn i `reserve.ny/`.
3. SHA.txt: hver frosset sha sammenlignet med `state/c1_frys.json`. Én avvik: stopp med 4.
4. Frysvakt på nytt etter kjøring og grep på `HOVEDTALL` og `TALLVAKT GRØNN`. Først da flyttes den nye reserven på plass.

## Prøvekjørt nå (14.37–14.41), ærlig
- `bash -n`: ok.
- **Ekte kjøring nå:** utgang **4**, 0,03 s: `FRYSVAKT: ikke frosset ennå … --krev: STOPP`. Forventet før 16; gammel reserve (13.18) urørt.
- **Grønn vei mot testfrys** (`C1_FRYS=/tmp/c1_frys_test2322.json C1_RESERVE_UT=/tmp/c1_reserve_test2322`, frys tatt 14.38 av dagens filer):
  utgang 0 på 1 min 7 s, alle 5 sha `LIK FRYS`, `FRYSVAKT GRØNN: 10 filer`, `HOVEDTALL F1 MOT … 0.476190`. Ingenting flyttet (testmodus).
  KP: forventet 0,476190 (tavle.py levert), fikk 0.476190. kjor_agent.py dedc9406…87e2, som i c1_demo_planB.md.
- **Avviksvei** (testfrys med kjor_agent-sha satt til nuller): utgang **4**, `FRYSVAKT RØD … kjor_agent.py ENDRET`, reserven urørt.

## Ikke rørt
Frossen pakke #2044, agentkoden, c1_frys.py og fremmed.sh er uendret. `C1_RESERVE_UT` er bare for test (skriver ikke over reserven).

## Ekte kjøring etter frysen (#2325, arkitekt, 05.11 16.02)
`sh arbeid/hack/levering/demo/reserve/lag_reserve.sh` → **utgang 0, `RESERVE GRØNN`**, 2 min 3 s. Frys 2026-11-05T16:00:01 (#2044 miks h2).
- Frysvakt før og etter: `FRYSVAKT GRØNN: 17 filer like`. `SHA-SJEKK GRØNN: alle 5 lik frysen`, kjor_agent.py `dedc9406…87e2` LIK FRYS.
- `HOVEDTALL F1 MOT … 0.476190`. KP: forventet 0,476190 (frossen #2044), fikk 0.476190.
- Ny reserve i `arbeid/hack/levering/demo/reserve/` (SHA.txt laget 16:02:48), forrige (13.18, før frys) i `/tmp/c1_reserve_forrige_160248`.
- Mot forrige reserve: demo5/sitat/mangler_styret-csv byte-like. test2026_agent.csv har 3 rader med annen `mot_styret`
  (2045311|16, 2066391|14, 2086078|6: styret MOT, anbefaling FOR, ny 0 / gml 1). Ventet: forrige reserve var laget med
  kjor_agent.py `638d5fea…` før frysen; anbefaling og hovedtall er like. Ikke rettet noe, bare notert for dommeren.
