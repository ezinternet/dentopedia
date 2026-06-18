#!/usr/bin/env python3
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
EXEMPT_FILES = {"_template.md", "index.md", "index.html", ".gitkeep", "overviews-map.html"}

# Allowed status values.
VALID_STATUS = {"draft", "in-progress", "review", "done", "archived"}

# Track files we can actually parse — agenda/_template.md is one of these
# but exempt; everything else under OPERATIONS_DIRS is checked.
TARGET_EXTS = {".md", ".html"}


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
                if fn in EXEMPT_FILES:
                    continue
                ext = os.path.splitext(fn)[1]
                if ext not in TARGET_EXTS:
                    continue
                path = os.path.join(root, fn)
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
