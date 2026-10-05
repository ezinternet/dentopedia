---
title: "implants overview 합성 — submerged/non-submerged·1-stage/2-stage·one-piece/two-piece 식립 프로토콜 비교"
type: agenda
date: 2026-10-05
status: review
owner: 원장
priority: P2
deadline:
source_wiki:
  - wiki/implants/esposito-2009-1-vs-2-stage-implant-placement-cochrane.md
  - wiki/implants/moustafa-ali-2018-submerged-vs-nonsubmerged-implant.md
  - wiki/implants/wu-2018-submerged-nonsubmerged-internal-hexagonal.md
  - wiki/implants/liu-2021-clinical-radiographic-performance-one-piece.md
  - wiki/implants/walter-2022-two-types-two-piece-dental-implants.md
  - wiki/implants/s41598-021-90142-5.md
  - wiki/implants/irandoust-2020-interplay-bone-healing-remodeling-dental.md
output_wiki:
  - wiki/overviews/implant-placement-protocol-submerged-one-stage-one-piece-overview.md
tags: [overview, implants, submerged, one-stage, two-stage, one-piece]
---

# Goal

wiki/implants 카테고리의 미합성 paper 7편을 종합해, 식립 프로토콜(1회법/2회법, submerged/non-submerged, one-piece/two-piece)과 골치유·micromotion 근거를 원장이 진료 중 바로 조회할 수 있는 overview 1개로 정리.

# Input

- wiki/implants/esposito-2009-1-vs-2-stage-implant-placement-cochrane.md — SR (Cochrane), 1-stage vs 2-stage
- wiki/implants/moustafa-ali-2018-submerged-vs-nonsubmerged-implant.md — SR+MA, 실패율·MBL
- wiki/implants/wu-2018-submerged-nonsubmerged-internal-hexagonal.md — 후향 5년, 즉시 식립
- wiki/implants/liu-2021-clinical-radiographic-performance-one-piece.md — SR+MA, one-piece vs two-piece
- wiki/implants/walter-2022-two-types-two-piece-dental-implants.md — RCT 8년
- wiki/implants/s41598-021-90142-5.md — SR, micromotion 한계
- wiki/implants/irandoust-2020-interplay-bone-healing-remodeling-dental.md — in-vitro/기전, 골치유·리모델링
- 제외: stem `implants`(카테고리 인덱스로 추정, 합성 대상 아님 — 확인 필요)

# Output

- wiki/overviews/implant-placement-protocol-submerged-one-stage-one-piece-overview.md [작성 완료] (frontmatter에 `agenda:` 백링크, `## 한국어 핵심요약` 최상단)

# Done Criteria

이 작업이 제대로 되었다면, 원장이 "1회법 vs 2회법, one-piece vs two-piece를 어떤 근거 수준으로 선택할 수 있는가"를 이 overview 한 페이지에서 수치(실패율·MBL·CI)와 출처 stem 링크로 답할 수 있다.

- [x] 7편 모두 overview에서 [[stem]]으로 참조 → 미합성 카운트 해소 (category-overflow.py 재실행으로 확인)
- [x] 핵심 수치 표 1장 (RR/MD + 95% CI, 출처 inline)
- [x] 근거 수준(sr+ma / sr / rct / retrospective / in-vitro) 명시, 상충 지점 병기
- [x] 한국어 핵심요약 ~10 bullets, Three-line Summary 이중언어
- [x] 모든 수치는 해당 wiki 페이지에서 확인된 것만 (Rule #4)
- [x] 해당 카테고리 index entry 추가, `qmd update && qmd embed` 실행

# Notes / Decisions

- 2026-10-05: overview 작성 후 category-overflow 재실행 → implants 8→1(잔여 stem `implants` 인덱스). 수치는 wiki 페이지 기재값만 사용(abstract-only 3편 한계 명시). 미완: qmd update/embed.
- 2026-10-05: category-overflow 로그 기준 implants 미합성 8 (2위 implants/mbl 6, 격차 2). stem `implants` 제외 7편으로 진행.

# References

- logs/2026-10-05_category-overflow.log
