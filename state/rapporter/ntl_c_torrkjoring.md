# NTL oppgave C: tørrkjøring av oppstarten (1,5B trinn 2, nytt frø) uten trening (#2843)

**GRØNN** for alt som kan sjekkes lokalt. Én ting må gjøres ved start: pushe kjernen (se under). Ingen trening, ingen tall. Case 1-filer ikke rørt.

## Kjernen (bygget, ikke pushet)
`arbeid/oppgave_2843/kernel_c/`: `ntl_gpu_c.py` + `kernel-metadata.json` (id `martinaka/ntl-smed3-c-seed100`, T4, kernel_sources `martinaka/ntl-smed3-gpu`, datasets `ntl-smed3-data` og `ntl-smed3-folds`).
Avledet av `arbeid/oppgave_1489/kernel_gpu/ntl_gpu.py`. Endringer: trinn 1 trenes ikke, adapteren `adapter_gpu_trinn1.pt` lastes fra kernel-kilden; Open Pool leses ikke; frø `SEED0+f` med SEED0=100 (assert mot 10); utdata `train_oof_trinn2_seed100.npy`; kontrollinje «trinn1-adapter på train.csv» skal gi ca. 0,5665; `DRY_RUN=1` stopper før modell-last. Trinn 2-oppskriften er uendret (5 målerfolder, E2=2, LR2=5e-5, LRH2=3e-4). Kompilerer.

## Eksakt kommando kl. 20:05
```
cd <repo>
bash arbeid/ntl_mal/ntl_start.sh . --data arbeid/name_that_llm/data --train arbeid/name_that_llm/data/train.csv \
  --test arbeid/name_that_llm/data/test.csv --maal model --tid ingen_tidskolonne --id id --kandidat ntl_c_seed100 --vekt-gb 4
export KAGGLE_API_TOKEN=$(cat state/kaggle/access_token)
env -u VIRTUAL_ENV uvx --with six kaggle kernels push -p arbeid/oppgave_2843/kernel_c
env -u VIRTUAL_ENV uvx --with six kaggle kernels status martinaka/ntl-smed3-c-seed100
# ferdig (ca. 30 min GPU): kernels output martinaka/ntl-smed3-c-seed100 -p arbeid/oppgave_2843/ut
# snitt: 0,5*(arbeid/oppgave_1536/ut/train_oof_trinn2.npy + ut/train_oof_trinn2_seed100.npy) -> NTL_LORA_DIR -> arbeid/oppgave_1618/blend.py
# dom: uv run python arbeid/verktoy/byttregel.py dom --navn ntl_C --tsv resultat.tsv  (rad: ntl_c_seed100 nestet <tall>)
```
Merk: Datasettet har ingen tidskolonne, så `--tid ingen_tidskolonne` (samme som smed2s stempel for B). Vil man kjøre kjernen tom først: legg `DRY_RUN=1` i miljøet i kjernen (koster én kjernestart).

## Sjekket
| Hva | Resultat |
|---|---|
| ntl_start.sh (sperre, lekkasjeport, diskvakt) | ALT GRØNT, exit 0. Kjørt mot midlertidig tmp-repo, ikke landsbyens .git (hook i felles repo under Case 1-frysen ville jeg ikke installere på egen hånd). Stempel: state/ntl_port/ntl_c_seed100.json. |
| blend.py-hash mot låsen ntl_C | stemmer: sha256 afc5f48c…3e98a = låsen (hash e129fe3e1278b3b9) |
| Gammel 1,5B OOF for snittet | arbeid/oppgave_1536/ut/train_oof_trinn2.npy, form (2699, 18) |
| Trinn-1-adapter | arbeid/oppgave_1536/ut/adapter_gpu_trinn1.pt, 70 MB, 394 tensorer; ligger også som utdata i kernel-kilden ntl-smed3-gpu (status: martinaka/ntl-smed3-gpu has status "KernelWorkerStatus.COMPLETE") |
| Datafiler | train.csv 2699 rader, 18 klasser, sha256 lik i ds/ og data/; folds_maaler.npy 2699 rader, folder 0–4 |
| Stisjekk av kjernens glob-logikk | kjørt lokalt uten torch (ingen lokal venv har torch lenger); finner adapter, train og folds |
| Disk / minne | 37,6 GB ledig (krav 20); ca. 7,4 GB ledig+inaktivt RAM av 16 |

## Ikke gjort
- Ingen kjernepush, ingen trening (oppgaven forbyr). Første ekte steg kjøres på Kaggle ved 20:05.
- Lekkasjeporten sjekker bare 3 offentlige testrader; den skjulte testen er større.
