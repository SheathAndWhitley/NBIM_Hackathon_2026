# Case 1: hull i kravresponsen mot bedømmingskriteriene (speider #2083, 05.11 kl. 12.25)

Full tabell: `arbeid/hack/levering/KRAVRESPONS.md` (28 krav: 11 løst, 11 delvis, 6 står på et hull).
Hovedtall som skal stå overalt: F1 MOT 0,4818 (P 0,465, R 0,500, 66 MOT, test 2026 real_votes), valgt på val 2025 (0,522),
måler v2 (`c1/maaler_offisiell_v2.py`), KI 0,37–0,58. Følg styret F1 0.

| Hull | Hva | Kriterium som taper | Eier |
|---|---|---|---|
| H1 | 1-sideren `c1/leveranse/kravrespons.md` er N-PX-regelen 0,383, ikke agenten | viktigste leveranse | speider (#1975) |
| H2 | Ett kall fra kald kopi gir ikke 0,4818: `kjor.sh` gir 0,383, `fremmed.sh`/README lover 0,474 og kopierer ikke real-delene | etterprøvbarhet 30 % | arkitekt |
| H3 | `c1/kaldstart.sh` steg 4 måler mot N-PX-fasit, REF 0,474. Kald start kl. 13 blir feil | etterprøvbarhet 30 % | arkitekt/dommer (#1952) |
| H4 | Motstandstest ikke kjørt på frosset modell #2044. På logreg #2046 snudde 82/174 med en frase vernet ikke kjente | robusthet 20 % | dommer2 etter 16.00 |
| H5 | Demoen kjører stubben og viser N-PX som fasit | «trekker ned», beslutningsstøtte 20 % | smed |
| H6 | README/BEGRENSNINGER har N-PX-KI 0,31–0,45 og «kjor.sh er deterministisk» | etterprøvbarhet | smed3 (#2086) → speider |
| H7 | Kilde for real_votes/npx_votes (arrangøren) mangler i README | felles regler §5 | tettet 12.30 (README «Datakilder») |
| H8 | AVSTÅ foreslås aldri, nå erklært | begrensninger | tettet 12.30 (BEGRENSNINGER pkt. 9) |
| H9 | Rutede saker viser `anbefaling` som om det var en stemme | beslutningsstøtte | smed2 (#2079) |

Mindre: måleren skriver «konfidens < 0,6» og «streng MOT F1 0,0000» i kjøreloggen. 176 rutet av 1578 inn mot 171 av 1539 vurderte. Skriv begge nevnerne.

Rekkefølge: H3 før 13.00, så H2. H4 og H1 etter frys 16.00. H5 før demo-prøven.

Merk: URL-en https://vd.nbim.no/ i README er skrevet fra hukommelsen og ikke åpnet. Dommeren bør sjekke den ved pakking.
