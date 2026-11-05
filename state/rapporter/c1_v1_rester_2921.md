# Case 1 (#2921): v1-rester ryddet i GitHub-repoen

Bygger på #2908 (`c1_v1_rester_2908.md`): `results/nokkeltall.md` og `docs/presentasjon.md` finnes ikke, og README har avsnittet «Hvor tallene står» (én kilde).

Funnet nå: v1-tallene lå igjen umerket i `arbeid/hack/levering/c1_v1/` (leveranse 1 kl. 12:55): F1 0,476, P 0,441, R 0,517, TP 30 FP 38 FN 28.
Tallvakta ga 6 avvik på de to filene.

Endret (i landsbyen, synket som repo-commit 8778cb6, skanning 0 funn):
- `c1_v1/README.md` og `c1_v1/kravrespons.md`: banner «Eldre leveranse (v1), ikke gjeldende», som peker på README og `sh KJOR.sh`. v1-linjene er merket `tallvakt: ignorer: eldre v1`. Tallvakta: 0 avvik (hele treet: 32 filer, 197 påstander, OK).
- README (`GITHUB_README_UTKAST.md`): sier at c1_v1 er historikk og er merket eldre. Den nevner også de byte-like kopiene av `stemmeagent/` (bytte/, leveranse/verktoy/), som sier «say-on-pay». De røres ikke, fordi bytt.sh kopierer dem over de frosne filene.
- README hadde en usann setning: «hentekoden for N-PX er ikke med». Henterne `arbeid/hack/c1/hent_*.py` er med (#2899). Setningen er rettet.

Fremmed-testen (`c1_fremmed_test.sh --uten-testaar`) før endringen: 7 FEIL (logg: `arbeid/oppgave_2921/fremmed_for.log`). Den kloner GitHub-main, og main var ikke pushet med denne synken. En kjøring etter endringen ville derfor testet samme kode.
Jeg kjørte trinn 5 (døde henvisninger) lokalt på repoen før og etter commit 8778cb6. Jurydokumentene hadde 78 døde henvisninger begge ganger, så endringen gjør ikke testen rødere. Trinn 6 (/Users/, Mac-sed) berøres ikke: endringen er bare tekst i .md.
Ikke gjort: andre «V1» i ERLIG_EVALUERING og kilder/ er en annen V1 (en modellvariant), ikke v1-leveransen. De står.
