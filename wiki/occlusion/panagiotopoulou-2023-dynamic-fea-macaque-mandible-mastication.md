---
title: "Dynamic finite element modelling of the macaque mandible during a complete mastication gape cycle"
authors: Panagiotopoulou O, Robinson D, Iriarte-Diaz J, Ackland D, Taylor AB, Ross CF
year: 2023
date: 2023-09-14
doi: 10.1098/rstb.2022.0549
source: panagiotopoulou-2023-dynamic-fea-macaque-mandible-mastication.md
category: [occlusion]
confidence: animal
pdf_path: /Users/oracleneo/llm-wiki/papers/panagiotopoulou-2023-dynamic-fea-macaque-mandible-mastication.pdf
pdf_filename: panagiotopoulou-2023-dynamic-fea-macaque-mandible-mastication.pdf
source_collection: external
tags: [occlusion, finite-element-analysis, mastication, mandible, biomechanics, chewing, gape-cycle, macaque, dynamic-fea, bone-strain]
relations:
  - type: contradicts
    target: ambili-2024-parafunctional-loading-stress-tooth-implant-fea
  - type: contradicts
    target: yesilyurt-2021-occlusion-concepts-hybrid-abutment-zirconia-fea
---

## Three-line Summary

First dynamic 3D finite element model of a primate (rhesus macaque, n=1) mandible over a complete unilateral chewing gape cycle, with EMG/PCSA-derived time-varying muscle forces validated against in-vivo bone-strain recordings for three foods (grapes, dried fruit, nuts).

Peak strains and moments occurred at ~35–40% of the gape cycle (not at peak EMG) and varied by food hardness (nuts > grapes > dried fruit); the dynamic model captured strain in mandibular regions the group's prior static single-time-point FEM did not identify.

Static single-load FEA — the near-universal assumption in dental FEA studies — underrepresents jaw mechanics; dynamic models are needed for human clinical mandible questions (fracture fixation, TMJ replacement, distraction osteogenesis).

## 세줄요약

붉은털원숭이(n=1) 하악의 완전한 편측 저작주기를 모델링한 최초의 동적 3D 유한요소모델(FEM): 근전도(EMG)·생리적 단면적(PCSA) 기반의 시변 근력을 적용하고 3가지 음식(포도·건과일·견과류)에서 생체 골 변형률로 검증했다.

최대 변형률·모멘트는 저작주기 약 35–40% 지점(최대 EMG 시점이 아님)에서 발생했으며 음식 경도에 따라 달랐다(견과류 > 포도 > 건과일); 동적 모델은 정적 단일-시점 FEM이 놓친 하악 부위 변형률까지 포착했다.

치과 FEA에서 보편적으로 쓰이는 정적 단일 하중 가정은 악안면 역학을 과소 표현하므로, 하악 골절 고정·TMJ 치환·골연장 같은 임상 문제에는 동적 FEM이 필요하다.

## Summary

Dental finite element analysis (FEA) of occlusal loading almost universally applies a **static, single-time-point** load. This study tests whether that assumption is adequate by building the **first dynamic 3D FEM of a primate mandible** across a complete unilateral chewing gape cycle, using one adult rhesus macaque (*Macaca mulatta*). Time-varying muscle forces were derived from in vivo EMG combined with subject-specific physiological cross-sectional areas (PCSA), and the model was validated against in vivo bone-strain recordings during chewing on three foods of differing mechanical properties (soft grapes, dried fruit, hard nuts).

The central finding is that **loading, deformation, and strain regimes vary continuously across the gape cycle in food-specific ways that static FEMs cannot capture.** Peak strains and moments occur at ~35–40% of the gape cycle (not at maximum EMG intensity), and the dynamic model revealed strain in mandibular regions the group's prior static FEM had not flagged. The authors argue static FEMs are therefore a limited tool for inferring diet–morphology relationships, and — given the mechanical similarity of macaque, chimpanzee and human feeding — that **dynamic FEMs are needed for human clinical mandible questions** (fracture fixation, TMJ replacement, distraction osteogenesis), none of which currently exist.

## Key Contributions

1. **First dynamic primate-mandible FEM during feeding**, spanning a complete gape cycle (Abaqus implicit, 100 increments × 0.0033 s) with EMG/PCSA-derived time-varying muscle forces.
2. **Direct demonstration that static single-time-point FEA underrepresents jaw mechanics** — food differences and strain hotspots emerge at times and locations static FEMs miss.
3. **Two model variants** (with and without the titanium kinematic screws + bone calluses) showing the in vivo instrumentation minimally affected lingual-symphysis mechanics.
4. **Peak-timing result**: strains/moments peak ~35–40% of the gape cycle, close to but distinct from the 46% static time point, and not coincident with peak EMG.

## Methodology

- **Subject**: one adult rhesus macaque; CT-segmented (Mimics/3-Matic) cortical bone, trabecular bone, teeth, PDL, screws; linear-tetrahedral mesh (max 0.7 mm).
- **Material properties**: cortical bone orthotropic/heterogeneous (subject-specific via ultrasonic velocity); trabecular/teeth/screws/PDL linear-elastic isotropic. No-screws variant reassigns PDL space to cortical bone.
- **Loading/constraints**: bite simulated at left P3/P4/M1 occlusal nodes (working = left); working condyle fully fixed, balancing condyle fixed SI+AP only; tied frictionless contacts.
- **Muscle forces**: EMG × PCSA × specific tension (30 N/cm²), applied as time-varying amplitude functions to temporalis (ant/post), masseter (superficial/deep), medial pterygoid on both sides; vectors track moving insertion centroids.
- **Foods**: grapes (soft), dried fruit, nuts (hard) — differing toughness/stiffness.
- **Outputs**: principal/shear strains over the cycle; moments about ML (sagittal bending), SI (transverse bending), AP (twisting) axes through hemimandible and symphysis cross-sections.

## Results

- **Peak timing**: moments peak ~35–40% (no-screws: nuts 40%, grapes 35%, dried fruit 39%); peak principal strains ~35–40%; generally highest for nuts, lowest for dried fruit.
- **Spatial loading**: sagittal bending highest at balancing-side anterior ramus/posterior corpus then working-side anterior corpus below bite point; twisting highest on working side behind bite point and at symphyseal incisor section; transverse bending peaks at symphysis.
- **Deformation regimes**: ramus twisting (coronoid inversion + angle eversion), sagittal bending, lateral transverse bending (wishboning). Grape chewing shows early lateral transverse bending (early balancing-side superficial masseter + medial pterygoid recruitment); nut chewing shows late, larger sagittal + transverse bending.
- **Temporal food differences**: early-cycle (10–30%) strains grapes > nuts > dried fruit; late-cycle (>30%) strains nuts > grapes > dried fruit — mirroring EMG amplitude differences.
- **Strain hotspots (ε1)**: coronoid process/endocoronoid ridge, anterior ramus border, plana triangulares, external oblique lines, extramolar sulci, lateral prominences, inferior transverse torus, medial prominence, torus triangularis, endocondylar ridge.
- **Dynamic > static**: dynamic FEM captured peak strains over a larger area of balancing-side corpus/ramus and across multiple working-side regions the static FEM did not identify.

## Related Papers

- [[occlusion/ambili-2024-parafunctional-loading-stress-tooth-implant-fea]] — methodological contrast: this and other dental FEA pages use static single-load FEA; Panagiotopoulou shows dynamic loading reveals patterns static models miss.
- [[occlusion/yesilyurt-2021-occlusion-concepts-hybrid-abutment-zirconia-fea]] — another static occlusal FEA whose single-time-point assumption this dynamic primate model directly challenges.
- [[occlusion/sippy-2021-condylar-incisal-guidance-canine-group-function-schemes]] — occlusal scheme / guidance and resulting muscle-driven loading patterns.
- [[tmj/wang-2024-tmj-ovd-elevation-occlusal-loss-rats]] — animal model of occlusal loading on the masticatory apparatus; complements this macaque chewing-biomechanics evidence.
