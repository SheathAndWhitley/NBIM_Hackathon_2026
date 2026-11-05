# Case 1: dom over ryddingen av leveransen (#2436, dommer, 05.11 kl. 15.55)

**Dom: GRØNN** etter én rettelse i pakkeskriptet. Ryddingen i #2422 (dommer2) ødela ingen pekere.
KJOR.sh går fra kald kopi i /tmp og gir hovedtallet.

## Brutte pekere
1. `c1/tall_tabell.md` (nevnt i README.md, JURY.md, JURY_SPORSMAL.md og kilder/c1_val_kaldstart.md):
   fila finnes i repoet (arbeid/hack/c1/tall_tabell.md), men ble ikke pakket i jury-zipen, fordi pakk_jury.sh bare tar
   fremmed.sh-lista, de frosne filene og leveranse/. **Rettet:** pakk_jury.sh kopierer nå fila (commit cc84f77).
   Tallvakta leser bare levering/*.md og c1/leveranse/*.md, så den nye fila kan ikke gjøre den rød.
2. `kilder/c1_beslutning_nyeste_historikk.md` (JURY.md pkt. 12) og `kilder/c1_offline_kaldstart.md` (JURY_SPORSMAL.md):
   lå ikke i zipen fra kl. 15.41, fordi filene kom inn i leveranse/kilder/ kl. 15.41.10, etter at zipen ble bygd.
   Ikke feil i pakkinga; neste pakking tar dem med. Må sjekkes i den endelige zipen (se under).

Alt annet holder. Sjekket med `arbeid/oppgave_2436/pekersjekk.py` (backtick-stier, lenker og `$ROT/`-stier i
leveranse/README.md, JURY.md, kjor.sh, jury-README og KJOR.sh) pluss håndsjekk:
- README.md (repo): fremmed.sh, maaler.sh, oppgave_2044/train.py, levering/c1_real.py, oppgave_2047/vern.py,
  kandidater/smed2_c1_mot, levering/kjor_agent.py, c1/hent_npx.py, c1/baseline.py, c1/arkiv/gammel_data/, begge
  datafilene og real_test_input.csv finnes.
- kjor.sh (repo): SPOR=npx-stien (gulv_v3.py, hent_nbim.py, lag_v3.py, maaler.py, spor_npx/motstand_inj.py,
  spor_npx/resultat.py) finnes i arbeid/hack/c1.
- KJOR.sh og jury-README (zip): train.py, kjor_agent.py, maaler_offisiell_v3.py, c1_tallvakt.py,
  sjekk_treffsikkerhet.sh, real_votes.csv og FROSNE_SHA256.txt finnes i zipen. `ut/` lages av kjøringen.
  `state/rapporter/…` er med vilje ikke i zipen, og jury-README sier det.
- Etter #2422: ingen __pycache__, .pyc eller .DS_Store i leveranse/ eller zipen. 99 filer i zipen fra kl. 15.41
  (hygienerapporten skrev 119 for zipen fra kl. 15.30; tallet avhenger av hvilken bygging som lagde den, ikke sjekket videre).

## KJOR.sh fra kald kopi
`/tmp/jurypakke_c1.zip` (kl. 15.41) kopiert til /tmp/dom2436, pakket ut, `sh KJOR.sh` med nohup:

    FRYSVAKT GRØNN: 15 frosne filer har samme sha256 som ved pakking
    tid: uv sync 1 s, kjøring 101 s
    HOVEDTALL F1 MOT mot styret (v3 --score mot): 0.476190
    18 filer, 168 påstander om hovedtallet stemmer, 0 avviker
    TALLVAKT GRØNN: tallene i pakka stemmer med kald kjøring

TP 30 FP 38 FN 28, 183 av 1539 med fasit til menneske. Varm uv-cache (1 s); kjøringen tok 101 s fordi maskinen
var under last fra generalprøvene (29 s i README gjelder uten last).

## Å gjøre i den endelige pakka (#1972, kl. 19.30)
Etter neste `pakk_jury.sh` skal dette gi 3:
`unzip -l /tmp/jurypakke_c1.zip | grep -c -E 'tall_tabell.md|c1_beslutning_nyeste_historikk.md|c1_offline_kaldstart.md'`

## #2444: ny zip bygd kl. 15.47, de tre filene er med
`pakk_jury.sh` kjørt til /tmp/d2444/jurypakke_c1.zip (egen bygge- og stagemappe, ikke /tmp/jurypakke_c1.zip):
fremmed.sh kald, TALLVAKT GRØNN, HOVEDTALL F1 MOT 0.476190, 104 filer (99 i forrige: +tall_tabell.md og
+kilder-filer fra #2432/#2439). Pakket ut og sjekket:
- `arbeid/hack/c1/tall_tabell.md`, `kilder/c1_beslutning_nyeste_historikk.md` og `kilder/c1_offline_kaldstart.md`
  finnes i zipen (grep-tellinga over gir 3). Ingen __pycache__/.pyc/.DS_Store.
- pekersjekk.py: 17 «brutte» pekere, alle av samme slag som dommen over godtok: filer kjøringen lager
  (`ut/`, `agent.csv`, `ut_egen/`, `.venv/`), kommandolinjer (`sh KJOR.sh`, sjekk_treffsikkerhet.sh med argument;
  selve skriptet finnes i zipen), mappenavnet `c1_stemmeagent` og `state/rapporter` som med vilje ikke er i zipen.
  Ingen peker på en fil som skulle vært med, mangler.
Merk: zipen er bygd FØR frysen (sha256 er dagens filer). Den endelige zipen bygges etter kl. 16 og sjekkes i #1972.

GRØNN: tall_tabell.md og begge kildefilene er med i ny jury-zip, ingen reelle brutte pekere.
