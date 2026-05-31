---
name: ingest-paper
description: Add a new dental research PDF to the LLM Wiki. Handles the full 4-step pipeline: copy PDF → write sources/*.md → write wiki/{category}/*.md → update index.md. Invoke when the user says "논문 추가", "ingest", or provides a PDF path. Always run lint after completing.
argument-hint: [/path/to/paper.pdf]
allowed-tools: Bash, Read, Write, Edit
---

# Ingest Paper Skill

Full pipeline to add a dental research PDF into the LLM Wiki knowledge base.

## Workflow

### Step 1 — Receive and validate input

The argument is an absolute path to a PDF file. Confirm it exists:

```bash
ls -lh "/path/to/paper.pdf"
```

If the file does not exist, stop and tell the user.

---

### Step 2 — Extract text and determine canonical stem

Extract up to 12,000 characters from the first 15 pages:

```bash
python3 -c "
import pypdf, sys
reader = pypdf.PdfReader(sys.argv[1])
text = ''
for page in reader.pages[:15]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print(text[:12000])
" "/path/to/paper.pdf"
```

From the extracted text, identify:
- **First author last name** (lowercase)
- **Publication year** (4 digits)
- **First 5 meaningful title words** (lowercase, spaces → hyphens, strip special chars)

Build the **canonical stem**:
```
{first-author-lastname}-{year}-{first-5-title-words}
```

Examples:
- `wu-2025-mb2-prevalence-maxillary-molar-han`
- `kaur-2024-eal-vs-radiograph-working-length`

Check for duplicates before proceeding:

```bash
python3 -c "
import os, hashlib
new = hashlib.md5(open('/path/to/paper.pdf','rb').read()).hexdigest()
for f in os.listdir('papers'):
    if f.endswith('.pdf'):
        existing = hashlib.md5(open(f'papers/{f}','rb').read()).hexdigest()
        if existing == new:
            print(f'DUPLICATE: {f}')
            break
else:
    print('OK: no duplicate')
"
```

If duplicate found → stop, inform user, delete the new file if it's in a temp location.

---

### Step 3 — Copy PDF to `papers/`

```bash
cp "/path/to/paper.pdf" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```

Verify the copy succeeded.

---

### Step 4 — Determine category

See [reference.md](reference.md) for the full category list. Choose the **single best category** based on the paper's primary method or procedure — not by disease or anatomy.

---

### Step 5 — Write `sources/{stem}.md`

Use the template in [reference.md](reference.md) → **Sources Template** section.

Fill in all fields from the extracted text:
- `title`: exact paper title
- `authors`: all authors, comma-separated
- `year`: publication year
- `doi`: DOI string only (no URL prefix)
- `category`: chosen category folder
- `pdf_path`: `/Users/oracleneo/llm-wiki/papers/{stem}.pdf`
- `pdf_filename`: `{stem}.pdf`

Sections to write:
1. **One-line Summary** — study type, n, key finding in one English sentence
2. **Document Information** — journal, DOI, institution
3. **Key Contributions** — bullet points of novel claims
4. **Methodology** — design, databases, n, outcomes
5. **Key Results** — numbers, tables, p-values
6. **Limitations** — explicitly stated or inferred
7. **Related Work** — wikilinks to relevant existing pages
8. **Glossary** — 3–6 key terms with definitions

---

### Step 6 — Write `wiki/{category}/{stem}.md`

Use the template in [reference.md](reference.md) → **Wiki Template** section.

Required frontmatter fields (all 9 must be present — lint checks these):
```
title, authors, year, doi, source, category, confidence, pdf_path, pdf_filename
```

Additional required fields:
- `date`: publication date `YYYY-MM-DD`; use `YYYY-01-01` if only year known; use ingest date if neither recoverable
- `tags`: relevant keywords as YAML list

Body sections (in order):
1. `## 한줄요약` — Korean one-liner: study type, n, key finding in plain Korean. Use **한국어 (English, 약어)** notation for technical terms.
2. `## Summary` — English paragraph, 3–5 sentences
3. `## Key Contributions`
4. `## Methodology`
5. `## Results` — include tables where helpful
6. `## Related Papers` — `[[category/stem]]` wikilinks with relationship description

Confidence vocabulary — pick the single best label. See [reference.md](reference.md) → **Confidence Vocabulary**.

---

### Step 7 — Update `index.md`

Add a one-line entry under the correct section heading in `/Users/oracleneo/llm-wiki/index.md`:

```
- [[{category}/{stem}]] — {one-line Korean summary with key numbers}
```

Find the correct section by matching the category to the section header. Use Edit tool to insert the new line at the **bottom** of the correct section (just before the blank line before the next `##`).

---

### Step 8 — Run lint

```bash
python3 -c "
import os, re
WIKI_DIR = 'wiki'
REQUIRED_FIELDS = ['title','authors','year','doi','source','category','confidence','pdf_path','pdf_filename']
SKIP_DIRS = {'_lint', 'overviews'}
errors = []
ok = 0
for root, dirs, files in os.walk(WIKI_DIR):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fn in files:
        if not fn.endswith('.md'): continue
        path = os.path.join(root, fn)
        with open(path) as f: content = f.read()
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m: errors.append(f'NO FRONTMATTER: {path}'); continue
        fm = m.group(1)
        missing = [field for field in REQUIRED_FIELDS if not re.search(rf'^{field}\s*:', fm, re.MULTILINE)]
        if missing: errors.append(f'MISSING {missing}: {path}')
        else: ok += 1
print(f'OK: {ok}  ERRORS: {len(errors)}')
for e in errors: print(e)
"
```

If errors → fix them before reporting completion.

---

### Step 9 — Orphan check

```bash
python3 -c "
import os
papers = {f[:-4] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs   = {f[:-3] for f in os.listdir('sources') if f.endswith('.md')}
orphan_pdfs = papers - srcs
orphan_srcs = srcs - papers
if orphan_pdfs: print('ORPHAN PDFs (delete):', orphan_pdfs)
if orphan_srcs: print('ORPHAN sources (missing PDF):', orphan_srcs)
if not orphan_pdfs and not orphan_srcs: print('OK: 1:1 match')
"
```

---

### Step 10 — Refresh search index (qmd)

A new wiki page is invisible to semantic search until qmd re-indexes and embeds it.
Run this **after** the wiki/sources files are written and lint passes:

```bash
# brew node(v25+)를 강제 — PATH에 구 node v18이 앞설 경우 ABI 불일치로 qmd가 깨짐.
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
qmd update      # 파일시스템 재스캔 — 신규 wiki/sources md 등록
qmd embed       # 신규 문서만 임베딩 (incremental — 1~2편이면 수 초)
```

Then confirm the new page is searchable (should return the new stem):

```bash
export PATH="/opt/homebrew/bin:$PATH"
qmd query "{paper topic in a few words}" -c wiki 2>/dev/null | grep -i "{stem}" | head -1
```

Notes:
- `qmd embed` is **incremental** — it only embeds documents whose content changed, so a single new paper finishes in seconds. Never use `-f` here (that forces a full re-embed of all ~1,800 docs, ~2.5 h).
- If `qmd` errors with `NODE_MODULE_VERSION` / `ERR_UNKNOWN_FILE_EXTENSION`, the wrong Node is on PATH. The `export PATH=...` line above fixes it; if it persists, run `cd /opt/homebrew/lib/node_modules/@tobilu/qmd && npm rebuild better-sqlite3`.
- The qmd MCP daemon picks up the new vectors automatically — no restart needed.

---

### Step 11 — Report completion

Tell the user:
```
✅ Ingest complete: {stem}
   Category  : {category}
   Confidence: {confidence}
   Lint      : OK {n} files, 0 errors
   Index     : added to {section heading}
   Search    : qmd re-indexed + embedded (searchable now)
```

---

## Rules

1. **No web search.** All content must come from the PDF only. Never use WebSearch or WebFetch to fill gaps.
2. Work from `/Users/oracleneo/llm-wiki/` as the base directory (all relative paths are from here).
3. All bash commands must be run from `/Users/oracleneo/llm-wiki/`.
4. **Term notation in Korean text**: always write technical terms as **한국어 (English, 약어)** — e.g., 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC).
5. Never guess DOI — extract from PDF text. If not found, write `unknown`.
6. If the paper is non-dental, do not ingest — delete the PDF and tell the user.
7. If duplicate detected (MD5 match), do not overwrite existing files — tell the user which stem it matches.
