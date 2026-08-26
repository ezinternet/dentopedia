---
title: "PSTD 예방·관리 도구 — 식립 전 위험 분류 + 술식 프로토콜"
date: 2026-08-26
type: agenda
status: in-progress
output_type: interactive
target_file: interactives/2026-08-26_pstd-prevention-management-tool.html
source_wiki:
  - wiki/overviews/peri-implant-soft-tissue-dehiscence-prevention.md
---

## 목적

`peri-implant-soft-tissue-dehiscence-prevention` (21 inbound) 오버뷰를
chairside 위험 분류 → 예방 프로토콜 → 기존 PSTD 관리 도구로 전환.

기존 PSTD 전용 인터랙티브 도구 없음.

## 형태 판단

오버뷰 핵심 질문: "이 환자/부위의 PSTD 위험은 얼마나 크고, 무엇을 해야 하는가?"
→ **위험인자 체크리스트 → LOW/MOD/HIGH 분류 → 단계별 프로토콜 + 기존 PSTD 관리 ladder**

## 입력 설계

### 섹션 A — 예방 평가 (식립 전)
| 입력 | 값 |
|---|---|
| Biotype | Thick(>1mm) / Thin(≤1mm) |
| KTW | ≥2mm / <2mm |
| 협측 골판 두께 (CBCT) | ≥1mm / <1mm / 모름 |
| 식립 시기 | 즉시식립(Type I·II·III) / 지연 |
| Socket type (즉시식립 시) | Type I / Type II / Type III |
| 흡연 | 비흡연 / 금연 ≥6개월 / 금연 <6개월 / 현재흡연 |
| 전신 위험인자 | 당뇨 / 치주염 이력 (복수 선택) |

### 섹션 B — 기존 PSTD (있는 경우)
| 입력 | 값 |
|---|---|
| PSTD 크기 | 없음 / ≤1mm / 1-3mm / ≥3mm |
| 협측 골 결손 동반 | 예 / 아니오 |

## 출력 설계

### Axis 1 — 위험 분류 (LOW / MOD / HIGH)
위험인자 점수 합산 → 색상 카드로 표시

### Axis 2 — 예방 프로토콜
| 단계 | LOW | MOD | HIGH |
|---|---|---|---|
| 식립 전 | KTW 평가만 | KTW 재평가; <2mm → FGG 권고 고려 | FGG 4-8주 healing → 식립; 흡연 ≥6mo 금연 |
| 식립 시 | 표준; CTG optional; SG(jump≥2mm) | CTG 또는 collagen matrix; SG mandatory; palatal position | CTG + SG + GBR |
| 유지 | 연 1회 SPT | 연 1-2회 SPT; PSTD 측정 | 집중 SPT 3개월 |

VST panel: Type II socket + 심미부위 → VST vs open-flap GBR 비교 (Ebrahim 2026)

### Axis 3 — 기존 PSTD 관리 ladder
- ≤1mm: 관찰 + 위생 강화
- 1-3mm: CTG 보강 (professional esthetic 7.7/10; 환자만족 60.8/100 괴리 주의)
- ≥3mm + 협측 골 결손: 보철 제거 → GBR → 6mo healing → 재수복

### 핵심 수치 배지
- PSTD prevalence 46.2% (Tavelli 2025, disease-free)
- MREC 23.1%
- CTG IIP midfacial 보존 0.4-0.7mm (Seyssens 2021)
- VST PES 12.78 vs GBR 11.56 p=0.03 (Ebrahim 2026)
- 금연 효과: ≥6mo 전 금연 권고 (Caggiano 2022)

## 라우터
- `2026-08-26_km-augmentation-decision-tool.html` — KM 증대 술식 선택
- `2026-08-26_immediate-implant-decision-tool.html` — 즉시식립 4변수 결정
- 사이너스 거상 이식재 도구

## Done Criteria
- [ ] 위험인자 체크리스트 → LOW/MOD/HIGH
- [ ] Axis 2 단계별 프로토콜 (3×3 표)
- [ ] VST vs open-flap panel (즉시식립 Type II)
- [ ] Axis 3 기존 PSTD ladder
- [ ] 환자 만족도 괴리 경고 (Nart 2025)
- [ ] 핵심 수치 배지 5개
- [ ] operations-lint OK
- [ ] 브라우저 테스트 ≥8케이스
- [ ] 커밋·배포
