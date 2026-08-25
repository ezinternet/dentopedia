# INGEST — Paper Ingestion Pipeline (치과학 llm-wiki)

CLAUDE.md의 **Adding a New Paper** 세부 절차를 분리한 파일. CLAUDE.md 본문은 3-tier 원칙·라우팅·audit만 담고, ingest 실행 세부(Step 0–5, 분기, PDF 규칙, 필드 정의)는 여기서 단일 관리한다. `wiki/_meta/categories.md`를 분리한 것과 같은 이유 — context 절약 + 단일 출처.

**When to read this file**: 논문을 위키에 추가(`인제스트`, `Add this paper`, PDF 경로 언급)하는 작업이면 이 파일을 먼저 연다. 답변 생성(질문 대답)에는 필요 없다.

---

## Adding a New Paper

Say: *"Add this paper to the wiki: /path/to/paper.pdf"*
Or: *"인제스트 해줘"* (processes all pending papers in the queue — parallel subagents)

**Parallel-subagent protocol — content in parallel, finalize in serial**

When multiple papers are pending, fan them out to **one subagent per paper** for the content work, then have the **parent serially finalize** (index + commit + push + qmd). This is faster than one-at-a-time *without* reintroducing context exhaustion, because each subagent gets its own fresh context window — the old single-context batch failure mode (5+ papers fill the main context and later papers fail silently) cannot happen when each paper lives in its own subagent.

```
PHASE 1 — fan out (parallel):  one subagent per pending stem
  Each subagent, for its ONE paper, runs Steps 0–3 below:
    • Step 0  dedup + retraction gate (scripts/dedup-check.py — DOI + 제목 정규화) — if duplicate, STOP and report "skip:<reason>"
    • rename PDF papers/{raw}.pdf → papers/{canonical-stem}.pdf
    • Step 2–3  write sources/{stem}.md + wiki/{category}/{stem}.md
  Subagent does NOT touch index.md, does NOT git-commit/push, does NOT run qmd.
  Subagent RETURNS: {stem, category, index_line, status: ok|skip:<reason>}
  Subagent LOGS deviations: whenever a non-standard situation is handled, call immediately:
    python3 scripts/log-deviation.py <stem> <type> "<description>"
    This is non-blocking (<1s) and feeds the Rule-of-Three SOP evolution trigger.

    <type> MUST come from the vocabulary in scripts/log-deviation.py — that docstring is
    the SSOT and defines what each type means. Do not guess a type and do not reach for
    `other`: an unknown string is silently downgraded to `other`, and `other` is invisible
    to the rule-of-three trigger. Current types:

      full text   empty-pmc-text · partial-pmc-text · abstract-only
      duplicate   duplicate-skip · duplicate-distinct · doi-conflict · rename-collision
      judgment    supersession-judgment · relation-judgment · category-judgment ·
                  wrong-category · confidence-judgment
      metadata    no-doi · date-fallback
      source/tool source-data-issue · qmd-unavailable · batch-relation-pending
      pipeline    why-ingested-skipped · step-skipped · other

    Log the JUDGMENT, not just the accident — a supersession call, a contradicts edge, or a
    category boundary you had to think about are all deviations worth a row, because three
    of them in a row is how this SOP learns. Do NOT log non-deviations: "standard ingest,
    no deviations" is not a row, it is silence.

    *Why this list is here:* on 2026-07-17 a reclassification found 87 of 92 `other` rows
    already had a home in this vocabulary. Agents were defaulting to `other` because this
    instruction said only "<type>" and never showed the options, so deviation-audit.py
    reported "92x other" — a rule-of-three trigger that could not fire. Keep the list
    visible here; keep the definitions in log-deviation.py.

PHASE 2 — finalize (serial, parent only — avoids git/index races):
  for each returned ok-paper (one at a time, in order):
    • Step 4  add its index_line to index.md
    • Step 5a  lint that page (scripts/lint.py) + orphan check (scripts/orphan-check.py)
    • python3 scripts/ingest-one.py --finish <stem>
        ← per-file git commit + push + qmd update/embed (incremental) + mark processed
  for each returned skip-paper: delete the duplicate PDF, mark queue processed (no page)

  AFTER the loop (large fan-out only, ≳5 papers): per-`--finish` incremental embeds can
  leave a backlog that exits 0 without finishing (daemon session expiry). Check the REAL
  backlog, then drain — see Step 5 for the full rules:
    • qmd status | grep Pending          ← 진짜 백로그 (update가 찍는 숫자는 거짓)
    • 남아 있으면 무인 드레인 (세션 죽어도 계속):
        launchctl kickstart gui/$(id -u)/com.llmwiki.embed-until-done
      (소량이라 세션 내에서 끝낼 거면: bash scripts/embed-until-done.sh &)
```

Why this split: file writes to distinct paths (`sources/*`, `wiki/*`, distinct PDFs) are conflict-free in parallel, so PHASE 1 parallelizes the real bottleneck (PDF read + page authoring — this is what was slow). But `index.md` edits and `git add/commit/push` share mutable state — running them concurrently races/corrupts the index and the git tree — so PHASE 2 keeps them strictly serial in the parent. Subagents do NOT use `isolation: worktree` (they must write into the main working tree the parent then commits). `qmd embed` is incremental (only changed docs, seconds), so running it inside each `--finish` is cheap; never force a full re-embed (`-f`). Caveat for large fan-outs: incremental embeds can accumulate a backlog the daemon leaves half-done (exit 0 ≠ complete), so PHASE 2 ends by checking `qmd status | grep Pending` and, if work remains, draining it until the `"All content hashes already have embeddings"` marker appears. Prefer the launchd job (`launchctl kickstart gui/$(id -u)/com.llmwiki.embed-until-done`) over a bare `bash scripts/embed-until-done.sh` for anything sizable — the bare script is session-bound and dies with the Claude Code session, while a big backlog takes ~10 passes / overnight. See Step 5.

Helper: `python3 scripts/ingest-one.py --next` prints one stem+text for a single subagent; read `.ingest-queue` `pending[]` to enumerate all stems to fan out in PHASE 1. For a single paper, skip the fan-out and run Steps 0–4 + `--finish` inline (no subagent needed).

The agent will do all steps automatically.

---

## Step 0 — Pre-ingest gate (dedup + retraction)

Before copying anything, run two checks. Skipping these is how the wiki accumulates duplicate and discredited pages.

1. **DOI / cross-stem duplicate check.** `scripts/dedup-check.py`를 돌린다. 맨 grep 대신 이걸 쓰는 이유는 아래 *왜 grep이 샜나*.

   ```bash
   python3 scripts/dedup-check.py --pdf /path/to/paper.pdf     # DOI·제목 자동 추출
   python3 scripts/dedup-check.py --doi 10.xxxx/yyy            # DOI를 이미 알 때
   python3 scripts/dedup-check.py --title "논문 제목 전체"       # DOI 없는 논문
   ```

   **exit 1이면 STOP** — 신규 페이지를 만들지 말고 출력된 기존 stem을 갱신한다. 팬아웃 서브에이전트는 `skip:<reason>`을 반환한다. exit 0이면 진행.

   무엇을 보는가: (a) DOI 정규화 후 정확일치 (`https://doi.org/` prefix·대소문자·후행 구두점 차이 흡수, `unknown`·`n/a` 같은 placeholder는 무효 처리), (b) **제목 정규화 후 정확일치**, (c) **제목 토큰 Jaccard ≥ 0.75 근사일치**. 정규화 함수는 `doi-duplicate-check.py`에서 **import해서 쓴다** — 복제하지 않는다(두 벌은 반드시 drift한다).

   **왜 grep이 샜나 (2026-08-25).** Step 0은 DOI grep이 전부였고 no-DOI 경로는 "title + first-author grep"이라는 **문장으로만** 있었다. 실제 grep은 표기 차이(대소문자·문장부호·괄호 병기·하이픈)에 그대로 깨진다. 결과가 `logs/ingest-deviations.md`에 duplicate-skip 22건 + duplicate-distinct 3건으로 쌓였고, 로그의 근본원인 문구가 그대로다 — *"DOI conflict/cross-stem duplicate: ... (doi was null, missed by Step0 grep)"*. `doi-duplicate-check.py`에는 제목 정규화 fallback이 **이미 있었지만 사후 일간 감사에만 있고 인제스트 시점에는 없었다.** 같은 로직을 앞단으로 당긴 것이 이 스크립트다.

   오탐 걱정은 실측으로 눌렀다: 제목이 극히 비슷한 형제 3편(`ada-2024-chairside-guide-adult-extraction` / `-pulpitis` / `carrasco-labra-2024-...-guideline`)을 교차 입력했을 때 각각 **자기 하나씩만** 맞았다(2026-08-25). 임계값 0.75는 부제 유무·전치사 차이는 흡수하고 다른 논문은 거른다.

   **No-DOI 논문.** DOI가 없으면 frontmatter `doi:`를 `null`(또는 `n/a (Journal Year;Vol(Iss):pp; PMID xxxxx)` — `vetromilla-2021`/`merli-2018` 선례)로 두고, dedup은 위 `--title` 경로가 자동으로 담당한다. `python3 scripts/log-deviation.py <stem> no-doi "..."` 기록은 그대로.

   > 사후 감사인 `scripts/doi-duplicate-check.py`(일간 signal)는 그대로 남는다 — 이 게이트를 우회해 들어온 것, 그리고 게이트 도입 이전에 쌓인 것을 계속 본다.

2. **Retraction check.** Verify via PubMed MCP (`get_article_metadata` → `article_types` contains `"Retracted Publication"`). This is sanctioned under Rule #1 — Rule #1 bans `WebSearch`/`WebFetch`, not PubMed MCP.

   **Default: do NOT ingest.** A retracted article, retraction notice, erratum-only page, or bare PubMed/publisher listing page must not become a normal knowledge page — it propagates discredited claims and violates the living-document/critical-appraisal principle. Delete retraction/erratum notice PDFs (they are not ingestable papers).

   **Exception — when the retraction *is* the knowledge.** If the retracted paper was the *only* evidence on a topic the wiki must be able to answer about, a full page may be kept. The point is inverted: you are not keeping evidence, you are recording an **evidence vacuum** — *"the only study on X was retracted, therefore no valid evidence exists"* — which is a stronger and more citable answer than silence, and is exactly what Rule #4 wants sayable. Two pages qualify today: [[wiki/professional-wellbeing/panagioti-2018-retracted-physician-burnout-patient-safety]] and [[wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift]].

   **Required structure for a kept retracted page** (enforced by `scripts/retraction-audit.py`, a daily signal):

   | Requirement | Why |
   |---|---|
   | `retraction_status: RETRACTED` in frontmatter | The only machine-readable hook. `grep -i retracted` is unusable — it hits 교정과 "canine retraction"(견인). |
   | `title:` starts with `[RETRACTED]`, `tags:` include `RETRACTED` | Title and tags travel with every search hit. |
   | `## ⚠️ RETRACTION NOTICE` section | What a human hits on opening the page. |
   | **Data section headings carry the warning** — `## Results (Original — Now Withdrawn, Do Not Cite)`, `## Methodology (Original — Now Withdrawn)`, etc. | ★ **The load-bearing rule.** QMD retrieves *chunks*: a top-of-page callout does NOT travel with a `## Results` chunk, so a bare heading lets withdrawn numbers reach an answer as clean evidence. The heading is the only warning that survives chunking. |
   | Three sections: `## Why This Page Exists (Despite Retraction)`, `## What We Can NOT Use From This Paper`, `## What This Paper Does Tell Us (Methodologically)` | Turns the vacuum into an explicit, citable conclusion. |
   | **Zero `relations:` typed edges, in either direction** | The typed graph is what overview synthesis warm-assembles from (see `relations:` below). A retracted paper must not contribute a live relationship — and no page may point *at* it. Prose `## Related Papers` links stay, for human navigation. |

   Keep `evidence_level:` as the paper's original study design — that axis is *what the study was*, and `retraction_status:` is the separate axis for *whether it still counts*. Same two-axis logic as `evidence_level:` vs the session `[확인]`/`[미검증]` tags.

## Step 1 — Copy PDF to `papers/` and extract text

```bash
cp /path/to/paper.pdf /Users/oracleneo/llm-wiki/papers/{stem}.pdf

python3 -c "
import pypdf, sys
reader = pypdf.PdfReader(sys.argv[1])
text = ''
for page in reader.pages[:15]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print(text[:12000])
" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```

### Step 1-T — PubMed-text 분기 (PDF 없는 OA/전문)

PubMed MCP `get_full_text_article`로 전문을 받은 경우 PDF가 없다. PDF 복사 대신 받은 전문을 `papers/{stem}.txt`로 저장하고, 그 텍스트로 Step 2·3을 작성한다. PMC 전문은 JATS 기반이라 pypdf 추출본보다 깨끗한 경우가 많다.

sources/·wiki/ frontmatter는 Step 2·3과 동일하되 아티팩트 필드만 교체:

```yaml
source_collection: pubmed-text   # external(PDF) 대신
full_text: true                  # 페이월로 초록만 받았으면 false
pmid: "xxxxxxxx"
pmcid: "PMCxxxxxxx"             # 없으면 생략
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxxx/
text_path: /Users/oracleneo/llm-wiki/papers/{stem}.txt
text_filename: {stem}.txt
# pdf_path / pdf_filename 생략
```

- `full_text: false`(초록만): Summary·Results를 초록 수준으로만 채우고 본문에 `abstract-only — full text not retrieved` 명시. `evidence_level`은 study type 그대로.
- dedup(Step 0)은 `dedup-check.py` 그대로 (PDF가 없으니 `--doi` 또는 `--title`로 호출; PMCID grep 병행). 1:1 매칭·linter는 `.txt`를 PDF와 동등한 아티팩트로 인식한다 (`scripts/lint.py`, `wiki/_lint/lint.py`에 `pubmed-text` 분기 반영, 2026-06-17).

### Step 1-D — DeepSeek v2 dump 분기 (전처리본이 루트에 드롭된 경우)

루트에 `===FILE: sources/...===` 구분자를 가진 `.md`가 있으면 **PDF를 직접 읽지 마라** — DeepSeek이 두 페이지를 이미 완성해 놓은 것이다. `scripts/deepseek-split.py`가 파싱·검증·`__CATEGORY__` 치환·저장을 대신한다:

```bash
python3 scripts/deepseek-split.py <dump.md>                    # 리포트: 검증 + Step0 DOI 중복 + REF_DOIS 보유 매칭
python3 scripts/deepseek-split.py <dump.md> --category <cat> --pdf <원본.pdf>   # 두 파일 쓰기 + papers/ 복사 + PDF 팩트체크
```

Claude가 이어서 하는 것만 남는다: `## Why Ingested`, `## Related Papers`, `relations:`, supersession, Step 4–5. 스크립트는 지어낸 `[[wikilink]]`·stem 불일치·필수 필드 누락에서 **exit 1로 중단**한다 (경고 아님). 프롬프트·역할분담 전문은 `deepseek-ingest-prompt 1.md`. 구분자 없는 구형(v1, `---METADATA---`) dump는 exit 2 — 그건 종전대로 Claude가 조립한다.

**PDF 팩트체크 (2026-08-04 사고 이후 필수)** — 위 구조 검증은 dump의 *형식*만 본다, DeepSeek이 논문을 *제대로 읽었는지*는 안 본다. `maurice-szamburski-2025-intravenous-nsaids-perioperative-pain-narrative-review` 건에서 구조 검증은 전부 통과했는데도 DeepSeek은 DOI 숫자 두 자리를 바꿔치기했고(`pharmacy13010108` vs 실제 `pharmacy13010018`) 제목도 verbatim 대신 의역해서 냈다 — 둘 다 아무도 PDF 원문을 안 읽어서 놓쳤다. `--pdf`를 넘기면 이제 자동으로:

- **DOI**: PDF 첫 5페이지에 (공백 무시) 문자 그대로 없으면 **exit 1로 중단**. DOI는 Step0 중복탐지의 유일한 키라서 오탈자가 나면 "clean — no existing page"가 그대로 오탐 통과한다 — hard block 외엔 답이 없다.
- **제목**: PDF 1페이지에 (공백·구두점 무시, 이어붙인 문자열로) 없으면 **WARNING만 찍고 계속 진행** (hard block 아님 — PDF 추출 시 줄바꿈·하이픈 노이즈가 있어 완전 일치를 강제하면 오탐이 잦다). WARNING이 뜨면 pypdf로 1페이지를 직접 읽어 제목·저자를 verbatim으로 대조하고 고친 뒤 커밋할 것.

단어 단위 overlap 체크는 시도했다가 버렸다 — "perioperative NSAIDs management" 같은 도메인 단어는 의역된 가짜 제목이라도 논문 본문 어딘가엔 다 나오기 때문에 걸러지지 않았다. 공백 제거 후 통짜 substring 매칭(DOI 체크와 같은 트릭)만 실제로 의역을 잡아냈다.

### Step 1-A — Abstract-only PDF 분기 (페이월 랜딩/초록 저장본)

가끔 받은 PDF가 전문이 아니라 **출판사 랜딩/초록 저장 페이지**(paywall, 흔히 1–2쪽, 본문 없음)다 — Step 1-T의 PMC-빈본문과 결과는 같지만 **아티팩트가 PDF**라 `source_collection: pubmed-text`를 쓸 수 없다. 이때:

- `source_collection: external` 유지(아티팩트는 PDF), `pdf_path`/`pdf_filename` 정상 기재.
- **frontmatter에 `full_text: false` 필드를 추가**하고, 본문 맨 위(Three-line Summary 위)에 `abstract-only — publisher landing/abstract page, full text not retrieved` 한 줄 명시. (초록만으로 Summary·Results 채움, `evidence_level`은 study type 그대로.)
  - 과거엔 이걸 frontmatter flag 없이 본문 caveat로만 처리해 일관성이 없었다(de-elio-2023 vs quesada-garcia-2012). 앞으로는 **frontmatter `full_text: false` + 본문 한 줄** 둘 다 박는다.
- DOI 없으면 위 Step 0 no-DOI fallback 병행.
- 로그: `python3 scripts/log-deviation.py <stem> abstract-only "publisher landing page, built from abstract"` (PMC 빈본문은 `empty-pmc-text`로 구분).

## Step 2 — Write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: [category-folder]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## Why Ingested
## Three-line Summary
## 세줄요약
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

**`## Why Ingested` is MANDATORY for sources ingested on/after 2026-05-27** (enforced by `scripts/ingest-rationale-lint.py`). Pre-cutoff sources are grandfathered (no backfill).

Required content of the section:
- 1–2 sentences explaining *why* this paper was ingested now (gap, conflict, new evidence, requested by user, related to current clinical case, etc.)
- At least one `[[wiki/category/stem]]` wikilink to an existing wiki page that this paper reinforces, contradicts, or extends.

**Wikilink lookup MUST use `qmd query` (MCP tool) — never `grep`, `find`, or `ls` over wiki/.** At this repo's scale a filesystem scan is slow and misses cross-category matches; qmd hybrid search returns relevant candidates in under 1 second. (Live page/paper counts are computed at deploy time into `interactives/wiki-stats-live.html` — never hard-coded here, so this file can't go stale.)

**Soft reminder (non-blocking, not lint-enforced):** before writing `## Why Ingested`, skim the paper's Methods against [[overviews/evidence-appraisal-toolkit]]'s study-type reading-order table (RCT: randomization/allocation concealment/ITT/CONSORT; observational: confounder adjustment/clustering/immortal-time bias; SR+MA: I²/funnel plot/pre-specified subgroups). This is a habit prompt, not a required field — it exists to catch inflated effect sizes or unchecked assumptions before they get cited elsewhere in the wiki.

Example:
```
## Why Ingested

기존 [[implants/isq/andersson-2019-rfa-factors-5year-neoss-survival]]의 ISQ ≥65 threshold가 5Y-PSZ implant에 적용되는지 의문. 본 RCT (Konuklu 2026)는 5개 osteotomy protocol을 직접 비교해 임계값 보강 근거로 활용.
```

Rationale: a 2-minute cost at ingest turns later overview synthesis from a cold start into a warm assembly. See `agenda/2026-05-26_synthesis-enforcement-setup.md` for the design.

## Step 3 — Write `wiki/{category}/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
date: YYYY-MM-DD       # publication date; fall back to ingest date (YYYY-MM-DD) when unknown
doi: DOI
source: {stem}.md
category: [category-folder]
evidence_level: sr+ma  # study-type label; see vocabulary below (renamed from `confidence:` 2026-07-15)
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## Three-line Summary
(Line 1: study type, n, context — what was studied)
(Line 2: primary result / key finding with numbers)
(Line 3: clinical implication or key limitation)

## 세줄요약
(줄1: 연구유형·n·맥락 — 연구 대상/설계)
(줄2: 핵심 결과/수치)
(줄3: 임상적 의미 또는 핵심 한계)

> **Three-line Summary 규칙 (SSOT — moved here from `CLAUDE.md` 2026-07-17).** 모든 wiki 페이지 **및** source 페이지는 이 이중언어 세줄요약을 **두 개의 분리된 섹션**으로, 이 순서대로 싣는다: `## Three-line Summary`(영어) 바로 뒤에 `## 세줄요약`(한국어). wiki 페이지에서는 이 쌍이 `## Summary` 바로 위, source 페이지에서는 `## 1. Document Information` 바로 위에 온다. 신규 페이지는 두 언어 모두 필수. 각 섹션은 정확히 3줄(줄 사이 빈 줄) — 줄1: 연구유형·n·맥락 / 줄2: 수치를 포함한 1차 결과 / 줄3: 임상적 함의 또는 핵심 한계.

## Summary
## Key Contributions
## Methodology
## Results
## Related Papers
- [[category/page]] — relationship
```

### `evidence_level:` vocabulary

> **Rename note (2026-07-15):** 이 필드는 이전 `confidence:`였다. userPreferences v4의 세션 확신도 2태그([확인]/[미검증], = *검증 상태* 축)와 개념 충돌을 없애기 위해 study-type = *근거 수준* 축임을 명시하는 `evidence_level:`로 리네이밍. Forward-only — 기존 페이지의 `confidence:`는 grandfather. 감사·빌드 스크립트(`scripts/lint.py`, `wiki/_lint/lint.py`, `supersession-audit.py`, `build-wiki-stats.py`, `build-weekly-digest.py`, `build-contradiction-radar.py`, `content-lint.py`)는 **두 키를 모두 인식**하며 `evidence_level`을 우선한다 (2026-07-15 패치 완료). 일괄 치환 마이그레이션(2885개 기존 페이지 `confidence:` → `evidence_level:`)은 별도 agenda로. 두 축을 구분: `evidence_level:`은 논문의 연구설계 강도, 세션 [확인]/[미검증]은 이번 세션에서 도구로 출처를 확인했는지.

Pick the **single best label** for the study type. Ordered roughly from highest to lowest evidence weight:

| Value | Applies to |
|---|---|
| `sr+ma` | Systematic review + meta-analysis (incl. umbrella review) |
| `sr` | Systematic review without meta-analysis |
| `rct` | Randomized controlled trial |
| `prospective` | Prospective cohort / prospective case series |
| `retrospective` | Retrospective cohort / chart review |
| `cross-sectional` | Cross-sectional study, survey |
| `case-report` | Case report or small case series (n < 10) |
| `in-vivo` | In vivo clinical/animal experimental study not covered above |
| `animal` | Animal-only experimental study (dog, rat, etc.) |
| `in-vitro` | Bench / laboratory study |
| `narrative-review` | Narrative review, perspective, expert commentary |
| `consensus` | Consensus statement / position paper |
| `synthesis` | Multi-paper synthesis page (wiki overviews); not external study type |

**Non-research document labels** (not on the evidence ladder — administrative/legal/engineering primary sources the wiki also holds; these are why lint accepts values beyond the 13 study types above):

| Value | Applies to |
|---|---|
| `regulation` | Korean health-insurance regulation — MOHW notice / decree / amendment (고시·훈령·개정) |
| `official-qa` | Official Q&A from MOHW / HIRA (보건복지부·심평원 유권해석) |
| `manual` | Practical guidebook / 실무편람 / 청구길라잡이 |
| `patent` | Patent disclosure (공개/등록특허공보) — primary engineering document |

**This table (study types + non-research labels) is the single source of truth for the `evidence_level:` vocabulary.** `references/evidence-ladder.md` holds the supersession *judgment* rules (which grade beats which) and the optional `rob:` field; it defers to this list for the value set. `scripts/lint.py` and `wiki/_lint/lint.py` `VALID_CONFIDENCE`/`CONFIDENCE_VOCAB` sets must match this table.

### `date:` field

- Publication date in `YYYY-MM-DD` format when known (use journal publication or e-pub date).
- `YYYY-01-01` when only year is known.
- If neither is recoverable from the paper, fall back to ingestion date (`YYYY-MM-DD` of when added to wiki).

### `superseded_by:` — living-document supersession (optional field)

The wiki is a living document: a paper page is not an ingest-time snapshot, it gets updated by later evidence. When a newer paper we hold **overturns the clinical bottom line** of an older page we hold, mark the *older* page. This converts the manual prose-update habit into a machine-checkable signal (`scripts/supersession-audit.py`).

**This is a clinical judgment, not a mechanical year comparison.** Newer ≠ superior — a 2026 narrative-review does NOT supersede a 2022 SR+MA. Set the field only when the newer page genuinely beats the older one on evidence weight or currency, and only between pages we actually hold.

**Forward-only trigger (no backfill needed).** At ingest of a new page, ask: *"does this overturn an existing page's bottom line?"* If yes, edit the *older* page — add the field + banner. Pre-existing pages are never bulk-scanned (same grandfather logic as `## Why Ingested`).

Two frontmatter fields on the **superseded (older)** page:

```yaml
superseded_by: tisci-2026-isq-it-mbl-survival-sr-ma   # newer stem(s); comma-separated if >1; must exist in wiki/
superseded_scope: full                                # full | partial
```

- `full` — the older page's conclusion is replaced; prefer the newer page for all current decisions.
- `partial` — only part of the page is outdated, or the page retains standalone value (e.g. first-of-kind synthesis, historical anchor). Use this rather than overstating `full`.

Plus a banner callout at the **top of the body** (right after frontmatter, before `## Three-line Summary` / `## 세줄요약`). Obsidian and Quartz both render `[!warning]`/`[!note]` callouts natively — no build change:

```markdown
> [!warning] Superseded (full) → [[tisci-2026-isq-it-mbl-survival-sr-ma]]
> 48-study SR+MA (r=0.44, p<0.001) overturns this 12-study NS result. (set 2026-05-31)
```

For `partial`, use `> [!note] Partially superseded → [[newer-stem]]` and state what the page still offers.

**`supersession_chain: intentional` — when a mid-chain pointer is correct (optional third field).**

`supersession-audit.py` also checks transitivity: if A → B and B → C, it reports A's pointer as stale and suggests repointing to the chain tail C. **That rule is only valid for `full` supersession.** `partial` supersession happens *per axis*, and axes do not compose: if C took over a different axis of B than the one B took over from A, then A's pointer belongs on B and moving it to C loses information.

Set this field on A when you have made that judgment, and **state the reason in A's banner** — the field alone tells the next reader nothing about why:

```yaml
superseded_by: avila-ortiz-2019-alveolar-ridge-preservation-interventions
superseded_scope: partial
supersession_chain: intentional    # 2019→canullo-2021 is a different axis; do not repoint
```

The declaration is not a mute: the audit moves the row out of `TRANSITIVITY chain stale` into a separate counted `chain intentional (선언)` line and still prints the chain tail, so the judgment stays visible and re-reviewable. Worked example: [[bone-regeneration/ridge-preservation/avila-ortiz-2014-alveolar-ridge-preservation-systematic-review]] (2026-08-15).

**Decay is computed, never stored.** Do NOT add a decay/staleness field — a stored decay value rots (the same reason `overview-thesis-staleness.py` exists). `supersession-audit.py` computes it each run: high-evidence pages (`sr+ma`/`sr`/`rct`) older than 5y and not superseded are flagged as "verify still current" candidates.

Design: `agenda/2026-05-31_supersession-decay-setup.md`.

### `relations:` — typed entity edges (optional field)

`[[wikilinks]]` encode *that* two pages relate; they don't encode *how*. The `## Why Ingested` section already states the relationship in prose ("X를 보강", "Y로 확장", "Z와 대비"). Lifting that into a structured frontmatter block turns overview synthesis from a cold start (re-read every page to infer relationships) into a warm assembly (the typed graph is already there). `superseded_by` is intentionally NOT part of this — it has its own audited field and banner.

To find `target` stems, use `qmd query` — do NOT scan wiki/ with grep/find. Example: `qmd query "PDRN bone regeneration"` returns the top candidate stems in under 1 second.

Optional block on the **page you're writing**, pointing out to the pages it relates to. Direction is not publication-date-ordered — see the note below.

```yaml
relations:
  - type: extends
    target: manfredini-2023-polydeoxyribonucleotides-pre-clinical-findings-bone-healing
  - type: reinforces
    target: ku-2025-polydeoxyribonucleotide-pdrn-dentistry-narrative-review
```

Relation vocabulary (5 types; pick the single best per edge):

| `type` | meaning | Why-Ingested 표현 예 |
|---|---|---|
| `extends` | builds on / expands target's scope or depth | "확장", "deep-dive", "적응증 확장" |
| `reinforces` | independently confirms / strengthens target | "보강", "재확인", "일관", "짝을 이룸" |
| `contradicts` | findings conflict with target | "반박", "상충", "대비되는 결과" |
| `refines` | narrows / qualifies target's conclusion | "한정 시나리오 강화", "조건부", "scope 제한" |
| `applies-to` | clinical/methodological application of target | "프로토콜 적용", "한국 임상 contextualization" |

- `target` must be an existing wiki stem (validated by `scripts/relations-audit.py`).
- Forward-only / grandfather: structure relations for **new** pages at ingest; old pages are not bulk-scanned. The audit reports a machine-readable typed-edge export (`logs/{date}_relations-graph.json`) for Quartz/custom rendering — Obsidian's graph view can't distinguish edge types, so the JSON export is where typed-edge value is harvested.

**Direction note (resolved 2026-07-19, after going back and forth twice the same day — settled here so it doesn't get re-litigated).** `type:` (extends/reinforces/refines/contradicts/applies-to) is chosen from the **content relationship between the two papers' findings** — does A's result extend/independently-confirm/narrow/conflict-with/clinically-apply B's claim. **Publication date order is NOT a requirement.** A page may `extends`/`reinforces` a target regardless of which was published first; the field encodes what the two papers' evidence does *relative to each other*, not a citation-priority claim about who could have read whom.

An earlier draft of this note required strict publication-date ordering (target must predate the citing page). That was reverted the same day: checking it against the *existing* graph found **815 of 2,432 typed edges (33.5%) violate strict date order — including one of the two edges in this very section's own canonical example above** (`lee-2024-... extends→ manfredini-2023` is forward, but the same page's `reinforces→ ku-2025-...` is backwards). A rule the field's own reference example fails was never actually the wiki's working convention — it just hadn't been checked before. Chronology-based edge validation was tried and dropped; do not re-add it to `scripts/relations-audit.py` without new evidence this is actually wanted.

The only hard requirement remains mechanical: `target` must already exist as a wiki stem — **sibling pages in the same parallel-ingest batch are mutually invisible until Phase 2 lands them** (paper A and paper B fanned out to two subagents in the same batch can't add typed edges to each other; use prose `## Related Papers` for those, a *later* ingest may add the edge once both exist).

**`reinforces` means *independently* confirms — so a derived document can never `reinforces` its own source material.** An overview built from paper X cannot independently confirm X; that is circular. Same for a consensus report and the review it commissioned, and for a paper pointing at an overview assembled *from* that paper (direction reversed as well). `scripts/relations-audit.py` reports these as a `CIRCULAR reinforces` signal, separate from its structural issue count.

When the audit flags one, read both pages and pick:
- the overview genuinely **narrows** a constituent's conclusion by reading it against the others → real `refines` (an overview does have a finding of its own: the cross-paper reading). Not every overview→constituent edge is circular — only `reinforces` is.
- the overview merely **restates** the constituent → drop the edge. No membership is lost: measured 227/227 of such targets are already body `[[wikilinks]]`, and body wikilinks are what `synthesis-backlog.py` reads (99.7% of papers are overview-linked that way).

**Do not read `reinforces` as the default for a strong target.** Measured 2026-07-17 on a 30-edge random sample judged by reading both pages: only 47% were correctly typed — 30% should have been `extends`/`applies-to`/`refines` (a reflex of typing `reinforces` whenever the target is an SR/MA), and 23% fit no type at all. Pick the type from what the two papers actually did, not from the target's evidence grade.

**There is no 6th type, and this was tested — do not re-propose one without new evidence.** A ~13% minority of pairs are genuinely "orthogonal axes of the same decision" (e.g. arginine-dentifrice efficacy vs free-sugar intake threshold — same caries decision, non-overlapping measurement, neither extends the other). A `complements` type was evaluated 2026-07-17 and rejected on a natural experiment: of 20 randomly sampled pairs where an author had written "complementary" in prose, only **2 (10%)** were actually orthogonal — the rest were `reinforces`, `extends`, or nothing at all (one pair's only real link was "ingested in the same batch"). The relation is real but the label would be misapplied 9 times in 10. Leave those in prose `## Related Papers`.

## Step 4 — Update `index.md`

Add a one-line entry under the correct category.

## Step 5 — Refresh search index (qmd)

A new page is invisible to semantic search until qmd re-indexes and embeds it. Run after the wiki/sources files are written:

```bash
export PATH="/opt/homebrew/bin:$PATH"   # brew node(v25+) 강제 — 구 node v18이 앞서면 ABI 불일치로 qmd 깨짐
cd /Users/oracleneo/llm-wiki
qmd update   # 파일시스템 재스캔 (신규/변경/삭제 반영)
qmd embed    # 신규 문서만 임베딩 (incremental — 1~2편이면 수 초). 전체 재임베딩(-f)은 ~2.5h이므로 금지
```

**주의 — `qmd embed`는 백로그가 크면 미완료로 끝난다.** 대량 백로그에서 daemon 세션이 중간에 만료되어 `qmd embed`가 남은 문서를 임베딩하지 않고 exit 0으로 끝난다 (exit-0 ≠ 완료). 유일하게 믿을 수 있는 완료 신호는 `"All content hashes already have embeddings"` 메시지다. 1~2편만 추가한 일반 ingest라면 위 단일 실행으로 충분하다.

### 고아 벡터 청소 — 자동화됨, ingest 때 손대지 마라

`qmd update`/`qmd embed`는 고아 벡터를 **절대 치우지 않는다.** 페이지를 수정하면 해시가 바뀌어 새 벡터가 생기는데 옛 벡터는 그대로 남고, 이것이 검색을 조용히 망가뜨린다 (아래 *왜 무해하지 않은가*). 이 청소는 **주간 launchd 잡이 알아서 한다 — ingest 절차에 넣지 마라**:

```
com.llmwiki.qmd-cleanup   매주 월 10:00   .claude/scripts/qmd-cleanup.sh
로그: .claude/scripts/qmd-cleanup.log
```

수동으로 지금 당장 돌려야 한다면 (대량 재작성 직후 등):

```bash
qmd cleanup    # 데몬 켠 채로 안전. 산 벡터는 안 건드림 → 재임베딩 불필요
```

**왜 무해하지 않은가.** qmd 벡터 검색은 두 단계다 (`dist/store.js` `searchVec` — sqlite-vec가 JOIN과 같이 쓰면 멈추는 버그 우회): ① 전체 벡터에서 후보 `limit × 3`개를 kNN으로 뽑고 ② 그 다음 `active = 1`로 죽은 걸 걸러낸다. 3배수 여유는 인덱스가 대부분 살아있다는 전제인데, 고아가 쌓이면 시체가 그 여유를 먹어 산 문서가 밀려난다. **에러가 안 나므로 감사로는 안 잡힌다** — 근거를 조용히 놓치는, 위키에서 가장 나쁜 실패 방식이다.

2026-07-17 실측 (첫 청소 전, 인덱스 생성 이래 한 번도 안 돌았음): 고아 **66.5%** (40,513/60,960), 검색 후보의 **70%가 시체**, 20개 요청 쿼리의 **절반이 개수 미달**, 최악은 후보 60개 중 **생존 2개**. 청소 후 후보 죽음률 0%, 미달 쿼리 0/10.

**하지 말 것**: `qmd cleanup`을 `--finish`나 ingest 루프에 넣지 마라. VACUUM이라 무겁고, 고아는 몇 달에 걸쳐 쌓이는 종류의 문제라 주간이면 충분하다. 그리고 전체 재임베딩(`qmd embed -f`)으로 "청소"하려 들지 마라 — ~2.5h이 걸리고 `qmd cleanup`이 수 초에 하는 일이다.

### 백로그 확인 — `qmd update`가 출력하는 숫자를 믿지 마라

`qmd update` 끝에 나오는 `Run 'qmd embed' to update embeddings (N unique hashes need vectors)`의 **N은 남은 작업량이 아니라 전체 인덱스 파일 수다** (실측 2026-07-16: update는 "5660", 실제 백로그는 713). 진짜 백로그는 `qmd status`로 본다:

```bash
qmd status | grep Pending      # ← 이것만이 진짜 백로그
```

**단위 주의**: `Pending:`은 **문서** 수, `Vectors:`는 **청크** 수다. 실측 환산 ≈ 문서당 3.2청크, 패스당 ~250청크 → **필요 패스 ≈ (Pending × 3.2) ÷ 250**. (713문서 ≈ 2,300청크 ≈ 10패스 ≈ 하룻밤)

### 드레인 — 규모에 따라 둘 중 하나

**(A) 무인·대량 — launchd (권장).** 세션·터미널과 무관하게 돌고, 세션 만료마다 자동 재실행하다 done 마커에서 스스로 멈춘다:

```bash
launchctl kickstart gui/$(id -u)/com.llmwiki.embed-until-done
tail -f logs/embed-until-done.log        # 관찰 (단 패스가 끝나야 한 번에 출력됨 — 아래 참고)
```

> ⚠️ **launchd는 다음번에 자동으로 돌지 않는다.** plist가 `KeepAlive={SuccessfulExit:false}`라, 드레인이 done 마커로 exit 0을 내는 순간 launchd는 재실행을 멈추고 잠든다. 다음 ingest로 생긴 백로그는 **자동으로 안 빠진다** — 위 `kickstart`로 매번 깨워야 한다. (재부팅·로그인 시에는 `RunAtLoad`로 한 번 자동 실행.) 미설치라면 `.claude/scripts/com.llmwiki.embed-until-done.plist`를 `~/Library/LaunchAgents/`로 복사 후 `launchctl load -w`.

**(B) 소량·세션 내 — 스크립트 직접.** Claude Code / 터미널 세션이 끝나면 **같이 죽는다**:

```bash
bash scripts/embed-until-done.sh      # done 마커 나올 때까지 반복 (내부에서 qmd update도 실행)
bash scripts/embed-until-done.sh &    # 백그라운드
bash scripts/embed-until-done.sh -c wiki   # 컬렉션 한정 (인자는 qmd embed로 통과)
```

`scripts/embed-until-done.sh`는 `qmd update` → `qmd embed`를 done 마커까지 반복하며 `MAX_PASSES=40` 상한이 있다. 단 `qmd update`는 루프 **바깥**이라 맨 처음 1회만 실행된다.

### 금지 · 진단

| 금지 | 이유 |
|---|---|
| `qmd embed` **동시 2개** | 같은 인덱스에서 교착 → 진행 0. 시작 전 `pgrep -f "qmd.js embed"` 확인 |
| `qmd embed -f` | 전체 재임베딩 ~2.5h |
| `exit 0`을 완료로 간주 | done 마커만이 완료 신호 |
| "session expired" 보고 daemon 재시작 | 그건 정상적인 패스별 타임아웃. daemon 누수는 *질의가 300초+* 라는 별도 signature가 있을 때만 |

**살아있는지 확인**: `Pending`은 SQLite 체크포인트 때만 갱신돼 몇 분씩 멈춰 보인다. 진짜 생존 지표는 WAL 수정 시각과 워커 누적 CPU다:

```bash
ls -l ~/.cache/qmd/index.sqlite-wal                  # 시각이 최근이면 정상
ps -o pid,etime,time,state -p $(pgrep -f "qmd.js embed" | head -1)   # TIME이 늘면 연산 중
```

**로그가 멈춰 보이는 이유**: 스크립트가 `out="$(qmd embed ...)"`로 출력을 변수에 담았다가 패스 종료 후 한 번에 찍는다. `tail -f`는 ~30분간 얼어붙은 듯 보이다 패스 전체를 쏟아낸다 — 고장이 아니다. 실시간 진행은 위 `qmd status` / WAL로 본다.

The MCP daemon picks up new vectors automatically — no restart needed.

---

## PDF Management Rules

- **Always copy, never symlink.** `cp` from Downloads or external into `papers/`.
- `pdf_path` always points inside `/Users/oracleneo/llm-wiki/papers/`. Never use `~/Downloads/`.
- `pdf_filename` must match `basename(pdf_path)`.
- **1:1 matching enforced.** Every PDF in `papers/` must have a matching `sources/{stem}.md`. After any ingest or rename operation, run:
  ```python
  pdfs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('papers/') if f.endswith('.pdf')]}
  srcs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('sources/') if f.endswith('.md')]}
  orphan_pdfs = pdfs - srcs   # → delete these
  orphan_srcs = srcs - pdfs   # → warn (missing PDF)
  ```
  Delete all `orphan_pdfs` immediately. Pre-rename originals and duplicate `(1)` copies count as orphans and must be deleted.

## File Naming Convention

All three tiers share the same stem:

```
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces → `-`
- Year is 4 digits
- Example: `jung-2023-immediate-implant-placement-sinus.pdf`
