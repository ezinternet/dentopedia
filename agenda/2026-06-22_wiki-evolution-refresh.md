---
title: "wiki-evolution 인터랙티브 v4 refresh (2026-06-22 현재기준)"
type: agenda
date: 2026-06-22
status: done
source_wiki:
  - index.md
output_wiki: []
---

# Goal
기존 `interactives/2026-06-09_wiki-evolution-v3.html`를 2026-06-22 현재 실측치로 갱신한 v4 생성. v3 대비 **4번째 view(System Evolution — 4단계 탈피 + 스크립트 출생 타임라인)** 추가.

# Input
- `sources/*.md`, `wiki/**/*.md` 실측 카운트
- git add-date / first-commit-date 기반 ingest·script 타임라인 (05-18 ~ 06-22)
- `scripts/*.py` 최초 커밋일

# Output
- `interactives/2026-06-22_wiki-evolution-v4.html`
- `interactives/index.html` 메타 섹션 카드 추가

# 실측 스냅샷 (2026-06-22)
- papers (sources, 1:1 artifact = PDF 1,586 + PubMed-text 202): **1,788** (v3 06-09 = 1,198, +590)
- overviews: **138** (v3 = 87, +51)
- 전체 wiki 페이지(_lint 제외): **1,928** (v3 = 1,285)
- 고근거 (sr+ma 393 + sr 225 + rct 177): **795** (v3 = 477)
- 최근 5년(2021–2026) 비중: 1,256/1,788 ≈ **70%**
- 임플란트 외과 축(implants 324 + immediate-implant 126 + sinus-lift 109 + bone-regen 79): 638 ≈ **33%**
- 총 커밋 3,395 · 최근 3일(6/20·21·22) = 412·244·775

# 4단계 탈피 (View ④)
- ① 부트스트랩 (5/18–24): 3-tier 적재 + day-1 lint/orphan-check
- ② 자가감사 생명체 (5/31): daily-audit 외 8개 audit script 동시 출생, overview 20→58
- ③ 출력공장 (6/02–08): interactives, build-interactives-index
- ④ 산업화·자동감시 (6/12–22): ingest-one(병렬 finalize), build-overviews-map, fetch-oa+sweep_state

# Done
- [x] 3-view(timeline/years/cats) 데이터 06-22 실측으로 교체
- [x] View ④ System Evolution 신규 추가
- [x] x축 06-22까지 연장, 06-09~22 ingest wave(+590 papers, +51 overview) 반영
