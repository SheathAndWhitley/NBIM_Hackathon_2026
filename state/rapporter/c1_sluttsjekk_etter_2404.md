# Case 1: hel sluttsjekk.sh etter tekstavtrykk-steget (#2407)

Kjørt 2026-11-05 15:29, git 9bf3b25, kald kopi /tmp/c1_sluttsjekk_smed4 (slettet først).

## Resultat
- **Ekte skript (uendret):** RØD i steg 1 etter 0 s: `FRYSVAKT: ikke frosset ennå ... --krev: STOPP`.
  Det er riktig oppførsel før frysen kl. 16 (state/c1_frys.json finnes ikke).
- **Kopi uten `--krev` i steg 1** (/tmp/smed4_sluttsjekk_utenkrev.sh, eneste endring + fast LAND-sti):
  `SLUTTSJEKK GRØNN ... HOVEDTALL F1 MOT 0.476190 = kv hack_levert = zipen` på **148 s** (krav: under 5 min).

## Tid per steg (fra tidsstempel på hver linje)
| Steg | Tid | Status |
|---|---|---|
| 1 frysvakt | 0 s | info: ikke frosset ennå (rød med --krev) |
| 2 kaldstart fremmed.sh | 29 s | grønn, TALLVAKT GRØNN, 169 påstander, 0 avvik |
| 3 tallvakt | <1 s | grønn, F1 0.4762 P 0.4412 R 0.5172, TP 30 FP 38 FN 28 |
| 3b tallsjekk | 1 s | 2456 tall i 18 filer funnet |
| 4 hovedtall mot kv | <1 s | 0.476190 = 0.476190 |
| 5 jury-zip | 57 s | 1.0M, 99 filer; sha256 er dagens filer (ikke frosset) |
| 6 ziptest | 61 s | ZIPTEST GRØNN, TP/FP/FN/TN stemmer, prediksjonsfil-sha lik frossen fil |
| 7 tekstavtrykk | 0 s | info: «ikke tatt ennå (tas kl. 16.03)», ikke rødt |
| **Totalt** | **148 s** | |

## Merknader
- Steg 7 ble bare prøvd i grenen «avtrykk ikke tatt». Sammenligningsgrenen kan først kjøres etter 16.03
  (den ble testet i speilkopi i #2404).
- Steg 1 med `--krev` må kjøres på nytt etter 16:00. Da skal ekte skript gi GRØNN uten endringer.
- Steg 5 skriver over standardzipen /tmp/jurypakke_c1.zip. Den er nå laget fra dagens filer før frysen og må lages på nytt etter frysen.
- Merk fra steg 5: 8 tekstfiler nevner ~, men kjørestien leser dem ikke (kjent, bare info).

Logger: /tmp/c1_sluttsjekk_logg.0YP8, utskrift med tidsstempel: /tmp/smed4_2407b.txt
