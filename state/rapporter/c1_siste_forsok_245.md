# Case 1: siste forsøk på flere MOT-stemmer (#2248, ordre #245): ærlig nei

smed2, 05.11 kl. 13.55. Utgangspunkt er frossen #2044 miks h2. Koden er en kopi med flagget `--x` (`arbeid/oppgave_2248/train.py`).
Valgt KUN på val 2025: trent på år < 2025, historikk < 2025. C og grense er valgt på val, som i #2081. Test 2026 er **ikke kjørt**, fordi ingen variant nådde kravet.

Trekkene. Alle leser bare agenda og etiketter fra år før, aldri rationale eller nbim_vote:
- **lt**: glattet MOT-rate for land×sakstype, marked×sakstype og land×forslagsstiller, fra etiketter år < målåret. Sikter på USA-sakene.
- **ny**: første gang sakstypen, samme tekst eller selskapet står på selskapets agenda. Bruker bare agendadatoer, ingen etiketter. Sikter på enkeltstående styrevalg/revisor og nye aksjonærrettighets-saker.
- **mt**: møtestruktur: antall saker i møtet, antall av samme type, «eneste av sin type». Sikter på «eneste MOT i møtet».
- Feltet for revisorens funksjonstid eller uavhengighet finnes ikke i dataene. Det trekket kunne derfor ikke lages.

| Variant (val 2025, n=1909, 103 MOT) | F1 | P | R | PR-AUC | flagget |
|---|---|---|---|---|---|
| **base #2044 miks h2** | **0,5217** | 0,593 | 0,466 | 0,474 | 81 |
| + lt (land×type-rate) | 0,5140 | 0,605 | 0,447 | 0,465 | 76 |
| + ny (ny for selskapet) | 0,5217 | 0,593 | 0,466 | 0,474 | 81 |
| + mt (møtestruktur) | 0,5213 | 0,577 | 0,476 | 0,461 | 85 |
| + lt + ny + mt | 0,4804 | 0,566 | 0,418 | 0,463 | 76 |

Kravet var val F1 > base + 0,03 = 0,552. Ingen variant kom over. PR-AUC falt litt med alle trekkene. Pakka står uendret med frossen modell, 0,476 F1 MOT på test 2026.

Til juryen: bommene vi fant på test, altså USA, «eneste MOT i møtet» og nye aksjonærrettighets-saker, lar seg ikke fange med enkle trekk valgt ærlig på 2025. De blir stående som menneskelig kontroll i BEGRENSNINGER.md pkt. 7, ikke som modellendring.

Reproduser:
`cd arbeid/oppgave_2248 && uv run --project ../oppgave_2023 python train.py ../../state/opplastet/20261105_114241_real_votes.csv --variant miks --hist 2 [--x lt|ny|mt|lt,ny,mt]`
Loggene ligger i `arbeid/oppgave_2248/{base,lt,ny,mt,alle}.log`.
