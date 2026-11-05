#!/bin/sh
# dommer2 #2507: kjør to rare innfiler fra kald jury-zip (pakket av meg, /tmp/dommer2_2507/jury.zip)
set -u
B=/tmp/dommer2_2507; INN=arbeid/oppgave_2499/inn
rm -rf $B/ut; mkdir -p $B/ut; cd $B/ut && unzip -q $B/jury.zip
R=$B/ut/c1_stemmeagent
cd $R && shasum -a 256 -c -q FROSNE_SHA256.txt && echo "FRYSVAKT GRØNN i zip ($(grep -c . FROSNE_SHA256.txt) filer)"
mkdir -p $R/home
UV_PROJECT_ENVIRONMENT=$R/.venv uv sync --frozen --no-install-project -q && echo "uv sync ok"
for f in d_semikolon e_aar2027_ukjent; do
  echo "=== $f"
  env -i HOME=$R/home PATH=$R/.venv/bin:/usr/bin:/bin LANG=C.UTF-8 $R/.venv/bin/python $R/arbeid/hack/levering/kjor_agent.py --ut $B/res_$f --csv $INN/$f.csv
  echo "UTGANG $?"
done
