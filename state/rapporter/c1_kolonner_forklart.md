# Case 1: er hver kolonne i agent.csv forklart for juryen? (#2432, smed3, 05.11)

Grunnlag: `/tmp/k2377_0.15_0.85/ut/agent.csv` fra siste kalde kjøring (kjor_agent.py 05.11 15:09, 1578 rader, 19 kolonner).
Dokumenter juryen får i zipen: `README.md` (= levering/JURY_README.md), `c1/leveranse/README.md`, `JURY.md`,
`BEGRENSNINGER.md`, og det eldre laget `levering/*.md` (METODE, BESLUTNINGSSTOTTE, JURY_SPORSMAL, JURYSVAR, KRAVRESPONS).
Ingen kodeendring. Verdiene er telt i fila og sammenlignet med det dokumentasjonen sier.

## Tabell: kolonne, forklart hvor, stemmer verdiene

| kolonne | forklart hvor | verdier i fila | stemmer |
|---|---|---|---|
| id | ingen steder som kolonne (README «Egne saker» sier bare at meeting_id/item_no må være heltall) | `meeting_id\|item_no`, f.eks. `2031740\|1`, 1578 unike | ja, men ikke forklart |
| company | ingen steder | selskapsnavn fra arrangørens fil | selvforklarende, ikke forklart |
| meeting_date | ingen steder | ÅÅÅÅ-MM-DD | selvforklarende, ikke forklart |
| proposal_text | ingen steder | forslagsteksten, **kuttet til 200 tegn** (c1_real.py:277) | kuttingen står ingen steder |
| styret | ikke som kolonnenavn; JURY.md bruker «styrets anbefaling» | FOR 1564, MOT 14 | ja, men ikke forklart |
| anbefaling | README.md (jurypakke) linje 26; JURY.md | FOR 1496, MOT 82 (koden kan også gi `TIL MENNESKE` ved ugyldig styreverdi) | **nei, delvis**: README.md linje 3 sier «anbefaler FOR, MOT eller AVSTÅ», men fila har aldri AVSTÅ, og BEGRENSNINGER pkt. 6 / JURY.md pkt. 9 sier agenten aldri foreslår AVSTÅ |
| mot_styret | ingen steder som kolonne | 0/1, 71 ett-tall = KJORING.txt «MOT styret 71». 11 saker der styret selv sier MOT og agenten MOT får 0 (følger styret) | ja, men ikke forklart; dette er kolonnen hovedtallet telles på |
| p_mot | c1/leveranse/README.md linje 3 og 52 («kalibrert P(MOT)»); BESLUTNINGSSTOTTE.md «Slik leser du p_mot»; JURY_SPORSMAL.md spm. 8 | 0,0 til 1,0; laveste p_mot blant MOT-flagg 0,1912 (= kalibrert grense 0,191 i KJORING.txt) | **nei**: BESLUTNINGSSTOTTE.md linje 81 og JURY_SPORSMAL.md spm. 8 sier «flagger først fra p ≥ 0,919» og «bruk som rekkefølge, ikke prosent». 0,919 er den *rå* grensa (kolonnen raa_score), ikke p_mot. p_mot i fila er kalibrert (#2132) og flagget går ved 0,191. Leveranse-README og det eldre laget motsier hverandre |
| til_menneske | README.md linje 26; c1/leveranse/README.md 52; JURY.md pkt. 6 og 8; TREFFSIKKERHET.md 24 | 0/1, 188 ett-tall = JURY.md pkt. 8 «188 av 1578». 127 i båndet [0,15; 0,85) + 60 ukjent selskap + 1 instruks = 188 | ja |
| rutingsgrunn | nevnt ved navn i c1/leveranse/README.md 52 og KRAVRESPONS 61; grunnene beskrives i prose i JURY.md pkt. 6/8/9 | tom (1390) eller tekst, flere grunner skilt med «; ». Former i fila: «usikker: kalibrert P(MOT) 0.52 i båndet [0.15, 0.85)», «ukjent selskap: ingen NBIM-stemmer for selskapet før møtedatoen», «instruksjonslignende tekst i forslaget», og «kan ikke vurderes: …» ved datafeil | ja, men lista over mulige grunner står ikke samlet |
| punkt | METODE.md § 7 B (`punkt`, `sitat` = NBIMs egen begrunnelse fra en tidligere sak, rationale_section/text) | tom 1504; «GVG 1.1» (12), «GVG 3.3» (11) … | ja. Merk: c1/leveranse/README.md 52 («GVG-punkt og ordrett GVG-sitat») blander B (punkt/sitat, tidligere NBIM-begrunnelse) og A (retningslinje_*, ordrett GVG). Sitatet i `sitat` står *ikke* ordrett på nbim.no (METODE B) |
| sitat | METODE.md § 7 B | tom 1504, 20 unike tekster på de 74 MOT-radene = METODE «20 unike tekster på test» | ja |
| sitat_kilde | ingen steder | «NBIMs begrunnelse 2024, PT Rukun Raharja Tbk: «Approve Changes …»» (år, selskap, sak sitatet er hentet fra). JURY.md pkt. 6 kaller det «linja kilde: i demoen» | ikke forklart som kolonne |
| sitat_likhet | ingen steder | 0,399 til **1,4** på 74 rader. Det er TF-IDF-cosinus + 0,3 for samme sakstype + 0,1 for samme selskap (c1_real.py finn_sitat), altså ikke en sannsynlighet og kan overstige 1 | **ikke forklart, og lett å misforstå** som sannsynlighet |
| injeksjon_flagget | ikke som kolonne; vakta beskrives i JURY.md pkt. 6 og 11, BEGRENSNINGER pkt. 3 | 0/1, 1 ett-tall = KJORING.txt «1 med injeksjon» | ja, men ikke forklart |
| raa_score | bare i c1_real.py-docstring (ikke i noen .md) | 0,0085 til 0,9987; laveste blant MOT-flagg 0,92068 = rå grense 0,91885 i KJORING.txt. Det er denne BESLUTNINGSSTOTTE mener med «p ≥ 0,919» | verdiene stemmer, kolonnen er ikke forklart |
| retningslinje_id | METODE.md § 7 A; JURYSVAR.md 26 | 15 unike; «NBIM 0.0.3» på 1504 rader, konkret punkt på 74 = METODE «1504 … 74» og «dommeren talte 15» | ja |
| retningslinje_sitat | METODE.md § 7 A; JURYSVAR.md 26; BEGRENSNINGER pkt. 5 | aldri tom; ordrett GVG-avsnitt | ja |
| retningslinje_grunnlag | nevnt ved navn i METODE.md § 7 A, innholdet er ikke forklart | «følger styret: NBIMs utgangspunkt er å støtte styret» (1504) eller f.eks. «BM25 43.7; type DIRECTOR_ELECTION: 74/27 …» | ikke forklart hva tallene betyr |

Oppsummert: 7 kolonner er forklart og stemmer (til_menneske, punkt, sitat, retningslinje_id, retningslinje_sitat, p_mot-verdiene,
rutingsgrunn-verdiene). 9 kolonner står ingen steder som kolonne (id, company, meeting_date, proposal_text, styret, mot_styret,
sitat_kilde, sitat_likhet, raa_score). To steder sier dokumentasjonen noe som ikke stemmer med fila:

1. **p_mot-grensa:** BESLUTNINGSSTOTTE.md linje 81 og JURY_SPORSMAL.md spm. 8 («flagger fra p ≥ 0,919», «ikke prosent») gjelder
   raa_score, ikke p_mot. I fila er p_mot kalibrert og MOT-flagget starter ved 0,191. En jurymedlem som sorterer agent.csv på p_mot
   og leter etter 0,919 finner ingenting.
2. **AVSTÅ:** README.md (jurypakka) linje 3 sier agenten «anbefaler FOR, MOT eller AVSTÅ». Fila har aldri AVSTÅ, og BEGRENSNINGER pkt. 6 sier det rett ut.

## Ferdig tekst speider kan lime inn etter frysen (#1975)

Alt under er dokumentasjon, ingen kodeendring. Forslag: nytt avsnitt i `levering/JURY_README.md` (blir `README.md` i zipen) rett etter linja «Agentens svar ligger i `ut/` …».

```
## Kolonnene i `ut/agent.csv`
| kolonne | betydning |
|---|---|
| `id` | `meeting_id|item_no` fra arrangørens fil |
| `company`, `meeting_date`, `proposal_text` | fra inn-saken; `proposal_text` er kuttet til 200 tegn i utskriften (modellen leser hele) |
| `styret` | styrets anbefaling (mgmt_rec): FOR, MOT eller AVSTÅ |
| `anbefaling` | agentens forslag: FOR eller MOT (aldri AVSTÅ, se BEGRENSNINGER pkt. 6), eller `TIL MENNESKE` når styreverdien er ugyldig |
| `mot_styret` | 1 når anbefalingen er MOT og styret ikke selv sa MOT. Hovedtallet (F1) telles på denne kolonnen |
| `p_mot` | kalibrert sannsynlighet for MOT, 0 til 1 (isotonisk regresjon lært på val 2025). MOT-flagget går ved p_mot ≥ 0,191 |
| `raa_score` | modellens rå rangsnitt før kalibrering, 0 til 1, ikke en sannsynlighet. Rå grense 0,919; kalibreringen er monoton, så flaggene er de samme |
| `til_menneske` | 1 når saken skal til et menneske: p_mot i [0,15; 0,85), ukjent selskap, instruks i teksten, tomme eller rare felt, eller MOT uten sitat |
| `rutingsgrunn` | hvorfor, i klartekst, flere grunner skilt med «; ». Tom når agenten tar saken selv |
| `injeksjon_flagget` | 1 når forslagsteksten ligner en instruks til agenten (vakta i JURY.md pkt. 11); saken rutes |
| `retningslinje_id`, `retningslinje_sitat` | ordrett avsnitt fra NBIMs Global Voting Guidelines som ligner mest (FOR-saker får alltid NBIM 0.0.3, «support the board») |
| `retningslinje_grunnlag` | hvordan avsnittet ble valgt: BM25-skår, sakstype og hvor mange tidligere NBIM-begrunnelser av den typen som peker på samme seksjon |
| `punkt`, `sitat`, `sitat_kilde` | bare på MOT-flagg: NBIMs egen begrunnelse fra en lignende MOT-sak i et tidligere år (seksjon, tekst, og år/selskap/sak den kommer fra). Ekte NBIM-tekst, men ikke nødvendigvis ordrett lik dagens retningslinjer |
| `sitat_likhet` | hvor lik den tidligere saken er: TF-IDF-cosinus pluss 0,3 for samme sakstype og 0,1 for samme selskap, altså 0 til 1,4 og ikke en sannsynlighet |
```

To rettinger i eksisterende tekst:

- `levering/JURY_README.md` linje 3: bytt «anbefaler FOR, MOT eller AVSTÅ slik NBIM ville stemt» med
  «anbefaler FOR eller MOT slik NBIM ville stemt (aldri AVSTÅ, se BEGRENSNINGER.md pkt. 6)».
- `levering/BESLUTNINGSSTOTTE.md` linje 81 og `levering/JURY_SPORSMAL.md` spm. 8: legg til først i avsnittet:
  «Merk: tallet 0,919 er den rå modellskåren (`raa_score`). Kolonnen `p_mot` i agent.csv er kalibrert (#2132): der går
  MOT-flagget ved 0,191, og 0,15–0,85 er båndet som rutes til menneske. Rangeringen er den samme i begge.»

## Status 05.11 (#2439, smed3)
Kolonnetabellen og de to rettingene er lagt inn i `arbeid/hack/levering/JURY_README.md` (blir README.md i zipen) og
`arbeid/hack/levering/BESLUTNINGSSTOTTE.md`. Tallvakta er grønn på begge.

**Gjenstår for #1975 (speider), ikke gjort her fordi arkitekt #2435 retter i fila nå:** `levering/JURY_SPORSMAL.md` spm. 8
sier fortsatt «flagger fra p ≥ 0,919» og «ikke prosent». Legg til først i svaret:
«Merk: tallet 0,919 er den rå modellskåren (`raa_score`). Kolonnen `p_mot` i agent.csv er kalibrert (#2132): der går
MOT-flagget ved 0,191, og 0,15–0,85 er båndet som rutes til menneske. Rangeringen er den samme i begge.»

