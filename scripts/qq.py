#!/usr/bin/env python3
"""qq — pretty wrapper around `qmd query` for readable terminal output.

`qmd query` prints a repeated Context boilerplate, diff-style `@@` meta lines,
and scattered scores that are hard to scan. This reformats the same results
into a compact, numbered, colorized list — no tokens, runs fully local.

Usage:
    scripts/qq.py "isq 하중 임계값"
    scripts/qq.py -n 3 "isq 하중 임계값"     # only top 3
    scripts/qq.py -s "lithium disilicate"     # use BM25 `qmd search` (faster, no LLM)
    scripts/qq.py --no-snippet "burning mouth" # titles + paths only

Recommended alias (add to ~/.zshrc):
    alias qq='python3 /Users/oracleneo/llm-wiki/scripts/qq.py'
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

# ── ANSI colors (disabled when not a TTY or NO_COLOR set) ──────────────
_TTY = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def c(code: str) -> str:
    return code if _TTY else ""


DIM = c("\033[2m")
BOLD = c("\033[1m")
RESET = c("\033[0m")
CYAN = c("\033[36m")
GREEN = c("\033[32m")
YELLOW = c("\033[33m")
RED = c("\033[31m")
BLUE = c("\033[34m")
GREY = c("\033[90m")

BLOCK_RE = re.compile(r"^qmd://(.+?):(\d+)\s+#\w+\s*$")
SCORE_RE = re.compile(r"^Score:\s+(\d+)%")
DIFF_RE = re.compile(r"^@@ ")

# Lines that are noise inside a snippet
SKIP_SNIPPET = re.compile(r"^(---\s*$|@@ )")


def parse_blocks(raw: str):
    """Yield dicts: {path, line, title, score, snippet:[lines]}."""
    lines = raw.splitlines()
    blocks = []
    cur = None
    section = None  # None | 'context' | 'snippet'
    for ln in lines:
        m = BLOCK_RE.match(ln)
        if m:
            if cur:
                blocks.append(cur)
            cur = {"path": m.group(1), "line": m.group(2),
                   "title": "", "score": None, "snippet": []}
            section = "head"
            continue
        if cur is None:
            continue
        if ln.startswith("Title:"):
            cur["title"] = ln[len("Title:"):].strip()
            continue
        if ln.startswith("Context:"):
            section = "context"
            continue
        sm = SCORE_RE.match(ln)
        if sm:
            cur["score"] = int(sm.group(1))
            section = "preview"  # next comes the @@ line then snippet
            continue
        if DIFF_RE.match(ln):
            section = "snippet"
            continue
        if section == "snippet":
            if SKIP_SNIPPET.match(ln):
                continue
            cur["snippet"].append(ln)
    if cur:
        blocks.append(cur)
    # trim trailing blank snippet lines
    for b in blocks:
        while b["snippet"] and not b["snippet"][-1].strip():
            b["snippet"].pop()
        while b["snippet"] and not b["snippet"][0].strip():
            b["snippet"].pop(0)
    return blocks


def score_color(s):
    if s is None:
        return GREY
    if s >= 80:
        return GREEN
    if s >= 55:
        return YELLOW
    return RED


def bar(s, width=10):
    if s is None:
        return " " * width
    filled = round(s / 100 * width)
    return "█" * filled + "░" * (width - filled)


def shorten_path(p):
    # drop leading wiki/ for compactness, keep category context
    return p[len("wiki/"):] if p.startswith("wiki/") else p


def render(blocks, max_results, show_snippet, snippet_lines):
    term_w = shutil.get_terminal_size((100, 24)).columns
    out = []
    shown = blocks[:max_results] if max_results else blocks
    for i, b in enumerate(shown, 1):
        sc = b["score"]
        scol = score_color(sc)
        score_txt = f"{sc:>3}%" if sc is not None else "  · "
        path = shorten_path(b["path"])
        header = (f"{BOLD}{i:>2}{RESET}  {scol}{score_txt}{RESET} "
                  f"{scol}{bar(sc)}{RESET}  {CYAN}{path}{RESET}{DIM}:{b['line']}{RESET}")
        out.append(header)
        if b["title"]:
            out.append(f"      {BOLD}{b['title']}{RESET}")
        if show_snippet:
            shown_lines = 0
            for sl in b["snippet"]:
                if not sl.strip():
                    continue
                text = sl.strip()
                budget = term_w - 6
                if len(text) > budget:
                    text = text[:budget - 1] + "…"
                out.append(f"      {GREY}{text}{RESET}")
                shown_lines += 1
                if shown_lines >= snippet_lines:
                    break
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(add_help=True, description="Readable qmd query wrapper")
    ap.add_argument("query", nargs="+", help="search query")
    ap.add_argument("-n", type=int, default=0, metavar="N",
                    help="show only top N results (default: all)")
    ap.add_argument("-s", "--search", action="store_true",
                    help="use BM25 `qmd search` (fast, no LLM) instead of `qmd query`")
    ap.add_argument("--snippet-lines", type=int, default=2, metavar="K",
                    help="snippet lines per result (default 2)")
    ap.add_argument("--no-snippet", action="store_true", help="titles + paths only")
    args = ap.parse_args()

    query = " ".join(args.query)
    subcmd = "search" if args.search else "query"
    # let qmd's progress spinner go to the user's terminal (stderr); capture stdout
    proc = subprocess.run(
        ["qmd", subcmd, query],
        stdout=subprocess.PIPE, stderr=sys.stderr, text=True,
    )
    raw = proc.stdout
    blocks = parse_blocks(raw)
    if not blocks:
        # fall back to raw output if parsing found nothing
        sys.stdout.write(raw)
        return proc.returncode

    print(f"\n{BLUE}🔍 {BOLD}{query}{RESET}  {DIM}({len(blocks)} hits · {subcmd}){RESET}\n")
    print(render(blocks, args.n, not args.no_snippet, args.snippet_lines))
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
