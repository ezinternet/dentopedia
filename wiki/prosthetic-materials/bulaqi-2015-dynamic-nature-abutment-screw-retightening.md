---
title: "Dynamic nature of abutment screw retightening: finite element study of the effect of retightening on the settling effect"
authors: "Bulaqi HA, Mousavi Mashhadi M, Safari H, Samandari MM, Geramipanah F"
year: 2015
date: 2015-05-01
doi: "10.1016/j.prosdent.2014.09.017"
source: bulaqi-2015-dynamic-nature-abutment-screw-retightening.md
category: [prosthetic-materials]
confidence: in-vitro
source_collection: pubmed-text
full_text: false
pmid: "25749092"
text_path: /Users/oracleneo/llm-wiki/papers/bulaqi-2015-dynamic-nature-abutment-screw-retightening.txt
text_filename: bulaqi-2015-dynamic-nature-abutment-screw-retightening.txt
tags: [settling-effect, abutment-screw, preload, retightening, coefficient-of-friction, fea]
relations:
  - type: extends
    target: kim-2020-axial-displacements-removal-torque-changes
  - type: reinforces
    target: nithyapriya-2018-factors-loss-preload-dental-implants
---

## One-line Summary

Finite element dynamic simulation (single Straumann implant–abutment–crown model) showing that rougher thread surfaces (higher coefficient of friction) increase the settling effect and lower remaining torque/preload, whereas retightening reduces the settling effect but has only an insignificant effect on preload — and the retightening benefit grows at high friction.

## 한줄요약

유한요소 동역학 시뮬레이션(Straumann 임플란트-지대주-크라운 단일 모델) — 나사산 표면이 거칠수록(마찰계수↑) 세틀링이펙트가 커지고 잔류 토크·프리로드가 감소하며, 재조임(retightening)은 세틀링이펙트를 줄이되 프리로드는 거의 못 올리고, 그 효과는 마찰이 높을수록 커진다.

> Note: abstract-only ingest — PMC full text was not available (no PMC ID). Directional findings are taken from the structured PubMed abstract; absolute preload/torque magnitudes and the simulated friction-coefficient values are not recoverable. Confidence reflects a computational (FEA) bench study.

## Summary

This finite element study models the **full dynamic life cycle** of an implant abutment screw — tightening, relaxation, retightening, and a second relaxation — to explain *why* screws lose preload (the settling effect) and *why retightening helps*. Using Abaqus dynamic simulation on a Straumann implant–abutment–crown model with thread surfaces characterized as fine, regular, or rough, the authors vary the **coefficient of friction** and track torque, preload, and settling. Rougher surfaces (higher friction) increase the settling effect and reduce the torque/preload retained after tightening. Retightening reduces the settling effect but raises preload only insignificantly, and this retightening benefit is amplified when friction is high. The clinical implication is mechanistic: low-friction, smooth thread interfaces preserve more preload, while a re-torque protocol mainly re-seats the joint (counters settling) rather than restoring lost clamping force.

## Key Contributions

- Frames screw loosening as a **dynamic, multi-step process** (tighten → relax → retighten → relax), not a single static tightening event.
- Identifies the **coefficient of friction / surface roughness** as the lever controlling both settling effect and retained preload.
- Provides a mechanistic basis for clinical **re-torque protocols**: retightening counters settling but does **not** meaningfully recover preload.
- Shows the retightening effect is **friction-dependent** — stronger at high coefficients of friction.

## Methodology

- **Design**: finite element / dynamic simulation (computational bench study).
- **Model**: precise CAD of a Straumann dental implant, directly attached crown, abutment screw, and surrounding bone; threaded interfaces modeled as a spiral thread helix with defined static and kinetic friction coefficients.
- **Surface conditions**: fine, regular, rough.
- **Solver/process**: Abaqus dynamic simulation applying rotational displacement to the screw under torque control across tightening, relaxation, retightening, and second relaxation, repeated at several friction coefficients.
- **Outcomes**: torque and preload (vs predicted values) and the magnitude of the settling effect across surface/friction conditions.

## Results

- Surface **fine → rough** (friction ↑): remaining torque ↓, preload ↓, **settling effect ↑**.
- **Retightening**: remaining torque ↑, preload ↑, **settling effect ↓**.
- **Lower coefficient of friction** → higher preload and lower settling effect.
- **Retightening reduced the settling effect but had an insignificant effect on preload.**
- **High coefficient of friction → retightening effect intensified.**
- Absolute Ncm/N magnitudes not available (abstract-only source).

## Related Papers

- [[prosthetic-materials/kim-2020-axial-displacements-removal-torque-changes]] — extends: Kim measures settling (axial displacement) and removal-torque change across five connections under static load; this FEA explains the friction/roughness mechanism behind that settling.
- [[prosthetic-materials/nithyapriya-2018-factors-loss-preload-dental-implants]] — reinforces: provides the quantitative friction/roughness mechanism for the "factors of preload loss" it reviews.
- [[prosthetic-materials/pardal-pelaez-2017-preload-loss-abutment-screws-dynamic-fatigue]] — relates: dynamic-fatigue preload loss is the in-vitro outcome this simulation rationalizes.
- [[prosthetic-materials/ren-2024-morse-taper-abutment-subsidence-locking-force]] — relates: abutment subsidence/locking-force in Morse-taper joints is a connection-specific manifestation of settling.
- [[prosthetic-materials/vinhas-2022-preload-loss-implant-abutment-connection-designs]] — relates: connection-design dependence of preload loss.
- [[prosthetic-materials/lee-2025-abutment-screw-design-torque-loss-fatigue]] — relates: screw-design effect on torque loss under fatigue.
