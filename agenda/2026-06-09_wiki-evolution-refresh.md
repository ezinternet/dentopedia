---
title: "wiki-evolution 인터랙티브 v3 refresh (2026-06-09 현재기준)"
type: agenda
date: 2026-06-09
status: done
source_wiki:
  - index.md
output_wiki: []
---

# Goal
기존 `interactives/2026-06-04_wiki-evolution-v2.html`를 2026-06-09 현재 실측치로 갱신한 v3 생성.

# Input
- `sources/*.md`, `wiki/**/*.md` 실측 카운트
- git add-date 기반 ingest 타임라인 (05-18 ~ 06-08)

# Output
- `interactives/2026-06-09_wiki-evolution-v3.html` ✅
- `interactives/index.html` 메타 섹션 카드 추가 ✅

# 실측 스냅샷 (2026-06-09)
- papers (sources, 1:1 PDF): 1,198 (v2 06-04 = 1,012, +186)
- overviews: 87 (v2 = 69, +18)
- 전체 wiki 페이지: 1,285 (_lint 9 제외)
- 고근거 (sr+ma 237 + sr 135 + rct 105): 477 (v2 = 383)
- 최근 5년(2021–2026) 비중: 814/1198 ≈ 68%
- 임플란트 외과 축(implants+immediate-implant+sinus-lift+bone-regeneration): 455 ≈ 35%

# Done
- [x] 3-view(timeline/years/cats) 데이터 전부 06-09 실측으로 교체
- [x] 06-05~08 ingest wave(+272 papers, +24 overviews) 타임라인 반영
