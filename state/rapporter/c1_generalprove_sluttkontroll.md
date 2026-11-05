# Case 1 generalprøve av sluttkontrollen (#2163): PASS på alle krav som kan sjekkes nå, 29 s

Kommando (fra #2150): `bash arbeid/hack/c1/sluttkontroll.sh`. Kald kopi i `/tmp/c1_sluttkontroll` (tømt først), git e74453d, kjørt 13:04 og 13:05 (etter rettingen i verktøyet). Pakkas tilstand er den fra 13:04 (`c1_real.py` og `kjor_agent_real_test2026.txt` endret 13:04).

| status | krav | bevis |
|---|---|---|
| PASS | 1 kald start | env -i, uv sync --frozen; uv sync 0 s, kjøring 27 s; utgang 0 |
| PASS | 2 F1 MOT = 0,476 | kald uten ruting 0.476190, med ruting 0.476190, frossen #2103 0.476190 (måler v3 sha 8b09c36e01) |
| VENTER | 3 modellfiler uendret siden frys | `state/c1_frys.json` finnes ikke ennå, frys kl. 16 (LaunchAgent). Etter 16 uten frys blir det FAIL av seg selv |
| PASS | 4a ingen utdaterte tall (kald kjøring) | 13 filer, 129 påstander, 0 avvik (til menneske 188 av 1578, 11,9 %) |
| PASS | 4b ingen utdaterte tall (lagrede filer) | 13 filer, 129 påstander, 0 avvik |
| PASS | 5 alle sitater har kilde | 1578/1578 GVG-sitater og 74/74 begrunnelsessitater ordrett |
| PASS | 6 varighet under 10 min | 29 s (30 s første kjøring) |

## FAIL med eier-forslag
- Ingen FAIL nå. De to FAIL-ene fra #2150 kl. 13:03 (4a/4b, 188 mot 222/228 til menneske) er borte: den lagrede loggen er laget på nytt og tallene stemmer med kald kjøring.
- **Risiko, ikke FAIL:** #2152 (smed, 50 %) legger inn flere menneske-vakter. Endrer de antallet til menneske, faller 4a/4b igjen. Eier: smed2 (#2159) retter tallene, smed (#2162) lager loggen på nytt, dommer (#2155) kjører sluttkontrollen etterpå. Kontrollen bør kjøres på nytt rett etter #2162 og rett etter frys kl. 16.

## Negativtest av tallvakta
Plantet «190 av 1578 (12,0 %)» i EN_SIDE.md i en kopi: 2 av 2 AVVIK funnet (antall og prosent). KP: forventet 2 avvik, fikk 2.

## Rettet i verktøyet (ikke i pakka)
1. Krav 1 ga PASS for alle utganger fra fremmed.sh så lenge svarfilene fantes. Nå er bare utgang 0, eller 1 (tallvakta, telles i krav 4), lov; annen utgang er FAIL.
2. Bevisteksten sa «(1 = bare tallvakta)» også ved utgang 0. Står nå bare når utgangen er 1.
3. `RAPP=<fil>` kan settes, så en prøvekjøring ikke overskriver rapporten med notater. Sluttlinja viser riktig rapportfil.
`bash -n` OK, kjørt på nytt etter rettingen: samme resultat.
