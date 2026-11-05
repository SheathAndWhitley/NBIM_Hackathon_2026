## Hackathon 2026 regler, leveranse og bedømmingskriterier

Gjelder begge caser (1 & 2). Dette dokumentet er bevisst kort og skal deles med teamene før start, sammen

med casebeskrivelsene.

## 1. Hva som faktisk bedømmes

Ikke hvem som har den mest treffsikre modellen. Vi bedømmer om teamet har forstått problemet, om

resultatet er etterprøvbart, og om en beslutningstaker kan bruke det.

Et team som leverer en enkel modell med ærlig evaluering og erklærte begrensninger rangeres over et team

som leverer en avansert modell uten baseline.

## 2. Leveranse per team

Tre ting, ikke mer:

- 1. Demo på 5 minutter. Helst kjørende løsning.

- Kravrespons, maks 1 side. Mal i punkt 3. Dette er den viktigste leveransen (dashboard eller 1 slide-presentasjon av funn).

- 2. Kode. Repo eller mappe som kan kjøres av en annen person. README med ett kommandolinjekall som reproduserer hovedresultatet.

- 3. Hvor? Send lenke til Repo eller del zippet mappe til milad.tootoonchi@nmbu.no

Etter demoen: 5 minutter spørsmål fra juryen. Se punkt 7.

## 3. Kravrespons (mal)

Fem overskrifter, 3–5 setninger under hver. Ingen markedsføring.

```
Hva vi bygde (2 min)
Hva løsningen gjør, hvilken beslutning den støtter og resultat.
Hvordan vi verifiserte det (2 min)
Fasit, målvariabel, baseline, og tallene. Oppgi hvilken metrikk og hvorfor.
Hva vi ville trengt videre (1 min)
Data, tid eller tilgang vi manglet.
```

## 4. Bedømmingskriterier

Poeng 0–10 per kriterium, der beste besvarelse settes til 10 og øvrige vurderes relativt til den.


| Kriterium | Vekt Hva som gir poeng |   |
| --- | --- | --- |
| Problemforståelse og | 30 | Valg av målvariabel og hvorfor. Avgrensning. At teamet forstår |
| metodevalg | % | hvilken beslutning løsningen støtter. |
| Evaluering og | 30 | Baseline oppgitt og slått. Riktig metrikk for problemet. Fasit brukt. |
| etterprøvbarhet | % | Resultatet kan reproduseres. |
| Beslutningsstøtte og | 20 | En beslutningstaker kan forstå og overprøve et enkeltresultat |
| forklarbarhet | % | innenfor tidsbudsjettet i caset. |
| Robusthet og styring | 20 | Motstandstesten i punkt 6 gjennomført. Sporbarhet i hva løsningen |
|   | % | gjorde. Erklærte begrensninger. |

## Dette trekker ned

- Demo på håndplukkede eksempler uten evaluering på et holdout-sett.

- Skjult datalekkasje: framtidig informasjon i treningsdata, eller tilfeldig train/test-splitt på tidsseriedata.

- Påstander om ytelse som ikke kan reproduseres fra koden.

- Løsning som utfører irreversible handlinger uten at det logges eller bekreftes.

## 5. Felles regler

- Data: kun åpne eller syntetiske kilder. Ingen interne data fra oppdragsgiver. Kildene skal oppgis med URL i README.

- AI-verktøy: tillatt og forventet. Teamet skal oppgi hvilke verktøy som ble brukt og til hva i README. Bruk av AI trekker ikke ned, uoppgitt bruk gjør det.

- Tid: 24 timer. Ingen innlevering etter frist.

- Teamstørrelse: 3 – 5.

- Ekstern kode: åpne biblioteker og forhåndstrente modeller er tillatt. Kopiert prosjektkode skal krediteres i README.

## 6. Juryens spørsmål

Alle team får de samme fem spørsmålene. De deles ut på forhånd. Poenget er ikke å overraske, men å gi rom

for å vise resonnement.

- 1. Hvorfor valgte dere den målvariabelen, og hva var alternativene?

- 2. Ville dere ha turt å sette resultatet deres i produksjon?

- 3. Med én uke til, hva ville dere gjort først?

Til juryen: sett av minst 5 minutter til dette per team, og la minst én person med fagbakgrunn fra data eller

risiko stille spørsmålene. Det er her forskjellen mellom et polert prosjekt og en sterk kandidat blir synlig. En femminutters demo belønner selvtillit, oppfølgingsspørsmål belønner kaliber.

## 7. Datatilgang, status per 20. august 2026

Verifisert mot kildenes egen dokumentasjon. Se startpakke/ for kode.


| Kilde | Status | Merknad |
| --- | --- | --- |
| SEC EDGAR API-er | Åpen. Ingen | Krever User-Agent-header med kontaktinfo. Ingen CORS. |
| (data.sec.gov) | nøkkel. |   |
| SEC Financial | Åpen. 2009 Q1 | Kvartalsvise ZIP: |
| Statement Data Sets | – 2026 Q1. | https://www.sec.gov/files/dera/data/financial- |
|   |   | statement-data-sets/YYYYqQ.zip |
| SEC Form N-PX | Åpen, | Påbudt format fra første rapport 31. august 2024. Inneholder |
| (stemmegivning) | strukturert | utsteder, CUSIP, forslagstekst ordrett fra stemmeseddelen, |
|   | XML. | kategori, stemmeretning og antall aksjer. |
| SEC AAER | Åpen, men | 3 340 saker tilbake til 1965. HTML-tabell med paginering og |
| (håndhevingssaker) | ikke | RSS-feed. Kobling fra navn til CIK må bygges selv, se punkt |
|   | maskinlesbar. | under. |
| NBIM |   | Søkbar tabell på nettsiden, «API-tilgang på forespørsel». Ingen |
| stemmedatabase | Ikke åpen. | dokumentert eksport. Må avklares med oppdragsgiver i god tid, |
|   |   | og kan ikke være kritisk sti. |
