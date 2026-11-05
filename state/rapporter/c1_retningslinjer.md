# Case 1 (#2105): NBIMs egne retningslinjer samlet i én siterbar jsonl

**Fil:** `arbeid/hack/retningslinjer/nbim_retningslinjer.jsonl`. Den har 672 avsnitt, alle fra nbim.no. Hvert avsnitt har feltene `id`, `kilde`, `tittel`, `avsnitt`, `tema`, `kilde_url` og `tekst`. Det er ingen Vanguard-tekst i fila. Dermed er H4 i kravsjekken løst på datasiden. Agenten (#2106, smed2) må fortsatt bytte kilde.

## Innhold
| Kilde | Id-mønster | Avsnitt | URL |
|---|---|---|---|
| Global Voting Guidelines (nettversjon) | `NBIM 3.3.8` | 140 | https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ |
| 12 posisjonsnotater (CEO-lønn, uavhengighet, styreleder/CEO, tidsbruk, mangfold, emisjoner, aksjeklasser, proxy access …) | `NBIM-PP3 5` | 256 | …/position-papers/<slug>/ |
| Forventninger: klima | `NBIM-EXP-KLIMA n` | 65 | …/our-expectations/climate-and-nature/climate-change/ |
| Forventninger: natur | `NBIM-EXP-NATUR n` | 87 | …/climate-and-nature/nature/ |
| Forventninger: menneskerettigheter | `NBIM-EXP-MR n` | 39 | …/people/human-rights/ |
| Forventninger: barns rettigheter | `NBIM-EXP-BARN n` | 40 | …/people/childrens-rights/ |
| Forventninger: human capital | `NBIM-EXP-HCM n` | 32 | …/people/human-capital-management/ |
| Stemmesiden | `NBIM-VOTE n` | 10 | …/responsible-investment/voting/ |
| Asset Manager Perspective: aksjonærforslag om bærekraft (2020) | `NBIM-AMP-SP n` | 3 | …/asset-manager-perspectives/2020/… |

Id-ene `NBIM …` og `NBIM-PP…` er de samme som i `c1/retningslinjer/punkter.jsonl` (#1948). Sitater som allerede finnes, gjelder derfor fortsatt.

## Akseptkravene: punktene agenten bør sitere
| Krav | Antall med tag | Avgjørende punkt |
|---|---|---|
| Styresammensetning | 163 | `NBIM 1.1.4`: stemmer ikke for ikke-uavhengig direktør når under 50 % av styret er uavhengig. `1.3.3`: styreleder som også er CEO. `2.1.x`: tidsbruk. `2.3.x`: mangfold |
| Godtgjørelse | 59 | `NBIM 3.3.8`: «clear misalignment between remuneration and long-term value creation». `3.3.10`: engangsbetalinger og fallskjermer. `NBIM-PP3`: CEO-lønn |
| Kapitalendringer | 103 | `NBIM 6.1.1`/`6.1.2`: aksjonærene skal godkjenne emisjoner og ha fortrinnsrett. `6.2.x`: fusjoner og oppkjøp. `NBIM-PP11`: emisjoner. `NBIM-PP7`: aksjeklasser |
| Aksjonærforslag: klima | 75 klima / 36 forslag | `NBIM 5.3.3`: støtter velbegrunnet forslag om rimelig rapportering. `5.3.4`: støtter ikke forslag som påtvinger strategi eller urealistiske mål. `5.3.10`: Say on Climate. `3.2.13`: ikke gjenvalg ved svikt i klimatilsynet. `NBIM-EXP-KLIMA` |
| Aksjonærforslag: menneskerettigheter | 115 | `NBIM-EXP-MR 1` (forventning om å integrere menneskerettigheter etter UNGP), `MR 9` (skjerpet aktsomhet i konfliktområder), og `NBIM-EXP-BARN`/`HCM`. Stemmeregelen for forslagene er `NBIM 5.3.3`/`5.3.4` |

## Ærlige forbehold
- NBIM har ingen egen stemmeregel for menneskerettighetsforslag. Forventningsdokumentene sier hva selskapene skal gjøre, ikke hvordan NBIM stemmer. Regelen som gjelder er 5.3.3 og 5.3.4 (støtte rimelig rapportering, avvise styring i detalj). Agenten bør sitere begge: stemmeregelen og forventningen.
- `tema` settes med nøkkelord og er grov. Natur og klima overlapper. Bruk taggen til filtrering, ikke som fasit.
- AMP-SP har bare 3 avsnitt, fra HTML-sammendraget. PDF-en (11 sider, `raa/sp.pdf`) er lagret, men ikke delt opp fordi tekstuttrekket av oppsettet er rotete.
- NBIMs side om rammeverket for bærekraftforslag (`NBIM-VOTE 10`) lenker ikke til noe eget dokument. Det er 5.3 i retningslinjene som gjelder.
- Teksten ble lastet ned 05.11.2026. GVG-nettversjonen ble lastet ned tidligere i dag (#1948). Retningslinjene endres over tid, så for 2025-møter kan teksten avvike noe (se `case1_val_test_gap.md` §3).

## For smed2 (#2106)
Lag BM25 over `tekst`. Filtrer først på `tema` ut fra saktypen, og siter `id` og `kilde_url`. For MOT på say-on-pay: `NBIM 3.3.8`/`3.3.10` og `NBIM-PP3`. For direktører: `1.1.4`, `1.3.3` og `2.1.x`.
