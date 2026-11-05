# Case 1: stemmeagenten, klar til å kjøres alene

**Kilder, kreditering og AI-bruk:** se `arbeid/hack/c1/leveranse/README.md`, avsnittene «Datakilder» og «AI-verktøy».

Agenten leser en generalforsamlingssak og anbefaler FOR eller MOT slik NBIM ville stemt (aldri AVSTÅ, se BEGRENSNINGER.md pkt. 6), siterer
NBIMs retningslinjer og sender usikre saker til et menneske. Hovedtallet er F1 på stemmer **mot styret**
på test 2026 (NBIMs egne stemmer fra arrangøren): **0.512000**. «Følg styret» har F1 0 på MOT.

## Det du trenger
macOS eller Linux med [uv](https://docs.astral.sh/uv/)
(`curl -LsSf https://astral.sh/uv/install.sh | sh`). Første kjøring trenger nett én gang og laster ned ca. 80 MB låste pakker (ca. 230 MB pakket ut)
(pluss ca. 70 MB Python hvis uv ikke finner Python 3.13+; uv henter den selv). Testet fra tom uv-cache og uten Python:
hele kjøringen tok ett til to minutter på vår maskin (nedlasting 3–20 s, totalt 41–89 s, varierer med last),
alltid samme hovedtall. På en treg linje tar nedlastingen lengre tid.

## Kjør (ord for ord)
1. `unzip jurypakke_c1*.zip` (fila du fikk; navnet kan slutte med klokkeslett og commit, f.eks. `jurypakke_c1_1930_abc1234.zip`)
2. `cd c1_stemmeagent`
3. `sh KJOR.sh`

Det skal ta et par minutter (pluss nedlastingen første gang), og slutte med:

    FRYSVAKT GRØNN: … frosne filer har samme sha256 som ved pakking
    HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000
    TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring

`SCORE`-linjene midt i utskriften er avvik fra styret inkludert AVSTÅ (sidetall, 0.529412), ikke hovedtallet.
Linja som starter med `IKKE HOVEDTALL` er en sjekk med test-fordelingen, ikke resultatet.
Agentens svar ligger i `ut/` (`agent.csv` med anbefaling, sitat og til_menneske per sak).

### Kolonnene i `ut/agent.csv`
| kolonne | betydning |
|---|---|
| `id` | `meeting_id|item_no` fra arrangørens fil |
| `company`, `meeting_date`, `proposal_text` | fra inn-saken; `proposal_text` er kuttet til 200 tegn i utskriften (modellen leser hele) |
| `styret` | styrets anbefaling (mgmt_rec): FOR, MOT eller AVSTÅ |
| `anbefaling` | agentens forslag: FOR eller MOT (aldri AVSTÅ, se BEGRENSNINGER.md pkt. 6), eller `TIL MENNESKE` når styreverdien er ugyldig |
| `mot_styret` | 1 når anbefalingen er MOT og styret ikke selv sa MOT. Hovedtallet (F1) telles på denne kolonnen |
| `p_mot` | kalibrert sannsynlighet for MOT, 0 til 1 (isotonisk regresjon lært på val 2025). MOT-flagget går ved p_mot ≥ 0,232 |
| `raa_score` | modellens rå rangsnitt før kalibrering, 0 til 1, ikke en sannsynlighet. Rå grense 0,923; kalibreringen er monoton, så flaggene er de samme |
| `til_menneske` | 1 når saken skal til et menneske: p_mot i [0,15; 0,85), ukjent selskap, instruks i teksten, tomme eller rare felt, eller MOT uten sitat |
| `rutingsgrunn` | hvorfor, i klartekst, flere grunner skilt med «; ». Tom når agenten tar saken selv |
| `injeksjon_flagget` | 1 når forslagsteksten ligner en instruks til agenten (vakta i JURY.md pkt. 11); saken rutes |
| `retningslinje_id`, `retningslinje_sitat` | ordrett avsnitt fra NBIMs Global Voting Guidelines som ligner mest (FOR-saker får alltid NBIM 0.0.3, «support the board») |
| `retningslinje_grunnlag` | hvordan avsnittet ble valgt: BM25-skår, sakstype og hvor mange tidligere NBIM-begrunnelser av den typen som peker på samme seksjon |
| `punkt`, `sitat`, `sitat_kilde` | bare på MOT-flagg: NBIMs egen begrunnelse fra en lignende MOT-sak i et tidligere år (seksjon, tekst, og år/selskap/sak den kommer fra). Ekte NBIM-tekst, men ikke nødvendigvis ordrett lik dagens retningslinjer |
| `sitat_likhet` | hvor lik den tidligere saken er: TF-IDF-cosinus pluss 0,3 for samme sakstype og 0,1 for samme selskap, altså 0 til 1,4 og ikke en sannsynlighet |

4. Uavhengig telling (valgfritt, etter steg 3): `sh arbeid/hack/levering/sjekk_treffsikkerhet.sh /tmp/c1_sjekk`
   Kjører agenten på nytt og teller 2x2 selv mot fasit, uten måleren. Forventet
   `TP 32 FP 35 FN 26 TN 1446 … STEMMER` og `sha256 … LIK`.

## Egne saker
    .venv/bin/python arbeid/hack/levering/kjor_agent.py --help

`meeting_id`, `item_no` og `company_id` må være heltall (ellers går saken til menneske som «kan ikke vurderes»). Eksempel:

    .venv/bin/python arbeid/hack/levering/kjor_agent.py --sak '{"meeting_id":9000001,"item_no":3,"company_id":537900,"meeting_date":"2026-05-01","proposal_text":"Shareholder Proposal Regarding Report on Climate Lobbying","proposal_type":"SHAREHOLDER","proponent":"Shareholder","mgmt_rec":"AGAINST","country":"United States","market":"DM"}' --ut ut_egen

gir (i `ut_egen/agent.csv`) P(MOT) 0,52, sendes til menneske, retningslinje NBIM 5.3.1 sitert.

## Hva som er hva
| fil | innhold |
|---|---|
| `arbeid/hack/c1/leveranse/` | kravrespons.md, JURY.md, README.md, BEGRENSNINGER.md, ERLIG_EVALUERING.md og `kilder/` (rapportene tallene kommer fra) |
| `arbeid/hack/levering/*.md` | metode, treffsikkerhet, beslutningsstøtte, jurysvar (eldre lag; der de peker på `state/rapporter/…` er det utviklingsrapporter som ikke er med i zipen, fire av dem ligger under `kilder/` med samme navn) |
| `arbeid/hack/levering/kjor_agent.py` | agenten |
| `arbeid/oppgave_2044/train.py` | grunnmodellen miks h2 (eldre frossen, 0,476); levert modell er repo4 = miks h2 + 4 historikktrekk (`arbeid/hack/levering/modell_repo4.py`, 0,512), trenes fra rådata ved hver kjøring |
| `state/opplastet/20261105_114241_real_votes.csv` | arrangørens data (målerne sjekker sha256) |
| `arbeid/hack/c1/maaler_offisiell_v3.py` | måleren for hovedtallet. Eneste endring fra originalen: datastien er relativ til fila |
| `FROSNE_SHA256.txt` | sha256 for de frosne filene (modell, prediksjoner, agent, data) |

Stier i noen rapporter under `kilder/` nevner utviklingsmaskinen (`~/...`); kjøringen leser dem ikke.
Gjenskapingsskript for enkelte delrapporter (ablasjoner, demo) trenger hele utviklingsmappa og er ikke med.
