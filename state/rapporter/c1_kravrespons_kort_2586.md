# Case 1 #2586: kravresponsen kortet ned til malen (R §3)

- `arbeid/hack/c1/leveranse/kravrespons.md`: 4/5/5 setninger under de tre overskriftene, 297 ord (før: 4/7/9 og 608 ord). Commit acdd689.
- Detaljer ut: motstandstesten (16 instrukser, 6 av 16 nye tittel-instrukser slipper forbi) og V2 (0,516 etter frys) sto allerede i JURY.md (pkt. 11 og «Hvorfor vi ikke jaget testtallet"). Praksis mot policy (81 av 82, 565 av 569) er flyttet til ny seksjon «Følger NBIM egne retningslinjer?» i JURY.md.
- Kravresponsen peker til JURY.md for begge.
- Ingen nye tall. Tallvakt: 0 avvik (171 påstander). Én falsk alarm ble rettet ved å omformulere: «F1 ... 96,2 % accuracy» i samme setning.
- frys_fasit_1600.sha256: bare sha-linjene for de to filene er oppdatert. `frys_diff.sh --kilde` viser 6 andre avvik (SVAKHETER, JURY_SPORSMAL, JURY_README, README, ny SLIDE.md), fra oppgavene som pågår (#2587, #2588, #2580). Fasiten må regenereres når de er ferdige.
- Obs for #2580 (smed3, byttedommen inn i kravresponsen): hold deg innenfor 5 setninger og 300 ord, f.eks. ved å bytte ut setningen om 0,476 under målet i «Hva vi ville trengt videre».
