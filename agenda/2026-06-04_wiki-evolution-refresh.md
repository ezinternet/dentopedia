---
title: "llm-wiki Evolution 인터랙티브 갱신 — ingest 타임라인 + 발행연도 + 카테고리 3-view"
type: agenda
date: 2026-06-04
status: done
source_wiki:
  - index.md
---

# Goal
기존 `interactives/2026-05-27_wiki-evolution.html`(05-09~05-27 정적 SVG stacked-area)을 최신 데이터(2026-06-04, 1,012 papers)로 갱신하고, 정적 1-view → 인터랙티브 3-view로 확장.

# Input
- git add-date 일별 누적 (sources/, wiki/overviews/) — 2026-05-18 repo-init seed 350 → 06-04 현재
- wiki frontmatter `year:` 발행연도 히스토그램 (2003–2026)
- 카테고리별 현재 페이지 수

# Output
- interactives/2026-06-04_wiki-evolution-v2.html
  - View 1: Ingest Evolution (papers + overviews 누적 곡선, hover tooltip, 마일스톤 마커)
  - View 2: Publication-Year Coverage (발행연도 막대 + 누적선)
  - View 3: Category Composition (현재 스냅샷 가로 막대)

# Done 기준
- 단일 HTML 파일, 외부 의존 없음(기존 하우스 스타일 유지: 크림 테마, hand-rolled SVG)
- 탭 전환 + hover 인터랙션 동작
- operations-lint 통과 (agenda 백링크 존재)
