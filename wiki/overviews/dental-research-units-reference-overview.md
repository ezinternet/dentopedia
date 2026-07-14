---
title: "치과 논문에 자주 쓰이는 단위 레퍼런스 (Common Units in Dental Research) — 빈도순 + 임계값 매트릭스"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-07-14
type: overview
category: [overviews]
tags: [units, mm, MPa, GPa, Ncm, ISQ, sievert, radiation-dose, ppm, HbA1c, surface-roughness, bond-strength, insertion-torque, marginal-bone-loss, reference]
source_papers:
confidence: synthesis
source: synthesis
source_wiki:
  - wiki/overviews/isq-loading-threshold.md
  - wiki/overviews/implant-primary-stability-arp-macrogeometry-low-density-overview.md
  - wiki/overviews/implant-bite-force-stability-short-implant-mbl-overview.md
  - wiki/overviews/dental-imaging-radiation-dose-optimization-overview.md
  - wiki/dental-materials/zirconia/ban-2023-dental-zirconia-types-development-review.md
  - wiki/implants/surface/hasegawa-2020-meso-micro-nano-rough-titanium-surface.md
  - wiki/drug/systemic-disease/chen-2022-interpretation-hba1c-analytical-methodology-hematology.md
  - wiki/suture-wound-closure/marsidi-2020-measuring-forces-suture-techniques-wound-closure.md
  - wiki/local-anesthesia/becker-2012-local-anesthetics-pharmacological-considerations.md
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **핵심 명제**: 치과 논문의 단위는 5개 계열로 수렴한다 — ① 거리·치수, ② 힘·토크, ③ 재료강도, ④ 방사선량, ⑤ 무차원 지수. 단위 자체보다 **각 단위에 붙는 임계값(threshold)을 아는 것**이 임상 판독의 핵심.
> - **빈도 순위 (위키 본문 스캔)**: 밀리미터 (millimeter, mm) ≫ 밀리그램 (milligram, mg) > 뉴턴 (Newton, N) > 마이크로미터 (micrometer, µm) ≈ 메가파스칼 (megapascal, MPa) > 뉴턴센티미터 (Newton-centimeter, Ncm) > 섭씨 (°C) > 시버트 (Sievert, µSv/mSv) > ppm ≈ 기가파스칼 (gigapascal, GPa).
> - **거리 — mm**: 압도적 1위(11,000회+). 변연골 소실 (Marginal Bone Loss, MBL) 첫 해 <1.5mm·이후 <0.2mm/년, 각화점막 폭 (Keratinized Mucosa width, KM) ≥2mm, 탐침 깊이 (Probing Depth, PD) 건강 ≤3mm가 대표 임계값.
> - **미세거리 — µm**: mm의 1/1000. 표면조도 (Surface roughness, Ra) ~1–2µm, 변연간극 (Marginal gap) <120µm 등 미세영역 전용.
> - **토크 vs 힘**: 식립 토크 (Insertion Torque, IT)는 회전력이라 뉴턴센티미터 (Ncm), 교합력·접착 하중은 직선력이라 뉴턴 (N). 즉시하중 기준 IT ≥35Ncm, 과압박 위험 >50Ncm — 둘을 혼동하면 안 됨.
> - **재료강도 — MPa**: 메가파스칼 (MPa) = N/mm². 굴곡강도 (Flexural strength) 지르코니아 ~1000–1200MPa vs 리튬디실리케이트 (lithium disilicate) ~400MPa, 접착강도 (Bond strength) 통상 20–40MPa. 탄성계수 (Elastic modulus)만 기가파스칼 (GPa) = MPa×1000.
> - **방사선량 — Sievert**: 유효선량(피폭)은 마이크로·밀리시버트 (µSv/mSv), 1mSv=1000µSv. 치근단 ~5µSv < 파노라마 ~10–20µSv < 콘빔CT (Cone-Beam CT, CBCT) ~20–200µSv. 흡수선량은 그레이 (Gray, Gy)로 별개.
> - **무차원 지수**: 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 1–100 스케일, 부하 임계 통상 ≥70. 백분율(생존율·골-임플란트 접촉률 BIC), pH(법랑질 탈회 임계 5.5), 당화혈색소 (HbA1c) 조절기준 <7%, 불소 농도 ppm(치약 1000–1450ppm).
> - **술기·기기 단위(정의·스펙)**: 봉합사 USP 게이지는 **0이 많을수록 얇음**(4-0>6-0), 구강 판막봉합 4-0~5-0·미세수술 7-0/8-0. 마취제 농도 %는 w/v라 **2% = 20mg/mL**(리도카인 2%·아티카인 4%·부피바카인 0.5%). 초음파 스케일러 주파수는 자왜형 ~18–45kHz·압전형 ~25–50kHz.
> - **환산 규칙 3개만 외우면 됨**: mm↔µm(×1000), MPa↔GPa(×1000), mSv↔µSv(×1000) — 모두 1000배 관계. MPa=N/mm²만 별도.
> - **임상 takeaway**: 논문을 읽을 때 단위를 보면 반사적으로 "이 단위의 정상/성공 임계값이 뭐였지?"를 떠올릴 것. 단위는 저장고, 임계값은 열쇠.

## Three-line Summary

A cross-wiki reference synthesizing the measurement units that recur across the dental literature we hold, ranked by raw occurrence frequency (body-text scan of the wiki).

Units cluster into five families — distance (mm dominates at 11,000+ hits; µm for microscale), force/torque (N vs Ncm), material strength (MPa = N/mm², GPa for modulus), radiation dose (Sv ladder, Gy separate), and dimensionless indices (ISQ, %, pH, HbA1c, ppm) — each paired with its canonical clinical threshold.

Clinical value lies not in the unit itself but in recalling the threshold attached to it (MBL <1.5mm, IT ≥35Ncm, ISQ ≥70, CBCT dose in µSv, HbA1c <7%); three ×1000 conversions (mm↔µm, MPa↔GPa, mSv↔µSv) cover most unit arithmetic.

## 세줄요약

위키가 보유한 치과 논문 전체를 본문 스캔해 실제 등장 빈도순으로 자주 쓰이는 단위를 정리한 크로스-위키 레퍼런스.

단위는 5계열로 수렴 — 거리(mm 압도적, 미세영역 µm), 힘·토크(직선력 N vs 회전력 Ncm), 재료강도(MPa=N/mm², 탄성계수만 GPa), 방사선량(시버트 사다리, 흡수선량 Gy는 별개), 무차원 지수(ISQ·%·pH·HbA1c·ppm) — 각 단위에 대표 임계값을 짝지음.

임상 가치는 단위가 아니라 거기 붙은 임계값(MBL <1.5mm, 토크 ≥35Ncm, ISQ ≥70, CBCT µSv, HbA1c <7%)을 떠올리는 데 있고, ×1000 환산 3개(mm↔µm, MPa↔GPa, mSv↔µSv)면 단위 계산 대부분이 해결된다.

## Summary

This page is a **reading aid**, not a study synthesis. It answers a recurring practical question — *"which units show up most, and what threshold should I attach to each?"* — by ranking units on their raw occurrence across the wiki body text and pairing each with the canonical clinical cut-off that appears in the source pages. Unit frequency is used only as evidence of how often a clinician meets each unit; every threshold is traceable to a linked wiki page.

Occurrence ranking (approximate, whole-wiki body scan):

| Rank | Unit | Hits | Family |
|---|---|---|---|
| 1 | mm | ~11,160 | distance |
| 2 | mg | ~820 | mass (drug dose) |
| 3 | N | ~740 | force |
| 4 | µm / μm | ~980 | microscale distance |
| 5 | MPa | ~700 | material strength |
| 6 | Ncm / N·cm | ~670 | torque |
| 7 | °C | ~450 | temperature |
| 8 | µSv / mSv | ~260 | radiation dose |
| 9 | mL | ~175 | volume |
| 10 | ppm | ~88 | concentration |
| 11 | GPa | ~87 | elastic modulus |

## 1. Distance — millimeter (mm) and micrometer (µm)

**mm** is by far the most common unit; most clinical outcomes are reported in it. Canonical thresholds:

- Marginal Bone Loss (MBL): success criterion of first-year <1.5 mm, then <0.2 mm/year (Albrektsson criteria) — see [[implant-bite-force-stability-short-implant-mbl-overview]].
- Keratinized Mucosa (KM) width: stability threshold ≥2 mm.
- Probing Depth (PD): health ≤3 mm.
- Working Length (WL) in endodontics: 0.5–1 mm short of the apical foramen.
- Residual Bone Height (RBH): decision variable for sinus-lift approach selection.

**µm (= mm/1000)** is reserved for the microscale: implant surface roughness (Ra ~1–2 µm; see [[hasegawa-2020-meso-micro-nano-rough-titanium-surface]]), prosthetic marginal gap (<120 µm), and material grain size.

## 2. Force and torque — Newton (N) vs Newton-centimeter (Ncm)

These are physically distinct and must not be conflated:

- **N (Newton)** — linear force. Occlusal/bite force, and the load applied to bond-strength or fracture-load specimens.
- **Ncm (Newton-centimeter)** — rotational force = **Insertion Torque (IT)**, the primary-stability proxy recorded at implant placement. Immediate-loading threshold ≥35 Ncm; over-compression risk >50 Ncm. See [[implant-primary-stability-arp-macrogeometry-low-density-overview]] and the osseodensification literature ([[al-ahmari-2022-osseodensification-conventional-low-density-jaw]]).

Mnemonic: Ncm is the "turning" force, N is the "pushing" force.

## 3. Material strength — megapascal (MPa) and gigapascal (GPa)

- **MPa = N/mm²** — pressure/strength. Read it as "how many Newtons per square millimeter." Flexural strength: zirconia ~1000–1200 MPa vs lithium disilicate ~400 MPa ([[ban-2023-dental-zirconia-types-development-review]], [[cesar-2024-dental-zirconia-15years-material-processing]]). Adhesive Bond strength: typically 20–40 MPa ([[magne-2005-ids-improves-bond-strength-indirect]]).
- **GPa = MPa × 1000** — reserved for Elastic modulus (stiffness): dentin ~18 GPa, titanium ~110 GPa. A high strength (MPa) with low modulus (GPa) behaves very differently from the reverse.

## 4. Radiation dose — sievert (Sv) family and gray (Gy)

- **µSv / mSv (microsievert / millisievert; 1 mSv = 1000 µSv)** — effective dose (patient exposure, weighted for tissue radiosensitivity). Dose ladder: periapical ~5 µSv < panoramic ~10–20 µSv < CBCT ~20–200 µSv (field-of-view dependent). See [[dental-imaging-radiation-dose-optimization-overview]] and [[dental-imaging-effective-dose-background-equivalent-overview]].
- **kVp / mA** — tube voltage / current, i.e., the exposure settings (CBCT typically ~90 kVp, 5–10 mA); collimation reduces dose ([[benchimol-2018-collimation-panoramic-effective-dose-reduction]]).
- **Gy (gray)** — absorbed dose, a separate quantity used for radiotherapy dosing, not diagnostic exposure.

## 5. Dimensionless indices (no unit, but load-bearing)

- **ISQ (Implant Stability Quotient)** — 1–100 scale from Resonance Frequency Analysis (RFA). Loading threshold commonly ≥70 (robust) / caution <60 — see [[isq-loading-threshold]] and [[implants-isq-stability-ladder]].
- **% (percent)** — survival rate, Bone-to-Implant Contact (BIC), and HbA1c.
- **pH** — enamel demineralization critical pH 5.5; also irrigant and liner chemistry.
- **HbA1c (glycated hemoglobin, %)** — glycemic control; dental threshold of concern typically <7% for elective implant surgery ([[chen-2022-interpretation-hba1c-analytical-methodology-hematology]], [[weykamp-2013-hba1c-review-analytical-clinical-aspects]]).
- **ppm (parts per million)** — fluoride concentration: toothpaste 1000–1450 ppm, high-concentration 5000 ppm ([[kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma]]).

## 6. Device / procedure units — suture gauge, anesthetic concentration, scaler frequency

These are less frequent in outcome tables but constant at the chairside; each is a **spec/definition**, not a research-derived cut-off.

- **USP suture gauge** — the United States Pharmacopeia caliber scale, written with zeros: **more zeros = thinner thread** (4-0 = "four-oh" is thicker than 6-0). Wiki suture pages span 3-0 to 8-0. Typical use: intraoral flap closure 4-0 to 5-0, delicate/esthetic 6-0, microsurgery 7-0/8-0 ([[marsidi-2020-measuring-forces-suture-techniques-wound-closure]], [[look-2022-novel-superficial-suture-pattern-tensile-strength]]). Thinner thread = lower tensile strength but less tissue trauma — the gauge is a strength-vs-trauma trade-off.
- **Local anesthetic concentration (% w/v)** — percent here is grams per 100 mL, so **2% = 20 mg/mL**. Canonical dental concentrations: lidocaine 2%, mepivacaine 2% (with vasoconstrictor) or 3% (plain), articaine 4%, prilocaine 4%, bupivacaine 0.5% ([[becker-2012-local-anesthetics-pharmacological-considerations]], [[alkandari-2024-articaine-versus-mepivacaine-ianb-irreversible-pulpitis]]). Higher % ≠ automatically stronger block — it interacts with max dose (mg/kg) and vasoconstrictor.
- **Ultrasonic scaler frequency (kHz)** — operating oscillation of the tip: magnetostrictive ~18–45 kHz, piezoelectric ~25–50 kHz (device-class spec; wiki holds an ultrasonic-tip instance at 28 ± 3 kHz — [[parra-2026-pushout-bond-strength-fiberglass-posts]] — and periodontal ultrasonic/GBT debridement context in [[cyris-2024-guided-biofilm-therapy-versus-conventional]]). The wiki has no paper dedicated to scaler frequency itself; the kHz ranges are the standard hardware spec, included here as a reference anchor.

## 7. The only conversions worth memorizing

Three unit pairs are all ×1000 relationships; a fourth is a definition:

| Convert | Factor |
|---|---|
| mm ↔ µm | ×1000 |
| MPa ↔ GPa | ×1000 |
| mSv ↔ µSv | ×1000 |
| MPa | = N/mm² (definition) |

Clinical takeaway: when a unit appears in a paper, let it trigger the reflex *"what was the normal/success threshold for this unit?"* The unit is the storage; the threshold is the key.

## Related Papers

- [[isq-loading-threshold]] — ISQ loading-decision threshold matrix (the ISQ index in depth)
- [[implants-isq-stability-ladder]] — ISQ interpretation ladder
- [[implant-primary-stability-arp-macrogeometry-low-density-overview]] — insertion torque (Ncm) and primary stability
- [[implant-bite-force-stability-short-implant-mbl-overview]] — MBL (mm) and bite force (N)
- [[dental-imaging-radiation-dose-optimization-overview]] — effective dose (µSv/mSv) optimization
- [[dental-imaging-effective-dose-background-equivalent-overview]] — dose expressed as background-equivalent
- [[ban-2023-dental-zirconia-types-development-review]] — flexural strength / modulus (MPa/GPa)
- [[cesar-2024-dental-zirconia-15years-material-processing]] — zirconia strength context
- [[magne-2005-ids-improves-bond-strength-indirect]] — adhesive bond strength (MPa)
- [[hasegawa-2020-meso-micro-nano-rough-titanium-surface]] — surface roughness (µm/Ra)
- [[al-ahmari-2022-osseodensification-conventional-low-density-jaw]] — osseodensification torque/ISQ
- [[chen-2022-interpretation-hba1c-analytical-methodology-hematology]] — HbA1c (%) interpretation
- [[weykamp-2013-hba1c-review-analytical-clinical-aspects]] — HbA1c analytical aspects
- [[kumar-2026-fluoride-varnish-caries-prevention-cost-effectiveness-sr-ma]] — fluoride (ppm) prevention
- [[benchimol-2018-collimation-panoramic-effective-dose-reduction]] — collimation / dose (kVp·mA·µSv)
- [[marsidi-2020-measuring-forces-suture-techniques-wound-closure]] — suture gauge (USP) and closure forces
- [[look-2022-novel-superficial-suture-pattern-tensile-strength]] — suture tensile strength by pattern/gauge
- [[becker-2012-local-anesthetics-pharmacological-considerations]] — anesthetic concentration (% w/v) and pharmacology
- [[alkandari-2024-articaine-versus-mepivacaine-ianb-irreversible-pulpitis]] — 4% articaine vs 2% mepivacaine
- [[parra-2026-pushout-bond-strength-fiberglass-posts]] — ultrasonic activation frequency (kHz) instance
- [[cyris-2024-guided-biofilm-therapy-versus-conventional]] — ultrasonic/GBT debridement context
