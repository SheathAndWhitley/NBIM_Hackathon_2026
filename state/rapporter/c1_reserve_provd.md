# Case 1: reserveplanen for demoen prøvd med stoppeklokke (#2200, smed, 05.11 13.19–13.22)

Plan: `arbeid/hack/levering/demo/RESERVE.md` (#2191). Frossen modell og agent ikke rørt; bare lesing og kjøring til /tmp.

## Simulerte feil i live-kjøringen (`bash arbeid/hack/c1/demo_saker_2026.sh`)
| Feil | Hva skjedde | Tid til feilen synes |
|---|---|---|
| A. Feil arbeidsmappe (kjørt fra /tmp) | exit 127, `No such file or directory`, tydelig | 0,01 s |
| B. Uten nett (proxy til død port) + tom uv-cache | **Feilet ikke.** exit 0, 15,5 s, byte-lik med reserveutskrift 1 | – |
| D. Kald kopi `fremmed.sh` uten nett (proxy død + UV_OFFLINE=1), ny .venv | **Feilet ikke.** exit 0, 42,7 s, HOVEDTALL 0,476190, TALLVAKT GRØNN (uv-cachen har pakkene) | – |
| C. Ny terminal uten uv i PATH (`env -i PATH=/usr/bin:/bin`) | exit 127, **ingenting på skjermen**. Feilen står bare i `<UTMAPPE>/full.log`: `uv: command not found` | 0,03 s |

## Reserveplanen kjørt fra start til slutt
`env -i PATH=/usr/bin:/bin sh arbeid/hack/levering/demo/reserve/vis_reserve.sh` fra /tmp:
exit 0, **0,037 s**, 122 linjer, alle 4 deler. Hvert steg alene 0,02–0,03 s (exit 0).
Fra feil oppdaget til reserve på skjermen: én kommando, under 10 s inkl. å skrive den.
Innhold: SCORE 0,4818, HOVEDTALL F1 MOT 0,476190, TALLVAKT GRØNN, sak 7 (styret mangler), 3 saker med NBIM-sitat.

## Hva så annerledes ut enn live
1. Øverste linje per del: `RESERVE: <fil> (ferdig kjøring, laget 2026-11-05 13:18:18)`. Live har ingen slik linje. Ellers er sak 1–6 byte-lik med live (B).
2. Ingen ventetid (0,04 s mot 15 s live), så det synes at det er lagret. Si det høyt, som RESERVE.md sier.
3. Del 3 viser tre SCORE-linjer (0,4818 / 0,481752) før HOVEDTALL 0,476190; kan forvirre. Pek på HOVEDTALL-linja.
4. Tidsstempelet 13:18 er før frys. Er `lag_reserve.sh` ikke kjørt på nytt etter kl. 16, ser juryen et tidspunkt før frysen.

## Funn og rettelse
- Nett er ikke en reell risiko: .venv finnes, uv trenger ikke nett. Den reelle risikoen er C: stille feil.
  Lagt inn rad i feiltabellen i RESERVE.md: tom skjerm/exit 127 → `export PATH=/opt/homebrew/bin:$PATH`, ellers `vis_reserve.sh 1`.
- Ikke rettet i demo_saker_2026.sh (sender feil til full.log); forslag for #1975/#2205: `|| { tail -3 "$UT/full.log"; exit 1; }` etter linje 9, men bare om ordføreren vil røre demoskriptet før frys.
- Etter frys (#1975): kjør `lag_reserve.sh` på nytt, sjekk at SHA.txt viser frysvakt grønn.
