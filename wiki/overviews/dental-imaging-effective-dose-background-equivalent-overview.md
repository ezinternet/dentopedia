---
title: "Overview: Dental Radiographic Effective Doses as Natural-Background Equivalents"
type: synthesis
category: overviews
date: 2026-06-25
confidence: synthesis
source_papers:
  - wiki/radiology/lee-2021-dental-imaging-doses-web-dose-calculator.md
  - wiki/radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction.md
  - wiki/radiology/lee-2019-monte-carlo-paediatric-panoramic-dose-reduction.md
  - wiki/radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison.md
  - wiki/radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation.md
  - wiki/radiology/yeh-2018-estimated-radiation-risk-cancer-dental.md
  - wiki/radiology/fontenele-2025-cbct-dentistry-clinical-recommendations-indication.md
  - wiki/radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical.md
  - wiki/radiology/baena-2022-cbct-diagnostic-performance-root-resorption.md
  - wiki/radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison.md
  - wiki/radiology/oenning-2019-halve-dose-paediatric-cone-beam-ct.md
  - wiki/radiology/schindler-2025-panoramic-thyroid-eye-lens-dose.md
  - wiki/radiology/khafaji-2023-scattered-dose-eye-dentistry-cbct.md
  - wiki/radiology/makdissi-2016-effects-device-position-operators-radiation.md
tags: [radiation-dose, effective-dose, background-radiation, cbct, panoramic, patient-safety, alara]
relations:
  - type: extends
    target: dental-imaging-radiation-dose-optimization-overview
---

> [!summary] 한국어 핵심요약
> - **핵심 메시지**: 치과 방사선 검사의 유효선량 (Effective Dose, µSv)을 "자연방사선 (Natural Background Radiation) 며칠분"으로 환산하면 일반 구내·파노라마 촬영은 **수 시간~2일**, 대형 시야 콘빔CT (Cone-Beam CT, CBCT)도 최대 **약 46일** 수준이다 — 즉 진단 이득 대비 매우 낮은 위험이라는 게 보유 근거의 결론.
> - **배경 기준값**: 우리가 보유한 논문 중 자연방사선 연간 선량을 명시한 것은 lee-2021 하나뿐 — **연 3110 µSv** (≈ 하루 8.52 µSv). 이 값을 분모로 모든 환산을 했고, 출처는 전부 lee-2021로 귀속.
> - **구내 치근단 (Periapical, PA)**: 평균 1.32 µSv (lee-2021) → 배경 **약 0.15일 (≈3.7시간)**.
> - **파노라마 (Panoramic)**: 17.6~17.93 µSv (lee-2021, benchimol-2018) → 배경 **약 2.1일**. 소아 파노라마는 3.5~3.9 µSv (lee-2019) → **약 0.4일 (≈10시간)**.
> - **CBCT**: 기기·시야 (Field of View, FOV)에 따라 폭이 큼 — 문헌 평균 121 µSv (lee-2021, ≈14일), i-CAT 16×13cm 약 31 µSv (yeh-2018, ≈3.6일), 전체 범위 3~500 µSv (fontenele-2025) / 34~1073 µSv (baena-2022).
> - **검증 포인트**: 소아 대형FOV CBCT 최대 392.2 µSv를 환산하면 배경 약 46일 = 연간의 12.6%인데, lee-2021이 본문에서 직접 "연간 자연방사선의 13%"라 적어 **산술이 논문 진술과 일치** (외삽 아님).
> - **발암 위험 (REID)**: 교정 CBCT의 평생귀속발암위험 (Risk of Exposure-Induced Death)은 10세 여아 22.6×10⁻⁵로 30세 (10.4×10⁻⁵)의 약 2배, 여>남 (yeh-2018) — 소아·여성에서 정당화 (Justification)가 더 중요.
> - **선량 저감 (ALARA) 레버**: CBCT 저선량 프로토콜로 성인 약 6배 감소 (charuakkra-2023), 소아 약 45% 감소 (oenning-2019); 작은 FOV 6회는 큰 FOV 1회의 1.2배라 **시야를 쪼개도 선량은 안 줄어든다** (ozaki-2021).
> - **차폐 논점**: 파노라마 갑상선 0.30~1.46 µSv·수정체 0.88~4.24 µSv (schindler-2025)로 절대선량이 낮아 갑상선 칼라·차폐 중단 권고의 근거가 됨 (별도 차폐 오버뷰·benavides-2023 연계).
> - **⚠️ 솔직한 공백**: **비행기·우주방사선 등가 비교**는 보유 논문에 수치가 전혀 없어 만들지 않았다 (Rule #1: 웹검색 금지). 비행 1회=며칠 같은 환산이 필요하면 해당 수치가 담긴 논문을 주시면 추가하겠음. 구내 비트윙 (Bitewing)·전악 (FMX)·측방두부 (Lateral Ceph)·휴대용 PA의 **환자** 유효선량도 보유 논문에 없음.

## One-line Summary

Synthesis of 14 held dental-dosimetry papers expressing radiographic effective doses (µSv) as natural-background-radiation equivalents: intraoral PA ≈ a few hours, panoramic ≈ 2 days, and CBCT from ≈3.6 days (small i-CAT) up to ≈46 days (max child large-FOV) of background — with the per-modality flight/cosmic comparison flagged as absent from our corpus.

## 한줄요약

보유 치과 선량 논문 14편을 합성해 유효선량을 자연방사선 등가일수로 환산 — 구내 PA 수 시간, 파노라마 약 2일, CBCT 약 3.6~46일; 단 비행/우주방사선 비교값은 우리 논문에 없어 공백으로 명시.

## Thesis

**Clinical question:** How large is the radiation from common dental radiographs when expressed in an intuitive unit — "days of natural background radiation" — and what does that imply for justification and dose optimization?

**Best-evidence answer from papers we hold:** Dental radiographic effective doses are small relative to natural background. Using the only background reference value present in our corpus — **3110 µSv/year ≈ 8.52 µSv/day** (lee-2021) — an intraoral periapical image (1.32 µSv) equals roughly **0.15 day (≈3.7 h)** of background, a panoramic (17.6–17.9 µSv) about **2.1 days**, and CBCT spans **~3.6 days (small i-CAT FOV, 31 µSv) to ~46 days (max child large-FOV, 392.2 µSv)**. The 46-day figure reproduces lee-2021's own statement that this dose ≈ 13% of annual background, confirming the conversion is faithful to the source rather than extrapolated. Risk rises in children and females (yeh-2018), so justification matters most there; dose can be cut substantially by FOV restriction and low-dose protocols (charuakkra-2023, oenning-2019), but **not** by tiling several small FOVs (ozaki-2021).

**Method note (Rule #1 compliance):** Every effective-dose value below is quoted from a paper we hold. The "days-of-background" column is plain arithmetic — `dose ÷ (3110 µSv/yr ÷ 365)` — using lee-2021's background value as the single, transparent denominator; it is **not** a figure imported from outside the corpus. No flight, cosmic, or per-capita comparator exists in our papers, so none is computed (see Gaps).

## Evidence Map

| Paper | Design | Modality / contribution | Key dose figure (verbatim) |
|---|---|---|---|
| lee-2021 | dose-calculator / literature synthesis | Intraoral, panoramic, CBCT means + **only background-equivalence anchor** | intraoral 1.32 (0.60–2.56) µSv; panoramic 17.93 (3.47–75.00) µSv; CBCT 121.09 (17.10–392.20) µSv; max child large-FOV 392.2 µSv ≈ 13% of annual background (3110 µSv) |
| benchimol-2018 | phantom MOSFET | Panoramic + collimation | full-size panoramic 17.6 µSv (ICRP 2007) |
| lee-2019 (paediatric pano) | Monte Carlo vs TLD | Paediatric panoramic | MC 3.474 µSv vs TLD 3.850 µSv |
| ozaki-2021 | Monte Carlo | CBCT FOV strategy | six small FOVs ≈ 1.2× one large FOV |
| yeh-2018 | Monte Carlo + BEIR-VII | CBCT effective dose + cancer risk | i-CAT 16×13 cm ≈ 31 µSv; REID 10yo female 22.6×10⁻⁵ ≈ 2× a 30yo |
| fontenele-2025 | narrative review | CBCT device spread | effective dose ~3–500 µSv |
| jacobs-2018 | consensus/recommendations | CBCT vs panoramic | ≈ 2–200 panoramic radiographs |
| baena-2022 | diagnostic SR | CBCT (root-resorption studies) | 34–1073 µSv |
| charuakkra-2023 | phantom dose/image | Low-dose CBCT (adult) | ~6× dose reduction, acceptable quality |
| oenning-2019 | optimization | Low-dose CBCT (paediatric) | ~45% effective-dose reduction (ALADAIP) |
| schindler-2025 | phantom | Panoramic organ dose | thyroid 0.30–1.46 µSv; eye lens 0.88–4.24 µSv |
| khafaji-2023 | SR (5 phantom) | CBCT eye-lens scatter | 0.103–8.3 mSv (FOV-dependent) |
| makdissi-2016 | phantom/TLD | Handheld PA (operator dose only) | peak 0.0310 mGy palm vs 0.0110 mGy background |

## Effective Dose → Background-Equivalent Table

Denominator (single source): natural background **3110 µSv/yr ≈ 8.52 µSv/day** (lee-2021). Equivalent days/hours are arithmetic on held values only.

| Modality | Effective dose (held value, stem) | ≈ background equivalent (derived) |
|---|---|---|
| Intraoral periapical (PA) | 1.32 µSv (lee-2021) | ~0.15 day (~3.7 h) |
| Panoramic (adult) | 17.6–17.93 µSv (benchimol-2018, lee-2021) | ~2.1 days |
| Panoramic (paediatric) | 3.47–3.85 µSv (lee-2019) | ~0.4 day (~10 h) |
| CBCT — small i-CAT FOV (16×13 cm) | ~31 µSv (yeh-2018) | ~3.6 days |
| CBCT — literature mean (all FOV) | 121.09 µSv (lee-2021) | ~14 days |
| CBCT — device range | 3–500 µSv (fontenele-2025); 34–1073 µSv (baena-2022) | ~0.35–59 / ~4–126 days |
| CBCT — max child large-FOV | 392.2 µSv (lee-2021) | ~46 days (lee-2021: ≈13% of annual) |

**No held effective-dose value for:** bitewing, full-mouth series (FMX), lateral cephalogram, handheld/portable PA **patient** dose. These rows are intentionally omitted rather than estimated.

## Clinical Decision Points

1. **Justification first, dose second.** Even the largest routine exposure (large-FOV CBCT, ~46 days of background) is a small fraction of annual natural dose, but stochastic risk is real and ~2× higher in children (yeh-2018) — so the decision to image at all, especially in young patients, dominates any dose-tuning.
2. **Match FOV to the task — don't tile.** Restricting FOV is the main CBCT dose lever, but six small FOVs ≈ 1.2× one large FOV (ozaki-2021): if multiple regions are needed, a single appropriately sized volume is dose-preferable to several small scans.
3. **Use low-dose protocols routinely.** ~6× reduction (adult, charuakkra-2023) and ~45% reduction (paediatric ALADAIP, oenning-2019) are achievable with maintained diagnostic quality via kVp/mAs/voxel adjustment.
4. **Shielding policy follows absolute dose.** Panoramic thyroid (0.30–1.46 µSv) and eye-lens (0.88–4.24 µSv) doses are very low (schindler-2025), the rationale behind contemporary discontinuation of routine thyroid collars/aprons — see the patient-shielding evidence ([[radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography]]).

## Gaps & Future Research

- **Flight / cosmic / per-capita equivalents — absent from our corpus.** No held paper expresses dental dose as flight-equivalents or a per-capita-dose fraction, and the only natural-background reference value anywhere in our files is lee-2021's 3110 µSv/yr. Per Rule #1 (no web search), these comparators were **not** fabricated. To add a "one panoramic = N hours of flight" row, ingest a paper that reports the flight/background comparator value.
- **Missing modality doses.** Bitewing, FMX, lateral cephalogram, and portable/handheld PA *patient* effective dose have no number in our papers — ingest dosimetry papers covering these to complete the table.
- **Effective dose ≠ individual risk.** ICRP warns against using effective dose for individual risk estimation (yeh-2018); the background-equivalent framing is a communication aid, not a personal risk calculator.

## Related Papers

- [[overviews/dental-imaging-radiation-dose-optimization-overview]] — **companion overview**: this page reframes the same dose hierarchy as background-equivalents for *patient communication*; that page covers the operator *dose-reduction levers* (FOV/collimation/kVp/voxel). Use together.
- [[radiology/lee-2021-dental-imaging-doses-web-dose-calculator]] — anchor: per-modality means + the sole background-equivalence statement
- [[radiology/yeh-2018-estimated-radiation-risk-cancer-dental]] — CBCT effective dose + BEIR-VII cancer risk (child ~2×)
- [[radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation]] — FOV strategy: tiling small FOVs is not dose-sparing
- [[radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction]] — panoramic dose + collimation
- [[radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison]] — ~6× adult low-dose reduction
- [[radiology/oenning-2019-halve-dose-paediatric-cone-beam-ct]] — ~45% paediatric reduction (ALADAIP)
- [[radiology/schindler-2025-panoramic-thyroid-eye-lens-dose]] — organ doses underpinning shielding discontinuation
- [[radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography]] — shielding-discontinuation consensus
- [[radiology/makdissi-2016-effects-device-position-operators-radiation]] — handheld PA operator (not patient) dose
