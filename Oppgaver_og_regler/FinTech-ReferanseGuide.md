## Innholdsfortegnelse

- [Erklæring om bruk av kunstig intelligens (AI)](#page-0)

- [Hva er FinTech](#page-0)

- [Introduksjon til Alpaca](#page-0)

- [Saldo](#page-0)

- [Noen Statistiske Verdier og Analyse](#page-0)

- [Teknisk og Fundamental Analyse](#page-0)

- [Maskinlæring på Historisk Markedsdata](#page-0)

- Modellvalidering og Evaluering [URL 🔗](#page-0)

- [Backtesting](#page-0)

## FinTech Referanseguide

## Erklæring om bruk av kunstig intelligens (AI)

Denne referanseguiden er laget med hjelp av kunstig intelligens (ChatGPT) til språk, struktur og forklaringer.

Alt innhold er gjennomgått og sjekket manuelt for å sikre at det er riktig og relevant.

Guiden er ikke ment som en fullstendig innføring i temaene i EikLab x FinTech, men som en enkel referanse

med viktige begreper, definisjoner og formler. Noen av temaene blir ikke forklart detaljert i videoserien, men er tatt med fordi de kan være nyttige senere.

## Hva er FinTech

## FinTech

Bruken av teknologi for å levere eller forbedre finansielle tjenester.

## Eksempel:

- 1. Vipps gjør det mulig å sende penger direkte mellom privatpersoner ved hjelp av mobiltelefonen.

- 2. Live Trading Platform automatiserer aksjehandel som brukes til automatisering av fond.

## API (Application Programming Interface)

Et sett med regler som gjør det mulig for ulike systemer å kommunisere med hverandre.

Eksempel: En handelsplattform bruker en API for å hente aksjepriser fra en børsleverandør.

## Algoritmisk Handel


Automatisert kjøp og salg av finansielle instrumenter basert på forhåndsdefinerte regler.

Eksempel: Et program kjøper aksjer når en teknisk indikator gir kjøpssignal.

## Blockchain

En distribuert database hvor transaksjoner lagres i sammenkoblede blokker.

Eksempel: Bitcoin-nettverket bruker blockchain til å registrere alle transaksjoner.

## Digital Lommebok (Digital Wallet)

Programvare som lagrer betalingsinformasjon og gjør elektroniske betalinger mulig.

Eksempel: Apple Wallet eller Google Wallet.

## Open Banking

Et rammeverk som lar tredjepartsaktører få tilgang til bankdata gjennom sikre API-er, etter samtykke fra

kunden.

Eksempel: En budsjettapp som automatisk henter kontotransaksjoner fra brukerens bank.

Peer-to-Peer (P2P)

En modell hvor brukere handler eller låner direkte med hverandre uten en tradisjonell mellommann.

Eksempel: En utlånsplattform der privatpersoner låner penger til andre privatpersoner.

## InsurTech

Bruk av teknologi for å forbedre forsikringsprodukter og forsikringsprosesser.

Eksempel: Automatisert behandling av forsikringskrav ved hjelp av kunstig intelligens.

## RegTech

Teknologiske løsninger som hjelper finansinstitusjoner med å overholde regulatoriske krav.

Eksempel: Automatisk overvåkning av transaksjoner for å oppdage hvitvasking.


## Kunstig Intelligens (AI)

Systemer som kan utføre oppgaver som normalt krever menneskelig intelligens.

Eksempel: En modell som analyserer markedsdata og estimerer sannsynligheten for fremtidige prisbevegelser.

## Machine Learning

En gren av kunstig intelligens hvor modeller lærer mønstre fra data.

Eksempel: En modell trenes på historiske aksjekurser for å predikere markedsretning.

## Introduksjon til Alpaca

## Alpaca

En plattform som tilbyr markedsdata og API-er for automatisert handel.

Eksempel: En Python-applikasjon bruker Alpaca for å hente aksjekurser og plassere ordre.

## Broker

En finansinstitusjon som utfører kjøps- og salgsordre på vegne av kunder.

Eksempel: Alpaca fungerer som broker når en bruker kjøper eller selger aksjer gjennom plattformen.

## Trading API

Et API som gjør det mulig å kommunisere med en handelsplattform gjennom kode.

Eksempel: Et Python-program sender en kjøpsordre til Alpaca via Trading API-en.

## Market Data API

Et API som gir tilgang til markedsdata som aksjekurser, volum og historiske priser.

Eksempel: Hente daglige sluttkurser for Apple de siste 5 årene.

## Historiske Markedsdata (Historical Data)

Tidligere registrerte markedspriser og handelsdata.


Eksempel: Aksjekurser for Tesla mellom 2020 og 2025.

## Sanntidsdata (Real-Time Data)

Markedsdata som oppdateres kontinuerlig mens markedet er åpent.

Eksempel: Visning av siste handlede pris for Nvidia-aksjen.

## Paper Trading

Simulert handel hvor ordre utføres med virtuelle penger.

Eksempel: Teste en handelsstrategi uten risiko for å tape ekte kapital.

## Live Trading

Handel som utføres med ekte penger i finansmarkedet.

Eksempel: Et handelssystem sender en ordre som faktisk kjøper aksjer i markedet.

## Handelskonto (Trading Account)

Kontoen som brukes til å holde kapital, posisjoner og handelsaktivitet.

Eksempel: En Alpaca-konto med \$10 000 i Paper Trading-kapital.

## Portefølje (Portfolio)

Samlingen av alle finansielle instrumenter som eies av en investor.

## Posisjon (Position)

En aktiv investering i et finansielt instrument.

Eksempel: Å eie 50 aksjer i Apple representerer en long-posisjon i Apple.

## Long Position

En posisjon som tjener penger dersom prisen stiger.

Eksempel: Kjøpe aksjer til \$100 med forventning om at prisen skal stige.


## Short Position

En posisjon som tjener penger dersom prisen faller.

Eksempel: Selge lånte aksjer til \$100 og kjøpe dem tilbake til \$90.

## Ordre (Order)

En instruksjon om å kjøpe eller selge et finansielt instrument.

## Market Order

En ordre som kjøper eller selger et verdipapir umiddelbart til beste tilgjengelige markedspris.

Eksempel: Kjøp 10 aksjer i Apple så raskt som mulig.

## Limit Order

En ordre som kun utføres dersom markedet når en spesifisert pris eller bedre.

Eksempel: Kjøp Apple-aksjer dersom prisen faller til \$180.

## Stop Order

En ordre som aktiveres når en forhåndsdefinert pris nås.

Eksempel: Selg en aksje dersom prisen faller under \$170.

## Stop Loss

En stop-ordre som brukes for å begrense tap.

Eksempel: En investor kjøper en aksje til \$100 og setter stop loss på \$90.

## Stop Limit Order

En kombinasjon av stop- og limit-ordre.

Eksempel: Når prisen faller til \$90 aktiveres ordren, men aksjen selges kun dersom prisen fortsatt er \$89 eller

høyere.

## Trailing Stop Order

En dynamisk stop-ordre som følger markedsprisen med en fast avstand.

Eksempel: En trailing stop på \$5 flyttes automatisk opp når aksjen stiger, men aldri ned.

Time in Force (TIF)


Regler som bestemmer hvor lenge en ordre skal være aktiv.

Eksempel: En ordre kan være gyldig kun samme handelsdag eller frem til den utføres.

## Day Order (DAY)

En ordre som kun er aktiv i inneværende handelssesjon.

Eksempel: En limit-ordre som ikke utføres før markedsstenging blir automatisk kansellert.

## Good Till Cancelled (GTC)

En ordre som forblir aktiv til den utføres eller kanselleres manuelt.

Eksempel: En limit-ordre på \$150 kan ligge aktiv i flere uker.

## Fill or Kill (FOK)

En ordre som må utføres umiddelbart og i sin helhet. Hvis ikke kanselleres hele ordren.

Eksempel: Kjøp 1 000 aksjer umiddelbart. Hvis alle aksjene ikke kan kjøpes med en gang, kanselleres ordren.

## Immediate or Cancel (IOC)

En ordre som forsøker å utføre så mye som mulig umiddelbart. Resten kanselleres.

Eksempel: Kjøp 1 000 aksjer. Dersom kun 700 er tilgjengelige kjøpes disse, mens de resterende 300

kanselleres.

## At the Open (OPG)

En ordre som sendes til markedet ved åpningen av neste handelssesjon.

Eksempel: Kjøp aksjer ved neste markedsåpning.

## At the Close (CLS)

En ordre som forsøker å utføres så nær markedsstenging som mulig.

Eksempel: Selg en posisjon ved slutten av handelsdagen.

## Ticker

Den unike identifikatoren som brukes for et verdipapir på en børs.

Eksempel: AAPL for Apple og TSLA for Tesla.

## Børs (Exchange)

Markedsplassen hvor finansielle instrumenter handles.


Eksempel: NASDAQ og New York Stock Exchange (NYSE).

## Markedsåpning (Market Open)

Tidspunktet hvor børsen starter handelsdagen.

Eksempel: NASDAQ åpner klokken 15:30 til 22:00 Norsk tid.

## API Request

En forespørsel sendt til et API.

Eksempel: Be Alpaca returnere historiske priser for AAPL.

## API Response

Dataene som returneres fra et API etter en forespørsel.

Eksempel: En liste med daglige aksjekurser.

## API Key

En unik identifikator som autentiserer en bruker mot et API.

## Secret Key

En privat nøkkel som brukes sammen med API Key for autentisering. Må aldri deles offentlig eller lagres i

GitHub-repositorier.

## Endpoint

En spesifikk URL som representerer en ressurs i et API.

Eksempel:

Et endpoint som returnerer kontoinformasjon.

## JSON

Et standardisert dataformat som ofte brukes i API-kommunikasjon.

Eksempel: En API-respons som inneholder prisdata strukturert som nøkkel-verdi-par.


## Saldo (Balance)

Cash

Kontanter tilgjengelig på kontoen som ikke er investert i åpne posisjoner.

Unrealized PnL

Gevinst eller tap på åpne posisjoner som ennå ikke er solgt:

## Equity

Verdien av kontoen etter at alle eiendeler og urealiserte gevinster/tap er tatt hensyn til:

## Daily Change

Prosentvis endring i kontoverdi siden forrige handelsdag:

Realized PnL

Gevinst eller tap som er låst inn ved at en posisjon er avsluttet:

## Initial Margin

Minimumskravet til egenkapital som kreves for å åpne en ny posisjon:

Maintenance Margin


Minimum egenkapital som må opprettholdes for å beholde en åpen posisjon:

Maintenance Margin = Position Value ×Maintenance Margin Requirement

## Margin Cushion

Hvor mye egenkapital som er tilgjengelig utover maintenance margin-kravet:

## Account Leverage

Forholdet mellom eksponering i markedet og egenkapital:

## Buying Power

Hvor stor markedsverdi som kan kjøpes med tilgjengelig kapital og margin:

## Noen Statistiske Verdier og Analyse

## Gjennomsnitt (Mean)

Gjennomsnittet representerer den sentrale verdien i et datasett og beregnes ved å summere alle

observasjoner og dele på antall observasjoner:

Varians (Variance)

Varians måler hvor mye observasjonene varierer rundt gjennomsnittet:


## Kvantil (Quantile)

En verdi som deler datasettet inn i bestemte andeler. Eksempelvis deler medianen (midterste verdien i et

sortert datasett) datasettet i to like store deler.

## Percentil (Percentile)

En verdi som angir hvilken prosentandel av observasjonene som ligger under en gitt verdi.

## Kovarians (Covariance)

Måler hvordan to variabler beveger seg sammen.

En positiv kovarians indikerer at variablene ofte beveger seg i samme retning, mens en negativ kovarians

indikerer motsatt bevegelse:

## Korrelasjon (Correlation)

Et standardisert mål på styrken og retningen til sammenhengen mellom to variabler. Korrelasjonen ligger alltid

mellom -1 og 1:

## Linjeplot (Line Plot)

Den vanligste visualiseringen av tidsserier hvor verdier plottes kronologisk over tid. Brukes ofte til å vise

prisutvikling for aksjer, valuta eller andre finansielle instrumenter.

## Scatter Plot

Visualisering hvor hver observasjon representeres som et punkt. Brukes ofte for å undersøke sammenhenger

mellom to variabler.

## Histogram

Visualisering av fordelingen til et datasett ved hjelp av intervaller (bins). Brukes ofte for å analysere

avkastningsfordelinger.


## Boksplot (Box Plot)

Visualisering som oppsummerer fordelingen gjennom median, kvartiler og outliers. Brukes ofte for å

identifisere ekstreme observasjoner.

## Candlestick Chart

En finansvisualisering som viser åpningspris, høyeste pris, laveste pris og sluttpris for hver tidsperiode. Brukes

mye innen teknisk analyse.

## Volumplot

Visualisering av handelsvolum over tid. Brukes ofte sammen med prisdata for å analysere markedsaktivitet.

## Rolling Statistics Plot

Visualisering av statistiske mål beregnet over et glidende vindu. Brukes ofte for å vise glidende gjennomsnitt

eller glidende volatilitet.

## Distribusjonsplot

Visualisering av sannsynlighetsfordelingen til et datasett. Brukes ofte for å undersøke avkastningsmønstre.

## Korrelasjonsmatrise (Correlation Matrix)

En tabell som viser korrelasjonen mellom alle variabler i et datasett. Hver celle inneholder korrelasjonen

mellom to variabler. Korrelasjonsmatriser brukes ofte for:

- Analyse av sammenhenger mellom aksjer

- Feature Engineering

- Dimensjonsreduksjon

- Risikoanalyse

- Identifisering av multikollinearitet

## Heatmap

En grafisk representasjon av en korrelasjonsmatrise hvor farger brukes for å visualisere styrken på

korrelasjonen. Sterke positive korrelasjoner vises ofte med én farge, mens sterke negative korrelasjoner vises


med en annen.

## Multikollinearitet

En situasjon hvor flere variabler er sterkt korrelerte med hverandre. Dette kan gjøre maskinlæringsmodeller mindre stabile og vanskeligere å tolke.

## Feature Selection

Prosessen med å velge hvilke variabler som skal brukes i videre analyse eller modellering. Korrelasjonsmatriser brukes ofte for å identifisere redundante variabler.

## Teknisk og Fundamental Analyse

## Teknisk Analyse

Teknisk analyse er studiet av historiske markedsdata, primært pris og volum, for å identifisere mønstre, trender og potensielle fremtidige prisbevegelser. Teknisk analyse bygger på antakelsen om at all tilgjengelig informasjon allerede er reflektert i markedsprisen.

## Fundamental Analyse

Fundamental analyse forsøker å estimere den virkelige verdien til et selskap ved å analysere økonomiske, finansielle og kvalitative faktorer.

Typiske faktorer inkluderer:

- Inntekter

- Overskudd

- Gjeld

- Kontantstrøm

- Ledelse

- Konkurransesituasjon

- Bransjeutvikling

## Hvorfor Fokusere på Teknisk Analyse?

Vi fokuserer primært på teknisk analyse fordi:

- Historiske prisdata er lett tilgjengelig gjennom API-er.

- Tekniske indikatorer kan beregnes automatisk.


- Tekniske indikatorer kan brukes som features i maskinlæring.

- Strategier basert på tekniske indikatorer er enkle å backteste.

- Teknisk analyse egner seg godt for automatisert handel.

Fundamental analyse er svært nyttig for langsiktige investeringer, men er ofte vanskeligere å automatisere og

oppdatere kontinuerlig.

## Likviditet (Liquidity)

Likviditet beskriver selskapets evne til å betale sine kortsiktige forpliktelser. Et selskap med høy likviditet har

normalt god betalingsevne på kort sikt.

## Current Ratio

Måler forholdet mellom omløpsmidler og kortsiktig gjeld:

## Quick Ratio

En strengere versjon av likviditetsmålet som ekskluderer varelager:

Stabilitet (Solvency)

Stabilitet beskriver selskapets evne til å håndtere langsiktig gjeld og overleve økonomiske utfordringer.

## Gjeldsgrad (Debt-to-Equity Ratio)

Måler forholdet mellom gjeld og egenkapital:

## Egenkapitalandel

Andelen av selskapets eiendeler som er finansiert med egenkapital:


## Lønnsomhet (Profitability)

Lønnsomhet beskriver selskapets evne til å generere overskudd.

## Netto Margin (Net Profit Margin)

Viser hvor stor andel av omsetningen som blir til overskudd:

## Return on Assets (ROA)

Måler hvor effektivt selskapet bruker sine eiendeler:

## Return on Equity (ROE)

Måler hvor effektivt selskapet genererer avkastning på egenkapitalen:

## Teknisk Indikator

En matematisk beregning basert på historiske markedsdata som brukes for å analysere markedsadferd.

Tekniske indikatorer brukes ofte til å:

- Identifisere trender

- Måle momentum

- Måle volatilitet

- Finne kjøps- og salgssignaler

- Bygge automatiserte strategier

Simple Moving Average (SMA)


Et glidende gjennomsnitt som beregner gjennomsnittsprisen over en bestemt periode. SMA brukes ofte for å

identifisere langsiktige trender:

## Exponential Moving Average (EMA)

Et glidende gjennomsnitt som gir nyere observasjoner høyere vekt. EMA reagerer raskere på nye

prisbevegelser enn SMA:

Relative Strength (RS)

Relative Strength er forholdet mellom gjennomsnittlig gevinst og gjennomsnittlig tap over en gitt periode. RS

brukes som grunnlaget for beregning av Relative Strength Index (RSI):

Relative Strength Index (RSI)

En momentumindikator som måler styrken i nylige prisbevegelser. RSI brukes ofte til å identifisere overkjøpte

og oversolgte markeder:

## MACD (Moving Average Convergence Divergence)

En momentum- og trendindikator basert på forskjellen mellom to eksponentielle glidende gjennomsnitt.

MACD brukes ofte for å identifisere trendendringer:

## Bollinger Bands

En volatilitetsindikator som består av et glidende gjennomsnitt og to standardavviksbånd. Bollinger Bands

brukes ofte til å identifisere perioder med høy eller lav volatilitet:

Lower Band = SMA− 2σ


## Average True Range (ATR)

En indikator som måler markedsvolatilitet. ATR brukes ofte til Risikohåndtering, Stop Loss-plassering og

Position Sizing:

Volume

Volum representerer antall enheter som handles i en gitt periode. Økende volum kan indikere sterkere

markedsinteresse.

## Volume Moving Average

Et glidende gjennomsnitt av volum. Brukes ofte for å avgjøre om dagens volum er høyere eller lavere enn

normalt.

## VWAP (Volume Weighted Average Price)

Gjennomsnittsprisen vektet etter handelsvolum. VWAP brukes mye av profesjonelle tradere og institusjoner:

## Momentum

Momentum beskriver hastigheten på prisbevegelser. Positivt momentum indikerer ofte styrke i markedet.:

## Mean Reversion

En teori som antar at priser har en tendens til å bevege seg tilbake mot sitt historiske gjennomsnitt.

Mean Reversion brukes ofte sammen med:

- Bollinger Bands

- RSI

- Z-Score


## Z-Score

En indikator som måler hvor langt en observasjon befinner seg fra gjennomsnittet målt i standardavvik:

## Trading Strategy

En trading strategi er et sett med forhåndsdefinerte regler som bestemmer når man skal kjøpe, selge eller

holde et finansielt instrument.

Strategier bygges ofte opp ved å kombinere flere tekniske indikatorer som analyserer ulike egenskaper ved

markedet.

Vanlige typer indikatorer:

- Trendindikatorer (SMA, EMA, MACD)

- Momentumindikatorer (RSI, Momentum)

- Volatilitetsindikatorer (Bollinger Bands, ATR)

- Volumindikatorer (Volume, VWAP)

En strategi kombinerer ofte flere indikatorer for å redusere falske signaler og øke sannsynligheten for gode

handler.

## Eksempel:

En strategi kan:

- Kjøpe når 50-dagers SMA er over 200-dagers SMA.

- Kreve at RSI er over 50.

- Bruke ATR til å beregne Stop Loss.

## Marked Før ≠ Marked Nå

Finansmarkedene endrer seg kontinuerlig over tid.

Strategier som fungerte godt historisk trenger ikke nødvendigvis fungere i fremtiden fordi markedsforholdene

stadig utvikler seg.

Årsaker til markedsendringer inkluderer:

- Endringer i renter

- Nye regulatoriske krav

- Teknologisk utvikling

- Geopolitiske hendelser

- Nye markedsaktører

- Endringer i investoradferd


Derfor er det viktig å:

Dette betyr at historiske mønstre kan svekkes eller forsvinne over tid.

En strategi som fungerte godt i ett markedsregime kan prestere dårlig i et annet.

- Evaluere strategier kontinuerlig

- Teste strategier på nye data

- Tilpasse modeller til endrede markedsforhold

- Unngå å anta at historisk ytelse garanterer fremtidige resultater

Denne utfordringen er en av hovedgrunnene til at Feature Engineering, Maskinlæring og kontinuerlig

modelloppdatering har blitt viktige verktøy innen moderne FinTech.

## Maskinlæring på Historisk Markedsdata

## Principal Component Analysis (PCA)

PCA er en metode for dimensjonsreduksjon som omgjør mange korrelerte variabler til et mindre antall

hovedkomponenter som bevarer mest mulig informasjon.

- Redusere antall features

- Fjerne redundante variabler

- Redusere støy i data

- Redusere multikollinearitet

PCA brukes ofte for å:

## Scikit-Learn

Scikit-Learn er et av de mest populære Python-bibliotekene for maskinlæring.

Biblioteket inneholder verktøy for:

- Datapreprosessering

- Feature Engineering

- Modelltrening

- Modellvalidering

- Evaluering

## Maskinlæringsmodell

data.

En maskinlæringsmodell er en algoritme som lærer mønstre fra historiske data for å gjøre prediksjoner på nye


Innen finans brukes modeller ofte til å:

- Predikere markedsretning

- Klassifisere kjøps- og salgssignaler

- Estimere risiko

## Logistic Regression

En klassifikasjonsmodell som estimerer sannsynligheten for at en observasjon tilhører en bestemt klasse.

Brukes ofte som et enkelt og tolkbart utgangspunkt.

## Random Forest

En modell som kombinerer mange beslutningstrær for å forbedre prediksjonskvaliteten.

Robust mot støy og mye brukt på tabulære data.

## Gradient Boosting

En modell som bygger flere svake modeller sekvensielt for å redusere feil.

Populær innen finans og maskinlæringskonkurranser.

## XGBoost

En optimalisert implementasjon av Gradient Boosting.

Kjent for høy ytelse på strukturerte datasett.

## CatBoost

CatBoost er en Gradient Boosting-modell som er spesielt utviklet for tabulære datasett og håndterer

kategoriske variabler effektivt.

Brukes ofte til:

- Klassifikasjon

- Regresjon

- Prediksjon på markedsdata


LightGBM er en Gradient Boosting-modell som er optimalisert for hastighet og skalerbarhet på store datasett.

## Brukes ofte til:

- Klassifikasjon

- Regresjon

- Finansiell modellering

## Artificial Neural Network (ANN)

ANN er et nevralt nettverk som lærer komplekse mønstre gjennom flere sammenkoblede lag av nevroner.

## Brukes ofte til:

- Klassifikasjon

- Regresjon

- Mønstergjenkjenning

## Convolutional Neural Network (CNN)

CNN er en type nevralt nettverk som er utviklet for å oppdage romlige mønstre i data.

## Brukes ofte til:

- Bildeanalyse

- Mønstergjenkjenning

- Finansielle heatmaps

## Recurrent Neural Network (RNN)

RNN er en type nevralt nettverk som er utviklet for sekvensielle data hvor tidligere observasjoner kan påvirke

fremtidige prediksjoner.

## Brukes ofte til:

- Tidsserier

- Sekvensanalyse

- Markedsdata

## Autoencoder

En Autoencoder er et nevralt nettverk som lærer å komprimere og rekonstruere data.

Brukes ofte til:


- Dimensjonsreduksjon

- Feature Engineering

- Anomalideteksjon

## Self-Attention

Self-Attention er en mekanisme som lar modellen vurdere hvor viktige ulike deler av en sekvens er i forhold til

hverandre.

Dette gjør det mulig for modellen å fokusere på de mest relevante observasjonene når en prediksjon

beregnes.

Brukes ofte til:

- Tidsserier

- Naturlig språkbehandling

- Finansielle sekvenser

## Transformer

Transformer er en modellarkitektur som er bygget rundt Self-Attention.

Modellen kan lære sammenhenger mellom observasjoner over lange tidsperioder uten å bruke rekursive

nettverk som RNN.

Brukes ofte til:

- Tidsserier

- Prediksjon

- Moderne AI-systemer

## Trening (Training)

Prosessen hvor modellen lærer sammenhenger mellom inputvariabler og målvariabelen ved hjelp av historiske

data.

## Treningssett (Training Set)

Datasettet som brukes til å lære opp modellen.

## Testsett (Test Set)

Datasettet som brukes for å evaluere modellens ytelse på usette data.


## Overfitting

Overfitting oppstår når modellen lærer treningsdataene for godt, inkludert tilfeldige mønstre og støy.

Resultatet er ofte svært gode resultater på treningsdata, men dårlig ytelse på nye data.

## Generalisering

Modellens evne til å prestere godt på nye og usette data.

God generalisering er ofte viktigere enn høy ytelse på treningsdata.

## Time Series Split

En valideringsmetode som bevarer tidsrekkefølgen i datasettet.

Tidligere observasjoner brukes til trening, mens senere observasjoner brukes til testing.

Dette er vanligvis mer realistisk for finansielle tidsserier enn tradisjonell kryssvalidering.

## K-Fold Cross Validation

En valideringsmetode hvor datasettet deles inn i flere deler som brukes vekselvis til trening og testing.

Metoden brukes ofte i maskinlæring, men er vanligvis mindre egnet for tidsserier fordi den bryter den

naturlige tidsrekkefølgen.

## Accuracy

Andelen korrekte prediksjoner gjort av modellen:

## Hvorfor er Accuracy viktig ved predikasjon av aksjer?

Accuracy gir et overordnet mål på hvor ofte modellen predikerer riktig retning i markedet. Dersom modellen

skal klassifisere om en aksje vil stige eller falle, viser Accuracy hvor stor andel av disse beslutningene som er korrekte.

Samtidig kan Accuracy være misvisende dersom datasettet er ubalansert. Hvis markedet for eksempel stiger

70 % av tiden, kan en modell som alltid predikerer "oppgang" oppnå høy Accuracy uten å ha reell prediktiv verdi. Derfor bør Accuracy vurderes sammen med andre evalueringsmål.


## Precision

Andelen positive prediksjoner som faktisk var positive:

## Hvorfor er Precision viktig ved predikasjon av aksjer?

Precision beskriver hvor pålitelige modellens kjøpssignaler er. En høy Precision innebærer at når modellen

predikerer at en aksje vil stige, skjer dette ofte i praksis.

Dette er særlig viktig dersom falske positive signaler er kostbare, ettersom hver feilaktige kjøpsbeslutning kan

føre til tap, transaksjonskostnader og redusert avkastning.

Recall

Andelen faktiske positive observasjoner som modellen klarte å identifisere:

## Hvorfor er Recall viktig ved predikasjon av aksjer?

Recall måler hvor godt modellen fanger opp de faktiske mulighetene i markedet. En høy Recall betyr at

modellen identifiserer mange av periodene hvor aksjen faktisk stiger.

Dette kan være verdifullt dersom målet er å utnytte flest mulig lønnsomme investeringsmuligheter. Ulempen

er at Recall ofte øker på bekostning av flere falske positive signaler.

F1-Score

Det harmoniske gjennomsnittet av Precision og Recall.

Brukes når begge målene er viktige:

## Hvorfor er F1-Score viktig ved predikasjon av aksjer?

F1-Score balanserer Precision og Recall i ett samlet mål. Dette er nyttig når både kvaliteten på kjøpssignalene

og evnen til å oppdage reelle markedsmuligheter er viktige.

Innen aksjeprediksjon gir F1-Score derfor et mer nyansert bilde av modellens prestasjon enn Accuracy alene,

spesielt ved ubalanserte datasett.


## Brier Score

Måler kvaliteten på sannsynlighetsprediksjoner.

Lavere verdi indikerer bedre kalibrerte sannsynligheter:

der:

- N er antall observasjoner,

- p i er modellens predikerte sannsynlighet,

- yi er den faktiske observasjonen (0 eller 1).

## Hvorfor er Brier Score viktig ved predikasjon av aksjer?

I finans er det ofte ikke nok å vite hvilken retning modellen predikerer; man ønsker også å vite hvor sikker

modellen er. Brier Score evaluerer hvor godt disse sannsynlighetene samsvarer med de faktiske utfallene.

Godt kalibrerte sannsynligheter kan brukes i risikostyring, porteføljeallokering og beslutninger om hvor store

posisjoner som bør tas.

## AUC-ROC

AUC (Area Under the Curve) er arealet under ROC-kurven (Receiver Operating Characteristic), som viser

forholdet mellom sann sann positiv-rate og falsk positiv-rate ved ulike klassifiseringsterskler.

ROC-kurven er definert ved:

AUC beregnes som arealet under denne kurven:

Verdier ligger mellom 0 og 1:

- AUC = 0.5 tilsvarer tilfeldig gjetning,

- AUC > 0.5 indikerer prediktiv evne,

- AUC = 1.0 representerer perfekt separasjon mellom klassene.

## Hvorfor er AUC-ROC viktig ved predikasjon av aksjer?

AUC-ROC måler modellens evne til å skille mellom perioder med oppgang og nedgang uavhengig av valgt

beslutningsterskel. Dette gjør metrikken spesielt nyttig når man ønsker å sammenligne ulike modeller før man bestemmer hvilken sannsynlighetsterskel som skal utløse kjøp eller salg.


En høy AUC indikerer at modellen generelt rangerer observasjoner korrekt ved å tilordne høyere sannsynlighet til faktiske oppgangsperioder enn til nedgangsperioder. Dette er verdifullt i finansielle anvendelser, hvor beslutningsregler og risikotoleranse ofte varierer mellom investorer og strategier.

## Confusion Matrix

En tabell som oppsummerer modellens klassifikasjoner.

## Består av:

- True Positive (TP)

- True Negative (TN)

- False Positive (FP)

- False Negative (FN)

Brukes for å forstå hvilke typer feil modellen gjør.

True Positive (TP)

Modellen predikerer positivt, og observasjonen er faktisk positiv.

## True Negative (TN)

Modellen predikerer negativt, og observasjonen er faktisk negativ.

## False Positive (FP)

Modellen predikerer positivt, men observasjonen er faktisk negativ.

## False Negative (FN)

Modellen predikerer negativt, men observasjonen er faktisk positiv.

## Walk-Forward Testing

En evalueringsmetode hvor modellen trenes på historiske data og testes på fremtidige perioder før vinduet flyttes fremover.

Metoden etterligner hvordan modellen ville blitt brukt i virkelige markeder.


## Look-Ahead Bias

Look-Ahead Bias oppstår når fremtidig informasjon utilsiktet brukes i modelltrening eller evaluering.

Dette kan føre til urealistisk gode resultater som ikke kan oppnås i praksis.

Eksempler:

- Bruke morgendagens pris i dagens feature.

- Normalisere data med informasjon fra fremtiden.

- Tilfeldig blande tidsseriedata før trening og testing.

## Backtesting

## Backtesting

Backtesting er prosessen med å teste en trading strategi på historiske markedsdata for å evaluere hvordan

strategien ville prestert tidligere.

Målet er å estimere strategiens ytelse før den brukes i live handel.

Total Return (%)

Total Return viser den totale prosentvise avkastningen strategien har generert gjennom backtest-perioden:

Final Value

Final Value representerer sluttverdien av porteføljen etter at backtesten er ferdig:

## Sharpe Ratio

Sharpe Ratio måler risikojustert avkastning ved å sammenligne avkastning med volatilitet.

Høyere Sharpe Ratio indikerer generelt bedre risikojustert ytelse:


## Drawdown

Drawdown beskriver hvor mye porteføljen har falt fra en tidligere toppverdi:

Maximum Drawdown (Max DD)

Maximum Drawdown er det største fallet porteføljen opplevde gjennom hele backtest-perioden:

## Trades

Antall handler som ble gjennomført i løpet av backtesten.

Brukes ofte for å evaluere hvor aktiv strategien er.

Win Rate (%)

Win Rate viser hvor stor andel av handler som endte med gevinst:

Benchmark

En benchmark er en referanse som brukes for å evaluere strategiens ytelse.

Vanlige benchmarks inkluderer:

- S&P 500

- Nasdaq 100

- MSCI World

## Benchmarking

Benchmarking er prosessen med å sammenligne strategiens resultater mot en benchmark.

Målet er å avgjøre om strategien faktisk tilfører verdi utover markedet.

Alpha


Alpha beskriver hvor mye en strategi har prestert bedre eller dårligere enn benchmarken:

## Position Sizing

Position Sizing er prosessen med å bestemme hvor stor en posisjon skal være i forhold til porteføljen.

God Position Sizing er en viktig del av risikohåndtering.

## Fixed Percentage Position Sizing

En metode hvor en fast prosentandel av porteføljen investeres i hver handel.

## Eksempel:

Investere 5 % av porteføljen i hver posisjon.

## Risk-Based Position Sizing

En metode hvor posisjonsstørrelsen bestemmes ut fra hvor mye kapital man er villig til å risikere.

Eksempel:

Risikere maksimalt 1 % av porteføljen per handel.

## Courtage

Courtage er gebyret som betales til megleren for å gjennomføre en handel.

Courtage reduserer den faktiske avkastningen til en strategi.

## Spread

Spread er forskjellen mellom kjøpsprisen (Ask) og salgsprisen (Bid):

## Slippage

Slippage oppstår når en ordre utføres til en annen pris enn forventet.

Dette skjer ofte ved:


- Høy volatilitet

- Lav likviditet

- Store ordr:

Slippage = Executed Price −Expected Price

## Transaksjonskostnader

Transaksjonskostnader er de totale kostnadene knyttet til handel.

Disse inkluderer ofte:

- Courtage

- Spread

- Slippage

Transaksjonskostnader bør alltid inkluderes i en realistisk backtest.
