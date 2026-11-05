# Case 1 #2919: ablasjon av forklarings-trekkene i K3: ingen av dem bærer en gevinst (smed, 05.11)

Det finnes ingen gevinst å fordele. Full K3 ligger alt 0,0015 under v2+av (#2907). Ingen ablasjon flytter snittet med 0,02 eller mer mot K3. Det var terskelen i `arbeid/oppgave_2919/REGEL.md`, skrevet før måling.
Oppsettet er identisk med #2907 (`arbeid/oppgave_2919/maal.sh`, kopi): v2+av, k 32/64/48, av-regel, maaler_aar.py F1 MOT. 2023 er vakt-år. K3 kjørt på nytt gir byte-like tall, så kjøringen er deterministisk.
Frossen = 0,5162 snitt 24–26 (2023-vakt 0,3535). v2+av = 0,5596.

| variant | trekk | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24–26 | mot K3 | mot v2+av | mot frossen |
|---|---|---|---|---|---|---|---|---|---|
| v2+av (ingen) | – | 0,3723 | 0,5731 | 0,5667 | 0,5391 | 0,5596 | +0,0015 | 0 | +0,0434 |
| **K3 full** | 1,2,3,4 | 0,3743 | 0,5679 | 0,5667 | 0,5397 | 0,5581 | 0 | −0,0015 | +0,0419 |
| A-1 (uten 1) | 2,3,4 | 0,3743 | 0,5732 | 0,5366 | 0,5714 | 0,5604 | +0,0023 | +0,0008 | +0,0442 |
| A-2 (uten 2) | 1,3,4 | 0,3684 | 0,5783 | 0,5618 | 0,5203 | 0,5535 | −0,0046 | −0,0061 | +0,0373 |
| A-3 (uten 3) | 1,2,4 | 0,3723 | 0,5610 | 0,5281 | 0,5378 | 0,5423 | −0,0158 | −0,0173 | +0,0261 |
| A-4 (uten 4) | 1,2,3 | 0,3743 | 0,5679 | 0,5587 | 0,5354 | 0,5540 | −0,0041 | −0,0056 | +0,0378 |
| S1 = K1 | 1 | 0,3723 | 0,5647 | 0,5587 | 0,5410 | 0,5548 | −0,0033 | −0,0048 | +0,0386 |
| S2 | 2 | 0,3723 | 0,5542 | 0,5207 | 0,5614 | 0,5454 | −0,0127 | −0,0142 | +0,0292 |
| S3 | 3 | 0,3684 | 0,5680 | 0,5568 | 0,5366 | 0,5538 | −0,0043 | −0,0058 | +0,0376 |
| S4 | 4 | 0,3723 | 0,5698 | 0,5667 | 0,5439 | 0,5601 | +0,0020 | +0,0005 | +0,0439 |

Trekk: 1 = personen fikk MOT med GVG 1.1–1.3 før, 2 = selskapet hadde det før, 3 = lønn (GVG 3.3), 4 = rem-komité × lønns-MOT i fjor.

## Funn
- **Ingen enkelt trekk bærer noe.** Det største utslaget kommer når trekk 3 fjernes: −0,0158, under terskelen på 0,02. Det samme ser vi når trekk 2 står alene: −0,0127. Begge drives av 2025, som faller med 0,03–0,04. Da må det være kombinasjonen av trekk og rangering som utløser fallet, ikke at trekk 3 er nyttig. Bare trekk 3 alene (S3) ligger likt med K3.
- **Svingene fra år til år er større enn effekten.** Ta bort trekk 1 (A-1): 2025 faller 0,030 og 2026 stiger 0,032, så snittet blir nesten uendret. Med fast frø gir altså en ny trekk-kombinasjon ±0,03 per år. Det er langt mer enn frø-sd 0,005 fra #2911. Miks-rangeringen og grensen flytter seg.
- **Beste variant er S4 (bare trekk 4) med 0,5601, og A-1 med 0,5604.** Det er +0,0005 og +0,0008 over v2+av, altså støy. Ingen av dem består regel B (+0,02 over v2+av). A-1 ville også feilet år-vakta mot v2+av: 2025 ligger 0,030 under.
- Alle variantene består regel A mot frossen. Det skyldes v2+av, ikke trekkene.

## Anbefaling til natt-dommen (#2874)
Ingen forklarings-variant meldes. Sporet er lukket på nytt, nå med ablasjon som grunn. Skal begrunnelser brukes, er det som etterregel (#2907) med ny regel før måling, ikke som trekk.

Rådata: `arbeid/oppgave_2919/ut/<variant>/resultat.txt` og `maal_<år>.txt`.

## Tillegg: støygulv for «legg til ett trekk» (R1–R6, regel i REGEL.md før måling)
Seks kjøringer: v2+av pluss ett helt tilfeldig binært trekk (3 % enere, frø 1–6). Trekket bærer ingen informasjon, så alt det flytter er støy.

| år | endring mot v2+av, snitt | sd | min | maks |
|---|---|---|---|---|
| 2023 | −0,0029 | 0,0073 | −0,0155 | +0,0040 |
| 2024 | −0,0093 | 0,0049 | −0,0150 | −0,0033 |
| 2025 | −0,0230 | 0,0182 | −0,0455 | −0,0032 |
| 2026 | +0,0134 | 0,0113 | −0,0013 | +0,0250 |
| snitt 24–26 | −0,0062 | 0,0090 | −0,0187 | +0,0021 |

R1–R6 snitt 24–26: 0,5440 / 0,5597 / 0,5608 / 0,5532 / 0,5617 / 0,5409.

- **Alle ablasjonene ligger inne i støybåndet** (0,5409–0,5617). Det gjelder også A-3 (0,5423) og S2 (0,5454). Forklarings-trekkene oppfører seg altså som tilfeldige trekk.
- **År-vakta (−0,02) utløses av ren støy i 3 av 6 kjøringer.** Det er nesten alltid 2025 som utløser den. Et ekte trekk kan derfor bli stoppet av vakta uten å være dårlig. Og sd på 0,009 i snittet er nær kravet på +0,02. Dette gulvet er nesten dobbelt så stort som frø-sd 0,0047 (#2911), fordi frø-spredning ikke fanger at trekk-settet endrer seg.
- **Til #2874:** når tidsvekt-kandidaten (#2910) og andre trekk-kandidater vurderes, bør +0,02 leses mot dette gulvet (sd 0,009), ikke mot frø-sd. Regelen endres ikke her. Det er dommerens sak.

Rådata: `arbeid/oppgave_2919/ut/R*/resultat.txt`. Kode: `v2f_rull.py --grunn r<frø>`.
