---
title: "llm-wiki 누적 성장 곡선 시각화"
type: agenda
date: 2026-05-26
status: done
owner: 원장
priority: P3
tags: [meta, audit, visualization, growth-curve]
output_wiki:
  - index.md
---

# Goal

llm-wiki 18일간 (2026-05-09 → 2026-05-26)의 폴더별 파일 누적 곡선을 stacked area chart로 시각화. 사용자가 본 외부 인포그래픽 패턴(한 달치 누적 곡선 + milestone dot)을 우리 wiki에 적용해 진화 궤적을 한 장으로 가시화한다.

# Input

- file mtime 데이터 (git log가 2026-05-18부터라 mtime을 proxy로 사용)
- 카테고리 5분류:
  1. Papers · sources (papers/*.pdf + sources/*.md)
  2. 구조 · overviews (wiki/overviews/*.md)
  3. Wiki 본문 (wiki/**/*.md, overviews 제외)
  4. 룰 · OPS (CLAUDE.md, SOP.md, index.md, agenda/, note-meeting/, scripts/, logs/)
  5. 분석·시각화 (interactives/, slides/, peer-review/)

# Output

- `interactives/2026-05-26_wiki-growth-curve.html` — stacked area chart, 단일 HTML, 외부 의존 없음
- milestone 6개 표시: 2026-05-09(첫 진입), 05-13(대량 ingest), 05-19(OPS 첫 진입), 05-23(룰·SOP 도입), 05-25(산출물 5건), 05-26(logs 활성화)

# Done Criteria

- [x] 5색 stacked area (사용자 이미지 톤 재현)
- [x] x축 일자, 상단 milestone dot + 점선 가이드
- [x] 하단 범례 (5 카테고리)
- [x] 단일 HTML 파일, CDN 의존 없음
- [x] 본문 아래 "읽는 법 + 사용자 이미지와 차이" 해설

# Notes / Decisions

- 2026-05-26: git log가 2026-05-18부터라 mtime 사용. 그래서 5/18 이전 ingest 파일도 mtime이 보존되어 곡선이 그 이전부터 그려짐. 진짜 ingest 일자는 아니지만 운영 timeline의 충분한 proxy.
- 2026-05-26: Papers·sources가 1492/2295 (65%)로 압도적 비중. 사용자 이미지보다 papers heavy. 향후 OPS·산출물 비중 증가 추적 지표로 본 차트 정기 갱신 가능.
- 본 작업은 operations 체인 health check의 일환 — 같은 세션에서 logs/ 활성화 + lint 통과 작업의 연속.

# References

- [[agenda/2026-05-25_q2-clinic-sop-dbbm-isq]] — 같은 세션 다른 작업
- [[agenda/2026-05-25_osseodensification-whole-picture]] — 같은 세션 다른 작업
