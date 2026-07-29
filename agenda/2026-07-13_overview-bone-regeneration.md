---
title: "bone-regeneration 골이식재 선택 매트릭스 overview 합성"
type: agenda
date: 2026-07-13
status: in-progress
owner: 원장
priority: P1
tags: [bone-regeneration, overview, graft-material, synthesis]
source_wiki:
  - wiki/bone-regeneration/zhao-2021-bone-grafts-substitutes-dentistry-review.md
  - wiki/bone-regeneration/depace-2025-bone-regeneration-treatment-strategies-review.md
  - wiki/bone-regeneration/bubalo-2026-bone-substitutes-alveolar-ridge-augmentation.md
  - wiki/bone-regeneration/elgali-2017-guided-bone-regeneration-materials-mechanisms.md
  - wiki/bone-regeneration/meza-mauricio-2022-substitute-autogenous-bone-graft-horizontal.md
  - wiki/bone-regeneration/janjua-2022-autogenous-tooth-bone-grafts-narrative.md
  - wiki/bone-regeneration/ridge-preservation/minetti-2020-alveolar-socket-preservation-autologous-graft.md
  - wiki/bone-regeneration/ridge-preservation/nakajima-2026-tooth-root-graft-alveolar-preservation.md
  - wiki/bone-regeneration/stricker-2021-resorption-retromolar-bone-grafts.md
  - wiki/bone-regeneration/rokn-2011-bone-formation-two-grafting-materials.md
  - wiki/bone-regeneration/elrefaei-2025-3d-printed-scaffolds-ridge-augmentation.md
  - wiki/bone-regeneration/sun-2025-3d-printed-scaffold-bone-defect-repair.md
  - wiki/bone-regeneration/giannotti-2023-autologous-platelet-concentrates-clinical-applications.md
  - wiki/bone-regeneration/tale-2026-simvastatin-guided-bone-regeneration-sr.md
  - wiki/bone-regeneration/ridge-preservation/domic-2023-hyaluronic-acid-tooth-extraction-sr-ma.md
  - wiki/bone-regeneration/raabe-2025-defect-morphology-membrane-fixation-graft.md
  - wiki/bone-regeneration/ahamed-2025-peri-implant-gaps-management-sr.md
output_wiki:
  - wiki/overviews/bone-graft-material-selection-matrix-overview.md
---

# Goal

bone-regeneration 카테고리 미합성 17편을 "골이식재 클래스 선택" 단일 축으로 종합해, 원장이 결손 유형별로 어떤 이식재(자가골·동종골·이종골·합성골·치아유래·3D스캐폴드)와 어떤 보조제(혈소판농축물·심바스타틴·히알루론산)를 고를지 chairside에서 참조할 overview 페이지 1장 생성. category-overflow(2026-07-13) 1위 카테고리 대응.

# Input

위 `source_wiki` 17편. 기존 인접 overview와 역할 분리:
- wiki/overviews/bone-regeneration-protocol-ladder.md — 소켓 벽 수 기반 ARP 결정트리 (본 페이지는 재료 클래스 taxonomy로 상보)
- wiki/overviews/dbbm-bone-substitute-overview.md — DBBM 단일재료 심화 (본 페이지는 클래스 전체 매트릭스)
- wiki/overviews/gbr-barrier-membrane-overview.md — 차폐막 축
- wiki/overviews/vertical-ridge-augmentation-overview.md — 수직증대 술식 축

# Output

- wiki/overviews/bone-graft-material-selection-matrix-overview.md
  - frontmatter에 `agenda: agenda/2026-07-13_overview-bone-regeneration.md` 백링크
  - 한국어 핵심요약 callout(top) + Three-line Summary(EN) + 세줄요약(KR) + English body + 17편 wikilink

# Done Criteria

- [x] 4대 생물학적 특성 매트릭스(골형성/골유도/골전도/골유착) 표 1장
- [x] 결손 유형별 재료 선택 프레임(수평/수직/소켓/peri-implant gap)
- [x] 17편 전부 본문 author-year 인용 + Related Papers wikilink
- [x] 한국어 핵심요약 ~10 bullet callout (top)
- [x] lint/orphan/link 감사 통과
- [x] qmd update+embed 검색 인덱스 반영
