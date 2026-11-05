# Case 1: når NBIM publiserer stemmene sine (#2301, speider, 05.11)

**Kort svar:** Fra og med 2021 publiserer NBIM stemmeintensjonen **5 dager FØR** møtet, der det er praktisk mulig.
Når NBIM stemmer mot styret, kommer det en kort begrunnelse med. I 2013–2020 ble stemmen publisert **dagen etter** møtet.
Testårene våre (2024 og 2025) ligger helt i ordningen med 5 dager før.

## Påstander med kilde

| # | Påstand | Sitat | Kilde | Type |
|---|---|---|---|---|
| 1 | Publisering 5 dager før møtet, der det er praktisk mulig | «We publish our voting instructions 5 days before the shareholder meeting where practicable.» | https://www.nbim.no/en/responsible-investment/voting/our-voting-records/ | NBIM selv (sitatet er gjengitt av hentverktøyet, se forbeholdet) |
| 2 | Ordningen gjelder fra 2021, og stemmer mot styret får en begrunnelse | «since 2021, we have published our voting intentions five days before each meeting, with a brief rationale referring to the relevant part of our voting guidelines whenever we vote against the board's recommendations.» | https://www.nbim.no/contentassets/ccd64fdd53d847c9aef7745f8b2241a8/voting-first-half_2025_uuweb.pdf | NBIM selv (forvaltningsrapporten «Voting first half 2025»; jeg hentet teksten ut av PDF-en selv) |
| 3 | Det samme står i 2025-rapporten | «We publish our voting intentions five days before each shareholder meeting where practicable, and provide explanations when we vote against the board.» | samme PDF som i rad 2 | NBIM selv |
| 4 | Stemmearkivet går tilbake til 2013 | «Voting instructions are available from 2013.» | samme side som i rad 1 | NBIM selv (gjengitt av hentverktøyet) |
| 5 | Endringen ble varslet i desember 2020 | «is to begin publishing its voting intentions five days before AGMs» | https://boardagenda.com/?p=24634 (15.12.2020) | presse |
| 6 | I 2013–2020 ble stemmen publisert dagen etter møtet | Søkesammendrag av Top1000funds: NBIM «began reporting its voting decisions the day after the meeting in 2013». Reuters, mai 2020: begrunnelsen publiseres «one day after the shareholder meeting». | https://www.top1000funds.com/events/sustainability-in-practice/sustainability-march-2021/nbim-prepares-to-up-voting-transparency/ (403 for oss) og https://archives.lincolndailynews.com/2020/May/20/NEWS/business_i.shtml (ga ikke svar) | **svakest**: bare fra søkesammendrag, jeg har ikke lest originalteksten |

Forbehold: sitatene i rad 1 og 4 er gjengitt av WebFetch-modellen, ikke kopiert fra rå HTML. Rad 2 og 3 hentet jeg ut av PDF-en selv med pypdf. Rad 6 er ikke bekreftet i primærkilden.

## Hva dette betyr for vår modell
- «Where practicable» betyr at noen stemmer kommer senere enn 5 dager før. Hvor mange det er, oppgir ikke NBIM. Vi kan ikke tallfeste andelen.
- Kravresponsen sier «NBIM publiserer stemmene løpende» uten kilde (H4 i c1_jurylesning_dommer2.md). Den bør bytte ut den setningen med sitat 2 og URL-en til PDF-en.
- Rapporten case1_lekkasjesjekk.md sier «dagen etter møtet». Det stemmer bare for 2013–2020. Fra 2021 blir stemmen kjent tidligere enn som så, så historikktrekket med møter < D er ikke en lekkasje.

## Forsinkelse N for arkitektens #2299
**Realistisk N = 0 dager:** historikk fra alle møter før D er kjent når agenten kjører. Strengt tatt er N = −5 for møter fra 2021, siden stemmen er ute 5 dager før møtet.
For de sakene som ikke er «practicable», og for regimet før 2021, kan vi regne **N = 1 som verste realistiske tilfelle**.
N = 7 eller mer er en stresstest. NBIMs egen praksis gir ikke grunnlag for å kalle det realistisk.
