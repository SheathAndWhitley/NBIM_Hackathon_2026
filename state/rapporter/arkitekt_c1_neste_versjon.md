# Arkitekt #2280: neste versjon av Case 1-agenten, tre tiltak regnet fra feilene

Fil: `arbeid/hack/c1/leveranse/NESTE_VERSJON.md` (speider lenker inn i JURY.md, #1975). Ingenting bygd eller trent.

| tiltak | feilgruppe | maks rettet (test / val) | øvre F1 test / val | data |
|---|---|---|---:|---|
| 1 historikk forfaller på styrevalg | falske MOT, styrevalg | 26 FP / 22 FP | 0,600 / 0,596 | rationale_section fra tidligere år (finnes) |
| 2 OTHER_MGMT + revisor til menneske med GVG 4.3/5.1-sjekkliste | savnede MOT, grunn ikke i teksten | 9 FN / 10 FN | 0,578 / 0,601 | revisorens år og honorar (finnes ikke i arrangørens data) |
| 3 India som egen gruppe | savnede MOT, India begge år | 3 FN + 6 FP / 14 FN + 1 FP | 0,537 / 0,634 | les de 14 val-sakene først |

Dagens tall: 0,476 test / 0,520 val. Hvert tall i fila har kilde (fil:linje) i c1_feil_per_gruppe.md, feil_val2025.md, c1_feil_stabilitet.md og c1_feilanalyse.md; øvre F1 er 2TP/(2TP+FP+FN) regnet fra dem.
Lagt bort: «styrevalg i USA → menneske» (test +0,028, val −0,032, c1_feil_stabilitet.md:23).
Trukket vinkel: «finn den nedre grensen først» → hvert tiltak har tak før noen bygger; samlet tak 0,792 på test. Vinkelen «lavrang-tilnærming» er forkastet uten tall: vi har ikke matriser å komprimere her.
Anbefaling: bygg tiltak 1 først etter hackathonet (data finnes, stabilt begge år); ingenting endres før frysen kl. 16.
