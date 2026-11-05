# Case 1: dom over rettingen av interne pekere (#2458, dommer, 05.11 kl. 16.08) — GRØNN

Dømmer #2454 (smed3), commit 912bc35. Før-versjon: jury-zipen fra kl. 15.45 (`/tmp/jurypakke_c1.zip`, pakket før rettingen). Nå-versjon: `arbeid/hack/c1/leveranse/` (lik frys-fasiten kl. 16.00, sha256 a9ffc9e6… og a3c4c6f8…).

## Sjekket
| Krav | Funn | |
|---|---|---|
| ERLIG_EVALUERING linje 48 peker ikke på hist_regel.py | «gammelt skript `hist_regel.py`» → «gammelt internt skript, ikke i pakka» | OK |
| ERLIG_EVALUERING linje 70 | «ligger i `hist_regel.py`» → «er beskrevet i `kilder/c1_enkle_regler_og_hist1.md` (selve skriptet er et gammelt internt skript, ikke i pakka)». Måla fila finnes i pakka, i zipen og i frys-fasiten | OK |
| `hist_regel.py` i fila | 2 treff før, 0 nå | OK |
| kilder/LESMEG har forklaringslinja | ny linje 3: filnavn uten sti viser til interne arbeidsmapper, tallene står ferdig målt i teksten | OK |
| Tallvakta, de to filene | 15 påstander stemmer, 0 avviker | OK |
| Tallvakta, hele pakka | 18 filer, 168 påstander, 0 avviker (samme nullpunkt som smed3 oppga) | OK |
| Ingen tall endret | diff før/nå: bare linje 48 og 70 i ERLIG, bare to nye linjer i LESMEG. Alle tokens med siffer er like, unntatt to nye filnavn (`hist1.md`, `gvg2024.txt`) | OK |

Git: filene var ikke sporet før (arbeid/ er gitignorert), så `git diff` mot forrige commit viser hele fila som ny. Derfor er diffen gjort mot zipen fra kl. 15.45, som er siste pakke før endringen.

## Dom
GRØNN. Ren tekstretting, ingen måletall rørt, tallvakta 0 avvik. Zipen fra 15.45 inneholder den gamle teksten; neste `pakk_jury.sh` tar den nye med (frys-fasiten kl. 16 er allerede regnet på den rettede teksten).
