# Case 1: robusthetstesten kjørt på nytt fra kald kopi, ett krasj funnet og rettet (#2724, smed3)

Kjørt 05.11 kl. 18:15–18:30. Kald kopi bygd med `fremmed.sh /tmp/kald2724` (frysvakt grønn mot frysen 17:18:18,
tallvakt grønn, hovedtall F1 MOT 0,512). Hver inn-fil kjørt med `kjor_agent.py --csv <fil> --ut <mappe>`
under `env -i`. Inn-filene (de 7 fra #2716 pluss 6 nye) ligger i `arbeid/oppgave_2724/inn/`.

| nr | input | oppførsel med frossen kode (17:18) | exit |
|---|---|---|---|
| 01 | tom fil (0 byte) | advarsel, tom agent.csv | 0 |
| 01b | bare overskrift | samme | 0 |
| 02 | proposal_text mangler | alle 5 til menneske «mangler felt» | 0 |
| 03 | ukjent selskap | til menneske «ukjent selskap», de to kjente svart normalt | 0 |
| 04 | dublett-id | første normalt, andre til menneske «duplikat» | 0 |
| 05 | norsk tekst, kjent id | til menneske («instruksjonslignende», se #2716) | 0 |
| 06 | norsk tekst, ny id | til menneske | 0 |
| 07 (ny) | tomme felt (proposal_text, mgmt_rec, meeting_date) | til menneske «mangler felt: meeting_date,proposal_text», anbefaling FOR = styret (tom styret → FOR) | 0 |
| 08 (ny) | meeting_date = «ikke-en-dato» | til menneske «ugyldig møtedato» | 0 |
| 09 (ny) | CRLF + UTF-8 BOM | alle 5 svart normalt, samme P(MOT) som ren fil | 0 |
| 10 (ny) | ekstra kolonne «ekstra» | ignorert, alle 5 normalt | 0 |
| 11 (ny) | semikolon-separert | 5 rader «rad1..rad5» til menneske «mangler felt …» (hele linja blir én kolonne) | 0 |
| 12 (ny) | binær fil (NUL, 0xff, alle byteverdier) | **TRACEBACK** `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff` i c1_real.py:149 | 1 |

12 av 13 gikk pent. Én krasj: en inn-fil som ikke er UTF-8-tekst. Det gjelder også en vanlig latin-1-CSV
fra Excel med æøå (testet som nr. 13 etter rettelsen, samme feil før).

## Rettelsen (c1_real.py, commit e0730dc)

Lesingen av inn-fila er pakket inn: `UnicodeDecodeError` gir varselet «inn-fila er ikke UTF-8-tekst (…, byte N);
prøver latin-1» og leser på nytt som latin-1. Gir latin-1-lesingen `csv.Error` (f.eks. NUL i linja), stopper
agenten med én linje «FEIL: inn-fila … kan ikke leses som CSV (…); ingen saker vurdert, ingen agent.csv skrevet»
uten traceback. Ingen annen linje er endret.

Etter rettelsen, samme kalde kopi:
- 12 binær: varsel, lest som latin-1, 2 søppelrader «rad1/rad2» til menneske «mangler felt», exit 0, ingen traceback.
- 13 latin-1 med «Blåøyd Fjørfe ASA»: varsel, æøå riktig i agent.csv, raden til menneske «felt avviker fra lagret
  sak (proposal_text)», den andre raden svart normalt (P 0,0072). Exit 0.

Prediksjonene er uendret: ekte inn-sett (1578 saker) kjørt i samme kalde kopi før og etter rettelsen,
`cmp` sier agent.csv byte-lik (sha256 24ee6b18…) og pred_maaler.csv byte-lik.

## Frysen

c1_real.py er en av de 21 frosne filene, så frysen er satt på nytt (`c1_frys.py frys --tving`) kl. 18:19:39.
Bare c1_real.py har ny sha; modell, train.py, prediksjoner og data er like. Grunnlaget er oppgaveteksten i
#2724 («legg til pen feilmelding/menneske-ruting, ikke endre prediksjoner»). Dommeren er varslet på tavla og kan
rulle tilbake med `git show e0730dc -- arbeid/hack/levering/c1_real.py` om ønsket.

## Fremmed.sh på nytt etter rettelsen (fersk kald kopi /tmp/kald2724b)

Kjørt 18:28 med den nye frysen:

    FRYSVAKT GRØNN: 21 filer like som ved frys 2026-11-05T18:19:39
    tid: uv sync 0 s, kjøring 32 s, totalt 32 s
    HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.512000
    Måler v3 --score mot på ut/pred_maaler.csv: F1 0.5120  P 0.4776  R 0.5517  TP 32 FP 35 FN 26  (58 MOT i fasit, 66 avvik)
    Kjøring: til menneske 164 av 1578 inn (10.4%), 161 av 1539 med fasit (10.5%)
    TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring

agent.csv i den ferske kopien er byte-lik agent.csv fra kopien bygd før rettelsen (cmp).

## Reproduksjon

    sh arbeid/hack/levering/fremmed.sh /tmp/kald
    cd /tmp/kald && for f in <repo>/arbeid/oppgave_2724/inn/*.csv; do
      .venv/bin/python arbeid/hack/levering/kjor_agent.py --csv $f --ut /tmp/ut_$(basename $f .csv); done
