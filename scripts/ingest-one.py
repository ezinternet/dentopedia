#!/usr/bin/env python3
"""
ingest-one.py — One-paper-at-a-time sequential ingest helper

Sequential loop:
  1.  python3 scripts/ingest-one.py --next
      Prints next pending stem + extracted PDF text (up to 12 000 chars).
      Claude reads output, then writes sources/{stem}.md, wiki/{category}/{stem}.md, index.md.

  2.  python3 scripts/ingest-one.py --finish <stem>
      - Per-file git commits  (sources/{stem}.md, wiki/{category}/{stem}.md, index.md)
      - git push origin main
      - qmd update && qmd embed
      - Marks stem as processed in .ingest-queue

  3.  Repeat until `--next` prints "Queue is empty."
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAPERS = REPO / "papers"
SOURCES = REPO / "sources"
WIKI = REPO / "wiki"
PAPERS = REPO / "papers"
QUEUE_FILE = REPO / ".ingest-queue"
INDEX = REPO / "index.md"

MAX_CHARS = 12_000
MAX_PAGES = 15


# ── queue helpers ────────────────────────────────────────────────────────────

def load_queue():
    if not QUEUE_FILE.exists():
        return {"pending": [], "processed": []}
    return json.loads(QUEUE_FILE.read_text())


def save_queue(q):
    QUEUE_FILE.write_text(json.dumps(q, indent=2, ensure_ascii=False))


# ── PDF extraction ───────────────────────────────────────────────────────────

def extract_text(pdf_path: Path) -> str:
    try:
        import pypdf
    except ImportError:
        sys.exit("pypdf not installed: pip install pypdf")

    reader = pypdf.PdfReader(str(pdf_path))
    text = ""
    for page in reader.pages[:MAX_PAGES]:
        t = page.extract_text()
        if t:
            text += t + "\n"
        if len(text) > MAX_CHARS:
            break
    return text[:MAX_CHARS]


# ── git helpers ───────────────────────────────────────────────────────────────

def git(args, cwd=REPO):
    result = subprocess.run(
        ["git"] + args, cwd=str(cwd), capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def commit_file(rel_path: str, message: str):
    rc, _, err = git(["add", rel_path])
    if rc != 0:
        print(f"  [warn] git add {rel_path}: {err}")
        return
    rc, out, err = git(["commit", "-m", message + "\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"])
    if rc != 0 and "nothing to commit" not in err and "nothing to commit" not in out:
        print(f"  [warn] git commit {rel_path}: {err or out}")
    else:
        print(f"  ✓ committed: {rel_path}")


# ── commands ──────────────────────────────────────────────────────────────────

def cmd_next():
    """Print next pending paper's stem + extracted text."""
    q = load_queue()
    pending = q.get("pending", [])
    if not pending:
        print("Queue is empty. All papers are ingested.")
        return

    entry = pending[0]
    stem = entry["stem"]
    pdf = PAPERS / f"{stem}.pdf"

    if not pdf.exists():
        print(f"ERROR: PDF not found: {pdf}")
        print(f"  Remove '{stem}' from queue pending manually.")
        return

    print(f"NEXT_STEM: {stem}")
    print(f"PDF_PATH:  {pdf}")
    print("=" * 60)
    text = extract_text(pdf)
    print(text)
    print("=" * 60)
    remaining = len(pending) - 1
    print(f"\nQueue: {remaining} more paper(s) after this one.")


def cmd_finish(stem: str):
    """Per-file commit + push + qmd. Mark stem as processed."""
    print(f"\n── finishing ingest for: {stem} ──")

    # 1. Find all files belonging to this stem
    source_file = SOURCES / f"{stem}.md"
    wiki_files = list(WIKI.rglob(f"{stem}.md"))

    files_committed = 0

    if source_file.exists():
        commit_file(
            str(source_file.relative_to(REPO)),
            f"source: {stem}"
        )
        files_committed += 1
    else:
        print(f"  [warn] sources/{stem}.md not found — skipping")

    # papers artifact — only .txt is tracked (PDFs are gitignored).
    # PubMed-text ingests (source_collection: pubmed-text) carry a .txt that
    # must be committed; PDF ingests have no .txt and this block is skipped.
    paper_txt = PAPERS / f"{stem}.txt"
    if paper_txt.exists():
        commit_file(str(paper_txt.relative_to(REPO)), f"papers: {stem} text artifact")
        files_committed += 1

    for wf in sorted(wiki_files):
        rel = wf.relative_to(REPO)
        # derive category from path: wiki/{category}/{stem}.md
        parts = rel.parts  # ('wiki', 'category', 'stem.md') or deeper
        category = parts[1] if len(parts) >= 3 else "wiki"
        commit_file(str(rel), f"wiki({category}): {stem}")
        files_committed += 1

    # index.md — commit only if staged changes exist after adding
    rc, _, _ = git(["add", "index.md"])
    rc2, out, _ = git(["status", "--porcelain", "index.md"])
    if "M" in out or "A" in out:
        commit_file("index.md", f"index: add {stem}")
        files_committed += 1

    if files_committed == 0:
        print("  [warn] no files found to commit — did the ingest complete?")
        return

    # 2. Push
    print("\n  pushing to origin main …")
    rc, out, err = git(["push", "origin", "main"])
    if rc == 0:
        print("  ✓ pushed")
    else:
        print(f"  [warn] push failed: {err or out}")

    # 3. QMD update + embed
    print("\n  running qmd update && qmd embed …")
    env = {**os.environ, "PATH": f"/opt/homebrew/bin:{os.environ.get('PATH', '')}"}
    for cmd in [["qmd", "update"], ["qmd", "embed"]]:
        r = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, env=env)
        label = " ".join(cmd)
        if r.returncode == 0:
            print(f"  ✓ {label}")
        else:
            print(f"  [warn] {label}: {r.stderr.strip() or r.stdout.strip()}")

    # 4. Mark as processed in queue
    q = load_queue()
    q["pending"] = [p for p in q["pending"] if p["stem"] != stem]
    # avoid duplicate processed entries
    if not any(p["stem"] == stem for p in q.get("processed", [])):
        q.setdefault("processed", []).append({
            "stem": stem,
            "filename": f"{stem}.pdf",
            "processed": datetime.now(timezone.utc).isoformat(),
        })
    save_queue(q)
    print(f"\n  ✓ {stem} marked as processed in .ingest-queue")

    # 5. Next
    remaining = len(q["pending"])
    if remaining == 0:
        print("\n✅ Queue empty — all papers ingested.")
    else:
        print(f"\n📋 {remaining} paper(s) remaining. Run --next to continue.")


def cmd_status():
    q = load_queue()
    pending = q.get("pending", [])
    processed = q.get("processed", [])
    print(f"Pending : {len(pending)}")
    for p in pending:
        print(f"  {p['stem']}")
    print(f"Processed: {len(processed)}")


# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "--status":
        cmd_status()
    elif args[0] == "--next":
        cmd_next()
    elif args[0] == "--finish":
        if len(args) < 2:
            sys.exit("Usage: ingest-one.py --finish <stem>")
        cmd_finish(args[1])
    else:
        print(__doc__)
