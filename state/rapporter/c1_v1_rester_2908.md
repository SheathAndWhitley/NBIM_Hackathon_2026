# Case 1 (#2908): v1-rester i GitHub-repoen (nøkkeltall, presentasjon, say-on-pay)

- `results/nokkeltall.md` og `docs/presentasjon.md` finnes ikke i repoen, og ingen fil viser til dem (grep, 0 treff). Ingenting å fjerne.
- README (`GITHUB_README_UTKAST.md`) har fått avsnittet «Hvor tallene står»: hovedtallet hentes fra én kilde (README-tabellen, `sh KJOR.sh`), og kandidatene står i KANDIDATER.md. Avsnittet sier også at v1 bare var say-on-pay.
- «say-on-pay votes only» står fortsatt i `levering/stemmeagent/{__init__,config}.py`. Filene er fryst (FROSNE_SHA256.txt), så de er ikke endret. README forklarer det.
- KRAVRESPONS.md: H1 og rad 2 er satt til løst. 1-sideren `c1/leveranse/kravrespons.md` sier allerede alle sakstyper.
- Synket: repo-commit 7d9e1ea, skanning 0 funn. Oppgaven ble droppet på tavla rett etter synken. Den er ikke lukket med done.
