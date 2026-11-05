# Name that LLM: bygg_snitt.py for oppgave A er skrevet, og tørrsjekken er grønn (#2862)

- Fila er `arbeid/oppgave_2561/bygg_snitt.py`, en kopi av `oppgave_1630/bygg.py` utvidet etter steg 3 i `oppgave_2850/KLAR.md`. Kjernen (`kernel_snitt/ntl_kjede.py`) gjør dette:
  a) kjører `lora_sub.py` to ganger: 1,5B med adapter fra `ntl-smed3-gpu`, så 3B med adapter fra `ntl-smed2-3b`. Hver kjøring har sin egen `NTL_LORA_UT` og sin egen tidsgrense (T0 nullstilles).
  b) snitter test-probaene og `*_sjekk_tr1.npy`, og printer `SJEKK snitt trinn1 train.csv bal.acc X (forventet ca. 0,5776)`.
  c) kjører `kjede_kaggle.py` med `NTL_LORA` satt til snittet, og med vektene og skiftet fra `--vekter`.
  d) metadata: slug `martinaka/ntl-landsby-sub-snitt`, begge adapterkernelene, begge modellene (1.5b/1 og 3b/1), T4 og internett av.
- Koden i kjernen hentes uendret fra `oppgave_1630/kode`. Den frosne `oppgave_1618/blend.py` er ikke rørt (sha `afc5f48c86cc2d0d`).

## Tørrsjekk (uten trening, uten innsending, uten GPU)
`uv run --project arbeid/oppgave_1618 python arbeid/oppgave_2561/bygg_snitt.py --torr` ga **TORR SJEKK GRØNN** med exit 0:
- sha-en til den frosne blend.py stemmer. Fra falsk rot `arbeid/oppgave_2561/rot/kjor` finnes `../oppgave_1616/oof_raa.npz` (symlenke) og `../oppgave_1536/ut/{train_oof_trinn2,train_proba}.npy`.
- Snitt-OOF-en (steg 1, likt snitt av 1536 og 1622, formen 2699×18) fantes ikke. Tørrsjekken laget den, uten trening.
- Kjernen kjørte med `NTL_TORR=1` mot et falskt `/kaggle/input`-tre og fant data, pool.npz, begge grunnmodellmappene, **begge adapterne** (1,5B gir smed3-gpu og 1536, 3B gir smed2-3b og 1622), qwen og bge. Etter det avsluttet den før trening.
- `ntl_start.sh` (kommando 0 i KLAR.md) er fortsatt **GRØNN** på 5/5 med exit 0.

## Ærlige forbehold
- `kernel_snitt` er nå bygget med **plassholder-vekter** (`oppgave_1630/vekter9_15b.json`), fordi `rot/kjor/vekter9.json` ikke finnes ennå. Før push: kjør steg 2 (den frosne blend.py fra rot/kjor), og bygg på nytt uten `--torr`. Da hentes `rot/kjor/vekter9.json` automatisk. Uten `--torr` nekter skriptet å bygge hvis den fila mangler.
- Røyktesten på CPU (roykt.sh, 0,5B) er ikke kjørt. Qwen2.5-0.5B er borte fra HF-cachen (der ligger bare 7B nå). I tørrmodus prøves derfor bare stien til qwen, gjennom en tom config.json. Selve kjøringen av to modeller etter hverandre er altså ikke prøvd lokalt. Tid og minne på T4 er heller ikke målt.
- Ingen Case 1-filer er rørt.
