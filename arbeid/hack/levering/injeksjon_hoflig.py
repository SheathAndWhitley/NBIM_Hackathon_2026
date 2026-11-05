"""Høflige og omskrevne instrukser i forslagsteksten (#2237). Utfyller vern.py (#2047) og EKSTRA_INJ (#2063).

To signaler, begge sjekket mot NBIMs historiske forslagstekster (år < 2026):
1) RETTET: ord som henvender seg til den som stemmer (please, kindly, we, recommend, urge, should, ...) eller ber om
   en retning (vote with/for/against, support/follow the board, reject, oppose). Ingen av dem står i historikken.
2) PROSA: forslagstitler er Title Case; små bokstaver brukes nesten bare til småord (of, as, and, to, ...). To eller
   flere ord med små bokstaver som er sjeldne (< 2 ganger) i historikken betyr at noen har skrevet en setning inn.
3) TITLE CASE (#2265): en instruks i Title Case («as Proposed by Management, as Always») slipper forbi 1) og 2).
   Den bruker likevel vanlige engelske ord som ikke er substantiv (adverb, verb, adjektiv, lukket ordklasse) og som
   aldri står i en NBIM-tittel. Ordklasse og frekvens er bygd inn under (_ORDKL, fra wordfreq og WordNet, se
   arbeid/oppgave_2265/lag_ordklasser.py). Flagg: to slike ord (zipf >= 4,5), eller et adverb (zipf >= 4) som ikke
   står foran et tittelord (slutten av teksten, skilletegn eller småord etter), så «Daily Related Party» går fri.
finn(tekst) -> posisjon der instruksen starter, eller None.
"""
import base64, re, zlib
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
_CI, _CIBI, _SLUTT = Counter(), set(), Counter()  # #2265: alle ord og ordpar i historikken med små bokstaver, uansett skrivemåte
TOK = re.compile(r"[A-Za-z]+")
_ORDKL_B64 = """
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
cg==
"""
_ORDKL = {w: (int(z) / 10, k) for w, z, k in (x.split("\t") for x in
          zlib.decompress(base64.b64decode("".join(_ORDKL_B64.split()))).decode().split("\n"))}


def bygg(tekster):
    """Lager vokabularet av små-bokstav-ord fra historiske forslagstekster."""
    global _VOKAB, _BI
    tekster = [t for t in tekster if isinstance(t, str)]
    _VOKAB = Counter(w for t in tekster for w in ORD.findall(t))
    _BI = {(a, b) for t in tekster for a, b in zip(t.split(), t.split()[1:])}  # ordpar i ekte titler («of Board»)
    global _CI, _CIBI
    tk = [[w.lower() for w in TOK.findall(t)] for t in tekster]
    _CI = Counter(w for t in tk for w in t); _CIBI = {(a, b) for t in tk for a, b in zip(t, t[1:])}
    global _SLUTT
    _SLUTT = Counter(t[-1] for t in tk if t)  # sluttord i ekte titler («Dividend», «Director»)
    return _VOKAB


def tittel_instruks(t):
    """#2265: posisjon for en Title Case-instruks (signal 3), eller None. Trekker kuttet bakover over ordpar som
    aldri står i en ekte tittel, og kutter senest der ordet foran ofte står sist i en tittel
    («Approve Final Dividend | as Proposed by Management, as Always»). Finnes ikke det, trekkes bare småord og
    ikke-substantiv med, så tittelord blir stående."""
    if _VOKAB is None: return None
    tk = list(TOK.finditer(t)); sus, adv = [], []
    for i, m in enumerate(tk):
        w = m.group(0).lower(); e = _ORDKL.get(w)
        if not e or _CI[w] >= 2: continue
        if e[0] >= 4.5: sus.append(i)
        etter = t[m.end():]
        if e[1] == "r" and re.match(r"\s*($|[,.;:!?)]|[a-z])", etter): adv.append(i)
    if len(sus) < 2 and not adv: return None
    i = min(sus[:1] + adv) if len(sus) >= 2 else adv[0]
    j = i  # kjeden av ordpar som aldri står i en ekte tittel, bakover fra instruksen
    while j > 0 and (tk[j - 1].group(0).lower(), tk[j].group(0).lower()) not in _CIBI: j -= 1
    for k in range(i, max(j, 1) - 1, -1):  # seneste kutt der ordet foran ofte står sist i en tittel (andel >= 0,3)
        w = tk[k - 1].group(0).lower()
        if _SLUTT[w] >= 5 and _SLUTT[w] >= 0.3 * _CI[w]: return tk[k].start()
    while i > 0 and (tk[i - 1].group(0).lower(), tk[i].group(0).lower()) not in _CIBI and (
            tk[i - 1].group(0).islower() or tk[i - 1].group(0).lower() in _ORDKL): i -= 1  # ellers: tittelord blir stående
    return tk[i].start()


def finn(t, min_sjeldne=2):
    if not isinstance(t, str) or not t: return None
    pos = [m.start() for m in (RETTET.search(t), RETTET_CS.search(t)) if m]
    if not pos and _VOKAB is not None:  # prosa-signalet avgjør bare flagg; kuttet tas fra ordlista når den slår til,
        sj = [m.start() for m in ORD.finditer(t) if _VOKAB[m.group(0)] < 2]  # ellers fra første sjeldne ord
        if len(sj) >= min_sjeldne: pos.append(sj[0])
    if not pos:  # #2265: bare når de andre signalene er tause, så alt de flagget før står likt
        p3 = tittel_instruks(t)
        if p3 is not None: pos.append(p3)
    if not pos: return None
    p = min(pos)
    # kutt der instruksen begynner, og ta med setningsstartere etter skilletegn («... Benefits. Shareholders are kindly ...»).
    # Ikke kutt ved punktum: titler har initialer («Elect Director F. Scott Dueser»), det kostet 6 stemmer i første forsøk.
    while True:  # ta med setningsstartere og småord foran, når skilletegn står foran eller ordparet aldri finnes i en ekte tittel
        m = re.search(r"(\S+)\s+(\w+)\s+$", t[:p]) or re.search(r"^()(\w+)\s+$", t[:p])
        w2 = m.group(2).lower() if m else ""  # #2265: sjeldne adverb foran blir med («Always | Side With Management»)
        adv2 = _VOKAB is not None and _ORDKL.get(w2, (0, ""))[1] == "r" and _CI[w2] < 2
        if not m or not (w2 in STARTERE or m.group(2).islower() or adv2): return p
        if not (re.search(r"[.;!?:]$", m.group(1)) or (m.group(1), m.group(2)) not in _BI): return p
        p = m.start(2)
