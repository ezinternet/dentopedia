---
title: "Evaluation of the Accuracy of Digital Workflow for Implant-Supported Full-Arch Fixed Dental Prostheses Using a Novel Micro-CT Measurement Technique"
authors: Fouda A, Wyatt C, McCullagh A, Vora SR, Ford NL, Gebril M
year: 2025
doi: 10.1111/jopr.14061
category: [digital-workflow]
source_collection: pubmed-text
full_text: true
pmid: "40285405"
pmcid: "PMC13247621"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13247621/
text_path: /Users/oracleneo/llm-wiki/papers/fouda-2025-accuracy-digital-workflow-implant-fullarch.txt
text_filename: fouda-2025-accuracy-digital-workflow-implant-fullarch.txt
---

## Why Ingested

사용자가 CAD/CAM 치과기공소 관련 논문을 요청 — 본 in-vitro micro-CT 연구는 [[wiki/digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]]가 다룬 IOS 전악 스캔 trueness 문제를, 실제 티타늄 프레임워크 passivity(단일나사검사/나사저항검사)까지 연결해 "스캔 오차 → 프레임워크 오적합" 인과 사슬을 직접 검증한 첫 연구로서 가치가 있다.

## One-line Summary

In-vitro micro-CT study (10 milled titanium full-arch frameworks from TRIOS 5 IOS scans on a 4-implant edentulous model): none acceptable by single-screw-test micro-CT, only 3/10 acceptable by final-fit-test micro-CT; subjective non-passivity rates 60% (SST) and 80% (SRT); only 2/10 intraoral scans fell within the 150 µm acceptable deviation vs. lab-scanner control, indicating scanning error as the dominant misfit source.

## 한줄요약

In-vitro micro-CT 연구 (4-임플란트 무치악 모델에서 TRIOS 5 IOS 스캔으로 제작한 티타늄 전악 프레임워크 10개): 단일나사검사 micro-CT 기준 전부 부적합, 최종 체결 micro-CT 기준 3/10만 적합; 주관적 비수동성(non-passivity)률 60%(SST)·80%(SRT); 실험실 스캐너 대비 150μm 이내에 든 구강스캔은 2/10에 불과해 오적합의 주된 원인이 스캔 오차임을 시사.

## 1. Document Information

- **Title**: Evaluation of the accuracy of digital workflow for implant-supported full-arch fixed dental prostheses using a novel micro-CT measurement technique
- **Authors**: Fouda A, Wyatt C, McCullagh A, Vora SR, Ford NL, Gebril M
- **Journal**: Journal of Prosthodontics, 2025;35(5):721-731
- **DOI**: 10.1111/jopr.14061
- **PMID**: 40285405 / **PMCID**: PMC13247621
- **Study type**: In-vitro (bench) study
- **Funding/COI**: Authors declare no conflicts of interest

## 2. Key Contributions

- First study to evaluate full-arch (not short-span) titanium framework fit accuracy using high-resolution micro-CT, rather than verification jigs or visual/tactile tests alone.
- Proposes a new 5-category classification of implant framework misfit: perfect fit, vertical misfit, horizontal misfit, combined vertical+horizontal misfit, and angular misfit.
- Directly links intraoral-scanner (IOS) trueness error to downstream framework passivity failure by superimposing each IOS-derived STL against a high-accuracy laboratory scanner (4 µm accuracy) control, isolating scanning error from milling/design error.
- Quantifies non-passivity under both objective (micro-CT gap measurement) and subjective (single-screw test, screw-resistance test) methods on the same 10 frameworks.

## 3. Methodology and Architecture

- 3D-printed edentulous mandibular model (3Shape design, resin-printed) with removable gingival mask; 4 ELOS implant analogs with multi-base abutments.
- Baseline micro-CT (Scanco µ100, 90 kVp/200 µA, 36.8 µm isotropic voxel) taken with temporary cylinders hand-tightened, establishing ground-truth gaps.
- Intraoral scanning: TRIOS 5 (3Shape) using BLO (buccal-lingual-occlusal) scan pattern, chosen per prior literature (Gomez-Polo et al.) for superior trueness/precision vs. zigzag/circumference patterns in full-arch implant cases. 20 calibration scans + 10 scans used for framework fabrication.
- Scanning-error control: same model scanned with E4 lab scanner (3Shape, 4 µm accuracy); each IOS STL superimposed on lab-scan STL in Medit Link software, non-scan-body regions erased, RMS heatmaps generated (100 µm visual tolerance); superimposition-method error itself verified as ~0.0055 RMS (negligible).
- 10 titanium (Grade 5) frameworks designed in Exocad, milled on a Zirkonzahn M1 milling machine.
- Fit assessment — objective: each framework micro-CT-scanned twice: (1) SST-CT — only terminal implant screw hand-tightened, simulating single-screw (Sheffield) test; (2) FFT-CT — all screws hand-tightened, simulating final seating. Marginal gaps measured at 8 points/implant, internal gaps at 12 points/implant (Microview software). Total measurement points: baseline 48, SST-CT 480, FFT-CT 480 (internal); 32/320/320 (marginal).
- Fit assessment — subjective: two blinded prosthodontists performed SST (tighten terminal screw, check contralateral gap) and SRT (screw-resistance test — misfit if >half turn needed for seating) on all 10 frameworks after removing the gingival mask.
- Statistics: Kolmogorov-Smirnov/Shapiro-Wilk normality tests; non-parametric internal/marginal fit data analyzed with Friedman's + Dunn's tests; parametric RMS data with paired t-test (SPSS v29).
- Acceptable misfit thresholds cited: ≤150 µm (Kan et al.), ≤100 µm (Katsoulis et al., Jemt et al.); vertical misfit ≤100 µm and horizontal misfit ≤345 µm tolerated per broader literature.

## 4. Key Results and Benchmarks

- **Objective (micro-CT) fit**: 0/10 frameworks acceptable by SST-CT; 3/10 acceptable by FFT-CT. Internal discrepancy differed significantly across baseline/SST-CT/FFT-CT (P<0.001), with SST-CT showing the highest discrepancy. Marginal discrepancy: no significant difference baseline vs. SST-CT, but FFT-CT significantly lower than baseline (P<0.05) — expected because tightening all screws elastically deforms the superstructure to reduce marginal gap without eliminating overall non-passivity.
- **Subjective fit**: non-passivity rate 60% (SST) and 80% (SRT) across the 10 frameworks, assessed by two blinded prosthodontists.
- **Scanning accuracy**: only 2/10 IOS scans fell within the 150 µm clinically acceptable RMS deviation vs. the lab-scanner control; mean RMS for most scans exceeded threshold. No significant anterior-vs-posterior implant location difference in scan deviation (t-test, P=0.902, effect size 0.032).
- **Attribution**: findings point to scanning error as the dominant misfit source (8/10 frameworks), with a smaller subset (2/10) also showing evidence of milling/design error.
- New 5-category misfit classification (perfect / vertical / horizontal / combined / angular) proposed as a framework for future micro-CT misfit studies.

## 5. Limitations and Future Work

- In-vitro design: rigid 3D-printed model with static gingival mask cannot replicate dynamic clinical factors (saliva, tongue mobility, patient-specific biomechanics); authors note real clinical fit may be equal or worse than the bench results.
- Only scanning error was isolated as a source of misfit in this study; milling error was only inferred (not directly isolated) in 2 frameworks — authors state follow-up studies are planned to directly assess milling error contribution.
- Single scanner (TRIOS 5) and single scan protocol (BLO) tested; results may not generalize to other IOS devices/protocols — authors note comparison across studies is difficult given scanner/protocol heterogeneity.
- Single anatomic model (4-implant edentulous mandible) — generalizability to maxillary arches or different implant number/angulation configurations untested.
- Authors recommend incorporating a verification-jig step before final framework fabrication to catch scan-derived misfit before milling.

## 6. Related Work

- Contrasts with Mizumoto et al. and other studies reporting digital impressions comparable/superior to conventional impressions for full-arch cases.
- Consistent with Andriessen et al. (inter-implant distance error >100 µm with IOS in edentulous mandibles), Lyu et al. (digital scanning inferior trueness/precision vs. splinted open-tray impression), Zingari et al. (IOS over/underestimation of scan-body dimensions), Uribarri et al. (scanning angulation error increases with >3 implants; milling error linked to internal/marginal discrepancy).
- Rutkunas et al. and Pera et al. reported no significant passivity difference between digital and conventional workflows — an inconclusive counterpoint in the literature this paper engages with.
- Cites verification-jig literature (Sinada et al., Negreiros et al., Ercoli et al.) supporting a verification-jig step to improve digital workflow passivity — directly informs this paper's recommendation.
- See [[wiki/digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]] (in-vitro IOS full-arch trueness 50-200 µm across devices) and [[wiki/digital-workflow/vitai-2023-intraoral-scanner-complete-arch-sr-network-ma]] (network MA ranking IOS complete-arch accuracy) for the upstream scanning-accuracy evidence this paper builds on.

## 7. Glossary

- **SST / SST-CT**: Single-screw test (Sheffield test) — tightening only the terminal implant screw and observing contralateral gap; SST-CT is its micro-CT-measured analog.
- **FFT-CT**: Final fit test via micro-CT — all screws hand-tightened, gaps measured.
- **SRT**: Screw-resistance test — misfit judged by amount of screw rotation resistance needed to fully seat the prosthesis.
- **RMS (root mean square) deviation**: Statistical measure of the difference between two superimposed 3D scan surfaces, used here to quantify IOS scanning error vs. a lab-scanner control.
- **Trueness / Precision**: Trueness = closeness of a measurement to the true value; precision = reproducibility across repeated measurements.
- **BLO scanning pattern**: Buccal-Lingual-Occlusal intraoral scanning sequence, reported to have better trueness/precision than zigzag or circumference patterns for full-arch implant scans.
- **Passivity / passive fit**: The absence of induced stress between a prosthetic framework and implant components when fully seated and screwed.
