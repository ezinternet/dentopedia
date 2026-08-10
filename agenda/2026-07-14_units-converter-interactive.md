---
title: "치과 단위 변환기 + 임계값 조회 chairside 도구"
type: agenda
date: 2026-07-14
status: done
owner: 원장
priority: P2
tags: [units, interactive, chairside, converter, threshold]
source_wiki:
  - wiki/overviews/dental-research-units-reference-overview.md
---

# Goal

치과 논문·차트에서 마주치는 단위를 chairside(iPad)에서 즉시 ① 변환하고 ② 그 단위의 정상/성공 임계값을 조회할 수 있는 단일 HTML 도구. 근거는 단위 레퍼런스 오버뷰 1편.

# Input

- wiki/overviews/dental-research-units-reference-overview.md — 5계열 단위·빈도·임계값의 단일 출처(thesis + 표)

# Output

- interactives/2026-07-14_units-converter.html — 단위 변환기(×1000 3쌍 + MPa=N/mm²) + 단위별 임계값 조회 카드

산출물 frontmatter에 `agenda: agenda/2026-07-14_units-converter-interactive.md` 백링크.

# Done Criteria

- [x] 변환기: mm↔µm, MPa↔GPa, mSv↔µSv, MPa↔N/mm² 실시간 계산
- [x] 임계값 조회: 단위 선택 → 임상 맥락별 정상/성공 임계값 카드 (오버뷰 inline 값)
- [x] 단일 HTML, 외부 CDN 0, 라이트/다크 테마, iPad 반응형
- [x] source_wiki 백링크 = 오버뷰 1편
