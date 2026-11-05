# Case 1: NBIMs egne begrunnelser for MOT-stemmer (sitatkilde, #1977)

**Kilde:** nbim.no stemmedatabase (our-voting-records → møteside `meeting?m=<id>`), feltet «Vote rationale» + lenker til Global Voting Guidelines / posisjonsnotat. Bare GET, rå HTML cachet i `arbeid/speider/c1begr_raa/`.
**Skript:** `arbeid/speider/c1begr/hent_begrunnelser.py` (stdlib, `python3 -I`, cache gjør omkjøring rask).

## Filer (arbeid/hack/c1/kilder/)
- `nbim_begrunnelser.csv`: 999 ikke-FOR-punkt på 402 møter (Against 742, Withhold 121, Do not vote 86, frekvens 50). Kolonner: utsteder, moetedato, forslag, styret_rek, nbim_stemme, begrunnelse, retningslinje, retningslinje_url, `etter_test_start`.
- `nbim_begrunnelser_saypay.csv`: 414 rader, én per say-on-pay-rad i train/test med MOT, koblet til case-id.

## Dekning
| | rader | med begrunnelse |
|---|---|---|
| Say-on-pay MOT, **test** | 129 | **113 (88 %)** |
| Say-on-pay MOT, train | 285 | 254 (89 %) |
| Alle punkt, etter test-start | 278 | 249 |
| Alle punkt, før test-start | 721 | 550 |

## Lekkasjevakt
`etter_test_start=1` betyr møtedato ≥ 2025-07-01 (test-start). Disse begrunnelsene er skrevet *etter* stemmen og avslører fasiten. Sitatagenten skal bare bruke rader med `etter_test_start=0` som eksempelbank/sitat ved prediksjon; testrader brukes kun til evaluering/demo av forklaring etter at stemmen er avgjort.

## For Smeden / sitatagenten
1. Bygg sitatbank fra train-begrunnelsene (mange er standardtekster per tema, f.eks. golden parachutes/CEO-lønn) → map forslagstype → begrunnelse + retningslinjelenke.
2. Mål sitattreff på test ved å sammenligne valgt tema mot NBIMs faktiske begrunnelse (113 test-MOT har fasit-begrunnelse).
