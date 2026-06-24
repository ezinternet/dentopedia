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

골밀도화 (Osseodensification, OD) 버 두 제품 — Densah(Versah, CCW 역회전 압밀) vs HaeNaem(해냄, CW 정회전 압밀) — 의 차이·근거강도·적응증을 chairside에서 즉시 비교할 수 있는 인터랙티브 1장으로 정리. 특히 두 킷의 회전방향이 반대라는 모터 셋업 함정과, head-to-head 동등성 주장의 근거가 없다(대표 논문이 단일군·비교군 없음 + 2024-11-21 정정 후 이후 철회/RETRACTED)는 점을 명시.

# Input

- wiki/sinus-lift/transcrestal/changrani-2024-haenaem-zero-bone-loss-indirect-sinus-lift.md — HaeNaem Zero Bone Loss Kit CW-OD 간접거상 단일군 연구; 2024-11-21 정정 후 **철회(RETRACTED)** — 본문유지+RETRACTED 배너로 정책예외 보관
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
- [x] head-to-head 동등성 근거 부재 명시 — 대표 논문(Changrani 2024, Cureus 10.7759/cureus.73130)은 단일군이며 2024-11-21 정정 후 **철회(RETRACTED)** 됨
- [x] 인터랙티브 frontmatter에 source_wiki / agenda 백링크
- [x] operations-lint 통과

# Notes / Decisions

- 두 킷의 densifying 회전방향이 **반대**(Densah=CCW, HaeNaem=CW)라는 점이 임상 안전상 핵심 — Densah reverse 프로토콜을 해냄에 그대로 적용 금지.
- **철회 처리 (2026-06-24):** `changrani-2024` (Cureus, DOI 10.7759/cureus.73130)는 2024-11-21 정정(Correction, cureus.c200 — 결론부 인용 1건 추가) 후 **이후 철회(RETRACTED)** 됨 (사용자/maintainer 확인). 로컬 PDF는 철회 이전 스냅샷이라 정정까지만 찍혀 있어 Rule #1(무웹검색)로는 정정만 확인 가능했음 — 한때 'PMID 39575356 ↔ 이 논문' 매핑이 불확실해 '철회 아님(정정)'으로 잠시 오기재했으나, 사용자 확인으로 철회 확정 후 되돌림.
- **보관 형태 결정:** CLAUDE.md 철회정책은 원칙상 'RETRACTED 스텁'만 허용하나, HaeNaem 유일 임상 데이터라는 점을 고려해 **전체 본문 유지 + 상단 `[!warning] RETRACTED` 배너**의 정책 예외로 보관(사용자 결정). wiki/sources 페이지에 배너 + `retracted` 태그, 인바운드 인용(osseodensification-clinical-applications, sinus-lift-isq-loading-timing 두 overview + kim-2019 페이지/소스)에 '(retracted/철회됨 — 인용 금지)' 주석. bone-regeneration-protocol-ladder는 changrani 미인용(kim-2019 bone-collector 특허만 참조)이라 해당 없음.
