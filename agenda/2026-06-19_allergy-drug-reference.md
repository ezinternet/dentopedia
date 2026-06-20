---
title: "알러지 환자 대체 약물 참조 인터랙티브"
type: agenda
date: 2026-06-19
status: done
source_wiki:
  - wiki/local-anesthesia/bina-2018-true-allergy-amide-local-anesthetics-case.md
  - wiki/drug/antibiotics/thornhill-2019-adverse-reactions-oral-antibiotics-dentists.md
output_wiki: []
---

# Goal

알러지(국소마취제·항생제·진통제 등) 환자에서 안전한 **대체 약물**을 빠르게 조회하는 임상 참조 인터랙티브(`interactives/2026-06-19_allergy-drug-reference.html`)의 작업 명세.

# Input

- LA 알러지: [[local-anesthesia/bina-2018-true-allergy-amide-local-anesthetics-case]] (진성 amide 알러지는 드묾, 교차반응)
- 항생제 이상반응/알러지: [[drug/antibiotics/thornhill-2019-adverse-reactions-oral-antibiotics-dentists]]
- 관련: drug/ 항생제·진통제·전신질환 카테고리

# Output

- `interactives/2026-06-19_allergy-drug-reference.html` — 알러지군별 대체약물 배지/표

# Done Criteria

- [x] 인터랙티브 산출
- [x] OPS frontmatter 크로스링크(agenda↔interactive) 연결 (operations-lint 통과)

# Notes

- 동시 진행된 drug 카테고리 재분류(2026-06-20) 맥락에서 생성된 참조 도구. frontmatter·agenda 체인은 lint 정합화 차원에서 후속 보강(2026-06-20).
