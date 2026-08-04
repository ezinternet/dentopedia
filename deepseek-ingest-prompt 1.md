# DeepSeek 논문 인제스트 프롬프트 v2

PDF를 DeepSeek에서 먼저 처리한 뒤 Claude에 넘겨 토큰을 절약하는 하이브리드 워크플로용.
산출물 `.md` 하나를 llm-wiki 루트에 드롭하면 Claude가 저장소 작업만 마저 처리한다.

**v1과의 차이**: v1은 *원재료 블록*(메타데이터·요약·발견)만 받아서 Claude가 두 파일을 처음부터 조립했다.
v2는 **완성된 파일 2개를 그대로 받는다.** Claude는 "작성"이 아니라 "치환 + 저장소 작업"만 한다.

---

## 역할 분담

| DeepSeek (PDF만 보면 되는 일) | Claude (저장소를 알아야 하는 일) |
|---|---|
| `sources/{stem}.md` 전체 | `category:` 확정 (`wiki/_meta/categories.md` 라우팅) |
| `wiki/{category}/{stem}.md` 전체 | `## Why Ingested` + 위키링크 (QMD 검색) |
| stem(파일명) 생성 | `relations:` 타입드 엣지 |
| frontmatter 전 필드 (경로 포함) | `superseded_by:` 판단 |
| `evidence_level` 라벨 | Step 0 중복(DOI grep)·철회(PubMed MCP) 게이트 |
| `index.md` 한 줄 (한국어) | PDF 복사·이름변경, `index.md` 반영 |
| 참고문헌 DOI 목록 | lint·orphan-check·git 커밋·qmd 재색인 |

**경계 원칙**: DeepSeek은 *논문 안에 답이 있는 것*만 한다. *다른 페이지를 알아야 하는 것*은 전부 Claude.

---

## PROMPT A — 본 프롬프트 (PDF와 함께 붙여넣기)

```
너는 치과 논문을 llm-wiki 형식으로 변환하는 전처리기다.
첨부한 논문 PDF를 읽고 아래 3개 블록을 순서대로, 형식 그대로 출력하라.
설명·인사말·마크다운 코드펜스 없이 블록만 출력한다.

[절대 규칙]
1. PDF에 없는 값은 절대 지어내지 마라. 메타데이터가 없으면 unknown,
   수치가 보고 안 됐으면 NR(not reported)라고 쓴다. 추정·계산·반올림 금지.
2. 위키링크 [[...]] 를 어디에도 쓰지 마라. relations:, superseded_by: 필드도 만들지 마라.
   너는 이 저장소에 어떤 페이지가 있는지 모른다. 지어낸 링크는 감사에서 깨진다.
3. __CATEGORY__ 는 그 글자 그대로 남겨라. 카테고리는 네가 정하지 않는다.
4. 수치는 원문 그대로 옮긴다: p값, 95% CI, I², n, 추적기간, 단위.
5. 한국어 문장 안의 기술용어는 반드시 "한국어 (English, 약어)" 형식.
   예: 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC) / 상악동 저부 거상술 (Maxillary Sinus Floor Augmentation, MSFA)
6. 구분자(===FILE: ... ===, ===CLAUDE-BRIEF===)를 한 글자도 바꾸지 마라.
7. 언어: 본문은 영어. 한국어는 "## 세줄요약", "## 7. Glossary" 설명, INDEX_LINE, CLAIM에만 쓴다.

[STEM 규칙] — 세 블록에서 동일한 stem을 쓴다
{제1저자성}-{연도}-{제목핵심어 5~8개}
- 전부 소문자, 공백은 하이픈, 관사·전치사·특수문자·움라우트 제거
- 체계적문헌고찰+메타분석이면 끝에 -sr-ma, 체계적문헌고찰만이면 -sr
- 예: wang-2025-porcine-bovine-xenograft-msfa-arp-sr-ma
아래 템플릿의 {stem} 자리는 네가 만든 stem으로 전부 치환한다.

[evidence_level 어휘] — 정확히 하나만 고른다
sr+ma / sr / rct / prospective / retrospective / cross-sectional /
case-report / in-vivo / animal / in-vitro / narrative-review / consensus

===FILE: sources/{stem}.md===
---
title: "논문 영문 제목 그대로"
authors: "전체 저자 목록, 쉼표 구분"
year: YYYY
doi: "10.xxxx/xxxxx"
category: [__CATEGORY__]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## Why Ingested

<!-- CLAUDE-FILL -->

## Three-line Summary

(1문단: 연구설계·n·세팅·기간 — 무엇을 연구했는가. 영어)

(2문단: 1차 결과 + 정확한 수치·p·95% CI·I². 영어)

(3문단: 임상적 함의 또는 핵심 한계. 영어)

## 세줄요약

(1문단: 위 Line1의 한국어 대응. 용어는 "한국어 (English, 약어)")

(2문단: 위 Line2의 한국어 대응. 수치는 그대로)

(3문단: 위 Line3의 한국어 대응)

## 1. Document Information

- Journal: 저널명 Vol(Iss):pages, Year
- DOI: 10.xxxx/xxxxx
- PMID: xxxxxxxx / PMCID: PMCxxxxxxx  (PDF에 없으면 이 줄 생략)
- Registration: PROSPERO / ClinicalTrials.gov 번호 (없으면 Not reported)
- Funding: (없으면 Not reported)
- Conflicts of interest: (없으면 Not declared)

## 2. Key Contributions

- (수치를 포함한 핵심 기여 5~8개, 영어)

## 3. Methodology and Architecture

- Design:
- (SR/MA면) Databases & search window / PRISMA 준수 여부 / 포함·제외 기준 / 포함 연구 수 / 비뚤림 평가 도구(ROB2, NOS, AMSTAR)
- (RCT면) 무작위화 방법 / 배정은닉 / 눈가림 / ITT 여부 / 표본수 산정 / 군 구성
- (관찰연구면) 코호트 정의 / 교란변수 보정 / 추적기간 / 결측 처리
- Outcomes: 1차 / 2차 지표
- Statistics: 검정·효과크기·이질성 지표
(영어, bullets)

## 4. Key Results and Benchmarks

- **Primary outcome —** (지표명): 수치 (95% CI, p, I²)
- (2차 지표들, 수치 그대로. 영어)

## 5. Limitations and Future Work

- (저자가 명시한 한계 + 방법론적으로 명백한 한계 3~6개, 영어)

## 6. Related Work

- (이 논문이 본문에서 실제로 비교·논의한 선행연구를 "저자 연도 — 무엇을 보고했는지" 형식으로.
   위키링크 금지. 5개 이내)

## 7. Glossary

- **ABC (Full Name)**: 한국어 설명
(핵심 약어·용어 4~8개)

===FILE: wiki/__CATEGORY__/{stem}.md===
---
title: "논문 영문 제목 그대로"
authors: 제1저자성 이니셜 et al.
year: YYYY
date: YYYY-MM-DD
doi: "10.xxxx/xxxxx"
source: {stem}.md
category: [__CATEGORY__]
evidence_level: (위 어휘 중 하나)
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## Three-line Summary

(sources의 것과 동일한 3문단)

## 세줄요약

(sources의 것과 동일한 3문단)

## Summary

(영어 1문단 150~250단어: 무엇을 어떻게 연구했고, 결과 수치가 무엇이며, 저자의 결론이 무엇인지)

## Key Contributions

- (영어 4~6 bullets — sources §2를 위키용으로 압축)

## Methodology

(영어 1~2문단 산문. 설계·검색/무작위화·포함제외·표본·통계·비뚤림평가)

## Results

| Outcome | Effect | 95% CI | p | I² |
|---|---|---|---|---|
| (1차 지표) | | | | |
| (2차 지표) | | | | |

(표로 담기 어려운 결과는 표 아래 문장으로 보충. 보고 안 된 칸은 NR)

## Related Papers

<!-- CLAUDE-FILL -->

===CLAUDE-BRIEF===
STEM: {stem}
DOI: (없으면 none)
PMID: (없으면 none)
PMCID: (없으면 none)
EVIDENCE_LEVEL: 
PUB_DATE: YYYY-MM-DD (일자 없으면 YYYY-01-01)
N_TOTAL: (총 참여자/샘플/사이트 수, 또는 unknown)
FOLLOW_UP: (예: 12 months / 5 years / unknown)
DOC_TYPE: full-text | abstract-only | landing-page | retraction-notice | erratum
RETRACTION_FLAG: yes | no
   (본문·워터마크·헤더에 RETRACTED / Withdrawn / Retraction Note / 철회 표기가 있으면 yes)
CATEGORY_CANDIDATES: (카테고리 목록을 받았으면 1순위/2순위/3순위 폴더명.
   목록을 못 받았으면 이 논문의 시술·방법 키워드 3개)
INDEX_LINE: - [[__CATEGORY__/{stem}]] — {제1저자성} {연도} · {evidence_level} · {한국어 한 줄 요약, 핵심 수치 포함} (DOI {doi})
CLAIM: (이 논문의 임상적 결론 한 문장 — 한국어)
CHALLENGES: (이 논문이 명시적으로 반박·수정·갱신한다고 밝힌 기존 통념이나 선행 결론. 없으면 none)
REF_DOIS:
- 10.xxxx/xxx — 저자 연도, 한 줄 설명
(본문 Discussion에서 실제로 논의된 핵심 참고문헌만 10~20개. DOI 없는 항목은 생략)
```

---

## PROMPT B (선택) — 카테고리 후보까지 시키기

PROMPT A 앞에 카테고리 목록을 한 번 붙여넣으면 `CATEGORY_CANDIDATES`가 실제 폴더명으로 나온다.
DeepSeek은 대화 컨텍스트를 유지하므로 **대화당 한 번만** 붙여넣으면 된다.

목록은 하드코딩하지 않는다 — `wiki/_meta/categories.md`가 유일한 출처이므로 매번 거기서 뽑는다:

```bash
python3 -c "import re,sys;print(' / '.join(f'{m.group(1)} = {m.group(2)}' for m in (re.match(r'^\|\s*\`([^\`]+)\`\s*\|\s*([^|]+?)\s*\|',l) for l in open('wiki/_meta/categories.md')) if m))"
```

출력 앞에 이 한 줄을 붙여 DeepSeek에 전달:

```
아래는 llm-wiki의 카테고리 폴더 목록이다. 이후 논문 처리 시 CATEGORY_CANDIDATES에
이 목록의 폴더명만 1~3순위로 제안하라. 분류 기준은 질환·해부가 아니라 술식·방법(method/procedure)이다.
목록에 없는 폴더명을 지어내지 마라.
```

**주의**: DeepSeek의 카테고리 제안은 *후보*일 뿐이다. Claude가 QMD로 유사 페이지를 찾아 최종 확정한다 (라우팅 원칙 1단계).

---

## 절대 DeepSeek에 시키지 않는 것

| 금지 | 이유 |
|---|---|
| `[[wikilink]]` 작성 | 존재하지 않는 stem을 지어낸다 → `link-integrity.py`에서 깨진 링크로 잡힘 |
| `relations:` 타입드 엣지 | `target`이 실존 stem이어야 함 (`relations-audit.py` 검증). 타입 선택도 두 논문을 다 읽어야 하는 판단 |
| `superseded_by:` | 우리가 보유한 페이지와의 근거 무게 비교 — 연도 비교가 아님 |
| `## Why Ingested` | QMD로 기존 페이지를 찾아 "왜 지금 넣는가"를 쓰는 것 = 저장소 지식 |
| `category:` 확정 | `categories.md` 라우팅 5단계 + 유사 페이지 조회 필요 |
| 중복·철회 판정 | DOI grep(로컬) + PubMed MCP 확인이 필요 |

**한 줄 요약**: DeepSeek은 링크를 만들지 않는다. 링크는 전부 Claude 몫이다.

---

## 워크플로

1. DeepSeek 새 대화 → (선택) PROMPT B 목록 → PDF 첨부 + PROMPT A 전송
2. 출력 전체를 그대로 복사해 `.md` 파일로 저장
   - 파일명: `deepseek_markdown_YYYYMMDD_XXXXXX.md` (아무 이름이나 무방, 확장자만 `.md`)
   - 저장 위치: `/Users/oracleneo/llm-wiki/` 루트
3. **PDF 원본도 같이 준비** — Claude가 `papers/{stem}.pdf`로 복사해야 한다 (3-tier 원칙: 원본 PDF는 불변 보관)
4. Claude에게: `"루트에 DeepSeek 인제스트 파일 있어, 마저 인제스트해줘. PDF는 <경로>"`
5. 논문이 여러 편이면 **논문당 DeepSeek 대화를 분리**한다 (한 대화에 여러 PDF를 넣으면 수치가 섞인다)

### 30초 검수 체크리스트 (저장 전 눈으로)

- [ ] `__CATEGORY__` 가 3군데(sources frontmatter / wiki 경로 / wiki frontmatter / INDEX_LINE)에 그대로 남아 있는가
- [ ] `[[` 가 파일 안에 하나도 없는가 (`## Related Papers`는 `<!-- CLAUDE-FILL -->` 이어야 함)
- [ ] `## Results` 표에 실제 수치가 있는가 (전부 NR이면 초록만 읽은 것 → `DOC_TYPE` 확인)
- [ ] `STEM`이 세 곳에서 동일한가
- [ ] `RETRACTION_FLAG: yes` 이면 Claude에게 반드시 알린다 (기본은 인제스트 금지)

---

## Claude가 이어받아 하는 일

기계적인 절반은 `scripts/deepseek-split.py`가 처리한다 (아래 절). 나머지가 Claude 판단:

1. **1단계 — 리포트** (스크립트): 검증 + Step 0 DOI 중복 grep + `REF_DOIS` 보유 여부 매칭
2. `CATEGORY_CANDIDATES` + QMD 조회로 `category:` 확정
3. **2단계 — 쓰기** (스크립트): `__CATEGORY__` 치환, 두 파일 저장, PDF를 `papers/{stem}.pdf`로 복사
4. `## Why Ingested` 작성 (QMD로 찾은 기존 페이지 위키링크 필수 1개 이상)
5. `## Related Papers` + `relations:` — 스크립트가 찾아준 `REF_DOIS` 매칭 stem이 1순위 후보
6. `CLAIM` / `CHALLENGES`로 supersession 판단 → 필요 시 **기존(더 오래된) 페이지**에 배너 추가
7. `INDEX_LINE`을 `index.md`의 해당 카테고리 아래 삽입
8. `DOC_TYPE`이 `abstract-only`/`landing-page`면 `full_text: false` + 본문 caveat (INGEST.md Step 1-A)
9. lint → orphan-check → 파일별 git 커밋 → push → `qmd update && qmd embed`
10. DeepSeek 원본 `.md` 삭제

---

## 분할 스크립트 — `scripts/deepseek-split.py`

Claude가 dump를 읽고 두 파일을 **다시 출력**하는 비용을 없앤다. 파싱·검증·치환·저장을 스크립트가 하고,
Claude는 짧은 리포트만 읽는다.

### 1단계 — 리포트 (검증 + 저장소 조회)

```bash
python3 scripts/deepseek-split.py <dump.md>
```

출력:
- 검증 결과 (아래 가드레일 중 하나라도 걸리면 **exit 1, 아무것도 쓰지 않음**)
- `STEM / DOI / EVIDENCE_LEVEL / DOC_TYPE / RETRACTION_FLAG / N_TOTAL / FOLLOW_UP`
- **Step 0 중복 판정** — 이 DOI를 가진 `sources/` 페이지가 이미 있으면 경고 + 기존 stem
- **`REF_DOIS` 매칭** — 인용문헌 중 우리가 이미 보유한 논문의 stem 목록 (관계 후보)
- `CATEGORY_CANDIDATES` / `CLAIM` / `CHALLENGES` / `INDEX_LINE`

### 2단계 — 쓰기 (카테고리 확정 후)

```bash
python3 scripts/deepseek-split.py <dump.md> --category bone-regeneration --pdf ~/Downloads/paper.pdf
```

`__CATEGORY__`를 전부 치환해 `sources/{stem}.md` + `wiki/{category}/{stem}.md`를 쓰고,
PDF를 `papers/{stem}.pdf`로 복사한 뒤, 치환된 `index.md` 한 줄과 남은 할 일을 출력한다.

| 옵션 | 용도 |
|---|---|
| `--dry-run` | 디스크 안 건드리고 무엇을 쓸지만 확인 |
| `--force` | 기존 페이지 덮어쓰기 (기본은 존재하면 거부) |
| `--new-category` | `wiki/{category}/` 폴더가 없을 때 신설 허용 (기본은 거부) |

### 거부(exit 1) 조건 — 경고가 아니라 중단

| 조건 | 이유 |
|---|---|
| 본문에 `[[wikilink]]` | DeepSeek은 우리 stem을 모른다 → 지어낸 링크. `link-integrity.py`가 잡기 전에 막는다 |
| `relations:` / `superseded_by:` 존재 | Claude 판단 필드 |
| stem 불일치 (두 헤더 / `source:` / `pdf_filename`) | `orphan-check.py`의 1:1 규칙이 조용히 깨진다 |
| frontmatter 필수 필드 누락 | `lint.py`와 동일한 목록으로 사전 차단 |
| `evidence_level` 어휘 이탈 | 같은 이유 |
| `<!-- CLAUDE-FILL -->` 없음 | DeepSeek이 Why Ingested / Related Papers를 채워버렸다는 뜻 |
| 필수 섹션 누락 | 이중언어 세줄요약 쌍 등 (`content-lint.py` 사전 차단) |
| `===FILE:===` 블록 없음 | v1 형식 dump — 그건 Claude가 조립 (exit 2) |

---

## 토큰 절약 (추정)

| 방식 | Claude 토큰 (추정) | 병목 |
|---|---|---|
| Claude 단독 (PDF 직접 읽기) | 100% | PDF 12,000자 입력 + 두 페이지 전문 작성 |
| v1 (원재료 블록) | ~50% | 블록 → 두 파일로 재조립하는 출력 비용이 그대로 남음 |
| v2 (완성 파일 2개, 수동 저장) | ~25~30% | Claude가 dump 전체를 읽고 두 파일을 다시 출력 |
| **v2 + `deepseek-split.py`** | **~10~15%** | dump를 아예 안 읽음. 짧은 리포트 + 판단 필드만 |

절약은 대부분 **출력 토큰**에서 나온다 — Claude가 위키 본문을 "쓰지" 않고, 스크립트가 "옮기기"만 하기 때문.
그래서 형식이 정확할수록 절약 폭이 커진다: 구분자가 어긋나면 스크립트가 거부하고 Claude가 수동 조립으로 되돌아간다.

---

## 참조

- 인제스트 파이프라인 전체: `INGEST.md` (Step 0–5, 필드 정의, 철회 페이지 구조)
- 카테고리 라우팅: `wiki/_meta/categories.md` (단일 출처)
- 행동 규칙: `CLAUDE.md` (THE FOUR RULES, 언어 정책, 용어 표기)
