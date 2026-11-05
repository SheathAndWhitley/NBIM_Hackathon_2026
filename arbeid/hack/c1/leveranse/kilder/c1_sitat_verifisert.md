# Case 1 (sak 2115, dommer2): sitatstikkprøve, 20/20 ordrett, 15/20 passer saktypen (4 delvis, 1 feil)

**Svarfil.** `arbeid/oppgave_2106/test2026_mot.csv` (sha1 60d82e2b), smed2s oppslag fra sak 2106 mens oppgaven var i arbeid (20 %). Fila har 63 rader: test 2026, MOT-stemmer med GVG-begrunnelse. Vekter: `[0, 12, 0, true]`.
**Kilde.** `arbeid/hack/retningslinjer/nbim_retningslinjer.jsonl` (sha1 6852e710, 672 avsnitt, speider sak 2105).
**Utvalg.** `pandas.sample(20, random_state=2115)`. Skript: `python3 arbeid/oppgave_2115/sjekk.py`. Sammenligningen normaliserer mellomrom og typografiske anførselstegn.

## Svar
| kontroll | resultat |
|---|---|
| Sitatet finnes ordrett i kilden | **20/20** (hele fila: 63/63) |
| `pid` finnes, og sitatet står i nettopp det avsnittet | **20/20** |
| Seksjonen er lik NBIMs egen begrunnelsesseksjon | 19/20 |
| **Sitatet handler om saktypen og er regelen som avgjør** | **15/20 riktige**, 4 delvis, 1 feil |

## Feil og delvis
| sak | type | sitert | dom |
|---|---|---|---|
| 2082048\|5 «Ratify Supermajority Vote Requirement…» | ARTICLES | NBIM 6.1.3 (en generell fullmakt skal ligge nær kapitalbruken i tid) | **FEIL.** Saken gjelder anti-takeover og vedtekter. Riktig er 6.2.5 eller 4.3.1. |
| 2089598\|12 «Issue of Equity without Pre-emptive Rights» | SHARE_ISSUANCE | NBIM 6.1.3 | **Delvis.** Seksjonen er riktig, men regelen som avgjør er fortrinnsretten i 6.1.2 (som NBIM selv siterer). |
| 2084790\|5, 2087754\|5 «Approve Changes in the Boards» | DIRECTOR_ELECTION | NBIM 3.1.3 (aksjonærer skal kunne foreslå kandidater) | **Delvis.** Seksjonen er riktig, men 3.1.1 (robust nominasjons- og valgprosess) er det NBIM sier. |
| 2084301\|47 «Elect Supervisory Board Member» | DIRECTOR_ELECTION | NBIM 3.1.3 | **Delvis**, samme grunn. |

## Mønster
- Agenten velger ofte samme setning for hele seksjonen: 3.1.3 brukes 9 av 63 ganger, 6.1.3 4 ganger. Avsnittsvalget innenfor seksjonen er svakere enn seksjonsvalget.
- 6.1.3 er feil også utenfor utvalget. Rad «Amend Articles (Office Term)» (2048411\|10) har fasit 4.3.
- **Forbehold.** Populasjonen er de *faktiske* MOT-sakene med GVG-begrunnelse, ikke agentens predikerte MOT. `pid==gull` gjelder for nesten alle, og `gull` lages fra fasit-seksjonen bare til måling. Det er ikke lekkasje i oppslaget så lenge `nabo` kommer fra tidligere år (se docstring i `retningslinje_oppslag.py`), men jeg har ikke reprodusert det. Når sak 2114 legger sitatene inn i agentens svarfil, bør stikkprøven gjentas på predikerte MOT med `sjekk.py <svarfil>`.
