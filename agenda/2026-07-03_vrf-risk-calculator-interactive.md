---
title: "수직치근파절(VRF) 위험도 계산기 — 근관치료 대구치"
type: agenda
date: 2026-07-03
status: done
owner: 원장
priority: P2
tags: [vertical-root-fracture, endodontics, risk-calculator, interactive]
source_wiki:
  - wiki/endodontics/shaping/lee-2026-residual-pericervical-apical-dentine-vertical.md
  - wiki/endodontics/shaping/rathke-2024-ex-vivo-minimally-invasive-endodontic.md
  - wiki/endodontics/diagnosis/alkhani-2026-optical-coherence-tomography-detection-dental.md
  - wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures.md
  - wiki/overviews/cracked-tooth-syndrome-overview.md
---

# Goal

근관치료된 대구치에서 수직치근파절(Vertical Root Fracture, VRF) 위험도를 chairside에서 빠르게 층화할 수 있는 계산기. Lee 2026 case-control의 4개 독립 위험인자(잔존 치근단부 상아질 소실 정도·치아종류·재근관치료 병력·1차 근관치료 후 경과기간)를 입력받아 정성적 위험 구간(저/중/고)과 근거 adjusted OR을 함께 제시. isolated PD≥5mm로 내원한 근관치료 대구치의 발치 vs 보존 결정을 보조.

# Input

- wiki/endodontics/shaping/lee-2026-residual-pericervical-apical-dentine-vertical.md — 1차 입력. 4개 위험인자의 adjusted OR·cut-off·통합모델 AUC 0.940(sens 85.7%/spec 89.5%/PPV 78.9%/NPV 93.2%)
- wiki/endodontics/shaping/rathke-2024-ex-vivo-minimally-invasive-endodontic.md — "최소침습 성형=보호" 통념에 대한 반증 경고 문구
- wiki/endodontics/diagnosis/alkhani-2026-optical-coherence-tomography-detection-dental.md — 향후 진단 옵션(OCT) 참고 노트
- wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures.md — VRF 정의·NRFT/RFT 구분 맥락
- wiki/overviews/cracked-tooth-syndrome-overview.md — VRF 진단·위험인자 클러스터 통합 위치

# Output

- interactives/2026-07-03_vrf-risk-calculator.html

frontmatter에 `agenda: agenda/2026-07-03_vrf-risk-calculator-interactive.md` 백링크·`source_wiki` 박음.

# Done Criteria

- [x] 4개 입력(치근단부 잔존 상아질 카테고리, 치아종류, reRCT 횟수, pRCT 경과기간) → 위험 구간 반환
- [x] 각 항목 adjusted OR + 95% CI 표시(출처 inline)
- [x] 통합모델 성능(AUC 0.940, sens/spec/PPV/NPV) 명시
- [x] "isolated PD≥5mm 근관치료 대구치에 한정된 판별모델 — 독립 진단검사 아님, 단일 case-control 근거" 한계 명시
- [x] Rathke 2024 반증 경고("최소성형이 예방 아님") 별도 카드
- [x] frontmatter에 source_wiki / agenda 백링크
- [x] Class B(임상 결정 도구) — 수치 재작성 금지 신호 대상으로 등록

# Notes / Decisions

- 2026-07-03: 이 논문은 진짜 다변량 로지스틱 회귀식의 절편(intercept)을 보고하지 않아 "정확한 확률값"은 계산 불가 — adjusted OR 기반 정성적 위험 구간(저/중/고)만 제시하고, 정량 AUC/sens/spec은 모델 전체 성능으로만 인용. 이 제약을 도구 내 명시.
- 모든 수치는 lee-2026 소스 페이지에서만 인용 — Rule #1 준수, 신규 수치 생성 없음.

# References

- [[wiki/endodontics/shaping/lee-2026-residual-pericervical-apical-dentine-vertical]]
- [[wiki/overviews/cracked-tooth-syndrome-overview]]
