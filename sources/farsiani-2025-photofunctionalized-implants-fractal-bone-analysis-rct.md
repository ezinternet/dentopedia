---
title: "Evaluation of the bone structure surrounding photofunctionalized implants using the fractal analysis method: a split-mouth randomized clinical study"
authors: Farsiani H, Bagis N, et al.
year: 2025
doi: 10.1186/s12903-025-06330-6
category: [implants/surface]
source_collection: pubmed-text
full_text: true
pmid: "40598042"
pmcid: "PMC12220636"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12220636/
text_path: /Users/oracleneo/llm-wiki/papers/farsiani-2025-photofunctionalized-implants-fractal-bone-analysis-rct.txt
text_filename: farsiani-2025-photofunctionalized-implants-fractal-bone-analysis-rct.txt
---

## Why Ingested

This split-mouth RCT adds patient-level radiomorphometric (fractal dimension, FD) evidence of peri-implant trabecular bone quality after UV photofunctionalization (PF) — claimed by the authors to be the *first* human study using fractal analysis (FA) to evaluate PF effects on peri-implant bone. It extends the stability/MBL clinical signal in [[implants/surface/hirota-2020-uv-photofunctionalization-dental-implant-7year]] and the meta-analytic findings in [[implants/surface/plasma/pesce-2020-photo-plasma-activation-titanium-sr-ma]] by supplying a non-ISQ, imaging-based surrogate marker for osseointegration. It also complements the ISQ-based UV case reports in [[implants/isq/seol-2017-uv-implant-resonance-frequency-early-loading]].

## One-line Summary

Split-mouth double-blind RCT (BMC Oral Health 2025; 21 patients, 42 implants in bilateral posterior mandible): UV-photofunctionalized (test) implants showed a statistically significant pre-to-post-placement rise in peri-implant trabecular fractal dimension (FD 1.075 → 1.103, p=0.044), whereas non-PF controls did not (1.113 → 1.118, p=0.794); early survival 100% in both arms, no ISQ collected.

## 한줄요약

분할입(split-mouth) 이중맹검 RCT (BMC Oral Health 2025, 환자 21명·임플란트 42개, 양측 하악 구치부): UV 광기능화 (Photofunctionalization, PF) 처리군은 식립 전→후 임플란트 주위 해면골 프랙탈 차원 (Fractal Dimension, FD)이 유의하게 상승(1.075→1.103, p=0.044)했으나 비처리 대조군은 무변화(1.113→1.118, p=0.794); 양군 모두 조기 생존율 100%, 임플란트 안정성 지수 (ISQ)는 측정 안 함.

## 1. Document Information

- **Journal**: BMC Oral Health (2025)
- **DOI**: 10.1186/s12903-025-06330-6 | **PMID**: 40598042 | **PMCID**: PMC12220636
- **Institution**: Ankara University Faculty of Dentistry, Turkey
- **Type**: Randomized, split-mouth, double-blind clinical trial (CONSORT-adherent; ClinicalTrials.gov registered)
- **Ethics**: Clinical Research Ethics Committee Approval No. 36290600/34/2021
- **Authors**: Listed in source as "Farsiani H, Bagis N, et al." Full given names were not recoverable from the PMC full-text body. Investigator initials cited in the methods: implanting clinician **H.F.** (first author Farsiani H), intervention assignment **F.K.** and **Z.D.G.**, blinded radiographic analyst **E.P.B.** (Bagis/Bagış N likely the supervising author).

## 2. Key Contributions

- **First human study** to apply fractal analysis (FA) on panoramic radiographs to evaluate the effect of UV photofunctionalization on peri-implant bone (prior PF evidence in humans was limited to ISQ or CBCT; cellular/animal level otherwise).
- Provides a **non-invasive, ISQ-independent imaging surrogate** (FD from box-counting) for osseointegration / bone-quality gain.
- Split-mouth design controls for patient-level confounders (systemic/bone-metabolic factors, age) — each patient is their own control.
- Demonstrates a statistically significant within-patient FD increase for PF-treated sites that is absent in untreated controls.

## 3. Methodology and Architecture

- **Design**: Randomized, split-mouth, double-blind RCT. Each patient with **bilateral edentulous posterior mandible** received a test (PF) implant on one side and a control (non-PF) implant on the other.
- **Sample**: 21 patients (12 F, 9 M; mean age 50.43 ± 9.22 y), 42 implants total (21 test, 21 control). Power analysis (G*Power, two-tailed paired t-test, Cohen's d=0.5, α=0.05, power=0.80) → 21 implants/group.
- **Implants**: Gravis Dental Implants (STARK, Turkey), all packaged ≥6 months prior; standard length/diameter only (to remove crown-root-ratio/dimension confounding); placed by a single clinician (H.F.). Mandibular premolar + molar regions.
- **PF protocol**: Test implants irradiated with UV for **10 s** per manufacturer recommendation (Dentis Co. LTD, South Korea), then **immediately** inserted. Implants removed from glass/plastic packaging before irradiation (UV does not penetrate glass).
- **Randomization**: Coin flip (heads→test, tails→control). Enrollment by study coordinator; allocation by two independent investigators (F.K., Z.D.G.); implanting clinician blinded to analysis; radiographic analysis by separate blinded investigator (E.P.B.).
- **Imaging**: Panoramic radiographs (Planmeca ProMax; 64 kV, 10 mA, 10 s), exported uncompressed TIFF at 300 dpi. Timepoints: **pre-implant (1st panoramic)** and **post-placement / follow-up (2nd panoramic, ~12–16 weeks)**.
- **ROI**: 25 × 25 pixels, **apical to the implant**, in trabecular bone (no overlap with cortex/adjacent structures); localized in MicroDicom using horizontal line to nearest adjacent tooth + vertical line along implant long axis; same reference re-applied to the pre-implant radiograph. Aligned via anatomical landmarks (adjacent teeth, mental foramen).
- **FDA**: ImageJ 1.49x, **White & Rudolph box-counting method**. Pipeline: crop → 400% upsampling (interpolation) → Gaussian blur (σ=35) → subtraction from original → +128 gray, threshold=128 → binarization → erosion/dilation → inversion → skeletonization. FD = slope of log-log box-count plot over box sizes 2–64 px (2,3,4,6,8,12,16,32,64).
- **Outcomes**: Primary = effect of PF placement on bone-formation quality (FD); secondary = effect of osseointegration process on FD.
- **Statistics**: SPSS 26. Shapiro-Wilk → non-normal → Wilcoxon signed-rank (intra-group), Mann-Whitney U (inter-group), Kruskal-Wallis (group×gender). Intra-observer reliability via Spearman on 20 repeated images 1 month apart.
- **ISQ / mechanical stability**: **NOT measured** (explicit limitation).

## 4. Key Results and Benchmarks

- **No participant withdrawals**; intra-observer reliability satisfactory (Spearman, p>0.05 = consistent).
- **No significant pre-treatment FD difference between sites** for the matched analysis.

**Within-group change (Table 2; mean ± SD (median)):**

| Side | 1st panoramic (pre) | 2nd panoramic (post) | Δ p (Wilcoxon) |
|---|---|---|---|
| Control (non-PF) | 1.113 ± 0.064 (1.102) | 1.118 ± 0.056 (1.105) | **0.794 (NS)** |
| Test (PF) | 1.075 ± 0.067 (1.053) | 1.103 ± 0.047 (1.092) | **0.044*** |

**Between-group comparison (Mann-Whitney):** 1st panoramic differed (control 1.113 vs test 1.075, p=0.021*); by 2nd panoramic the gap closed (control 1.118 vs test 1.103, p=0.428 NS) — i.e., PF sites caught up.

- **Region-specific (Table 1):** significant FD increase observed in the **#45 region** subjected to PF (p=0.046*).
- **Gender (Table 3):** no significant male/female differences within either group; no significant Δ1–2 by sex (all p>0.05).
- **Survival/bone loss:** **100% early survival in both arms**; no implant/bone loss; healing abutments placed on all by month 3–4 confirming integration. No MBL or ISQ values reported.

**Bottom line:** UV-PF sites started with lower trabecular FD but underwent a statistically significant FD gain post-placement and converged toward control levels, interpreted as PF-enhanced trabecular bone complexity / accelerated osseointegration.

## 5. Limitations and Future Work

- **Small, single-center sample** (n=42 implants) — pilot-grade; limited generalizability.
- **Panoramic (2D) instead of CBCT** — lower spatial resolution/precision (chosen for lower dose; authors argue 2D FA is reliable with standardized acquisition).
- **No ISQ or mechanical stability** — functional/clinical outcome cannot be correlated; FD effect lacks a clinical-measurement anchor.
- ROI location/size sensitivity not fully resolved; intra-observer variability acknowledged.
- Authors call for larger prospective multicenter trials and pairing FA with ISQ/CBCT.

## 6. Related Work

- [[implants/surface/hirota-2020-uv-photofunctionalization-dental-implant-7year]] — 7-yr prospective UV-PF clinical outcomes (ISQ-based); this paper adds an FA-based imaging surrogate.
- [[implants/surface/plasma/pesce-2020-photo-plasma-activation-titanium-sr-ma]] — SR+MA of photo/plasma Ti activation; this RCT is patient-level primary evidence consistent with its osseointegration signal.
- [[implants/isq/seol-2017-uv-implant-resonance-frequency-early-loading]] — UV-PF ISQ case reports (stability dip absent); complementary stability-based readout.
- [[implants/surface/park-2025-uv-photofunctionalization-osseointegration-soft-tissue]] — comprehensive UV-PF narrative review (bone/soft-tissue/bacterial interfaces).
- [[implants/surface/ogawa-2025-3d-theory-osseointegration-material-topography]] — D3 (time/aging) osseointegration theory underpinning why PF reverses Ti biological aging.

## 7. Glossary

- **Photofunctionalization (PF, 광기능화)**: UV irradiation of Ti that converts the surface from hydrophobic to superhydrophilic, removes hydrocarbon contamination, restores electropositivity → enhanced protein adsorption, osteoblast adhesion, antibacterial behavior.
- **Fractal dimension / fractal analysis (FD / FDA, 프랙탈 차원/분석)**: mathematical quantification of trabecular bone structural complexity from radiographs; higher FD = more complex/dense trabeculation.
- **Box-counting method (White & Rudolph)**: standard FD computation — overlay grids of varying box size, count boxes containing the skeletonized trabecular pattern, FD = slope of log-log plot.
- **ROI (Region of Interest)**: 25 × 25 px trabecular area apical to the implant used for FD measurement.
- **Split-mouth design**: each patient receives test and control interventions on opposite sides — patient acts as own control.
- **ISQ (Implant Stability Quotient)**: RFA-derived stability metric — **not** measured here (key limitation).
