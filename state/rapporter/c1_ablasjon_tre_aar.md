# Case 1 (#2581): ablasjon av frossen modell over tre testår (F1 MOT)

Forklaring til ERLIG_EVALUERING, ikke et byttforslag. Frossen = miks h2 (#2044), kjørt med
benken fra #2567: val = året før (C og grense velges der), test 2024/2025/2026, offisiell
måler (`--score mot`). Kopien gir byte-lik prediksjonsfil som frossen alle tre år (cmp LIK).
Én trekkgruppe tas ut av gangen; Δ og 95 % KI er parret klyngebootstrap mot frossen.

| ut av modellen | 2024 (Δ; KI) | 2025 (Δ; KI) | 2026 (Δ; KI) | snitt | Δ snitt |
|---|---|---|---|---|---|
| ingenting (frossen) | 0.4545 (+0.0000; KI +0.000; +0.000) | 0.5143 (+0.0000; KI +0.000; +0.000) | 0.4762 (+0.0000; KI +0.000; +0.000) | 0.4817 | +0.0000 |
| kategorier (sakstype, forslagsstiller, styrets anbefaling, land, marked, punktnr på dagsorden; i begge halvdeler) | 0.4462 (-0.0083; KI -0.109; +0.077) | 0.4490 (-0.0653; KI -0.126; -0.014) | 0.4667 (-0.0095; KI -0.060; +0.043) | 0.4540 | -0.0277 |
| forslagstekst (tf-idf, bare LR-delen) | 0.4311 (-0.0234; KI -0.110; +0.062) | 0.4608 (-0.0535; KI -0.106; -0.008) | 0.4821 (+0.0059; KI -0.045; +0.052) | 0.4580 | -0.0237 |
| all MOT-historikk | 0.3279 (-0.1266; KI -0.272; +0.027) | 0.3072 (-0.2071; KI -0.315; -0.092) | 0.2756 (-0.2006; KI -0.313; -0.083) | 0.3036 | -0.1781 |
| historikk: samme selskap | 0.4684 (+0.0139; KI -0.091; +0.120) | 0.4804 (-0.0339; KI -0.092; +0.022) | 0.3926 (-0.0836; KI -0.160; -0.018) | 0.4471 | -0.0345 |
| historikk: samme selskap + samme tekst | 0.4933 (+0.0388; KI -0.032; +0.109) | 0.5202 (+0.0059; KI -0.029; +0.044) | 0.4444 (-0.0318; KI -0.064; -0.010) | 0.4860 | +0.0043 |
| historikk: samme tekst (alle selskap) | 0.4394 (-0.0151; KI -0.067; +0.043) | 0.4575 (-0.0568; KI -0.128; +0.007) | 0.4627 (-0.0135; KI -0.046; +0.022) | 0.4532 | -0.0285 |
| sakstype (proposal_type) | 0.4697 (+0.0152; KI -0.078; +0.089) | 0.4886 (-0.0257; KI -0.054; -0.002) | 0.5000 (+0.0238; KI -0.012; +0.062) | 0.4861 | +0.0044 |
| LightGBM-halvdelen (bare LR igjen) | 0.4485 (-0.0060; KI -0.104; +0.097) | 0.4094 (-0.1049; KI -0.183; -0.028) | 0.4545 (-0.0217; KI -0.094; +0.057) | 0.4375 | -0.0442 |
| LR-halvdelen (bare LightGBM igjen) | 0.4817 (+0.0272; KI -0.108; +0.155) | 0.4512 (-0.0631; KI -0.121; -0.008) | 0.4167 (-0.0595; KI -0.107; -0.005) | 0.4499 | -0.0318 |

## Hva det betyr
- **Historikken bærer modellen.** Uten MOT-historikk faller F1 fra 0,48 til 0,30 i snitt, og
  presisjonen til ~0,2 (160 falske MOT per år). Agenten er i hovedsak «NBIM stemte mot dette før».
  Det er ærlig å si til juryen: modellen ser mønstre i NBIMs egne tidligere stemmer, ikke forstår
  saken fra bunnen.
- Viktigst av historikk-delene: samme selskap (−0,035, tydeligst 2026) og samme tekst (−0,029).
- Alle andre grupper bidrar litt (−0,02 til −0,03 i snitt), men bare 2025 har KI helt under 0
  for kategorier og tekst. Enkeltår svinger ±0,05 uten at noe er endret i modellen.
- To grupper kan tas ut uten tap i snitt: sakstype (+0,004) og selskap+tekst-historikk (+0,004).
  Begge er langt under byttregelen (+0,02) og har år med −0,03; de er støy, ikke funn. Ingen bytte.
- Miksen er bedre enn hver halvdel (LR alene −0,044, LightGBM alene −0,032), og de to halvdelene
  vinner i ulike år. Det er grunnen til at vi miksa.

Filer: arbeid/oppgave_2581/ (abl_rull.py med `--uten`, kjor.sh, maal.sh, benk.txt). Gjenskap:
`cd arbeid/oppgave_2581 && bash kjor.sh && bash maal.sh > benk.txt` (ca. 2 min).
