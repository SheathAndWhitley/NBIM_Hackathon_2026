# Generalprøve av frysvakta kl. 16 (#2174): PASS på alle tre punkter

Kjørt 13:11 på en kald kopi i /tmp/c1frys_prove. Ekte frys er ikke tatt (`state/c1_frys.json` finnes fortsatt ikke).

| Punkt | Resultat | Bevis |
|---|---|---|
| 1 LaunchAgent lastet, 16:00 | PASS | `launchctl print gui/501/no.landsby.c1frys`: lastet, `StartCalendarInterval` 16:00, runs=0 (har ikke fyrt). Ekstra: en midlertidig kopi av agenten (samme program og argumenter, frysfil i tmp) ble kjørt én gang med `kickstart`: exit 0, «FROSSET … 9 filer», samme hasher som tørrkjøringa. Kopien er fjernet etterpå. Konklusjon: /usr/bin/python3 3.9.6 under launchd leser landsbyfilene. |
| 2 Tørr frys skriver hashene | PASS | `c1_frys.py frys --frys /tmp/c1frys_prove/torr.json`: 9 filer hashet, exit 0. `sjekk` mot den: «FRYSVAKT GRØNN», exit 0. |
| 3 Negativtest: én byte endret | PASS | Kopi av de 9 filene frosset, så ble én byte i `arbeid/oppgave_2103/full_test.csv` endret (5→7, linje 788). `kaldstart.sh`: **exit 4**, «RØD FRYSVAKT: kald start stoppet». `fremmed.sh`: **exit 4**, «FRYSVAKT RØD», ingen målmappe laget. Begge viser fila og hash frosset 69702192d3a4 / nå e981bdc67c63. |

## Retting i verktøyet
Kaldstart- og fremmed-skriptene kaller `c1_frys.py sjekk` uten flagg, så det gikk ikke an å peke dem mot en kopi.
Jeg la inn testvariabelen `C1_FRYS_ROT` (standard for `--rot`, samme mønster som `C1_FRYS`). Uten variabelen
oppfører verktøyet seg som før. Pakka er ikke rørt.

## Å vite kl. 16
- Er minien i dvale kl. 16, kjører launchd jobben når den våkner. Sjekk `state/c1_frys.log` og `state/c1_frys.json` kl. 16.01.
- `frys` overskriver aldri en eksisterende frys, så at den fyrer igjen i morgen er ufarlig.
- Etter frys: en endring i noen av de 9 filene gir exit 4 i kaldstart.sh og fremmed.sh, og FAIL på krav 3 i sluttkontroll.sh.

Gjenta prøven: se kommandoene i oppgave #2174 (`C1_FRYS=<tmp.json> C1_FRYS_ROT=<kopi> bash arbeid/hack/c1/kaldstart.sh`).
