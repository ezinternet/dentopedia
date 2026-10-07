---
title: "Digital workflow for implant-supported restorations in the mandible including reverse scan bodies: a feasibility study"
authors: Kernen-Gintaute A, Akulauskas M, Kernen F, Wenger S, Zitzmann NU, Spies BC, Burkhardt F
year: 2026
date: 2026-08-04
doi: 10.1186/s12903-026-09507-9
pmid: "42668365"
pmcid: "PMC13526298"
source: kernen-gintaute-2026-digital-workflow-for-implant-supported.md
category: [implants/full-arch]
evidence_level: retrospective
source_collection: pubmed-text
text_path: /Users/oracleneo/llm-wiki/papers/kernen-gintaute-2026-digital-workflow-for-implant-supported.txt
text_filename: kernen-gintaute-2026-digital-workflow-for-implant-supported.txt
tags: [digital-workflow, reverse-scan-body, intraoral-scanner, TRIOS, verification-bar, edentulous-mandible, passive-fit, Sheffield-test, model-free, CAD-CAM]
relations:
  - type: extends
    target: mijiritsky-2026-segmented-full-arch-digital-workflow-mandible
  - type: compares
    target: pozzi-2025-photogrammetry-versus-intraoral-scanning-in
  - type: compares
    target: papaspyridakos-2024-reverse-scan-body-double-full-arch-zirconia
---

> [!summary] 한국어 핵심요약
> - **핵심 명제**: 무치악 하악 2임플란트 모델프리 디지털 워크플로우(IOS→VB) 정확도 검증 — **IOS→VB 편차 12µm/0.18°로 우수**, 단 **구강내 스플린팅(SVB) 시 유의한 열화(50µm/0.79°)** 발생
> - **연구 규모**: 단일 환자, 10회 반복 스캔(n=10), TRIOS 4 IOS, Exocad/PowerMill, Straumann Variobase 모델프리 시멘트 고정
> - **임상적 피트**: 10개 VB 모두 Sheffield test 포함 **임상적 수동적 피트 달성**
> - **핵심 발견**: 구강내 스플린팅(아크릴 재연결) → 선형 50µm(p=0.001), 각도 0.79°(p=0.01) 유의 증가; 리버스 스캔바디 신규 VB(NVB)로 회복 가능(26µm/0.06°, n.s.)
> - **임상 시사점**: 모델프리 워크플로우 자체는 정확하나, 구강내 스플린팅 단계가 정확도 저하 주범 → 리버스 스캔바디 활용 신규 프레임워크 제작 권장

## Three-line Summary

Single-patient prospective feasibility study of model-free digital workflow for edentulous mandible with two canine implants: 10 intraoral scans (TRIOS 4) → CAD/CAM titanium verification bars (VBs) with adhesively cemented Ti-bases (no physical model); all 10 VBs clinically passive (Sheffield test); intraoral re-splinting (SVB) vs new VB with reverse scan bodies (NVB) compared via metrology (Geomagic Control X).

IOS→VB linear deviation 12 µm (p=0.23), angular 0.18° (p=0.50) — excellent accuracy; VB→SVB (intraoral splinting) degradation: linear 50 µm (p=0.001), angular 0.79° (p=0.01); SVB→NVB (reverse scan body recovery): linear 26 µm (p=0.20), angular 0.06° (p=0.82) — non-significant recovery.

Model-free digital workflow achieves clinically acceptable accuracy for edentulous mandible; intraoral splinting is the major accuracy-degrading step; reverse scan body workflow restores accuracy — supports clinical adoption of model-free protocols with reverse scan bodies for full-arch cases.

## 세줄요약

단일 환자, 무치악 하악 2임플란트, 모델프리 디지털 워크플로우(IOS→VB) 10회 반복 검증.

IOS→VB 12µm/0.18° 우수; 구강내 스플린팅(SVB) 시 50µm/0.79° 유의 열화; 리버스 스캔바디 신규 VB(NVB)로 26µm/0.06° 회복.

모델프리 워크플로우 자체 정확하나 구강내 스플린팅이 주 열화 원인; 리버스 스캔바디 프로토콜로 해결 가능.

## Study Design

| Item | Detail |
|---|---|
| **Type** | Single-patient prospective clinical feasibility (repeated measures) |
| **Setting** | University of Freiburg / University of Basel |
| **Patient** | Edentulous mandible, 2 tissue-level implants (canine regions #33, #43) |
| **n** | 10 repeated intraoral scans (IOS group) |
| **IOS** | TRIOS 4 (3Shape, v21.2.0), calibrated, standardized lighting |
| **Scan bodies** | Mounted throughout entire impression process |
| **CAD/CAM** | Exocad Dental CAD 3.1 Rijeka 8349; PowerMill 2016 R2 |
| **VB Fabrication** | Titanium verification bar; Straumann RN Variobase for bridge/bar cylindrical (5×3.5 mm) |
| **Cementation** | Dual-cure resin cement (Multilink Hybrid Abutment); **model-free** |
| **Clinical Fit Test** | Visual, tactile, Sheffield test (probe) — all 10 VBs passive |
| **Splinting Protocol** | VB sectioned → intraoral re-splinting with light-cure acrylic (SVB) |
| **Reverse Scan Body** | New VB (NVB) fabricated with reverse scan bodies attached extraorally |
| **Metrology** | Geomagic Control X 2018.1.2; STL superposition, reference coordinate system at scan body coronal surface |
| **Statistics** | Descriptive/exploratory (Shapiro-Wilk, Levene, repeated-measures ANOVA); no formal sample size calculation |

## Key Results

### Linear Deviations (Inter-implant Distance)

| Comparison | Mean Diff (µm) | p-value | Clinical Significance |
|---|---|---|---|
| **IOS → VB** (model-free transfer) | **12** | 0.23 (ns) | **Excellent** — within clinical tolerance |
| **VB → SVB** (intraoral splinting effect) | **50** | **0.001** | **Significant degradation** |
| SVB → NVB (reverse scan body recovery) | 26 | 0.20 (ns) | Recovery to near-VB accuracy |
| IOS → SVB (combined IOS+splinting) | 62 | <0.001 | Largest cumulative error |
| IOS → NVB (IOS + reverse scan body) | 36 | 0.29 (ns) | Acceptable |
| VB → NVB (VB vs reverse scan body VB) | 24 | 0.64 (ns) | Equivalent |

### Angular Deviations (Inter-implant Angle)

| Comparison | Mean Diff (°) | p-value | Clinical Significance |
|---|---|---|---|
| **IOS → VB** | **0.18** | 0.50 (ns) | **Excellent** |
| **VB → SVB** | **0.79** | **0.01** | **Significant degradation** |
| SVB → NVB | 0.06 | 0.82 (ns) | Full recovery |
| IOS → SVB | 0.97 | <0.001 | Largest cumulative |
| IOS → NVB | 0.91 | 0.02 | Borderline |
| VB → NVB | 0.73 | 0.17 (ns) | Equivalent |

### Clinical Outcomes

- **10/10 VBs**: Clinically passive fit (Sheffield test + visual/tactile)
- **Model-free cementation**: Feasible without physical model
- **Maximum single deviation**: 126 µm outlier in SVB→NVB (single case)

## Key Contributions

1. **Model-free workflow validated**: IOS→VB transfer accuracy (12 µm, 0.18°) supports eliminating physical model for edentulous mandible 2-implant cases
2. **Intraoral splinting quantified as major error source**: 50 µm / 0.79° degradation — previously suspected, now measured with clinical try-in
3. **Reverse scan body recovery demonstrated**: NVB restores accuracy to VB-equivalent levels (24 µm, 0.73°; both n.s.)
4. **Clinical try-in as gold standard**: Not just theoretical thresholds — rigid titanium VBs tested in mouth (Sheffield test)
5. **Single-patient repeated-measures design**: Controls inter-patient variability; isolates workflow-inherent errors

## Methodology Details

**Scanning Protocol**: Occlusal start Q4 → contralateral → lingual → buccal; lip/cheek retractor (OptraGate); experienced operator (A.K.-G.)

**Verification Bar Design**: Titanium, screw-retained to implants; Variobase cemented extraorally on VB

**Splinting Procedure**: VB sectioned at midpoint → intraoral re-splinting with light-polymerizing acrylic resin (Pattern Resin LS, GC) → SVB

**Reverse Scan Body Workflow**: Reverse scan bodies attached to implants intraorally → scanned → NVB designed/milled extraorally → Ti-bases cemented on NVB

**Coordinate System**: Vertical axis through scan body center; reference plane at coronal surface of scan bodies; linear = intersection points on reference plane; angular = orientation of vertical axes

## Clinical Implications

| Finding | Clinical Action |
|---|---|
| Model-free IOS→VB accurate | Adopt model-free workflow for 2-implant edentulous mandible |
| Intraoral splinting degrades accuracy | Avoid intraoral acrylic splinting of verification bars; use reverse scan bodies instead |
| Reverse scan bodies recover accuracy | Implement reverse scan body protocol for full-arch prototype/framework verification |
| Clinical passive fit achieved | Digital workflow + model-free fabrication = clinically acceptable for immediate loading protocols |

## Limitations

- Single patient (n=1), two parallel implants — cannot generalize to divergent/angled implants, maxilla, or >2 implants
- Descriptive statistics only — no hypothesis testing powered
- Experienced operator only — operator variability not assessed
- One IOS system (TRIOS 4) — scanner generalizability unknown
- Short-term — no long-term prosthetic outcome data

## Related Papers

- [[implants/full-arch/mijiritsky-2026-segmented-full-arch-digital-workflow-mandible]] — segmented digital workflow for mandible; complementary clinical protocol
- [[implants/full-arch/pozzi-2025-photogrammetry-versus-intraoral-scanning-in]] — photogrammetry vs IOS accuracy; benchmarks for full-arch
- [[implants/full-arch/papaspyridakos-2024-reverse-scan-body-double-full-arch-zirconia]] — reverse scan body workflow for double-arch zirconia; clinical application
- [[implants/full-arch/andriessen-2014-applicability-accuracy-intraoral-scanner-edentulous-mandibles]] — earlier pilot study (25 patients, 2 implants); only 5/21 scans analyzable
- [[implants/full-arch/azevedo-2024-effect-splinting-scan-bodies-trueness]] — splinting scan bodies improves trueness (5 IOS); contrasts with intraoral splinting degradation here