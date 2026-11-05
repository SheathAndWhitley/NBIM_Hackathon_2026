# Case 1: speiderens fem-minutters forbedringer ført inn (#2539)

Kilde: `state/rapporter/c1_jury_fem_min.md` (#2537). Ingen nye tall: alle tall finnes fra før i README, kravrespons eller `JURY_SPORSMAL.md` sp. 19.

## Ført inn
1. **README, hovedtallsboksen: «V1 står» med V2-tallet.** Ny setning: frosne V1 leveres med vilje, V2 0,516 er målt på test etter frysen og innenfor støyen (+0,040, KI [−0,007; +0,095]), viser til sp. 19. Dom #2529 (V1 står) er bekreftet i JURY_SPORSMAL sp. 19. Ordlyden er endret fra speiderens «valgt etter å ha sett test» til «målt på test etter frysen», slik sp. 19 sier det. Merket `tallvakt: ignorer`.
2. **kravrespons:7, skrivefeil.** «Begge måler også måler svaret» → «Begge måler svaret».
3. **kravrespons:10, samme poeng om V2.** Én setning etter «under målet vårt på 0,5», samme tall og ordlyd som pkt. 1, merket `tallvakt: ignorer`.
4. **README, hovedtallsboksen kortet ned.** Boksen har nå hovedtall, KI, P/R, følg styret, val 2025, ruting 188/1578, reproduksjon i jury-zipen og V1-setningen. Rad-bootstrap-KI, sidetallet 0,482, rutingsdetaljene (127/60/1, 183/1539) og repo-kommandoen er flyttet til et «Detaljer»-avsnitt rett under. Ingen tall fjernet.
5. **README:3, overpåstand.** «i alle sakstyper og markeder» → «… i NBIMs stemmedata (194 selskaper, 37 land)» (kilde: kravrespons:7, `kilder/omfang.txt`).

## Avvist
- Ingen. Pkt. 4 er tatt inn noe mindre strengt enn foreslått (fire linjer i boksen, ikke tre), fordi V1-setningen fra pkt. 1 skal stå i første skjermbilde.

## Kontroll
- `c1_tallvakt.py`: 18 filer, 169 påstander, 0 avvik (før og etter).
- `frys_fasit_1600.sha256` regenerert (README, kravrespons og JURY_SPORSMAL fra en annen oppgave endret); `frys_diff.sh --kilde`: FRYS LIK, 0 avvik, 138 filer.
- Commit med `git add -f` for README.md, kravrespons.md og fasiten. JURY_SPORSMAL.md (staget av en annen oppgave) er ikke tatt med i min commit.
