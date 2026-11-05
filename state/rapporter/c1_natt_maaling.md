# Case 1 natt: dommermåling av de selvrapporterte kandidatene (dommer2 #2880, 2026-11-05 19:46)

Måler: `arbeid/c1_natt/mal_kandidat.sh` (F1 MOT mot styret, oppgave_2567/maaler_aar.py --score mot), frossen repo4 ga de pinnede
tallene i alle kjøringer (exit 0). Referanse: c1_natt_referanse.md (#2878). Bytteregel #265/#281: snitt 2024-26 >= +0,02 over
frossen OG intet år (2023 medregnet) < -0,02. Ingen bytte her, dette er tall til 02:00-dommen (#2874).

| kandidat | 2023 (vakt) | 2024 | 2025 | 2026 | snitt 24-26 | diff snitt | verste år | dom | forsøk | selvrapportert |
|---|---|---|---|---|---|---|---|---|---|---|
| frossen repo4 | 0,3535 | 0,5057 | 0,5309 | 0,5120 | 0,5162 | 0 | | referanse | #1243 | |
| #2875 v1 likhet tfidf på midt+av (w=0 på val alle år) | 0,3736 | 0,5083 | 0,5276 | 0,5424 | 0,5261 | +0,0099 | 2025 -0,0033 | **STÅR** | #1252 | 0,5261 ✓ |
| #2875 v2 likhet MiniLM på midt+av (w 0/0,2/0) | 0,3736 | 0,5083 | 0,5119 | 0,5424 | 0,5209 | +0,0047 | 2025 -0,0190 | **STÅR** | #1253 | 0,5209 ✓ |
| #2871 tekstmal første-MOT oppå repo4 | 0,3535 | 0,5143 | 0,5309 | 0,5120 | 0,5191 | +0,0028 | 0,0000 | **STÅR** | #1254 | 0,5191 ✓ |
| #2881 regimeskifte K5 R0,3 D0,3 oppå repo4 | 0,4277* | 0,5057 | 0,5375 | 0,5203 | 0,5212 | +0,0050 | 2024 0,0000 | **STÅR** | #1255 | 0,5212 ✓ |
| #2881b av (#2701) + regimeskifte | 0,4371* | 0,5269 | 0,5443 | 0,5333 | **0,5349** | **+0,0187** | 2025 +0,0134 | **STÅR** | #1256 | 0,5349 ✓ |

Alle selvrapporterte tall er reprodusert på fjerde desimal. Svarmapper: `arbeid/oppgave_2880/k2875_tfidf`, `arbeid/oppgave_2880/k2875_emb`
(REGEL.md skrevet 19:45:33, filene kopiert etterpå fra oppgave_2875), `arbeid/c1_natt/fa`, `arbeid/oppgave_2881/svar`, `arbeid/oppgave_2881/svar_av`
(smed2s mapper, kjørt på nytt av dommer; DOM.md i hver).

## Dom per kandidat
- **#2875 likhet (smed):** val valgte w=0 i alle år for tfidf, så kandidaten ER lederen midt+av (#2703, #1246). Null ny informasjon på test.
  MiniLM-varianten valgte w=0,2 for 2025 på val og tapte 0,019 på test der: trekket generaliserer ikke. Sporet «likhet til tidligere
  MOT-forslag lagt på p_avvik» er lukket med to varianter. 2023-fila (0,3736) er identisk med test_2701/av_2023.csv, altså «av alene» uten midt.
- **#2871 tekstmal (smed2):** la til ett flagg (2024), som traff. Ærlig +0,0028, ingen risiko, ingen gevinst. Gruppe 1 er ikke nåbar slik.
- **#2881 regimeskifte (smed2):** fjerner aldri et riktig flagg i 2024-26 (0/2/2 flagg fjernet), +0,0050. 2023-tallet (+0,074) er tunet
  på 2023 selv og teller ikke.
- **#2881b av + regimeskifte (smed2):** beste natt-kandidat så langt, +0,0187, 0,0013 under kravet. Alle tre testår over frossen
  (+0,021/+0,013/+0,021). STÅR etter regelen. Merk for 02:00: den er bygd av to regler som hver er valgt på val, og 2023-vakta er
  in-sample for skift-delen. Et tredje ledd (avstå-regel, gruppe 5) må ha REGEL.md før måling og kan ikke velges på testårene.

## Til 02:00-dommen
Ingen kandidat fyller +0,02. Nærmest: #2881b (+0,0187). Lederen midt+av (#2703) står på +0,0099 og «av alene» (#2701) på +0,0135.
Kombinasjonen midt+av+skift er ikke målt; den må i så fall deklareres i REGEL.md før måling, ikke velges fordi tallene nå er sett.
