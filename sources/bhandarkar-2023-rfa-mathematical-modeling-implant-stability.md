---
title: "A two-degree of freedom mathematical modelling of a dental implant to estimate frequency and micro-displacement using electromagnetic RFA"
authors: Shubham Bhandarkar, Aditya Badgujar, Shreyas Rajebahadur, Pankaj Dhatrak
year: 2023
doi: 10.1016/j.prime.2023.100314
category: implants/isq
pdf_path: /Users/oracleneo/llm-wiki/papers/bhandarkar-2023-rfa-mathematical-modeling-implant-stability.pdf
pdf_filename: bhandarkar-2023-rfa-mathematical-modeling-implant-stability.pdf
source_collection: external
---

## One-line Summary
Engineering / in-vitro mathematical model (2 DOF) of a dental implant under electromagnetic resonance frequency analysis (RFA): finite element analysis derived stiffness/damping; MATLAB FFT analysis of an input range 5–15 kHz extracted resonance frequencies and corresponding maximum micro-displacements; the framework validates and quantifies the electromagnetic RFA technique for monitoring primary implant stability.

## 1. Document Information
- **Journal**: e-Prime — Advances in Electrical Engineering, Electronics and Energy, Vol 6 (2023) 100314
- **DOI**: 10.1016/j.prime.2023.100314
- **Available online**: 10 October 2023
- **Institution**: School of Mechanical Engineering, Dr. Vishwanath Karad MIT World Peace University, Pune, India
- **License**: CC BY-NC-ND 4.0 (open access)
- **Study type**: Mathematical model + finite element analysis (in-vitro / engineering)

## 2. Key Contributions
- Provides a **2-degree-of-freedom (2-DOF) mathematical model** of the implant-bone interface suitable for analyzing electromagnetic RFA signals.
- Couples FEA-derived stiffness and damping with vibration theory to predict micro-displacement at the implant top.
- Demonstrates that **5–15 kHz** is an appropriate excitation band to resolve resonance frequencies and associated micro-mobility.
- Underpins the engineering basis of commercial devices such as Osstell (magnetic RFA) and Penguin RFA.

## 3. Methodology and Architecture
- **Geometry / FEA**: implant model (likely Ti-6Al-4V) embedded in cortical and trabecular bone; FEA used to compute stiffness (k) and damping (c) values.
- **2-DOF model**: implant top mass + abutment-coupling mass; springs and dampers represent peri-implant bone.
- **Excitation**: electromagnetic forcing across 5–15 kHz swept input in MATLAB; output micro-displacement plotted in time and frequency domain via FFT.
- **Outputs**: resonance frequency (f_r), maximum micro-displacement amplitude, and frequency-response curves.

## 4. Key Results and Benchmarks
- **Input frequency band 5–15 kHz** captures the principal resonance peak of a typical dental implant.
- Resonance frequency from the 2-DOF model maps to the ISQ (Implant Stability Quotient) scale used clinically.
- Higher stiffness (denser cortical bone, more BIC) → higher resonance frequency → higher ISQ; lower micro-displacement at the resonance peak.
- The 2-DOF model reproduces measured behavior closely enough to validate the magnetic RFA principle.

## 5. Limitations and Future Work
- In-vitro / theoretical: no clinical RFA correlation data here; readers must integrate with clinical RFA validation (Osstell papers).
- Simplified bone model — does not address non-linear viscoelastic behavior of trabecular bone.
- 2-DOF is a minimal model; higher-DOF models (or full FEA modal analysis) could refine accuracy.
- Effect of implant macro-design (taper, thread pitch) is partially abstracted.

## 6. Related Work
- Zix 2008 — clinical RFA (Osstell) vs Periotest comparison.
- Sennerby 2008, Huang 2020 — ISQ theory and clinical interpretation.
- Pagliani 2013 — RFA vs lateral displacement bench study.
- Herrero-Climent 2013 — Osstell reliability (ICC 0.97).

## 7. Glossary
- **RFA**: Resonance Frequency Analysis — non-invasive method to estimate implant stability via the resonance of a transducer mounted on the implant.
- **2 DOF**: two-degree-of-freedom mathematical model (two independent generalized coordinates).
- **FFT**: Fast Fourier Transform — converts time-domain signal to frequency-domain spectrum.
- **ISQ**: Implant Stability Quotient (clinical RFA scale 1–100, derived from resonance frequency).
- **BIC**: Bone-to-Implant Contact.
