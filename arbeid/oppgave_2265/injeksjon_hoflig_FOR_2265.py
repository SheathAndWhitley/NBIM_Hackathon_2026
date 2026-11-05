"""Høflige og omskrevne instrukser i forslagsteksten (#2237). Utfyller vern.py (#2047) og EKSTRA_INJ (#2063).

To signaler, begge sjekket mot NBIMs historiske forslagstekster (år < 2026):
1) RETTET: ord som henvender seg til den som stemmer (please, kindly, we, recommend, urge, should, ...) eller ber om
   en retning (vote with/for/against, support/follow the board, reject, oppose). Ingen av dem står i historikken.
2) PROSA: forslagstitler er Title Case; små bokstaver brukes nesten bare til småord (of, as, and, to, ...). To eller
   flere ord med små bokstaver som er sjeldne (< 2 ganger) i historikken betyr at noen har skrevet en setning inn.
finn(tekst) -> posisjon der instruksen starter, eller None.
"""
import re
from collections import Counter

RETTET = re.compile(
    r"(?i)\b(please|pls|kindly|we|our|recommend\w*|urg(e|es|ed|ing)|encourag\w*|advise[ds]?|ignore|disregard|"
    r"should|must|asked|requested\s+to|regardless|instructions?\s+(to|for|above|below)|previous\s+instructions|"
    r"(the\s+)?(voting\s+)?(agent|model|assistant|ai|llm|bot)\b|automated|prompt|override|"
    r"vote\s+(for|against|with|in\s+favou?r|yes|no)\b(?!\s+(the\s+)?(election|appointment))|voting\s+(with|against|in\s+favou?r)|"
    r"(support|back|follow|side\s+with|trust|agree\s+with|go\s+with|stand\s+with|align\s+with)\s+(the\s+)?(management|board|directors)|"
    r"(reject|oppose|approve|support|endorse)\s+(it|this)\b|this\s+(item|proposal|resolution|agenda)|"
    r"note(?=\s*:)|note\s+to|(correct|right)\s+answer|answer\s+is|in\s+line\s+with\s+(the\s+)?(management|board)|as\s+recommended|reject|oppose)\b")
RETTET_CS = re.compile(r"\b(us|you|your)\b")  # små bokstaver: «US» og spørsmål i brasilianske kort er lovlige
ORD = re.compile(r"(?<![-'\w])[a-z][a-z']+\b")
STARTERE = {"shareholders", "shareholder", "investors", "investor", "holders", "management", "the", "a", "an", "it",
            "this", "thank", "note", "vi", "board", "dear", "all"}
_VOKAB, _BI = None, set()


def bygg(tekster):
    """Lager vokabularet av små-bokstav-ord fra historiske forslagstekster."""
    global _VOKAB, _BI
    tekster = [t for t in tekster if isinstance(t, str)]
    _VOKAB = Counter(w for t in tekster for w in ORD.findall(t))
    _BI = {(a, b) for t in tekster for a, b in zip(t.split(), t.split()[1:])}  # ordpar i ekte titler («of Board»)
    return _VOKAB


def finn(t, min_sjeldne=2):
    if not isinstance(t, str) or not t: return None
    pos = [m.start() for m in (RETTET.search(t), RETTET_CS.search(t)) if m]
    if not pos and _VOKAB is not None:  # prosa-signalet avgjør bare flagg; kuttet tas fra ordlista når den slår til,
        sj = [m.start() for m in ORD.finditer(t) if _VOKAB[m.group(0)] < 2]  # ellers fra første sjeldne ord
        if len(sj) >= min_sjeldne: pos.append(sj[0])
    if not pos: return None
    p = min(pos)
    # kutt der instruksen begynner, og ta med setningsstartere etter skilletegn («... Benefits. Shareholders are kindly ...»).
    # Ikke kutt ved punktum: titler har initialer («Elect Director F. Scott Dueser»), det kostet 6 stemmer i første forsøk.
    while True:  # ta med setningsstartere og småord foran, når skilletegn står foran eller ordparet aldri finnes i en ekte tittel
        m = re.search(r"(\S+)\s+(\w+)\s+$", t[:p]) or re.search(r"^()(\w+)\s+$", t[:p])
        if not m or not (m.group(2).lower() in STARTERE or m.group(2).islower()): return p
        if not (re.search(r"[.;!?:]$", m.group(1)) or (m.group(1), m.group(2)) not in _BI): return p
        p = m.start(2)
