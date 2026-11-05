# Case 1 (#2304, speider): NBIMs egne ord bak India-regelen «styreleder som også er MD/CEO → MOT»

**Konklusjon:** NBIMs regel gjelder **alle markeder**. Verken retningslinjene eller posisjonsnotatet nevner India eller gir unntak for noe marked. India-regelen (#2294) er derfor ikke en egen NBIM-politikk for India. Den er den globale regelen brukt på India, der forslag av typen «Approve appointment of X as Chairman and Managing Director» er vanlige.

## Sitater (ordrett, sjekket på nbim.no 05.11.2026 kl. 14.3x)
1. **GVG 1.3.3:** «We may not support the election of a chairperson who is also the CEO of the company.»
   Kilde: https://www.nbim.no/en/responsible-investment/voting/global-voting-guidelines/ , del 1 «Board independence», avsnitt 3 «Separation of chairperson and CEO», punkt 1.
2. **GVG 1.3.4:** «We will not support an authorisation for the chairperson to serve as CEO.»
   Samme URL og avsnitt, punkt 2. Dette punktet passer best til indiske forslag om å *godkjenne* at styreleder også er MD/CEO. «Will not» er sterkere enn «may not» i 1.3.3.
3. **Posisjonsnotatet, avsnitt 8:** «The responsibilities of the board include hiring, remunerating, monitoring and, when necessary, replacing the CEO. For the board to be independent in carrying out these responsibilities, it cannot be chaired by the CEO.»
   Kilde: https://www.nbim.no/en/responsible-investment/position-papers/separation-of-chairperson-and-ceo/

Innledningen til GVG 1.3 sier også: «We believe shareholders are best served when the chairperson and CEO roles are held by different individuals.»

## Forbehold
- **«May not» betyr ikke «alltid MOT».** Posisjonsnotatet (avsnitt 12 og 19) åpner for kombinerte roller i perioder, med tiltak mot interessekonflikt. Regelen bør derfor sitere 1.3.3/1.3.4 som grunn, ikke som fasit. Det stemmer med at regelen R bare traff 5 av 14 indiske MOT (#2294).
- **NBIMs egne begrunnelser er nesten bare amerikanske.** I `arbeid/hack/c1/kilder/nbim_begrunnelser.csv` (fra 2023-11 til 2026-05) viser 64 avvik til styreleder/CEO-teksten. Ingen av dem er i et indisk selskap; nesten alle er «Elect Director <CEO>» i USA. 63 av 64 bruker en eldre tekst: «The roles of chairperson and CEO should not be held by the same individual. Where a company founder combines both roles, we may support this for a limited period…». Grunnleggerunntaket står ikke lenger på nettsiden (se `c1_sitatkilder.md`). Siter dagens tekst med hentedato.
- I `arbeid/hack/retningslinjer/nbim_retningslinjer.jsonl` har sitatene id-ene `NBIM 1.3.3`, `NBIM 1.3.4` og `NBIM-PP10 8`. Agenten kan bruke dem direkte.
