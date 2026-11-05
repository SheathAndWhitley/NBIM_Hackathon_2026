# Case 1: generalprøve av demoen fra jury-zipen med stoppeklokke (#2493, smed3, 05.11 kl. 16.43–16.50)

Zip: `state/levering/c1_gronn/SISTE_GRONNE.zip` -> `jurypakke_c1_1642_bf0d3f8.zip`, sha256 `83c3fdb6…` (lik SHA256.txt).
Pakket ut i tom `/tmp/c1_generalprove_2493` med `env -i` og tom HOME (tom uv-buffer, uv fra /opt/homebrew/bin). Fulgte README steg 1–3 og deretter DEMO_MANUS.md ord for ord. Tmp er slettet etterpå. Ingen frosne filer rørt.

## Tider

| Steg | Kommando | Tid | Manus/README sier |
|---|---|---|---|
| 1 | `unzip jurypakke_c1.zip` (138 filer) | 0 s | – |
| 3 (før demoen) | `sh KJOR.sh` kald, tom uv-buffer | 43 s (uv sync 3 s, agent 40 s), FRYSVAKT GRØNN 15 filer, HOVEDTALL 0.476190, TALLVAKT GRØNN (169 påstander, 0 avvik) | «ett til to minutter», README 41–89 s |
| live 1 | `sh arbeid/hack/c1/leveranse/demo.sh` | 0,28 s | «under 1 s» |
| live 2 | `python3 -I arbeid/hack/c1/vis_manussaker.py ut/agent.csv` | 0,15 s (system-python3) | «0,03 s» |
| opplesing | 341 ord i de leste «»-blokkene (manus: 341; forskjellen er «» i Skjerm-linjene) | ikke målt med stemme | 2:20–2:40 |

uv-buffer etter kjøring: 233 MB i `home/.cache/uv`. uv fant Homebrew-Python 3.14 utenfor PATH, så ingen Python-nedlasting her. På en jurymaskin uten Python 3.13+ kommer ca. 70 MB i tillegg (README sier det).

## Tall og saker: manus mot skjerm

Alt i de leste linjene stemmer med det skjermen viser:
- `ut/agent.csv` sha256 `1543706f…` (manuset: samme sha for alle kalde kopier siden sak 2329). `pred_maaler.csv` `b113b545…`.
- vis_manussaker: **MANUS OK, linje 276 / 89 / 15**. Mobimo `2041367|21` MOT p_mot 1.0 til_menneske 0 punkt GVG 5.2 med sitatet ordrett; LOTTE `2048411|10` FOR p_mot 0.0896 til_menneske 0, NBIM 0.0.3-sitatet ordrett, fasit Against med «right to vote on fundamental changes»; Kura Sushi `2033470|1` MOT p_mot 0.5833 til_menneske 1, rutingsgrunn ordrett lik manus, GVG 1.1 (manusets sitat er en delsetning av punktteksten på skjermen, ordrett).
- demo.sh-hodet: F1 0.476190, MOT funnet 30, falsk MOT 38, mistet 28, presisjon 0.441, recall 0.517, 183 av 1539 (11,9 %), 58 i fasit. Alle lik manuset (0,476; 30 av 58; 44 %; 38; 28; 183/1539).
- Egen telling fra `ut/agent.csv` + real_votes (eget skript, ikke måleren): TP 30 FP 38 FN 28 P 0.4412 R 0.5172 F1 0.4762; **FN maskin 17 / menneske 11; FP maskin 0 / menneske 38**. Lik manusets «11 til et menneske, 17 ble FOR» og «alle 38 falske MOT til et menneske».
- «96 av 100»: `kilder/TREFFSIKKERHET.md:16` sier 96,2 % (1481 av 1539). Stemmer.
- «Ærlig hvis spurt»-merknaden stemmer: skjermen viser retningslinje NBIM 5.2.1 (årsrapporten) på Mobimo, og det er GVG 5.2-sitatet som bærer.
- Avrundinger som leses høyt (0,09 for 0.0896, 0,58 for 0.5833) er greie.

## Avvik (til dommer, ingen rettinger gjort)

1. **Medsendt `demo_utskrift.txt` i zipen er fra før frysen.** `arbeid/hack/c1/leveranse/demo_utskrift.txt` i pakka har linje 1 «2026-11-05 15:28, ny kald kopi i /tmp/c1_kald_2406» og linje 4 «FRYSVAKT: ikke frosset ennå (<repo>/state/c1_frys.json finnes ikke)». Manusets avslutning («Skjerm: tidsstempelet i linje 1 … viser at den kalde kjøringen ble gjort rett før demoen») holder bare hvis presentøren har kjørt demo.sh først; da overskrives fila (0 forekomster av ~ etterpå). Glemmes demo.sh, viser skjermen 15:28 og «ikke frosset ennå». Forslag: pakk neste zip etter en demo.sh-kjøring fra frosset pakke, eller la det stå og pass på rekkefølgen i manuset (KJOR.sh, demo.sh, vis_manussaker).
2. **Ingen GRØNN-status i demo-utskriften fra zipen.** I zipen skriver demo.sh linje 4 «tallvakt/frysvakt: se utskriften fra fremmed.sh (i jury-zipen: fra sh KJOR.sh)». FRYSVAKT/TALLVAKT GRØNN vises altså bare i KJOR.sh-utskriften, som er ferdig før de 3 minuttene. Vil presentøren vise grønt live, må terminalvinduet fra KJOR.sh stå igjen (siste tre linjer). Ikke en feil i manuset, men en skjermdetalj.
3. **Frysvakt-tellingen:** manuset (seksjonen «Etter modellfrys») sier FRYSVAKT GRØNN 17 filer, zipen sier 15 (målerne v2/v3 er unntatt i pakka, pakk_jury.sh steg 4). README skriver «…» og er riktig. Leses ikke høyt.
4. **Tallene 11/17 og 0/38 har ingen skjermkilde i zipen.** Manuset peker på `maaling.txt` og `telling.py` «i repoet, ikke i zipen». I zipen står tallene bare i tekst: `leveranse/JURY_SPORSMAL.md:31` og `leveranse/kilder/demo_saker.md:101`. Min egne telling over bekrefter dem fra agent.csv i pakka, så de er etterprøvbare, men juryen må telle selv. Forslag (ikke frosset, lav kost): legg `arbeid/oppgave_2267/telling.py` i neste zip, eller la demo_vis.py skrive FN/FP-fordelingen i hodet.
5. **Tid for vis_manussaker:** 0,15 s målt mot «0,03 s» i manuset. Uten betydning.

## Konklusjon
Demoen fra jury-zipen kjører som manuset sier, fra kald start på 43 s pluss under 0,5 s live, og hvert tall og hver sak i de leste linjene stemmer med skjermen. Det eneste som kan gi feil bilde på skjermen er den medsendte demo_utskrift.txt fra før frysen (avvik 1), som forsvinner så snart demo.sh kjøres i riktig rekkefølge.
