---
title: "임플란트 로딩 시기 결정 인터랙티브 도구"
type: agenda
date: 2026-06-16
status: done
source_wiki:
  - wiki/implants/isq/diehl-2022-narrow-diameter-implant-stability-hyperglycemic.md
  - wiki/implants/isq/shiffler-2016-implant-length-diameter-location-isq.md
  - wiki/implants/isq/stoilov-2023-macrodesign-length-diameter-bone-quality-isq.md
output_wiki: []
---

## Goal

임플란트 직경, ISQ, 식립 후 경과 월수, 부위(전치/구치/상악동) 4변수를 입력하면 로딩 타이밍(즉시/조기/표준/지연)을 판정하는 브라우저 계산기 작성.

## Input

- ISQ 기반 stability threshold 문헌 (3편 ISQ 카테고리)
- 직경·부위별 subgroup 데이터

## Output

- `interactives/implant-loading-decision.html`

## Done criteria

- 4개 변수 입력 시 로딩 타이밍 권고 및 근거 문헌 표시
- 모바일 반응형
