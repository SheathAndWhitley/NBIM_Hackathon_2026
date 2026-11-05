# Hack #2023 (smed2, innsikt): de nye arrangørfilene fra 11:42 (ordre #227/#228)

Guden lastet opp en rettet NPX-fil (52 906 rader, test `split_year` 2026) og NBIMs egne stemmer fra API
(`real_votes.csv`, 13 757 rader, 2019–2026). Etiketten er `against_board` (stemme ≠ styrets anbefaling, AVSTÅ teller som avvik).
Måler: `arbeid/oppgave_2023/maaler_ny.py` (F1 på MOT, test 2026, `injection_flag==0`). Den er foreløpig; dommeren må sette den (#2035).

## Funn 1: NPX-tallet er oppblåst
| NPX test 2026 (634 MOT) | n | MOT | type+kilde+styre | logreg | +tfidf (t1) |
|---|---|---|---|---|---|
| alle | 16 455 | 634 | 0,660 | 0,808 | **0,903** |
| aksjonærforslag | 302 | 302 | 0,983 | 1,000 | 1,000 |
| styret anbefaler MOT (fond avstår) | 861 | 332 | 0,296 | 0,726 | 0,859 |
| **ekte uenighet (ledelsens forslag, styret FOR)** | 15 333 | **41** | 0,250 | 0,255 | **0,610** |

- Regelen «aksjonærforslag = MOT» gir alene F1 0,645, og presisjonen er 1,00.
- 94 % av MOT i NPX er enten aksjonærforslag eller saker der styret selv anbefaler MOT og fondet avstår
  (prosedyrepunkter som «Transact Other Business» og brasiliansk kumulativ stemmegivning). Juryen bør få se tallet for **ekte uenighet** separat.

## Funn 2: NBIMs ekte data er det vanskelige problemet
- 58 av 66 MOT i 2026 er ekte uenighet. Følg styret gir F1 0, og grådig per forslagstype gir 0,237.
- Logistisk regresjon (C og terskel valgt på 2025, trent på data før 2025, så på alt før 2026, test 2026 én gang):

| trinn (én endring om gangen) | val 2025 | test 2026 F1 | 95 % bootstrap |
|---|---|---|---|
| t0: type/kilde/styre/land/marked | 0,212 | 0,356 | |
| t1: + tfidf på forslagstekst | 0,480 | 0,458 | 0,37–0,55 |
| t2: + selskapets tidligere MOT-rate (bare eldre møter) | **0,500** | 0,481 | 0,38–0,58 |
| t4: t2 + samme tekst i samme selskap stemt MOT før | 0,488 | 0,497 | 0,40–0,59 |
| t4e: t4 + NPX før 2025 som ekstra trening | 0,468 | 0,529 | 0,42–0,63 |

- Ærlig valg på val: **t2**. Fra t2 til t4e er det +0,05 på test, men val går motsatt vei og intervallet for differansen er −0,01 til +0,10. Det er støy med 66 positive.
- Feil per type (t4): styrevalg 18/33 treff og 28 falske. Revisor 5/7. «Other business» 6/6. Vedtektsendringer gir 1/3 treff og 8 falske.

## Funn 3: lekkasje i real_votes
- `rationale_text` er utfylt i 627 rader. 618 av dem er MOT (98,6 %), og feltet dekker 618 av 744 MOT.
  `position_paper` er det samme. **Ingen av feltene må brukes som feature.** De kan bare brukes som sitatkilde etter at avgjørelsen er tatt.
- 141 rader med `injection_flag=1` i NPX (motstandstest-rader, 57 uten etikett) er holdt utenfor måleren.

## Neste steg
1. Dommeren setter måler for de nye filene (#2035) og bestemmer hvilken fil som er hovedtallet. Mitt forslag: real_votes for 2026, med NPX rapportert per delmengde.
2. Agenten (#44) bør kjøres på real_votes. Regelen for aksjonærforslag og styret-MOT-saker kan gi en enkel og forklarbar forhåndsregel.
3. Filer: `arbeid/hack/ut_innsikt/` (modell.py, maaler_ny.py, grunnlinjer.py, real_beste.csv = t2, npx_beste.csv = t1).
