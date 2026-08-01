# DeepSeek 논문 인제스트 프롬프트

PDF를 DeepSeek에서 먼저 처리한 뒤 Claude에 넘겨 토큰을 절약하는 하이브리드 워크플로용.
산출물은 md 파일로 저장해 llm-wiki 루트 폴더에 드롭하면 Claude가 마저 인제스트.

---

## DeepSeek에게 보내는 프롬프트 (복사해서 사용)

```
이 논문 PDF를 읽고 아래 형식 그대로 출력해줘.
한 글자도 형식 바꾸지 말고, 빈 칸은 "unknown"으로 채워줘.

---METADATA---
title: (논문 영문 제목 그대로)
authors: (First Author, Second Author, Third Author — 쉼표 구분)
year: (출판 연도 4자리)
doi: (DOI 번호만, 앞에 https://doi.org/ 붙이지 말 것. 없으면 unknown)
journal: (저널명, 권호 페이지)
institution: (제1저자 소속기관)
evidence_level: (아래 중 하나만: sr+ma / sr / rct / prospective / retrospective / cross-sectional / case-report / in-vitro / narrative-review)
n_total: (총 참여자/샘플 수, 예: 20 또는 unknown)
follow_up: (추적 기간, 예: 6 months / 2 years / unknown)

---THREE_LINE_SUMMARY_EN---
Line1: (연구유형·n·맥락 — what was studied, in English)
Line2: (primary result with exact numbers and p-values, in English)
Line3: (clinical implication or key limitation, in English)

---THREE_LINE_SUMMARY_KO---
줄1: (연구유형·n·맥락 — 한국어, 기술용어는 "한국어(English, 약어)" 형식)
줄2: (핵심 결과 + 수치 + p값 — 한국어)
줄3: (임상적 의미 또는 핵심 한계 — 한국어)

---KEY_FINDINGS---
(수치가 포함된 핵심 결과 bullet 5~10개, 영어로)
- ...

---METHODOLOGY---
(연구설계, 포함기준, 제외기준, 평가지표, 통계방법 — 영어로 간결하게)

---LIMITATIONS---
(저자 명시 또는 추론 가능한 한계점 3~5개, 영어)
- ...

---GLOSSARY---
(논문의 핵심 약어·용어 3~6개, 영어 term: 한국어 설명)
- TERM: 설명
```

---

## 워크플로

1. DeepSeek에 PDF + 위 프롬프트 전송
2. 산출물을 `.md` 파일로 저장 → llm-wiki 루트 폴더에 드롭
3. Claude에게: `"루트 폴더에 DeepSeek 인제스트 파일이 있어, 마저 인제스트해줘"`
4. Claude가 Step 0(중복·철회 체크), QMD 검색, Why Ingested, relations, index, git, qmd 자동 처리

## 토큰 절약 효과

| 방식 | Claude 토큰 |
|---|---|
| Claude 단독 | 100% |
| DeepSeek → Claude (위 형식 준수) | ~40~50% |
| DeepSeek → Claude (자유 형식) | ~70% (재해석 비용 발생) |

형식이 정확할수록 Claude가 "변환" 대신 "조립"만 하므로 절약 폭이 커진다.
