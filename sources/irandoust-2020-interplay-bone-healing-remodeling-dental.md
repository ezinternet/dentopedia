---
title: "The interplay between bone healing and remodeling around dental implants"
authors: Irandoust S, Müftü S
year: 2020
doi: 10.1038/s41598-020-60735-7
category: implants
pdf_path: /Users/oracleneo/llm-wiki/papers/irandoust-2020-interplay-bone-healing-remodeling-dental.pdf
pdf_filename: irandoust-2020-interplay-bone-healing-remodeling-dental.pdf
source_collection: external
---

## Why Ingested
This computational modeling study is the first to consecutively simulate both bone healing (days 1–30) and bone remodeling (up to 15,000 days) around immediately loaded dental implants using a mechano-regulatory cellular differentiation model. It fills a gap where prior healing studies omitted long-term adaptation and remodeling studies lacked realistic initial conditions [[implants/loading-protocol]].

## Three-line Summary
Computational mechano-regulatory model simulating bone healing (30 days) and remodeling (15,000 days) around immediately loaded implants with controlled initial micromotion (5, 10, 20 μm).
At 5 and 10 μm micromotion, ~95–100% immature/trabecular bone formed by day 30 but 35% resorbed by day 15,000 due to stress shielding; at 20 μm, only 45% bone formed initially with 16% fibrous tissue, and steady-state cortical bone not fully established at 15,000 days.
Implant micromotion during early healing critically determines long-term bone volume and quality — an optimal patient-specific micromotion range exists for desired functional outcomes.

## 세줄요약
메카노-조절 세포분화 모델로 즉시부하 임플란트 주위 골치유(30일)와 골리모델링(15,000일)을 연속 시뮬레이션 — 초기 마이크로모션 5, 10, 20 μm 조건 비교.
5·10 μm에서 30일째 미성숙/해면골 ~95–100% 형성되나 15,000일째 스트레스 실딩으로 35% 흡수; 20 μm에선 초기 골형성 45%·섬유조직 16%, 피질골 정상상태 미도달.
초기 힐링 단계 마이크로모션이 장기 골용적·질 결정 — 환자 맞춤 최적 마이크로모션 범위 설계 가능성 제시.

## 1. Document Information
- **Journal**: Scientific Reports 2020;10:4335
- **DOI**: 10.1038/s41598-020-60735-7
- **Institution**: Department of Mechanical and Industrial Engineering, Northeastern University, Boston, MA, USA

## 2. Key Contributions
- First study to consecutively model both bone healing and bone remodeling phases using a unified mechano-regulatory cellular differentiation framework
- Demonstrated that tissue between implant threads differentiates into bone during healing but resorbs during remodeling due to stress shielding, regardless of micromotion magnitude
- Quantified long-term (15,000 days) tissue volume (TV) and tissue-to-implant contact (TIC) outcomes: 65%, 63%, 33% bone TV for 5, 10, 20 μm micromotion respectively
- Showed that large micromotion (20 μm) leads to fibrous/cartilaginous tissue formation during healing but remaining bone achieves higher density via remodeling

## 3. Methodology and Architecture
- **Design**: Computational in silico study — mechano-regulatory cellular differentiation model with poroelastic tissue properties
- **Model**: Axisymmetric finite element model of implant in osteotomy gap (no initial bone-implant contact)
- **Healing phase**: 30 days, poroelastic tissues, material properties updated per loading cycle, implant micromotion as independent variable (5, 10, 20 μm)
- **Remodeling phase**: 15,000 days, bone apparent density adaptation via homeostatic remodeling stimulus, mastication force (100 N) as independent variable
- **Outcomes**: Tissue volume (TV), tissue-to-implant contact (TIC), elastic modulus distribution, solid/fluid stimuli

## 4. Key Results and Benchmarks
| Outcome | 5 μm | 10 μm | 20 μm |
|---|---|---|---|
| **Day 30 (healing end) — Immature/Trabecular Bone TV** | ~100% | 95% | 45% |
| **Day 30 — Fibrous Tissue TV** | 0% | ~0% | 5% |
| **Day 30 — Cartilaginous Tissue TV** | 0% | 0% | 45.8% |
| **Day 15,000 (remodeling end) — Total Bone TV (trabecular + cortical)** | 65% | 63% | 33% |
| **Day 15,000 — Cortical Bone TV** | 7% | ~7% | 15% |
| **Day 15,000 — Fibrous Tissue TV** | 35% | ~35% | 16% |
| **Day 15,000 — TIC (Cortical Bone)** | 10% | ~10% | 8% |

- Solid stimulus (shear strain) lowest between threads → faster healing but later resorption (stress shielding)
- High fluid velocity in coronal region due to low cortical bone permeability → soft tissue development
- 20 μm: steady-state cortical bone not fully established at 15,000 days

## 5. Limitations and Future Work
- Axisymmetric 2D model — cannot capture 3D thread geometry effects or off-axis loading
- Single implant diameter/geometry; patient-specific anatomy not incorporated
- Mastication force simplified to 100 N static load; dynamic/cyclic loading patterns not modeled
- Cellular/molecular signaling pathways (RANKL/OPG, Wnt) not explicitly represented — phenomenological stimulus only
- No validation against in vivo histomorphometry or clinical outcome data

## 6. Related Work
- Trisi et al. 2016 (osseodensification) — bone condensing effects on primary stability and healing
- Rowe 2023 (bone remodeling physiology) — canonical biology of remodeling stimulus

## 7. Glossary
- **Mechano-regulatory cellular differentiation model (메카노-조절 세포분화 모델)**: Computational framework where mechanical stimuli (strain, fluid flow) direct mesenchymal stem cell differentiation into fibrous, cartilaginous, or bone tissue
- **Poroelastic (다공탄성)**: Material model treating tissue as a fluid-saturated porous solid where fluid pressure and solid deformation are coupled
- **Stress shielding (스트레스 실딩)**: Bone resorption due to insufficient mechanical stimulus when implant carries disproportionate load
- **Tissue volume — TV (조직 용적)**: Ratio of specific tissue type volume to total healing region volume
- **Tissue-to-implant contact — TIC (임플란트-조직 접촉율)**: Percentage of implant surface in contact with a specific tissue type
- **Remodeling stimulus (리모델링 자극)**: Homeostatic mechanical signal (strain energy density or equivalent) that drives bone apparent density adaptation