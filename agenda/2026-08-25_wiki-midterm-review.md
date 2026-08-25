---
title: "위키 중간평가 — 개설 99일차 (2026-05-18 → 2026-08-25)"
type: agenda
date: 2026-08-25
status: in-progress
owner: 원장
priority: P1
tags: [meta, audit, midterm-review, knowledge-compounding, coverage]
source_wiki:
  - wiki/overviews/implants-isq-stability-ladder.md
  - wiki/overviews/immediate-implant-decision-ladder.md
  - wiki/overviews/periodontics-treatment-ladder.md
  - wiki/overviews/bone-regeneration-protocol-ladder.md
  - wiki/overviews/oral-medicine-decision-ladder.md
---

# Goal

개설 99일차 위키의 상태를 실측해, 다음 국면(확장 → 활용)의 우선순위를 하나로 못박는다. 결론: **인제스트 감속은 문제가 아니며, 손볼 곳은 종합→산출물 전환율(14.8%)과 도메인 편중(임플란트 35%)이다.**

# Input

- `logs/2026-08-25_*` — 당일 00:11 생성 감사 로그 16종 (synthesis-backlog · output-coverage · recall-coverage · link-integrity · supersession · relations · retraction · volatility · overview-catalogue · overview-coverage-lint · overview-thesis-staleness · category-overflow · contradiction-candidates · interactive-staleness · ingest-rationale-lint)
- `logs/2026-08-14_doi-duplicate-check.log` — 최신 DOI 중복 로그
- `git log` 실측 — 월별·주별 신규 sources/overviews, 커밋 카데니, 최초 커밋일
- `qmd status` — 인덱스 신선도·고아 벡터
- 파일시스템 실측 — 카테고리별 페이지 수, evidence_level 분포, 페이지 분량, 세줄요약 준수율

# 중간평가 결과

## 1. 규모 — 99일에 3,049편

| 지표 | 값 |
|---|---|
| sources | 3,049편 |
| wiki 페이지 | 3,459 (논문 ~3,052 + overview 277 + 네비 허브 120 + `_lint`/`_meta` 10) |
| PDF 원본 | 1,975개 / 3.5GB (PMC 전문텍스트 우선 정책 반영 — sources의 65%만 PDF 보유) |
| 커밋 | 9,466 |
| 일평균 인제스트 | 30.8편/일 |

overview 평균 23KB, 논문 페이지 평균 5.9KB. overview가 얇은 요약이 아니라 실제 종합 문서다.

## 2. 무결성 — 사실상 만점

3천 페이지 규모에서 이 숫자는 드물다. **이 위키의 최대 강점.**

- 본문 위키링크 20,692개 중 깨짐 **0**
- typed 엣지 2,941개 중 dangling **0** · self-ref **0**
- superseded 44건 — 깨진 링크 0, 배너 누락 0, 필드↔배너 불일치 0, transitivity stale 0
- 철회 논문 4페이지 — 구조 검사 전부 통과 (wiki/ + sources/ 두 티어)
- overview 277편 → 카탈로그 1:1 등재 276/276, 누락 0, dangling 0
- ingest-rationale 2,372건 검사, 에러 **0**
- 이중언어 세줄요약 3,448/3,459 · overview 한국어 핵심요약 **277/277**
- overview thesis staleness — 276편 fresh(<90일), WARN 0, INFO 0
- overview 본문 커버리지 — WARN(<40%) 0, INFO 1건(`mandibular-third-molar-management-overview` 57.1%)
- interactive 도구 63개 전부 `OK` — STALE 0, BROKEN 0

**감사 오탐 1건 확인**: link-integrity의 "index 미등재 119건"은 결함이 아니다. 전부 2026-08-11에 만든 `source: navigation` 허브 페이지(총 120개)다. 알려진 오탐 클래스로 처리할 것 — 감사 자체를 고치거나 `INDEX_EXEMPT` 계열로 면제하는 판단이 필요.

## 3. 속도 — 피크 대비 89% 감소 (문제 아님)

주별 신규 sources:

```
W25 308 → W26 439(피크) → W27 177 → W28 243 → W29 106
→ W30 101 → W31 68 → W32 54 → W33 45 → W34 47
```

overview도 같은 곡선 — W26 33편 → W33 2편, W34 7편. 월별 6월 1,356 → 7월 640 → 8월 181편.

**방치가 아니다.** 최근 14일 중 14일 모두 커밋이 있고 8/15엔 227커밋(대규모 정비), 8/24엔 90커밋. 인제스트가 줄어든 자리를 갱신·통합·정비가 채우고 있다. 확장 국면 → 심화 국면 전환으로 읽는 것이 데이터에 맞다. **감속을 되돌리려는 조치는 하지 않는다.**

## 4. 진짜 병목 — 파이프라인 비대칭

| 방향 | 커버리지 |
|---|---|
| 입력 → 종합 (synthesis) | **99.0%** (3,018/3,049), stale 0건 |
| 종합 → 산출물 (output) | **14.8%** (41/277) |
| 종합 → 기억 (recall) | **17.3%** (48/277) |

들어오는 쪽은 거의 완벽한데 나가는 쪽이 15%다. 그리고 미전환 목록 맨 위가 하필 **가장 많이 참조되는 허브**:

```
inbound 39  implants-isq-stability-ladder
inbound 32  immediate-implant-decision-ladder
inbound 30  periodontics-treatment-ladder
inbound 28  bone-regeneration-protocol-ladder
inbound 28  oral-medicine-decision-ladder
```

위키에서 가장 중심에 있는 결론 5개가 슬라이드·인터랙티브·강의 어디에도 안 꺼내져 있다. **지금 한 편을 산출물로 전환하는 값이 새 논문 47편 인제스트보다 크다.**

## 5. 최종목적(진단·치료계획 생성) 대비 갭

의사결정 골격은 있다 — 사다리·결정트리형 overview 39편/277 (14%).

**문제는 도메인 편중과 결손이다.**

- 임플란트 4축(implants · immediate-implant · sinus-lift · bone-regeneration)이 논문 페이지의 **35.0%** (1,111/3,172)
- **폴더 자체가 없는 도메인**: 소아치과, 고정성 보철(크라운·브릿지), 국소의치(RPD), 구강병리·구강암
- **얇은 도메인**: 방사선 58, 교합 65, 우식 49, 총의치 51

최종목적이 "교합상태·치아상태·파노라마 → 치료계획"이라면, 파노라마 판독 근거가 58편이고 **"발치 후 무엇으로 수복하나" 분기에서 크라운·브릿지·RPD 근거가 0편**이다. 임플란트로 가는 가지만 두껍고 나머지 가지가 비어 있어, 지금 치료계획을 뽑으면 **구조적으로 임플란트 편향**이 나온다.

## 6. 노후화 부채

- decay 후보 **299편** (5년↑ 고근거 sr+ma/sr/rct 중 미대체)
- 상위: implants 52편(중앙 6.9년) · immediate-implant 31편(8.6년) · periodontics 27편(7.6년) · **drug 21편(10.1년)**
- 허브가 낡은 게 문제 — sinus-lift decay 논문 중 maxInbound 29, immediate-implant 22
- volatility 적색 4편 + **철회 하드 플래그 4편** (`changrani-2024`가 overview 3편, `panagioti-2018`이 1편 오염)

`decay-review-2026-06-21` 메모는 "~2027까지 재검토 말 것"이지만 그건 당시 후보 기준이다. **drug 중앙 10.1년은 그 결정과 별개로 볼 값.**

## 7. 미해결 잔여

- DOI 중복 `gupta-2019` 2 stem — 2026-08-14부터 미해결
- relations off-vocab 17건 — `extended-by` 4 · `related` 4 · `complements` 4 · `synthesizes` 3
- contradiction Tier 1 2건 (`naughton-2023`→`kastel-2019`, `pignatelli-2020`→`elzein-2021`)
- category-overflow 후보 3개 — implants/isq 10편 · drug/analgesics 5편 · drug/mronj 5편
- CIRCULAR reinforces 1건

# Output

## 즉시 (2026-08-25 실행 완료)

- [x] `qmd update` — 인덱스가 08-24 18:59에 멈춰 있었고 당일 wiki md 5개가 커밋된 상태였다 (CLAUDE.md가 경고한 재색인 누락 창이 열려 있었음)
- [x] `qmd embed` — "All content hashes already have embeddings" 확인까지
- [x] `qmd cleanup` — 고아 벡터 266개(1%) 제거

## 후속 (미착수)

- [ ] **허브 overview 상위 5편 → 산출물 전환** (최우선). `implants-isq-stability-ladder` 1편부터. agenda 선행 필수 (OPERATIONS.md §1 hard rule)
- [ ] 같은 5편에 recall 스펙 3문항씩 동반 (retention 축)
- [ ] 결손 도메인 3개 최소 종합 확보 — 크라운·브릿지 / RPD / 소아치과, 각 15~20편
- [ ] CLAUDE.md 자기서술 교정 — 2곳의 "20 audits" → **21** (`daily-audit.py` 실측 21개, AUDITS.md도 21)
- [ ] link-integrity 네비 허브 오탐 119건 처리 방침 결정
- [ ] `gupta-2019` DOI 중복 병합
- [ ] relations off-vocab 17건 정규 vocab으로 교정
- [ ] drug 카테고리 decay 21편(중앙 10.1년) 우선 triage

# Done Criteria

- [x] 감사 로그 16종 + git + qmd + 파일시스템 실측으로 수치 확보 (추정치 없음)
- [x] 즉시 조치 2건(①인덱스 재색인 ②고아 벡터) 실행 및 전후 비교
- [ ] 후속 항목 중 최우선 1건(허브 overview 산출물 전환) agenda 생성

# Notes / Decisions

- 2026-08-25: **인제스트 감속을 문제로 규정하지 않기로 결정.** 커밋 카데니가 유지되고(14/14일) 정비 작업이 그 자리를 채우고 있어, 속도를 되돌리는 조치는 오히려 활용 국면 전환을 방해한다. *signal, not gate* 원칙과 동일한 논리 — 인제스트 수치는 할당량이 아니다.
- 2026-08-25: 다음 국면 우선순위를 **"활용률 > 도메인 균형 > 노후화"** 순으로 고정. 노후화 299편은 숫자가 크지만 허브 오염(maxInbound 20~29)만 골라 처리하면 실질 리스크가 덮인다.
- 2026-08-25: 감사 전체 재실행 소요가 AUDITS.md의 "~15분"에 가깝게 관측됨 (20분+ 관측). `daily-audit-rationale-lint-slow` 메모의 "전체 ~3분(2026-07-17 실측)"은 sources 3,049편 규모에서 더 이상 유효하지 않을 가능성 — 재측정 필요.

# References

- `AUDITS.md` — 21개 감사 표·억제 조건
- `OPERATIONS.md` §1 routing, §3 frontmatter cross-link
- `wiki/_meta/categories.md` — 카테고리 라우팅 단일 출처 (결손 도메인 신설 시 여기부터)
- [[note-meeting/2026-07-11_wiki-team-feedback-system]]
