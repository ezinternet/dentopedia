# OPERATIONS — Routing & Cross-link Rules

> Split out of `CLAUDE.md` on 2026-07-17 to keep that file lean (agent rules only, loaded every session). Same pattern as `INGEST.md`. **Open this file when creating any artifact in `agenda/`, `slides/`, `interactives/`, `peer-review/`, or `note-meeting/`.** Answering a question does not require it.

KNOWLEDGE (papers/sources/wiki) is the substrate; OPERATIONS is where it gets converted into outputs (slides, calculators, review reports, meeting decisions). Without these rules every output drifts away from its source wiki page.

Human-facing companion: `SOP.md` §2-bis (폴더 역할 요약).

---

## 1. Routing — 어디에 만드는가

When creating any new artifact, ask in order:

1. **재사용되는 지식인가?** → `wiki/{category}/` (단일 paper) or `wiki/overviews/` (cross-paper synthesis)
2. **시간·이벤트 기록인가?** → `note-meeting/`
3. **외부 deliverable인가? (슬라이드·인터랙티브·peer review)** → 해당 OPERATIONS 폴더
4. **외부 deliverable의 작업 명세인가?** → `agenda/`

**Hard rule**: `slides/`, `interactives/`, `peer-review/` 산출물은 반드시 `agenda/` 파일이 선행되어야 한다. agenda 없는 산출물은 출처·done 기준 추적이 끊긴다.

## 2. File Naming — OPERATIONS

```
agenda/YYYY-MM-DD_<kebab-case-topic>.md
interactives/YYYY-MM-DD_<kebab-case-topic>.html
slides/YYYY-MM-DD_<event-or-audience>_<topic>.md
peer-review/YYYY-MM_<journal-code>_<topic>.md
note-meeting/YYYY-MM-DD_<meeting-type>.md
```

날짜 prefix는 정렬·검색을 위함. `_template.md` 같은 시스템 파일은 날짜 prefix 면제.

## 3. Frontmatter Cross-link — OPERATIONS 파일 전 필수

```yaml
---
title: "..."
type: agenda | interactive | slides | peer-review | meeting
date: YYYY-MM-DD
status: draft | in-progress | review | done | archived
# 아래 3개 중 최소 하나는 비어있지 않아야 함
source_wiki:                              # 이 산출물의 근거가 된 wiki 페이지들
  - wiki/<category>/<stem>.md
agenda: agenda/<date>_<topic>.md          # slides/interactives/peer-review 필수
output_wiki:                              # 이 산출물이 갱신·생성한 wiki 페이지 (meeting에서 자주 발생)
  - wiki/<category>/<stem>.md
---
```

`source_wiki` · `agenda` · `output_wiki` 세 필드가 모두 비어있는 OPERATIONS 파일은 **orphan**으로 간주하고 lint에서 경고한다 (`scripts/operations-lint.py`).

## 4. agenda Workflow

새 작업은 agenda 파일 1개로 시작:

```bash
cp agenda/_template.md agenda/$(date +%Y-%m-%d)_<topic>.md
```

agenda는 Goal·Input·Output·Done이 박힌 단일 명세서. 진행되며 status 갱신 (`draft` → `in-progress` → `review` → `done` → `archived`).

agenda에서 파생된 산출물(slides·interactive·overview)은 자신의 frontmatter에 `agenda:` 백링크를, 그리고 agenda 파일의 `# Output` 섹션에 산출물 경로를 양쪽으로 박는다.

## 5. note-meeting Workflow

미팅 1회 = 파일 1개. 결정 사항(decisions)이 wiki SOP나 임상 프로토콜에 반영되어야 하는 경우:

- meeting note frontmatter의 `output_wiki:` 에 갱신될 wiki 페이지 경로
- followup이 필요하면 `followup_agenda:` 에 신설할 agenda 파일 경로 (그리고 실제로 agenda 신설)

미팅 → agenda → 산출물의 chain이 끊기면 미팅은 메모로만 남고 클리닉 SOP에 반영이 안 된다.

---

## 6. Interactive tools — deploy-time freshness (two classes)

`interactives/`의 chairside 계산기·결정트리·시뮬레이터는 freshness 메커니즘이 다른 두 부류로 갈린다.

- **메타·통계 도구 (Class A)** — numbers ARE repo state (paper/overview/category counts, ingest timeline, 발행연도 histogram). `scripts/build-wiki-stats.py` regenerates **`interactives/wiki-stats-live.html`** on every deploy from live repo state + git history (reuses the v4 render engine; only the JS DATA blocks + header scalars are injected). It is the single always-current dashboard. The date-stamped lineage (`wiki-evolution` v1~v4, `wiki-growth-curve`) stays **frozen as the evolution archive** — never regenerated (mutating a dated snapshot would make its filename lie). Never hand-edit `wiki-stats-live.html` (overwritten). git cumulative needs full history → deploy uses `fetch-depth: 0`.
- **임상 결정 도구 (Class B)** — numbers are clinical thresholds an LLM extracted from specific papers (ISQ ≥65, r=0.44, doses, risk %). A deploy script **cannot** safely re-extract these (would hallucinate/corrupt clinical values → violates Rule #1), so they are **not auto-rewritten**. Instead `scripts/interactive-staleness.py` emits a signal when a tool's `source_wiki:` page is newer than the tool (STALE → re-author with LLM) or a source path vanished (BROKEN). Re-authoring stays a human/LLM-in-the-loop step. This matches the wiki's signal-not-gate philosophy.

Deploy order (in `deploy-pages.yml`): `build-wiki-stats.py` → `build-interactives-index.py` (so the live tool is indexed) → `interactive-staleness.py` (non-blocking) → copy `interactives/` into the site.

**색인 카테고리 — `category:`는 인덱스 전용 taxonomy다.** `interactives/index.html`은 각 도구 frontmatter의 `category:` 값으로 섹션을 나눈다. 이 키 집합은 `scripts/build-interactives-index.py`의 `CATEGORIES` 리스트가 단일 출처이며 — **`wiki/_meta/categories.md`(논문 라우팅 카테고리)와는 다른 축이다.** 새 도구를 쓸 때 wiki 카테고리 값(`bone-regeneration`, `endodontics`, `tmj` …)을 그대로 적으면 안 되고, 스크립트의 `CATEGORIES` 키 중 하나를 쓴다. 잘못된/누락된 값은 '기타 · 미분류' 버킷으로 떨어지고 빌드가 stderr에 경고한다. 흔한 wiki 값은 같은 스크립트의 `ALIASES`가 흡수하지만 안전망일 뿐 — 정규 키를 직접 쓰는 것이 원칙.

*Why*: 2026-08-27 실측 — 84개 도구 중 30개(36%)가 wiki taxonomy 값을 달고 '기타·미분류' 한 덩어리에 몰려 있었다. 빌드는 성공하고 도구도 다 보였기 때문에 어떤 감사에도 안 걸렸고, 배포 사이트에서 **분류만 조용히 무너진** 상태였다.

## 7. Interactive HTML 디자인 규칙 (항상 적용)

**라이트 고정 — OS 다크 모드 무시.** 임상 인터랙티브는 환경에 관계없이 항상 라이트로 렌더링한다.

```css
/* ✅ 올바른 구조 — :root 라이트 토큰만, 다크 블록 없음 */
:root {
  --bg: #F2F3EF;
  --surface: #FFFFFF;
  --text: #1A2030;
  /* … 나머지 라이트 토큰 */
}

/* ❌ 금지 — 이 블록들을 절대 넣지 말 것 */
/* @media (prefers-color-scheme: dark) { … }  */
/* :root[data-theme="dark"] { … }             */
```

`artifact-design` 스킬의 3-state 다크 모드 패턴은 이 규칙에 의해 override된다. 위반 시 즉시 해당 블록 제거.

**2026-08-31부터 기계 강제된다** — `scripts/operations-lint.py`가 `interactives/*.html`에서 위 두 패턴을 찾으면 **error로 block**한다 (줄 번호까지 출력). 그 전까지 이 규칙은 문서에만 있고 판독 고리가 없어, 네 차례 지적됐음에도 감사 22개가 전부 초록불인 채 다크 토글을 단 임상 도구가 배포됐다. `EXEMPT_FILES`(자동생성 대시보드)도 이 검사만은 면제되지 않는다 — 다만 고칠 곳은 파일이 아니라 생성 스크립트다.

## 8. Overviews domain map (auto-generated — do NOT hand-edit)

`interactives/overviews-map.html` is the at-a-glance browser for all `wiki/overviews/` pages, grouped by clinical domain (search + expand/collapse, titles link to each page). It is **auto-generated** by `scripts/build-overviews-map.py` from each overview's frontmatter (`title`/`date`); the deploy workflow regenerates it on every push to `wiki/**`, and the homepage `wiki/index.md` embeds it via `<iframe>`. The iframe src uses the full absolute `PUBLISH_BASE` URL (Quartz `CrawlLinks` rewrites root-relative/`.html` srcs, so the iframe and the interactives-index link both need the full `{PUBLISH_BASE}/...` URL).

Never edit `overviews-map.html` by hand (it's overwritten). A new overview appears automatically once its file lands in `wiki/overviews/`; if its `stem` matches no domain keyword in the script's `DOMAINS` map, it falls into the `기타 · 미분류` bucket (never dropped). To re-home it, add its keyword to `DOMAINS` in `scripts/build-overviews-map.py`. Regenerate locally with `python3 scripts/build-overviews-map.py`.
