---
title: "Influence of Immediate Versus Delayed Loading on Peri-Implant Bone Healing: A Comparative FEA Study of Titanium Threaded and Scaffold Dental Implants"
authors: Giuseppe Casalino, Mario Ceddia, Nicola Contuzzi, Luciano Lamberti, Bartolomeo Trentadue
year: 2026
doi: 10.3390/ma19081607
category: implants
pdf_path: /Users/oracleneo/llm-wiki/papers/casalino-2026-influence-immediate-versus-delayed-loading.pdf
pdf_filename: casalino-2026-influence-immediate-versus-delayed-loading.pdf
source_collection: external
---

## Why Ingested

The first comparative FEA to pair a porous scaffold-based dental implant against a conventional threaded design under both immediate and delayed loading inside a single peri-implant callus mechanobiological model — it converts a perennial clinical question (immediate-loading biomechanical risk) into a design-dependent, mechanobiological prediction. Extends the same group's FEA bone–implant stress framework in [[implants/ceddia-2025-crestal-position-splinted-implant-fea]] from prosthetic alignment to loading-protocol × implant-design interaction.

## Three-line Summary

Comparative 3D FEA (ABAQUS/Standard) of a bone block with a 0.2 mm peri-implant callus: threaded Ti-6Al-4V implant (Model A) vs porous scaffold implant (Model B, 64.26% porosity, apparent E 14.05 GPa), each under immediate (IL, frictional interface μ=0.3) and delayed (DL, tied interface) loading with 100 N vertical load.

Under IL, Model B reduced cortical bone stress from ~88 to 32.5 MPa (~63% reduction) and raised callus mechanical stimulation from ~2.5 to 20.5–31.6 MPa; Prendergast–Huiskes mechanobiological analysis predicted higher immature+mature bone (84.8% vs 46.7%) and far less cartilage (14.5% vs 50.4%) than Model A.

The porous implant thus offers a mechanically more favorable early-healing environment, particularly under immediate loading, and reduces stress shielding; all implant stresses stayed below yield strength, but results are purely in silico and require validation.

## 세줄요약

골 블록에 0.2 mm 임플란트주위 가골(peri-implant callus)을 모델링해 나사형 Ti-6Al-4V 임플란트(모델 A)와 다공성 스캐폴드 임플란트(모델 B, 다공률 64.26%, 등가 탄성계수 14.05 GPa)를 즉시부하(Immediate Loading, IL)·지연부하(Delayed Loading, DL) 조건에서 비교한 3D 유한요소해석(Finite Element Analysis, FEA) 연구.

IL에서 모델 B는 피질골 응력을 약 88→32.5 MPa로(약 63% 감소) 낮추고 가골 자극을 약 2.5→20.5~31.6 MPa로 크게 높였으며, Prendergast–Huiskes 기전생물학 분석상 미성숙·성숙골 분율이 46.7%→84.8%로 높아지고 연골은 50.4%→14.5%로 줄었음.

다공성 임플란트가 특히 즉시부하 조건에서 초기 골유착(osseointegration) 치유와 응력 차폐(stress shielding) 감소에 유리한 기계적 환경을 제공하나, 모든 조건에서 임플란트 응력은 항복강도 미만 — 시뮬레이션이므로 실험·임상 검증이 필요함.

## 1. Document Information

- **Journal**: Materials 2026;19(8):1607
- **DOI**: 10.3390/ma19081607
- **Institution**: Department of Mechanics, Mathematics and Management, Polytechnic University of Bari, 70125 Bari, Italy

## 2. Key Contributions

- First comparative FEA to directly pair a porous scaffold-based dental implant with a conventional threaded implant under both immediate and delayed loading within a single healing-callus mechanobiological model
- Combined poroelastic bone/callus modeling with the Prendergast–Huiskes stimulus to translate raw stress outputs into predicted tissue phenotypes (bone/cartilage/fibrous differentiation fractions)
- Quantified stress-shielding reduction: the porous design cut crestal cortical stress ~63% under immediate loading and redirected callus stimulation toward the osteogenic window
- Explicit lattice geometry (0.6 mm cylindrical pores in a cubic unit cell, 64.26% porosity; apparent E 14.05 GPa, compressive yield 190.16 MPa via Gibson–Ashby) brings implant stiffness far closer to bone than solid Ti-6Al-4V (110 GPa)

## 3. Methodology and Architecture

- **Design**: Static 3D finite element analysis (in-vitro computational), ABAQUS/Standard 2017 (Simulia, Dassault Systèmes)
- **CAD**: Bone block + implant models in Autodesk Inventor 3D CAD (2024); bone block with a 0.2 mm-thick peri-implant bone callus (per Chou & Müftü)
- **Model A**: Threaded implant, 10 mm endosseous length × 4.1 mm diameter + 7 mm coronal portion not in contact with bone (conventional clinical geometry baseline)
- **Model B**: Porous implant, cubic unit cell with cylindrical pore 0.6 mm (600 µm) diameter × 0.9 mm length; 64.26% porosity computed from the explicit architecture; apparent E = Es(1−φ)² = 14.05 GPa, compressive yield σ = σs(1−φ)^1.5 = 190.16 MPa (Es 110 GPa, σs 890 MPa, Gibson–Ashby)
- **Tissues**: Cortical, trabecular bone and callus as isotropic linear poroelastic materials (E 20,000 / 6,000 / 0.2 MPa; permeability 9.81e−11 / 3.629e−6 / 9.81e−8; void ratio 0.04 / 2.33 / 4.0). For DL, the 0.2 mm region was assigned cancellous-bone properties (mineralized, healed state)
- **Interfaces**: DL = tie constraint (complete osseointegration); IL = frictional contact μ=0.3 (compressive-load transfer only, non-osseointegrated early healing)
- **Load**: 100 N vertical at implant top; inferior bone surface fully fixed; pore pressure zeroed on upper cortical/callus surfaces
- **Mesh**: Quadratic tetrahedral pore-pressure elements (C3D10MP) for bone/callus, C3D10 for implant; 1 mm bone, 0.2 mm callus, 0.3 mm implant average size; Model A 20,194 nodes / 79,188 elements; Model B 129,288 nodes / 165,081 elements. Mesh convergence verified
- **Mechanobiology**: Prendergast–Huiskes stimulus S = γ/a + v/b (a = 0.0375, b = 3), computed for the immediate-loading callus only; tissue phenotypes: fibrous S > 3, cartilage 1 < S ≤ 3, immature bone 0.266 < S ≤ 1, mature bone 0.010 < S ≤ 0.266, resorption S ≤ 0.010

## 4. Key Results and Benchmarks

**Equivalent stress in cortical bone and callus:**

| Condition | Model A — threaded | Model B — porous |
|---|---|---|
| IL cortical (MPa) | ~88 | 32.5 (~63% lower) |
| IL callus (MPa) | ~2.5 (near-constant) | 20.5 upper / 31.6 lower (avg 26.05) |
| DL cortical (MPa) | 34.7 (apex 37.6) | ~16 |
| DL callus (MPa) | 9–26.5 | 2.26–7.56 |

**Implant equivalent stress (all below yield):**

| Condition | Model A (yield 890) | Model B (yield 190.16) |
|---|---|---|
| IL (MPa) | 38 | 48.56 |
| DL (MPa) | 75 | 85 |

**Prendergast–Huiskes tissue fractions in callus (IL only):**

| Phenotype | Model A (%) | Model B (%) |
|---|---|---|
| Fibrous tissue (S > 3) | 2.85 | 0.54 |
| Cartilage (1 < S ≤ 3) | 50.42 | 14.46 |
| Immature bone (0.266 < S ≤ 1) | 19.18 | 35.65 |
| Mature bone (0.010 < S ≤ 0.266) | 27.55 | 49.16 |
| Resorption (S ≤ 0.010) | 0.00 | 0.19 |

- IL stress concentrated at crestal cortical bone around the implant neck in both models; the threaded implant left the callus nearly unstimulated
- DL load-transfer was more effective after tissue maturation; both models produced DL stresses within remodeling-compatible ranges (cortical 20–60 MPa, trabecular 6–18 MPa)
- Higher callus stimulation is biphasic, not monotonic — benefit arises from shifting stimulus into the osteogenic window, not from raw stimulation magnitude

## 5. Limitations and Future Work

- Bone modeled as isotropic linear poroelastic, whereas bone is orthotropic/direction-dependent — a simplification of the biological structure
- Delayed loading idealized as a tie (perfect osseointegration); in vivo osseointegration is progressive with graded interfacial bonding
- Static axial 100 N only — no dynamic, multidirectional, cyclic/fatigue loading; fatigue is a critical safety factor for porous Ti-6Al-4V
- Prendergast–Huiskes thresholds are literature-derived and may vary by site/loading; predictions are comparative, not absolute patient-specific thresholds
- Numerical findings require experimental and clinical validation; future work should include oblique and cyclic loading, parafunctional scenarios, and partial-osseointegration interfaces

## 6. Related Work

- Ceddia et al. (2024): comparative FEA + experimental testing of implant-related structures — validates the group's FEA methodology used here
- Chou & Müftü (2013): immediate-loading peri-implant bone healing simulation — source of the 0.2 mm callus model
- Esaki et al. (2012) / Nagasawa et al. (2013): animal studies linking load magnitude to peri-implant osteogenesis/overload degeneration — biological rationale for the mechanical window
- Arabnejad et al. (2016) / Taniguchi et al. (2016): porous titanium bone-ingrowth and pore-size evidence for the scaffold rationale
- Liu et al. (2022): graded porous titanium implant (59.86% porosity) — similar stress-shielding design direction
- Xu et al. (2021): cylindrical pore geometry favored over spherical for stiffness/hydraulic performance — basis for Model B's pore shape

## 7. Glossary

- **Immediate Loading (IL, 즉시부하)**: Functional prosthetic loading within 48–72 h (or first week) of implant placement, simulated here by a frictional bone–implant interface
- **Delayed Loading (DL, 지연부하)**: Implant left unloaded ~3–6 months for osseointegration before loading, simulated by a tied (fully bonded) interface
- **Peri-implant callus (임플란트주위 가골)**: 0.2 mm healing soft-tissue region between implant and bone in early healing, modeled with granulation-tissue properties
- **Porous scaffold implant (다공성 스캐폴드 임플란트)**: Implant whose central region is an explicit porous lattice (cubic unit cell, 0.6 mm cylindrical pores, 64.26% porosity) to lower apparent stiffness toward bone
- **Stress shielding (응력 차폐)**: Overly stiff implant carrying excess load, depriving peri-implant bone of physiological mechanical stimulation
- **Prendergast–Huiskes stimulus (프렌더가스트–하위키스 자극)**: Mechanobiological criterion S combining octahedral shear strain and interstitial fluid velocity to predict early tissue differentiation phenotype
- **Bone-to-Implant Contact (BIC, 골-임플란트 접촉률)**: Fraction of implant surface in direct contact with bone — the clinical outcome mechanobiology aims to predict