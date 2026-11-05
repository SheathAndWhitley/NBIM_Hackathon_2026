# Case 1: dommerens gjentakelse av robusthetstesten (#2387, dom over smed3 #2380, 05.11 kl. 15:25)

**Dom: GODKJENT. Smed3s tall er reprodusert. 16/16 testtyper like, 56/56 svarrader like felt for felt. Eneste avvik er tidskolonnen (sekunder), som ikke er et resultat.**

## Hva jeg gjorde
- Egen fersk kald kopi: `sh arbeid/hack/levering/fremmed.sh /tmp/c1_kald_2387` (logg: `arbeid/oppgave_2387/fremmed.log`).
  HOVEDTALL F1 MOT mot styret (v3 --score mot): **0,476190**. TALLVAKT GRØNN. Frysvakt: ikke frosset ennå (før kl. 16). uv sync 0 s, kjøring 30 s.
- Smed3s skript kopiert uendret til `arbeid/oppgave_2387/robusthet_kald.py` (bare mappenavn 2380 -> 2387 i stier og tmp-prefiks, se `diff`),
  kjørt med `python3 -I` mot min kopi, kopiens eget python under `env -i`. Utdata: `arbeid/oppgave_2387/ut/tabell.md` og `resultat.json`.
- Sammenligning mot `arbeid/oppgave_2380/ut/`:
  - `tabell.md` uten sek-kolonnen: byte-lik (`diff` tom).
  - `resultat.json`: samme 16 tester, samme rc / saker inn / saker ut; alle 56 svarrader (agent.csv) like i alle 19 felt
    (id, anbefaling, mot_styret, p_mot, til_menneske, rutingsgrunn, sitat, injeksjon_flagget, raa_score, retningslinje_*, ...). Ulike felt: 0.

## Tallene (like hos smed3 og dommer)
| test | inn | ut | krasj | MOT | til menneske | uten grunn |
|---|---|---|---|---|---|---|
| original (nye møte-id) | 6 | 6 | nei | 1 | 1 | 0 |
| tomt felt (tekst/type/selskap/dato) | 6 | 6 | nei | 0 | 6 | 0 |
| ugyldige verdier | 8 | 8 | nei | 0 | 6 | 0 |
| ukjent selskap | 6 | 6 | nei | 1 | 6 | 0 |
| ukjent forslagstype | 6 | 6 | nei | 0 | 6 | 0 |
| lang tekst | 3 | 3 | nei | 0 | 3 | 0 |
| injeksjon | 6 | 6 | nei | 1 | 6 | 0 |
| duplikat-id | 2 | 2 | nei | 0 | 1 | 0 |
| kjent sak uendret | 3 | 3 | nei | 1 | 1 | 0 |
| kjent sak, endret tekst/styret | 3 | 3 | nei | 1 | 3 | 0 |
| tom fil (bare overskrift) | 0 | 0 | nei | 0 | 0 | 0 |
| manglende kolonne proposal_type | 3 | 3 | nei | 0 | 3 | 0 |
| sak: tomt objekt {} | 1 | 1 | nei | 0 | 1 | 0 |
| sak: null-felt | 1 | 1 | nei | 0 | 1 | 0 |
| sak: ukjent selskap og type | 1 | 1 | nei | 0 | 1 | 0 |
| sak: injeksjon | 1 | 1 | nei | 0 | 1 | 0 |

Ingen krasj. Tid per test: smed3 4,5–7,1 s, dommer 4,4–5,3 s (maskinlast, ikke resultat).

## Merknader
- Testen er deterministisk (frø 2063, låst modell), så byte-likhet er forventet; avvik ville betydd at pakka ikke er stabil.
- Kjørt FØR modellfrysen kl. 16. #2266 (smed2) gjentar motstandstesten på den frosne agenten etter frysen; denne dommen gjelder pakka slik den var 15:10–15:25.
- Ryddet 2,1 GB egne gamle kalde kopier fra #2127 (`/tmp/c1_kald2..6_2127`) for å få plass; disken sto på 1 GB.
