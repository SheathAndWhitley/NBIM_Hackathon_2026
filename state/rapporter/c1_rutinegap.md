# Case 1: hvorfor fant ikke vi jury-hullene selv (ordre #283, oppgave #2909)

Kort svar: alle testene våre fikk hjelp som juryen ikke får. De kjørte i en kopi vi hadde satt sammen selv, med data
vi la inn selv, på den eneste maskinen vi har, og ingen av dem leste README. Juryen gjør det motsatte på alle fire punktene.

## Årsak (5 punkter)

1. **Vi testet det vi kopierte, ikke det vi publiserte.** `fremmed.sh` kopierer en håndplukket filliste fra landsbyen,
   der alt finnes. `c1_natt_push.sh` bruker riktignok `git archive`, men kopierer selv inn `real_votes.csv` og `data_off/*.csv`
   (linje 57–59) før `KJOR.sh` kjøres. Porten gjorde altså datasteget for juryen. Derfor var hull 1 («FEIL DATAFIL»)
   usynlig hos oss.
2. **Ingen kjøring gikk via GitHub slik en fremmed gjør det.** Alle kaldstarter brukte zip-en eller den lokale repoen,
   aldri en `git clone https://` uten nøkkel. At repoen var privat og at GitHub viser main (hull 2), kunne derfor ikke
   vises. Oppgaven som skulle gjøre dette (#2756), ble autolukket på tidsboks («se TILSTAND.md») uten at den hadde
   kjørt, og ingen port stoppet på at den var ugjort.
3. **Dokumentasjonen var ikke under test.** Vi kjørte egne skript (`KJOR.sh`, `fremmed.sh`), ikke kommandoene README
   ber juryen kjøre, og ikke i README-rekkefølgen. `demo.sh` ble aldri kjørt på en klone uten at `KJOR.sh` hadde kjørt
   først (hull 3). Ingen sjekket at stiene i *.md fantes. Tekstene ble skrevet i landsbyen, der alle stier finnes, og
   `arbeid/` er gitignored der, så heller ikke `git status` viste noe. Arkitekten fant 107 døde henvisninger i dok og kode
   (#2898, `c1_repo_dode_henvisninger.md`).
4. **Én plattform og eksakt likhet.** Tallvakta krevde nøyaktig 0,512000. Vi har ikke Linux, og ingen visste at tallet
   avhenger av plattformen: Linux gir 0,520 (hull 4). En vakt uten toleranse på én maskin måler maskinen, ikke pakka.
5. **«Kald» var aldri definert, og samme gjenstand ble sjekket to ganger.** Akseptkravet «grønn fra kald start» sa ikke
   *hva* som skulle startes. Smeden bygde zip-en, og dommeren verifiserte den samme zip-en. Ingen hadde jobben «gjør
   bare det README sier, på det GitHub serverer». I tillegg teller autolukking på tidsboks som `done` på tavla.

## Mekanisme: fast klone-port i `c1_natt_push.sh`, gjenbrukbar for Name that LLM

Prinsipp: **porten legger ingenting inn.** Den kloner med git, kjører README-blokkene ordrett under `env -i` og
sjekker dokumentene. Alt den må gjøre for hånd, regnes som FEIL.

### Byggeklosser (smeden bygger, ~45 min; mye finnes alt)

**A. `arbeid/verktoy/klone_port.sh <manifest>`**. Dette er `c1_fremmed_test.sh` (#2900, dommeren) gjort generell.
Manifestet er en sh-fil med variabler, så Case 1 og Name that LLM bruker samme skript:

```sh
# arbeid/verktoy/port/c1.env
PORT_NAVN=c1
PORT_URL_ANON=https://github.com/Martinkristofferhansen/nbim.git   # det README sier
PORT_URL_SSH=git@github.com:Martinkristofferhansen/nbim.git
PORT_GREN=main                       # GitHub viser denne som standard; det er den juryen ser
PORT_README=README.md                # kodeblokkene kjøres ordrett i rekkefølge
PORT_FORVENT='HOVEDTALL F1 MOT .*: 0\.5(0[2-9]|1[0-9]|2[0-2])'   # 0,512 ±0,01 (Mac 0,512 / Linux 0,520)
PORT_FORVENT2='TALLVAKT GRØNN'
PORT_ETTER='sh arbeid/hack/c1/leveranse/demo.sh "$PWD"'           # det README sier etter blokkene
PORT_DATA=                           # tom = ingen data legges inn (etter #2897 henter KJOR.sh ny_data/ selv)
PORT_UNNTAK=.port_unntak             # fil i repoen: kjente plassholdere og genererte stier (ut/, *.csv i DATA.md)
```

Trinn med OK/FEIL per linje og utgang 0 bare når alt er grønt:
1. `git clone --branch $PORT_GREN <kilde>` til tom `mktemp -d`. Kilden er `--kilde` (standard `PORT_URL_ANON`).
   Bruk `git clone`, ikke `git archive` og ikke `cp`, så `.gitignore`/`export-ignore` slår inn som hos juryen.
2. `env -i HOME=<tom> PATH=<bin med bare uv,git>:/usr/bin:/bin`. Ingen landsby-stier og ingen arvet `.venv`.
3. README-blokkene kjøres ordrett. Er `PORT_DATA` tom og en blokk trenger data, er det FEIL (hull 1).
   Klonelenka i blokkene byttes til `--kilde` bare i før-push-modus (se B), og det står i loggen.
4. `PORT_ETTER` kjøres i ny klone uten at blokk 3 har kjørt først. Står demoen, er det FEIL (hull 3, rekkefølge).
   Deretter kjøres den i klonen fra trinn 3.
5. `PORT_FORVENT*` på utskriften, med toleranse i regex (hull 4).
6. Døde henvisninger: `arbeid/verktoy/dode_henvisninger.py <klone> --unntak $PORT_UNNTAK`. Dette er `arbeid/oppgave_2898/dode.py`
   flyttet til verktoy med utgang 1 ved ≥1 død henvisning i klassene dok/kode. `state/` og `kilder/` er unntatt med én
   linje i unntaksfila, ikke linje for linje. Trinn 5 i `c1_fremmed_test.sh` (enkel *.md-skann) erstattes av denne.
7. Grep etter `/Users/`, landsby-stier og Mac-konstruksjoner (`sed -i ''`, `stat -f`, `date -v`, `shasum`). Det finnes
   alt i `c1_fremmed_test.sh` trinn 6. Uten Linux er dette den ærlige erstatningen. Treff er FEIL utenfor `arkiv/`.

**B. Koble inn i `c1_natt_push.sh`, før og etter push:**

- *Før push* (erstatter linje 55–61, `git archive` + `cp` data + `KJOR.sh` + `testaar.sh`):
  `bash arbeid/verktoy/klone_port.sh arbeid/verktoy/port/c1.env --kilde "file://$REPO" --gren main`
  (klone av den lokale commiten). Rød port betyr ingen push, med første FEIL-linje i `c1_natt_synk.md`.
  `testaar.sh` og hemmelighetsskanningen står som før, men kjøres i klonen. **De tre `cp`-linjene slettes.**
- *Etter push* (nytt, etter `git push`):
  1. `git ls-remote origin refs/heads/main` må være `$LOK`, ellers RØD.
  2. Porten kjøres på nytt med `--kilde $PORT_URL_ANON` (anonym https).
     - Svarer GitHub 200: porten må være grønn. Er den rød, skriver `til-guden` én linje.
     - Svarer GitHub 404/auth og `state/c1_PRIVAT` finnes (guden har sagt privat til fredag, #284): GUL «privat,
       ventet», og porten kjøres med `--kilde $PORT_URL_SSH` så resten likevel testes.
     - Svarer GitHub 404 og `state/c1_PRIVAT` mangler: RØD, fordi juryen ikke kommer inn (hull 2).
- Porten kjøres bare når det er noe nytt å pushe, slik som i dag. Kjøretid ≈ to `KJOR.sh` (~2 × 45 s) og passer i
  10-minutters takten.

**C. Tavleregel (én linje i tavle.py eller dommerens håndbok):** en oppgave med akseptkrav som inneholder «kjør» eller
«klon», som autolukkes på tidsboks, får status `requeue`, ikke `done`. #2756 skal ikke kunne skje igjen.

### Name that LLM

Samme `klone_port.sh` med `arbeid/verktoy/port/ntl.env`. `PORT_README` blir notatbokas README eller
`ntl_start.sh`, `PORT_FORVENT` blir CV-tallet ±toleranse, og `PORT_DATA` tom, for Kaggle henter data selv.
Hovedgevinsten der er trinn 6 og 7 (døde stier og `/Users/` i innsendt kode) og trinn 1 med `git clone` i stedet for
kopi. Én port, to manifester.

### Kontrollpunkt (KP) for smeden: porten skal bevise at den ser hullene

- **KP1:** Kjør porten mot `08d0806` (HEAD før jury-fiksene, 19:48). Forventet: FEIL på alle fire jury-funnene
  (trinn 3 data, trinn 1/B anonym klone, trinn 4 demo, trinn 5 0,520 tåles, men 0,512-eksakt i gammel tallvakt feiler)
  og >0 døde henvisninger. Finner porten ikke disse, er den ikke god nok, og den skal ikke kobles inn.
- **KP2:** Kjør porten mot HEAD etter #2897/#2899. Forventet: ALT GRØNT, eller bare GUL «privat, ventet».
- Skriv begge som «KP: forventet X, fikk Y» i `state/rapporter/c1_klone_port.md`.

## Anbefaling

**Bygg.** Det meste finnes alt: `c1_fremmed_test.sh` (#2900) og `oppgave_2898/dode.py`. Arbeidet er å flytte dem til et
manifest-styrt `klone_port.sh`, slette de tre `cp`-linjene i `c1_natt_push.sh` og legge til etter-push-steget.
Rekkefølge: etter at #2897 og #2899 er ferdige (ellers blokkerer porten pushen av selve fiksene), og før guden gjør repoen
offentlig fredag. Ny smed-oppgave foreslått på tavla.
