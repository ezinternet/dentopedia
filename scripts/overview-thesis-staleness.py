#!/usr/bin/env python3
"""
LLM Wiki — Overview Thesis Staleness Audit (signal, non-blocking)

Problem: file mtime 또는 "git last commit date"는 overview의 신선도를 판정하기에
부정확하다. Ingest 시 Related Papers 섹션에 wikilink 한 줄 추가하면서 mtime 갱신되지만
overview의 본문 thesis는 그대로일 수 있다.

이 스크립트는 각 wiki/overviews/*.md 파일의 git log diff를 line-by-line으로 분석해
각 commit을 다음 두 부류로 분리한다:

  1. wikilink-only edit: 추가/삭제된 non-blank line이 전부 wikilink·frontmatter list
     항목 패턴. Related Papers 섹션이나 source_papers frontmatter에 paper 추가하는
     ingest 작업이 여기 해당.
  2. thesis edit: 그 외. heading, prose, 표, 결정 분기 등 본문이 실제로 변경된 commit.

가장 최근 thesis edit의 author-date를 'thesis_last_modified'로 보고,
오늘로부터 경과 일수를 계산한다.

임계값:
  - WARN ≥ 90일: 'thesis-stale' 후보
  - INFO ≥ 180일: 'thesis-very-stale'

Output: logs/{date}_overview-thesis-staleness.log

Usage:
    python3 scripts/overview-thesis-staleness.py
    python3 scripts/overview-thesis-staleness.py --stdout   # print full list
    python3 scripts/overview-thesis-staleness.py --warn-days 60 --info-days 120

Signal, non-blocking. daily-audit.py 통합 시 must_pass=False.
"""

import os
import re
import sys
import argparse
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
OVERVIEWS_DIR = WIKI_ROOT / "wiki" / "overviews"
LOGS_DIR = WIKI_ROOT / "logs"

# ---- patterns -----------------------------------------------------------

# 한 line이 "wikilink만" 라인인지 판별. True면 wikilink-only.
# 매치 대상:
#   - "[[foo/bar]]"
#   - "- [[foo/bar]]"
#   - "- [[foo/bar]] — 설명 텍스트" (Related Papers 섹션 bullet)
#   - "  - implants/foo-bar-2024"  (frontmatter source_papers YAML list)
#   - "  - wiki/overviews/foo"
WIKILINK_LINE_RE = re.compile(
    r"""
    ^
    \s*
    (?:
        -\s+\[\[[^\]]+\]\](?:\s*[—:\-]\s*.*)?      # bullet wikilink + optional desc
      | \[\[[^\]]+\]\]                              # bare wikilink
      | -\s+[a-z][\w./-]*$                          # YAML list item (path-like)
    )
    \s*$
    """,
    re.VERBOSE,
)

# 빈 line (whitespace only)
BLANK_LINE_RE = re.compile(r"^\s*$")

# frontmatter 경계
FRONTMATTER_DELIM_RE = re.compile(r"^---\s*$")


def is_wikilink_only_change_line(line: str) -> bool:
    """line은 git diff의 +/- prefix 없는 본문. blank 또는 wikilink 패턴이면 True."""
    if BLANK_LINE_RE.match(line):
        return True
    if WIKILINK_LINE_RE.match(line):
        return True
    return False


def classify_commit_diff(diff_text: str) -> tuple[str, int, int, int]:
    """Return (classification, n_added, n_removed, n_nontrivial_changed).
    classification ∈ {'wikilink-only', 'thesis', 'mixed-but-thesis'}.
    """
    added = removed = nontrivial = 0
    in_hunk = False
    for raw in diff_text.splitlines():
        if raw.startswith("@@"):
            in_hunk = True
            continue
        if not in_hunk:
            continue
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        if raw.startswith("+"):
            line = raw[1:]
            added += 1
            if not is_wikilink_only_change_line(line):
                nontrivial += 1
        elif raw.startswith("-"):
            line = raw[1:]
            removed += 1
            if not is_wikilink_only_change_line(line):
                nontrivial += 1
    if added == 0 and removed == 0:
        return ("no-change", 0, 0, 0)
    if nontrivial == 0:
        return ("wikilink-only", added, removed, 0)
    return ("thesis", added, removed, nontrivial)


def git_log_for_file(path: Path) -> list[tuple[str, datetime, str, str]]:
    """Return list of (sha, author_date, subject, diff_text) for commits touching path."""
    rel = str(path.relative_to(WIKI_ROOT))
    try:
        # --follow to track renames
        r = subprocess.run(
            ["git", "log", "--follow", "--reverse",
             "--format=%H%x00%aI%x00%s%x00", "-p", "--", rel],
            cwd=WIKI_ROOT, capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError:
        return []
    raw = r.stdout
    # Parse: each commit starts with sha\0iso-date\0subject\0\n followed by diff
    commits: list[tuple[str, datetime, str, str]] = []
    chunks = raw.split("\x00")
    # Reassemble. The format is sha NUL date NUL subject NUL <newline + diff> sha NUL date NUL ...
    # Easier: split lines, detect header line by NUL count.
    lines = raw.splitlines(keepends=True)
    cur_meta = None
    cur_diff_parts: list[str] = []
    for line in lines:
        if line.count("\x00") == 3 and not line.startswith(("+", "-", " ", "@", "d", "i", "n")):
            # heuristic: header line of the commit format
            # flush previous
            if cur_meta is not None:
                commits.append((cur_meta[0], cur_meta[1], cur_meta[2], "".join(cur_diff_parts)))
            parts = line.split("\x00")
            sha = parts[0]
            try:
                dt = datetime.fromisoformat(parts[1])
            except ValueError:
                dt = datetime.now(timezone.utc)
            subj = parts[2].rstrip("\n")
            cur_meta = (sha, dt, subj)
            cur_diff_parts = []
        else:
            cur_diff_parts.append(line)
    if cur_meta is not None:
        commits.append((cur_meta[0], cur_meta[1], cur_meta[2], "".join(cur_diff_parts)))
    return commits


def analyze_overview(path: Path) -> dict:
    commits = git_log_for_file(path)
    result = {
        "path": str(path.relative_to(WIKI_ROOT)),
        "total_commits": 0,
        "thesis_commits": 0,
        "wikilink_only_commits": 0,
        "first_thesis_date": None,
        "last_thesis_date": None,
        "last_any_date": None,
        "uncommitted": False,
    }
    if not commits:
        # not yet committed (new file in working tree)
        result["uncommitted"] = True
        return result
    for sha, dt, subj, diff in commits:
        cls, added, removed, _ = classify_commit_diff(diff)
        if cls == "no-change":
            continue
        result["total_commits"] += 1
        result["last_any_date"] = dt
        if cls == "thesis":
            result["thesis_commits"] += 1
            if result["first_thesis_date"] is None:
                result["first_thesis_date"] = dt
            result["last_thesis_date"] = dt
        else:
            result["wikilink_only_commits"] += 1
    return result


def days_since(dt: datetime | None) -> int | None:
    if dt is None:
        return None
    now = datetime.now(timezone.utc)
    return (now - dt).days


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--warn-days", type=int, default=90)
    p.add_argument("--info-days", type=int, default=180)
    p.add_argument("--stdout", action="store_true")
    args = p.parse_args()

    if not OVERVIEWS_DIR.exists():
        print(f"  No overviews dir: {OVERVIEWS_DIR}")
        return 0

    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{date.today().isoformat()}_overview-thesis-staleness.log"

    rows = []
    for f in sorted(OVERVIEWS_DIR.rglob("*.md")):
        rows.append(analyze_overview(f))

    n = len(rows)
    n_uncommitted = sum(1 for r in rows if r["uncommitted"])
    warn = []
    info = []
    fresh = 0
    for r in rows:
        if r["uncommitted"]:
            continue
        d = days_since(r["last_thesis_date"])
        if d is None:
            # has commits but only wikilink-only ones — counts as info (never had thesis edit since tracking?)
            d = days_since(r["last_any_date"]) or 0
            info.append((d, r))
            continue
        if d >= args.info_days:
            info.append((d, r))
        elif d >= args.warn_days:
            warn.append((d, r))
        else:
            fresh += 1

    warn.sort(key=lambda x: -x[0])
    info.sort(key=lambda x: -x[0])

    lines = []
    lines.append(f"# Overview Thesis Staleness — {date.today().isoformat()}")
    lines.append(f"TOTAL overviews         : {n}")
    lines.append(f"uncommitted (new files) : {n_uncommitted}")
    lines.append(f"fresh (<{args.warn_days}d thesis edit) : {fresh}")
    lines.append(f"WARN ({args.warn_days}-{args.info_days}d)         : {len(warn)}")
    lines.append(f"INFO (≥{args.info_days}d)            : {len(info)}")
    lines.append("")
    if warn:
        lines.append(f"=== WARN: thesis edit ≥{args.warn_days}d ago (top 50) ===")
        for d, r in warn[:50]:
            wo = r["wikilink_only_commits"]
            th = r["thesis_commits"]
            lines.append(f"  {d:>5}d  {r['path']}   (thesis={th}, wikilink-only={wo})")
        lines.append("")
    if info:
        lines.append(f"=== INFO: thesis edit ≥{args.info_days}d ago (top 50) ===")
        for d, r in info[:50]:
            wo = r["wikilink_only_commits"]
            th = r["thesis_commits"]
            lines.append(f"  {d:>5}d  {r['path']}   (thesis={th}, wikilink-only={wo})")
        lines.append("")

    body = "\n".join(lines) + "\n"
    log_path.write_text(body, encoding="utf-8")

    print(f"📐  Thesis Staleness: {fresh} fresh, {len(warn)} warn, {len(info)} info, {n_uncommitted} uncommitted (of {n})")
    print(f"      log → logs/{log_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
