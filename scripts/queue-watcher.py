#!/usr/bin/env python3
"""
LLM Wiki — Ingest Queue Watcher
Detects PDFs in papers/ that lack a matching sources/*.md and
maintains .ingest-queue for batch processing.

Run periodically (e.g. via launchd) or call directly:
    python3 scripts/queue-watcher.py          # update queue, print status
    python3 scripts/queue-watcher.py --check  # print pending count only (exit 0)
"""

import json
import os
import sys
from datetime import datetime, timezone

PAPERS_DIR = "papers"
SOURCES_DIR = "sources"
QUEUE_FILE = ".ingest-queue"


def get_stems(directory, extension):
    return {
        os.path.splitext(f)[0]
        for f in os.listdir(directory)
        if f.endswith(extension)
    }


def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return {"pending": [], "processed": []}
    with open(QUEUE_FILE) as f:
        return json.load(f)


def save_queue(q):
    with open(QUEUE_FILE, "w") as f:
        json.dump(q, f, indent=2, ensure_ascii=False)


def main():
    check_only = "--check" in sys.argv

    pdfs = get_stems(PAPERS_DIR, ".pdf")
    srcs = get_stems(SOURCES_DIR, ".md")

    orphans = sorted(pdfs - srcs)  # PDFs without sources

    q = load_queue()

    # Clean up processed entries that were removed or are now ingested
    q["processed"] = [p for p in q["processed"] if p["stem"] in pdfs]
    processed_stems = {p["stem"] for p in q["processed"]}

    # Pending = orphans not yet processed
    pending_stems = {p["stem"] for p in q["pending"]}

    newly_added = []
    for stem in orphans:
        if stem not in pending_stems and stem not in processed_stems:
            entry = {
                "stem": stem,
                "filename": f"{stem}.pdf",
                "added": datetime.now(timezone.utc).isoformat(),
            }
            q["pending"].append(entry)
            newly_added.append(stem)

    # Remove pending entries that were since ingested
    q["pending"] = [p for p in q["pending"] if p["stem"] in (pdfs - srcs)]

    save_queue(q)

    pending_count = len(q["pending"])

    if check_only:
        print(pending_count)
        return

    if newly_added:
        print(f"📥  {len(newly_added)} new PDF(s) added to ingest queue:")
        for stem in newly_added:
            print(f"    {stem}")
        print()

    if pending_count == 0:
        print("✅  Ingest queue is empty — all papers are processed.")
    else:
        print(f"📋  Ingest queue: {pending_count} paper(s) pending")
        for entry in q["pending"]:
            added_dt = entry["added"][:10]
            print(f"    [{added_dt}] {entry['filename']}")
        print()
        print(f"  → Tell Claude: 'ingest 새로 추가된 논문들'")


if __name__ == "__main__":
    main()
