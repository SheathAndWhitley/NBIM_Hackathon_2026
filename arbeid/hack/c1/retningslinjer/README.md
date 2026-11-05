# Retningslinjer for Case 1, nummerert og siterbar (speider #1948)

Lages på nytt med `python3 -I arbeid/speider/c1ret/lag_retningslinjer.py` (rå nedlastinger i `arbeid/speider/c1ret_raa/`).
Alle punktene står i `punkter.jsonl` (felt: `id`, `pilar`, `avsnitt`, `tekst`), klare for BM25 eller embedding.

| Fil | Kilde | Punkter | Id-format |
|---|---|---|---|
| `vanguard_us_2026.md` | https://corporate.vanguard.com/content/dam/corp/about-our-funds/pdf/vpm/vpm-proxy-voting-policy-us.pdf (VCM-versjonen er ordrett lik: .../vcm/vcm-proxy-voting-policy-us.pdf) | 132 | `VG26 pilar.avsnitt.ledd` |
| `vanguard_us_2025.md` | Vanguard-advised funds, effektiv feb. 2025 (tekst fra Vanguard SAI på EDGAR, smed3s kopi) | 109 | `VG25 ...` |
| `nbim_global_voting_guidelines.md` | https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ | 140 | `NBIM prinsipp.delpunkt.ledd` |
| `nbim_posisjonsnotater.md` | https://www.nbim.no/en/responsible-investment/position-papers/ (12 notater) | 256 | `NBIM-PP<n> ledd` |

**Hvilken Vanguard-versjon:** møter før 12.01.2026 → VG25, fra 12.01.2026 → VG26 (Vanguard delte stewardship i VPM/VCM fra 2026-sesongen; teksten er nesten lik, avsnittsnummer kan avvike, sjekk 3.x).
BlackRock er ikke tatt med: blackrock.com gir feilside til skript, og datasettet vårt er Vanguard (BlackRocks CIK 1364742 er en NOTICE uten stemmer).

## Kart: forslagstype → punkt (VG26)
| Forslagstype i N-PX | Avgjørende punkt |
|---|---|
| Direktørvalg, uavhengighet / komité | 1.1.x (flertall uavhengig, nøkkelkomiteer) |
| Direktørvalg, for mange verv (overboarded) | 1.4.1 (CEO > 2 styrer), 1.4.2 (> 4 styrer) |
| Direktørvalg, oppmøte < 75 % | 1.5.1 |
| Direktørvalg, styret ignorerte flertallsvedtak / svikt i tilsyn | 1.6.1 |
| Direktørvalg, styresammensetning (nom.-komitéleder) | 1.3.3 |
| Aksjonærforslag: skille CEO/styreleder | 1.2.2 (normalt MOT) |
| Say on Pay | 3.0.x (3.0.9-3.0.13 = sterke bekymringer, 3.0.14-3.0.19 = varsler) |
| Say on Pay-frekvens | 3.1.1 (årlig) |
| Aksjeopsjonsplaner | 3.3.x |
| Revisor | 2.5.1 |
| Miljø/sosiale aksjonærforslag | 2.4.1-2.4.7 (støtte bare ved mangelfull, vesentlig, ikke-preskriptiv) |
| Aksjonærrettigheter (staggered board, supermajoritet, spesialmøte, proxy access) | 4.1-4.6 |

NBIM-ekvivalenter: direktørvalg 1.x/2.x/3.1, lønn 3.3 (+ NBIM-PP3 CEO remuneration), revisor 5.1, kapital 6.x, anti-takeover 6.2.
