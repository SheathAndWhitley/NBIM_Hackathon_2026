# Case 1: dårlig inndata mot tekststopp-zipen etter 19:00 (#2799, smed3) – VENTER PÅ ZIPEN

Status 18:58: #2549 (tekststopp-zip) starter 19:00. Nyeste grønne zip er fortsatt `jurypakke_c1_1827_0e3b14b.zip`
(18:26, sha256 98257a6e…), den #2783 alt testet 6 av 6 godkjent. Vakt står på `state/levering/c1_gronn/`
(ny zip eller endret SISTE_GRONNE-peker).

Ryddet: egne tmp-kopier `/tmp/rob2783` og `/tmp/rob2774_prov` slettet (570 MB). `/tmp/rob2739` er dommer2s, urørt.
`/tmp/rob2755` (285 MB) står: eier ikke bekreftet i rapportene.

Referanse (#2783, zip 0e3b14b): tom/bare_overskrift -> 0 rader, nan; uten_proposal_text -> 1578 rader alle til
menneske, 0,000; uten_mgmt_rec -> 0,512; latin1 -> 0,512; binaer -> 400 rader, nan. Exit 0 og ingen traceback i alle.

## Mot tekststopp-zipen
Ikke kjørt ennå (zipen finnes ikke). Kommando når den kommer:
`sh arbeid/oppgave_2774/robust_zip.sh state/levering/c1_gronn/SISTE_GRONNE.zip /tmp/rob2799` (ca. 1 min),
deretter `rm -rf /tmp/rob2799`.
