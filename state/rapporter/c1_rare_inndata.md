# Case 1: den frosne jury-zipen med rare inndata på filnivå (smed4, #2499, 05.11 kl. 16.19–16.30)

**Svar:** Akseptkravet er oppfylt. Ingen av de 9 kjøringene krasjer stille. Agenten gir enten tydelig feilmelding (utgang 3) eller svar der alle rare saker er flagget til menneske. Jeg fant tre svakheter. Ingen av dem gir en stille feil stemme, og ingen er rettet, siden filene er frosset. Dommeren avgjør om de skal inn i BEGRENSNINGER/NESTE_VERSJON.

## Oppsett
- Fersk zip: `sh arbeid/hack/levering/pakk_jury.sh /tmp/smed4_2499/jury.zip` (117 filer, «sha256 i pakka = frysfila»). Pakket ut og kjørt med `uv sync --frozen` i zipens egen .venv.
- Hver kjøring (som KJOR.sh, under `env -i`): `env -i HOME=$R/home PATH=$R/.venv/bin:/usr/bin:/bin LANG=C.UTF-8 $R/.venv/bin/python $R/arbeid/hack/levering/kjor_agent.py --ut DIR --csv FIL [--historikk FIL]`, der `R` er `/tmp/smed4_2499/ut/c1_stemmeagent`.
- Innfilene ligger i `arbeid/oppgave_2499/inn/` og full utskrift i `arbeid/oppgave_2499/kjoring.log`.
- Jeg har ikke gjentatt dette: de 16+16 injeksjonene (c1_motstand_etter_frys.md) og radnivå-sakene i #2202 og #2257 (tom tekst, ukjent selskap, ukjent land, rar dato, osv.). Her testes **hele filer**.

## Tilfellene
| # | inndata | utgang | hva agenten sier | ok? |
|---|---|---|---|---|
| a | tom fil, 0 byte | 0 | `advarsel: inn-fila har ingen saker (bare overskrift); skriver tom agent.csv`, 0 saker | ja, men teksten er feil (se 1) |
| b | bare overskriftslinje | 0 | samme advarsel, tom agent.csv | ja |
| c | kolonnen `proposal_type` mangler (20 saker) | 0 | 20/20 til menneske, `kan ikke vurderes: mangler felt: proposal_type` | ja, men ingen samlet feilmelding (se 2) |
| d | semikolon-separert CSV (Excel-norsk, 20 saker) | 0 | 20/20 til menneske, `mangler felt: meeting_id,item_no,…,proponent` | ja, men ingen hint om skilletegnet (se 2) |
| e | helt nytt år 2027: 4 ukjente selskaper, og på 10 av 20 en ny sakstype `AI_GOVERNANCE` | 0 | 20/20 til menneske. Alle har `ukjent selskap`, de 10 nye har også `ukjent forslagstype «AI_GOVERNANCE»`, P(MOT) 0,00–0,05 | ja, men de 10 har også en falsk injeksjonsgrunn (se 3) |
| f | `--historikk` med tom historikkfil (bare overskrift) | 3 | `FEIL DATAFIL: forventet sha256 71ba5135… og 13757 rader …, fikk … 0 rader` | ja, tydelig |
| g | `--historikk` peker på en fil som ikke finnes | 3 | `FEIL DATAFIL: kan ikke lese …: [Errno 2] No such file or directory` | ja, tydelig |
| h/i | 200 ekte testsaker alene, og de samme 200 + de 20 rare sakene fra e | 0 / 0 | samme 6 MOT, samme ruting på de 200. 46 av 200 får en litt annen P(MOT), maks 0,0072, og rå grense går fra 0,91885 til 0,91896 | ja (se 4) |

## Svakheter (meldes, ikke rettet)
1. **Tom fil (0 byte)** gir meldingen «bare overskrift». Den er ufarlig, men upresis. Utgang 0 med tom agent.csv kan se ut som en vellykket kjøring for et skript som bare sjekker utgangskoden.
2. **Manglende kolonne og feil skilletegn** stopper ikke kjøringen. Agenten ruter i stedet hver rad til menneske med «mangler felt». Det er trygt, siden ingen stemme blir avgitt. Men en hel fil med feil format burde gi én tydelig feilmelding om kolonnene (f.eks. «fant kolonnen `id;injection_flag;…`, er fila semikolon-separert?»). Ellers får mennesket 1500 saker å se på.
3. **Falsk injeksjonsflagg på AI-saker:** «Shareholder Proposal Regarding Report on AI Risk Oversight» blir flagget som instruksjonslignende, fordi regexen i `injeksjon_hoflig.py:21` treffer ordet `ai`. Hverken real_votes eller test 2026 har tekster med «AI», så tallene er ikke påvirket (F1 0,476 står). Men AI-forslag fra aksjonærer blir vanligere, og alle sånne vil gå til menneske med feil grunn. Det trygge utfallet er riktig (de rutes), men grunnen er misvisende.
4. **P(MOT) avhenger litt av resten av fila:** «nye saker lagt til uten etikett» gir litt andre tall (maks 0,007), og grensa flytter seg med 0,0001. Ingen avgjørelse eller ruting endret seg på de 200 sakene. Det betyr likevel at samme sak ikke alltid får byte-lik P(MOT) i ulike batcher. Dette bør stå i BEGRENSNINGER, fordi en jury som kjører én sak med `--sak` kan få et annet desimaltall enn i fullkjøringen.

## Forslag til NESTE_VERSJON (etter dommen)
Sjekk av hele fila før radene behandles: 0 byte → egen melding og utgang ≠ 0; påkrevde kolonner mangler → én feilmelding som viser skilletegnet som ble funnet, og utgang ≠ 0. Fjern `ai` alene fra regexen (eller krev at det står i en instruks, som «the AI should»).
