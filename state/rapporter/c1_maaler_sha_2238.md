# Case 1: papirene bruker nå måler-sha 418a937e57 (#2238)

**Hvorfor sha-en endret seg:** I #2221 la arkitekten inn en datavakt i `maaler_offisiell_v3.py`. Den sjekker sha256 og antall rader i datafila. Selve målingen er den samme, og tallet er fortsatt 0,476190.

**Endret:**
- `arbeid/hack/c1/leveranse/JURY.md` linje 40: sha er 8b09c36e01 → 418a937e57, med én setning om hvorfor.
- `arbeid/hack/c1/tall_tabell.md`: generert på nytt med `lag_tall_tabell.py`. Diffen viser at bare sha og tidspunkt endret seg, ingen tall.
- DEMO_MANUS.md, JURY_METODE.md og levering/JURY*.md oppga ingen sha. kravrespons.md er ikke rørt (#2229 er åpen), og den har heller ingen gammel sha.

**Funn underveis:** Første kaldstart var RØD med `ModuleNotFoundError: injeksjon_hoflig`. c1_real.py importerer nå den nye modulen fra smed3 (#2237), men fila var ikke med i kopilista. Jeg la `hack/levering/injeksjon_hoflig.py` inn i kopilista i både `kaldstart.sh` og `levering/fremmed.sh`.

**Bevis:**
- `bash arbeid/hack/c1/kaldstart.sh` ga exit 0, `GRØNN F1_MOT 0.476190 REF 0.476190 AVVIK +0.000000` og `måler sha256[:10] 418a937e57`. Logg: `arbeid/oppgave_2238/kald.log`.
- `grep -rn 8b09c36e01 arbeid/hack/c1/leveranse/ arbeid/hack/c1/DEMO_MANUS.md arbeid/hack/c1/JURY_METODE.md arbeid/hack/c1/tall_tabell.md arbeid/hack/levering/JURY*.md` gir ingen treff.
