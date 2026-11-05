# Case 1 sluttkontroll 2 (#2171) etter juryrettingene: PASS, 32 s

Kommando: `bash arbeid/hack/c1/sluttkontroll.sh` (RAPP=/tmp/c1_sk2.md), kald kopi `/tmp/c1_sluttkontroll`, git e74453d, 13:10, etter at #2167 (smed2) og #2168 (smed3) var done.

| status | krav | forskjell fra #2163 (13:05) |
|---|---|---|
| GRØNT | 1 kald start | ingen (utgang 0; 30 s mot 27 s) |
| GRØNT | 2 F1 MOT = 0,476 | ingen (0.476190 kald uten/med ruting og frossen #2103) |
| VENTER | 3 modellfiler uendret siden frys | ingen (frys kl. 16, `state/c1_frys.json` finnes ikke ennå) |
| GRØNT | 4a tall, kald kjøring | 14 filer / 136 påstander, 0 avvik (før 13 / 129). Ny fil: `levering/TREFFSIKKERHET.md` (13:10) |
| GRØNT | 4b tall, lagrede filer | samme som 4a |
| GRØNT | 5 sitater | ingen (1578/1578 GVG, 74/74 begrunnelser) |
| GRØNT | 6 varighet | 32 s mot 29 s |

## Funnet og rettet underveis: falsk alarm i tallvakta
Mellomkjøring 13:08 (etter #2168, mens #2167 pågikk) ga FAIL 4a/4b: `levering/README.md:29: antall MOT 1, måleren sier 58`. Linja er smed2s nye «**HOVEDTALL F1 MOT mot styret 0,4762**». Regexen `(?<![\d,.–-])(\d+) MOT mot styret` leste «F**1** MOT mot styret» som 1 MOT. Rettet i `arbeid/verktoy/c1_tallvakt.py` linje 84: bakoverblikket utelukker nå `\w` (også bokstaver). Pakka var riktig; feilen var i verktøyet.
- Negativtest: plantet «57 MOT mot styret» + «F1 MOT mot styret 0,4762» i en fil. KP: forventet 1 avvik (57), fikk 1.
- arbeid/ er ikke i git (gitignore), så rettingen står bare på disk.

## Risiko
#2162 (smed) kjører agenten på nytt og skriver utskriftene. Endrer det antallet til menneske (188/183), kan 4b falle. Kjør sluttkontrollen på nytt etter #2162 og etter frys kl. 16 (30 s).
