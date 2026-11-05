# Case 1: målte tall rett fra den offisielle måleren

Generert 2026-11-05 17:36 med `python3 -I arbeid/hack/c1/lag_tall_tabell.py`. Måler `maaler_offisiell_v3.py --score mot` (sha256 418a937e57), data real_votes (NBIMs ekte stemmer), VAL = 2025, TEST = 2026 (58 stemmer MOT mot styret; 66 avvik inkl. AVSTÅ er ikke hovedtallet).
Hovedtall: F1 på MOT mot styret (ordre #231). P, R, KI og flagget gjelder TEST; PR-AUC er på avvik (måleren har ingen MOT-sannsynlighet). KI = 95 % bootstrap (2000 trekk) over testradene (rader, ikke klynger), punkt-F1 kontrollert lik målerens. README, JURY.md og ERLIG_EVALUERING.md bruker klyngebootstrap per selskap for hovedtallet (repo4), [0,40; 0,62]; for eldre frossen #2044 er klyngebootstrap [0,36; 0,59].
Grensa er valgt på VAL av hver modell; måleren får modellens egen beslutning. Ingen selvrapporterte tall.

| gruppe | forsøk | VAL F1 | TEST F1 | P | R | 95 % KI | flagget | PR-AUC (avvik) |
|---|---|---|---|---|---|---|---|---|
| grunnlinje | følg styret | 0.000 | 0.000 | 0.00 | 0.00 | [0.00, 0.00] | 0 | 0.038 |
| modell | repo4 = #2044 miks h2 + 4 historikktrekk (levert agent, maskin alene, #2592) | ikke målt (ingen fil) | 0.512 | 0.48 | 0.55 | [0.40, 0.62] | 67 | 0.536 |
| modell | smed2 #2044 miks LR+LGBM, løpende historikk (eldre frossen, levert til 17:03) | ikke målt (ingen fil) | 0.476 | 0.44 | 0.52 | [0.37, 0.59] | 68 | 0.524 |
| modell | smed3 #2037 tfidf+LR+selskapshistorikk med NBIM-sitat (agentens sitatvariant) | 0.505 | 0.454 | 0.39 | 0.55 | [0.35, 0.56] | 83 | 0.490 |
| ablasjon #2045 (eldre frossen #2044) | ingen (full modell = eldre frossen #2044) | ikke målt (ingen fil) | 0.476 | 0.44 | 0.52 | [0.37, 0.59] | 68 | 0.524 |
| ablasjon #2045 (eldre frossen #2044) | uten tekst (tfidf) | ikke målt (ingen fil) | 0.482 | 0.50 | 0.47 | [0.36, 0.60] | 54 | 0.498 |
| ablasjon #2045 (eldre frossen #2044) | uten selskapshistorikk | ikke målt (ingen fil) | 0.352 | 0.26 | 0.55 | [0.26, 0.44] | 124 | 0.504 |
| ablasjon #2045 (eldre frossen #2044) | uten teksthistorikk | ikke målt (ingen fil) | 0.463 | 0.41 | 0.53 | [0.35, 0.57] | 76 | 0.508 |
| ablasjon #2045 (eldre frossen #2044) | uten all historikk | ikke målt (ingen fil) | 0.276 | 0.19 | 0.53 | [0.20, 0.35] | 167 | 0.429 |
| ablasjon #2045 (eldre frossen #2044) | uten forslagstype | ikke målt (ingen fil) | 0.500 | 0.50 | 0.50 | [0.38, 0.61] | 58 | 0.502 |
| ablasjon #2045 (eldre frossen #2044) | uten forslagsstiller | ikke målt (ingen fil) | 0.496 | 0.48 | 0.52 | [0.38, 0.60] | 63 | 0.520 |
| ablasjon #2045 (eldre frossen #2044) | uten land | ikke målt (ingen fil) | 0.448 | 0.45 | 0.45 | [0.33, 0.56] | 58 | 0.489 |
| ablasjon #2045 (eldre frossen #2044) | uten styrets anbefaling | ikke målt (ingen fil) | 0.492 | 0.47 | 0.52 | [0.38, 0.60] | 64 | 0.514 |
| ablasjon #2045 (eldre frossen #2044) | bare historikk | ikke målt (ingen fil) | 0.462 | 0.52 | 0.41 | [0.34, 0.58] | 46 | 0.422 |
| ablasjon #2045 (eldre frossen #2044) | bare tekst | ikke målt (ingen fil) | 0.388 | 0.30 | 0.55 | [0.29, 0.48] | 107 | 0.423 |

«ikke målt (ingen fil)»: smeden har ikke lagret VAL-prediksjoner, så VAL-tallet finnes bare i loggen og står ikke her. Med 58 MOT i test er ±0,05 F1 innenfor støyen; se KI.
