# Dom #2814: GitHub-historikken etter rensen (#2812/#2816) er GRØNN

Dommer2, 2026-11-05 19:2x. Fersk `git clone` av origin (git@github.com:Martinkristofferhansen/nbim.git,
deploy-nøkkel) til tom mappe /tmp/c1_rens_dom_v2/klon.

| sjekk | resultat |
|---|---|
| `git ls-remote origin` | bare HEAD og refs/heads/main = e844c6e, ingen andre grener/tags |
| commits i hele historikken (`git rev-list --all`) | 3: 499ae0c ren start, 77436c6 synk 19:08, e844c6e synk 19:12 |
| stier med opplastet_ / real_votes / npx_votes (`git log --all --name-only`) | 0 |
| arrangørrader i alle blobs (`^20NN-NN-NNNNN,` / `SAY-ON-PAY VOTES,`) | 0 ekte (1 treff = regex-teksten i c1_historikk_rens.md) |
| nøkler/tokens i alle blobs (sk-ant, ghp_, AKIA, PRIVATE KEY, nbim_deploy) | 0 ekte (2 treff = stien til nøkkelen omtalt i to rapporter) |
| csv-filer i historikken (31) | alle egne prediksjoner (id, anbefaling, p_avvik), ingen forslagstekst eller fasit |
| README-kommando `sh KJOR.sh` uten casedata | stopper med FEIL DATAFIL, som README sier |
| `sh KJOR.sh` med de tre filene fra DATA.md | rc=0, 23 s. HOVEDTALL F1 MOT 0.512000, FRYSVAKT GRØNN, TALLVAKT GRØNN, 197 påstander 0 avvik |

Dom: GRØNN. Historikken på GitHub inneholder ingen arrangørdata og ingen hemmeligheter, og pakken
reproduserer hovedtallet 0,512 fra klonen.

## Merknader
- Rapporten #2816 sa "én commit"; nå er det tre fordi to synker er pushet etter rensen. Begge er skannet
  her (skanningen går over `--all`), ingen funn. Ikke et avvik.
- Gamle objekter via direkte sha: JA: 5deae34 (gammel main med opplastet_-rapporter) kan fortsatt hentes med `git fetch origin <full sha>`; d33a7aa kan ikke (not our ref).
  GitHub beholder ureferte objekter en stund. Repoen er privat, så det er bare synlig for den som har nøkkel.
  Vil guden være helt sikker før repoen gjøres offentlig: slett og opprett repoen på nytt, eller be GitHub Support
  om å tømme (står også i c1_historikk_rens.md).
- Klonen og loggen ligger i /tmp/c1_rens_dom_v2 (kan slettes).
