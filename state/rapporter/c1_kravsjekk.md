# Case 1: kravsjekk, hvert krav mot KRAVRESPONS.md (speider #2102, 05.11 ca. kl. 12.40)

Kilder: casen (C, `FinTech_Hackathon_Caser_H2026.pdf`), reglene (B, `Regler_og_bedommingskriterier.pdf`), startpakkens
`case1_stemmegivning/README.md` (R). Fasit for tallet: 0,476 [0,36; 0,59] (`c1_tall_likt.md`).

## Krav med feil tall (rettet i `arbeid/hack/levering/KRAVRESPONS.md`)
| krav | sto | står nå |
|---|---|---|
| 1 Målvariabel | «MOT = avvik fra styret» | MOT der styret sier FOR, AVSTÅ ikke med, 58 i test 2026 |
| 4 Baseline slått | 0 mot 0,4818 | 0 mot 0,476 [0,36; 0,59] |
| 5 Metrikk | ingen tall, viste til v2-logg | F1 0,476, P 0,441, R 0,517, TP 30 FP 38 FN 28, 58 av 1539 = 3,8 % MOT |
| 6 Fasit | 66 MOT, måler v2 | 58 MOT (66 avvik), måler v3 `--score mot` |
| 7 Ett kall | gir 0,4818 | kall + v3 gir 0,476 (fortsatt HULL H2/H3) |
| 11 Til menneske | 176 (11,2 %) | 176 av 1578 og 171 av 1539, begge nevnere |
| 19 Reproduserbart | 0,4818 målt to ganger | 0,476 (#2087, #2090) og 0,4818 (#2077, #2080) |
| 8 merknad | 0,482 / 0,386 uten merke | merket som avvik, ikke MOT-F1 |
| H2 | «ett kall for 0,4818» | 0,476 (#2094) |

## Krav som manglet i tabellen (lagt til som 29–32)
1. **FOR/MOT/AVSTÅ (C):** agenten gir aldri AVSTÅ. Bare erklært. Delvis.
2. **Sitere retningslinjen som avgjør (C):** vi siterer NBIMs egen tidligere begrunnelse + seksjon, ikke et oppslag i retningslinjene. Må sies rett ut. Delvis.
3. **Kategori-lekkasje (R):** **ingen fil med tall.** Ablasjonen uten type (0,504/0,511) er målt med egne målere, ikke v3 MOT. Må kjøres på nytt med `--score mot` (forslag: smed3 #2101 eller smed #2097).
4. **Juryspørsmål (B §6):** PDF har 3 spørsmål, teksten sier fem. JURYSVAR har gamle tall (#1975).

## Krav med tall som ikke kan etterprøves nå
- Krav 10: «74/74 MOT har sitat» er fra #2053, ikke den frosne kjøringen (68 predikerte MOT). Tell på nytt (#2012).
- H3: REF 0,481752 i kaldstart er avviks-tallet. Skal kald start sjekke hovedtallet, må REF være 0,476190 med v3 (#2099).

## Ikke rørt (bare tekst kan rettes, men eies av andre)
H1 1-sideren (0,383, N-PX), `levering/README.md`/`METODE.md`/`JURYSVAR.md` (0,474), demo (H5). Står i `c1_tall_likt.md` «Gjenstår».

Opptelling etter sjekken: 32 krav, 11 løst, 14 delvis, 6 HULL (7, 14, 18, 20, 22, 23*) + krav 31 uten tall. *H7 er tettet i README.
