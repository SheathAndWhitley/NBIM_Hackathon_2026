# Case 1: dom over GitHub-repoen nbim (oppgave #2765, dommer2, 05.11 18:37)

**GODKJENT** for innholdet som lå på GitHub 18:35 (HEAD c66408c): hemmelighetsskann 0 funn, ingen fasitfil (ingen `pred_miks*`, `svar.csv` eller label-fil, verken i arbeidstre eller i historikken), største blob 255 KB (ingen over 50 MB), FROSNE_SHA256.txt stemmer 14 av 14 og er lik den lokale repoens.

## Slik ble det målt
- Klonet til tom mappe `/tmp/nbim_dom/nbim` med deploy-nøkkelen (HTTPS krever innlogging, repoen er privat).
- `bash arbeid/verktoy/c1_hemmelig_skann.sh /tmp/nbim_dom/nbim` → exit 0 (nøkler, hjemmestier, persondata, hemmelige filnavn, symlenker, >50 MB).
- `git ls-files | grep -iE "pred_miks|fasit|h2|svar\.csv|labels|y_test"` → bare `kilder/case1_hvilken_fasit.md` (en tekstrapport, ikke data).
- `git log --all --name-only` for samme mønstre → samme eneste treff; ingen fasitfil har vært committet og fjernet.
- `verktoy/lagret/repo4_*_test.csv` har kolonnene `id,anbefaling,p_avvik`: prediksjoner, ikke sanne stemmer.
- `shasum -a 256 -c FROSNE_SHA256.txt` → 14 OK, 0 avvik.

## Forbehold
- GitHub lå én commit bak den lokale repoen (lokal HEAD 37fed69 = README-boksen fra #2767); smed2 pusher den i #2768. Innholdsendringen er bare README-tekst.
- Oppgaven ba om dom «når #2762 er pushet». #2762 (ALT Case 1-arbeid inn) er ennå ikke pushet (venter på #2712). Denne dommen dekker derfor ikke de nye mappene. Samme sjekk må kjøres igjen etter #2762; kommandoene over kan gjentas ordrett på ny klone.

---

# Ny dom etter #2762 (oppgave #2775, dommer2, 05.11 18:52)

**GODKJENT** for GitHub HEAD 5deae34 (#2762, 957 filer, .git 2,2 MB): hemmelighetsskann exit 0, ingen fasitfil, største blob 255 KB, FROSNE_SHA256.txt 14 av 14 OK og lik lokal repo.

## Slik ble det målt (fersk klone til tom mappe `/tmp/nbim_dom2/nbim`, deploy-nøkkel via GIT_SSH_COMMAND)
- `c1_hemmelig_skann.sh` på klonen → exit 0.
- Alle 32 csv-filer i treet har bare prediksjonskolonner (`id,anbefaling[,konfidens],p_avvik[,regel,punkt,injeksjon_flagget]`). Ingen kolonne med sann stemme. `punkter.jsonl` er NBIMs retningslinjer, ikke data.
- Treff på «fasit» er bare tekstrapporter, `frys_fasit.py` og `frys_fasit_1600.sha256` (sha256-liste over jury-zipen, ikke data). Samme i hele historikken (`git log --all --name-only`): ingen `pred_miks*`, `svar.csv`, label- eller `.env`/nøkkelfil har vært committet.
- Ingen symlenker. Ingen privatnøkkel eller GitHub-token i innhold; eneste treff på «nbim_deploy» er stien til nøkkelen nevnt i `state/rapporter/c1_github_push_2712.md` (ufarlig, nøkkelen ligger utenfor repoen).
- Største blobs: 255 KB (punkter.jsonl), 209 KB (uv.lock). Ingen over 50 MB.
- `shasum -a 256 -c FROSNE_SHA256.txt` → 14 OK, 0 avvik; fila er byte-lik den lokale.

## Forbehold
- Dommen gjelder 5deae34. Tekststopp-synken (#2728, etter kl. 19) gir ny HEAD; #2773 (19:45) må sjekke at SHA-fila fortsatt stemmer og at skannen er grønn. Kommandoene over kan gjentas ordrett.
