---
title: "Assessment of the Impact of Bone Quality and Abutment Configuration on the Fatigue Performance of Dental Implant Systems Using Finite Element Analysis (FEA)"
authors: Erdoğdu M, Demirel MG, Mohammadi R, Güntekin N
year: 2024
doi: 10.3390/jpm14101040
pmid: "39452546"
pmcid: "PMC11508474"
category: [implants]
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/erdogdu-2024-abutment-angle-bone-quality-fatigue-fea.txt
text_filename: erdogdu-2024-abutment-angle-bone-quality-fatigue-fea.txt
---

## Why Ingested

인접 자연치가 경사진 경우 임플란트를 대합치 치조골에 수직으로 식립하면 지대주 각도 보정이 필요한데, 각도 지대주가 응력·피로 강도에 미치는 영향이 궁금했음. 본 FEA는 멀티유닛 vs 시멘트형 지대주의 각도별 피로 성능을 직접 비교해 [[implants/chi-2024-customized-angled-abutment-tooth-inclination-fea]]의 전임상 근거를 보강한다.

## One-line Summary

FEA (maxillary 3-unit bridge, 150 N oblique, 6 abutment configs × 2 bone types): abutment angle ↑ → von Mises stress ↑ and fatigue performance ↓; multiunit abutments outperform cemented at all angles; resorbed bone amplifies both findings.

## 한줄요약

FEA (상악 3단 브릿지, 150 N 사선 하중, 6 지대주 구성 × 2 골 유형): 지대주 각도 증가 → 응력 증가·피로 강도 감소; 멀티유닛 지대주가 시멘트형보다 모든 각도에서 우수; 흡수 골에서 두 경향 모두 심화.

## 1. Document Information

- **Type**: FEA (finite element analysis) study
- **Journal**: Journal of Personalized Medicine
- **Year**: 2024
- **DOI**: [10.3390/jpm14101040](https://doi.org/10.3390/jpm14101040)
- **Sample**: maxillary 3-unit implant-supported bridge (2 implants: 1st premolar + 1st molar)
- **Groups**: Multiunit 0°/15°/30° (Mu0/Mu15/Mu30); Cemented 0°/15°/25° (C0/C15/C25); Healthy bone (Hb) vs Resorbed bone (Rb)
- **Load**: 150 N oblique, palatal→buccal, 30° angle; 1000 load cycles (Abaqus)

## 2. Key Contributions

- Quantified abutment angle effect on both stress distribution AND fatigue performance — distinguishes from stress-only FEA studies
- Demonstrated multiunit abutments superiority over cemented at equivalent angles
- Showed resorbed bone amplifies every adverse finding (higher vMS, lower fatigue)
- Provided clinically relevant groups (0°, 15°, 25–30°) matching real abutment options

## 3. Methodology and Architecture

- 3D maxillary bone model (SolidWorks): cortical + trabecular + mucosa; 2 implants Ø3.7 mm × 10 mm (Bil Implant)
- Healthy bone (Hb) vs Resorbed bone (Rb) models
- Monolithic zirconia restoration; 40 µm cement layer (cemented groups)
- Screw preload: 781 N (25 N·cm tightening torque)
- Friction coefficient: 0.3 at interfaces
- Fatigue analysis: critical-plane criterion + Coffin-Manson (plastic) + Basquin (elastic) → cycles to crack initiation
- 1000 direct cyclic steps

## 4. Key Results and Benchmarks

| Metric | Best | Worst |
|---|---|---|
| Implant vMS (Hb premolar) | Mu0 (lowest) | C25 (highest) |
| Cortical bone vMS | Mu0 | C25 |
| Implant fatigue performance | Mu0 (highest) | C25 (lowest) |
| Bone effect | Hb > Rb | Rb → ↑ vMS, ↓ fatigue |

- vMS increases proportionally with angle in all groups
- Multiunit < Cemented vMS at every angle
- Fatigue decreases inversely with angle increase
- Molar region → higher stress + lower fatigue than premolar (thinner cortical bone)

## 5. Limitations and Future Work

- Only monolithic zirconia tested (no material variation)
- Only 1000 cycles (under-represents lifetime masticatory cycles)
- Static oblique load — no dynamic simulation or thermal analysis
- No in vivo validation; FEA assumptions (isotropic, linear elastic, full osseointegration) simplify reality
- Single implant company / single diameter — limits generalizability

## 6. Related Work

- Chi 2024: customized abutment angles based on tooth inclination (FEA + in vitro, anterior maxilla)
- Murat 2025: load direction × implant angulation interaction in All-on-4 (FEA + RSM)

## 7. Glossary

- **vMS**: von Mises stress — combined stress measure for ductile materials
- **Mu/C**: Multiunit / Cemented abutment type prefix
- **Hb/Rb**: Healthy bone / Resorbed bone
- **IAJ**: Implant-Abutment Junction — stress concentration point
- **Coffin-Manson law**: relates plastic strain amplitude to cycles to failure
