# Case 1: grunnlinja «følg styret» (F1 0,357) er en stråmann – korrigert er F1 0,947

Dommer, #1954, 05.11 kl. 11:10.

**Funn:** I Vanguard-filene (N-PX) står `managementRecommendation` = FOR på nesten alle
aksjonærforslag (kilde SECURITY HOLDER), også der selskapet går imot. Eksempel fra rådata:
Brookdale 2025-07-11, «Ortelius Nominees OPPOSED by the Company», rec=FOR, Vanguard stemte WITHHOLD.
Hele votes_v0: SECURITY HOLDER har (rec FOR, stemme AGAINST) 808 ganger og (rec AGAINST, stemme FOR) 212 ganger.
Feltet er altså snudd eller meningsløst for aksjonærforslag. Kolonnen `ledelsen` er derfor ikke styrets
reelle anbefaling der.

**Konsekvens:** «følg styret» slik måleren regner den nå (MOT bare når rec=AGAINST) bommer på alle
47 MOT på aksjonærforslag i holdout. Med styrets reelle syn (styret går imot aksjonærforslag):

| Grunnlinje (holdout 1544, 65 MOT) | MOT P | MOT R | F1 |
|---|---|---|---|
| følg styret, rå `ledelsen` (nå på tavla) | | | 0,357 |
| følg styret korrigert: MOT hvis kilde=SECURITY HOLDER eller rec=AGAINST | 0,939 | 0,954 | **0,947** |
| referansemodell TF-IDF+LR (motstandstest.py) | 0,922 | 0,908 | 0,915 |

Kommando: se `arbeid/hack/levering/motstandstest.py` og
`python3 -I arbeid/hack/c1/maaler.py <pred> --fasit arbeid/hack/c1/data/fasit.csv`.

**Hva det betyr:** Å slå 0,357 beviser ingenting. NBIM-juryen vet at Vanguard stemmer med styret
mot aksjonærforslag og vil se dette straks. Den ærlige grunnlinja er 0,947. Det reelle målet blir
da enten (a) avvik fra styret (53 av 1543 i holdout, der korrigert «følg styret» fanger 0 per
definisjon), eller (b) å forklare og sitere, ikke å slå F1 på MOT. Gjelder dette ikke den
endelige forvalteren (NBIM, CIK 1374170), må det sjekkes på nytt på de dataene.
