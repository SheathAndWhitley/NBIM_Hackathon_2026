# Case 1 #2521: fire feilhenvisninger i jurytekstene rettet

Lista: `c1_tallkontroll.md`, «Avvik». Ingen av de fire var rettet av #2509 (dom #2523 bekreftet dette). Ingen tall er endret, ingen frosne filer er rørt.

1. `arbeid/hack/c1/DEMO_MANUS.md:60` «96 av 100» peker nå på `leveranse/kilder/TREFFSIKKERHET.md:16` (96,2 % følg styret).
2. `leveranse/kravrespons.md:7` 194 selskaper / 37 land / 24 sakstyper peker på `kilder/omfang.txt`. `omfang.py` skriver nå også antall sakstyper (24, en ny linje, resten lik), og `omfang.txt`/`omfang.py` er kopiert til `leveranse/kilder/`.
3. `leveranse/JURY.md:28-29` 95,7 % peker på `kilder/TREFFSIKKERHET.md:16`, og avvik-F1 0,482 på `kilder/c1_bootstrap_f1.md:6` (TREFFSIKKERHET har ikke 0,482).
4. `c1_bootstrap_f1.md`, `c1_neste_steg.md`, `c1_valgt_bort.md` og `c1_huskeregel.md` kopiert til `leveranse/kilder/`. `ERLIG_EVALUERING.md` § 6 peker på `kilder/c1_bootstrap_f1.md:16`; `JURY_SPORSMAL.md` pkt. 11 og `NESTE_VERSJON.md` (fire pekere) har byttet `landsbyrapport:` mot `kilder/`.

LESMEG i kilder/ har fått en linje om de seks nye filene.

Kontroll: frysvakt GRØNN (17 filer), tallvakt 18 filer, 169 påstander, 0 avvik (F1 MOT 0,4762). `frys_diff --kilde` før regenerering: 7 ENDRET + 6 NY, alle forventede; `frys_fasit_1600.sha256` regenerert (137 filer), FRYS LIK.

Merk: `leveranse/kravrespons.md` er ikke sporet i git (arbeid/ er ignorert), så rettingen der står bare på disk og kommer med i zipen via pakk_jury.sh. `JURY_SPORSMAL.md` hadde en annens ucommittede endring (linje 62, «sak 2511» → «sak #2511»); den ble med i commiten.
