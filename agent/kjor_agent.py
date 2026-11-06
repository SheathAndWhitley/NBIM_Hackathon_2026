"""Stemmeagenten (Case 1): foreslår FOR eller MOT styret for hver generalforsamlingssak, med kalibrert P(MOT),
sitat fra NBIMs retningslinjer og ruting til menneske. Selve agenten ligger i kjerne.py.

Bruk (fra repo-roten, i miljøet sh KJOR.sh lager):
  .venv_kjor/bin/python agent/kjor_agent.py --ut ut                     test 2026 (ut/inndata/test_2026.csv)
  .venv_kjor/bin/python agent/kjor_agent.py --csv saker.csv --ut UTMAPPE  egne saker i real_votes-format uten fasitfelt
  .venv_kjor/bin/python agent/kjor_agent.py --sak '{"meeting_id": ...}' --ut UTMAPPE
Ut (i --ut): agent.csv (svar per sak), pred_maaler.csv og _pred_uten_ruting.csv (for maaling/maaler.py).
"""
import argparse, os, sys

HER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HER)


def main():
    import kjerne
    p = argparse.ArgumentParser(description="Stemmeagenten (Case 1) på NBIMs stemmer (real_votes-format).")
    p.add_argument("--csv", help="saker i real_votes-format uten fasitfelt (standard: test 2026, ut/inndata/test_2026.csv)")
    p.add_argument("--sak", help="én sak som JSON-objekt med feltene " + ",".join(kjerne.TRENG) + " (+ mgmt_rec, country, market)")
    p.add_argument("--historikk", default=kjerne.REAL, help="NBIMs tidligere stemmer (data/real_votes.csv)")
    p.add_argument("--vindu", default=None, help="mål mot fasit med maaling/maaler.py (test|val); standard test når --csv og --sak mangler")
    p.add_argument("--ut", required=True, help="utmappe (opprettes)")
    p.add_argument("--baand", default="0.15,0.85", metavar="LO,HI",
                   help="til menneske når kalibrert P(MOT) er i [LO, HI) (standard 0.15,0.85)")
    p.add_argument("--til-menneske", type=float, default=None, metavar="PROSENT",
                   help="alternativ ruting i stedet for --baand: andel saker nær grensen (logit-bånd låst på val 2025)")
    a = p.parse_args()
    if a.til_menneske is not None and not 0 <= a.til_menneske <= 100: sys.exit("--til-menneske må være mellom 0 og 100")
    try:
        lo, hi = (float(x) for x in a.baand.split(",")); assert 0 <= lo <= hi <= 1
    except (ValueError, AssertionError): sys.exit("--baand må være LO,HI med 0 <= LO <= HI <= 1")
    if a.vindu is None and not a.csv and not a.sak: a.vindu = "test"
    kjerne.main(a, None if a.til_menneske is None else a.til_menneske / 100)


if __name__ == "__main__":
    main()
