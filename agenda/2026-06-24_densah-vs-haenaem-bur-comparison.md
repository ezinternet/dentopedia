---
title: "Densah(Versah) vs HaeNaem(해냄) 골밀도화 버 임상 비교 인터랙티브"
type: agenda
date: 2026-06-24
status: done
owner: 원장
priority: P2
tags: [osseodensification, densah, haenaem, versah, bur-comparison, interactive]
source_wiki:
  - wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift.md
  - wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric.md
  - wiki/implants/soldatos-2024-temperature-changes-osseodensification-cadaver-tibiae-cw-ccw.md
  - wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability.md
  - wiki/implants/gaspar-2022-implant-stability-osseodensification-conventional-sr-ma.md
  - wiki/implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr.md
  - wiki/implants/versah-protocols/versah-densah-sinus-lift-i-protocol-rbh-6mm-minimum.md
  - wiki/overviews/osseodensification-clinical-applications.md
output_wiki:
  - interactives/densah-vs-haenaem-bur-comparison.html
---

# Goal

골밀도화 (Osseodensification, OD) 버 두 제품 — Densah(Versah, CCW 역회전 압밀) vs HaeNaem(해냄, CW 정회전 압밀) — 의 차이·근거강도·적응증을 chairside에서 즉시 비교할 수 있는 인터랙티브 1장으로 정리. 특히 두 킷의 회전방향이 반대라는 모터 셋업 함정과, head-to-head 동등성 주장의 근거가 약하다(대표 비교 논문 철회)는 점을 명시.

# Input

- wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift.md — HaeNaem Zero Bone Loss Kit CW-OD 간접거상 단일군 연구(본문이 인용한 head-to-head 근거 출처; 철회 이슈)
- wiki/implants/versah-protocols/rittipakorn-2025-clockwise-osseodensification-primary-stability-cadaveric.md — CW 골밀도화 1차 안정성 cadaveric 근거
- wiki/implants/soldatos-2024-temperature-changes-osseodensification-cadaver-tibiae-cw-ccw.md — CW vs CCW 회전방향에 따른 발열 차이
- wiki/implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability.md — Densah(Versah) OD 원리 원전
- wiki/implants/gaspar-2022-implant-stability-osseodensification-conventional-sr-ma.md — OD vs 통상 드릴 안정성 SR+MA(근거강도)
- wiki/implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr.md — OD 대안 술식 SR(근거강도)
- wiki/implants/versah-protocols/versah-densah-sinus-lift-i-protocol-rbh-6mm-minimum.md — Densah 경치조골 상악동거상 프로토콜(적응증)
- wiki/overviews/osseodensification-clinical-applications.md — OD 임상 적용 종합

# Output

- interactives/densah-vs-haenaem-bur-comparison.html

산출물 frontmatter에 `agenda: agenda/2026-06-24_densah-vs-haenaem-bur-comparison.md` 백링크 + 위 source_wiki 박음.

# Done Criteria

- [x] 항목별 비교 표(개발·유통/회전방향/형상/재질/적응증/근거/가격)
- [x] 장단점 + 의사결정 분기(Densah / HaeNaem / 무관(D1) / 공통전제)
- [x] 근거강도 등급 라벨(근거강함 / 합의수준 / claude해석 / 추정) 명시
- [x] head-to-head 비교 논문 철회 경고 명시(PMID 39575356)
- [x] 인터랙티브 frontmatter에 source_wiki / agenda 백링크
- [x] operations-lint 통과

# Notes / Decisions

- 두 킷의 densifying 회전방향이 **반대**(Densah=CCW, HaeNaem=CW)라는 점이 임상 안전상 핵심 — Densah reverse 프로토콜을 해냄에 그대로 적용 금지.
- `changrani-2024` 페이지가 인용한 HaeNaem head-to-head 효능 논문(PMID 39575356)은 **철회(Retraction)** 됨. 해당 wiki 페이지가 retraction marker 없이 일반 페이지로 존재하면 retraction 정책 위반 — 별도 점검 필요(이 agenda 범위 밖).
