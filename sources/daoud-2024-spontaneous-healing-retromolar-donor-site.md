---
title: "Computer-Assisted Evaluation Confirms Spontaneous Healing of Donor Site One Year following Bone Block Harvesting from Mandibular Retromolar Region—A Cohort Study"
authors: Shadi Daoud, Adeeb Zoabi, Adi Kasem, Amir Totry, Daniel Oren, Idan Redenski, Samer Srouji, Fares Kablan
year: 2024
doi: 10.3390/diagnostics14050504
journal: "Diagnostics, 14, 504"
stem: daoud-2024-spontaneous-healing-retromolar-donor-site
---

## Why Ingested

Quantifies the rate and quality of spontaneous bone healing at the mandibular retromolar donor site using computer-assisted 3D CBCT analysis — directly complements [[bone-regeneration/stricker-2021-resorption-retromolar-bone-grafts]], which measured graft resorption at the recipient site, by focusing on what happens to the donor.

## Three-line Summary

This prospective cohort study of 20 patients used computer-assisted 3D 콘빔 전산화 단층촬영 (Cone Beam Computed Tomography, CBCT) analysis (segmentation, superimposition, Boolean subtraction) to quantify spontaneous bone healing at the mandibular retromolar donor site 6 and 12 months after bone block harvesting.

The residual bone defect showed 64.5 ± 4.24% volumetric healing at 6 months and 89.2 ± 2.6% healing at 12 months (p<0.05). Bone density decreased to 102.5 ± 27.8 HU (하운스필드 단위, Hounsfield Unit) at 6 months but recovered to 453.9 ± 91.4 HU at 12 months, approaching the original harvest density of 690.3 ± 81 HU.

Spontaneous healing of the retromolar donor site is nearly complete (89.2%) at 12 months, supporting feasibility of re-harvesting from the same site and eliminating the need for donor site grafting.

## 세줄요약

본 전향적 코호트 연구는 20명을 대상으로 컴퓨터 보조 3D 콘빔 전산화 단층촬영 (Cone Beam Computed Tomography, CBCT) 분석(분할·중첩·불리언 차집합)을 사용하여 하악 후구치 부위 (retromolar region) 공여부의 6개월 및 12개월 자발적 골 치유를 정량화했다.

잔존 골 결손 부피는 6개월 64.5 ± 4.24%, 12개월 89.2 ± 2.6% 치유를 보였다(p<0.05). 골 밀도 (하운스필드 단위, Hounsfield Unit, HU)는 6개월에 102.5 ± 27.8 HU로 감소 후 12개월에 453.9 ± 91.4 HU로 회복되어 원래 채취 골 밀도 (690.3 ± 81 HU)에 근접했다.

하악 후구치 공여부의 자발적 치유가 12개월에 89.2%로 거의 완전함을 보여주며, 동일 부위 재채취 가능성 및 공여부 추가 이식 불필요성을 지지하나, 소표본(n=20)과 조직학 부재가 한계다.

## 1. Document Information

- **Journal**: Diagnostics 2024;14(5):504
- **DOI**: 10.3390/diagnostics14050504
- **Institution**: Department of Oral and Maxillofacial Surgery, Galilee College of Dental Sciences, Galilee Medical Center
- **Evidence level**: Prospective cohort study
- **Sample size**: n=20 patients (8 male, 12 female; mean age 48.3 ± 11.1 years)
- **Follow-up**: 12 months (CBCT at intraoperative, 6 months, 12 months)

## 2. Key Contributions

- First prospective cohort study to use fully computer-assisted 3D CBCT volumetric analysis (Mimics Innovation Suite) for quantifying spontaneous healing of the mandibular retromolar donor site.
- Demonstrates that no additional bone grafting at the donor site is required — spontaneous healing reaches 89.2% volumetric fill at 12 months.
- Confirms bone density recovery pattern: initially drops to woven/immature bone HU levels at 6 months, then recovers substantially by 12 months, approaching cortical donor quality.
- Provides specific harvested bone volumes (mean 606.5 ± 77.7 mm³) which can guide clinical planning for ridge augmentation needs.
- Supports possibility of re-harvesting from the same site after adequate healing time.

## 3. Methodology and Architecture

**Study design**: Prospective cohort. Patients undergoing alveolar ridge augmentation with retromolar bone block graft.

**Surgical technique**: Bone block harvested from external oblique ridge (MicroSaw technique). Donor site closed in layers without additional grafting — spontaneous healing only.

**Imaging**: CBCT acquired at three time points:
1. Intraoperative (baseline defect)
2. 6 months postoperative
3. 12 months postoperative

**3D Analysis pipeline (Mimics Innovation Suite, Materialise)**:
1. Segmentation — thresholding to isolate bone objects in each CBCT
2. Superimposition — 3D alignment of time-point scans
3. Boolean subtraction — subtracting 12-month or 6-month volume from intraoperative volume to measure residual defect

**Bone density measurement**: Mean HU averaged across the 3D segmented volume at each time point.

**Statistics**: Descriptive (mean ± SD); two-tailed paired sample t-test (p<0.05 significance threshold).

## 4. Key Results and Benchmarks

**Harvested bone volume**: mean 606.5 ± 77.7 mm³ (range 485.7–740 mm³)

| Time Point | Volumetric Healing | Bone Density (HU) |
|---|---|---|
| Intraoperative (harvest) | — | 690.3 ± 81 HU |
| 6 months | 64.5 ± 4.24% | 102.5 ± 27.8 HU |
| 12 months | 89.2 ± 2.6% | 453.9 ± 91.4 HU |

- 6 → 12 month improvement: p<0.05 for both volumetric healing and bone density.
- No significant difference in healing based on pre-operative bone block size, sex, age, or side of jaw.

## 5. Limitations and Future Work

- Small sample size (n=20); limits generalizability.
- Only 3 CBCT time points due to radiation safety considerations; detailed healing trajectory not captured.
- No histologic assessment (ethical constraints); HU correlates with mineral density but does not confirm histologic maturity.
- 12-month endpoint may be insufficient for assessing long-term outcomes (e.g., cortical remodeling, re-harvest safety).
- No control group with additional donor site grafting for direct comparison.

## 6. Related Work

- [[bone-regeneration/stricker-2021-resorption-retromolar-bone-grafts]] — Complementary study: measures recipient-site graft resorption (43.7% at 12 months) using the same 3D CBCT method; both papers form a full block-graft cycle picture.

## 7. Glossary

- **CBCT (콘빔 전산화 단층촬영, Cone Beam Computed Tomography)**: 3D dental imaging modality for implant planning and volumetric analysis.
- **HU (하운스필드 단위, Hounsfield Unit)**: Standardized radiodensity measure in CT; cortical bone ~400–1000 HU, woven/immature bone much lower.
- **Segmentation (분할)**: Partitioning a 3D image volume into labeled objects for analysis.
- **Superimposition (중첩)**: Aligning and overlaying 3D images from different time points to enable comparison.
- **Boolean Subtraction (불리언 차집합)**: Subtracting one 3D object from another to measure volume difference (residual defect).
- **Retromolar region (후구치 부위)**: Area distal to the last mandibular molar; a common intraoral donor site for bone blocks (external oblique ridge).
- **MicroSaw technique**: Piezoelectric/oscillating saw technique for controlled bone block harvesting.
