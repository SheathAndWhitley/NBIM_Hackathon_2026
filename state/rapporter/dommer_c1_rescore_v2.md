# Case 1: alle modeller målt på nytt med måler v2 (dommer, #1965)

Måler v2 `arbeid/hack/c1/maaler.py` (sha 52292737df), holdout 1544 forslag, 65 MOT, 22 avvik fra utledet styre.
**Alle 22 avvik gjelder ISSUER-forslag: 18 MOT + 4 AVSTÅ.** ISSUER-MOT telles med `arbeid/oppgave_1965/issuer_mot.py`.

| kandidat | forsøk | ISSUER-MOT tp/fp/fn (n=18) | AVVIK P/R | AVVIK F1 (SCORE) | AVVIK PR-AUC | MOT-F1 totalt |
|---|---|---|---|---|---|---|
| grunnlinja: følg utledet styre | #977 | 0/0/18 | 0 / 0 | 0,000 | 0,014 (basisrate) | 0,839 |
| smed2 lgbm, pred.csv (mål=mot) | #978 | 0/0/18 | 0 / 0 | 0,000 | 0,018 | 0,839 |
| smed2 lgbm, mål=avvik (kjørt av dommer) | #979 | 0/0/18 | 0 / 0 | 0,000 | 0,021 | 0,839 |
| smed3 sitatagent v2 (0,8596 på v1) | #980 | 2/0/16 | 1,00 / 0,136 | 0,240 | 0,153 | 0,860 |
| smed3 sitatagent v5 | #981 | 2/0/16 | 1,00 / 0,136 | 0,240 | 0,155 | 0,860 |

## Kontroller
- **Lekkasje:** test_input.csv har ingen av `ledelsen/mot_ledelsen/delt/n_rec/stemme/mgmt_felt_LEKKER` (måleren gir UGYLDIG hvis de finnes). Koden er lest: smed3s `agent.py` og smed2s `train.py` bygger historikk bare fra train.csv (smed3: strengt før møtedato, smed2: `_del=="tr"`), og ingen av dem leser de forbudte kolonnene. Begge er godkjent.
- **Reproduksjon:** smed3 v5 er kjørt på nytt fra ren tilstand (`python3 -I agent.py data/train.csv data/test_input.csv`). Kolonnene id, anbefaling og konfidens ble identiske med innmeldt fil. smed2 med mål=avvik er kjørt av dommeren.

## Hva treffene egentlig er (ærlig)
- smed3s to ISSUER-MOT-treff er begge **Garmin «new or modified agenda items»** (fullmakt til ukjente saker). Det er én regel og nesten triviell. Ingen styrevalg, say-on-pay eller reinkorporering er fanget.
- Avvikstreff nr. 3 er **Dell, reinkorporering**: agenten sier AVSTÅ, fasit er MOT. Måleren teller det som tp fordi begge avviker fra styret, men retningen er feil.
- De 16 som ikke fanges ligger samlet: T-Mobile 6, Warner Bros. Discovery 4 (+1 AVSTÅ), Rocket 3 (+1 AVSTÅ), Dell say-on-pay, AON pay. Avvikene klumper seg per selskap. En selskapsvis vinkel (kontrollert selskap, Class-struktur, kontroversielt møte) kan flytte mange på én gang. Det er et tips til #1964.
- smed2: lgbm finner ingen avvik, heller ikke med mål=avvik. PR-AUC 0,021 er bare litt over basisraten.

## Dom
smed3s sitatagent er eneste kandidat over grunnlinja: MOT-F1 0,860 mot 0,839 og AVVIK F1 0,24 mot 0. Fortrinnet hviler på én regel (Garmin-typen). Med 22 positive er det tynt: én fanget sak gir ca. 0,05–0,08 F1.
