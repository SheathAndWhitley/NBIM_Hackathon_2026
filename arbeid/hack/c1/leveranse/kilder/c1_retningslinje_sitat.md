# Case 1 (sak 2106, smed2): agenten siterer nå avsnittet i NBIMs Global Voting Guidelines, ikke bare gamle begrunnelser

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

**Kort:** `kjor_agent.py` gir tre nye kolonner i `agent.csv`: `retningslinje_id` (f.eks. `NBIM 5.2.4`),
`retningslinje_sitat` (ordrett avsnitt fra nbim.no) og `retningslinje_grunnlag` (hvorfor dette avsnittet, og hvilke
«We will not support»-regler i seksjonen et menneske bør sjekke). På MOT-sakene i test 2026 treffer oppslaget samme
seksjon som NBIM selv oppga i **86 %** av tilfellene (54 av 63). Blant agentens riktige MOT-prediksjoner er treffet **94 %** (31 av 33).
Prediksjonene er byte-like med versjonen uten oppslaget (`pred_maaler.csv` og `_pred_uten_ruting.csv` sjekket med cmp).
F1 på MOT er fortsatt 0,4818 (maskin alene, test 2026). <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->

## Hvordan
- Kilde: `arbeid/hack/c1/retningslinjer/punkter.jsonl`, de 131 nummererte NBIM GVG-punktene i prinsipp 1-6 (speider sak 1948).
  Mappa `arbeid/hack/retningslinjer/` fra oppgaveteksten fantes ikke. Speiderens filer lå allerede i `hack/c1/retningslinjer/`.
- Kode: `arbeid/hack/levering/retningslinje_oppslag.py`, ren BM25 uten ny modell og uten nye pakker. Det kobles inn i `c1_real.py`
  etter at MOT/FOR er bestemt.
- Spørring: forslagstypen (utvidet med noen ord) + forslagsteksten + teksten i nabo-begrunnelsen (NBIMs begrunnelse fra en
  tidligere, lignende sak, som agenten allerede fant). Avsnitt i nabo-begrunnelsens seksjon får +12.
- Vektene er valgt på val 2025 (`arbeid/oppgave_2106/evaluer.py`, rutenett over 120 kombinasjoner) og låst før test 2026.
- FOR-saker får `NBIM 0.0.3` («Our starting point when deciding how to vote is to support the board»).
- Sakens egen begrunnelse og seksjon brukes aldri, bare tidligere år. Fasit-seksjonen brukes bare til måling.

## Målt (MOT-saker med NBIM-seksjon, fasit = `rationale_section`)
| Variant | val 2025 (n=103) | test 2026 (n=63) |
|---|---|---|
| bare BM25 på saksteksten | 34 % | 43 % |
| BM25 + forslagstype-prior | 54 % | 59 % |
| bare nabo-begrunnelsens seksjon | 67 % | 86 % |
| **låst: BM25 + nabo-tekst + nabo-seksjon** | **68 %** | **86 %** |

Ærlig lesning: nesten hele treffet kommer fra nabo-begrunnelsen som agenten allerede hadde. BM25 på saksteksten alene er
svak (34-43 %), fordi teksten ofte bare er «Elect Director X» eller «Approve Remuneration Report». Oppslaget legger
ikke til mye på seksjonsnivå (+1 pp på val, 0 på test). Det det gir, er en **retningslinje-id og ordrett NBIM-tekst**
i stedet for en gammel begrunnelse.

## Stikkprøve: 20 MOT-prediksjoner (seed 2106, `arbeid/oppgave_2106/stikkprove20.csv`)
13 er ekte MOT med NBIM-seksjon, 7 er feil-MOT eller mangler fasit.

| # | Sak (type, tekst) | NBIM | Valgt | Vurdering |
|---|---|---|---|---|
| 1 | DIR, Elect J. Mariner Kemper | ikke MOT | 1.3.1 styreleder/CEO | plausibel, men saken er feil-MOT |
| 2 | OTHER_MGMT, limits Sec. 186 | 6.3 | 6.3.3 nærstående | **treff** |
| 3 | DIR, Tanaka | 1.1 | 1.1.2 uavhengighet | **treff** |
| 4 | DIR, An Meng | 1.2 | 1.2.1 komiteer | **treff** |
| 5 | DIR, Approve Changes in Boards | 3.1 | 3.1.3 | seksjon treff, avsnittet er svakt (3.1.1/3.1.9 passer bedre) |
| 6 | DIR, Elect/Ratify Directors and Alternates | 3.1 | 3.1.3 | seksjon treff, avsnittet er svakt |
| 7 | DIR, Otsuka | 1.1 | 1.1.2 | **treff** |
| 8 | SAY_ON_PAY | 3.3 | 3.3.2 | **treff** |
| 9 | OTHER_BUSINESS | (ingen fasit) | 5.2.4 «other business» | riktig regel |
| 10 | SAY_ON_PAY | 3.3 | 3.3.2 | **treff** |
| 11 | DIR-type, Remuneration of Vice-Chairman | ikke MOT | 3.1.3 | **bom**: burde vært lønn |
| 12 | SHP, Majority Vote for Director Elections | 3.1 | 6.2.5 anti-takeover | **bom**: riktig er 3.1.8 |
| 13 | DIR, Korys Management (dominant eier) | ikke MOT | 1.1.2 | plausibel |
| 14 | DIR, Havner | ikke MOT | 2.1.1 tidsbruk | plausibel |
| 15 | DIR, Miida | ikke MOT | 1.1.2 | plausibel |
| 16 | DIR, Franklin | 2.1 | 2.1.1 tidsbruk | **treff** |
| 17 | DIR, D. Bryan Jordan | ikke MOT | 1.3.1 | plausibel |
| 18 | OTHER_BUSINESS | 5.2 | 5.2.4 | **treff** |
| 19 | AUDITOR | 5.1 | 5.1.2 ikke-revisjonshonorar | **treff** |
| 20 | SAY_ON_PAY | 3.3 | 3.3.2 | **treff** |

Av de 13 med fasit: **12 av 13 treffer seksjonen**. To av dem (5, 6) har et svakt avsnitt innenfor riktig seksjon, og én bommer (12, aksjonærforslag).
Av de 7 uten fasit: 5 er plausible, 1 passer godt (9) og 1 bommer (11). Feil-MOT får et plausibelt sitat. Sitatet
skiller altså ikke riktige MOT fra feil-MOT, og det skal det ikke heller. Rutingen til menneske er det som tar usikkerheten.

## Hvor den bommer, og hvorfor (arbeid/oppgave_2106/bom.py, selskap.py)
- Direktørvalg står for nesten alle bom (2025: 56 % treff på 63 saker, 2026: 80 % på 30). Teksten er «Elect Director X».
  Grunnen (uavhengighet 1.1, tidsbruk 2.1 eller ansvar 3.2) står ikke i dataene.
- Samme person i samme selskap tidligere år treffer 95-100 % når den finnes (40 av 103 saker i 2025, 22 av 63 i 2026).
  Nabo-finneren tar den allerede, så «person først» ga ingen gevinst (68 % / 86 %, likt). Selskapets siste MOT-begrunnelse
  for samme type er dårligere (73 % / 82 % der den finnes). Resten er et ærlig tak: uten historikk for personen kan
  teksten ikke si hvilken regel som slo til.
- Posisjonsnotat: `retningslinje_grunnlag` nevner nå også NBIMs posisjonsnotat fra nabo-begrunnelsen (f.eks. «Board
  independence (NBIM-PP2)»), på 49 av 74 MOT-saker. Det stemmer med sakens eget notat i 56 % (val 2025) og 79 % (test 2026),
  så det er en henvisning, ikke hovedsitatet.

## Prøvd og forkastet
`REGEL=True`: inne i seksjonen velges regelen i riktig retning («We will not support …») ut fra saksteksten. Det ga konkrete,
men gjettede regler, f.eks. 3.3.9 «lav støtte» for hver lønnsrapport og 2.1.4 «oppmøte under 75 %» for direktører.
Dataene sier ikke hvilken regel som slo til. Derfor står prinsippavsnittet igjen som sitat, og det er også det NBIM selv
skriver i begrunnelsene. Reglene i seksjonen listes i `retningslinje_grunnlag` for mennesket.

## Kjør
```
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut
uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/oppgave_2106/evaluer.py      # tabellen over
python3 arbeid/oppgave_2106/stikk.py /tmp/c1_ut/agent.csv /tmp/stikk.csv                    # stikkprøven
```
Neste steg: aksjonærforslag (sak 12) bør få seksjon fra typen (SHP_GOVERNANCE → 3.1/4.x) heller enn fra naboen, og
METODE.md/JURYSVAR bør nevne de nye kolonnene og tallet 86 %. Det siste er speiderens oppgave.

## Kald start (12:45)
Kopilistene i `arbeid/hack/levering/fremmed.sh` og `arbeid/hack/c1/kaldstart.sh` hadde ikke de nye filene, og kald kopi
ville da krasjet. Begge har nå fått `hack/levering/retningslinje_oppslag.py` og `hack/c1/retningslinjer/punkter.jsonl`.
- `fremmed.sh /tmp/fremmed_2106`: 27 s, `agent.csv` er byte-lik den varme kjøringen.
- `kaldstart.sh`: **GRØNN F1_MOT 0,476190, avvik +0,000000** mot referansen (måler v3).
- Merk: sha-en til `c1_real.py` i `arbeid/kandidater/FROSSEN.md` er utdatert. Endringen legger bare til kolonner,
  og prediksjonen er byte-lik. `arbeid/oppgave_2118/fremmed_kopi.sh` (ikke min) mangler de samme to filene.
