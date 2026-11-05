#!/bin/bash
# #2867: Case 1 natt-måler, én kommando. Bruk: mal_kandidat.sh SVARMAPPE [--av NAVN] [--vinkel TEKST] [--oppgave ID] [--torr]
# Krever REGEL.md skrevet før svarfilene (mtime), måler F1 MOT på 2023 (vakt) + 2024/25/26 mot frossen repo4, skriver BYTT/STÅR
# i SVARMAPPE/DOM.md og fører forsøket på tavla. Se mal_kandidat.py for detaljer.
exec python3 -I "$(cd "$(dirname "$0")" && pwd)/mal_kandidat.py" "$@"
