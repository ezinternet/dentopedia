#!/usr/bin/env python3
"""qq — pretty wrapper around `qmd query` for readable terminal output.

`qmd query`'s default CLI output repeats a Context boilerplate, prints
diff-style `@@` meta lines, anchors snippets on frontmatter, and shows
scattered scores. This consumes qmd's `--format json` (robust) and reformats
into a compact, numbered, colorized list, enriching each hit with the real
page title + `## 한줄요약` read straight from the file. Fully local, no tokens.

Usage:
    scripts/qq.py "하중 임계값"            # hybrid query + rerank (default 8 hits)
    scripts/qq.py -n 20 "하중 임계값"      # more results
    scripts/qq.py -s "lithium disilicate"  # BM25 `qmd search` (fast, no LLM)
    scripts/qq.py --fast "burning mouth"   # skip LLM rerank (much faster on CPU)
    scripts/qq.py --no-snippet "..."       # titles + paths only

Quotes are optional for plain words; only needed when the query contains
shell metacharacters (?, *, >, <, |, (), $).

Alias (already in ~/.zshrc):
    alias qq='python3 /Users/oracleneo/llm-wiki/scripts/qq.py'
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

REPO_ROOT = "/Users/oracleneo/llm-wiki"

# ── ANSI colors (disabled when not a TTY or NO_COLOR set) ──────────────
_TTY = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def _c(code):
    return code if _TTY else ""


DIM, BOLD, RESET = _c("\033[2m"), _c("\033[1m"), _c("\033[0m")
CYAN, GREEN, YELLOW, RED, BLUE, GREY = (
    _c("\033[36m"), _c("\033[32m"), _c("\033[33m"),
    _c("\033[31m"), _c("\033[34m"), _c("\033[90m"),
)


def read_gist(rel_path):
    """Open the actual file and pull (title, one-liner) — local, no tokens.

    qmd anchors hits on frontmatter lines, so its snippet is often just YAML.
    Instead we read the file and extract the frontmatter `title:` plus the
    `## 한줄요약` / `## One-line Summary` body — the real gist of the page.
    """
    full = os.path.join(REPO_ROOT, rel_path)
    title, gist = "", ""
    try:
        with open(full, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError:
        return title, gist

    if lines and lines[0].strip() == "---":
        for ln in lines[1:]:
            if ln.strip() == "---":
                break
            m = re.match(r"\s*title:\s*(.+)", ln)
            if m:
                title = m.group(1).strip().strip('"').strip("'")
                break

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
    if not gist:  # overview pages: first 한국어 핵심요약 bullet
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


def strip_scheme(p):
    """qmd://wiki/foo.md → wiki/foo.md (repo-relative path for reading)."""
    return p[len("qmd://"):] if p.startswith("qmd://") else p


def shorten_path(p):
    """Repo-relative path → display path (drop leading wiki/ for compactness)."""
    return p[len("wiki/"):] if p.startswith("wiki/") else p


def wrap(text, width, indent):
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


def render(hits, show_snippet, snippet_lines):
    term_w = shutil.get_terminal_size((100, 24)).columns
    out = []
    for i, h in enumerate(hits, 1):
        sc = h["score"]
        scol = score_color(sc)
        score_txt = f"{sc:>3}%" if sc is not None else "  · "
        rel = strip_scheme(h["file"])      # wiki/...md — for reading the file
        path = shorten_path(rel)           # display path
        title, gist = read_gist(rel)
        if not title:
            title = h.get("title", "")
        out.append(f"{BOLD}{i:>2}{RESET}  {scol}{score_txt}{RESET} "
                   f"{scol}{bar(sc)}{RESET}  {CYAN}{path}{RESET}")
        if title:
            for wl in wrap(title, term_w - 6, "      "):
                out.append(f"{BOLD}{wl}{RESET}")
        if show_snippet and gist:
            budget = term_w - 6
            wrapped = wrap(gist, budget, "      ")
            if len(wrapped) > snippet_lines:
                wrapped = wrapped[:snippet_lines]
                wrapped[-1] = wrapped[-1].rstrip() + " …"
            for wl in wrapped:
                out.append(f"{GREY}{wl}{RESET}")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Readable qmd query wrapper")
    ap.add_argument("query", nargs="+", help="search query")
    ap.add_argument("-n", type=int, default=8, metavar="N",
                    help="max results (default 8)")
    ap.add_argument("-s", "--search", action="store_true",
                    help="BM25 `qmd search` (fast, no LLM) instead of `qmd query`")
    ap.add_argument("--fast", action="store_true",
                    help="skip LLM reranking (--no-rerank; much faster on CPU)")
    ap.add_argument("--snippet-lines", type=int, default=3, metavar="K",
                    help="one-liner lines per result (default 3)")
    ap.add_argument("--no-snippet", action="store_true", help="titles + paths only")
    args = ap.parse_args()

    query = " ".join(args.query)
    subcmd = "search" if args.search else "query"
    cmd = ["qmd", subcmd, query, "-n", str(args.n), "--format", "json"]
    if args.fast and not args.search:
        cmd.append("--no-rerank")

    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=sys.stderr, text=True)
    try:
        hits = json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError):
        sys.stdout.write(proc.stdout)  # fall back to raw on parse failure
        return proc.returncode
    # qmd scores are 0–1 floats → percent
    for h in hits:
        s = h.get("score")
        h["score"] = round(s * 100) if isinstance(s, (int, float)) else None

    if not hits:
        print(f"\n{YELLOW}no hits{RESET} for {BOLD}{query}{RESET} "
              f"{DIM}(try fewer/standard terms, or -s for BM25){RESET}\n")
        return proc.returncode

    print(f"\n{BLUE}🔍 {BOLD}{query}{RESET}  {DIM}({len(hits)} hits · {subcmd}){RESET}\n")
    print(render(hits, not args.no_snippet, args.snippet_lines))
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
