---
title: "Under-milling ITV·ISQ 예측기 — Rosas-Díaz 2024 (interactive 작업명세)"
type: agenda
date: 2026-08-18
status: done
owner: 원장
priority: P2
tags: [interactive, under-milling-itv-isq-predictor]
source_wiki:
  - wiki/implants/isq/rosasdiaz-2024-insertion-compression-primary-stability.md
  - wiki/overviews/isq-loading-threshold.md
---

# Goal

언더밀링(under-milling)량에 따른 삽입 토크(insertion torque, ITV)와 ISQ 상승을 Rosas-Díaz 2024 데이터 기반으로 예측하는 계산기 — 과도한 언더밀링의 골압박 리스크 경고 포함.

# Input

- wiki/implants/isq/rosasdiaz-2024-insertion-compression-primary-stability.md
- wiki/overviews/isq-loading-threshold.md
- (물리·임상 파라미터는 위 페이지에서 추출한 Class B 정적값 — deploy 자동재생성 금지)

# Output

- interactives/2026-08-18_under-milling-itv-isq-calculator.html  ← 소급 명세: 도구가 먼저 만들어졌고 2026-08-24 감사(operations-lint)에서 agenda 누락 지적되어 보완함

# Done

- [x] 도구 구현 및 interactives/ 배치
- [x] source_wiki 근거 페이지 연결
- [x] frontmatter agenda 백링크 양방향 완료
