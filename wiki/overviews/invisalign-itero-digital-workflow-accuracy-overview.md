---
title: "Invisalign + iTero: 디지털 워크플로우와 이동 정확도 종합"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-09-04
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [orthodontics, clear-aligner, invisalign, itero, intraoral-scanner, digital-workflow, clincheck, accuracy, predictability, distalization, transverse-expansion, torque, intrusion, overcorrection, anchorage-loss, practice-economics, overview]
relations:
  - type: extends
    target: mackay-2017-acquisition-digital-intraoral-scanning-device
  - type: extends
    target: saif-2026-clear-aligner-anterior-3d-accuracy
  - type: extends
    target: goncalves-2023-invisalign-upper-incisor-accuracy-sr
  - type: extends
    target: xianggang-2026-predictability-maxillary-transverse-changes-invisalign
  - type: extends
    target: algarni-2026-treatment-predictability-two-clear-aligner
  - type: extends
    target: liu-2025-maxillary-molar-distalization-invisalign-adult
  - type: extends
    target: saif-2022-efficiency-evaluation-maxillary-molar-distalization
  - type: extends
    target: de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables
  - type: extends
    target: de-la-rosa-gay-2025-expansion-predictability-clear-aligner
  - type: refines
    target: christopoulou-2022-intraoral-scanners-orthodontics-critical-review
  - type: refines
    target: singh-2025-intraoral-scanners-accuracy-umbrella-review
  - type: reinforces
    target: clear-aligner-indications-limitations
---

> [!summary] 한국어 핵심요약
> - **iTero는 Align Technology 생태계의 전용 스캐너** — 교정의 중 디지털 사용자의 86%가 선택(Christopoulou 2022); 도입 시 Invisalign 시작 건수 +20.71% 증가(Mackay 2017, ITS, 제조사 데이터 — 연관성 수준)
> - **학습곡선**: iTero는 TRIOS보다 학습속도 빠르지만 평균 스캔 시간은 더 길고, TRIOS는 학습곡선이 느리지만 숙련 후 스캔 시간이 일정함 (Christopoulou 2022)
> - **구개주름(Palatal Rugae) 중첩**: 인비절라인 결과 계측의 표준 방법론 — iTero 3D 모델을 T0/T1/T2에서 구개주름 부위로 정합해 예측 대 실제 이동 비교 (Liu 2025, Saif 2022)
> - **ClinCheck 아치폭 표의 신뢰성**: 독립 계측(Geomagic Control X)과 교합면 기준 편향 0.03 mm — "측정도구"는 신뢰할 수 있음; "얼라이너가 계획을 달성한다"는 별개 문제 (de-la-Rosa-Gay 2026)
> - **전치부 이동 정확도 전체 평균 50.3%** (상악 47.6%, 하악 53%) — 재치료 없는 초기 세트 기준 (Saif 2026)
> - **최악 이동: 상악 절치 압하(Intrusion) 23.1%** → 가장 예측 불가능; 방향이 역전되어 정출(Extrusion)로 이어진 사례도 보고 (Saif 2026, Goncalves 2023)
> - **최고 이동: 정출(Extrusion) 최대 142.4%** — 과달성 경향 (Goncalves 2023)
> - **Torque(근첨이동)**: 49–51% — 교정적으로 가장 중요하지만 얼라이너 단독으로는 신뢰 불가 (Goncalves 2023)
> - **횡적 확장(Transverse Expansion)**: 견치 72%, 제1소구치 81%, 제2소구치 79%, 제1대구치 72% — 가장 예측도 높은 이동 유형 (Xianggang 2026 SR+MA)
> - **수직이동: 두 브랜드 모두 불량** — Invisalign "신뢰불가", Eon도 변동성 높음; 수직교정은 얼라이너 단독 계획 금지 (Algarni 2026)
> - **대구치 원심이동(Distalization): 체이동이 아닌 경사이동** — U6 1.71mm, U7 2.04mm, 원심경사 5.2–5.4°; 전치부 고정원 손실은 Class II 고무줄로도 방지 불가 → TAD 필요 (Liu 2025)
> - **임상 결론**: ClinCheck는 모든 이동 유형을 과대예측; 임상가는 이동유형별 정확도 격차를 인식하고 ① 압하·Torque는 과교정 + 어태치먼트 필수, ② 원심이동은 TAD 고려, ③ 횡적 확장은 비교적 신뢰 가능하되 여전히 ~20–30% 부족으로 과교정 계획

## Three-line Summary

Invisalign and iTero form a vertically integrated digital orthodontic ecosystem: iTero is the predominant intraoral scanner (IOS) among orthodontic digital users (86%), and its acquisition is associated with a significant increase in Invisalign treatment starts (+20.71%, ITS; Mackay 2017 — manufacturer data, association only); digitally, iTero 3D models superimposed via palatal-rugae registration are the de-facto measurement standard for ClinCheck accuracy research, and ClinCheck arch-width table values have been independently metrologically validated (de-la-Rosa-Gay 2026).

Across movement types, Invisalign's ClinCheck systematically overestimates achieved tooth movement: overall anterior accuracy is 50.3% with first-set-only (no refinement) treatment (Saif 2026); maxillary incisor intrusion is the worst (23.1%), torque is poor (49–51%), transverse expansion is the most predictable (72–81% by region, SR+MA Xianggang 2026), and molar distalization is primarily tipping-not-bodily with anterior anchorage loss that Class II elastics cannot fully mitigate (Liu 2025).

The clinical synthesis: plan overcorrection for virtually all tooth movements, never plan intrusion or vertical correction with aligners alone, add TADs for substantial distalization, and treat ClinCheck's virtual setup as an upper-bound estimate rather than an achievable target — refinements should be expected after first-set treatment in most cases.

## 세줄요약

인비절라인(Invisalign)과 아이테로(iTero)는 수직통합 디지털 교정 생태계를 구성: 교정과 디지털 사용자의 86%가 iTero를 선택하고, 도입 시 Invisalign 시작 건수가 유의하게 증가하지만(+20.71%, ITS, 제조사 데이터 — 연관성 수준; Mackay 2017), 디지털 측면에서 iTero 3D 모델의 구개주름 중첩(palatal rugae registration)이 ClinCheck 정확도 연구의 사실상 표준이며, ClinCheck 아치폭 표 수치의 독립적 계측 타당성도 검증됨(de-la-Rosa-Gay 2026).

이동 유형별로 ClinCheck는 달성 치아이동을 일관되게 과대예측: 전치부 정확도 전체 평균 50.3%(재치료 없는 초기 세트 기준; Saif 2026), 상악 절치 압하가 최저(23.1%), Torque 저조(49–51%), 횡적 확장이 가장 예측가능(부위별 72–81%; Xianggang 2026 SR+MA), 대구치 원심이동은 경사이동 위주·전치부 고정원 손실 동반으로 Class II 고무줄만으로 불충분(Liu 2025).

임상 종합: 사실상 모든 이동 유형에 과교정 계획 필요; 압하·수직이동은 얼라이너 단독 절대 금지; 상당한 원심이동에는 TAD 추가 고려; ClinCheck 가상 셋업은 달성 가능한 결과가 아닌 상한 추정치로 취급할 것 — 대부분 케이스에서 초기 세트 후 재치료(Refinement)를 예상해야 함.

---

## 1. iTero in the Invisalign Ecosystem

### 1-1. Practice Uptake and Economics

iTero (Align Technology, Santa Clara, CA) is the proprietary intraoral scanner of the Invisalign ecosystem. Among orthodontists already using digital study models, 86% use iTero — higher than any other device brand [[digital-workflow/christopoulou-2022-intraoral-scanners-orthodontics-critical-review]].

From a practice-economics perspective, [[practice-management/mackay-2017-acquisition-digital-intraoral-scanning-device]] analyzed 1,871 GP and orthodontic practices worldwide using interrupted time series (ITS) analysis over 48 months. At the month of iTero acquisition, Invisalign treatment starts increased significantly:

| Group | Effect at acquisition (month 25) | 12-month projection |
|---|---|---|
| All practices (n=1,871) | b=0.49, p<0.001; +20.71% vs. counterfactual | +5.92 receipts |
| Low-volume NA GPs (n=319, ≤5 prior-year receipts) | b=0.28, p<0.001; persisted ≥24 months | +3.41 receipts |

**Critical appraisal**: The outcome is Align Technology's own Invisalign receipt data with no non-Invisalign comparator, no cost-side accounting (scanner capital + per-scan cost not netted), and no ability to separate a scanner effect from concurrent marketing or organic growth. Read as association evidence for a capital-equipment purchase decision, not as net ROI or causal proof.

### 1-2. Scanner Performance in Orthodontic Context

iTero's learning curve characteristics differ from competing devices. Christopoulou 2022 (narrative review, orthodontic in-vivo studies) reports:
- **Faster learning rate** vs. TRIOS Classic — clinicians reach proficiency more quickly
- **Longer average scan time** vs. TRIOS — even after learning, scans take more time per patient
- **TRIOS**: slower to learn but mean scan time is shorter and **experience-independent** once learned

For full-arch accuracy in the restorative/prosthodontic context, [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] ranks **TRIOS 3 and Primescan** highest. iTero is not ranked highest in this context — but Singh 2025's evidence base is restorative (crown/bridge/edentulous full-arch), not orthodontic diagnostic models, so this ranking does not directly transfer to the Invisalign treatment monitoring context.

---

## 2. Digital Measurement Methodology

### 2-1. Palatal Rugae Registration — The Standard for Invisalign Accuracy Research

Serial 3D superimposition of iTero digital models via the **palatal rugae area** is the established method for measuring predicted-vs-achieved tooth movement in Invisalign research. The palatal rugae are stable, non-moving landmarks through orthodontic treatment, making them an ideal registration zone:

- [[orthodontics/clear-aligner/saif-2022-efficiency-evaluation-maxillary-molar-distalization]] — used iTero + palatal-rugae superimposition for 38-patient molar distalization study
- [[orthodontics/clear-aligner/liu-2025-maxillary-molar-distalization-invisalign-adult]] — serial iTero scans at T0/T1/T2 using 12-point crown landmark scheme with palatal-area registration
- This approach enables per-stage measurement (after U7, after U6) and correlation analysis between movement magnitude and anchorage loss

### 2-2. ClinCheck Arch-Width Table Validation

A common research question: can ClinCheck's internal arch-width table numbers be trusted as measurement data? [[orthodontics/clear-aligner/de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables]] provides the first independent metrological answer.

**Study design**: 35 adults (Invisalign SmartTrack), 840 paired arch-width measurements across 3 ClinCheck timepoints, measured with Geomagic Control X vs. ClinCheck's reported values. Mixed-effects Bland–Altman with patient-level random intercepts.

| Reference point | Bias | 95% Limits of Agreement |
|---|---|---|
| Occlusal (Align's internal reference) | **0.03 mm** | −0.78 to +0.84 mm |
| Cusp tip | +0.21 mm | ~−1.0 to +1.5 mm |
| Gingival | −0.30 to −0.48 mm | up to ±1.8 mm |

**Key distinction**: This validates the *measurement tool* — ClinCheck's table numbers agree with independent measurement. It does **not** validate that the aligner achieves the planned expansion. The "discrepancy" variable (observed minus predicted expansion) was the most stable metric across all reference points.

---

## 3. Movement-Type Accuracy: Evidence Matrix

### 3-1. Anterior Teeth (Incisors to Canines)

**[[orthodontics/clear-aligner/saif-2026-clear-aligner-anterior-3d-accuracy]]** — 40 adults, 480 anterior teeth, first-set only (no refinement), 10-day wear, Invisalign:

| Movement type | Upper arch | Lower arch |
|---|---|---|
| **Overall mean** | **47.6%** | **53%** |
| Vertical (intrusion) | **23.1% (worst)** | — |
| Mesiodistal rotation | — | — |
| Distal crown tipping | 64.85% | — |
| Lingual tipping | — | **75.52% (best lower)** |
| Labial tipping | — | 66.51% |
| Mesial rotation | 63.32% | — |

All movement types showed significant predicted-vs-achieved differences (p<0.05).

**[[orthodontics/clear-aligner/goncalves-2023-invisalign-upper-incisor-accuracy-sr]]** — SR of 5 studies, 612 upper-incisor movements, SmartTrack era:

| Movement | Accuracy range |
|---|---|
| Torque (3rd-order root movement) | **49.1–51.5%** |
| Rotation | 41.8–66.2% |
| Mesiodistal tipping | 38.5–155.7% |
| Horizontal translation | 67.6–78.9% |
| **Extrusion** | **Up to 142.4% (over-achieved)** |
| **Intrusion** | **0% in worst case** (reversed to extrusion due to bite-block effect) |

> **Clinical red flag**: Intrusion of upper incisors predicted by ClinCheck may produce the opposite movement (extrusion) in some patients — attributed to posterior-tooth superimposition acting as a bite block.

### 3-2. Transverse Arch Width

**[[orthodontics/clear-aligner/xianggang-2026-predictability-maxillary-transverse-changes-invisalign]]** — SR+MA, 6 retrospective studies, 233 adults:

| Region | Pooled predictability | 95% CI | I² | GRADE |
|---|---|---|---|---|
| Canine (intercanine) | **72.01%** | 59.67–84.35% | 74.7% | Low |
| 1st premolar | **80.73%** | 73.78–87.68% | 43.5% | High |
| 2nd premolar | **78.74%** | 70.41–87.08% | 57.4% | Moderate |
| 1st molar | **71.57%** | 62.41–80.73% | 50.2% | Moderate |

Rule of thumb: roughly **0.72–0.81 mm achieved per 1 mm programmed**, consistently across all regions. Overcorrection is implied but no specific number is evidence-based. Canine region has the most heterogeneous, least certain evidence.

**Brand comparison** — [[orthodontics/clear-aligner/algarni-2026-treatment-predictability-two-clear-aligner]] (Invisalign vs. Eon, n=76, pre-refinement):

| Movement | Invisalign | Eon Aligner | Verdict |
|---|---|---|---|
| Interpremolar/intercanine width | 0.06–0.34 mm error | Similar | ≈ Equal (both near Camardella 0.4 mm threshold) |
| Mesiodistal rotation (incisors) | Significant bias | 1.9–4.2° less bias | Eon better |
| Horizontal movement | 0.206–0.341 mm | 0.015–0.24 mm | Eon better |
| Vertical movement | **"Unreliable"** | Moderate/fluctuating | Both poor |

### 3-3. Molar Distalization

**[[orthodontics/clear-aligner/liu-2025-maxillary-molar-distalization-invisalign-adult]]** — 12 adults, iTero serial models T0/T1/T2:

| Outcome | U6 (T0→T2) | U7 (T0→T2) |
|---|---|---|
| Distalization achieved | 1.71 ± 0.89 mm | 2.04 ± 1.16 mm |
| Distal tipping | −5.20 ± 2.62° | −5.35 ± 4.19° |
| U6 distopalatal rotation | +2.83 ± 2.45° | — |
| U1 sagittal anchorage loss | −0.88 ± 0.99 mm | — |
| U1 torque change | +3.58 ± 4.69° | — |

Mechanism: **tipping, not bodily movement** — significant distal crown tipping without root-parallel translation. Class II intermaxillary elastics did not prevent anterior anchorage loss. Sequential distalization causes a small U7 mesial rebound (−0.21 mm, NS) when U6 begins moving, attributed to progressive loss of posterior anchor teeth.

**[[orthodontics/clear-aligner/saif-2022-efficiency-evaluation-maxillary-molar-distalization]]** — 38 adults, iTero + palatal-rugae superimposition:
- Predicted vs. achieved distalization: significantly different for both U6 and U7 (both p<0.0001)
- Mean prescribed distalization: **2.6 mm** achievable
- Attachments on molars did **not** enhance the molars' own distalization movement
- Correlation: more distalization → more anterior anchorage loss (central incisor r=0.39, lateral r=0.36)

---

## 4. Clinical Decision Framework

### 4-1. Movement-Type Triage

```
HIGH confidence (plan as-is, mild overcorrection):
  ✅ Extrusion (up to over-achieved — monitor for over-expression)
  ✅ Horizontal translation (67–79%)
  ✅ Transverse expansion, premolar region (79–81%, GRADE High)

MODERATE confidence (overcorrect 20–30%, monitor):
  ⚠️ Rotation (42–66%)
  ⚠️ Transverse expansion, canine/molar regions (72%, GRADE Low–Moderate)
  ⚠️ Tipping (variable, 39–65%)

LOW confidence (overcorrect aggressively + attachment mandatory):
  ⛔ Torque (49–51% — Power Ridge / optimized attachments improve but do not resolve)
  ⛔ Intrusion (23% overall; can reverse to extrusion — consider supplemental mini-screw)

AVOID ALIGNER ALONE:
  🚫 Vertical correction (both Invisalign and Eon: unreliable/fluctuating)
  🚫 Large distalization without TAD — tipping inevitable, anchorage loss expected
```

### 4-2. Distalization Protocol Implications

Based on Liu 2025 and Saif 2022:
1. **Expect tipping, not bodily movement** — root angulation post-distalization will need correction
2. **Class II elastics alone are insufficient** for anchorage protection; TADs should be the default for >2 mm per molar
3. **Sequential distalisation** (U7 first, then U6) causes U7 mesial rebound when U6 starts — build this into plan timing
4. **Correlation between distalization magnitude and anchorage loss** — the more ambitious the distal movement, the greater the anterior loss; size plans accordingly

### 4-3. The "ClinCheck as upper bound" principle

ClinCheck overestimates achievement in virtually every movement category. The validated implication:
- **Initial case presentation**: do not show ClinCheck animation as the "guaranteed result"
- **First-set completion**: expect refinement in nearly all cases involving torque, rotation, or intrusion
- **Research context**: ClinCheck arch-width table numbers are metrologically reliable (de-la-Rosa-Gay 2026); the gap between plan and outcome reflects aligner biomechanics, not measurement error

---

## 5. Evidence Map

| Domain | Key Paper | Evidence Level | Core Finding |
|---|---|---|---|
| iTero practice economics | [[practice-management/mackay-2017-acquisition-digital-intraoral-scanning-device]] | retrospective (ITS) | +20.71% Invisalign starts post-acquisition (assoc., mfr data) |
| iTero vs. IOS devices | [[digital-workflow/christopoulou-2022-intraoral-scanners-orthodontics-critical-review]] | narrative review | 86% orthodontist iTero choice; faster learn, longer scan |
| IOS full-arch accuracy | [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] | sr+ma (umbrella) | TRIOS 3 / Primescan highest (restorative context) |
| ClinCheck arch-width validation | [[orthodontics/clear-aligner/de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables]] | retrospective | Occlusal bias 0.03mm — tool reliable; achievement ≠ validated |
| Anterior 3D accuracy (first-set) | [[orthodontics/clear-aligner/saif-2026-clear-aligner-anterior-3d-accuracy]] | retrospective | Overall 50.3%; intrusion 23.1%; all types p<0.05 |
| Upper incisor accuracy SR | [[orthodontics/clear-aligner/goncalves-2023-invisalign-upper-incisor-accuracy-sr]] | sr | Torque 49–51%; extrusion 142.4%; intrusion may reverse |
| Transverse expansion SR+MA | [[orthodontics/clear-aligner/xianggang-2026-predictability-maxillary-transverse-changes-invisalign]] | sr+ma | Canine 72%, PM1 81%, molar 72%; overcorrection implied |
| Brand comparison (Invisalign vs Eon) | [[orthodontics/clear-aligner/algarni-2026-treatment-predictability-two-clear-aligner]] | retrospective | Both need overcorrection; vertical unreliable in both |
| iTero molar distalization (serial) | [[orthodontics/clear-aligner/liu-2025-maxillary-molar-distalization-invisalign-adult]] | retrospective | U6 1.71mm, U7 2.04mm; tipping-dominant; TAD needed |
| Distalization + anchorage | [[orthodontics/clear-aligner/saif-2022-efficiency-evaluation-maxillary-molar-distalization]] | retrospective | 2.6mm prescribable; attachments ≠ enhanced distalization |

---

## Related Overviews

- [[overviews/clear-aligner-indications-limitations]] — broader clear aligner indication/limitation synthesis (periodontal, TMJ, OHRQoL, complex cases); this overview is its iTero/accuracy-specific companion
- [[overviews/digital-workflow-decision-ladder]] — when to use IOS vs. conventional impression across all clinical contexts
