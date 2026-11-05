"""NBIM's published voting guidelines as citable chunks, plus BM25 retrieval.

Each chunk has a stable id such as  GVG-2025/p12/CEO-remuneration/rule-8
(document / page / section / rule). The agent may only cite text that appears verbatim
in a chunk; `quote_is_valid` enforces that after whitespace/typography normalization.

Version in force: for a meeting date d, the Global Voting Guidelines (GVG) edition of
year(d) is used, falling back to the newest earlier edition (no 2026 edition was
published at the time of writing). Voting reviews are used from their publication date.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
import requests
from pypdf import PdfReader
from rank_bm25 import BM25Okapi

from .config import DATA_RAW

WEB_CACHE = DATA_RAW / "web" / "nbim.no"
UA = "Mozilla/5.0 (X11; Linux x86_64) NBIM-Hackathon-H2026-research"

SOURCES = [
    # doc_id, file, url, in force from, kind
    ("GVG-2023", "gvg-2023.pdf", "https://www.nbim.no/contentassets/34530895f32743a0a9528d6e55b73f6d/global-voting-guidelines-2023.pdf", "2023-01-01", "guidelines"),
    ("GVG-2024", "gvg-2024.pdf", "https://www.nbim.no/contentassets/34530895f32743a0a9528d6e55b73f6d/global_voting_guidelines_2024_uuweb.pdf", "2024-01-01", "guidelines"),
    ("GVG-2025", "gvg-2025.pdf", "https://www.nbim.no/contentassets/cbee6983c7d044a6a6d2f286ed5fa3df/global-voting-guildeines_2025.pdf", "2025-01-01", "guidelines"),
    ("CEO-PAY-2017", "ceo-remuneration-2017.pdf", "https://www.nbim.no/contentassets/24fdd154fecb4ca499faaf17e9bc9ba1/ceo-remuneration.pdf", "2017-04-07", "position_paper"),
    ("VR-2024H1", "voting-review-2024h1.pdf", "https://www.nbim.no/contentassets/cbd2328b64ec4bb483ac2935b5da8cc4/voting-review-first-half-2024_uu.pdf", "2024-08-01", "voting_review"),
    ("VR-2025H1", "voting-review-2025h1.pdf", "https://www.nbim.no/contentassets/5476944f2d3e47babc15239aa620aa23/voting-first-half_2025_uuweb.pdf", "2025-08-01", "voting_review"),
]
SOURCE_URL = {s[0]: s[2] for s in SOURCES}

_RULE_START = re.compile(r"(?m)^\s*(\d{1,2})\.\s+")
_HEADER_RE = re.compile(r"^(Norges Bank Investment Management.*|Global voting guidelines|\d{1,2}|→)$")


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    kind: str
    page: int
    section: str
    text: str
    in_force_from: str
    url: str
    tags: list[str] = field(default_factory=list)


def normalize(text: str) -> str:
    t = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-").replace(" ", " ").replace("­", "")
    t = re.sub(r"-\n(?=[a-z])", "-", t)
    return re.sub(r"\s+", " ", t).strip()


def download_all() -> None:
    WEB_CACHE.mkdir(parents=True, exist_ok=True)
    for _, fname, url, _, _ in SOURCES:
        path = WEB_CACHE / fname
        if not path.exists():
            r = requests.get(url, headers={"User-Agent": UA}, timeout=60)
            r.raise_for_status()
            path.write_bytes(r.content)


def _pages(fname: str) -> list[str]:
    return [(p.extract_text() or "") for p in PdfReader(WEB_CACHE / fname).pages]


def _clean_lines(page_text: str) -> list[str]:
    return [l.rstrip() for l in page_text.split("\n") if l.strip() and not _HEADER_RE.match(l.strip())]


# Canonical GVG structure (identical in the 2023, 2024 and 2025 editions). NBIM's own
# vote rationales cite these numbers ("GVG 3.2"), so agent citations can be scored.
GVG_SECTIONS = {
    "1.1": "Independence of the board", "1.2": "Independence of main committees",
    "1.3": "Separation of chairperson and CEO",
    "2.1": "Time commitment", "2.2": "Industry expertise", "2.3": "Diversity",
    "3.1": "Board nomination and election", "3.2": "Board decisions and conduct", "3.3": "CEO remuneration",
    "4.1": "Voting rights", "4.2": "Shareholder meeting", "4.3": "Governing documents",
    "5.1": "Auditor", "5.2": "Financial statements", "5.3": "Sustainability",
    "6.1": "Share issuance", "6.2": "Mergers, acquisitions and other corporate transactions",
    "6.3": "Related party-transaction",
}
GVG_CHAPTERS = {"1": "Board independence", "2": "Board composition", "3": "Board accountability",
                "4": "Shareholder protection", "5": "Company reporting", "6": "Capital"}
_SECTION_BY_TITLE = {re.sub(r"[^a-z]", "", v.lower())[:18]: k for k, v in GVG_SECTIONS.items()}


def _match_section(title: str) -> str | None:
    key = re.sub(r"[^a-z]", "", title.lower())[:18]
    for k, num in _SECTION_BY_TITLE.items():
        if key.startswith(k[: max(8, min(len(k), len(key)))]):
            return num
    return None


def _gvg_chunks(doc_id: str, fname: str, url: str, in_force: str) -> list[Chunk]:
    """Each numbered rule ('We will not support ...') becomes one chunk; the principle
    text before the rules of a section becomes a 'principle' chunk. Chunk ids:
    GVG-2025/§1.3/rule-1, GVG-2025/§1.3/principle."""
    chunks: list[Chunk] = []
    sec, chapter_seen = None, False
    buffer: list[str] = []
    rule_no, rule_lines = None, []
    page_of_buffer = 1

    def flush_rule(pno):
        nonlocal rule_no, rule_lines
        if rule_no is not None and sec:
            text = normalize("\n".join(rule_lines))
            chunks.append(Chunk(f"{doc_id}/§{sec}/rule-{rule_no}", doc_id, "guidelines", pno,
                                f"{sec} {GVG_SECTIONS[sec]}", text, in_force, url))
        rule_no, rule_lines = None, []

    def flush_principle(pno):
        nonlocal buffer
        t = normalize("\n".join(buffer))
        if sec and len(t) > 40 and not any(c.chunk_id == f"{doc_id}/§{sec}/principle" for c in chunks):
            chunks.append(Chunk(f"{doc_id}/§{sec}/principle", doc_id, "guidelines", pno,
                                f"{sec} {GVG_SECTIONS[sec]}", t, in_force, url))
        buffer = []

    for pno, raw in enumerate(_pages(fname), 1):
        if pno < 5:  # cover, introduction and table of contents
            continue
        lines = _clean_lines(raw)
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            m = re.match(r"^(\d{1,2})\.\s+(.*)$", line)
            if m and not re.search(r"(?i)\b(we will|we may|we would)\b", line):
                title = m.group(2) + (" " + lines[i + 1].strip() if i + 1 < len(lines) and len(m.group(2)) < 25 else "")
                num = _match_section(title)
                if num:  # new section
                    flush_rule(pno)
                    flush_principle(pno)
                    sec = num
                    i += 2 if len(m.group(2)) < 25 and _match_section(m.group(2)) != num else 1
                    continue
                if m.group(2).split()[0] in ("Board", "Shareholder", "Company", "Capital") and len(m.group(2)) < 25:
                    flush_rule(pno)  # chapter heading: ends the previous section
                    flush_principle(pno)
                    i += 2
                    continue
            if m and re.search(r"(?i)\b(we will|we may|we would)\b", line) and sec:
                flush_rule(pno)
                if buffer:
                    flush_principle(pno)
                rule_no, rule_lines = m.group(1), [m.group(2)]
            elif rule_no is not None:
                rule_lines.append(line)
            elif sec:
                buffer.append(line)
            i += 1
    flush_rule(pno)
    flush_principle(pno)
    return chunks


def gvg_section_text(chunks: list[Chunk], doc_id: str) -> str:
    """The whole edition as one citable text block for the LLM, grouped by section."""
    out = []
    for num, title in GVG_SECTIONS.items():
        part = [c for c in chunks if c.doc_id == doc_id and c.section.startswith(num + " ")]
        if not part:
            continue
        out.append(f"### GVG {num} {title}  (source: {doc_id}, page {part[0].page})")
        for c in part:
            label = "Principle" if c.chunk_id.endswith("principle") else "Rule " + c.chunk_id.rsplit("-", 1)[-1]
            out.append(f"[{c.chunk_id}] {label}: {c.text}")
        out.append("")
    return "\n".join(out)


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")[:40] or "section"


def _paragraph_chunks(doc_id: str, fname: str, url: str, in_force: str, kind: str,
                      keep: re.Pattern | None = None, max_words: int = 120) -> list[Chunk]:
    """Position papers / voting reviews: sentence windows of <= max_words, per page."""
    chunks = []
    for pno, raw in enumerate(_pages(fname), 1):
        text = normalize("\n".join(_clean_lines(raw)))
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
        window: list[str] = []
        k = 0
        for s in sentences + [None]:
            if s is not None and sum(len(w.split()) for w in window) + len(s.split()) <= max_words:
                window.append(s)
                continue
            if window:
                body = " ".join(window)
                if keep is None or keep.search(body):
                    k += 1
                    chunks.append(Chunk(f"{doc_id}/p{pno}/para-{k}", doc_id, kind, pno, "", body, in_force, url))
            window = [s] if s is not None else []
    return chunks


_PAY_RE = re.compile(r"(?i)\b(pay|remuneration|compensation|incentive|CEO|golden|vesting|shares)\b")


def build_corpus() -> list[Chunk]:
    download_all()
    chunks: list[Chunk] = []
    for doc_id, fname, url, in_force, kind in SOURCES:
        if kind == "guidelines":
            chunks += _gvg_chunks(doc_id, fname, url, in_force)
        elif kind == "position_paper":
            chunks += _paragraph_chunks(doc_id, fname, url, in_force, kind)
        else:  # voting reviews: keep the pay-related passages only
            chunks += _paragraph_chunks(doc_id, fname, url, in_force, kind, keep=_PAY_RE)
    for c in chunks:
        if re.search(r"(?i)remuneration|pay|compensation", c.section + " " + c.text[:200]):
            c.tags.append("pay")
    return chunks


def in_force(chunks: list[Chunk], meeting_date) -> list[Chunk]:
    """Chunks applicable at `meeting_date`: newest GVG edition in force + earlier papers/reviews."""
    d = pd.Timestamp(meeting_date).strftime("%Y-%m-%d")
    gvg_versions = sorted({c.doc_id for c in chunks if c.kind == "guidelines" and c.in_force_from <= d})
    current_gvg = gvg_versions[-1] if gvg_versions else None
    reviews = sorted({c.doc_id for c in chunks if c.kind == "voting_review" and c.in_force_from <= d})
    latest_review = reviews[-1] if reviews else None
    return [c for c in chunks if (c.kind == "guidelines" and c.doc_id == current_gvg)
            or (c.kind == "position_paper" and c.in_force_from <= d)
            or (c.kind == "voting_review" and c.doc_id == latest_review)]


class Retriever:
    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        self._bm25 = BM25Okapi([self._tok(c.section + " " + c.text) for c in chunks])

    @staticmethod
    def _tok(t: str) -> list[str]:
        return re.findall(r"[a-z0-9]+", t.lower())

    def search(self, query: str, k: int = 6, pool: list[Chunk] | None = None) -> list[Chunk]:
        scores = self._bm25.get_scores(self._tok(query))
        allowed = None if pool is None else {c.chunk_id for c in pool}
        ranked = sorted(range(len(self.chunks)), key=lambda i: -scores[i])
        out = [self.chunks[i] for i in ranked if allowed is None or self.chunks[i].chunk_id in allowed]
        return out[:k]


def quote_is_valid(quote: str, chunk: Chunk, min_words: int = 6) -> bool:
    q = normalize(quote).strip(' ".')
    return len(q.split()) >= min_words and q.lower() in normalize(chunk.text).lower()


def to_frame(chunks: list[Chunk]) -> pd.DataFrame:
    return pd.DataFrame([c.__dict__ for c in chunks])
