---
name: hygienist-education
description: 치위생사·스탭 교육자료 생성 — 주제/카테고리를 던지면 위키(QMD)에서 근거를 retrieve해 학습목표+핵심요약+플래시카드+퀴즈(정답·해설)+Anki 붙여넣기 블록을 한국어로 생성한다. 사용자가 "교육자료", "치위생사 교육", "수업자료", "레슨", "온보딩 자료", "플래시카드", "퀴즈 만들어", "이번 주 주제", "가르칠 자료", "스탭 교육"을 언급하면 트리거. 임상 자문(clinical-consult)이나 논문 ingest(ingest-paper)와는 다른 독립 스킬 — 교육/학습 자료 제작이면 명시적으로 "스킬"이라 말 안 해도 적용.
argument-hint: [주제 또는 카테고리 (예: 치간청소, 국소마취, 임플란트 유지관리)]
allowed-tools: Bash, Read, Grep
---

# 치위생사 교육 엔진 (Hygienist Education)

주제/카테고리를 받아, **위키에 실제로 있는 근거만**으로 치위생사·스탭이 바로 쓸 수 있는
**레슨팩**(학습목표 → 읽기요약 → 플래시카드 → 퀴즈 → Anki 카드)을 한국어로 생성한다.
52개 카테고리가 그대로 커리큘럼 — 온보딩·주간교육이 위키에서 흘러나오게 하는 것.

## ⛔ THE FOUR RULES (CLAUDE.md — 절대 위반 금지)

1. **웹검색 금지.** WebSearch/WebFetch 안 씀. 교육 내용은 오직 위키.
2. **위키에서 먼저.** `wiki/`가 유일한 진실원천.
3. **부족하면 PDF 재독** 후 위키 갱신.
4. **논문 없으면 없다고.** "이 주제는 위키에 논문이 없습니다 — PDF를 주세요." 지어내지 말 것.

교육자료는 학습자가 그대로 외운다 — **틀린 사실·환각 인용은 임상 위험**. 모든 카드·문항은
실제로 읽은 페이지로의 `[[wikilink]]`를 달고, 수치는 페이지에서 그대로 인용한다.

## 언제 이 스킬이 아닌가

- 임상 케이스 근거 질문 → `clinical-consult`
- 논문을 위키에 넣기 → `ingest-paper`
- 환자 민원 응대 → `claim-coach`

---

## Step 0 — 옵션 확인 (한 번만)

한 줄로 물어 진행(모호할 때만). 기본값으로 바로 만들어도 됨:
- **대상 수준**: 신입(기초·용어 중심) / 숙련(임상 판단·수치 중심). 기본 신입.
- **분량**: 플래시카드 8~15장, 퀴즈 5문항 (기본).

## Step 1 — 주제 → 범위 결정

주제가 카테고리명이면 그 폴더 전체가 소재. 개념이면 관련 페이지를 검색으로 모은다.
overview가 있으면 그것이 뼈대(이미 종합됨).

## Step 2 — 근거 검색 (QMD, 위키 한정)

```bash
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
qmd search  "<주제 핵심 용어>"      # BM25 — 빠르고 안정적 (1차)
qmd vsearch "<주제 개념 문장>"       # 벡터 — 개념 검색
ls wiki/<category>/*.md              # 카테고리면 폴더 나열
```

- `qmd query`(LLM 리랭킹)는 비대화형에서 멈출 수 있음 → `search`/`vsearch` 우선 (memory [[qmd-query-hangs-headless]]).
- **overview 우선** 읽기 → 이어서 개별 페이지 3~8편. 각 페이지의 One-line Summary·한줄요약·Results·confidence 확인.

## Step 3 — Rule #4 게이트

관련 페이지가 안 나오면 멈추고 "위키에 이 주제 논문이 없습니다 — PDF 주세요."

## Step 4 — 레슨팩 저작 (한국어, 용어표기 규칙)

**용어표기**: 한국어 (English, 약어) — 예: 치간칫솔 (Interdental Brush, IDB).
아래 5개 블록을 순서대로:

```
# 🦷 [주제] 교육 레슨팩  ([대상 수준])

## 📚 학습 목표
- 행동 동사로 3~5개 (…을 설명할 수 있다 / 비교할 수 있다 / 선택할 수 있다).

## 📖 핵심 요약 (읽기 자료)
- 근거 기반 3~6문단/불릿. 각 핵심 주장에 [[category/stem]] 인용 + 핵심 수치.
- 논쟁·회색지대가 있으면 명시("아직 근거 불충분").

## 🃏 플래시카드 (앞 → 뒤)
1. **Q** (앞면 질문)
   **A** (뒷면 답) — [[근거 페이지]]
   … (8~15장)

## ✅ 퀴즈 (정답·해설)
Q1. (문항, 4지선다 A~D)
   정답: X — 해설 (왜 맞고 나머지는 왜 틀린지) — [[근거]]
   … (5문항)

## 📥 Anki 붙여넣기 (Import → 텍스트/TSV, Basic: Front·Back·Tags)
```tsv
앞면 질문<TAB>뒷면 답<TAB>주제태그
...
```
```

**저작 규율(엄수):**
- 모든 사실·카드·문항은 **실제로 읽은 페이지**에 근거. 인용·수치를 지어내지 않는다.
- 퀴즈 오답 보기(distractor)는 그럴듯하되 명백히 틀린 것으로 — 애매한 함정 금지.
- 위키에 없는 내용(제품 사용법, 보험코드 등)은 넣지 않는다.
- Anki 블록은 진짜 탭 문자로 구분(스페이스 아님) — Anki가 그대로 import.

**면책 한 줄**: *교육용 요약 — 최신 임상 프로토콜·개별 판단은 위키 원문·원장 확인.*

## Step 5 — 지식 복리 (optional)

- 공백이 드러나면: "이 하위주제는 위키에 논문이 없어요 — PDF 주시면 ingest."
- 좋은 레슨이면: "이걸 `slides/`에 강의자료로 저장할까요? (agenda 선행)"

---

## Worked example (형식 참고 — 실제는 검색·독해한 실 페이지로 채움)

**입력:** "치간청소 신입 교육자료"

**Step 2:** `qmd search "interdental cleaning floss brush water flosser"` →
overview `interdental-cleaning-devices-synthesis` + 개별 RCT/SR 읽기.

**Step 4 발췌:**

> ## 🃏 플래시카드
> 1. **Q** 인접면 치태 제거에 치실보다 효과적일 수 있는 기구는?
>    **A** 치간칫솔 (Interdental Brush, IDB) — 공간이 허용될 때 우수. [[interdental-cleaning/...]]
> 2. **Q** 물치실 (Water Flosser)의 근거상 위치는?
>    **A** 접근 어려운 부위에서 유용하나 치실 대비 우월성은 근거 혼재. [[overviews/interdental-cleaning-devices-synthesis]]
>
> ## ✅ 퀴즈
> Q1. 치간칫솔이 치실보다 유리한 조건은?
>    A. 치간공간이 좁고 치은이 건강 / **B. 치간공간이 열려 있고 IDB가 통과 가능** / C. 교정장치 없음 / D. 항상
>    정답: B — IDB는 공간이 허용될 때 인접면 치태 제거가 우수. [[interdental-cleaning/...]]
