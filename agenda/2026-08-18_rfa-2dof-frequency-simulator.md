---
title: "RFA 2-DOF 시뮬레이터 — 강성·공진주파수·미세변위 (interactive 작업명세)"
type: agenda
date: 2026-08-18
status: done
owner: 원장
priority: P2
tags: [interactive, rfa-2dof-frequency-simulator]
source_wiki:
  - wiki/implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability.md
  - wiki/overviews/rfa-isq-measurement-mechanism.md
---

# Goal

Bhandarkar 2023의 2자유도(2-DOF) 수학 모델로 골 접합 강성 변화가 RFA 공진주파수와 ISQ에 미치는 영향을 실시간 시뮬레이션 — SmartPeg-임플란트-골 계의 물리를 교육용으로 시각화.

# Input

- wiki/implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability.md
- wiki/overviews/rfa-isq-measurement-mechanism.md
- (물리·임상 파라미터는 위 페이지에서 추출한 Class B 정적값 — deploy 자동재생성 금지)

# Output

- interactives/2026-08-18_rfa-2dof-frequency-simulator.html  ← 소급 명세: 도구가 먼저 만들어졌고 2026-08-24 감사(operations-lint)에서 agenda 누락 지적되어 보완함

# Done

- [x] 도구 구현 및 interactives/ 배치
- [x] source_wiki 근거 페이지 연결
- [x] frontmatter agenda 백링크 양방향 완료
