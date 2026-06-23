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

REPO_ROOT = "/Users/oracleneo/llm-wiki"

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


def read_gist(rel_path):
    """Open the actual file and pull a human-readable (title, one-liner).

    qmd anchors hits on frontmatter lines (:2, :10), so the raw chunk snippet
    is just YAML. Instead we read the file locally (no tokens) and extract the
    frontmatter `title:` plus the `## 한줄요약` / `## One-line Summary` body —
    the actual "what is this page about" line.
    """
    full = os.path.join(REPO_ROOT, rel_path)
    title, gist = "", ""
    try:
        with open(full, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError:
        return title, gist

    # ── frontmatter title ──
    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            m = re.match(r"\s*title:\s*(.+)", ln)
            if m:
                title = m.group(1).strip().strip('"').strip("'")
                break

    # ── one-liner: prefer Korean 한줄요약, then English One-line Summary ──
    def section_body(header):
        for i, ln in enumerate(lines):
            if ln.strip() == header:
                buf = []
                for nxt in lines[i + 1:]:
                    s = nxt.strip()
                    if s.startswith("## "):
                        break
                    if s in ("", "---"):
                        if buf:
                            break
                        continue
                    buf.append(s)
                return " ".join(buf)
        return ""

    gist = (section_body("## 한줄요약")
            or section_body("## One-line Summary")
            or section_body("## Summary"))
    # overview pages: fall back to first 한국어 핵심요약 bullet
    if not gist:
        for ln in lines:
            s = ln.strip()
            if s.startswith("> -"):
                gist = s.lstrip("> -").strip()
                break
    return title, gist


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


def wrap(text, width, indent):
    """Soft-wrap text to width, prefixing each line with indent."""
    words, line, lines = text.split(), "", []
    for w in words:
        if line and len(line) + 1 + len(w) > width:
            lines.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        lines.append(line)
    return [indent + ln for ln in lines]


def render(blocks, max_results, show_snippet, snippet_lines):
    term_w = shutil.get_terminal_size((100, 24)).columns
    out = []
    shown = blocks[:max_results] if max_results else blocks
    for i, b in enumerate(shown, 1):
        sc = b["score"]
        scol = score_color(sc)
        score_txt = f"{sc:>3}%" if sc is not None else "  · "
        path = shorten_path(b["path"])
        # read the real title + one-liner from the file (local, no tokens)
        title, gist = read_gist(b["path"])
        if not title:
            title = b["title"]  # fall back to qmd's matched section header
        header = (f"{BOLD}{i:>2}{RESET}  {scol}{score_txt}{RESET} "
                  f"{scol}{bar(sc)}{RESET}  {CYAN}{path}{RESET}")
        out.append(header)
        if title:
            for wl in wrap(title, term_w - 6, "      "):
                out.append(f"{BOLD}{wl}{RESET}")
        if show_snippet and gist:
            budget = term_w - 6
            wrapped = wrap(gist, budget, "      ")[:snippet_lines]
            # mark truncation if the one-liner overflowed the line budget
            if len(wrap(gist, budget, "")) > snippet_lines and wrapped:
                wrapped[-1] = wrapped[-1].rstrip() + " …"
            for wl in wrapped:
                out.append(f"{GREY}{wl}{RESET}")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(add_help=True, description="Readable qmd query wrapper")
    ap.add_argument("query", nargs="+", help="search query")
    ap.add_argument("-n", type=int, default=0, metavar="N",
                    help="show only top N results (default: all)")
    ap.add_argument("-s", "--search", action="store_true",
                    help="use BM25 `qmd search` (fast, no LLM) instead of `qmd query`")
    ap.add_argument("--snippet-lines", type=int, default=3, metavar="K",
                    help="one-liner lines per result (default 3)")
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
