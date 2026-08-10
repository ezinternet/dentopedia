---
title: "GCF 바이오마커 매트릭스 chairside 결정도구"
type: agenda
date: 2026-07-03
status: done
owner: 원장
priority: P2
tags: [gcf, biomarkers, interactive, periodontics, orthodontics]
source_wiki:
  - wiki/overviews/gingival-crevicular-fluid-biomarker-diagnostics-overview.md
  - wiki/periodontics/donertas-2026-gbt-subgingival-debridement-gcf-biomarkers.md
  - wiki/periodontics/cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal.md
  - wiki/periodontics/fadli-2024-oral-gingival-crevicular-fluid-jawbone-turnover.md
  - wiki/periodontics/foroughi-2025-bridging-oral-systemic-health-periodontal.md
  - wiki/orthodontics/bud-2024-gingival-crevicular-fluid-biomarkers-orthodontic.md
---

# Goal

치은열구액(Gingival Crevicular Fluid, GCF) 바이오마커 종합 overview를 chairside에서 바로 쓸 수 있는 인터랙티브 결정도구로 확장. "무엇을 감시하려는가(치주 진단·치료반응 / 교정 치아이동 / 골대사·전신)"를 고르면 해당 마커 패널·읽는 의미·채취법·주의점을 돌려주고, 전체 바이오마커 매트릭스와 시료(GCF vs 타액 vs 혈액) 선택 로직을 함께 제공.

# Input

- wiki/overviews/gingival-crevicular-fluid-biomarker-diagnostics-overview.md — 1차 입력(두 축·매트릭스·시료대비·기술로드맵)
- wiki/periodontics/donertas-2026-gbt-subgingival-debridement-gcf-biomarkers.md — 치료반응 RCT(IL-1β)
- wiki/periodontics/cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal.md — miRNA 진단(AUC>0.8)
- wiki/periodontics/fadli-2024-oral-gingival-crevicular-fluid-jawbone-turnover.md — 골대사 패널·시료 중첩
- wiki/periodontics/foroughi-2025-bridging-oral-systemic-health-periodontal.md — 시료대비·labside↔chairside 기술
- wiki/orthodontics/bud-2024-gingival-crevicular-fluid-biomarkers-orthodontic.md — OTM 마커·압박/긴장·타이밍·스트립 채취

# Output

- interactives/2026-07-03_gcf-biomarker-matrix.html

각 산출물 frontmatter에 `agenda: agenda/2026-07-03_gcf-biomarker-interactive.md` 백링크·`source_wiki` 박음.

# Done Criteria

- [x] 목적 3종(치주 진단·치료반응 / 교정 OTM / 골대사·전신) 선택 → 마커 패널·채취·주의점 반환
- [x] 바이오마커 매트릭스 표(마커 × 기능계층 × 근거논문 × 읽는 의미) — overview 표 반영
- [x] 시료 선택(GCF vs 타액 vs 혈액) 로직
- [x] 핵심 수치 inline(AUC>0.8 miRNA, RANKL:OPG, MMP-9 4h, donertas p<0.05) + 출처 표기
- [x] "연구·모니터링 도구지 독립 진단검사 아님" 한계 명시
- [x] frontmatter에 source_wiki / agenda 백링크
- [x] interactives-index는 배포 시 자동 재생성(build-interactives-index.py)

# Notes / Decisions

- 2026-07-03: Class B(임상 결정 도구) — 수치가 특정 논문에서 추출된 임상 임계값이므로 배포 스크립트가 재작성하지 않음. source_wiki가 도구보다 최신이면 interactive-staleness.py가 STALE 신호.
- 모든 수치는 overview(및 그 5개 근거 페이지)에서만 인용 — Rule #1 준수, 신규 수치 생성 없음.

# References

- [[wiki/overviews/gingival-crevicular-fluid-biomarker-diagnostics-overview]]
- [[wiki/overviews/saliva-diagnostics-and-salivary-gland-dysfunction-overview]]
