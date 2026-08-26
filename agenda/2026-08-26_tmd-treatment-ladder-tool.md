---
title: "TMD 치료 Ladder 도구 — 진단형·병기별 비약물·약물·중재 결정"
date: 2026-08-26
type: agenda
status: in-progress
output_type: interactive
target_file: interactives/2026-08-26_tmd-treatment-ladder-tool.html
source_wiki:
  - wiki/overviews/tmd-management-evidence-ladder.md
---

## 목적

TMD/TMJ 관리 10축 오버뷰(36편, 27 inbound links)를 chairside 치료 결정 도구로 전환.
이 도메인에 기존 인터랙티브 도구 전무.

## 형태 판단

- 오버뷰 10축: 역학·진단 / 비약물 보존 / 약물 / NMA / arthrocentesis / 이갈이 / BTX / OA / QoL+VD / 편측저작
- 진료실 핵심 질문: "이 환자에게 지금 무엇을 할 것인가?"
- → **주증상형 × 병기 기반 치료 Ladder 도구**

## 입력 설계

| 입력 | 값 |
|---|---|
| TMD 유형 | 근육형(Myogenous) / 관절형(Articular) / 복합형(Combined) |
| 주증상 | 근육통·두통 / 관절음(Click/Popping) / 개구제한 / 이명 |
| 병기 | 급성(<3개월) / 만성(≥3개월) |
| 이갈이 동반 | 예 / 아니오 |
| 편측저작 습관 | 예 / 아니오 |
| 보존치료 실패 여부 | 아직 미시행 / 8주 이상 실패 |
| OVD 변경 계획 | 없음 / 교합 수복 예정 |

## 출력 설계

### Axis 1 — 비약물 1차 치료
BMJ NMA 2023 (Yao, 233 RCT) 근거:
- 근육형: PBMT(통증 SUCRA 88.9%) + 도수치료(개구 SUCRA 92.9%) 우선 → CBT+바이오피드백(RD 36%)
- 관절형: 하악 가동화(RD 36%) + 수기 트리거포인트(RD 32%)
- 교육·자기관리(ED/SM) 단독: 단기 열세 주의 (Ferland 2026, 47 RCT, very low~low)
- 스플린트: 조건부 추가 (운동과 동등 또는 운동 우위 — Zhang 2021)

편측저작 체크: 습관저작측 = TMD 통증측 (κ=0.767, RR 4.5 — Santana-Mora 2021)
→ 저작측 교정을 1차 비약물 항목에 통합

### Axis 2 — 약물 (비약물 단독 불충분 시 추가)
- 관절통: NSAIDs / IA corticosteroid / Hyaluronate
- 근육통: Cyclobenzaprine
- 이갈이 동반: Cyclobenzaprine (수면이갈이 포함)
- 관절내 NMA (Al-Hamed 2026): DD → MESNA·HA, OA → PEA·글루코사민+HA (근거 낮음~매우낮음)
- 경고: 교합조정·비가역 교합치료는 1차 금기 (Cochrane 2024 Singh)

### Axis 3 — 중재 (보존 실패 8주↑ 시)
- 관절천자(Arthrocentesis):
  - 단독 우월성: 미입증 (Valenzuela-Fuenzalida 2026, 32 RCT, VAS p=0.55) — 보조 옵션
  - i-PRF 부가: TSA 결정적, VAS −1.62, MMO +5.03mm (Bader Alzamanan 2026, GRADE moderate)
  - HA·스테로이드 부가: 근거 있음 (Zhang 2024)
- 극단 이질성 caveat: I²=85–98%, SMD 해석 주의 (Fuentes-Barría 2026)

### Axis 4 — 특수 상황
- 이갈이: 스플린트·biofeedback 우위 (Minakuchi 2022)
- OVD 거상 예정: 점진 거상 + TMJ 모니터링 (Wang 2024 — OVD가 교합 상실보다 연골 손상 빠름)
- 이명 동반: 편측저작 선호 90.7% 동측성 (Ma 2025) → 저작패턴 평가 필수
- TMJ OA: CT gold standard (κ=0.71 vs 파노라마 0.16) + 보존 우선

### 핵심 수치 패널
BMJ NMA 3인방: CBT+바이오피드백 RD 36% / 하악 가동화 RD 36% / 트리거포인트 RD 32%
편측저작: RR 4.5 / κ=0.767 / 이명 동반 90.7%
arthrocentesis 상충: 단독 VAS p=0.55(NS) vs i-PRF VAS −1.62(GRADE moderate)
근육성 NMA: PBMT SUCRA 88.9% / 도수치료 SUCRA 92.9%

## 라우터

- `2026-08-26_periodontics-staging-treatment-tool.html` — 치주 감별
- `2026-08-26_oral-medicine-decision-tool.html` — BMS·구강점막 감별
- `2026-08-26_km-augmentation-decision-tool.html` — 연조직 증대 (임플란트 위치 관련)

## Done Criteria

- [ ] 유형×병기 입력 → Axis 1 비약물 경로 (PBMT/도수/CBT 분기)
- [ ] Axis 2 약물 계층 (관절형 vs 근육형)
- [ ] Axis 3 중재 기준 (보존 실패 8주↑ + i-PRF 상충 데이터 나란히)
- [ ] 편측저작 경고 통합
- [ ] OVD 위험 경고
- [ ] 핵심 수치 배지
- [ ] operations-lint OK
- [ ] 브라우저 테스트 ≥8케이스
- [ ] 커밋·배포
