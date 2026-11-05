# Case 1: GitHub-historikken renset for arrangørens rader (#2816, beslutning #2810)

Ferdig 19:08. Remote `main` er nå én commit: **499ae0c** «Case 1 stemmeagent: ren startcommit uten arrangørdata».

## Hva ble gjort
1. Lokal backup-gren `backup_for_rens_2810` = gammel main d33a7aa (11 commits). Pushes aldri.
2. Synken (no.landsby.githubsynk) pauset 19:05 (ingen synk kjørte; siste var 19:04:03). Ført i maskinendringer.md.
3. Funn underveis: HEAD hadde fortsatt to opplastet_-rapporter, `opplastet_..._startpakke.md` og
   `opplastet_..._NBIM_Hackathon_2026-main_1_.md`. Den siste viste rader fra arrangørens csv-er
   (f.eks. `20NN-NN-NNNNN,<selskap>,...`). Rettet i kilden: `arbeid/verktoy/c1_github_alt.py`
   MONSTER_UT har nå `opplastet_*` (alle opplastings-rapporter ute), så synken ikke legger dem tilbake.
   Lista 1009 -> ingen opplastet_. Kjørte synken én gang for hånd (uten push): GRØNN.
4. `git checkout --orphan ren`, commit, `git branch -M ren main`, reflog utløpt + gc.
5. Skanning over `git rev-list main` (backup utelatt): c1_hemmelig_skann.sh rc=0 uten funn; 0 nøkler/tokens;
   0 opplastet_-stier; 0 radtreff på `20NN-NN-NNNNN,` / `SAY-ON-PAY VOTES,`.
6. `git push --force-with-lease=main:5deae34 origin main`: `+ 5deae34...499ae0c main (forced update)`. Eneste push.
7. Synken slått på 19:08; første synk 77436c6 lagt lokalt oppå 499ae0c (synken pusher ikke, PUSH ikke satt).

## Akseptkrav
- `git ls-remote origin`: HEAD og refs/heads/main = 499ae0c6dd42…, ingen andre grener. OK
- Fersk klone (deploy-nøkkel): 1 commit i hele historikken, 0 opplastet_/real_votes/npx_votes-stier, 0 radtreff. OK
- README-kommando `sh KJOR.sh` i fersk klone: uten casedata stopper den med `FEIL DATAFIL` som README sier;
  med de tre filene fra DATA.md lagt på plass: rc=0, `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000`,
  `TALLVAKT GRØNN`, 197 påstander 0 avvik. OK

## Merk
- Gamle commits (5deae34 m.fl.) kan fortsatt nås på GitHub via direkte sha en stund (GitHub sletter ikke
  ureferte objekter straks). Ingen fork/PR finnes så vidt vi vet; repoen var privat. Vil man være helt sikker,
  kan guden be GitHub Support om cache-tømming, eller slette og lage repoen på nytt før den gjøres offentlig.
- #2728 (synk med tekststopp-versjonen): den manuelle synken 19:07 og 19:08-synken ligger lokalt; neste push må gjøres av den som har push-fullmakt.
