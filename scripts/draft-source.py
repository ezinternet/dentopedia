#!/usr/bin/env python3
"""draft-source.py — Generate a sources/{stem}.md draft from a research PDF.

Reads a PDF, sends it to the Claude API as a document block, and asks the model
to produce a structured `sources/` page draft that follows the LLM Wiki
conventions in CLAUDE.md (English body, bilingual one-line summaries, the seven
numbered sections, and a `## Why Ingested` rationale).

The script ASSEMBLES the YAML frontmatter itself (pdf_path / pdf_filename /
source_collection are filled deterministically) so those fields are always
correct; the model only supplies the scalar metadata and the markdown body.

This is a DRAFT generator — a human (or the ingest skill) still:
  - adds the real `[[wikilink]]` in `## Why Ingested`,
  - confirms the category and stem,
  - copies the PDF into papers/{stem}.pdf,
  - writes the matching wiki/ page, updates index.md, and refreshes qmd.

Rule #1 (no web search) is respected: the only source is the PDF you pass in.

Usage:
    export ANTHROPIC_API_KEY=...   # or `ant auth login`
    python3 scripts/draft-source.py /path/to/paper.pdf
    python3 scripts/draft-source.py /path/to/paper.pdf --stdout
    python3 scripts/draft-source.py /path/to/paper.pdf --out sources/foo.md --force
    python3 scripts/draft-source.py /path/to/paper.pdf --category endodontics/irrigation
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path

REPO = Path("/Users/oracleneo/llm-wiki")
WIKI = REPO / "wiki"
PAPERS = REPO / "papers"
SOURCES = REPO / "sources"

MAX_PDF_BYTES = 32 * 1024 * 1024  # API hard limit: 32 MB request
DEFAULT_MODEL = "claude-opus-4-8"


def discover_categories() -> list[str]:
    """Build the valid category list from the live wiki/ directory tree.

    Returns folder names one and two levels deep, e.g. "endodontics",
    "endodontics/irrigation", "sinus-lift/lateral".
    """
    cats: list[str] = []
    if not WIKI.is_dir():
        return cats
    for parent in sorted(WIKI.iterdir()):
        if not parent.is_dir() or parent.name.startswith((".", "_")):
            continue
        subs = [s for s in sorted(parent.iterdir())
                if s.is_dir() and not s.name.startswith((".", "_"))]
        if subs:
            for s in subs:
                cats.append(f"{parent.name}/{s.name}")
        cats.append(parent.name)  # parent itself is always a valid bucket
    return cats


SYSTEM_PROMPT = """You are a meticulous dental-research librarian writing a \
source-summary page for a personal clinical knowledge wiki.

You are given ONE research paper as a PDF. Produce a faithful, detailed summary \
grounded STRICTLY in that PDF. Do not invent findings, numbers, citations, or \
authors. If a value is not in the paper, omit it rather than guessing.

Hard rules:
- The markdown BODY must be in ENGLISH (RAG-friendly), EXCEPT the `## 한줄요약` \
section which must be in Korean.
- Both one-line summaries (English `## One-line Summary` and Korean `## 한줄요약`) \
must state: study type, n (sample size), and the single key finding.
- Use specific numbers from the paper (sample sizes, p-values, effect sizes, %, \
follow-up duration) wherever the paper provides them.

The `body_markdown` field MUST contain exactly these sections, in this order, \
and MUST begin with `## Why Ingested`:

## Why Ingested
(1-2 sentences on why this paper matters / what gap or comparison it fills. \
Because you cannot see the existing wiki, end this section with the literal line:
<!-- TODO: add at least one [[wiki/category/stem]] wikilink to a related page -->)

## One-line Summary
(English: study type, n, key finding — one sentence)

## 한줄요약
(Korean: study type, n, key finding — one sentence, plain Korean)

## 1. Document Information
(bullet list: Title, Authors (with country if stated), Journal/year, DOI, Type, Source)

## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary

Match the depth of a thorough literature note: bullet points, bolded key terms, \
concrete values. Do not wrap the body in code fences.

Separately return the scalar metadata:
- `stem`: filename stem as {first-author-lastname}-{year}-{first-5-title-words}, \
all lowercase, special chars stripped, spaces -> hyphens, year is 4 digits.
- `title`, `authors` (comma-separated), `year` (4-digit integer), `doi` ("" if none).
- `category`: choose the SINGLE best value from the allowed list provided by the \
user. Classify by method/procedure, not by disease or anatomy. Return it verbatim."""


def build_user_blocks(pdf_b64: str, categories: list[str]) -> list[dict]:
    cat_list = "\n".join(f"- {c}" for c in categories)
    instruction = (
        "Summarize the attached paper as a wiki source page following the system "
        "instructions.\n\nAllowed `category` values (pick exactly one, verbatim):\n"
        f"{cat_list}"
    )
    return [
        {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": pdf_b64,
            },
        },
        {"type": "text", "text": instruction},
    ]


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "stem": {"type": "string"},
        "title": {"type": "string"},
        "authors": {"type": "string"},
        "year": {"type": "integer"},
        "doi": {"type": "string"},
        "category": {"type": "string"},
        "body_markdown": {"type": "string"},
    },
    "required": ["stem", "title", "authors", "year", "doi", "category", "body_markdown"],
    "additionalProperties": False,
}


def assemble_page(data: dict, pdf_filename: str) -> str:
    """Build the full sources/*.md content: frontmatter + body."""
    doi = data.get("doi") or ""
    fm_lines = [
        "---",
        f'title: "{data["title"]}"',
        f"authors: {data['authors']}",
        f"year: {data['year']}",
        f"doi: {doi}",
        f"category: [{data['category']}]",
        f"pdf_path: {PAPERS}/{pdf_filename}",
        f"pdf_filename: {pdf_filename}",
        "source_collection: external",
        "---",
        "",
    ]
    body = data["body_markdown"].strip()
    return "\n".join(fm_lines) + body + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate a sources/{stem}.md draft from a research PDF.",
    )
    ap.add_argument("pdf", help="Path to the research PDF")
    ap.add_argument("--out", help="Output path (default: sources/{stem}.md)")
    ap.add_argument("--stdout", action="store_true",
                    help="Print to stdout instead of writing a file")
    ap.add_argument("--category",
                    help="Force a category (else the model picks from wiki/)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--force", action="store_true",
                    help="Overwrite the output file if it already exists")
    args = ap.parse_args()

    pdf_path = Path(args.pdf).expanduser()
    if not pdf_path.is_file():
        print(f"error: PDF not found: {pdf_path}", file=sys.stderr)
        return 1
    size = pdf_path.stat().st_size
    if size > MAX_PDF_BYTES:
        print(f"error: PDF is {size/1e6:.1f} MB; API limit is 32 MB. "
              "Split it or use the Files API.", file=sys.stderr)
        return 1

    try:
        import anthropic
    except ImportError:
        print("error: pip install anthropic", file=sys.stderr)
        return 1

    categories = discover_categories()
    if not categories:
        print(f"error: no categories found under {WIKI}", file=sys.stderr)
        return 1
    if args.category and args.category not in categories:
        print(f"warning: '{args.category}' is not an existing wiki category",
              file=sys.stderr)

    pdf_b64 = base64.standard_b64encode(pdf_path.read_bytes()).decode("ascii")

    client = anthropic.Anthropic()
    print(f"→ reading {pdf_path.name} ({size/1e6:.1f} MB) with {args.model} ...",
          file=sys.stderr)

    resp = client.messages.create(
        model=args.model,
        max_tokens=args.max_tokens,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_blocks(pdf_b64, categories)}],
        output_config={"format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
    )

    if resp.stop_reason == "refusal":
        print("error: model refused this request.", file=sys.stderr)
        return 1
    if resp.stop_reason == "max_tokens":
        print("warning: output hit max_tokens — body may be truncated. "
              "Re-run with --max-tokens 32000.", file=sys.stderr)

    raw = next((b.text for b in resp.content if b.type == "text"), None)
    if not raw:
        print("error: no text returned by the model.", file=sys.stderr)
        return 1
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"error: could not parse model JSON: {e}\n---\n{raw[:500]}",
              file=sys.stderr)
        return 1

    if args.category:
        data["category"] = args.category
    elif data["category"] not in categories:
        print(f"warning: model chose category '{data['category']}' which is not "
              "an existing wiki folder — confirm before ingesting.", file=sys.stderr)

    stem = data["stem"]
    pdf_filename = f"{stem}.pdf"
    page = assemble_page(data, pdf_filename)

    if args.stdout:
        print(page)
        _print_next_steps(stem, data["category"], pdf_path, to_stderr=True)
        return 0

    out = Path(args.out).expanduser() if args.out else SOURCES / f"{stem}.md"
    if out.exists() and not args.force:
        print(f"error: {out} already exists. Use --force to overwrite, "
              "--out to pick another path, or --stdout to preview.", file=sys.stderr)
        return 1
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"✓ wrote {out}", file=sys.stderr)
    _print_next_steps(stem, data["category"], pdf_path, to_stderr=True)
    return 0


def _print_next_steps(stem: str, category: str, pdf_path: Path, to_stderr: bool):
    f = sys.stderr if to_stderr else sys.stdout
    print("\nNEXT STEPS (draft — review before ingesting):", file=f)
    print(f"  1. Fill the [[wikilink]] in '## Why Ingested' (search the wiki "
          "for a related page).", file=f)
    print(f"  2. Confirm category: {category}", file=f)
    print(f"  3. Copy the PDF:  cp '{pdf_path}' '{PAPERS}/{stem}.pdf'", file=f)
    print(f"  4. Write the wiki/{category}/{stem}.md page + update index.md.", file=f)
    print("  5. Run lint + qmd update/embed.", file=f)


if __name__ == "__main__":
    raise SystemExit(main())
