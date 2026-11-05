# Case 1: ordsjekk av jurytekstene, ny kjøring etter innlimingen #2639 (#2648, kl. 17:33)

## Ny kjøring (#2648): før/etter
`bash arbeid/oppgave_2646/ordsjekk.sh` (BYTT) og `bash arbeid/oppgave_2648/ordsjekk_staar.sh` (samme skript, stier `c1/reserve_staar/`). Utskrift: `arbeid/oppgave_2648/treff_bytt.txt`, `treff_staar.txt`.

| Tekstsett | Før (17:30, #2646) | Etter (#2648) | Synlig tekst | `<!-- tallvakt` |
|---|---|---|---|---|
| BYTT (`c1/leveranse/` + `levering/README.md`) | 49 | **49** | 24 | 25 |
| STÅR-reserven (`c1/reserve_staar/` + `levering/README.md`) | ikke kjørt | **51** | 31 | 20 |

**Ærlig: 0 treff ble borte.** BYTT-filene ble endret kl. 17:21 (commit 5514792), altså før #2646-kjøringen. «Før»-tallet inneholder allerede #2639, og treff-listene er linje for linje like. #2639 rettet andre ting (ERLIG:34 «like over», benk A-overskriften), men **ingen av radene i tabellene under**. Rettelseslista fra #2646 står altså uendret. Den gjelder smed2 og må gjøres før tekststopp 19:00.

### Rettelsesliste BYTT til smed2 (fortsatt åpne, prioritert)
1. kravrespons.md:10 «0,512 ligger under målet vårt på 0,5» → «like over». Regnefeil.
2. ERLIG_EVALUERING.md:53 «les 0,512 (0,40–0,62), under målet 0,5» → «like over målet 0,5».
3. kravrespons.md:7 «[0,36; 0,59]» → «[0,40; 0,62]».
4. ERLIG_EVALUERING.md:29 og JURY_SPORSMAL.md:23 «fra 0,512 til 0,415»: fallet er målt på den frosne. Skriv «fra 0,476 til 0,415 (målt på den frosne modellen)».
5. JURY_SPORSMAL.md:82 «Den frosne agenten står.» er usant i BYTT. Skriv «Dommen 16:37 lot den frosne stå; ved 17:02 ble repo4 byttet inn (se § 7)», og se også :81 og :83.
6. README.md:9 «Valgt på val 2025 (0,530), kjørt én gang på test»: legg til «repo4 ble deretter byttet inn etter regelen på tre testår (2024–2026)».
7. Internspråk: kravrespons.md:7 og ERLIG:79 «grønn pakke innen 18:45» → «kjørt feilfritt fra kald start». ERLIG:79/93/102/104 «benk A/B» → «sammenligning A/B». ERLIG:106 og J:88 «grønne» → «besto». J:52 «tallvakt» → «tallsjekk (skript som sjekker tallene mot kjøringen)».
8. repo4 uforklart første gang: levering/README.md:3 (har #-numre), c1/leveranse/README.md:11, JURY_SPORSMAL.md:12 → «repo4 (frossen modell + fire historikktrekk)».

### Rettelsesliste STÅR til smed3 (#2640)
Er **riktige i STÅR** og skal stå: «[0,36; 0,59]» (README:8, kravrespons:7, J:15/92, ERLIG:6/33), «under målet» (kravrespons:10, ERLIG:53), «Den frosne agenten står» (J:82), «valgt på test» (README:9, J:69, ERLIG:34).
Skal rettes:
1. Internspråk «grønn»: README:12 og kravrespons:7 («på vilkår om grønn pakke innen 18:45» og «ble ikke grønn i tide»), ERLIG:106 og J:87 («ikke var grønn før tekststoppen»), MUNTLIG:13, ERLIG:108 og J:88 («alle grønne»). Forslag: «pakken med repo4 ble ikke kjørt feilfritt fra kald start før fristen» og «alle seks besto». OBS: tidspunktene «innen 18:45» og «før tekststoppen» må stemme med det som faktisk skjer.
2. «benk A/B»: ERLIG:79, 81, 93, 102, 104 → «sammenligning A/B». Overskriften på :81 ble rettet i BYTT, men ikke i STÅR.
3. J:52 «tallvakt» → «tallsjekk».
4. repo4 uforklart første gang: kravrespons:7, J:86 (sp. 20-overskriften), ERLIG:78 → «repo4 (frossen + fire historikktrekk)». ERLIG:86 har forklaringen, men først senere.

Felles for begge: `levering/README.md:45` «TALLVAKT GRØNN» er forklart og kan stå. `<!-- tallvakt`-kommentarene skal ikke fjernes før tekststoppen.

---

## Opprinnelig kjøring: ordsjekk av BYTT-jurytekstene, treff kl. 17:30 (#2646, til smed2 #2639 og smed3 #2640)

Skript: `bash arbeid/oppgave_2646/ordsjekk.sh [rot]` (rot = `arbeid/hack`, standard). Gir `fil:linje: [mønster] tekst`, exit 1 ved treff. `bash -n` er ok. Det søker i synlig tekst, der HTML-kommentarer er fjernet. `<!-- tallvakt` telles for seg. «repo4 uforklart» betyr at første «repo4» i fila står uten «historikktrekk», «frossen +» eller «internt kalt» på samme linje. Full utskrift: `arbeid/oppgave_2646/treff_1730.txt`. Kilder: `c1_juryles_bytt.md`, `c1_jury_rettelser.md`. Ingen leveransefiler er endret.

**Nå: 49 treff, 22 i synlig tekst og 27 `<!-- tallvakt`-kommentarer. MUNTLIG.md har 0 treff.** Stier er relative til `arbeid/hack/`.

## Feil tall og påstander (rettes først)
| Fil:linje | Treff | Hva er galt |
|---|---|---|
| c1/leveranse/kravrespons.md:10 | «0,512 ligger under målet vårt på 0,5» | Regnefeil: 0,512 > 0,5 |
| c1/leveranse/ERLIG_EVALUERING.md:53 | «les 0,512 (0,40–0,62), under målet 0,5» | Samme regnefeil, **ikke dekket av noen rettelse** |
| c1/leveranse/kravrespons.md:7 | «[0,36; 0,59]» | KI-et til den frosne modellen. Skal være [0,40; 0,62] |
| c1/leveranse/ERLIG_EVALUERING.md:29 | «fra 0,512 til 0,415» | Fallet på 0,06 er målt på den frosne modellen: skal være 0,476 → 0,415 |
| c1/leveranse/JURY_SPORSMAL.md:23 | «fra 0,512 til 0,415» | Samme feil, **ikke dekket av noen rettelse** |
| c1/leveranse/JURY_SPORSMAL.md:82 | «Den frosne agenten står.» | Usant i BYTT. Merk «før byttet» eller skriv om (også :81 «hovedtallet 0,476», :83 «I drift i dag setter vi den frosne») |
| c1/leveranse/README.md:9 | «Valgt på val 2025 (0,530), kjørt én gang på test» | Stemmer ikke for repo4, som ble byttet inn etter måling på 2024/25 |
| c1/leveranse/ERLIG_EVALUERING.md:104 | «ingen terskel, C eller trekk er valgt på test» | Samme spenning. Tåles hvis forbeholdet om tidspunktet rett etter står |

Godtatt, ingen endring nødvendig: ERLIG:34 «valgt på test» og «under målet» (2b er limt inn, og «Den frosne modellen (0,476) lå under målet» er sant), og J:69 «Én ting er valgt på test: båndet» (sant).

## Internspråk
| Fil:linje | Treff | Forslag |
|---|---|---|
| c1/leveranse/kravrespons.md:7 | «grønn pakke innen 18:45» | Skriv «kjørt feilfritt fra kald start med samme tall» (som 4b). Fyll inn utfallet etter dommen 18:45 |
| c1/leveranse/ERLIG_EVALUERING.md:79 | «på vilkår om grønn pakke innen 18:45», «benk A» | Som over. Skriv «sammenligning A» |
| c1/leveranse/ERLIG_EVALUERING.md:93, :102, :104 | «Benk B», «benk B sin trening», «benk A» | Skriv «sammenligning B/A» (4g dekket bare linje 81) |
| c1/leveranse/ERLIG_EVALUERING.md:106 | «grønn» (protokollsjekk) | Skriv «alle seks punkter besto» |
| c1/leveranse/JURY_SPORSMAL.md:88 | «alle grønne» | Skriv «alle besto» |
| levering/README.md:45 | «TALLVAKT GRØNN» | Er forklart på linja. Kan stå |
| c1/leveranse/JURY_SPORSMAL.md:52 | «målere, tallvakt» | Skriv «tallsjekk» eller legg til «(skript som sjekker tallene mot kjøringen)» |
| levering/README.md:3 | første «repo4» med «#2044 miks h2 + 4 repotrekk», «byttedom #2570» | Skriv «repo4 = frossen modell + fire historikktrekk fra tidligere møter». Fjern #-numrene |
| c1/leveranse/README.md:11 | første «repo4» er uforklart (forklaringen kommer på :12) | Flytt forklaringen til :11, eller skriv «repo4 (se under)» |
| c1/leveranse/JURY_SPORSMAL.md:12 | første «repo4» står i en kildelinje | Forklar første gang i en svartekst |

## `<!-- tallvakt`-kommentarer (27)
Kommentarene står i README.md:11–14, kravrespons.md:7, JURY_SPORSMAL.md (19 linjer) og ERLIG_EVALUERING.md:79, :104. De vises ikke i rendret markdown, men en jury som leser råfila ser dem. Tallvakten bruker dem, så **ikke fjern dem før tekststoppen**. Det er en egen avgjørelse for smed/dommer om de skal strippes i jury-zipen.

## Bruk
- smed2 (#2639): kjør etter innliming. Målet er 0 treff i tabellene over, mens kommentarene og levering/README.md:45 kan bli stående.
- smed3 (#2640): STÅR-reserven har andre filstier. Kjør `bash arbeid/oppgave_2646/ordsjekk.sh` med en kopi der FILER peker til `c1/reserve_staar/`. Mønstrene «Den frosne agenten står», «under målet» og «[0,36; 0,59]» er **riktige** i STÅR og skal ikke rettes der.
