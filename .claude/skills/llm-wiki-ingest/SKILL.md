---
name: llm-wiki-ingest
description: /Users/oracleneo/llm-wiki 치과 임상 지식 위키에 PDF 논문을 인제스트하는 전체 파이프라인을 안내한다. 사용자가 "위키에 추가", "논문 추가", "PDF 추가", "ingest", "위키 업데이트", "sources 페이지 만들어줘", "wiki 페이지 만들어줘", "논문 정리해줘", PDF 파일 경로를 언급하면서 위키와 연관짓는 경우 항상 이 스킬을 사용할 것. 새 논문을 위키에 넣는 작업이라면 명시적으로 "ingest"나 "위키"라는 단어가 없어도 트리거.
argument-hint: [/path/to/paper.pdf]
allowed-tools: Bash, Read, Write, Edit
---

# LLM-Wiki Ingest Pipeline

`/Users/oracleneo/llm-wiki`에 PDF 논문을 추가하는 5단계 파이프라인.
각 단계는 순서대로 실행. 중단·건너뜀 금지.

---

## 전체 흐름

```
Step 0: Pre-ingest gate (중복·철회 검사)
Step 1: PDF 복사 + 텍스트 추출
Step 2: sources/{stem}.md 작성
Step 3: wiki/{category}/{stem}.md 작성
  ↳ Step 3a: 카테고리 결정 (신규 카테고리 생성 포함)
Step 4: index.md 업데이트
Step 5: QMD 인덱스 갱신
Step 6: Overview 연동 (기존 갱신 또는 신규 생성)
Step 7: Interactive 콘텐츠 제안
```

---

## Step 0 — Pre-ingest Gate

새 논문을 받으면 반드시 이 단계부터 시작.

**중복 검사 (DOI 기반):**
```bash
grep -rl "10.xxxx/doi-here" /Users/oracleneo/llm-wiki/sources/
```
결과가 있으면 **신규 ingest 금지** — 기존 페이지 갱신만 허용.

같은 논문이 다른 stem으로 이미 있을 수 있으므로, DOI 외에 제목 핵심어로도 확인:
```bash
grep -rl "keyword-from-title" /Users/oracleneo/llm-wiki/sources/
```

**철회 논문 확인:**
- Retraction Notice, Erratum 등이 확인되면 ingest 자체를 거부.
- 철회된 논문이어야 기록이 필요한 경우: "RETRACTED — do not cite" 스텁만 생성, 정규 페이지 금지.

---

## Step 1 — PDF 복사 & 텍스트 추출

### Stem 명명규칙
```
{first-author-lastname}-{year}-{first-5-title-words}
```
- 전부 소문자
- 특수문자 제거 (콤마, 괄호, 콜론 등)
- 공백 → 하이픈
- 예: `jung-2023-immediate-implant-placement-sinus.pdf`

### PDF 복사
```bash
cp "/path/to/paper.pdf" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```
심볼릭 링크 금지. 항상 `cp`.

### 텍스트 추출
```python
import pypdf, sys

reader = pypdf.PdfReader("/Users/oracleneo/llm-wiki/papers/{stem}.pdf")
text = ""
for page in reader.pages[:15]:
    t = page.extract_text()
    if t:
        text += t + "\n"
    if len(text) > 12000:
        break
print(text[:12000])
```
추출 텍스트를 바탕으로 Step 2·3 작성.

---

## Step 2 — sources/{stem}.md 작성

### Frontmatter (전 필드 필수)
```yaml
---
title: "Paper Full Title"
authors: "First Author, Second Author, et al."
year: YYYY
doi: "10.xxxx/xxxxx"
category: [category-folder]   # 아래 카테고리 목록 참조
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---
```

### 섹션 순서 (필수, 비우지 말 것)

```markdown
## Why Ingested
왜 지금 이 논문을 인제스트하는지 1~2문장.
반드시 기존 위키 페이지 [[wikilink]] 최소 1개 포함.
예: 기존 [[implants/isq/andersson-2019-rfa-factors]] ISQ threshold 보강 근거로 활용.

## One-line Summary
(English: study type, n, primary outcome — one sentence)

## 한줄요약
(한국어: study type, n, 핵심 결과 — 한 문장)

## 1. Document Information
- Journal, volume, pages, publication date
- Funding source, conflicts of interest

## 2. Key Contributions
- 이 논문이 기존 지식에 추가한 것 (bullet 3~5개)

## 3. Methodology and Architecture
- Study design, population, inclusion/exclusion
- Intervention, control, follow-up duration
- Statistical methods

## 4. Key Results and Benchmarks
- Primary outcome: 수치 + 95% CI
- Secondary outcomes
- Subgroup analyses (해당 시)

## 5. Limitations and Future Work
- 저자가 명시한 한계
- 추가로 식별된 한계 (방법론적 결함 등)

## 6. Related Work
- 이 논문이 인용·비교한 핵심 선행연구

## 7. Glossary
- 논문 특유의 약어·용어 정의
```

---

## Step 3a — 카테고리 결정

wiki 페이지를 쓰기 전에 카테고리를 확정한다.

### 판단 기준
1. 아래 **카테고리 목록**에서 가장 가까운 항목 선택.
2. 기존 카테고리 2개 이상에 걸치면 **method/procedure 우선** (병리·해부 기준 아님).
3. 기존 카테고리 어디에도 맞지 않으면 → **신규 카테고리 생성**.

### 신규 카테고리 생성 절차

기존 카테고리가 없는 토픽(예: `implant-occlusion`, `sleep-dentistry`, `fluoride-therapy`)이면:

```bash
# 1. wiki 하위에 새 폴더 생성
mkdir -p /Users/oracleneo/llm-wiki/wiki/{new-category}/

# 2. CLAUDE.md 카테고리 표 갱신 (아래 형식으로 한 행 추가)
# | `new-category` | 한국어 명칭 | 포함 내용 |

# 3. index.md에 새 카테고리 섹션 추가
## New Category (한국어명)
- [[new-category/stem]] — one-line summary (year)
```

카테고리명 규칙:
- 소문자, 하이픈 구분
- 단수형 권장 (`implant-occlusion`, not `implant-occlusions`)
- 기존 계층 구조 준수 (예: `endodontics/새하위`, `implants/새하위`, `behavioral-dentistry/새하위`)

신규 카테고리를 만들 때는 사용자에게 한 줄로 보고: `"[new-category] 카테고리를 신규 생성했습니다."`

---

## Step 3 — wiki/{category}/{stem}.md 작성

### Frontmatter (전 필드 필수)
```yaml
---
title: "Paper Full Title"
authors: "First Author et al."
year: YYYY
date: YYYY-MM-DD          # 출판일; 연도만 알면 YYYY-01-01; 모르면 ingest 날짜
doi: "10.xxxx/xxxxx"
source: {stem}.md
category: [category-folder]
confidence: sr+ma          # 아래 vocabulary 참조
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---
```

### confidence vocabulary (단일 레이블)
| 값 | 적용 |
|---|---|
| `sr+ma` | Systematic review + meta-analysis |
| `sr` | Systematic review (meta-analysis 없음) |
| `rct` | Randomized controlled trial |
| `prospective` | Prospective cohort / case series |
| `retrospective` | Retrospective cohort / chart review |
| `cross-sectional` | Cross-sectional study, survey |
| `case-report` | Case report / 소규모 case series (n < 10) |
| `in-vivo` | In vivo clinical/animal (위 분류 미해당) |
| `animal` | 동물 실험 전용 |
| `in-vitro` | 실험실 연구 |
| `narrative-review` | Narrative review, commentary |
| `consensus` | Consensus statement / position paper |
| `synthesis` | Wiki overview page (외부 study 아님) |

### 섹션 순서 (필수)
```markdown
## One-line Summary
(English: study type, n, key finding — one sentence)

## 한줄요약
(한국어: study type, n, 핵심 결과 — 한 문장)

## Summary
3~5문장. 논문의 목적·방법·주요 결과·임상적 의의.

## Key Contributions
- bullet 3~5개. 기존 지식 대비 이 논문이 추가한 것.

## Methodology
Study design, population (n), intervention/control, outcome measures, follow-up.
수치·통계 방법 포함.

## Results
Primary outcome: 수치 (95% CI, p-value).
Secondary outcomes. 중요 subgroup.

## Related Papers
- [[category/stem]] — relationship (reinforces / extends / contradicts / refines)
```

**본문 언어: 영어** (RAG 최적화. 한줄요약만 한국어).

### 선택적 frontmatter 필드

**relations** (신규 페이지가 기존 페이지와 명확한 관계가 있을 때):
```yaml
relations:
  - type: extends         # extends | reinforces | contradicts | refines | applies-to
    target: existing-stem-name
```

**superseded_by** (신규 논문이 기존 페이지의 결론을 뒤집을 때, 기존 페이지에 추가):
```yaml
superseded_by: newer-stem-name
superseded_scope: full    # full | partial
```
이 경우 기존 페이지 본문 최상단에 배너도 추가:
```markdown
> [!warning] Superseded (full) → [[newer-stem-name]]
> 이유 한 줄. (set YYYY-MM-DD)
```

---

## Step 4 — index.md 업데이트

```bash
# 해당 카테고리 섹션 아래에 한 줄 추가
/Users/oracleneo/llm-wiki/index.md
```
형식: `- [[category/stem]] — one-line summary (year)`

---

## Step 5 — QMD 인덱스 갱신

```bash
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
qmd update   # 파일시스템 재스캔
qmd embed    # 신규 문서 임베딩 (incremental — 수 초)
```

전체 재임베딩(`-f`)은 ~2.5시간 — 절대 금지. incremental만.

---

## 카테고리 목록

```
implants                              implants/isq
implants/surface                      implants/vertical-ridge-augmentation
implants/peri-implantitis             implants/versah-protocols
bone-regeneration                     immediate-implant
sinus-lift/lateral                    sinus-lift/transcrestal
sinus-lift/pseudocyst                 endodontics/eal
endodontics/irrigation                endodontics/anatomy
endodontics/vpt                       endodontics/shaping
endodontics/regenerative              periodontics
dental-materials                      digital-workflow
resin                                 resin-bonding
prosthetic-materials                  drug
pdrn                                  oral-surgery
suture-wound-closure                  occlusion
geriatric-dentistry                   local-anesthesia
inlay                                 evidence-appraisal
bone-biology                          radiology
oral-medicine                         botulinum-toxin
orthodontics                          tmj
caries                                cracked-tooth
professional-wellbeing                dentin-hypersensitivity
practice-management                   overviews
behavioral-dentistry/motivational-interviewing
behavioral-dentistry/communication-relationship
behavioral-dentistry/patient-reported-outcomes
behavioral-dentistry/dental-anxiety
```

---

## Step 6 — Overview 연동

논문 ingest 후 반드시 실행. wiki/overviews/ 와의 연결이 끊기면 지식이 고립된다.

### 6-1. 기존 Overview 갱신 대상 탐색

먼저 이 논문이 어느 overview에 걸리는지 찾는다:

```bash
grep -rl "{category}" /Users/oracleneo/llm-wiki/wiki/overviews/
grep -rl "{key-topic-keyword}" /Users/oracleneo/llm-wiki/wiki/overviews/
```

매칭되는 overview마다 **두 단계로 분리**해 갱신한다. link-level은 항상, body-level(coverage)은 조건부.

**(a) Link-level — 항상 수행 (무조건)**
- frontmatter `source_papers:` 에 새 stem 추가
- `## Related Papers` 에 `- [[category/stem]] — relationship` 한 줄 추가
- 여기까지만 하면 overview에 *링크는 걸렸지만 본문엔 안 들어간* 상태 → `overview-coverage-lint.py`의 cov%를 떨어뜨린다. 아래 (b)를 반드시 판정할 것.

**(b) Body-level (coverage) — 임계값 충족 시 본문 직접 편집**

아래 트리거 중 **하나라도 해당하면** 단순 링크에 그치지 말고 overview *본문*(Thesis 분기·Evidence Map 표·Clinical Decision Points)에 author·year로 인용해 녹인다. 이게 "coverage 추가할 정도"의 판정 기준이다:

| 트리거 | 본문 반영 동작 |
|---|---|
| 논문이 overview의 thesis 질문에 직접 답함 | Thesis 또는 해당 분기 문장 갱신 + (Author, Year) 인용 |
| SR+MA / RCT (confidence `sr+ma`·`sr`·`rct`) | Evidence Map 표에 행 추가 (Design·n·Key Finding·Confidence) |
| overview가 쓰는 수치·임계값을 보강·수정 (ISQ, 용량, 생존율 등) | 해당 수치 문장 옆에 근거로 병기, 값이 바뀌면 본문 값 갱신 |
| 기존 Decision Point를 강화·약화·반박 | 해당 decision node 문장 직접 수정, 방향 전환이면 표시 |
| 기존 결론을 뒤집음 | `superseded_by` 절차(Step 3) 연계 + Thesis 갱신 |

위 어디에도 안 걸리면 (예: 주변적 narrative-review, 동물실험 단편) link-level만 두고 본문은 건드리지 않는다 — 억지 인용으로 cov%만 채우지 말 것.

**결론 변경 수준의 본문 수정**(Thesis 전환, Decision Point 방향 반전)은 적용 전에 사용자에게 한 줄 보고 후 진행.

**자가 점검**: 본문 편집 후, 추가한 stem이 overview 본문에 `(Author Year)` 또는 그에 준하는 형태로 실제 등장하는지 확인. 등장하지 않으면 coverage 미반영 상태 → (b) 재수행.

### 6-2. 신규 Overview 생성 판단

아래 조건 중 하나라도 해당하면 신규 overview를 제안:

| 조건 | 예시 |
|---|---|
| 해당 카테고리에 논문이 ≥5편 쌓였고 overview가 없음 | `caries` 카테고리에 6편, overview 0편 |
| 방금 ingest한 논문이 SR+MA이고 기존 overview에 통합하기 어려움 | 독립적 체계적 고찰 |
| 신규 카테고리를 만든 경우 | Step 3a에서 신규 카테고리 생성 시 자동 제안 |
| 2개 이상 카테고리를 포괄하는 임상 결정 논문 | multimodal approach SR |

**신규 overview 생성 시 기본 템플릿:**

```yaml
---
title: "Overview: {Topic}"
type: synthesis
category: overviews
date: YYYY-MM-DD
source_papers:
  - wiki/{category}/{stem}.md
tags: []
---
```

```markdown
## One-line Summary
(English: what clinical question this overview answers)

## 한줄요약
(한국어)

## Thesis
이 overview가 답하는 핵심 임상 질문과 현재 best evidence 결론.

## Evidence Map
| Paper | Design | n | Key Finding | Confidence |
|---|---|---|---|---|

## Clinical Decision Points
임상적으로 가장 중요한 decision node 2~4개. 표 또는 decision tree.

## Gaps & Future Research
현재 근거의 공백. 진행 중인 RCT, 미해결 쟁점.

## Related Papers
- [[category/stem]] — relationship
```

신규 overview를 만들 때 사용자에게 한 줄 보고: `"[topic] 신규 overview 생성했습니다: wiki/overviews/{stem}.md"`

---

## Step 7 — Interactive 콘텐츠 제안

ingest 완료 후, 논문 내용을 기반으로 `/Users/oracleneo/llm-wiki/interactives/`에 만들 만한 HTML 위젯을 제안한다. 제안은 항상 선택적 — 사용자가 원할 때만 생성.

### 제안 기준

논문에 아래 요소가 있으면 해당 인터랙티브를 제안:

| 논문 특성 | 제안 인터랙티브 | 예시 |
|---|---|---|
| 수치 파라미터(용량·시간·ISQ 임계값) | 계산기 / 슬라이더 | ISQ 로딩 결정 계산기 |
| 여러 술식·재료 비교 | 비교 매트릭스 / 필터 테이블 | 골이식재 비교 표 |
| 시계열 데이터(ISQ 변화, 생존율 곡선) | 차트 위젯 | 임플란트 안정성 시간 그래프 |
| 의사결정 분기 (적응증·금기) | 결정 트리 | 즉시식립 적응증 체커 |
| 해부 구조 + 수치 | 다이어그램 + 수치 오버레이 | EAL 측정 원리 인터랙티브 |
| 위험도 계층화 | 리스크 스코어러 | 임플란트 실패 위험 계산기 |
| 프로토콜 순서 | 단계별 체크리스트 | 상악동거상술 프로토콜 체커 |

### 제안 형식

ingest 완료 메시지 끝에 다음처럼 제안:

```
💡 인터랙티브 제안:
- [계산기] ISQ 로딩 결정 계산기: 이 논문의 ISQ ≥65 임계값 + 골밀도 보정 변수 반영
- [비교표] 5개 osteotomy 프로토콜 ISQ 궤적 비교 (T0~T4 그래프)
원하면 만들어드릴게요.
```

제안 개수: 1~3개. 논문 관련성이 낮으면 제안 생략.

---

## 완료 체크리스트

Step 종료 전 자가 점검:

- [ ] sources/{stem}.md — frontmatter 전 필드 채워졌는가?
- [ ] sources/{stem}.md — `## Why Ingested` + `[[wikilink]]` 있는가?
- [ ] wiki/{stem}.md — 본문이 **영어**인가?
- [ ] wiki/{stem}.md — confidence 레이블 정확한가?
- [ ] wiki/{stem}.md — `## 한줄요약` 한국어로 있는가?
- [ ] papers/{stem}.pdf — cp로 복사됐는가? (symlink 아닌지)
- [ ] index.md — 해당 카테고리에 항목 추가됐는가?
- [ ] qmd update && qmd embed — 실행됐는가?
- [ ] 1:1 매칭 — papers/의 PDF와 sources/의 .md 이름 일치하는가?
- [ ] 신규 카테고리 생성 시 — CLAUDE.md 표 + index.md 섹션 추가됐는가?
- [ ] overview 연동 (link) — 매칭 overview의 source_papers·Related Papers에 추가됐는가?
- [ ] overview 연동 (coverage) — 6-1(b) 트리거 충족 시 본문에 author·year로 인용됐는가?
- [ ] interactive 제안 — 관련 제안 1~3개 제시됐는가?
