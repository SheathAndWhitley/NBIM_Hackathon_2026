"""Sitatvakt for Case 1 (arkitekt #2150): alle sitater i agentens svar har kilde, og kilden har teksten ordrett.

To slags sitater i agent.csv (kjor_agent.py):
  A retningslinje_id + retningslinje_sitat: NBIMs GVG-punkt. Krav: id finnes, sitatet står ordrett i NBIMs
    rå HTML (arbeid/speider/c1ret_raa/nbim_gvg.html), og nummeret stemmer med nummeret utledet fra HTML-
    overskriftene (h3 = prinsipp, h4 = delpunkt, avsnitt = ledd; samme metode som dommer2 #2143).
    «NBIM 0.0.x» er innledningen før første prinsipp: bare ordrett-kravet.
  B sitat + sitat_kilde: NBIMs egen begrunnelse fra real_votes. Krav: kilde finnes, og sitatet står ordrett
    i rationale_text for samme selskap og år i real_votes-fila.
Bruk:  python3 -I arbeid/hack/c1/sitatvakt.py <agent.csv> [--rot LANDSBY]
Siste linje: SITATVAKT OK|AVVIK A <ok>/<n> B <ok>/<n>. Utgang 0 = OK, 1 = avvik.
"""
import csv, html, os, re, sys

args = sys.argv[1:]
ROT = "."
if "--rot" in args:
    i = args.index("--rot"); ROT = args[i + 1]; del args[i:i + 2]
AGENT = args[0]
GVG = os.path.join(ROT, "arbeid/speider/c1ret_raa/nbim_gvg.html")
VOTES = os.path.join(ROT, "state/opplastet/20261105_114241_real_votes.csv")


def n(t):
    t = html.unescape(re.sub(r"<[^>]+>", " ", str(t)))
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("\xa0", " ")
    return re.sub(r"\s+", " ", t).strip().lower()


raw = open(GVG, encoding="utf-8").read()
fulltekst = n(raw)
num = {}; h3 = h4 = ledd = 0
for m in re.finditer(r"<(h3|h4|p|li)[^>]*>(.*?)</\1>", raw, re.S):
    tag, txt = m.group(1), n(m.group(2))
    if tag in ("h3", "h4"):
        k = re.match(r"(\d+)\.", txt)
        if not k: continue
        if tag == "h3": h3, h4 = int(k.group(1)), 0
        else: h4 = int(k.group(1))
        ledd = 0; continue
    if h3 and txt: ledd += 1; num.setdefault(txt, f"NBIM {h3}.{h4}.{ledd}")

begr = {}  # (selskap, år) -> samlet rationale_text
with open(VOTES, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r.get("rationale_text"):
            k = (r["company"].strip(), r["year"].strip())
            begr[k] = begr.get(k, "") + " || " + n(r["rationale_text"])

rader = list(csv.DictReader(open(AGENT, encoding="utf-8")))
feil = []; a_n = a_ok = b_n = b_ok = 0
for r in rader:
    s, rid = (r.get("retningslinje_sitat") or "").strip(), (r.get("retningslinje_id") or "").strip()
    if s or rid:
        a_n += 1; ns = n(s)
        if not s or not rid: feil.append(f"A {r['id']}: sitat uten id eller id uten sitat ({rid!r})")
        elif ns not in fulltekst: feil.append(f"A {r['id']}: {rid} står ikke ordrett i NBIMs HTML: «{s[:80]}»")
        elif not rid.startswith("NBIM 0.") and rid not in [v for k, v in num.items() if ns in k]:
            feil.append(f"A {r['id']}: nummer {rid} stemmer ikke med HTML ({[v for k, v in num.items() if ns in k]})")
        else: a_ok += 1
    s, kilde = (r.get("sitat") or "").strip(), (r.get("sitat_kilde") or "").strip()
    if s or kilde:
        b_n += 1
        m = re.match(r"NBIMs begrunnelse (\d{4}), (.*?): «", kilde)
        if not s or not kilde: feil.append(f"B {r['id']}: sitat uten kilde eller kilde uten sitat")
        elif not m: feil.append(f"B {r['id']}: ukjent kildeformat «{kilde[:60]}»")
        elif n(s).rstrip(".… ") not in begr.get((m[2].strip(), m[1]), ""):
            feil.append(f"B {r['id']}: sitatet står ikke i NBIMs begrunnelse {m[2]} {m[1]}: «{s[:80]}»")
        else: b_ok += 1

for x in feil[:15]: print("  " + x)
if len(feil) > 15: print(f"  ... og {len(feil) - 15} til")
ok = not feil and a_n > 0
print(f"SITATVAKT {'OK' if ok else 'AVVIK'} A {a_ok}/{a_n} GVG-sitater ordrett med riktig nummer, "
      f"B {b_ok}/{b_n} begrunnelsessitater ordrett i kilden ({len(rader)} rader)")
sys.exit(0 if ok else 1)
