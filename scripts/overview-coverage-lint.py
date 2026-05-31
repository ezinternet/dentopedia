#!/usr/bin/env python3
"""
LLM Wiki — Overview Body Coverage Lint (signal, non-blocking)

각 wiki/overviews/*.md 페이지에 대해, 페이지가 link하는 paper 중 본문
(Related Papers·source_papers 섹션 외)에서 실제로 author+year inline 또는
stem으로 인용된 비율 (coverage %)을 측정한다.

cov%가 낮다 = paper들이 link만 되고 thesis 분기·표·결정 트리에 반영 안 됨
            = "wikilink-only ingest"로 자기 자신을 점검하는 카운터파트.

임계값:
  - WARN cov% < 40 : thesis 갱신 시급
  - INFO cov% < 60 : 부분 갱신 권장
  - linked < 5     : 너무 작은 페이지·허브 페이지 (제외)

Output: logs/{date}_overview-coverage-lint.log

Usage:
    python3 scripts/overview-coverage-lint.py
    python3 scripts/overview-coverage-lint.py --warn 40 --info 60 --min-linked 5
    python3 scripts/overview-coverage-lint.py --stdout

Signal, non-blocking.
"""

from __future__ import annotations
import re
import sys
import argparse
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
OVERVIEWS_DIR = WIKI_ROOT / "wiki" / "overviews"
LOGS_DIR = WIKI_ROOT / "logs"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
HEADING_RE = re.compile(r"^##+\s")
FM_LIST_ITEM_RE = re.compile(r"^\s+-\s+([a-z][\w/-]+)\s*$")
STEM_AY_RE = re.compile(r"^([a-z][a-z-]+?)-(19\d{2}|20\d{2})-")

RELATED_HEADING_KEYWORDS = (
    "related papers",
    "관련 페이지",
    "관련페이지",
    "spine paper",
    "## related",
    "## reference",
    "## 인접",
    "spine·spoke",
)


def split_body_related(text: str) -> tuple[str, str]:
    """Split text into body (before any 'Related Papers'-like heading) and the rest."""
    lines = text.splitlines()
    rs = None
    for i, line in enumerate(lines):
        if not HEADING_RE.match(line):
            continue
        s = line.strip().lower()
        if any(k in s for k in RELATED_HEADING_KEYWORDS):
            rs = i
            break
    if rs is None:
        return text, ""
    return "\n".join(lines[:rs]), "\n".join(lines[rs:])


def extract_paper_stems(text: str) -> set[str]:
    """All paper-like wikilinks (category/stem, excluding overviews/)."""
    stems = set()
    for m in WIKILINK_RE.finditer(text):
        t = m.group(1).strip().lstrip("/")
        if t.startswith("wiki/"):
            t = t[5:]
        parts = t.split("/")
        if len(parts) >= 2 and parts[0] != "overviews":
            stem = re.sub(r"\.md$", "", parts[-1])
            stems.add(stem)
    return stems


def extract_frontmatter_source_papers(text: str) -> set[str]:
    """source_papers·source_wiki YAML list under frontmatter."""
    stems = set()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return stems
    for line in m.group(1).splitlines():
        m2 = FM_LIST_ITEM_RE.match(line)
        if m2:
            path = m2.group(1)
            stem = re.sub(r"\.md$", "", path.split("/")[-1])
            stems.add(stem)
    return stems


def stem_to_author_year(stem: str) -> tuple[str | None, str | None]:
    m = STEM_AY_RE.match(stem)
    return (m.group(1), m.group(2)) if m else (None, None)


def body_cites_stem(body_text: str, stem: str) -> bool:
    """Body cites stem if stem appears verbatim OR author·year combo appears."""
    if stem in body_text:
        return True
    author, year = stem_to_author_year(stem)
    if not author:
        return False
    pat = re.compile(rf"\b{re.escape(author)}\b.*?{year}", re.IGNORECASE)
    if pat.search(body_text):
        return True
    cap = author[0].upper() + author[1:]
    if re.search(rf"\b{re.escape(cap)}\b.*?{year}", body_text):
        return True
    return False


def analyze_overview(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    body, _ = split_body_related(text)
    text_stems = extract_paper_stems(text)
    fm_stems = extract_frontmatter_source_papers(text)
    linked = text_stems | fm_stems
    cited = {s for s in linked if body_cites_stem(body, s)}
    cov = 100.0 * len(cited) / len(linked) if linked else 0.0
    return {
        "path": str(path.relative_to(WIKI_ROOT)),
        "linked": len(linked),
        "cited": len(cited),
        "cov_pct": cov,
        "uncited": sorted(linked - cited),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--warn", type=float, default=40.0, help="WARN threshold (cov%%)")
    p.add_argument("--info", type=float, default=60.0, help="INFO threshold (cov%%)")
    p.add_argument("--min-linked", type=int, default=5, help="skip pages with linked<n (hubs)")
    p.add_argument("--stdout", action="store_true")
    args = p.parse_args()

    if not OVERVIEWS_DIR.exists():
        print("  No overviews dir.")
        return 0
    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{date.today().isoformat()}_overview-coverage-lint.log"

    rows = [analyze_overview(f) for f in sorted(OVERVIEWS_DIR.rglob("*.md"))]
    n = len(rows)
    skipped_hubs = [r for r in rows if r["linked"] < args.min_linked]
    rows = [r for r in rows if r["linked"] >= args.min_linked]

    warn = [r for r in rows if r["cov_pct"] < args.warn]
    info = [r for r in rows if args.warn <= r["cov_pct"] < args.info]
    healthy = [r for r in rows if r["cov_pct"] >= args.info]

    warn.sort(key=lambda r: r["cov_pct"])
    info.sort(key=lambda r: r["cov_pct"])

    lines = []
    lines.append(f"# Overview Body Coverage Lint — {date.today().isoformat()}")
    lines.append(f"TOTAL overviews         : {n}")
    lines.append(f"hub/small skipped (<{args.min_linked}) : {len(skipped_hubs)}")
    lines.append(f"WARN (cov% < {args.warn:.0f}) : {len(warn)}")
    lines.append(f"INFO ({args.warn:.0f} ≤ cov% < {args.info:.0f}) : {len(info)}")
    lines.append(f"healthy (cov% ≥ {args.info:.0f}) : {len(healthy)}")
    lines.append("")

    if warn:
        lines.append(f"=== WARN: thesis 갱신 시급 (cov% < {args.warn:.0f}, top 30) ===")
        for r in warn[:30]:
            lines.append(
                f"  {r['cov_pct']:>5.1f}%  {r['path']}   (linked={r['linked']}, cited={r['cited']})"
            )
        lines.append("")
    if info:
        lines.append(f"=== INFO: 부분 갱신 권장 ({args.warn:.0f} ≤ cov% < {args.info:.0f}, top 30) ===")
        for r in info[:30]:
            lines.append(
                f"  {r['cov_pct']:>5.1f}%  {r['path']}   (linked={r['linked']}, cited={r['cited']})"
            )
        lines.append("")

    body = "\n".join(lines) + "\n"
    log_path.write_text(body, encoding="utf-8")

    print(
        f"🪞  Coverage Lint: {len(healthy)} healthy, {len(info)} info, {len(warn)} warn "
        f"({len(skipped_hubs)} hubs skipped, of {n})"
    )
    print(f"      log → logs/{log_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
