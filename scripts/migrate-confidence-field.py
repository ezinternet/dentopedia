#!/usr/bin/env python3
"""
Migrate frontmatter `confidence:` → `evidence_level:` across wiki/ and sources/.

Only replaces the key at the START of a line inside the frontmatter block
(between the opening `---` and the closing `---`). Body text is never touched.

Usage:
  python3 scripts/migrate-confidence-field.py            # dry-run (no writes)
  python3 scripts/migrate-confidence-field.py --apply    # live run
  python3 scripts/migrate-confidence-field.py --verify   # count residuals
"""

import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [ROOT / "wiki", ROOT / "sources"]

FM_RE = re.compile(r"^(---\n)(.*?)(\n---(?:\n|$))", re.DOTALL)
CONF_LINE_RE = re.compile(r"^confidence:", re.MULTILINE)

def migrate_text(text: str):
    m = FM_RE.match(text)
    if not m:
        return text, False
    head, fm_body, tail_sep = m.group(1), m.group(2), m.group(3)
    new_fm, n = CONF_LINE_RE.subn("evidence_level:", fm_body)
    if n == 0:
        return text, False
    after_fm = text[m.end():]
    return head + new_fm + tail_sep + after_fm, True

def collect_md_files():
    files = []
    for base in TARGETS:
        for p in sorted(base.rglob("*.md")):
            if "_lint" in p.parts or "_meta" in p.parts:
                continue
            files.append(p)
    return files

def main():
    apply  = "--apply"  in sys.argv
    verify = "--verify" in sys.argv

    files = collect_md_files()

    if verify:
        residuals = [p for p in files
                     if re.search(r"^confidence:", open(p, encoding="utf-8").read(), re.MULTILINE)]
        print(f"Residual `confidence:` files: {len(residuals)}")
        for p in residuals[:20]:
            print(f"  {p.relative_to(ROOT)}")
        return

    changed, skipped, errors = [], [], []
    for p in files:
        try:
            original = p.read_text(encoding="utf-8")
            new_text, did_change = migrate_text(original)
            if did_change:
                changed.append(p)
                if apply:
                    p.write_text(new_text, encoding="utf-8")
            else:
                skipped.append(p)
        except Exception as e:
            errors.append((p, e))

    mode = "APPLIED" if apply else "DRY-RUN"
    print(f"[{mode}] changed={len(changed)}  unchanged={len(skipped)}  errors={len(errors)}")
    if errors:
        for p, e in errors:
            print(f"  ERROR {p}: {e}")
    if not apply and changed:
        print(f"  (pass --apply to write changes)")

if __name__ == "__main__":
    main()
