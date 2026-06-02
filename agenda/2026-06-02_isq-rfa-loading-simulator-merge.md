---
title: "ISQ·RFA 통합 시뮬레이터 v1 — 측정 시각화 + 부하결정 + 치유궤적 병합"
type: agenda
date: 2026-06-02
status: done
source_wiki:
  - wiki/implants/isq/andersson-2019-rfa-factors-5year-neoss-survival.md
  - wiki/implants/isq/tisci-2026-isq-it-mbl-survival-sr-ma.md
  - wiki/implants/isq/bavetta-2024-isq-osstell-osseo-device-comparison.md
  - wiki/implants/isq/stoilov-2023-macrodesign-length-diameter-bone-quality-isq.md
  - wiki/implants/isq/konuklu-2026-five-osteotomy-protocols-isq-rct.md
  - wiki/implants/isq/huang-2020-isq-clinical-significance-literature-review.md
---

# Goal
두 개의 별도 산출물 — (A) `isq_rfa_simulation.html`(Beacon/SmartPeg 공진측정 애니메이션), (B) `ISQ-Loading Calculator`(부하결정 엔진) — 을 단일 HTML로 병합하고, wiki 논문 실데이터(치유궤적·임계값·기기동등)를 입혀 "실제와 가까운" 통합 시뮬레이터 v1을 만든다.

# Input
- 업로드: isq_rfa_simulation.html, ISQ-Loading Calculator — chairside.html
- wiki 근거: source_wiki 6편

# Output
- interactives/2026-06-02_isq-rfa-loading-simulator-v1.html

# Done 기준
- [x] rig 슬라이더(골질·직경·디자인·유착도·MBL) → 실시간 ISQ·스펙트럼·rig 애니메이션 연동
- [x] 부하결정 엔진(시점×ISQ×ITV) green/yellow/red + Andersson 70 임계 + Tisci 보조지표 caveat
- [x] 하단 치유궤적 차트: D1-D2 / D3-D4 밴드 + 3주 dip(Bergamo) + 70 임계선 + 현재 측정점
- [x] ISQ 절댓값이 논문 범위 내 캘리브레이션 (D1-D2 식립 ~70-77, D3-D4 ~58-65)

# Notes / 정정사항
- 구버전 계산기의 "Bavetta 2024 → Osseo가 Osstell보다 -3 ISQ 자동보정" 가정 제거.
  wiki bavetta-2024 원문은 두 기기 **동등(r>0.95), 계통오차 없음** → -3 보정은 미검증 가정이라 v1에서 삭제.
- 궤적 곡선 절댓값은 wiki 추세 기반 보간치 [claude해석]. 임계값·동등성·dip 시점은 논문 직접 근거.

# Next (v2 후보)
- Konuklu 2026 osteotomy 프로토콜(300rpm vs OD vs condensation)별 궤적 분기 추가
- ΔISQ 추세 기반 점수합 판정(현재는 범위기반 + dip 강등 modifier)
