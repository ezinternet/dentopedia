---
title: "KM 증대 결정 도구 — 각화점막 위험 판정·술식 선택"
date: 2026-08-26
type: agenda
status: in-progress
output_type: interactive
target_file: interactives/2026-08-26_km-augmentation-decision-tool.html
source_overview: wiki/overviews/keratinized-mucosa-peri-implant-health-overview.md
source_wiki:
  - wiki/overviews/keratinized-mucosa-peri-implant-health-overview.md
---

## 목적

각화점막(Keratinized Mucosa, KM) 증대를 다루는 임상 인터랙티브 도구가 전무하다.
`keratinized-mucosa-peri-implant-health-overview` (27 inbound links, 10편 종합)를 chairside 결정 도구로 전환한다.

## 형태 판단

- 오버뷰 핵심 결정 축: ① 증대 필요 여부 ② 목표(폭 vs 두께/심미) ③ 술식 선택 × 시점
- 기존 도구 중 KM 관련 0개 → 전체 경로 커버
- → **3축 순차 도구** (위험 판정 → 목표 → 술식·시점)

## 입력 설계

| 입력 | 값 |
|---|---|
| KMW (각화점막 폭, mm) | 수치 입력 (0–10) |
| 병적 징후 | BOP · 퇴축 · 치태↑ — 체크 (복수 선택) |
| 해당 부위 | 하악 구치 / 상악 전치 / 상악 구치 / 하악 전치 |
| 목표 | 폭(Width) 확보 / 두께·심미 개선 / 임플란트 주위 점막 열개 예방 |
| 수술 시점 | 임플란트 식립 시 / 2차 수술(노출) 시 / 유지관리 중 구제 |
| 자가이식 공여부 의향 | 가능 / 거부 |
| 심미 우선 | 상악 전치부 색조 우선 여부 |

## 출력 설계

### Axis 1 — 위험 판정
- KMW 별 위험 단계: <2mm+병적징후 → 즉시 증대 / <2mm+징후없음 → 감시 강화 / ≥2mm → 정기 측정
- 핵심 근거 배지: Mahardawi 2023 (OR 2.78), Roccuzzo 2025 (20년, OR 6.67), Sabri 2025 umbrella

### Axis 2 — 목표 분기
- 폭(Width) 목표: FGG 경로
- 두께·심미 목표: CTG/XCM bilaminar 경로
- 두 목표 동시: FGG + separate CTG (or STG+FGG)

### Axis 3 — 술식 × 시점
Zhang 2025 결정트리 구현:
- 하악 KMW <2mm → 2차 수술 전 FGG (APF + FGG)
- 하악 KMW 2-3mm → SFGG 또는 FGG
- 상악 전치 심미 → SFGG + 대체재 (색조불일치 회피)
- 상악 구치 → ARF (구개측 KM 충분)

시점별 메모:
- 즉시 식립 시: 퇴축 예방 효과 최대 (Raghoebar 2021: MD +0.34mm 퇴축 적음)
- 2차 수술 시: 실용적·생물학적 선호 창, Bassetti 2016 체계화
- 유지관리 중: Roccuzzo 2025 — 구제 FGG도 20년 원발 KT와 통계적 동등

### 대체재 계층
| 재료 | KMW 우위 | 두께 우위 | 비고 |
|---|---|---|---|
| 자가 FGG | 기준 (+2.6mm avg) | 낮음 | 색조불일치, 공여부 morbidity |
| 자가 CTG | CTG ≈ XCM (width) | 기준 (+0.64mm vs 대체재) | 두께 gold standard |
| 이종 XCM | FGG보다 −0.96~−1.16mm | CTG보다 −0.30mm | 시간 18.5분↓, 통증↓ |
| 동종 ADM | 수축 19.5% 더 큼 | 낮음 | 하위 옵션 |

### 핵심 수치 패널
- OR 2.78 (Mahardawi 2023, 임플란트주위염)
- OR 6.67 (Roccuzzo 2025, 20년)
- TSA-confirmed: 치태 MD 0.37, p=0.002 (Ravidà 2022)
- FGG KMW gain: +1.5–6.5mm (Sanz 2022), +2.6mm avg (Oh 2024)
- CTG recession reduction: 2mm avg (Oh 2024)

## 라우터

기존 연결 도구:
- `2026-08-26_periodontics-staging-treatment-tool.html` — 치주 병기·Grade
- `2026-08-26_arp-decision-tool.html` — 발치와 보존(ARP)
- `2026-08-26_immediate-implant-decision-tool.html` — 즉시 식립
- `2026-08-26_periodontics-staging-treatment-tool.html` → SPT 주기

## Done Criteria

- [ ] Axis 1 위험 판정 (KMW + 병적 징후 → 즉시/감시/정기)
- [ ] Axis 2 목표 분기 (Width vs 두께/심미)
- [ ] Axis 3 술식 결정트리 (Zhang 2025 기반, 부위 × 목표 × 시점)
- [ ] 대체재 계층 시각화
- [ ] 핵심 수치 배지 (OR 2.78 / 6.67 / TSA 치태)
- [ ] 라우터 4도구 연결
- [ ] operations-lint OK
- [ ] 브라우저 테스트 ≥8케이스
- [ ] 커밋·배포
