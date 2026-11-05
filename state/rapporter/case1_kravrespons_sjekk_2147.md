# Case 1: hvert krav i casen koblet til svar i kravresponsen (speider #2147, 05.11 kl. 13.10)

Jurys 1-sider: `arbeid/hack/c1/leveranse/kravrespons.md` (KR). Kilder: casen C = `CASE/.../FinTech_Hackathon_Caser_H2026.pdf.pakk_ut.txt`,
R = `case1_stemmegivning/README.md`, B = `Regler_og_bedommingskriterier.pdf.pakk_ut.txt`. Stier fra `arbeid/hack/`.
(Casefila `arbeid/hack/CASE/oppgave.md` finnes ikke, så kravene er tatt fra startpakken.)
Hovedtall = F1 MOT 0,476, test 2026, 58 MOT.

| # | Krav (kilde) | Svar i KR (fil:linje) | Tall der | Status |
|---|---|---|---|---|
| 1 | Leser saksliste, foreslår FOR/MOT/AVSTÅ per forslag (C:11) | KR:4 | – | **rettet nå**: FOR/MOT per forslag, AVSTÅ predikeres ikke (5 i test) |
| 2 | Predikerer MOT, ikke bare følg styret (#231, C:24–27) | KR:4, KR:11 og 15 | 30 av 58, F1 0,476, følg styret 0 | ok, hovedtall |
| 3 | Siterer retningslinjen som avgjør, og hvorfor (C:13, R:51) | KR:4 | – | **rettet nå**: sa bare «begrunnelse fra tidligere år». Agenten gir `retningslinje_id` + ordrett GVG-tekst + grunnlag på 1578/1578 rader (kjørt 13.05, /tmp/sp2147) |
| 4 | Konfidens, usikre til menneske (C:13, R:53) | KR:4 | **228 av 1 578 (14,4 %)** | utdatert: agenten gir nå 188 (11,9 %). Tallvakta: #2145 |
| 5 | Fasit = NBIMs faktiske stemmer (C:15) | KR:7 | – | ok |
| 6 | Baseline følg styret oppgitt og slått, P/R på MOT, ikke accuracy (C:19–27, R:49, B:44) | KR:7, KR:9–15 | 96,2 %, F1 0 vs 0,476 | ok |
| 7 | Motstandstesten, rapporter uansett (R:55, B:52) | KR:17 | 82 av 174 (logreg #2046) | **rettet nå** (manglet helt). Tall på frossen modell venter på #2144 |
| 8 | Tidssplitt (R:61, B:55) | KR:7 | val 2025 / test 2026 | ok |
| 9 | Kategori-/feltlekkasje (R:63) | KR:7 | – | ok |
| 10 | Klasseubalanse (R:65) | KR:7 | 96,2 % | ok |
| 11 | Beslutningen løsningen støtter (B:23, B:39) | KR:4, KR:20 | – | ok (sortere for analytiker) |
| 12 | Reproduserbart, ett kall (B:16, B:45) | KR:17 | 31–52 s | ok. README:16 `bash leveranse/kjor.sh` |
| 13 | Mal: Hva vi bygde / verifiserte / trengt videre, maks 1 side (B:14, B:21–27) | KR:3, 6, 19 | – | ok, 4,2 kB (~1 side) |
| 14 | Hva vi ville trengt videre (B:26) | KR:19–20 | 0,415 / 0,145 | ok, men sier mest begrensninger. Data/tilgang (API til NBIM-databasen, flere år) kan stå én setning |
| 15 | Erklærte begrensninger, sporbarhet (B:52) | KR:20 | – | ok |
| 16 | Kilder med URL (B:59) | README:64–80 | – | ok |
| 17 | AI-verktøy oppgitt (B:61) | README:82–87 | – | ok |
| 18 | Kopiert kode kreditert (B:65) | README:78–80 | – | ok |
| 19 | Juryspørsmål 1–3 (B:70–72) | `c1/leveranse/JURY.md` | – | finnes, ikke sjekket tall (#1975) |
| 20 | Praksis vs. policy (R:39, «vrien») | – | – | **ikke besvart** noe sted i KR. Valgfritt; kan bli én setning når GVG-punktene er koblet til MOT-treff |

## Utdatert utenfor KR (for #2145 / README-eier, ikke rettet av meg)
- `c1/leveranse/README.md:3–5`: «say-on-pay», «konfidens under 0,6», «N-PX»: beskriver den gamle grunnlinja, ikke agenten.
- `README.md:44`: «sitat (Vanguards policy)»: agenten siterer NBIM GVG nå.
- `README.md:94–95`: «motstandstest 0 av 158», «sitatlaget gir 0 MOT»: utdatert.
- `BEGRENSNINGER.md:28` (15 av 64, Vanguard-sporet) og `JURY.md:48` (0 av 50, «ikke tavleført»): to ulike motstandstall, ingen på frossen modell. #2144 må gi ett tall, og det skal stå likt i KR:17, BEGRENSNINGER og JURY.
- KR:4 228 til menneske mot README:9 188. Det er samme kjøring med ulik kode: dagens `kjor_agent.py` gir 188.
