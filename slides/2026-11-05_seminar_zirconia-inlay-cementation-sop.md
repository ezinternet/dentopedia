---
title: "지르코니아 인레이 세팅 SOP"
type: slides
date: 2026-11-05
status: done
source_wiki:
  - wiki/dental-materials/zirconia/al-akhali-2025-zirconia-cleaning-bonding-duration.md
  - wiki/dental-materials/zirconia/nasri-2025-surface-conditioning-zirconia-bonding-umbrella.md
  - wiki/resin-bonding/gauthier-2005-oxygen-inhibition-dental-resins.md
  - wiki/dental-materials/lim-2022-oxygen-shielding-glycerin-vacuum-3d-printed.md
agenda: agenda/2026-11-05_seminar_zirconia-inlay-cementation-sop-slides.md
marp: true
theme: dentopedia
paginate: true
size: 16:9
lang: ko
description: "APA → 세정 → 프라이머 → 접착의 근거기반 프로토콜 (Al-Akhali 2025, Nasri 2025, Gauthier 2005, Lim 2022)"
---

<!-- _class: lead -->

# 지르코니아 인레이 세팅 SOP

## APA → 세정 → 프라이머 → 접착의 근거기반 절차

---
출처: Al-Akhali 2025 · Nasri 2025 Umbrella SR

---

## 왜 표면처리가 중요한가?

지르코니아 (Zirconia, ZrO₂)는 본질적으로 소수성 · 비반응성 — 처리 없이는 접착이 성립하지 않는다

| 요소 | 미처리 ZrO₂ | 최적 처리 후 |
|---|---|---|
| 표면 에너지 (SFE) | 낮음 (오염막 존재) | 68 mN/m↑ |
| 레진 접착 (TBS) | 불안정 | 장기 안정 |
| 임상 근거 | — | Nasri 2025: 233연구 Umbrella SR |

> **핵심 원칙**: APA + 10-MDP 프라이머 = 현재 가장 검증된 조합

---

## 전체 흐름 한눈에

<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:720px;font-family:sans-serif;font-size:14px">
  <!-- 기공소 납품 -->
  <rect x="260" y="10" width="200" height="40" rx="6" fill="#e8f0fe" stroke="#4a6cf7" stroke-width="1.5"/>
  <text x="360" y="35" text-anchor="middle" font-weight="bold" fill="#1a237e">기공소 납품</text>
  <!-- 화살표 -->
  <line x1="360" y1="50" x2="360" y2="70" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <!-- APA 박스 -->
  <rect x="200" y="70" width="320" height="44" rx="6" fill="#fff3e0" stroke="#e65100" stroke-width="1.5"/>
  <text x="360" y="88" text-anchor="middle" font-weight="bold" fill="#bf360c">APA</text>
  <text x="360" y="106" text-anchor="middle" font-size="11" fill="#6d4c41">(공기입자연마, Airborne Particle Abrasion)</text>
  <!-- 세 갈래 분기 수직선 -->
  <line x1="360" y1="114" x2="360" y2="134" stroke="#555" stroke-width="2"/>
  <line x1="140" y1="134" x2="580" y2="134" stroke="#555" stroke-width="2"/>
  <!-- 즉시 세팅 -->
  <line x1="160" y1="134" x2="160" y2="154" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="80" y="154" width="160" height="40" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="160" y="170" text-anchor="middle" font-weight="bold" fill="#1b5e20" font-size="13">즉시 세팅</text>
  <text x="160" y="186" text-anchor="middle" font-size="11" fill="#388e3c">(APA 직후)</text>
  <!-- ≤72시간 -->
  <line x1="360" y1="134" x2="360" y2="154" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="275" y="154" width="170" height="40" rx="6" fill="#fff8e1" stroke="#f57f17" stroke-width="1.5"/>
  <text x="360" y="170" text-anchor="middle" font-weight="bold" fill="#e65100" font-size="13">≤72시간 이내</text>
  <text x="360" y="186" text-anchor="middle" font-size="11" fill="#f57f17">세정만 추가</text>
  <!-- >72시간 -->
  <line x1="560" y1="134" x2="560" y2="154" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="470" y="154" width="180" height="40" rx="6" fill="#fce4ec" stroke="#c62828" stroke-width="1.5"/>
  <text x="560" y="170" text-anchor="middle" font-weight="bold" fill="#b71c1c" font-size="13">&gt;72시간 경과</text>
  <text x="560" y="186" text-anchor="middle" font-size="11" fill="#c62828">Re-APA 필수</text>
  <!-- 세 갈래 → 합류 -->
  <line x1="160" y1="194" x2="160" y2="254" stroke="#555" stroke-width="1.5"/>
  <line x1="360" y1="194" x2="360" y2="254" stroke="#555" stroke-width="1.5"/>
  <line x1="560" y1="194" x2="560" y2="254" stroke="#555" stroke-width="1.5"/>
  <line x1="160" y1="254" x2="560" y2="254" stroke="#555" stroke-width="2"/>
  <line x1="360" y1="254" x2="360" y2="270" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <!-- 최종 -->
  <rect x="170" y="270" width="380" height="40" rx="6" fill="#ede7f6" stroke="#4527a0" stroke-width="2"/>
  <text x="360" y="295" text-anchor="middle" font-weight="bold" fill="#311b92" font-size="14">세정 → 10-MDP → 레진 접착</text>
  <!-- 화살표 마커 -->
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#555"/>
    </marker>
  </defs>
</svg>

분기점 = **APA 후 경과 시간**

---

## Step 1 — APA (Airborne Particle Abrasion, 공기입자연마)

> = 샌드블라스팅. 기공소에서 미리 시행하거나 임상에서 직접 시행

### 표준 파라미터

| 파라미터 | 권장값 | 주의 |
|---|---|---|
| **입자 크기** | 50 µm alumina | 25–150 µm 범위 (Nasri 2025) |
| **압력** | 0.1–0.2 MPa | 최대 0.45 MPa 이하 |
| **처리 시간** | 10–20초 | 20초 초과 시 표면 손상 위험 |
| **거리** | 10 mm | 5–20 mm 범위 |
| **방향** | 90° 수직 | 사각도 금지 |

---

## Step 2 — 세정 선택: 경과 시간에 따른 분기

APA 완료 후 → **몇 시간이 경과했는가?**

```
즉시 (< 몇 시간)          ≤ 72시간              > 72시간
        │                     │                     │
        ▼                     ▼                     ▼
  증류수 세척 10s         Ivoclean 20s          ⛔ Katana 금지
  에어 건조               수세 10s              → re-APA 시행
                          에어 건조             → Ivoclean 20s
```

---

## ✅ 즉시 세팅 (APA 직후)

**상황**: 기공소에서 APA 완료 → 당일 오전 / 오후 바로 세팅

### 프로토콜

1. **증류수 세척** 10초 → 에어 건조
2. **10-MDP 프라이머** 도포 → 20–30초 → 가볍게 에어 건조
3. **레진 시멘트** (MDP 함유 권장) 적용 후 접착

> Al-Akhali 2025: 즉시 세팅 그룹 TBS = 단기에서 Ivoclean 세정군과 동등

---

## ✅ ≤72시간 이내 세팅 (Ivoclean 프로토콜)

**상황**: 기공소 납품 후 다음날 ~ 3일 이내 세팅

### Ivoclean 프로토콜

| 단계 | 조작 |
|---|---|
| 1 | Ivoclean 적용, 20초 대기 |
| 2 | 증류수 수세 10초 |
| 3 | 에어 건조 |
| 4 | 10-MDP 프라이머 도포 |
| 5 | 레진 시멘트 접착 |

> **Ivoclean SFE = 68.4 mN/m** — 세정제 중 최고값 (Al-Akhali 2025)

---

## ⚠️ >72시간 경과 — Re-APA 필수

**상황**: APA 후 72시간 초과 → 오염막 재형성

### 처리 순서

```
Re-APA (새로 시행)
    ↓
Ivoclean 20s → 수세 → 에어 건조
    ↓
10-MDP 프라이머
    ↓
레진 시멘트 접착
```

> Al-Akhali 2025: 72시간이 "한계"가 아닌 **연구된 기준점** — 임상 판단 필요

---

## ⛔ Katana Cleaner — 사용 금지

### 왜 금기인가?

| 세정제 | SFE (mN/m) | 단기 TBS | 장기 TBS |
|---|---|---|---|
| **Ivoclean** | **68.4** | ✅ 양호 | ✅ 양호 |
| Monobond Plus | 54.2 | 양호 | 양호 |
| **Katana Cleaner** | **33.1** | 단기 비슷 | ⛔ **불량** |
| 미처리 (APA만) | — | 가변 | 가변 |

> **Katana Cleaner는 APA로 얻은 표면 에너지를 오히려 낮춘다**
> → 단기 접착력이 비슷해도 장기 내구성 저하

---

## 10-MDP 프라이머 — 접착의 핵심 화학

### 작용 기전

```
MDP의 인산기 (-OPO₃H₂)
        ↕  화학적 결합
ZrO₂ 표면의 Zr-OH (수산기)
```

- APA가 ZrO₂ 표면을 **거칠게** (기계적 유지) + **세정**(화학적 유지 준비)
- MDP가 **ZrO₂와 화학결합** + 레진과 공유결합

> Nasri 2025 Umbrella SR (8편 SR, 233연구): **APA + 10-MDP = 가장 검증된 조합**

---

## 레진 시멘트 선택

### 권장 조건

- **MDP 함유 자기접착 레진 시멘트** 또는
- **MDP 함유 접착제** + 레진 시멘트 콤보

### 사용 금지

- 인산아연 시멘트 (zinc phosphate) — 화학적 결합 없음
- 글래스아이오노머 — 지르코니아와 결합 불가
- MDP 없는 레진 시멘트 단독 — 프라이머 없이 사용 시 불안정

---

## 글리세린 겔 도포 — 최종 광중합 전 필수

### 왜 필요한가?

레진 시멘트는 **산소 억제층 (Oxygen Inhibition Layer, OIL)** 때문에 표면이 완전히 중합되지 않는다.

- 산소가 광중합 라디칼을 소거 → 표면 1~5 µm 미중합 (Suh 2004)
- OIL 두께는 레진 점도에 반비례 — 점도↑ 시 산소 확산↓ → 표면 중합전환도 (Degree of Conversion, DC) ↑ (Gauthier 2005)
- **글리세린 침지 = OIL 완전 차단** → DC·경도 최고값; 진공처리보다 우월 (Lim 2022, n=16/group)

### 방법

| 단계 | 내용 |
|---|---|
| 1. 잉여 시멘트 제거 | 광중합 전 탐침 · 플로스로 제거 |
| 2. 교합지 체크 | 간섭점 조정 완료 후 |
| 3. 글리세린 겔 도포 | **모든 마진 라인 + 접착면 전체**에 도포 (산소 차단) |
| 4. 최종 광중합 | **각 면 20초 이상** (협·설·인접면 별도) |
| 5. 글리세린 세척 | 수세 후 에어 건조 → 표면 광택 확인 |

> **근거**: Gauthier 2005 (J Dent Res) — 점도·산소확산 메커니즘 · Lim 2022 (J Mech Behav Biomed Mater) — 글리세린 > 진공 > 대조군 (DC·경도)

---

## 임상 체크리스트 — 세팅 당일

```
□ APA 시행일시 확인 → 72시간 경과 여부 판단
□ 경과 > 72h: Re-APA 시행
□ Ivoclean 20초 → 수세 → 에어 건조
□ Katana Cleaner 세팅 트레이에 없는지 확인 ⛔
□ 10-MDP 프라이머 충분히 도포 → 에어 건조
□ 레진 시멘트 MDP 함유 여부 확인
□ 잉여 시멘트 제거 → 교합 조정
□ 글리세린 겔 도포 → 각 면 20초 이상 광중합
□ 글리세린 수세 → 마진 확인
```

---

## 근거 요약

| 논문 | 디자인 | 핵심 기여 |
|---|---|---|
| **Al-Akhali 2025** | In vitro RCT-급 비교 | Ivoclean SFE 68.4 mN/m 최고값; Katana Cleaner 금기; 72h 기준 |
| **Nasri 2025** | Umbrella SR (8편 SR, 233연구) | APA + 10-MDP = 가장 검증된 조합; APA 파라미터 범위 |
| **Gauthier 2005** | In vitro (Raman 분광) | OIL 메커니즘: 점도↑ → 산소확산↓ → DC↑; 110°C 이상 → OIL 소거 |
| **Lim 2022** | In vitro (n=16/group) | 글리세린 침지 > 진공 > 대조군 (DC·경도); GL+80°C = 최적 |

---

<!-- _class: lead -->

## 요약

**APA → Ivoclean 20s → 10-MDP → 레진 시멘트**

- 즉시: 증류수 세척으로 대체 가능
- ≤72h: Ivoclean
- >72h: Re-APA + Ivoclean
- Katana Cleaner는 쓰지 않는다

---

*슬라이드 출처: Al-Akhali 2025 (PMID: 41362452) · Nasri 2025 (Umbrella SR) · Gauthier 2005 (J Dent Res) · Lim 2022 (J Mech Behav Biomed Mater)*
*작성일: 2026-11-05 | 업데이트: 2026-11-05 | LLM Wiki — Dentopedia*
