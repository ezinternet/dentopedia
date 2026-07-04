---
title: "Biomechanical comparison of various implant inclinations and abutment types in a bendable implant system"
authors: Bilgi-Ozyetim E, Dinçer G, Sulaiman A, Dayan SÇ, Kurtulmus-Yilmaz S, Geçkili O
year: 2025
doi: 10.1186/s12903-025-06610-1
pmid: "40684102"
pmcid: "PMC12276677"
category: [implants]
source_collection: pubmed-text
full_text: true
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12276677/
text_path: /Users/oracleneo/llm-wiki/papers/bilgi-ozyetim-2025-biomechanical-comparison-implant-inclinations.txt
text_filename: bilgi-ozyetim-2025-biomechanical-comparison-implant-inclinations.txt
---

## Why Ingested

무치악 하악 All-on-4에서 후방 임플란트 경사 각도(17°/30°/45°)에 따른 응력 분포 FEA. 보철 연결 방식(스크류 vs 시멘트)과 경사 조합 비교 — [[implants/implants-clinical-decision-ladder]] 의 경사 식립 biomechanics 근거 보완.

## Three-line Summary

Finite element analysis (3D CT-based edentulous mandible, All-on-4 with 1-piece bendable implants, 6 models: 17°/30°/45° × screw/cement retention, 150 N vertical + 150 N oblique loading) comparing bone and implant stress across posterior implant angulation and framework retention types.

Increasing posterior implant angulation raised bone and implant stress; cement-retained frameworks showed >3.5× lower framework stress than screw-retained; maximum posterior implant VM stress was 108.6 MPa at 45° with vertical load — all values remained below titanium yield strength (550 MPa).

FEA only; single prosthetic material (CoCr); static loading; fixed 14 mm cantilever; findings support clinical safety of angulation up to 45° in bendable implant All-on-4, with cement retention offering biomechanical advantage.

## 세줄요약

유한요소분석(3D CT 기반 무치악 하악, All-on-4 1체형 굴곡형 임플란트, 6모델: 17°/30°/45° × 나사/시멘트 유지, 150 N 수직+150 N 사선 하중) — 후방 임플란트 경사 각도 및 프레임워크 유지 방식에 따른 골·임플란트 응력 비교.

경사 각도 증가 시 골·임플란트 응력 증가; 시멘트 유지(Cement-retained) 프레임워크가 나사 유지(Screw-retained)보다 3.5배 이상 응력 낮음; 45° 수직 하중 시 최대 후방 임플란트 폰 미세스(Von Mises) 응력 108.6 MPa — 모두 티타늄 항복강도(550 MPa) 이하.

FEA만으로 단일 보철 재료(CoCr); 정적 하중; 고정 14 mm 캔틸레버; 굴곡형 임플란트 All-on-4에서 최대 45° 경사의 임상적 안전성과 시멘트 유지의 생역학적 이점을 지지.

## 1. Document Information

## 1. Document Information
- **Journal**: BMC Oral Health 2025;25(1):1213
- **Study type**: Finite element analysis (in silico)
- **Model**: 3D edentulous mandible (CT data, Visible Human Project)
- **Protocol**: All-on-4 with 2 anterior vertical + 2 posterior tilted implants (Mode Provo one-piece bendable)
- **Models**: 6 (3 inclinations × 2 retention types)
- **Loading**: 150N vertical + 150N oblique (75° linguo-buccal)

## 2. Key Contributions
- First FEA comparing stress in BENDABLE single-piece implants across 17°/30°/45° inclinations
- Shows cement vs screw retention stress difference in angulated one-piece system
- Demonstrates that all stress values remain below titanium yield strength (550 MPa) even at 45°

## 3. Methodology and Architecture
- CT-based mandible reconstruction (DICOM → 3D Slicer → ANSYS)
- 2mm cortical bone shell + trabecular core
- Tetrahedral mesh: ~836,000–904,000 nodes, ~3.4–3.7 million elements
- Convergence validated (<3% relative error)
- Materials: cortical bone E=13,700 MPa, titanium E=110,000 MPa, CoCr framework E=218,000 MPa
- 14mm distal cantilever standardized across all models

## 4. Key Results and Benchmarks

| Model | Inclination | Retention | Posterior Pmin (oblique, MPa) | Posterior VM stress (vertical, MPa) | Framework VM (oblique, MPa) |
|---|---|---|---|---|---|
| 1 | 17° | Screw | — | — | 75.297 |
| 2 | 17° | Cement | −32.598 | 72.794 | ~20 |
| 5 | 45° | Screw | −75.093 | 108.568 | ~72 |
| 6 | 45° | Cement | −79.256 | — | ~19 |

Key findings:
- Angulation ↑ → bone stress ↑ (cortical Pmax/Pmin, implant VM)
- Posterior implants > anterior implants in stress
- Screw-retained framework: 3.5× higher stress than cement-retained
- All VM values < 550 MPa (titanium yield) → no fracture risk
- Highest posterior implant stress: 108.6 MPa (Model 5, 45°, vertical)

## 5. Limitations and Future Work
- FEA cannot fully replicate complex masticatory force patterns
- Single prosthetic material (CoCr) only
- Static loading only; dynamic/fatigue not modeled
- Cantilever length fixed at 14mm (may not reflect all clinical scenarios)

## 6. Related Work
- [[implants/implants-clinical-decision-ladder]]
- Lin & Eckert 2018: clinical SR confirming no survival difference tilted vs axial
- Del Fabbro 2022 SR+MA: marginal bone lower in axial vs tilted at long-term

## 7. Glossary
- **Bendable implant (굴곡형 임플란트)**: single-piece implant where abutment is physically bent to correct angulation
- **All-on-4**: 4-implant full-arch concept (2 axial anterior + 2 tilted posterior)
- **Pmax/Pmin**: maximum/minimum principal stress in bone
- **Von Mises stress**: composite stress measure for ductile materials (implant, framework)
- **Yield strength (항복강도)**: titanium = 550 MPa; stress above this causes permanent deformation
