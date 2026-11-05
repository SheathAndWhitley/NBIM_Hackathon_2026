# Dom #2507: rare inndata mot jury-zipen (#2499) – GODKJENT, tallene stemmer, fire svakheter til BEGRENSNINGER

**Dom:** Smed4s rapport (c1_rare_inndata.md) er riktig. Jeg bygde jury-zipen selv fra kald start og kjørte to av de rare filene. Akseptkravet holder: ingen krasj uten melding, ingen stille feil, alle tall i rapporten stemmer med det jeg så. Ingen av svakhetene krever endring i frosne filer. De fire under skal inn i BEGRENSNINGER (#2512), svakhet 3 og 5 også i NESTE_VERSJON.

## Hva jeg gjorde (05.11 kl. 16.27–16.31)
- `C1_JURYBYGG=/tmp/dommer2_2507/bygg C1_JURYSTAGE=/tmp/dommer2_2507/stage sh arbeid/hack/levering/pakk_jury.sh /tmp/dommer2_2507/jury.zip`: fremmed.sh HOVEDTALL 0.476190, «sha256 i pakka = frysfila», 129 filer. <!-- eldre: frossen #2044 (0,476), dagens hovedtall er repo4 0,512 -->
- Pakket ut, FRYSVAKT GRØNN (15 filer), `uv sync --frozen` i zipens egen .venv, så `kjor_agent.py` under `env -i` som i KJOR.sh. Skript: `<arbeidsmappe>/oppgave_2507/kjor_rare.sh`, full utskrift `<arbeidsmappe>/oppgave_2507/kjoring.log`.
- Innfiler fra smedens `<arbeidsmappe>/oppgave_2499/inn/`: **d** (semikolon-separert, 20 saker) og **e** (år 2027, 4 ukjente selskaper, 10 saker med ny type AI_GOVERNANCE).

## Tall: smedens rapport mot min kjøring
| fil | smed | dommer2 | likt |
|---|---|---|---|
| d: utgang | 0 | 0 | ja |
| d: til menneske / ikke vurderes / injeksjon | 20 / 20 / 0 | 20 / 20 / 0 | ja |
| d: rutingsgrunn | «mangler felt: meeting_id,item_no,…,proponent» | samme, 7 felt, på alle 20 | ja |
| d: rå grense | 0.91885 | 0.91885 | ja |
| e: utgang | 0 | 0 | ja |
| e: til menneske / ikke vurderes / injeksjon | 20 / 0 / 10 | 20 / 0 / 10 | ja |
| e: grunner | alle «ukjent selskap», 10 også «ukjent forslagstype AI_GOVERNANCE» + injeksjon | samme | ja |
| e: P(MOT) | 0,00–0,05 | 0,0–0,0896 (én sak 0,0896, resten ≤ 0,0455) | nesten: rapporten sier 0,05, maks er 0,09. Uten betydning, alle rutes |
| e: rå grense | 0.91896 | 0.91896 | ja |
| e: nye saker uten etikett | 20 | 20 | ja |

MOT styret = 0 i begge, ingen prediksjon uten flagg: hver av de 40 radene har `til_menneske=1` med grunn.

## Svakheter (smedens 1–4 bekreftet, pluss én fra meg)
1. 0-byte fil: meldingen «bare overskrift» er upresis, utgang 0. (ikke kjørt av meg, smedens logg er entydig)
2. Feil skilletegn / manglende kolonne stopper ikke: hver rad rutes med «mangler felt», ingen samlet melding om format. Bekreftet i d: id blir `rad1…rad20`, company/dato/tekst tomme.
3. Falsk injeksjonsgrunn på AI-saker: bekreftet i koden, `injeksjon_hoflig.py:21` har `ai` alene i `(agent|model|assistant|ai|llm|bot)` med `(?i)`. «Report on AI Risk Oversight» flagges. Trygt utfall (rutes), feil grunn.
4. P(MOT) avhenger litt av batchen (grense 0.91885 mot 0.91896 mellom d og e). Bekreftet.
5. **Ny:** på rader som ikke kan leses får `styret` og `anbefaling` verdien **FOR** i stedet for tomt (`c1_real.py:210`, `r.get("mgmt_rec") or "FOR"`). Rutes til menneske, så ingen stemme avgis, men et nedstrøms skript som bare leser `anbefaling` ser «FOR» på en sak agenten ikke har sett innholdet i. Bør stå i BEGRENSNINGER: «anbefaling gjelder bare når til_menneske=0».

## Ikke dekket
Bare d og e kjørt av meg (tidsboks). a, b, c, f, g, h, i er dømt på smedens logg (`<arbeidsmappe>/oppgave_2499/kjoring.log`), som er konsistent med det jeg reproduserte.
