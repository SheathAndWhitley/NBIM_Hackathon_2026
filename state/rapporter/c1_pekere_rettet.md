# Case 1: to interne pekere rettet før frysen (#2454, smed3, 05.11)

Fra speiderens sortering `state/rapporter/c1_pekere_uten_sti.md`, bøtte c, punkt 4 og 5. Bare tekst, ingen tall eller kode endret.

## Gjort
1. `arbeid/hack/c1/leveranse/ERLIG_EVALUERING.md`
   - linje 48: «gammelt skript `hist_regel.py`» → «gammelt internt skript, ikke i pakka».
   - linje 70: «ligger i `hist_regel.py`» → «er beskrevet i `kilder/c1_enkle_regler_og_hist1.md` (selve skriptet er et gammelt internt skript, ikke i pakka)». Fila finnes i zipen.
   - `hist_regel.py` forekommer ikke lenger i fila.
2. `arbeid/hack/c1/leveranse/kilder/LESMEG.md`: én ny linje rett under overskriften som sier at filnavn uten sti i kildene (abl.py, val_pred.py, reprod.sh, gvg2024.txt o.l.) viser til lagets interne arbeidsmapper og ikke er med i pakka, og at tallene står ferdig målt i teksten.

## Kontroll
- Tallvakta på de to filene: 15 påstander stemmer, 0 avviker.
- Tallvakta på hele pakka: 18 filer, 168 påstander, 0 avviker (likt nullpunktet før endringen).
- Ikke rørt: pakk_jury.sh, JURY/JURY_SPORSMAL/NESTE_VERSJON, DEMO_MANUS.

## Merk
`arbeid/` er gitignorert; de to filene er lagt til med `git add -f`, slik JURY.md og de andre leveransefilene er sporet fra før.
