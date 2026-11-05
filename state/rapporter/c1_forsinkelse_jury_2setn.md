# Case 1: sen publisering forklart i to setninger for juryen (#2308, speider)

Til arkitektens #2300. Ingen nye målinger. Hvert tall er sjekket mot `arbeid/oppgave_2299/resultat_hoved.json`.

## Norsk
1. Siden 2021 har NBIM lagt ut hvordan de skal stemme fem dager før hvert generalforsamlingsmøte, og de forklarer hver stemme mot styret. Når agenten slår opp hvordan NBIM har stemt i et selskap før, bruker den derfor bare opplysninger som allerede er offentlige når saken skal avgjøres.
2. Vi har prøvd å la NBIMs stemmer bli kjent først 1 til 90 dager etter møtet. Treffet på stemmer mot styret (F1 på MOT) lå da på 0,52 i 2025 og 0,51–0,54 i 2024, mot 0,52 og 0,54 uten forsinkelse, og det største fallet (−0,03) er innenfor støyen. Det er fordi verdien kommer fra stemmer i tidligere år; uten noen historikk faller F1 til 0,34.

## English
1. Since 2021, NBIM has published its voting intentions five days before each shareholder meeting, with a reason whenever it votes against the board. When the agent looks up how NBIM voted at a company in the past, it only uses information that is already public when the decision is made.
2. We tested what happens if NBIM's votes only become known 1 to 90 days after the meeting. Accuracy on votes against the board (F1 on AGAINST) stayed at 0.52 in 2025 and 0.51–0.54 in 2024, compared with 0.52 and 0.54 with no delay, and the largest drop (−0.03) is within noise. The value comes from votes in earlier years; with no history at all, F1 falls to 0.34.

## Kilder
| Påstand | Kilde |
|---|---|
| 5 dager før møtet fra 2021, begrunnelse ved stemme mot styret | NBIM «Voting first half 2025», https://www.nbim.no/contentassets/ccd64fdd53d847c9aef7745f8b2241a8/voting-first-half_2025_uuweb.pdf (sitat i `c1_nbim_publisering.md` rad 2). NBIM skriver «where practicable», så noen få kan komme senere. Derfor er det testet med opptil 90 dager. |
| 0,52 (2025, N=0 og N=1–90) | `resultat_hoved.json`: 2025 N0 0,520231; N1–90 0,518072–0,526946 (A og B) |
| 0,54 / 0,51–0,54 (2024) | samme fil: 2024 N0 0,536313; N1–90 0,507246–0,536313 |
| største fall −0,03, KI dekker 0 | samme fil: 2024 N7 B, fall −0,0291, KI [−0,145; 0,074] |
| 0,34 uten historikk | `arbeid/oppgave_2299/kontroll.log`: 2025 N100000 B 0,335714. Tabellen i `c1_historikk_forsinkelse.md`: 2024 B 0,340 |

Forbehold: tallene gjelder val 2025 og 2024, ikke test 2026. Den leverte agenten har 0,476 på test, og dette er ikke målt med forsinkelse på test. Står setning 2 i JURY.md ved siden av 0,476, bør det komme fram at det er val/2024.
