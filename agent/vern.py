"""Vern mot instrukser i forslagsteksten: rens_tekst() fjerner setninger som er instrukser eller depotvarsler
(ikke forslagsinnhold), og flagger saken, så den går til et menneske. Brukes av kjerne.py."""
import re

DATO = re.compile(r'^\s*\d{1,2} [A-Z]{3} \d{4}\s*:?\s*')
INSTRUKS = re.compile(
    r"(\b\d{1,2} [A-Z]{3} \d{4}\s*:|FOR SHAREHOLDERS (NOT )?HOLDING|FOR THE PROPOSAL \d+ REGARDING|PLEASE (NOTE|BE ADVISED)|IF YOU (HOLD|INTEND)|YOUR CUSTODIAN|CUSTODIAN BANK|VOTING INSTRUCTION|STANDING INSTRUCTION"
    r"|PROXY CARD|VOTING FORM|VOTING MUST BE LODGED|(BOARD|DIRECTORS|DRECTORS)( OF DIRECTORS)? RECOMMENDS?|RECOMMENDS (YOU|A\b|:)"
    r"|\bVOTE\s+['\"]?(FOR|AGAINST)['\"]?\s*(THIS|THE (PROPOSAL|RESOLUTION|ITEM)|[,.;:!]|$)|\bIGNORE\b|\bINSTRUCT\b|(PREVIOUS|YOUR|THESE) INSTRUCTIONS|MUST VOTE|SHOULD VOTE|IS A VALID VOTING OPTION|DEFAULT TO"
    r"|HEREBY CERTIFIES|\bAI (AGENT|ASSISTANT|MODEL|SYSTEM)|VOTING (AGENT|SYSTEM)|AUTOMATED SYSTEM|SYSTEM PROMPT|LANGUAGE MODEL)", re.I)


def rens_tekst(t):
    """-> (renset tekst, flagget). Deler i setninger og dropper setninger som er instrukser/varsler."""
    if not isinstance(t, str) or not t: return '', False
    t2 = DATO.sub('', t)
    deler = re.split(r'(?<=[.;!?])\s+|\n+', t2)
    # Kutt fra der første instruks starter: det som står foran (selve forslaget) beholdes, resten kastes.
    beholdt, flagget = [], False
    for s in deler:
        m = INSTRUKS.search(s)
        if m: flagget = True; s = re.sub(r'(\b(NOTE|PLEASE|THE|TO|A|AN)\s*)+$', '', s[:m.start()], flags=re.I).strip(' :,-')
        if s: beholdt.append(s)
        if m: break  # alt etter første instruks er varsel/instruks, ikke forslag
    return ' '.join(beholdt).strip(), flagget
