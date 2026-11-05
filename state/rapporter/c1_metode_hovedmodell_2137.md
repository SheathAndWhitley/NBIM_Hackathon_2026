# Case 1 (#2137, speider): METODE.md har hovedmodellen først, og sitatsvarene gjelder nå den leverte agenten

**Kort:** Jurylesningen #2129 pkt 1 og 4 er lukket i `arbeid/hack/levering/`. Modellen er ikke rørt, og hovedtallet 0,476 er uendret.

## Endret
- **METODE.md, ny pkt. 0 «Hovedmodellen på real_votes»:** data, splitt med saker og MOT per split, trekk, valget av grensen 0,9188, lekkasjesjekk #2103 og KI #2095. Pkt. 1–6 og 8 ligger nå under «Vedlegg: eldre N-PX-modell». «Les dette først»-boksen er erstattet av pkt. 0.
- **METODE.md pkt. 7** er flyttet opp foran vedlegget og skrevet om til den leverte agenten. Vanguard-teksten står igjen i vedlegget som «pkt. 7 i den eldre N-PX-agenten (ikke den leverte)».
- **JURYSVAR.md svar 6** er skrevet om: «Ja», med kilde, antall og stikkprøve, og med forklaring på hvorfor `rationale_text` er sitat og ikke trekk. Vanguard står bare på én merket linje. I svar 10 er N-PX-delen merket, og hovedmodellen har fått en egen setning.
- Kopi av filene før endringen: `/tmp/METODE_for_2137.md`, `/tmp/JURYSVAR_for_2137.md`.

## Kilder til tallene
| tall | kilde |
|---|---|
| train 2019–24: 9876 saker/504 MOT, val 2025: 1909/99, test 2026: 1539/58 (avvik 574/103/66) | Talt fra `state/opplastet/…real_votes.csv`. MOT er `nbim_vote` MOT og `against_board` 1. Test 1539/58 stemmer med måler v3 (#2087) |
| C=3, grense 0,9188, val-F1 0,522 (avvik) | `c1_agent_real_2053.md:15`, `oppgave_2044/train.py:101-116` |
| sakstype-ablasjon −0,011 / +0,024 med KI | `c1_lekkasje_v3.md` (#2103) |
| `--hist 1` 0,386 (avvik) | #1038 via `c1_agent_real_2053.md:19` |
| KI [0,36; 0,59] og [0,41; 0,63], 135 selskaper | #2095 og JURYSVAR 4 |
| 1578 rader, 18 avsnitt, 1504 × 0.0.3, 18/18 ordrett på nbim.no, 8 av 20 begrunnelser avviker | `c1_sitatkilder.md` (#2130) |
| 54 av 63 riktig seksjon (86 %), val 68 %, byte-like prediksjoner | `c1_retningslinje_sitat.md` (#2106) |
| stikkprøve 20/20 ordrett, 15/20 riktig regel, 4 delvis, 1 feil | `c1_sitat_verifisert.md` (#2115) |
| sitatbanken tar bare andre møter i tidligere år | `levering/c1_real.py:107` (lest i koden: `s[(by >= year) \| (bm == meeting_id)] = -9`) |

## Aksept
`grep Vanguard METODE.md JURYSVAR.md` gir fire linjer, og alle gjelder N-PX: METODE:44 er under vedlegget, METODE:84 er merket eldre agent, JURYSVAR:28 er merket eldre agent, og JURYSVAR:40 står etter «På den eldre N-PX-modellen».

## Rester (ikke rørt, for eier)
- `oppgave_2044/train.py:5-6`: docstringen sier fortsatt «ingen etiketter fra samme sesong», men koden kjøres med `--hist 2` (jurylesningen pkt 2).
- `KRAVRESPONS.md:63` (krav 13) nevner bare `rationale_text`. Den kan få GVG-sitatet og stikkprøven 15/20.
- Stikkprøven #2115 er på faktiske MOT, ikke predikerte. Den bør gjentas på agentens predikerte MOT etter #2120.
- Når #2134 har målt «bare år før» på MOT, skal tallet inn i pkt. 0 i stedet for avvikstallet 0,386.
