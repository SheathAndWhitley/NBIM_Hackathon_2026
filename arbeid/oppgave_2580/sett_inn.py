"""Setter byttedom-setningen (#2580) inn i README.md og kravrespons.md, og sluttfører den når byttet er avgjort.

Bruk (fra landsbymappen):
  uv run python -I arbeid/oppgave_2580/sett_inn.py --dom [--torr]          # dommen slik den står kl. 17:02: BYTT på vilkår
  uv run python -I arbeid/oppgave_2580/sett_inn.py --sluttfor BYTT|STAAR   # etter bytt.sh --utfor (grønt) eller tilbakerulling
Idempotent: finnes markøren fra før, settes ingenting inn. Bare tall fra dom #2570 (c1_byttedom_265.md).
Linjene har tallvakt-markør, så bytt_tall.py rører dem ikke.
"""
import argparse, pathlib, sys

ROT = pathlib.Path(__file__).resolve().parents[2]
README = ROT / "arbeid/hack/c1/leveranse/README.md"
KRAV = ROT / "arbeid/hack/c1/leveranse/kravrespons.md"
MARK = "<!-- tallvakt: ignorer: byttedom, ikke hovedtall -->"
VILKAR = "på vilkår om grønn pakke innen 18:45"
SLUTT = {"BYTT": "og byttet ble gjennomført, så tallene i denne pakka er fra repo4",
         "STAAR": "men byttet ble ikke grønt før tekststopp, så den frosne agenten står med 0,476"}

README_T = ("> Etter modellfrysen testet vi, etter en regel satt før måling (snitt minst +0,02 over frossen på F1 MOT over tre "
            "rullende testår 2024–2026, intet år under −0,02), kandidaten repo4 (frossen + fire historikktrekk): "
            "0,5057/0,5309/0,5120 mot frossen 0,4545/0,5143/0,4762, snitt +0,0345, verste år +0,017, KI for snittet "
            f"[−0,005; +0,078], og kontrollagenten dømte BYTT kl. 17:02 {VILKAR} (se `ERLIG_EVALUERING.md` § 7). {MARK}\n")
KRAV_T = (" Etter frysen prøvde vi én kandidat etter en regel satt før måling på tre testår (2024–2026): repo4 ga snitt "
          f"+0,0345 over frossen og intet år under, og kontrollagenten dømte BYTT kl. 17:02 {VILKAR}. {MARK}")

def sett_inn(sti, anker, linje, torr):
    s = sti.read_text()
    if MARK in s:
        print(f"{sti.name}: finnes fra før, hopper over"); return
    if anker not in s:
        sys.exit(f"{sti.name}: fant ikke ankeret: {anker[:60]}")
    if torr:
        print(f"--- {sti.name} (tørr) ---\n{linje}"); return
    sti.write_text(s.replace(anker, anker + linje, 1)); print(f"{sti.name}: satt inn")

def sluttfor(sti, utfall):
    s = sti.read_text()
    if VILKAR not in s:
        sys.exit(f"{sti.name}: vilkårsteksten finnes ikke (allerede sluttført, eller ikke satt inn)")
    sti.write_text(s.replace(VILKAR, SLUTT[utfall], 1)); print(f"{sti.name}: sluttført {utfall}")

p = argparse.ArgumentParser()
p.add_argument("--dom", action="store_true")
p.add_argument("--sluttfor", choices=["BYTT", "STAAR"])
p.add_argument("--torr", action="store_true")
a = p.parse_args()
if a.dom:
    # README: ny >-linje etter V2-linja i Hovedtall-boksen
    sett_inn(README, "<!-- tallvakt: ignorer: V2, ikke hovedtall -->\n", README_T, a.torr)
    # kravrespons: i «Hvordan vi verifiserte det», etter setningen om val 2025 / test 2026 (metode, ikke hovedtall)
    sett_inn(KRAV, "kjørt én gang på 2026, med 95 %-intervall [0,36; 0,59].", KRAV_T, a.torr)
elif a.sluttfor:
    sluttfor(README, a.sluttfor); sluttfor(KRAV, a.sluttfor)
else:
    p.print_help()
