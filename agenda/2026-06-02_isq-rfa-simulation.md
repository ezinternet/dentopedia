---
title: "ISQ·RFA 공진주파수 시뮬레이터 (교육용)"
type: agenda
date: 2026-06-02
status: done
owner: 원장
priority: P2
tags: [isq, rfa, resonance-frequency, education, interactive, smartpeg]
source_wiki:
  - wiki/implants/isq/andersson-2019-rfa-factors-5year-neoss-survival.md
  - wiki/implants/isq/bavetta-2024-isq-osstell-osseo-device-comparison.md
---

# Goal

공진주파수분석(Resonance Frequency Analysis, RFA)으로 임플란트 안정성지수(Implant Stability Quotient, ISQ)가 측정되는 물리(SmartPeg 1차 굽힘 공진 → 주파수 → ISQ 환산)를 원장·동료가 직관적으로 보도록 인터랙티브로 시각화. 골질·골유착도·골 상연 위 노출 길이(MBL)·직경 4개 파라미터를 조절하면 공진주파수와 ISQ가 실시간 변하고, SmartPeg 진동 모드와 주파수 스펙트럼이 함께 갱신된다.

# Input

- wiki/implants/isq/andersson-2019-rfa-factors-5year-neoss-survival.md — RFA 영향 인자(골·노출 길이) 근거
- wiki/implants/isq/bavetta-2024-isq-osstell-osseo-device-comparison.md — ISQ 측정 디바이스·환산 맥락
- 물리 모델: 캔틸레버 빔 1차 굽힘 공진 f=(1/2π)√(k/m); k ∝ E_interface·D^4/L_eff^3

# Output

- interactives/2026-06-02_isq-rfa-loading-simulator-v1.html  (병합 최종본)
- interactives/2026-06-02_isq-rfa-simulation.html  (구버전, v1로 대체)

# Done Criteria

- [x] 4개 슬라이더 → 실시간 f·ISQ 환산 (Osstell 3500–8500 Hz ↔ ISQ 1–100 선형 맵)
- [x] 환산값 임상 범위 검증 (D1≈80, D2≈70, D3≈57, D4≈46; dip·MBL 반영)
- [x] SmartPeg 진동 애니메이션 + 주파수 스펙트럼 피크 + ISQ 게이지/존
- [x] 단일 HTML, 외부 CDN 없음 (오프라인 chairside)

# Notes

교육·직관용 단순 모델. 검증된 예측기가 아님 — 노출 길이/직경의 ISQ 민감도는 단순화된 캔틸레버 가정이며,
극단값(예: D1 + 5.0mm)에서 ISQ 100으로 clamp됨. 실제 임상 임계값 판단은
interactives/2026-05-25_isq-loading-threshold-calculator.html 사용.
