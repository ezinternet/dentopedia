#!/usr/bin/env python3
"""
LLM Wiki — DeepSeek ingest prompt emitter.

Prints the exact text to paste into a new DeepSeek conversation (alongside the
PDF attachment): the PROMPT B category-list preamble + the live category list +
PROMPT A.

Why a script instead of a saved paste-file: both halves have a single source of
truth already — the prompt text lives in `deepseek-ingest-prompt 1.md`, the
category list in `wiki/_meta/categories.md`. A second copy of either would
drift silently, and a stale category list is exactly the failure that sends
DeepSeek's CATEGORY_CANDIDATES to a folder that no longer exists.

Usage:
  python3 scripts/deepseek-prompt.py | pbcopy    # → clipboard, paste in DeepSeek
  python3 scripts/deepseek-prompt.py --no-categories   # PROMPT A only
Exit codes: 0 ok · 2 a source file or block is missing
"""

from __future__ import annotations

import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_DOC = os.path.join(REPO, "deepseek-ingest-prompt 1.md")
CATEGORIES = os.path.join(REPO, "wiki", "_meta", "categories.md")

CAT_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|")


def fenced_blocks(text: str) -> list[tuple[str, str]]:
    """[(heading the block sits under, block body)] for every ``` fence."""
    out: list[tuple[str, str]] = []
    heading = ""
    buf: list[str] | None = None
    for line in text.splitlines():
        if line.startswith("```"):
            if buf is None:
                buf = []
            else:
                out.append((heading, "\n".join(buf)))
                buf = None
            continue
        if buf is not None:
            buf.append(line)
        elif line.startswith("## "):
            heading = line[3:].strip()
    return out


def read(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description="Emit the DeepSeek ingest prompt.")
    ap.add_argument("--no-categories", action="store_true",
                    help="skip the PROMPT B category list (PROMPT A only)")
    args = ap.parse_args()

    blocks = fenced_blocks(read(PROMPT_DOC))
    prompt_a = next((b for h, b in blocks if h.startswith("PROMPT A")), None)
    if not prompt_a:
        print(f"ERROR: no PROMPT A fenced block in {os.path.basename(PROMPT_DOC)}",
              file=sys.stderr)
        return 2

    parts: list[str] = []
    if not args.no_categories:
        preamble = next((b for h, b in blocks
                         if h.startswith("PROMPT B") and "카테고리 폴더 목록" in b), None)
        cats = [f"{m.group(1)} = {m.group(2)}"
                for m in (CAT_ROW.match(l) for l in read(CATEGORIES).splitlines()) if m]
        if not preamble or not cats:
            print("ERROR: PROMPT B preamble or category table not found "
                  "(check wiki/_meta/categories.md table format)", file=sys.stderr)
            return 2
        parts.append(preamble.strip())
        parts.append(" / ".join(cats))

    parts.append(prompt_a.strip())
    print("\n\n".join(parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
