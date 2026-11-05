# Case 1: jury-zipen har nå kandidatens pyproject.toml og uv.lock (#2475, smed4)

## Retting
- `arbeid/hack/levering/pakk_jury.sh`: etter `kopier $FILER` kopieres `arbeid/kandidater/smed2_c1_mot/pyproject.toml`
  og `uv.lock` til zip-rota (samme filer som fremmed.sh måler med), og skriptet stopper hvis byggemappas uv.lock
  ikke er kandidatens. Før tok `kopier` landsbyens rotfiler (395499ad…/66faa0a3…: torch, catboost, claude-agent-sdk).
- `frys_fasit.py`: `rot_kopi` peker på kandidatens filer. Fasiten er regnet på nytt (117 filer).
- `JURY_README.md`: «laster ned ca. 230 MB» → «ca. 80 MB låste pakker (ca. 230 MB pakket ut)».
- Funnet underveis: i HEAD (bb8289f, #2469) lå speider-linja i pakk_jury.sh etter `echo "3/5..."`, utenfor
  `kopier`. `sh -n` feilet (syntaksfeil linje 43), så pakk_jury.sh i HEAD kunne ikke kjøres. Arbeidsfila hadde
  linja riktig plassert, og den er det som er committet nå.

## Akseptkrav
1. Ny zip bygd i egen mappe: `/tmp/s4_2475/jurypakke_c1.zip` (117 filer, sha256 c14a4636…3218), byggemapper
   `/tmp/s4_2475/bygg` og `/tmp/s4_2475/stage`.
2. pyproject.toml i zipen: sha256 96fcf3b1c1089027cddcf815ff4266268a8d45f38151be33ba760fe596607d50 (name «smed2-c1-mot»),
   uv.lock: ed54fd6c8f92f347a7c58d2af5986c153921ba46a89fb7244bff70ee2f7c21a6. Begge er kandidatens.
3. Kaldstart med `test_jury_zip.sh` (tom HOME og uv-cache, sandkasse som nekter landsbymappa), to ganger:
   ZIPTEST GRØNN, HOVEDTALL F1 MOT 0.476190, TP 30 FP 38 FN 28 TN 1443 STEMMER, prediksjonsfila lik den frosne.
4. `frys_fasit.py` regnet på nytt; `frys_diff.sh` mot zipen: FRYS LIK 0 avvik; `--kilde`: FRYS LIK 0 avvik.
   `c1_frys.py sjekk --krev`: GRØNN før og etter (17 filer like som ved frys 16:00:01).
5. Størrelse målt fra tom cache: uv-cache 233 MB (utpakket), .venv 265 MB etter `du` (APFS-kloner fra cachen),
   nedlasting ca. 81 MB (sum av macOS arm64-hjulene i uv.lock, 20 pakker). uv sync 3 s, hele kjøringen 47–73 s.
   README sa «laster ned ca. 230 MB». Det var størrelsen pakket ut, ikke nedlastingen, så teksten er rettet.
