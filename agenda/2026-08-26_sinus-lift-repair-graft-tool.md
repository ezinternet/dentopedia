---
title: "상악동 거상 — 천공 수리 결정 + 이식재 선택 도구"
date: 2026-08-26
type: agenda
status: in-progress
output_type: interactive
target_file: interactives/2026-08-26_sinus-lift-repair-graft-tool.html
source_wiki:
  - wiki/overviews/sinus-lift-lateral-2026-synthesis.md
---

## 목적

`sinus-lift-lateral-2026-synthesis` (26 inbound) 오버뷰 40편의 미커버 부분을 전환.
기존 `2026-06-12_sinus-perforation-risk-calculator.html`이 위험 예측을 담당하므로,
이 도구는 **"천공이 생겼을 때 무엇을 할 것인가"** + **"이식재를 무엇으로 쓸 것인가"** 두 축을 담는다.

## 형태 판단

- Cluster 1 (천공 수리): 크기 ≤10mm vs >10mm × 재료(PRF vs 콜라겐) 분기 — 2×2 결정 표
- Cluster 5 (이식재): DBBM / BCP / dpDTM / PRF adjunct 계층
- → **2축 결정 도구** (수리 + 이식재)
- 핵심 근거 배지 포함

## Axis 1 — 천공 수리 결정

### 전제: 수리된 천공은 금기가 아님
- 임플란트 손실 4% (95% CI 2–8%) = 온전막과 동등 (Soares 2024 SR+MA, 130연구)
- OR 1.35 비유의 (Sala 2024, 6,860 임플란트)
- 천공 크기는 임플란트 손실 예측 안 함 (p=0.86)

### 수리 결정트리 (천공 크기 기반)

| 크기 | 1차 재료 | 근거 | 비고 |
|---|---|---|---|
| ≤10 mm | PRF (L-PRF/A-PRF/e-PRF) | Xin 2020 RCT: 콜라겐보다 신생골↑, 1주 완전재형성 | 콜라겐과 동등 이상 |
| ≤10 mm | 콜라겐 막 (대안) | 표준 대안 | PRF 준비 안 될 때 |
| >10 mm | tack 고정 콜라겐 + 동시 이식 | Tian 2026 기법 | 기계적 봉합 필수 |
| >10 mm (합병증) | 수술 중단·재입원 고려 | — | 대형 천공+회수 불가 |
| 특수: 항골흡수제 환자 | handle-tab 콜라겐 + 피브린 글루 | Kim 2026 단일 케이스 | tack 대체 |

### 기구 선택 근거
- Piezoelectric > Rotary bur (Lee 2023 NMA: SMP 10%↑마다 생존 OR 0.45)
- SUCRA: rotary bur 0.0745 (최저), piezoelectric 상위권

## Axis 2 — 이식재 선택 (Cluster 5)

### 재료 계층

| 재료 | 신생골 형성 | ISQ 이득 | 생존율 데이터 | 특기 |
|---|---|---|---|---|
| DBBM (탈단백우골) | 기준 | 기준 | 풍부 | 흡수 불완전, 기준재료 |
| DBBM + PRF | +7–12% 신생골 | 없음 (Scarano 2016) | 기준 동등 | ISQ로 조기부하 불가 |
| BCP (이상다공성칼슘인산염) | DBBM보다 많음 | 별도 확인 필요 | 제한적 | 완전흡수 장점 |
| dpDTM (탈단백화 인간 치아기질) | DBBM과 동등 | ~70 동등 (Paetnukroh 2024) | 실패 0건 (소표본) | 자가 발치치아 유래, 근거 가장 약함 |

### PRF 부가 원칙
- DBBM + PRF: 신생골 +7–12% (일관), 잔존graft 감소 → 조직학적 이득
- ISQ 이득 없음 → 조기부하 정당화 근거 없음
- e-PRF 단독 barrier: Estrin 2025 전향, 31임플란트 100% 생존 (최근 강력 신호)

## 핵심 수치 배지

- OR 1.35 비유의 (수리 천공 = 온전막, Sala 2024)
- 임플란트 손실 4% 95% CI 2–8% (Soares 2024, 130편)
- Lee 2023 NMA: SMP 10%↑마다 생존 OR 55%↓ (OR 0.45)
- e-PRF sole barrier: 100% 생존 (Estrin 2025, 31임플란트)
- HR 27.75 점액저류낭 (Nemati 2023) — 예측 배지

## 라우터

- `2026-06-12_sinus-perforation-risk-calculator.html` — 천공 위험 예측 (먼저 실행)
- `2026-08-26_arp-decision-tool.html` — 발치와 보존 (이식재 결정)
- `2026-08-26_immediate-implant-decision-tool.html` — 상악동+즉시식립 교차

## Done Criteria

- [ ] Axis 1 천공 크기 입력 → 수리 재료 결정 + 기구 권장
- [ ] 수리 후 식립 가능 여부 명시 (=금기 아님)
- [ ] Axis 2 이식재 계층 시각화
- [ ] PRF 부가 조직학 이득 vs ISQ 이득 없음 구분
- [ ] 핵심 수치 배지 5개
- [ ] 라우터 3도구
- [ ] operations-lint OK
- [ ] 브라우저 테스트 ≥8케이스
- [ ] 커밋·배포
