# Case 1: tre vinkler for å finne avvik fra styret (arkitekt, #1964)

Testet på et øyeblikksbilde av `arbeid/hack/c1/data/votes.csv` tatt kl. 11:15: 513 421 rader, bare Vanguard, 2023–2026.
Fila vokste fra 21k rader mens jeg jobbet, fordi #1946 henter mer data.
Jeg fjernet duplikater per (utsteder, møtedato, forslag), og etiketten er flertallet av seriene.
Det ga 102 048 unike styrevalg, med basisrate for avvik 4,3 % (US 3,6 %).
Alle historikksignaler bruker bare møter strengt før datoen.
Testskript (kjører på 6 s): `python3 -I arbeid/oppgave_1964/test_vinkler.py arbeid/oppgave_1964/votes_snap.csv`.
Det viktigste: 85 % av avvikene er styrevalg, og de kommer i klynger.
83 % av avvikene ligger i møter med minst 2 avvik, og i et avviksmøte får 35 % av kandidatene MOT.
Det betyr at Vanguard straffer et styre for noe, ikke en enkeltperson.

## V1 Kontrollert selskap og dual-class (passer smed, #1958 felles kjennetegn)
- **Signal:** utstederen har flere CUSIP-er i N-PX, eller mangler ISIN.
  Stikkprøven av selskaper uten ISIN er typisk dual-class: Clover, Warby Parker, Berkshire.
  Fra Vanguards policy: stemme mot styremedlemmer, særlig leder av nominasjonskomiteen, når selskapet har ulik stemmerett uten solnedgangsklausul.
- **Ett-minutts test:** flere CUSIP gir 9,2 % avvik (n=7 652) mot 4,3 % i basis, altså 2,1x. I US er det 9,2 % mot 3,6 %.
- **Datakilde ut over N-PX:** EDGAR 10-K-forsiden (XBRL `dei:Security12bTitle`, ett element per klasse som er registrert) og ordet «controlled company» i 10-K eller DEF 14A. Å lese fra EDGAR er lov.
- **Bygg:** to binære kjennetegn per utsteder, `flere_klasser` og `kontrollert`, i felles tabell.

## V2 Styrets egen syndeliste: tidligere avvik og lønn (passer smed2, lgbm)
- **Signal:** utstederen har tidligere fått avvik fra Vanguard (alle forslag), eller tidligere avvik på say-on-pay.
  Dette er utstedernivå. Det er ikke samme spor som speiderens «direktøren fikk MOT i et annet styre».
- **Ett-minutts test:**
  - Tidligere avvik hos utstederen: 10,3 % (n=13 951) mot 3,7 % for utstedere med tidligere møte uten avvik.
  - Tidligere say-on-pay-avvik: 9,7 % (n=4 167) mot 2,4 % når say-on-pay alltid fulgte styret.
  - Samme person med tidligere avvik: 16,4 % (n=4 234), men det sporet er speiderens.
- **Fra lønnsvinkelen:** et møte uten say-on-pay har 8,7 % mot 2,2 %. Det henger sammen med få direktører i møtet, se V3.
- **Bygg:** `utsteder_tidl_avvik`, `utsteder_tidl_sop_avvik`, `dager_siden_siste_avvik`. Kombinert med V1 og V3 (tabellen under) gir det 8x spredning.

## V3 Regelmotor fra Vanguards policy: klassedelt styre og komitéledere (passer smed3, sitatagent)
- **Signal:** få direktører på valg i samme møte (≤6). Det er en grov stedfortreder for klassedelt styre eller lite selskap.
  Policyen sier: stem mot lederen av governance-komiteen ved klassedelt styre, krav om supermajoritet eller giftpille uten aksjonærgodkjenning.
- **Ett-minutts test:** ≤6 direktører gir 7,7 % (n=26 146) mot 2,8–3,3 % ved 7 eller flere. I US er det 7,1 % mot 3,6 %.
  Ordet «Class I/II/III» i forslagsteksten gir lite (4,2 %).
  Supermajority- eller declassify-forslag i samme møte gir lavere rate (0,9 % og 3,9 %), fordi selskapet allerede er i ferd med å rette det.
- **Datakilde:** DEF 14A (komitémedlemskap og leder per kandidat, klassedelt styre ja/nei, giftpille). Da kan regelen peke på hvilken direktør i møtet som får MOT. Det er nettopp de 35 % innen avviksmøtet, og agenten kan sitere policy-punktet.

## Kombinert (V1 × V2 × V3, styrevalg)
| få dir | flere CUSIP | tidl. avvik | n | avvik |
|---|---|---|---|---|
| 0 | 0 | 0 | 63 587 | 2,1 % |
| 0 | 0 | 1 | 7 671 | 8,9 % |
| 1 | 0 | 0 | 19 046 | 6,2 % |
| 1 | 1 | 0 | 1 987 | 11,2 % |
| 1 | 0 | 1 | 4 092 | 10,8 % |
| 1 | 1 | 1 | 1 021 | 16,7 % |

KP: forventet basisrate 1,7 % (beslutningsnotatet, alle hovedposter). Jeg fikk 4,3 % på styrevalg og 5,3 % på andre selskapsforslag.
Avviket kommer av at datasettet nå er større og jeg deduperer annerledes, så nivåene er ikke direkte sammenlignbare med holdout i måler v2.
Løftene er relative og strengt tidsriktige, men **ikke målt med måler v2**. Dommeren må måle dem.

## Lukket med tall
- **Overboarding via navnetelling i N-PX:** 3+ verv gir 3,9 % mot 4,7 % for 1 verv. Ingen signal. Navnene er for støyete, og Vanguard har myket opp grensen. Ikke bygg.
- **Land via ISIN:** utenlandske utstedere har nesten aldri avvik (IE 0,1 %, GB 0,3 %, CA 1,2 %). Det er nyttig som negativt kjennetegn, men ikke en egen vinkel.

## Trukket vinkel (#156): «bytt rekkefølgen på stegene»
Steg 1 er å predikere avviksmøtet. 12,3 % av møtene har avvik, og V1–V3 er kjennetegn på møtenivå.
Steg 2 er å velge direktører innen møtet, med 35 % MOT der. Bare 10,7 % av avviksmøtene har MOT på alle.
Tallene viser at det meste av løftet ligger på møtenivå. Anbefaling til smed2: tren et lgbm på møtenivå, gang det med en rangering innen møtet, og bruk DEF 14A-komitédata når de finnes.

## Anbefaling
Bygg V2 først, fordi den er gratis fra votes.csv og gir 2,7–4x. Så V1, med ett kall per utsteder mot EDGAR-forsiden. V3 med DEF 14A går til smed3 sitt sitat.
