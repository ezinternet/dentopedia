#!/usr/bin/env python3
from __future__ import annotations  # PEP 604 unions must run on Python 3.9
"""
LLM Wiki — OPERATIONS Frontmatter Lint

Checks every file under OPERATIONS folders for required cross-link frontmatter.

Rules enforced (see CLAUDE.md § OPERATIONS — Routing & Cross-link Rules):
  1. File must have YAML frontmatter (--- ... ---).
  2. `type` must match folder (e.g. agenda/ → type: agenda).
  3. `date` and `status` must be present.
  4. At least ONE of these cross-link fields must be present and non-empty:
       - source_wiki
       - agenda
       - output_wiki
     Files missing all three are "orphan" and break the
     knowledge ↔ operations chain.
  5. For slides/, interactives/, peer-review/: `agenda:` is REQUIRED
     (hard rule: outputs must trace back to an agenda spec).
  6. interactives/*.html: NO dark-mode CSS (OPERATIONS.md §7 "라이트 고정").
     `@media (prefers-color-scheme: dark)` and `[data-theme="dark"]` are the
     two constructs that actually render a clinical tool dark; the rule names
     exactly these two. Unlike checks 1-5 this one also runs on EXEMPT_FILES
     (the auto-generated dashboards) — a generator that starts emitting dark
     CSS is just as dark on the operatory screen, and the fix (patch the
     generator) is equally actionable.

Usage:
    python3 scripts/operations-lint.py            # full run
    python3 scripts/operations-lint.py --quiet    # errors only
"""

import os
import re
import sys
import argparse

# Folder → expected `type:` value. agenda is type=agenda, etc.
OPERATIONS_DIRS = {
    "agenda":       "agenda",
    "interactives": "interactive",
    "slides":       "slides",
    "peer-review":  "peer-review",
    "note-meeting": "meeting",
}

# Folders whose outputs MUST cite an `agenda:` (hard rule from CLAUDE.md).
AGENDA_REQUIRED = {"slides", "interactives", "peer-review"}

# These filenames are exempt from all checks (templates, indices, gitkeep, auto-generated).
EXEMPT_FILES = {"_template.md", "index.md", "index.html", ".gitkeep", "overviews-map.html", "wiki-stats-live.html", "contradiction-radar.html", "volatility-index.html"}

# Allowed status values.
VALID_STATUS = {"draft", "in-progress", "review", "done", "archived"}

# Track files we can actually parse — agenda/_template.md is one of these
# but exempt; everything else under OPERATIONS_DIRS is checked.
TARGET_EXTS = {".md", ".html"}

# ── OPERATIONS.md §7 — 라이트 고정 (임상 인터랙티브는 OS 다크 모드도 무시) ──────
#
# 왜 감사가 필요한가: 이 규칙은 2026-08-13부터 네 차례 지적됐고 OPERATIONS.md에
# hard rule로 박혀 있는데도 2026-08-31 `2026-08-31_it-stability-clinical-tool.html`이
# 미디어쿼리 다크 + [data-theme="dark"] + 토글 버튼을 다 갖고 태어났다. 당시 감사
# 22개 중 어느 것도 이걸 보지 않았다 — operations-lint는 frontmatter만,
# interactive-staleness는 source_wiki 날짜만 봤다. 즉 규칙이 문서에만 있고 기계
# 판독 고리가 없어서, 오직 작성자의 자각으로만 지켜지는 상태였다.
#
# 왜 signal이 아니라 error인가: 위키의 기본값은 signal-not-gate지만 그 원칙은
# **판단이 개입하는 감사**(인제스트 압력·종합 백로그)를 겨눈 것이다. 이건 리터럴
# CSS 토큰 두 개의 결정론적 존재 검사라 오탐이 원리상 없고, 고치는 데 판단이
# 필요 없으며, OPERATIONS.md §7 자체가 "위반 시 즉시 해당 블록 제거"로 적혀 있다.
# lint.py(YAML 구조)·operations-lint(frontmatter 구조)와 같은 부류다.
# 도입 시점 실측 87개 중 위반 0 — block으로 둬도 오늘 아무것도 막지 않는다.
LIGHT_ONLY_DIRS = {"interactives"}
DARK_CSS_PATTERNS = [
    (re.compile(r"prefers-color-scheme\s*:\s*dark"), "@media (prefers-color-scheme: dark)"),
    (re.compile(r"""\[data-theme\s*=\s*["']dark["']\]"""), '[data-theme="dark"]'),
]


def check_light_only(path: str, content: str) -> list[str]:
    """OPERATIONS.md §7 — 임상 인터랙티브에 다크 렌더 경로가 있으면 error."""
    errors: list[str] = []
    lines = content.splitlines()
    for rx, label in DARK_CSS_PATTERNS:
        hits = [i for i, line in enumerate(lines, 1) if rx.search(line)]
        if hits:
            where = ", ".join(f"L{n}" for n in hits[:5])
            more = f" (+{len(hits) - 5})" if len(hits) > 5 else ""
            errors.append(
                f"DARK CSS {label} at {where}{more} "
                f"— OPERATIONS.md §7 라이트 고정 위반, 해당 블록 제거: {path}"
            )
    return errors


def parse_frontmatter(content: str) -> dict | None:
    """Minimal YAML frontmatter parser: returns dict of raw string values.
    Lists are returned as the raw block of indented lines (good enough
    to detect "empty" vs "has at least one item")."""
    # HTML comment-wrapped frontmatter (interactives/.html files)
    m = re.match(r"^<!--\s*\n---\n(.*?)\n---\s*\n-->", content, re.DOTALL)
    if not m:
        m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None

    fm_text = m.group(1)
    fields: dict[str, str] = {}
    current_key: str | None = None
    current_list_items: list[str] = []

    for line in fm_text.splitlines():
        if not line.strip():
            continue
        # New top-level key: `key:` or `key: value`
        m_kv = re.match(r"^(\w[\w-]*)\s*:\s*(.*)$", line)
        if m_kv and not line.startswith(" "):
            # flush previous list
            if current_key is not None and current_list_items:
                fields[current_key] = "\n".join(current_list_items)
            elif current_key is not None and current_key not in fields:
                fields[current_key] = ""
            current_key = m_kv.group(1)
            value = m_kv.group(2).strip()
            current_list_items = []
            if value:
                fields[current_key] = value
                current_key = None  # scalar, done
        elif line.startswith(" ") or line.startswith("\t"):
            # list item or nested — treat as content for current_key
            stripped = line.strip()
            if stripped.startswith("- ") or stripped == "-":
                current_list_items.append(stripped)
            else:
                current_list_items.append(stripped)

    # flush trailing list
    if current_key is not None:
        if current_list_items:
            fields[current_key] = "\n".join(current_list_items)
        elif current_key not in fields:
            fields[current_key] = ""

    return fields


def field_is_nonempty(fields: dict, key: str) -> bool:
    if key not in fields:
        return False
    v = fields[key].strip()
    if not v:
        return False
    # Common "empty list" patterns
    if v in {"[]", "null", "~"}:
        return False
    # Pure dash bullets with no content after them
    only_dashes = all(
        line.strip() in {"-", ""} for line in v.splitlines()
    )
    if only_dashes:
        return False
    return True


def lint_file(path: str, folder: str) -> list[str]:
    errors: list[str] = []

    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return [f"READ ERROR ({e}): {path}"]

    fields = parse_frontmatter(content)
    if fields is None:
        return [f"NO FRONTMATTER: {path}"]

    # 1. type matches folder
    expected_type = OPERATIONS_DIRS[folder]
    actual_type = fields.get("type", "").strip().strip('"').strip("'")
    if actual_type != expected_type:
        errors.append(
            f"BAD type (expected '{expected_type}', got '{actual_type}'): {path}"
        )

    # 2. date present
    if not field_is_nonempty(fields, "date"):
        errors.append(f"MISSING date: {path}")

    # 3. status present and valid
    status = fields.get("status", "").strip().strip('"').strip("'")
    if not status:
        errors.append(f"MISSING status: {path}")
    elif status not in VALID_STATUS:
        errors.append(
            f"INVALID status '{status}' (allowed: {sorted(VALID_STATUS)}): {path}"
        )

    # 4. cross-link orphan check
    has_source = field_is_nonempty(fields, "source_wiki")
    has_agenda = field_is_nonempty(fields, "agenda")
    has_output = field_is_nonempty(fields, "output_wiki")
    if not (has_source or has_agenda or has_output):
        errors.append(
            f"ORPHAN (no source_wiki/agenda/output_wiki): {path}"
        )

    # 5. hard rule — slides/interactives/peer-review need agenda
    if folder in AGENDA_REQUIRED and not has_agenda:
        errors.append(
            f"MISSING agenda (required for {folder}/): {path}"
        )

    # 6. hard rule — interactives must render light (OPERATIONS.md §7)
    if folder in LIGHT_ONLY_DIRS and path.endswith(".html"):
        errors.extend(check_light_only(path, content))

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="LLM Wiki OPERATIONS frontmatter / cross-link lint"
    )
    parser.add_argument("--quiet", action="store_true", help="Only show errors")
    args = parser.parse_args()

    all_errors: list[str] = []
    ok_count = 0
    checked_count = 0

    for folder in OPERATIONS_DIRS:
        if not os.path.isdir(folder):
            continue
        for root, _dirs, files in os.walk(folder):
            for fn in sorted(files):
                ext = os.path.splitext(fn)[1]
                if ext not in TARGET_EXTS:
                    continue
                path = os.path.join(root, fn)
                if fn in EXEMPT_FILES:
                    # 자동 생성 대시보드 등 — frontmatter 검사는 면제하되
                    # §7(라이트 고정)은 면제하지 않는다. 생성기가 다크 CSS를
                    # 뱉기 시작하면 진료실 화면에서는 똑같이 다크다.
                    if folder in LIGHT_ONLY_DIRS and ext == ".html":
                        try:
                            with open(path, encoding="utf-8") as f:
                                gen_errors = check_light_only(path, f.read())
                        except (OSError, UnicodeDecodeError) as e:
                            gen_errors = [f"READ ERROR ({e}): {path}"]
                        if gen_errors:
                            all_errors.extend(gen_errors)
                    continue
                checked_count += 1
                errors = lint_file(path, folder)
                if errors:
                    all_errors.extend(errors)
                else:
                    ok_count += 1

    status = "✅" if not all_errors else "❌"
    print(
        f"{status}  OK: {ok_count}   ERRORS: {len(all_errors)}   "
        f"CHECKED: {checked_count}"
    )

    if all_errors:
        print()
        for e in all_errors:
            print(f"  {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
