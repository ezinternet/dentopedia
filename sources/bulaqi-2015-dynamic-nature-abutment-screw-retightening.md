---
title: "Dynamic nature of abutment screw retightening: finite element study of the effect of retightening on the settling effect"
authors: "Haddad Arabi Bulaqi, Mahmoud Mousavi Mashhadi, Hamed Safari, Mohammad Mahdi Samandari, Farideh Geramipanah"
year: 2015
doi: "10.1016/j.prosdent.2014.09.017"
category: [prosthetic-materials]
source_collection: pubmed-text
full_text: false
pmid: "25749092"
source_url: https://pubmed.ncbi.nlm.nih.gov/25749092/
text_path: /Users/oracleneo/llm-wiki/papers/bulaqi-2015-dynamic-nature-abutment-screw-retightening.txt
text_filename: bulaqi-2015-dynamic-nature-abutment-screw-retightening.txt
---

## Why Ingested

기존 settling-effect 클러스터([[prosthetic-materials/kim-2020-axial-displacements-removal-torque-changes]] static-loading settling, [[prosthetic-materials/ren-2024-morse-taper-abutment-subsidence-locking-force]] subsidence, [[prosthetic-materials/pardal-pelaez-2017-preload-loss-abutment-screws-dynamic-fatigue]] dynamic fatigue)는 세틀링이펙트의 *결과*(preload 손실량·removal torque 변화)는 측정하지만 *왜* 세틀링이 일어나고 *재조임(retightening)이 왜 그것을 회복시키는지*의 메커니즘은 비워둔다. 본 FEA 논문은 마찰계수(coefficient of friction)와 표면 거칠기가 settling effect를 어떻게 구동하는지, 그리고 retightening이 settling을 줄이되 preload는 거의 못 올리는 이유를 동역학 시뮬레이션으로 설명해 그 메커니즘 공백을 채운다. [[prosthetic-materials/nithyapriya-2018-factors-loss-preload-dental-implants]]의 "factors of preload loss" 서술을 정량적 메커니즘으로 보강.

## One-line Summary

Finite element analysis (dynamic simulation, single Straumann implant–abutment–crown model) showing that rougher thread surfaces (higher coefficient of friction) increase the settling effect and reduce remaining torque/preload, while retightening reduces the settling effect but has only an insignificant effect on preload — with the retightening benefit amplified at high friction.

## 한줄요약

유한요소해석(FEA 동역학 시뮬레이션, Straumann 임플란트-지대주-크라운 단일 모델) — 나사산 표면이 거칠수록(마찰계수↑) 세틀링이펙트가 커지고 잔류 토크·프리로드가 감소하며, 재조임(retightening)은 세틀링이펙트를 줄이지만 프리로드는 거의 못 올리고, 이 재조임 효과는 마찰이 높을수록 더 커진다.

## 1. Document Information

- **Journal**: The Journal of Prosthetic Dentistry, 2015 May;113(5):412–419
- **DOI**: 10.1016/j.prosdent.2014.09.017 · **PMID**: 25749092
- **Type**: Computational study (finite element / dynamic simulation), in vitro–equivalent
- **Affiliations**: School of Mechanics, University of Tehran (Mechanical Engineering); Qom & Tehran University of Medical Sciences (Dentistry), Iran
- **Source artifact**: PubMed structured abstract only — **PMC full text not available** (no PMC ID). Absolute numeric preload/torque values and the exact friction-coefficient settings are not recoverable from the abstract.

## 2. Key Contributions

- Models the **entire dynamic sequence** of an abutment screw — tightening → relaxation → **retightening** → second relaxation — rather than a single static tightening snapshot, which the authors argue is why prior work failed to capture the true nature of screw loosening.
- Isolates the **coefficient of friction** (via fine / regular / rough thread surface characterization) as the driver linking surface roughness to settling and preload.
- Shows **retightening reduces the settling effect but does not meaningfully raise preload** — a mechanistic explanation for why "re-torque after 10 min" protocols help seating yet do not restore lost clamping force.
- Demonstrates the retightening benefit is **friction-dependent**: larger at high coefficients of friction.

## 3. Methodology and Architecture

- **Models**: precise CAD models of a Straumann dental implant, directly attached crown, abutment screw, and surrounding bone.
- **Threaded interfaces**: spiral thread helix with defined static and kinetic friction coefficients; surfaces characterized as **fine, regular, rough**.
- **Solver**: Abaqus, dynamic simulation. Rotational displacement applied to the abutment screw with torque control across steps: tightening, relaxation, retightening, second relaxation — repeated at different coefficients of friction.
- **Outcome**: obtained torque and preload values compared to predicted values; settling effect quantified across surface/friction conditions.

## 4. Key Results and Benchmarks

- **Surface roughness ↑ (fine → rough)** → remaining torque ↓, preload ↓, **settling effect ↑**.
- **Retightening** → remaining torque ↑, preload ↑, **settling effect ↓**.
- **Lower coefficient of friction** → higher preload, lower settling effect.
- **Retightening reduced settling effect but had an *insignificant* effect on preload.**
- At **high coefficients of friction, the retightening effect was intensified**.
- (Absolute Ncm / N preload magnitudes not available in abstract-only source.)

## 5. Limitations and Future Work

- **Abstract-only ingest**: full text/figures unavailable; absolute values and convergence details not captured here.
- **FEA model** of a single Straumann geometry — results are connection-/geometry-specific and idealized (no manufacturing tolerance, no contamination, no cyclic mastication).
- Static/dynamic simulation of friction does not reproduce in-vivo lubrication, saliva, or repeated load cycling.

## 6. Related Work

- Static-loading settling measurement: Kim & Lim 2020 (Materials) — five implant–abutment connections.
- Preload-loss factor reviews and dynamic-fatigue / connection-design studies that quantify the *outcome* this paper mechanistically explains.

## 7. Glossary

- **Settling effect (embedment relaxation)**: micro-flattening of contacting thread/seat asperities under load, reducing the effective screw elongation and thus the clamping preload after initial tightening.
- **Preload**: tensile clamping force generated in the abutment screw by applied tightening torque; resists joint separation under function.
- **Coefficient of friction**: ratio governing tangential resistance at the thread interface; higher μ converts more input torque into friction loss rather than preload.
- **Retightening (re-torque)**: re-applying tightening torque after an initial relaxation interval to recover seating lost to settling.
- **FEA**: finite element analysis — numerical solution of stress/strain over a meshed geometry.
