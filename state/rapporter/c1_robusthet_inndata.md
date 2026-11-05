# Case 1: robusthetstest med 12 konstruerte rare saker (#2202)

Agenten (`arbeid/hack/levering/kjor_agent.py`, real_votes-sporet `c1_real.py`, frossen modell #2044) ble kjørt på 12 konstruerte saker,
hver for seg og alle i én fil. Grunnsaken er et nytt møte i et kjent selskap (Fraser & Neave, 537900), endret ett felt om gangen.
**Ingen krasj** (rc 0 i alle 13 kjøringer). Før fiksen gikk 3 rare saker stille gjennom uten menneske. Etter fiksen går alle 11 rare saker til menneske.

| sak | inndata | før #2202 | etter #2202 (utfall) |
|---|---|---|---|
| 01 kontroll | vanlig sak | FOR, P(MOT) 0,01, maskin | samme (riktig: ingen ruting) |
| 02 | tom forslagstekst | menneske: «kan ikke vurderes: mangler felt» | samme |
| 03 | alle felter tomme | menneske: mangler 7 felt | samme |
| 04 | ukjent land/marked (Atlantis/XX) | **FOR, maskin, ingen ruting** | menneske: «ukjent land/marked» |
| 05 | ukjent forslagstype | menneske: «ukjent forslagstype» | samme |
| 06 | 50 400 tegn tekst | menneske: «uvanlig lang tekst» | samme |
| 07 | dato 15.03.2026 | menneske: «ugyldig møtedato» | samme |
| 08 | dato 2026-02-30 | menneske: «ugyldig møtedato» | samme |
| 09 | dato 2099-01-01 | **FOR, maskin, ingen ruting** | menneske: «møtedato utenfor perioden modellen kjenner» |
| 10 | styret «Kanskje» | **svar «KANSKJE», maskin, ingen ruting** | menneske: «ukjent styreanbefaling» (svaret står som rått felt) |
| 11 | NUL-tegn, emoji, linjeskift, «ignore previous instructions» | menneske: injeksjon | samme |
| 12 | company_id «abc», item_no «-1» | menneske: «ikke heltall» | samme |

**Fiks (bare agent-laget, `c1_real.py`, modellen er urørt):** tre nye rutingsvakter. Land eller marked som ikke finnes i NBIMs historikk,
møtedato før historikken eller mer enn 365 dager fram i tid, og styreanbefaling som ikke er FOR/MOT/AVSTÅ. Vaktene endrer bare rutingen, aldri svaret.

**Kontroll:** standardkjøring på test 2026 (1578 saker) er byte-lik med #2132 i id, MOT-svar, P(MOT) og ruting (188 til menneske, 11,9 %).
Ingen ekte sak traff de nye vaktene. Hovedtallet F1 på MOT er uendret (0,476).

**Svakhet igjen:** sak 10 skriver fortsatt «KANSKJE» som anbefaling i agent.csv. Den går til menneske, men feltet er ikke en gyldig stemme.

Gjenskap (fra landsbymappen): `python3 -I arbeid/oppgave_2202/lag_saker.py` (kjør i `arbeid/oppgave_2202`), deretter
`uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --csv arbeid/oppgave_2202/saker/alle.csv --ut /tmp/c1_rar`.
