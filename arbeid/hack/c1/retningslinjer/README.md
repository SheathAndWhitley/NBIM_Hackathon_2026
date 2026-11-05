# NBIMs retningslinjer, nummerert og siterbar

Agenten siterer ordrett fra disse filene. `arbeid/hack/levering/retningslinje_oppslag.py` leser `punkter.jsonl`
(felt: `id`, `pilar`, `avsnitt`, `tekst`) og bruker bare NBIM-punktene.

| Fil | Kilde | Punkter | Id-format |
|---|---|---|---|
| `nbim_global_voting_guidelines.md` | https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ | 140 | `NBIM prinsipp.delpunkt.ledd` |
| `nbim_posisjonsnotater.md` | https://www.nbim.no/en/responsible-investment/position-papers/ (12 notater) | 256 | `NBIM-PP<n> ledd` |

Filene ble laget med `arbeid/speider/c1ret/lag_retningslinjer.py` fra sidene over. De rå nedlastingene ligger ikke i repoet.

`punkter.jsonl` inneholder også 241 punkter fra Vanguards amerikanske stemmeretningslinjer (`VG25`, `VG26`), fra et
tidlig spor med SEC N-PX-data. Agenten bruker dem ikke. Fila står uendret fordi den er frosset (sha256 i `FROSNE_SHA256.txt`).
