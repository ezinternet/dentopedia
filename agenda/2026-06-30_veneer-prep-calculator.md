---
title: "비니어 삭제량 계산기 — Do-the-Math (EV−LT=P) chairside 도구"
type: agenda
date: 2026-06-30
status: in-progress
owner: 원장
priority: P1
tags: [veneer, preparation, do-the-math, chairside-calculator, minimally-invasive]
source_wiki:
  - wiki/overviews/veneer-preparation-design-minimally-invasive-overview.md
  - wiki/veneers/coachman-2014-tooth-color-veneer-preparation-design.md
  - wiki/veneers/gurel-2007-porcelain-laminate-veneers-minimal-preparation.md
  - wiki/veneers/cattoni-2016-3d-digital-smile-planning-mockups.md
  - wiki/veneers/chandode-2026-no-preparation-conventional-veneers-clinical-considerations.md
  - wiki/veneers/ali-2023-conventional-minimally-invasive-veneers-sr.md
  - wiki/veneers/el-mowafy-2018-glass-ceramic-veneer-materials-narrative-review.md
output_wiki:
  - interactives/2026-06-30_veneer-prep-calculator.html
---

# Goal

라미네이트 비니어 삭제량을 chairside에서 정량 산출하는 단일 HTML 계산기. Coachman의 "Do the Math" 수식 **EV − LT = P**(부위별 추가부피 − 라미네이트 두께 = 삭제량)와 색변화(shade tone) → 권장 도재 두께 규칙을 입력받아, 부위별(치경/중앙/절단 1/3·인접면·절단연) 삭제 깊이와 "법랑질 한정 / 0mm 무삭제 / intrasulcular 변연 필요" 판정을 출력 → 원장이 prep 전 의사결정 보조로 사용.

# Input

- wiki/overviews/veneer-preparation-design-minimally-invasive-overview.md — 종합 로직(3세대·진화·결정 로직·법랑질 비협상)
- wiki/veneers/coachman-2014-tooth-color-veneer-preparation-design.md — EV−LT=P 수식·부위별 Table 1·색변화 규칙(1–2 tone→0.3mm, ≥3 tone→침습+intrasulcular)
- wiki/veneers/gurel-2007-porcelain-laminate-veneers-minimal-preparation.md — "prepare through the APT" 패러다임·법랑질 보존
- wiki/veneers/cattoni-2016-3d-digital-smile-planning-mockups.md — 디지털 목업 가이드(부가 맥락)
- wiki/veneers/chandode-2026-no-preparation-conventional-veneers-clinical-considerations.md — 무삭제 적응증/금기
- wiki/veneers/ali-2023-conventional-minimally-invasive-veneers-sr.md — MPV 0.2–0.5mm 생존 동등 이상
- wiki/veneers/el-mowafy-2018-glass-ceramic-veneer-materials-narrative-review.md — 상아질 변연 노출 ~10× 실패(법랑질 confinement 경고)

# Output

- interactives/2026-06-30_veneer-prep-calculator.html
  - frontmatter에 `agenda: agenda/2026-06-30_veneer-prep-calculator.md` + 위 `source_wiki:` 백링크 박을 것

# Done Criteria

- [x] 부위별 EV·LT 입력 → P = EV − LT 자동 계산 (5부위: 치경/중앙/절단 1/3·인접면·절단연)
- [x] 색변화(shade tone) 입력 → 권장 라미네이트 두께(LT) 프리셋 + intrasulcular 변연 경고
- [x] P≤0 → "0mm 무삭제(법랑질 무손상)" 판정, P>0 → 삭제 깊이 + depth-bur(0.3/0.5/0.7mm) 매핑
- [x] 법랑질 두께 한계 경고(상아질 노출 ~10× 실패, El-Mowafy 2018) 비협상 배너
- [x] 무삭제 금기(내인성 변색·부정정렬·큰 형태수정) 체크 → 경고
- [x] 모든 수치에 inline 출처(Coachman 2014 / Ali 2023 / Chandode 2026 등) 명시
- [x] frontmatter source_wiki / agenda 백링크 박힘
- [ ] index 또는 interactives/index.html에 반영(배포 스크립트가 자동 생성)

# Notes / Decisions

- 2026-06-30: 이 도구는 Class B(임상 결정 도구) — 수치는 Coachman 2014 등 특정 논문에서 추출. 배포 시 자동 재작성 안 됨(interactive-staleness 신호만). source_wiki page가 갱신되면 LLM 재작성 대상.
- 2026-06-30: EV(추가부피)는 진단 왁스업/목업에서 caliper로 실측하는 값 — 계산기는 술자가 측정한 EV를 입력받는다(계산기가 EV를 추정하지 않음). LT는 색변화 기반 프리셋 제공하되 술자 override 가능.
- 색변화 규칙(Coachman Table 1 + 본문): 1–2 tone→thin ~0.3mm, ≥3 tone→더 두꺼운 도재+intrasulcular 변연. 어두운 기질일수록 LT↑ → P↑(더 침습적). 이는 "더 어두운 치아 = 더 많은 삭제"라는 역설의 근거.

# References

- [[agenda/2026-06-30_veneer-prep-calculator]]
- 종합: [[wiki/overviews/veneer-preparation-design-minimally-invasive-overview]]
