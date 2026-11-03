---
title: "SDA 임상 보조 인터랙티브 도구 2종"
type: agenda
date: 2026-11-04
status: done
output_wiki:
  - interactives/2026-11-04_sda-strategy-decision-tree.html
  - interactives/2026-11-04_sda-masticatory-compensation-calculator.html
source_wiki:
  - wiki/overviews/sda-shortened-dental-arch-evidence-overview.md
  - wiki/removable-partial-denture/liang-2015-effects-removable-dental-prostheses-masticatory.md
  - wiki/removable-partial-denture/koyama-2026-effects-occlusal-contact-loss-preferred.md
  - wiki/removable-partial-denture/gao-2025-effectiveness-restoration-strategies-posterior.md
  - wiki/removable-partial-denture/nassani-2013-fesrpd-shortened-dental-arch-reappraisal.md
---

## 목적

단축치열궁 (Shortened Dental Arch, SDA) 근거 합성(11편 오버뷰)을 chairside 에서 바로 쓸 수 있는 인터랙티브 도구 2종으로 구현한다.

## 산출물

### 1. [결정트리] SDA vs 보철 전략 체커

`interactives/2026-11-04_sda-strategy-decision-tree.html`

- 4단계 분기: 결손 범위 → 선호 저작측 (Preferred Chewing Side, PCS) → 보철 희망 → 임플란트 vs 의치
- 수요 기울기 (Demand Gradient) 배지: 3% / 58% / 93% (Nassani 2013)
- Witter 3단계 기준 내장
- Gao 2025 M1-only 임플란트 vs 국소의치 (Removable Partial Denture, RPD) 비교표
- OHRQoL 계층 (Nakai 2022): 비금속클라스프 의치 (Non-Metal Clasp Denture, NMCD) > SDA > 통상 RPD

### 2. [계산기] 저작 기능 보상 예측기

`interactives/2026-11-04_sda-masticatory-compensation-calculator.html`

- Liang 2015 SR dose-effect 데이터 기반 저작 기능 보상 (Masticatory Function Compensation) 추정
- 입력: 치열 유형 (SDA / ESDA), 선호 저작측 결손 여부, RPD 인공치 수 (0–8개)
- 출력: 초기 결손 %, RPD 보상 %, 최종 저작 수행능 %, 잔여 결손 %
- Koyama 2026 PCS 페널티 (+10%) 보정 적용

## 근거 매핑

| 도구 기능 | 출처 |
|---|---|
| 수요 기울기 3/58/93% | Nassani 2013 |
| SDA 저작 결손 28–39% | Liang 2015 SR |
| RPD 보상 ~50%, 용량-반응 | Liang 2015 SR |
| PCS 결손 시 저작효율 (Masticatory Efficiency, ME) 저하 | Koyama 2026 RCT |
| M1-only 임플란트 = SDA 구현, 비용 1.7배↓ | Gao 2025 |
| OHRQoL: NMCD > SDA > RPD | Nakai 2022 |
| Witter 3단계 임계값 | Nassani 2013 |
