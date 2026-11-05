# Case 1: dom over AVVIK i frysen kl. 16 (#2474, kontroll #2247)

Dommer, 05.11 kl. 16:15. Dom: **FRYSEN ER RIKTIG. Avviket er et foreldet referansesett, ikke en gal frys.**

## Hva kontroll.sh meldte
9 av 17 frosne filer «sha ulik #2243». Referansen (`arbeid/oppgave_2247/referanse_2243.json`) ble tatt kl. 13:51 av 10 filer; frysen kl. 16:00 låste 17.

## Funn, fil for fil

| Fil | Type avvik | Forklaring | Dom |
|---|---|---|---|
| real_test_input.csv, maaler_offisiell_v2.py, maaler_offisiell_v3.py, punkter.jsonl, retningslinje_oppslag.py, smed2_c1_mot/pyproject.toml, smed2_c1_mot/uv.lock | «ref mangler» (7 filer) | Sto ikke i referansen fra 13:51. Alle har mtime før 13:51 (nyeste 13:31:15), de git-sporede har ingen diff mot 9012a58 og ingen commit etterpå. Ikke endret. | ikke et avvik |
| arbeid/hack/levering/injeksjon_hoflig.py | ekte sha-endring, mtime 14:27:52 | #2265 Title Case-vakt (smed2, lukket 14:2x). Rapportert ny sha 51cd0698 = frossen sha. Bekreftet fra kald kopi i #2266, #2358 (dommer2), #2380/#2387 (16/16 fanget, F1 0,476190). | godkjent, bevisst før frys |
| arbeid/hack/levering/c1_real.py | ekte sha-endring, mtime 14:32:22 | To endringer: (a) #2257 ruting «ikke-latinsk skrift» (dom #2264: godkjent, treffer 0 test-/historikkrader). (b) #2309 mot_styret i agent.csv = anbefaling MOT og styret ≠ MOT; gammel verdi lever videre som internt felt `avvik` og er det pred_maaler.csv skrives fra. 3 celler i agent.csv endret (74→71), pred_maaler byte-lik. | godkjent, bevisst før frys |

Gammel versjon hentet fra kald kopi `/private/tmp/c1_kald.oChD4r` (13:49:03, sha 83fe0eb0 / 150b92e9 = referansen). Diff lest linje for linje: ingen modell-, terskel- eller treningsendring. pred_maaler.csv skrives fra samme verdi som før (`avvik` = gammel `mot_styret`), derfor samme pred-sha b113b545 og F1 MOT 0,476190 i kontrollens egen kaldstart etter frys.

## Konsekvens
- Frossen sha for begge filer er den som alle dommer etter 14:32 har målt på (#2380, #2387, #2395, #2406, #2414, #2421, #2436, #2452, kald kopier 15:09–16:01 har alle 439b49f7/51cd0698).
- agent.csv har ny sha (1543706f, ikke f0444a47) siden #2309. Det er kjent og rettet i papirene (#2325, #2329, commit b269f8d).
- kontroll.sh-feil: «ref mangler» telles som NEI. Det er en rapporteringsfeil, ikke et pakkeavvik. For #2440 og sluttsjekken 19:30 er riktig fasit `state/c1_frys.json` (17 filer) og `arbeid/hack/levering/frys_fasit_1600.sha256` (#2445), ikke referanse_2243.json.

## Ikke gjort
Jeg har ikke kjørt egen kaldstart her: kontrollen kjørte den kl. 16:01 (GRØNN, 58 s) og #2473 (dommer2) dømmer smed3s kaldstart etter frys parallelt.
