---
title: "완전 가이드 수술 로딩 결정 트리 — Ko 2021 경고 내장 인터랙티브"
type: agenda
date: 2026-07-30
status: done
owner: 원장
source_wiki:
  - wiki/implants/loading-protocol/ko-2021-immediate-loading-protocols-increase-risk.md
  - wiki/implants/loading-protocol/gallucci-2018-implant-placement-loading-protocols-partially.md
  - wiki/implants/loading-protocol/esposito-2013-loading-times-dental-implants-cochrane.md
  - wiki/implants/full-arch/kern-2018-single-implants-edentulous-mandible-immediate.md
  - wiki/overviews/implant-loading-protocol-prosthesis-type-overview.md
tags: [immediate-loading, delayed-loading, fully-guided-surgery, ISQ, insertion-torque, decision-tree, interactive, chairside, Ko-2021]
---

# Agenda: 완전 가이드 수술 로딩 결정 트리

> **소급 작성 (retroactive, 2026-07-31)**: 이 인터랙티브는 2026-07-30에 먼저 만들어졌고(커밋 `af3d9b1`), agenda 명세가 누락돼 `operations-lint`가 `MISSING status` · `MISSING agenda`로 블로킹했다. 이 파일은 그 산출물을 규정된 양방향 cross-link 구조에 소급 편입하기 위한 명세다. 아래 Goal·Input·Output은 **실제로 만들어진 결과물과 커밋 기록에서 복원**한 것이며, 새로 기획한 내용이 아니다.

## Goal

완전 가이드 수술 (Fully Guided Surgery) 로 식립한 증례에서 **즉시로딩 (Immediate Loading, IL) 을 걸 것인가**를 체어사이드에서 판단할 수 있게 한다.

이 도구가 존재하는 이유는 단 하나의 반직관적 사실 때문이다 — 가이드 수술은 정확도를 높이지만 **즉시로딩의 실패 위험을 낮춰주지 않는다**. Ko 2021 RCT는 식립토크 (Insertion Torque, IT) >20 Ncm + 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) >65 라는 통상적 IL 적격 기준을 **충족한 증례에서도** 1년 임플란트 생존율이 83.4% (ITT) 에 그쳤고, 같은 시험의 지연로딩군은 100%였다 (p<0.01, n=72 / 187 임플란트). 안정성 수치만 보고 IL을 거는 습관이 가이드 증례에서 특히 위험하다는 뜻이다.

따라서 목표는 "안정성 수치 → 로딩 결정" 이라는 단순 매핑을 깨고, **수술 접근법을 결정 변수로 승격**시킨 분기를 제공하는 것이다.

## Input

`wiki/implants/loading-protocol/` 의 로딩 프로토콜 근거 4편 + 종합 1편.

- `wiki/implants/loading-protocol/ko-2021-immediate-loading-protocols-increase-risk.md` — **중심 근거**. 가이드 수술 맥락에서 IL vs 지연로딩(DL)을 직접 비교한 RCT (n=72, 187 임플란트, 1년). IL 생존 83.4% ITT / 90.2% PP vs DL 100%, 모두 p<0.01. 변연골소실 (Marginal Bone Loss, MBL) 은 양군 <0.1 mm 로 차이 없음 — 실패는 골 반응이 아니라 조기 탈락 형태로 나타난다. IL 배정 환자의 약 11%(4명/7 임플란트)가 IT·ISQ 기준 미달로 IL을 못 받았다는 사실도 "가이드가 1차 안정성을 보장하지 않는다"는 근거로 도구에 반영.
- `wiki/implants/loading-protocol/gallucci-2018-implant-placement-loading-protocols-partially.md` — 식립시점 × 로딩 조합 9종의 ITI 분류 틀 (Type 1A~4C) 과 조합별 가중생존율. **식립과 로딩을 분리해 판단하지 말라**는 원칙이 결정 트리의 1·2단계 분리 구조 근거.
- `wiki/implants/loading-protocol/esposito-2013-loading-times-dental-implants-cochrane.md` — Cochrane SR+MA (26 RCT, n=1,217). 즉시/조기/통상 로딩 간 보철실패·임플란트실패·MBL 임상적 유의차 없음, **단 IT ≥35 Ncm 전제**. 도구의 IT 임계선(≥35 Ncm)의 출처이자, Ko 2021과의 긴장을 만드는 대조축.
- `wiki/implants/full-arch/kern-2018-single-implants-edentulous-mandible-immediate.md` — 하악 정중부 단일 임플란트 오버덴처 IL vs DL 비열등성 RCT (24개월). **비열등성 미확인**(IL 조기실패 9건 vs DL 1건), 실패가 초기 치유기에 몰림 → 1차 안정성이 핵심 조절인자. 보철 유형이 결정에 들어가야 하는 근거.
- `wiki/overviews/implant-loading-protocol-prosthesis-type-overview.md` — 보철유형별 로딩 프로토콜 종합. 1단계(보철 유형) 분기의 상위 틀.

## Output

- `interactives/2026-07-30_guided-surgery-loading-decision-tree.html` — 4단계 결정 위저드

**설계**: `보철 유형 → 수술 접근법 → 안정성 (IT / ISQ) → 판정`

- 수술 접근법에서 **가이드 수술을 고르면 Ko 2021 경고가 카드 안에 인라인으로 뜬다** — 사용자가 안정성 수치를 입력하기 *전에* 위험을 먼저 보게 하는 배치.
- ISQ는 **선택 입력** (미측정 증례를 배제하지 않기 위함). IT만으로도 판정이 나온다.
- 판정 색상: 가이드 수술 + IT ≥35 / ISQ ≥70 인 경우에도 초록이 아니라 **앰버(주의)** — Ko 2021의 "기준 충족에도 83.4%"를 색으로 번역한 것. 안정성이 좋아도 가이드 증례에서는 자동 승인하지 않는다는 것이 이 도구의 핵심 주장.
- IT ≥20 Ncm + ISQ ≥65 미달 시 즉시로딩 시도 자체를 권고하지 않고 지연로딩(3개월) + 6~8주 ISQ 재측정 경로로 보낸다.
- 모든 판정에 근거 논문(저자-연도)이 함께 표시된다.

## Done 기준

- [x] HTML이 `interactives/` 에 존재하고 `category` 프론트매터를 가진다 (`implant-stability`)
- [x] 도구가 인용하는 모든 저자-연도가 `source_wiki` 의 실존 위키 페이지로 추적된다
- [x] 밝은 배경 고정 (위키 인터랙티브 정책)
- [x] `interactives/index.html` 카드에 반영 (빌드 스크립트가 생성)
- [x] HTML frontmatter 에 `status:` · `agenda:` 백링크 존재
- [x] `operations-lint` 통과

## Notes / Decisions

- 2026-07-30: 다크모드 제거 (커밋 `81c4299`). 위키 인터랙티브는 밝은 배경 고정이 정책 — 개별 도구가 테마를 갖지 않는다.
- 2026-07-30: `category` 를 `implant-stability` 로 정정 (커밋 `eb98638`). 도구의 판정 축이 로딩 시점이 아니라 **1차 안정성 측정치**이므로 안정성 카테고리로 귀속.
- 2026-07-31: 소급 agenda 작성 중 `source_wiki` 의 `kern-2018` 경로 오류 발견 — `wiki/implants/loading-protocol/` 로 적혀 있었으나 실제 위치는 `wiki/implants/full-arch/`. HTML 과 이 agenda 양쪽에서 정정.
- **미해결 / 재검토 후보**: Ko 2021(가이드 증례 IL 위험)과 Esposito 2013 Cochrane(IT ≥35면 IL 비열등)은 서로 다른 방향을 가리킨다. 현재 도구는 가이드 여부를 상위 변수로 두어 Ko 2021을 우선시키는 방식으로 봉합했으나, 이 우선순위는 단일 RCT(n=72, 단일기관)에 기대고 있다. 가이드 수술 IL을 다룬 후속 RCT가 인제스트되면 앰버 판정 기준을 재검토할 것.

## References

- [[overviews/implant-loading-protocol-prosthesis-type-overview]]
- [[implants/loading-protocol/ko-2021-immediate-loading-protocols-increase-risk]]
- 커밋: `af3d9b1` (최초 생성) · `81c4299` (다크모드 제거) · `eb98638` (category 정정)
