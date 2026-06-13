---
title: "Dynamic finite element modelling of the macaque mandible during a complete mastication gape cycle"
authors: Panagiotopoulou O, Robinson D, Iriarte-Diaz J, Ackland D, Taylor AB, Ross CF
year: 2023
doi: 10.1098/rstb.2022.0549
category: [occlusion]
pdf_path: /Users/oracleneo/llm-wiki/papers/panagiotopoulou-2023-dynamic-fea-macaque-mandible-mastication.pdf
pdf_filename: panagiotopoulou-2023-dynamic-fea-macaque-mandible-mastication.pdf
source_collection: external
---

## Why Ingested

기존 occlusion FEA 페이지들([[occlusion/ambili-2024-parafunctional-loading-stress-tooth-implant-fea]], [[occlusion/yesilyurt-2021-occlusion-concepts-hybrid-abutment-zirconia-fea]])은 모두 **정적(static) 단일 시점** FEA로 교합 하중을 모델링한다. 본 논문은 영장류 하악에서 **동적(dynamic) 완전 저작주기 FEA**가 정적 FEA가 놓치는 시점·음식별 변형/변형률 패턴을 포착함을 보여, 치과 FEA의 정적 단일-시점 가정의 한계를 직접 비판하는 방법론적 근거로 인제스트. 또한 음식 경도에 따른 저작근 활성 비대칭 → 하악 응력 분포 변화는 [[tmj/wang-2024-tmj-ovd-elevation-occlusal-loss-rats]] 등 저작 생체역학 동물 모델 페이지를 보강한다.

## One-line Summary

First dynamic 3D FEM of a primate (rhesus macaque) mandible over a complete unilateral chewing gape cycle, EMG/PCSA-driven muscle forces and validated against in vivo bone strain; peak strains/moments occur ~40% of the gape cycle and vary by food (nuts > grapes > dried fruit), with dynamic models capturing strain in mandibular regions static single-time-point FEMs miss.

## 한줄요약

영장류(붉은털원숭이) 하악의 완전한 편측 저작주기를 모델링한 최초의 동적 3D 유한요소모델(FEM) 연구. 근전도(EMG)·생리적 단면적(PCSA) 기반 근력을 적용하고 생체 골 변형률로 검증했으며, 최대 변형률·모멘트는 저작주기의 약 40% 지점에서 발생하고 음식(견과류 > 포도 > 건과일)에 따라 달라졌다. 동적 모델은 정적 단일-시점 FEM이 놓치는 하악 부위의 응력까지 포착함을 입증.

## 1. Document Information

- **Title**: Dynamic finite element modelling of the macaque mandible during a complete mastication gape cycle
- **Authors**: Olga Panagiotopoulou, Dale Robinson, Jose Iriarte-Diaz, David Ackland, Andrea B. Taylor, Callum F. Ross
- **Journal**: Philosophical Transactions of the Royal Society B 2023;378:20220549 (theme issue "Food processing and nutritional assimilation in animals")
- **DOI**: 10.1098/rstb.2022.0549
- **Received**: 8 June 2023; Accepted: 14 September 2023
- **Subject area**: Biomechanics
- **Study type**: Animal experimental / computational (validated subject-specific dynamic FEA of a single adult rhesus macaque, *Macaca mulatta*)
- **Funding/affiliations**: Monash University, University of Melbourne, University of the South, Touro University California, University of Chicago

## 2. Key Contributions

1. **First dynamic 3D FEM of a primate mandible during feeding.** Prior macaque mandible FEA from the same group was static — a single time point (46% of the gape cycle, where the in vivo strain gauge recorded peak strain). This study builds the first dynamic FEM spanning a complete gape cycle (100 increments, 0.0033 s each) driven by in vivo muscle-force time histories.
2. **Demonstrates static FEMs underrepresent jaw mechanics.** Loading, deformation and strain regimes vary across the chewing cycle in subtly food-specific ways invisible to static single-time-point FEMs. Static models may therefore be a poor tool for inferring diet–morphology (form–function) relationships.
3. **Two model variants for transparency.** A "screws model" (validated static FEM geometry retaining the titanium kinematic-marker screws and remodelled bone/calluses in the anterior mandible) and a previously unpublished "no-screws model" (screws and calluses virtually removed in Mimics v.25 / 3-Matic v.17). Screws/calluses minimally affected lingual-symphysis mechanics — confirming the in vivo kinematic instrumentation did not corrupt jaw function.
4. **Peak strain timing identified.** Peak principal strains and moments occur at ~40% of the gape cycle across all foods (no-screws: grapes 35%, dried fruit 37%, nuts 38%), close to but not identical to the 46% static time point and NOT at maximum EMG intensity.
5. **Translational claim.** Because macaque, chimpanzee and human feeding mechanics are similar, dynamic FEMs are argued to be necessary for human mandible clinical questions (fracture fixation, TMJ replacement, distraction osteogenesis) — to date no dynamic FEM of a human mandible during a complete chewing sequence exists.

## 3. Methodology and Architecture

- **Subject/geometry**: Adult rhesus macaque skull CT (Philips Brilliance, 0.8 mm slices, 0.2 mm pixel) segmented in Mimics v.17 into cortical bone, trabecular bone, teeth, PDL, and bone screws. Meshed in 3-Matic into linear tetrahedral elements (hybrid for PDL), max nominal element size 0.7 mm.
- **Material properties**: Cortical bone = orthotropic, heterogeneous, subject-specific (ultrasonic velocity + theoretical modelling). Trabecular bone, teeth, screws, PDL = linear elastic isotropic (trabecular E=10 GPa, ν=0.3; teeth E=24.5 GPa, ν=0.3; screws E=105 GPa, ν=0.36; PDL E=6.80×10⁻⁴ GPa, ν=0.49). No-screws model: screws/calluses removed, PDL space reassigned to cortical bone.
- **Loads/constraints**: Bite force simulated by constraining occlusal-surface nodes on left P3, P4, M1 (working = left side). Working-side condyle fully fixed at one node; balancing-side condyle fixed in SI and AP only. All intersecting surfaces tied (frictionless).
- **Muscle forces**: Estimated from in vivo EMG (working & balancing anterior/posterior temporalis, superficial & deep masseter, medial pterygoid) × subject-specific PCSA × specific tension (30 N/cm²). PCSA from muscle mass, pennation angle, fibre length (sarcomere-normalized). Applied as time-varying amplitude functions; vectors from origin (cranium) to dynamically moving insertion centroids (mandible).
- **Foods**: three categories of differing toughness/stiffness — soft (grapes), dried fruit (prune, date, gummy bear, dried apricot/pineapple/cranberry), nuts (almond, cashew, Brazil nut, walnut, pecan).
- **Solver**: Abaqus CAE SIMULIA v.2021, implicit solver, 100 increments × 0.0033 s.
- **Post-processing**: Axial, principal and shear strains visualized over the gape cycle. Moments computed about Y (AP/twisting), X (SI/transverse bending), Z (ML/sagittal bending) axes through centroids of hemimandible and symphysis cross-sections.

## 4. Key Results and Benchmarks

- **Moment/strain peak timing**: Moments peak ~35–40% of the gape cycle (no-screws: nuts 40%, grapes 35%, dried fruit 39%); peak principal strains ~35–40% (no-screws: grapes 35%, dried fruit 37%, nuts 38%). Generally highest during nut chewing, lowest during dried fruit.
- **Spatial loading pattern (consistent across foods)**: Sagittal bending moments highest at balancing-side anterior ramus / posterior corpus, then working-side anterior corpus below the bite point (P4, M1). Twisting (AP) moments highest on working side just behind the bite point (between M1–M2) and at the symphyseal first-incisor section. Transverse bending (SI) moments peak in the symphyseal region.
- **Three common deformation regimes**: (1) ramus twisting (coronoid inversion + angle eversion), (2) sagittal bending, (3) lateral transverse bending ("wishboning").
- **Food-specific dynamics**: Nut/dried-fruit chews show slow balancing-side sagittal bending rise to ~20% then rapid increase (food differences emerge late in power stroke). Grape chewing shows rapid early rise (10–15%) then slower later — early lateral transverse bending driven by early recruitment of balancing-side superficial masseter and medial pterygoid. Early-cycle (10–30%) strains: grapes > nuts > dried fruit; late-cycle (>30%) strains: nuts > grapes > dried fruit.
- **Strain hotspots (ε1, tensile)**: bilateral coronoid process / endocoronoid ridge (twisting); anterior ramus border, plana triangulares, external oblique lines, extramolar sulci, lateral prominences (sagittal bending); inferior transverse torus, medial prominence, torus triangularis, endocondylar ridge (transverse bending).
- **Dynamic vs static gain**: Dynamic FEM captured peak strains over a LARGER area of the balancing-side corpus/ramus and across the coronoid process, endocoronoid ridge, external oblique lines, extramolar sulci, lateral prominences and plana triangulares of the working side — regions the static FEM did not flag.
- **Screws vs no-screws**: minimal difference at the lingual symphysis, validating that the kinematic instrumentation did not compromise jaw mechanics.

## 5. Limitations and Future Work

- **(i)** The original static-FEM geometry had titanium kinematic screws + activated bone remodelling/calluses in the anterior mandible of unknown mechanical impact. The no-screws model removes them but still shows artefacts (isolated high-strain elements at labial symphysis from CT radiodensity distortion → low Young's modulus assignment).
- **(ii)** During screw/callus removal the PDL had to be reassigned to cortical bone (PDL not separately modelled in no-screws variant).
- **Single specimen, single species** (one adult rhesus macaque) — generalization to other primates/humans is by analogy, not direct measurement.
- **Human mandible dynamic FEM still unpublished** — authors call for dynamic models for clinical applications (fracture fixation, TMJ replacement, distraction osteogenesis) and for comparative diet–morphology studies that should avoid single-time-point analysis.

## 6. Related Work

- Builds directly on the authors' prior static, validated macaque mandible FEMs (Panagiotopoulou et al., refs [5,6]) and in vivo EMG / 3D jaw-kinematic experiments.
- Cites FEM + rigid-body TMJ studies in humans (refs [32,33]) and comparative diet–mandible-morphology literature (symphysis/corpus cross-section, condyle shape).
- Relevant to dental occlusion/TMJ biomechanics: muscle-activation asymmetry, working- vs balancing-side loading, and the limits of static occlusal-load FEA assumptions common in dental FEA papers.

## 7. Glossary

- **FEM/FEA** — Finite element model / analysis; discretizes a structure into elements to solve stress/strain under loads.
- **Gape cycle** — One full open-close jaw cycle during chewing; expressed as 0–100%.
- **Working side / balancing side** — Working (chewing) side bears the bolus and bite force; balancing (non-chewing) side opposes it.
- **PCSA** — Physiological cross-sectional area; proxy for a muscle's maximum force capacity.
- **EMG** — Electromyography; records muscle electrical activation, used to scale muscle force over time.
- **Microstrain (με)** — Strain × 10⁻⁶; ε1 = maximum (tensile) principal strain, ε3 = minimum (compressive) principal strain.
- **Wishboning** — Lateral transverse bending of the mandible at the symphysis during the power stroke.
- **Sagittal / transverse / AP twisting moments** — Bending moments about ML (Z), SI (X), and AP (Y) axes respectively.
- **Endocondylar ridge / medial prominence / torus triangularis** — Macaque mandibular features forming the load path from bite point to balancing-side ramus.
- **Static vs dynamic FEM** — Static = single time-point load snapshot; dynamic = time-varying loads across the whole cycle.
