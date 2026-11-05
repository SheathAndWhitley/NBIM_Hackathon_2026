# Case 1: siste kalde kjøring før modellfrys (#2243)

Kjørt 05.11 kl. 13:49 på git 9012a58, etter rydding (#2236), ny sha (#2238) og injeksjonsvakta (#2237, lukket 13:48).

| Sjekk | Resultat |
|---|---|
| kaldstart.sh (tom kopi, `uv sync --frozen`, 34 s) | GRØNN, utgang 0 |
| fremmed.sh (/tmp/fremmed_2243, 29 s) | OK + TALLVAKT GRØNN, utgang 0. 14 filer og 153 påstander om hovedtallet, 0 avvik |
| F1 MOT mot styret (måler v3 `--score mot`) | **0,476190** (TP 30, FP 38, FN 28, P 0,441, R 0,517, 58 MOT i fasit), samme med og uten ruting |
| pred_maaler.csv sha256 | b113b545dd86… i begge kjøringene, lik `b113b545…3653` i README.md |
| måler v3 sha256 | 418a937e57, lik papirene |
| Til menneske | 188 av 1578 (11,9 %), 1 av dem på grunn av injeksjon (ny vakt) |

Runde 1 (13:42, før #2237 var ferdig) ga samme F1 og samme pred-sha. Injeksjonsvakta endrer bare rutingen, ikke prediksjonene.
Avvik: ingen. Frysvakta sier «ikke frosset ennå», som ventet før kl. 16.
Kommandoer: `BEHOLD=1 bash arbeid/hack/c1/kaldstart.sh; sh arbeid/hack/levering/fremmed.sh /tmp/fremmed_2243`
