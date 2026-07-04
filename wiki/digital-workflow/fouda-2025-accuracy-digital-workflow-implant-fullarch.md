---
title: "Evaluation of the Accuracy of Digital Workflow for Implant-Supported Full-Arch Fixed Dental Prostheses Using a Novel Micro-CT Measurement Technique"
authors: Fouda A, Wyatt C, McCullagh A, Vora SR, Ford NL, Gebril M
year: 2025
date: 2025-04-25
doi: 10.1111/jopr.14061
source: fouda-2025-accuracy-digital-workflow-implant-fullarch.md
category: [digital-workflow]
confidence: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "40285405"
pmcid: "PMC13247621"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13247621/
text_path: /Users/oracleneo/llm-wiki/papers/fouda-2025-accuracy-digital-workflow-implant-fullarch.txt
text_filename: fouda-2025-accuracy-digital-workflow-implant-fullarch.txt
tags: [micro-ct, framework-passivity, full-arch, intraoral-scanner, cad-cam]
---

## Three-line Summary

In-vitro micro-CT study (J Prosthodont Res 2025, 10 milled titanium full-arch frameworks fabricated from TRIOS 5 IOS scans on a 4-implant edentulous model, Scanco µ100 micro-CT at 36.8 µm voxel as reference).

0/10 frameworks were acceptable by single-screw-test micro-CT; only 3/10 passed the final-fit-test micro-CT criterion; subjective non-passivity rates were 60% (SST) and 80% (SRT); and only 2/10 intraoral scans fell within 150 µm RMS deviation vs. the lab-scanner control, implicating scanning error as the dominant misfit source.

Current fully digital workflows using IOS for full-arch implant frameworks cannot reliably achieve passive fit by micro-CT standards; improved scanning accuracy or analog verification steps remain necessary before clinical adoption.

## 세줄요약

In-vitro micro-CT 연구 (J Prosthodont Res 2025, 4-임플란트 무치악 모델에서 TRIOS 5 IOS로 스캔해 제작한 티타늄 전악 프레임워크 10개, Scanco µ100 micro-CT 36.8μm 복셀 기준).

단일나사검사 micro-CT 기준 0/10 부적합; 최종 체결 micro-CT 기준 3/10만 적합; 주관적 비수동성률 60%(SST)·80%(SRT); 실험실 스캐너 대비 RMS 150μm 이내의 구강 스캔은 2/10에 불과해 스캔 오차가 오적합의 주된 원인임을 시사.

현 IOS 기반 완전 디지털 전악 임플란트 프레임워크 워크플로우는 micro-CT 기준 수동 적합을 안정적으로 달성하지 못하므로, 스캔 정확도 개선 또는 아날로그 검증 단계가 임상 도입 전에 필요하다.

## Summary

This in-vitro study tested whether a fully digital workflow (TRIOS 5 intraoral scanning → Exocad design → titanium milling) can produce passively fitting full-arch implant frameworks, using a novel objective measurement technique: micro-computed tomography (micro-CT) of milled titanium frameworks seated on a 4-implant edentulous model, cross-checked against subjective clinical passivity tests (single-screw test, screw-resistance test). The results were uniformly poor — none of 10 frameworks passed the single-screw-test micro-CT criterion, and superimposition analysis traced most of the misfit back to intraoral scanning error rather than milling/design error.

## Key Contributions

- First application of micro-CT (rather than verification jigs or subjective tests alone) to quantify full-arch (not short-span) titanium framework misfit.
- New 5-category misfit classification: perfect fit, vertical misfit, horizontal misfit, combined vertical+horizontal misfit, angular misfit.
- Isolates intraoral scanning error from milling/design error by superimposing each of the 10 IOS-derived STL files against a 4 µm-accuracy laboratory scanner control.
- Cross-validates objective micro-CT misfit measurement against blinded prosthodontists' subjective single-screw test (SST) and screw-resistance test (SRT) assessments on the same frameworks.

## Methodology

3D-printed edentulous mandibular model (3Shape design) with 4 ELOS implant analogs and removable gingival mask. Baseline micro-CT (Scanco µ100, 36.8 µm voxel) established ground-truth gaps with temporary cylinders. TRIOS 5 intraoral scans (BLO scan pattern, 10 scans used for fabrication) were converted to 10 milled titanium (Grade 5) frameworks (Exocad design, Zirkonzahn M1 milling). Each framework was micro-CT scanned under single-screw-test conditions (SST-CT, only terminal screw tightened) and final-fit-test conditions (FFT-CT, all screws tightened), with marginal/internal gaps measured at multiple points per implant (Microview software). Separately, each IOS scan was superimposed against a high-accuracy (4 µm) laboratory scanner scan of the same model to quantify scanning error via RMS heatmaps. Two blinded prosthodontists independently performed SST and SRT on all 10 frameworks. Statistics: Friedman's/Dunn's tests (non-parametric fit data) and paired t-test (parametric RMS data).

## Results

- **0/10 frameworks** acceptable by SST-CT (micro-CT single-screw test); **3/10** acceptable by FFT-CT (final fit test).
- Internal discrepancy differed significantly across baseline/SST-CT/FFT-CT (P<0.001), highest at SST-CT.
- Marginal discrepancy at FFT-CT was significantly lower than baseline (P<0.05) — expected artifact of full screw-tightening elastically deforming the superstructure, not evidence of true passivity.
- Subjective non-passivity rates: **60% (SST)** and **80% (SRT)**.
- Only **2/10 intraoral scans** fell within the 150 µm clinically acceptable RMS deviation vs. the lab-scanner control; most scans exceeded this threshold, implicating scanning error as the dominant source of framework misfit (with a possible additional milling/design error contribution in 2 frameworks).
- No significant difference in scan deviation between anterior and posterior implant locations (P=0.902).

## Related Papers

- [[digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]] — upstream in-vitro evidence of IOS full-arch trueness limitations (50–200 µm range across devices) that this study's scanning-error findings corroborate and extend into downstream framework passivity.
- [[digital-workflow/vitai-2023-intraoral-scanner-complete-arch-sr-network-ma]] — SR+network MA ranking IOS complete-arch scanning accuracy; provides broader device-comparison context for the single-scanner (TRIOS 5) findings here.
- [[implants/del-fabbro-2022-full-arch-tilted-axial-implants-sr-ma]] — clinical full-arch implant prosthesis outcomes literature; this paper's misfit findings offer a mechanistic bench-side explanation for prosthetic complications (screw loosening, framework chipping) reported in such clinical full-arch series.
