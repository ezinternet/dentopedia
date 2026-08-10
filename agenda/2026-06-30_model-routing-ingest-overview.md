---
title: "모델 라우팅 SOP — ingest는 Sonnet, 종합·판단은 Opus"
type: agenda
date: 2026-06-30
status: done
owner: 원장
priority: P1
tags: [model-routing, sonnet, opus, ingest, overview, sop, cost]
source_wiki:
  - wiki/overviews/adhesive-bonding-strategies-overview.md            # Opus-필수 작업의 대표 예 (교차논문 종합)
  - wiki/immediate-implant/esthetic-soft-tissue/aldhohrah-2022-soft-tissue-augmentation-immediate-delayed-sctg-sr-ma.md  # Sonnet-충분 작업의 대표 예 (단일논문 추출)
output_wiki: []
---

# Goal

위키 작업에서 **어떤 작업을 Sonnet으로 돌리고 어떤 작업을 Opus로 escalate할지** 단일 기준으로 고정한다. 핵심 원칙: **"추출이면 Sonnet, 종합·판단이면 Opus."** 비용 최적화(인제스트 물량은 Sonnet ~1/5 비용)와 품질(고-판단 산출물은 Opus)을 동시에 만족시키는 운영 규칙.

# Input

- `.claude/skills/ingest-paper/SKILL.md` — Step 0 모델 체크 분기의 근거 문서
- `CLAUDE.md` § Adding a New Paper (PHASE 1 fan-out / PHASE 2 finalize 병렬 프로토콜)
- 메모리: [[supersession-judgment-at-ingest]] — 매 ingest 시 기존 페이지 대체 판단 (= 고-판단 영역)

# Output

- `.claude/skills/ingest-paper/SKILL.md` Step 0·4·6에 **Opus escalation 분기** 추가 (이 agenda에서 파생)
- 본 agenda 파일 = 라우팅 규칙의 SSOT(single source of truth)

# 핵심 규칙 — 작업별 모델

판단 기준은 **"모델의 판단(judgment)이 들어가느냐"** 한 가지다. 사실 추출·기계 변환 = Sonnet, 교차논문 추론·임상 판단·재작성 = Opus.

| 작업 | 모델 | 이유 |
|---|---|---|
| PDF 텍스트 추출 (pypdf) | Sonnet/Haiku | 순수 기계 작업 |
| `sources/{stem}.md` 작성 | **Sonnet** | 7섹션 추출형 정리 |
| 카테고리 분류 | **Opus** (경계 사례) | 60+ 폴더 경계 오분류가 누적되면 구조 붕괴. 짧지만 고-판단 |
| `wiki/{category}/{stem}.md` 단일 페이지 | **Sonnet** | 대부분 추출형 |
| `## Why Ingested` + `superseded_by` 판단 | **Opus** | 기존 페이지와의 관계(보강/반박/대체) = 교차논문 추론 |
| `wiki/overviews/` 종합 페이지 | **Opus (필수)** | 여러 논문의 thesis·수치·결정트리를 한 논증으로. 최고가치·최고판단. Sonnet 금지 |
| 한국어 핵심요약 / 한줄요약 | **Opus** | 밀도 높은 영문을 ~10불릿으로 압축 + 임상 takeaway 선별 (번역 아님) |
| `interactives/*.html` 임상 계산기 (Class B) | **Opus** | 논문에서 임계값 추출 — Rule #1 환각 위험 최대 |
| lint/audit/스크립트 실행 | Sonnet | 결정론적 코드 작업 |
| index.md 갱신 / commit·push / qmd | Sonnet/Haiku | 순수 기계 작업 |

# 병렬 인제스트 프로토콜 매핑 (CLAUDE.md)

- **PHASE 1 (fan-out, 논문당 1 서브에이전트)** → 기본 **Sonnet** (`model: sonnet`, `effort: high`). *단, 경계 카테고리이거나 supersession 후보인 논문만 그 논문 한정 Opus.*
- **PHASE 2 (parent finalize: index·commit·qmd)** → **Sonnet**. supersession 배너를 실제로 박을지 **판단**하는 순간만 Opus급 사고.
- **overview 작성** → 항상 **Opus**, 별도 세션.

# Done Criteria

- [x] 작업별 모델 표 확정
- [x] 병렬 프로토콜(PHASE 1/2)에 매핑
- [x] `ingest-paper` 스킬 Step 0에 Opus escalation 분기 추가
- [x] 스킬 Step 4(분류)·Step 6(Why Ingested/supersession)에 escalation 트리거 명시

# Notes / Decisions

- 2026-06-30: **"추출 vs 종합"** 한 축으로 라우팅 고정. "newer ≠ better"와 동일 철학 — 비싼 모델을 전부에 쓰지 않고 판단이 가치를 만드는 지점에만 투입.
- 기존 스킬 Step 0은 "Sonnet 최고등급 vs 현재 모델" 2지선다였음 → 여기에 **escalation 트리거**(경계 카테고리·supersession 후보·overview·한국어 digest·임상 interactive)를 3번째 분기로 추가.
- 2026-06-30: **누락 방지 — Step 3.5(Related-page & supersession lookup) 신설.** escalation 트리거를 Sonnet의 자발적 기억에 의존하면 supersession을 조용히 놓침(탐지기=작업자 사각지대). DOI grep + qmd 관련페이지 검색을 **모델 무관 기계 단계**로 박아, 관련/대체 후보를 *데이터로* 띄운 뒤 escalation을 트리거하도록 변경.

# References

- [[supersession-judgment-at-ingest]]
- `.claude/skills/ingest-paper/SKILL.md`
