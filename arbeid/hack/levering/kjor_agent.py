"""Case 1, hele stemmeagenten med én kommando (smed #1998, real_votes som standard fra #2053).

Bare arrangørens data (ordre #242): NBIMs stemmer i state/opplastet/20261105_114241_real_votes.csv og
hack/c1/data_off/real_*.csv avledet av den (maaler_offisiell_v3.py lag --data real). Modellen er smed2s
MOT-modell #2044 (oppgave_2044/train.py, miks h2), kjørt uendret via c1_real.py.
Den gamle N-PX-agenten (--data v3, egen skraping) er tatt ut; koden ligger i arkiv/kjor_agent_med_v3_foer_242.py.

Bruk (fra landsbymappen):
  uv run --project arbeid/kandidater/smed2_c1_mot python arbeid/hack/levering/kjor_agent.py --ut /tmp/c1_ut
  ... --csv min_fil.csv --ut DIR        ... --sak '{"meeting_id": "...", ...}' --ut DIR   (real_votes-format)
Standard inn er holdout 2026 (hack/c1/data_off/real_test_input.csv), målt med maaler_offisiell_v2.py.
Ut (i --ut): agent.csv med stemmeforslag, P(MOT), ruting til menneske, punkt og sitat, pluss
pred_maaler.csv, _pred_uten_ruting.csv og KJORING.txt.
"""
import argparse, os, sys

HER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HER)


def main():
    if "--data" in sys.argv and sys.argv[sys.argv.index("--data") + 1:][:1] == ["v3"]:
        sys.exit("--data v3 (gammel N-PX-agent på egen skraping) er tatt ut (ordre #242): bare arrangørens real_votes "
                 "brukes. Gammel kode: hack/levering/arkiv/kjor_agent_med_v3_foer_242.py")
    return main_real()


def main_real():
    """Standard (#2053): NBIMs egne stemmer (real_votes) med smed2s MOT-modell #2044, se c1_real.py."""
    import c1_real
    p = argparse.ArgumentParser(description="Case 1-agenten på real_votes (standard).")
    p.add_argument("--csv", help="saker i real_votes-format uten fasitfelt (standard: test 2026, data_off/real_test_input.csv)")
    p.add_argument("--sak", help="én sak som JSON-objekt med feltene " + ",".join(c1_real.TRENG) + " (+ mgmt_rec, country, market)")
    p.add_argument("--historikk", default=c1_real.REAL, help="NBIMs tidligere stemmer (real_votes.csv)")
    p.add_argument("--vindu", default=None, help="mål mot fasit med maaler_offisiell_v2 (test|val); standard test når --csv og --sak mangler")
    p.add_argument("--ut", required=True, help="utmappe (opprettes)")
    p.add_argument("--baand", default="0.15,0.85", metavar="LO,HI",
                   help="til menneske når kalibrert P(MOT) er i [LO, HI) (standard 0.15,0.85, valgt i #2128)")
    p.add_argument("--til-menneske", type=float, default=None, metavar="PROSENT",
                   help="gammel ruting i stedet for --baand: andel saker nær grensen (logit-bånd låst på val 2025)")
    a = p.parse_args()
    if a.til_menneske is not None and not 0 <= a.til_menneske <= 100: sys.exit("--til-menneske må være mellom 0 og 100")
    try:
        lo, hi = (float(x) for x in a.baand.split(",")); assert 0 <= lo <= hi <= 1
    except (ValueError, AssertionError): sys.exit("--baand må være LO,HI med 0 <= LO <= HI <= 1")
    if a.vindu is None and not a.csv and not a.sak: a.vindu = "test"
    c1_real.main(a, None if a.til_menneske is None else a.til_menneske / 100)


if __name__ == "__main__":
    main()
