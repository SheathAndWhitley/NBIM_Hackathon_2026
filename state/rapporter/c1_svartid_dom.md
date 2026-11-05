# Dom: svartidstallene fra #2259 holder (#2292, dommer2)

Reprodusert fra fersk kald kopi (`arbeid/oppgave_2292/kald_kopi.sh` → `/tmp/d2_svartid`, egen låst venv, samme filer som `fremmed.sh`),
samme 100 saker (test 2026, frø 0), nettet sperret med `sandbox-exec (deny network*)`, uten fasit. Alle 100 gikk med utgang 0.

| Tall (per sak, egen prosess) | Rapportert (#2259) | Kald kopi (dommer2) | Avvik |
|---|---|---|---|
| Median | 5,28 s | 4,44 s | −16 % |
| p95 | 7,14 s | 6,18 s | −13 % |
| Snitt | 5,48 s | 4,87 s | −11 % |
| Verste | 12,15 s | 12,98 s | +7 % |
| Samlet, 100 saker i én kjøring | 0,042 s/sak | 0,044 s/sak | +5 % |

**Godkjent.** Median og p95 er innenfor 20 % av det rapporterte. Kald kopi var litt raskere, trolig lavere last på maskinen
under min kjøring. Verste tilfelle er i begge kjøringer første sak (oppstart, cache kald), ikke en spesiell sak:
2066000|3 hos meg, 2066391|5 hos smeden. Konklusjonen i `c1_svartid.md` («ca. 5 s per enkeltsak fra kald start,
en hel liste på sekunder») står. Rapporten kan trygt si «under 10 s per sak, p95 ca. 6–7 s».

Rådata: `arbeid/oppgave_2292/kjoring.log`. Kommando: `python3 -I arbeid/oppgave_2292/svartid_kald.py` (etter `kald_kopi.sh`).
