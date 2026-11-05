# Case 1: India-byttet som ferdig oppskrift (#2319, ikke tatt i bruk)

Smed, 05.11. Levert/frossen mappe er IKKE endret: sha256 av 15 filer i arbeid/hack/levering (+ oppgave_2044/2303 train.py)
er like før og etter (`arbeid/oppgave_2319/sha_levert_for.txt` = `sha_levert_etter.txt`), `git status` rent.

## 1. Hva diffen #2044 -> #2303 betyr
`oppgave_2303/train.py` er frossen `oppgave_2044/train.py` + flagg. Uten flagg er modellen lik. Med `--india 1`
legges regelen *land = India og teksten har «chairman» og «managing director|whole time director|chief executive|ceo»
=> MOT* oppå modellens flagg (etter grensa; ingen etiketter, ingen ny trening, grensa 0,9188 uendret).
Øvrige flagg (`--vaar`, `--val-ut`, `--kun-val`) brukes ikke av agenten.

Levert agent kjører train.py med runpy fra `c1_real.py`. Byttet er derfor 3 linjer i `c1_real.py` + 1 i `fremmed.sh`:
- linje 35: `TRAIN` -> `oppgave_2303/train.py`
- linje 85: `--india 1` i argv
- linje 219: `mot = bool(s >= t or g["REGEL"][idx[rid(r)]])` (P(MOT), ruting og sitat er uendret)
- fremmed.sh linje 21: kopierer også `arbeid/oppgave_2303/train.py` (ellers krasjer kald kopi)

## 2. Prøvekjøring i kopi (arbeid/oppgave_2319/levering)
| | c1_real.py sha | fremmed.sh sha |
|---|---|---|
| frossen (før bytt) | 439b49f7…e434f378 | a24b2f66…28a28472 |
| etter bytt | fc440fd6…b6778721 | d3c9003b…5339bff3 |
| etter angre | 439b49f7… (BYTE-LIK, cmp) | a24b2f66… (BYTE-LIK, cmp) |

Etter angre: `diff -rq arbeid/hack/levering <kopi>` gir ingen forskjell. bytt.sh nekter levert mappe (utgang 3, prøvd).
India-kopien på test 2026 (kjøring 10 s): 2 av 1579 svar endret (2080562|4 og |6, 0->1). Måler v3 `--score mot`:
**0,468750** (TP 30 FP 40 FN 28) mot frossen **0,476190** (TP 30 FP 38). pred_maaler.csv er byte-lik #2307s kobling.
Testtallet skal ikke avgjøre (det er hovedtallet, ikke valgdata), men juryen vil se det: byttet koster 0,007 på test.

## 3. Kommandoene #2312 kjører (bare ved dommer JA i #2297), ca. 5 min
```
cd <repo>; S=arbeid/oppgave_2312; P="uv run --project arbeid/kandidater/smed2_c1_mot python"
mkdir -p $S && ln -s ../hack/c1 $S/c1          # kopien må ligge 2 nivåer under arbeid/ med c1 ved siden av
cp -R arbeid/hack/levering $S/levering && rm -rf $S/levering/__pycache__
sh arbeid/oppgave_2319/bytt.sh $S/levering        # før 439b49f7/a24b2f66, etter fc440fd6/d3c9003b
$P $S/levering/kjor_agent.py --ut $S/ut           # ~10 s
$P -I arbeid/hack/c1/maaler_offisiell_v3.py $S/ut/pred_maaler.csv test --data real --score mot   # ventet 0.468750
# ta i bruk:
cp $S/levering/c1_real.py $S/levering/fremmed.sh arbeid/hack/levering/
shasum -a 256 arbeid/hack/levering/c1_real.py arbeid/hack/levering/fremmed.sh   # skal være fc440fd6…, d3c9003b…
```
Angre etter at byttet er tatt i bruk (5 s):
```
python3 -I arbeid/oppgave_2319/bytt.py tilbake $S/levering
cp $S/levering/c1_real.py $S/levering/fremmed.sh arbeid/hack/levering/
shasum -a 256 arbeid/hack/levering/c1_real.py arbeid/hack/levering/fremmed.sh   # skal være 439b49f7…, a24b2f66… (frossen)
```

## 4. Utenfor lappen, må gjøres samtidig hvis byttet tas
- **Frys kl. 16** (`arbeid/verktoy/c1_frys.py`): tar sha av c1_real.py. Bytt FØR 16:00, ellers går frysvakta rød og
  fremmed.sh/kaldstart.sh stopper (utgang 4); da må frysen tas på nytt med `--tving` og grunn på tavla.
  Legg også `arbeid/oppgave_2303/train.py` i FILER.
- `arbeid/hack/c1/kaldstart.sh` linje 39 kopierer bare oppgave_2044/train.py (legg til oppgave_2303/train.py) og
  `REF=0.476190` (linje 69) må bli 0.468750.
- `kjor_agent_real_maskin_alene.csv` / `kjor_agent_real_pred_maaler.csv` lages på nytt, `tavle.py levert` settes på nytt,
  og alle 0,476-tall i .md-ene (tallvakta i fremmed.sh vil ellers melde avvik) -> #2314/#2317/#1975.

Filer: `arbeid/oppgave_2319/{bytt.py,bytt.sh,angre.sh,logg_bytt.txt,logg_angre.txt,log_india.txt,ut_india/}`.
