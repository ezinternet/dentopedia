---
title: "Influence of Immediate Versus Delayed Loading on Peri-Implant Bone Healing: A Comparative FEA Study of Titanium Threaded and Scaffold Dental Implants"
authors: Giuseppe Casalino, Mario Ceddia, Nicola Contuzzi, Luciano Lamberti, Bartolomeo Trentadue
year: 2026
date: 2026-04-16
doi: 10.3390/ma19081607
source: casalino-2026-influence-immediate-versus-delayed-loading.md
category: implants
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/casalino-2026-influence-immediate-versus-delayed-loading.pdf
pdf_filename: casalino-2026-influence-immediate-versus-delayed-loading.pdf
source_collection: external
tags: [FEA, mechanobiology, immediate-loading, delayed-loading, porous-implant, scaffold, threaded-implant, peri-implant-callus, stress-shielding, Prendergast-Huiskes, ABAQUS, stress-distribution]
relations:
  - type: extends
    target: ceddia-2025-crestal-position-splinted-implant-fea
---

## Three-line Summary

Comparative 3D FEA (ABAQUS/Standard) of a bone block with a 0.2 mm peri-implant callus: threaded Ti-6Al-4V implant (Model A) vs porous scaffold implant (Model B, 64.26% porosity, apparent E 14.05 GPa), each under immediate (IL, frictional interface μ=0.3) and delayed (DL, tied interface) loading with 100 N vertical load.

Under IL, Model B reduced cortical bone stress from ~88 to 32.5 MPa (~63% reduction) and raised callus mechanical stimulation from ~2.5 to 20.5–31.6 MPa; Prendergast–Huiskes mechanobiological analysis predicted higher immature+mature bone (84.8% vs 46.7%) and far less cartilage (14.5% vs 50.4%) than Model A.

The porous implant thus offers a mechanically more favorable early-healing environment, particularly under immediate loading, and reduces stress shielding; all implant stresses stayed below yield strength, but results are purely in silico and require validation.

## 세줄요약

골 블록에 0.2 mm 임플란트주위 가골(peri-implant callus)을 모델링해 나사형 Ti-6Al-4V 임플란트(모델 A)와 다공성 스캐폴드 임플란트(모델 B, 다공률 64.26%, 등가 탄성계수 14.05 GPa)를 즉시부하(Immediate Loading, IL)·지연부하(Delayed Loading, DL) 조건에서 비교한 3D 유한요소해석(Finite Element Analysis, FEA) 연구.

IL에서 모델 B는 피질골 응력을 약 88→32.5 MPa로(약 63% 감소) 낮추고 가골 자극을 약 2.5→20.5~31.6 MPa로 크게 높였으며, Prendergast–Huiskes 기전생물학 분석상 미성숙·성숙골 분율이 46.7%→84.8%로 높아지고 연골은 50.4%→14.5%로 줄었음.

다공성 임플란트가 특히 즉시부하 조건에서 초기 골유착(osseointegration) 치유와 응력 차폐(stress shielding) 감소에 유리한 기계적 환경을 제공하나, 모든 조건에서 임플란트 응력은 항복강도 미만 — 시뮬레이션이므로 실험·임상 검증이 필요함.

## Summary

This static 3D finite element study modeled a bone block with a 0.2 mm peri-implant healing callus in ABAQUS/Standard and compared a conventional threaded Ti-6Al-4V implant (Model A) with a porous scaffold implant (Model B, 64.26% porosity, apparent elastic modulus 14.05 GPa) under immediate and delayed loading. Immediate loading was simulated by a frictional bone–implant interface (μ=0.3, compressive load transfer only) and delayed loading by a tied interface, with a 100 N vertical load. Under immediate loading, the porous implant cut crestal cortical stress by ~63% (32.5 vs 88 MPa) while markedly increasing callus mechanical stimulation (20.5–31.6 vs ~2.5 MPa). A Prendergast–Huiskes mechanobiological analysis of the callus predicted that the porous design produces a substantially higher fraction of immature and mature bone (84.8% vs 46.7%) and far less cartilage (14.5% vs 50.4%), indicating a more favorable environment for osteogenic differentiation and callus maturation. Implant stresses remained below yield strength in all conditions; the porous implant appears to be a promising strategy for early peri-implant healing and reduced stress shielding, pending experimental and clinical validation.

## Key Contributions

- First comparative FEA pairing a porous scaffold dental implant with a conventional threaded implant under both immediate and delayed loading in a single healing-callus mechanobiological model
- Combined poroelastic bone/callus modeling with the Prendergast–Huiskes stimulus to translate raw stress outputs into predicted tissue differentiation phenotypes
- Quantified stress-shielding reduction: ~63% lower crestal cortical stress under immediate loading plus redirection of callus stimulation into the osteogenic window
- Explicit scaffold geometry (0.6 mm cylindrical pores, cubic unit cell, 64.26% porosity) with apparent stiffness ~14.05 GPa — far closer to bone than bulk Ti-6Al-4V (110 GPa)

## Methodology

3D FEA (in-vitro computational) in ABAQUS/Standard 2017; bone block + implants designed in Autodesk Inventor 2024. Model A: threaded implant (10 mm endosseous × 4.1 mm diameter + 7 mm coronal). Model B: porous implant from a cubic unit cell with 0.6 mm-diameter cylindrical pores (64.26% porosity); apparent modulus and yield via Gibson–Ashby relationships. Cortical, trabecular bone and callus were isotropic linear poroelastic (E 20,000 / 6,000 / 0.2 MPa; permeability 9.81e−11 / 3.629e−6 / 9.81e−8; void ratio 0.04 / 2.33 / 4.0). Delayed loading used a tied interface with the 0.2 mm region assigned cancellous-bone properties; immediate loading used frictional contact (μ=0.3). A 100 N vertical load, fixed inferior bone surface, and zero pore pressure on upper surfaces were applied. Mesh: quadratic tetrahedra — bone 1 mm, callus 0.2 mm, implant 0.3 mm; 20,194 nodes/79,188 elements (Model A) and 129,288 nodes/165,081 elements (Model B), with mesh convergence verified. Mechanobiology used the Prendergast–Huiskes stimulus S = γ/a + v/b (a=0.0375, b=3) on the immediate-loading callus.

## Results

**Equivalent stress in peri-implant bone:**

| Condition | Model A — threaded | Model B — porous |
|---|---|---|
| IL cortical (MPa) | ~88 | 32.5 (~63% lower) |
| IL callus (MPa) | ~2.5 (near-constant) | 20.5 upper / 31.6 lower (avg 26.05) |
| DL cortical (MPa) | 34.7 (apex 37.6) | ~16 |
| DL callus (MPa) | 9–26.5 | 2.26–7.56 |

Implant equivalent stress: IL 38 MPa (A) / 48.56 MPa (B); DL 75 MPa (A) / 85 MPa (B) — all below yield (890 MPa solid; 190.16 MPa porous).

**Prendergast–Huiskes tissue fractions in callus (immediate loading only):**

| Phenotype | Model A (%) | Model B (%) |
|---|---|---|
| Fibrous tissue (S > 3) | 2.85 | 0.54 |
| Cartilage (1 < S ≤ 3) | 50.42 | 14.46 |
| Immature bone (0.266 < S ≤ 1) | 19.18 | 35.65 |
| Mature bone (0.010 < S ≤ 0.266) | 27.55 | 49.16 |
| Resorption (S ≤ 0.010) | 0.00 | 0.19 |

Under delayed loading, both models stayed within remodeling-compatible stress ranges (cortical 20–60 MPa, trabecular 6–18 MPa). The authors caution that greater callus stimulation is biphasic — benefit comes from shifting stimulus into the osteogenic window, not from raw magnitude.

## Related Papers

- [[implants/ceddia-2025-crestal-position-splinted-implant-fea]] — Same research group (Ceddia, Trentadue); extends their FEA bone–implant stress framework from prosthetic crestal alignment to loading-protocol × implant-design mechanobiology
- [[implants/chang-2024-optimization-implant-design-bone-quality-fea]] — FEA optimizing threaded-implant geometry per bone quality; complements this threaded-vs-porous design comparison
- [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]] — Threaded-implant FEA localizing peak stress to crestal cortical bone; the threaded model here reproduces the same crestal-concentration pattern
- [[implants/loading-protocol/esposito-2013-loading-times-dental-implants-cochrane]] — Clinical Cochrane evidence on loading timing; this FEA supplies the biomechanical rationale underlying immediately-loaded-implant risk
- [[implants/loading-protocol/rismanchian-2025-immediate-nonimmediate-loading-umbrella-review]] — Clinical umbrella review of immediate vs non-immediate loading outcomes; in silico complement on the mechanical mechanism
- [[bone-regeneration/sun-2025-3d-printed-scaffold-bone-defect-repair]] — Porous scaffold design principles (pore architecture, mechanical/biological balance) for bone repair; this paper applies them to a dental implant
- [[implants/loading-protocol/ko-2021-immediate-loading-protocols-increase-risk]] — RCT showing guided immediate loading increases failure risk; mechanobiological context for why implant design may modulate that risk