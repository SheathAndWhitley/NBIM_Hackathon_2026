# Case 1: prøvefrys kl. 15:30 (#2405), tørrmodus

**Dom: GRØNN. Frysen kl. 16 kan gå rent.** Ingenting ble låst: `state/c1_frys.json` finnes ikke før eller etter prøven.

## Hva ble gjort
- `python3 -I arbeid/verktoy/c1_frys.py frys --frys /tmp/c1_provefrys.json` (egen frysfil i /tmp): FROSSET 17 filer, utgang 0.
- `c1_frys.py sjekk --krev --frys /tmp/c1_provefrys.json`: FRYSVAKT GRØNN, 17 filer like. Også kjørt med `/usr/bin/python3 -I`, samme tolk som LaunchAgenten: FRYSVAKT GRØNN: 17 filer like som ved frys 2026-11-05T15:27:58.
- LaunchAgent `no.landsby.c1frys` er lastet (launchctl list, siste utgang 0), kjører kl. 16:00: `/usr/bin/python3 -I .../c1_frys.py frys`, logg i state/c1_frys.log. Kontrollen `no.landsby.c1frys_kontroll` kl. 16:03 (#2247) er også lastet.
- Hovedtallet: `maaler_offisiell_v3.py kjor_agent_real_maskin_alene.csv test --data real --score mot` gir SCORE 0.476190 = kv hack_levert (forsøk 1046, frossen #2044 miks h2). Det er #2044 som fryses (frysfila sier modell "#2044 miks h2").

## Filene som fryses kl. 16 (sha256, første 16 tegn, målt nå)
| sha256 | fil |
|---|---|
| 772fb71500e397cc | arbeid/oppgave_2044/train.py |
| 40afcc3e2fec85b2 | arbeid/oppgave_2044/pred_miks_h2.csv |
| 69702192d3a4309e | arbeid/oppgave_2103/full_test.csv |
| dedc94062cf414e9 | arbeid/hack/levering/kjor_agent.py |
| 439b49f7483674e5 | arbeid/hack/levering/c1_real.py |
| 51cd0698342cfd7b | arbeid/hack/levering/injeksjon_hoflig.py |
| 22ac6717e1287c5a | arbeid/hack/levering/kjor_agent_real_maskin_alene.csv |
| 19c3629fa670ffd8 | arbeid/oppgave_2047/vern.py |
| d403dd3c8f3b5876 | arbeid/oppgave_2046/case1_mot.py |
| 71ba5135e7ba9d64 | state/opplastet/20261105_114241_real_votes.csv |
| 0a45c013471bd0b1 | arbeid/hack/levering/retningslinje_oppslag.py |
| 089ddbddb839d9f3 | arbeid/hack/c1/retningslinjer/punkter.jsonl |
| 1e0e22f86bbf21ea | arbeid/hack/c1/data_off/real_test_input.csv |
| 1111f1afce04f906 | arbeid/hack/c1/maaler_offisiell_v2.py |
| 418a937e57e52e56 | arbeid/hack/c1/maaler_offisiell_v3.py |
| 96fcf3b1c1089027 | arbeid/kandidater/smed2_c1_mot/pyproject.toml |
| ed54fd6c8f92f347 | arbeid/kandidater/smed2_c1_mot/uv.lock |

## Endret etter siste grønne kaldstart #2402 (done 15:25:49)?
- De 17 frosne filene: **nei**. Nyeste mtime er 14:32:22 (c1_real.py), alle committet, `git status` tom for alle 17.
- sluttsjekk.sh: endret 15:27 (commit 4164bb5, steg 7 tekstavtrykk, #2392). Ikke i frysen, lov ifølge oppgaven. `bash -n` ok, ingen ucommittet diff.
- Andre pakkefiler endret etter #2402 (alle tekst i arbeid/hack/c1/leveranse/, ikke kode eller modell, dekkes ikke av frysen men av tekstavtrykket fra 16:03): ERLIG_EVALUERING.md (15:26, smed3 #2395), kilder/c1_robusthet_reprod.md (15:27, smed3), demo_utskrift.txt (15:28, ucommittet, speider #2406 pågår). Ventet, siden tekstene skal oppdateres etter frysen (#1975).

## Merknader
- #2392 (smed) og #2404 (smed4) er samme oppgave (tekstavtrykk-linja i sluttsjekk.sh). Innholdet er alt committet i 4164bb5; #2404 bør lukkes som dublett så to smeder ikke redigerer samme fil før frysen.
- Prøvefrysfila /tmp/c1_provefrys.json kan brukes til å sammenligne med state/c1_frys.json etter kl. 16: sha-ene skal være identiske.
