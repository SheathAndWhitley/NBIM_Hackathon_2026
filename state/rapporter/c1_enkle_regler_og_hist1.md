# Case 1: to enkle regler og «bare år før» mot hovedtallet 0,476 (dommer2 #2134, 05.11 ca. 13.05)

Måler: `arbeid/hack/c1/maaler_offisiell_v3.py <svar> test --data real --score mot` (sha256 8b09c36e01), real_votes test 2026, 58 MOT mot styret i fasit.
KI: klyngebootstrap per selskap, 2000 trekk, seed 0 (`arbeid/oppgave_2103/diff_ki.py`, KI for raden selv = parret mot «følg styret» (alle 0)).
Differansen er parret med samme trekk mot `arbeid/oppgave_2103/full_test.csv` (frossen #2044 miks h2). Den gir 0,4762 på måleren, sjekket på nytt nå.
Ingen modellendring. Reglene bruker løpende historikk (møter strengt før radens dato, alle år), altså samme antagelse som hovedmodellen.

| Rad | F1 MOT | P | R | flagget | 95 % KI | Diff mot 0,476 [95 % KI] | Forsøk |
|---|---|---|---|---|---|---|---|
| **Hovedmodell #2044 miks `--hist 2` (løpende)** | **0,476** | 0,441 | 0,517 | 68 | [0,359; 0,590] | – | (#2090) |
| (a) MOT hvis NBIM stemte MOT mot styret i selskapet før | 0,097 | 0,052 | 0,828 | 928 | [0,072; 0,124] | −0,379 [−0,489; −0,269] | #1115 |
| (b) MOT hvis samme forslagstekst fikk MOT før (alle selskaper) | 0,287 | 0,199 | 0,517 | 151 | [0,203; 0,378] | −0,189 [−0,274; −0,103] | #1116 |
| (b2, ekstra) samme selskap + samme tekst fikk MOT før | 0,365 | 0,317 | 0,431 | 79 | [0,252; 0,492] | −0,111 [−0,216; −0,006] | #1117 |
| (c) frossen #2044 miks `--hist 1` (bare år før), nedre grense | 0,415 | 0,458 | 0,379 | 48 | [0,301; 0,533] | −0,061 [−0,143; +0,022] | #1118 |
| følg styret (gulv) | 0,000 | – | 0 | 0 | [0; 0] | −0,476 | – |

## Slik leses det
- **Modellen slår begge enkle regler, og hele KI-en for differansen ligger under null** (a: 2000 av 2000 trekk, b: 2000 av 2000, b2: 98 %). Svaret på «slår dere noe enkelt?» er altså ja. Regel b2 er den sterkeste enkle regelen (0,365), og vi slår den med 0,11.
- **Regel a er den gamle presedensregelen** (0,100 i #2086 på avvik; 0,097 her på MOT mot styret). Den flagger 60 % av sakene.
- **Hovedtallet uten samme-sesong-historikk er 0,415.** Med bare år før faller F1 med 0,061, men KI-en for differansen krysser null (92 % av trekkene ligger under). Det er det ærlige golvet hvis NBIM ikke publiserer stemmene løpende. Grensen er valgt på val 2025 i samme kjøring (C=0,3, grense 0,9446, val F1 0,448).
- 0,415 erstatter tallet 0,386 i KORT.md/#1038. Det var F1 på `against_board` (66 avvik), mens 0,415 er MOT mot styret (58) med v3. Samme kjøring gir begge tallene (logg: `arbeid/oppgave_2134/h1.log`).

## Kommandoer (fra landsbymappen)
```
python3 -I arbeid/oppgave_2134/regler.py                       # skriver regel_{a,b,b2}_test.csv
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2134/regel_a_test.csv test --data real --score mot   # tilsvarende b, b2
(cd arbeid/oppgave_2044 && uv run --project ../oppgave_2023 python train.py ../hack/CASE/20261105_114241_real_votes.csv --variant miks --hist 1 --ut ../oppgave_2134/pred_miks_h1.csv)
python3 -I arbeid/oppgave_2134/til_id.py arbeid/oppgave_2134/pred_miks_h1.csv arbeid/oppgave_2134/hist1_test.csv
python3 -I arbeid/hack/c1/maaler_offisiell_v3.py arbeid/oppgave_2134/hist1_test.csv test --data real --score mot
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2103/full_test.csv arbeid/oppgave_2134/<svar>_test.csv test   # diff mot 0,476
python3 -I arbeid/oppgave_2103/diff_ki.py arbeid/oppgave_2134/null_test.csv  arbeid/oppgave_2134/<svar>_test.csv test   # KI for raden
```
Kontroll: `til_id.py` på `oppgave_2044/pred_miks_h2.csv` gir 0,4762 (`kontroll_h2_test.csv`), så konverteringen er riktig.

## Til speider (METODE/JURYSVAR/KRAVRESPONS)
Én setning: «Modellen (0,476) slår den beste enkle regelen, samme selskap og tekst fikk MOT før (0,365, diff +0,11 [0,01; 0,22]). Med bare historikk fra tidligere år er F1 0,415 [0,30; 0,53]. Det er nedre grense hvis stemmene ikke publiseres løpende.»

## Verifisert fra kald kopi (dommer #2139, 05.11 ca. 13.10)
Kald kopi i `/tmp/kald_2139` (bare skriptene, dataene, måleren v3 og train.py kopiert inn; venv fra oppgave_2023). Kommandoene over er kjørt som de står.
| Rad | Rapportert | Kald kopi | Avvik | Forsøk på måler de049083d9 (v3 --score mot) |
|---|---|---|---|---|
| (a) | 0,097 | 0,097363 | 0 | ikke registrert (utenfor oppgaven) |
| (b) | 0,287 | 0,287081 | 0 | ikke registrert |
| (b2) | 0,364964 | 0,364964 | 0 | **#1122, målt** |
| (c) hist1 | 0,415094 | 0,415094 | 0 | **#1123, målt** |
- Alle fire svarfilene er byte-identiske med filene i `arbeid/oppgave_2134/`. hist1-treninga tok 5 s, val-valg C=0,3, grense 0,9446, som i rapporten.
- Liten merknad: regler.py skriver «a 967 flagget, b 152» (alle rader, ikke bare test), mens tabellen sier 928/151. Det er en tellegrunnlag-forskjell, ikke et scoreavvik.
- Merk: forsøkstavla sier «MOT 79/66 av fasit»; 66 er `against_board`, ikke 58 MOT mot styret (se #2146).
- #2139 hadde ingen egen måler og falt tilbake til den globale (Name that LLM, 8733327407), så første registrering ble avvist. Satt `tavle maaler --oppgave 2139` til samme v3-måler som #2123/#2148.
