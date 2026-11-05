# Case 1: agenten kjører fra kald start uten nett (sak 2412, smed, 05.11 ca. 15.35)

> **Eldre tall:** linjer merket «eldre frossen modell #2044» gjelder modellen som var frossen før byttet til repo4 (#2572). Målte tall er ikke endret. Dagens hovedtall står i `arbeid/hack/c1/tall_tabell.md`.

**Resultat: GRØNN.** Agenten trenger ikke nett og laster ikke ned noen modell.

## Hva ble kjørt
```
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 sandbox-exec -p '(version 1)(allow default)(deny network-outbound (remote ip))(deny network-inbound (local ip))' \
  sh arbeid/hack/levering/fremmed.sh /tmp/offline_2412
```
- Nettsperren er bevist først: `curl https://pypi.org` i samme sandbox gir «Couldn't connect» (utgang 7).
- Hele prosessen (kopi, `uv sync --frozen`, agent, målere, tallvakt) gikk med IP-nett sperret.
- Logg: `<arbeidsmappe>/oppgave_2412/offline_kjoring.log` (37 linjer).

## Tall
- Utgang 0. `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190` — uendret. <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
- Måler v3: P 0,4412, R 0,5172, TP 30 FP 38 FN 28. Til menneske 188 av 1578 (11,9 %). <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
- `TALLVAKT GRØNN`: 18 filer, 169 påstander, 0 avvik. Kjøring 70 s, uv sync 0 s.

## Ingen nedlastingsforsøk
- Loggen har ingen linjer med download/http/huggingface/connect.
- Agentfilene som kopieres (kjor_agent, c1_real, train.py miks h2, vern, case1_mot, målerne, tallvakta) inneholder ingen
  `transformers`, `huggingface`, `from_pretrained`, `torch`, `requests` eller `urllib`.
- Avhengighetene er bare lightgbm, matplotlib, pandas, scikit-learn, scipy (pyproject i smed2_c1_mot). Ingen torch/transformers i kopiens .venv.
- Den slettede modellcachen (sak 2400) var aldri i bruk av Case 1-agenten.

## Ett forbehold (ikke en feil i agenten)
`uv sync --frozen` gikk uten nett fordi hjulene ligger i uv-cachen på minien. En jury på egen maskin uten cache trenger nett én gang
for `uv sync` (pakker fra PyPI, låst i uv.lock), eller en ferdig .venv. Etter det kjører agenten helt uten nett.
Forslag hvis vi vil fjerne dette: nevn det i JURY_README («uv sync trenger nett én gang, agenten aldri»). Ingen frosne filer er rørt.

## Dommerens kontroll (sak 2414, dommer, 05.11 15:36)
**BEKREFTET.** Egen kjøring i ny mappe `/tmp/dommer_offline_2414`, samme sandbox-profil (deny network-outbound/inbound), `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`.
- Nettsperre bevist først i samme sandbox: `curl https://pypi.org` gir utgang 7 (Couldn't connect, 9 ms).
- `fremmed.sh` utgang 0. `HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190`. Måler v3: P 0,4412, R 0,5172, TP 30 FP 38 FN 28. <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 --> <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
- Til menneske 188 av 1578 (11,9 %). TALLVAKT GRØNN: 18 filer, 169 påstander, 0 avvik. Kjøring 29 s (smed 70 s, bare last på maskinen). <!-- eldre frossen modell #2044, ikke dagens hovedtall (repo4, se tall_tabell.md); tallvakt: ignorer -->
- `ut/pred_maaler.csv` og `ut/agent.csv` er bit-identiske med smedens (`cmp`; sha256 b113b545…).
- Uavhengig sjekk: kopiens .venv har ingen torch/transformers/huggingface/requests/urllib3/httpx. Ingen av de kopierte agentfilene
  importerer transformers, torch, requests, urllib, httpx eller socket. Loggen har ingen download/http/connect-linjer.
- Logg: `<arbeidsmappe>/oppgave_2414/offline_kjoring.log` (37 linjer).
- Frysvakta meldte «ikke frosset ennå» (kl. 15:3x, før frys 16). Smedens forbehold om `uv sync` (hjul fra uv-cachen; jury uten cache trenger nett én gang) står, og er ikke en feil i agenten.
Avvik: ingen.
