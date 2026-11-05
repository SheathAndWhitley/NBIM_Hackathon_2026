# Case 1: tallvakt på JURY.md, DEMO_MANUS og jury-zipen etter frysen (#2470)

Kjørt av smed3 05.11 kl. 16.05–16.17, verktøy `arbeid/verktoy/c1_tallvakt.py` (måler v3 `--score mot`
på `levering/kjor_agent_real_maskin_alene.csv`: TP 30 FP 38 FN 28, P 0.4412, R 0.5172, F1 0.4762, 58 i fasit;
ruting 183 av 1539 med fasit, 188 av 1578 inn). Ingen tekst rettet av meg.

## Resultat: 0 avvik

| Hva | Påstander sjekket | Avvik |
|---|---|---|
| `arbeid/hack/c1/leveranse/JURY.md` (16.06) | 9 | 0 |
| `arbeid/hack/c1/DEMO_MANUS.md` (16.13) | 9 | 0 |
| Jury-zip, fersk bygging kl. 16.14 (`/tmp/jurypakke_c1_tv2470.zip`, 117 filer): alle `levering/*.md`, `c1/leveranse/*.md` og `DEMO_MANUS.md` i zipen | 178 i 19 filer | 0 |
| Jury-zip som lå på `/tmp/jurypakke_c1.zip` (bygd 15.45) | 168 i 18 filer | 0 |

JURY.md og DEMO_MANUS.md i den ferske zipen er byte-like med kildefilene.

## Ett avvik som ble rettet av andre underveis
Første kjøring kl. 16.08 ga 1 avvik: `arbeid/hack/c1/DEMO_MANUS.md:63` «F1 MOT 0,476190», måleren skriver 4 desimaler (0.4762).
Tallet var riktig (30/63 = 0,476190…), men vakta krever samme antall desimaler. Linja ble endret til
«F1 MOT 0,4762 (0.476190)» kl. 16.13 (commit 7a5d892, sak 2487) før jeg var ferdig; ny kjøring gir 0 avvik.

## Merk
- Zipen på `/tmp/jurypakke_c1.zip` er fra kl. 15.45: den mangler `DEMO_MANUS.md` (pakk_jury.sh kopierer den nå) og har
  en eldre JURY.md (pkt. 11 uten henvisningen til `kilder/c1_motstand_etter_frys.md`). Den må bygges på nytt før
  levering: `sh arbeid/hack/levering/pakk_jury.sh`. Min ferske bygging ligger på egen sti og rører ikke den.
- Tallvakta kjørt på *alle* 60 .md i zipen (også `kilder/`) gir 41 treff, men ingen er avvik på hovedtallet: det er
  robusthetsvarianter (`c1_robusthet_frossen.md`: tom_tekst, uten_styret osv.), val 2025-tall (99 i fasit),
  alternativ A+B (`c1_beslutning_nyeste_historikk.md`) og «0,476190» med 6 desimaler i fire kildefiler
  (`c1_kjoretid.md:14`, `c1_robusthet_kald_2380.md:3`, `c1_injeksjon_hoflig.md:26`, `c1_beslutning_nyeste_historikk.md:10`).
  `kilder/` er utenfor vaktas standardomfang (sluttsjekk.sh steg 3), så dette er ikke krav om retting.

Logger: `/tmp/tv_2470_filer.txt`, `/tmp/tv_2470_zip_std.txt`, `/tmp/tv_2470_zip2_std.txt`, `/tmp/tv_2470_zip.txt`.
