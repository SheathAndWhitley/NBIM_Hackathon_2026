# Case 1: tallvakta er grønn igjen (#2388, smed4, 05.11 ca. 15.16)

## Resultat
`sh arbeid/hack/levering/fremmed.sh /tmp/c1_tv2388.vKjj` i tom mappe, utgang 0, 1 min 34 s.
- `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190`
- `18 filer, 165 påstander om hovedtallet stemmer, 0 avviker` → **TALLVAKT GRØNN**
- Logg: `/tmp/c1_tv2388_1.log` (rød kjøring til sammenligning: `/tmp/c1_reserve_2372.log`)

## De tre rettelsene (før = kopien /tmp/c1_reserve_2372 fra 15.05, etter = landsbymappa nå)
Rettelsene var allerede gjort i landsbymappa da jeg startet: filene ble endret 15:06:23 (BEGRENSNINGER, ERLIG_EVALUERING)
og 15:07:23 (kravrespons), altså rett etter den røde kjøringa. Jeg endret bare dobbeltordet nevnt under. Ingen frosne filer eller målere er rørt.
Ikke committet ennå i git (filene står som endret i arbeidstreet).

| Fil:linje | Vakta sa | Før | Etter | Kilde for tallet |
|---|---|---|---|---|
| leveranse/BEGRENSNINGER.md:33 | «til menneske 5 av 1578, måleren sier 188» | «… og 5 av 1578 i test 2026, så agenten …» | «… og 5 i test 2026 (av 1578 saker), så agenten …» | 5 AVSTÅ i fasit: `kilder/oppgave_2234_baseline_real_test.txt:6`; 1578 saker: kjøringas `inn:`-linje. Tallet gjaldt AVSTÅ, ikke til menneske. |
| leveranse/ERLIG_EVALUERING.md:68 | «antall MOT 569, måleren sier 58» | «fra 2020 viser 565 av 569 MOT-stemmer mot styret (99,3 %) …» | «fra 2020 viser 565 av de 569 stemmene mot styret mot styret (99,3 %) …» | `kilder/c1_praksis_dom.md:15` (dommerkontrollert): MOT der styret sa FOR, år ≥ 2020: 569, 565 med GVG |
| leveranse/kravrespons.md:10 | «antall MOT 569, måleren sier 58» | «fra 2020 viser 565 av 569 MOT-stemmer en GVG-begrunnelse» | «fra 2020 viser 565 av de 569 stemmene mot styret en GVG-begrunnelse» | samme som over |

## Vurdering, ærlig
- Ingen av de tre var feil tall. Vakta tolket 569 (alle år fra 2020) som antall MOT i test (58), og «5 av 1578» (AVSTÅ) som antall til menneske (188).
  Rettelsen er en omformulering slik at vakta ikke leser tallene som hovedtall. Hvert tall har fortsatt en kilde i `kilder/`.
- Rettet av meg kl. ca. 15.18: dobbelt «mot styret mot styret» i ERLIG_EVALUERING.md:68 → «565 av de 569 stemmene mot styret (99,3 %)».
  Ny kald kjøring etterpå: `fremmed.sh /tmp/c1_tv2388b.QcGB`, utgang 0, HOVEDTALL 0.476190, 166 påstander, 0 avvik, TALLVAKT GRØNN.
  Logg: `/tmp/c1_tv2388_2.log`. Dette er den gjeldende grønne kjøringa.
- Reserven (#2372) har teksten fra 14:54 og trenger ikke endres.
