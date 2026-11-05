# Case 1 #2653: ordsjekk-treff i BYTT-tekstene rettet (smed2)

- Rettet alle punkt 1–8 i «Rettelsesliste BYTT til smed2» og dommer-tillegget #2658 (J:57, J:81).
- Regnefeil: «0,512 under målet» → «like over målet» (kravrespons:10, ERLIG:53). KI i kravrespons:7 → [0,40; 0,62].
- J:82 → «Dommen 16:37 lot den frosne stå mot V2 og hybriden; ved 17:02 ble repo4 byttet inn etter regelen (se sp. 20).» J:83 → repo4 i drift.
- J:57/J:81 skrevet om til repo4 (0,512, byttet 17:02 etter regel på 2024/25, sp. 20).
- «0,512 til 0,415» → «den eldre frosne modellen fra 0,476 til 0,415» (ERLIG:29, J:23).
- Internspråk: grønn/benk/tallvakt → «kjørte feilfritt fra kald start», «sammenligning A/B», «besto», «tallsjekk (...)». «valgt på test» → «valgt ut fra test».
- repo4 forklart ved første bruk i levering/README, leveranse/README, J:12, kravrespons, ERLIG.

Sjekker etterpå: ordsjekk.sh 0 treff utenom `<!-- tallvakt` og levering/README.md:45. sjekk_rod.sh punkt 1 og 3 GRØNN (punkt 5 RØD: SVAKHETER.md:77 «older 0.476», smed4 sitt #2665). c1_tallvakt.py --rot .: 195 påstander, 0 avvik, OK.
Skript: arbeid/oppgave_2653/rett.py. Backup: arbeid/oppgave_2653/backup_*.
