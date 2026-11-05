"""Polite, cached client for SEC EDGAR (www.sec.gov and data.sec.gov).

SEC fair-access policy: declare who you are in the User-Agent and stay below
10 requests per second. Set SEC_USER_AGENT="Team name contact@example.com".

Every response is cached under data/raw/sec/<host>/<path>, so the whole pipeline
reruns offline (OFFLINE=1 forbids network access). Each live download is appended
to data/raw/sec_fetch_log.jsonl with a SHA-256 digest, for traceability.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import threading
import time
import warnings
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

from .config import DATA_RAW

CACHE_DIR = DATA_RAW / "sec"
FETCH_LOG = DATA_RAW / "sec_fetch_log.jsonl"
MIN_INTERVAL_S = 0.125  # 8 requests/second, below SEC's limit of 10
_PLACEHOLDER_UA = "NBIM-Hackathon-H2026 research script (set SEC_USER_AGENT) admin@example.org"

_last_request = 0.0
_rate_lock = threading.Lock()
_local = threading.local()
_warned = False


def _user_agent() -> str:
    global _warned
    ua = os.environ.get("SEC_USER_AGENT", "").strip()
    if not ua:
        if not _warned:
            warnings.warn("SEC_USER_AGENT is not set - using a placeholder. "
                          "Set it to 'Team name your@email' as SEC requires.", stacklevel=3)
            _warned = True
        ua = _PLACEHOLDER_UA
    return ua


def cache_path(url: str) -> Path:
    p = urlparse(url)
    rel = p.path.lstrip("/")
    if p.query:
        rel += "__" + re.sub(r"[^A-Za-z0-9._-]", "_", p.query)
    return CACHE_DIR / p.netloc / rel


def is_cached(url: str) -> bool:
    return cache_path(url).exists()


def get(url: str, *, refresh: bool = False, offline: bool | None = None) -> bytes:
    """Return the body of `url`, from cache when available."""
    global _last_request
    if offline is None:
        offline = os.environ.get("OFFLINE") == "1"
    cp = cache_path(url)
    if cp.exists() and not refresh:
        return cp.read_bytes()
    if offline:
        raise FileNotFoundError(f"Not in cache and OFFLINE=1: {url}")
    session = getattr(_local, "session", None)
    if session is None:  # one session per thread; the rate limit is shared
        session = _local.session = requests.Session()
        session.headers.update({"User-Agent": _user_agent(), "Accept-Encoding": "gzip, deflate"})

    for attempt in range(6):
        with _rate_lock:
            wait = MIN_INTERVAL_S - (time.monotonic() - _last_request)
            if wait > 0:
                time.sleep(wait)
            _last_request = time.monotonic()
        try:
            r = session.get(url, timeout=60)
        except requests.RequestException:
            if attempt == 5:
                raise
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            break
        if r.status_code == 404:
            raise FileNotFoundError(f"404 from SEC: {url}")
        if r.status_code in (403, 429) or r.status_code >= 500:
            if attempt == 5:
                r.raise_for_status()
            time.sleep(2 ** attempt + 1)
            continue
        r.raise_for_status()

    body = r.content
    cp.parent.mkdir(parents=True, exist_ok=True)
    tmp = cp.with_name(cp.name + f".tmp{threading.get_ident()}")
    tmp.write_bytes(body)
    tmp.replace(cp)  # atomic: a crash never leaves a half-written cache file
    FETCH_LOG.parent.mkdir(parents=True, exist_ok=True)
    with _rate_lock, FETCH_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "url": url,
            "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        }) + "\n")
    return body


def get_json(url: str, **kw):
    return json.loads(get(url, **kw))
