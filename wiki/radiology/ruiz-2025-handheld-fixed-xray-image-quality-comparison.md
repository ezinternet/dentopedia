---
title: "A Comparative Investigation of the Quality of Radiographs Produced by Portable Handheld and Fixed X-Ray Units"
authors: Débora Costa Ruiz, Matheus L. Oliveira, Rocharles Cavalcante Fontenele, Deborah Queiroz Freitas, Francisco Haiter-Neto
year: 2025
date: 2025-01-01
doi: 10.1590/0103-644020256319
source: ruiz-2025-handheld-fixed-xray-image-quality-comparison.md
category: [radiology]
confidence: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "41172496"
pmcid: "PMC12551989"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12551989/
text_path: /Users/oracleneo/llm-wiki/papers/ruiz-2025-handheld-fixed-xray-image-quality-comparison.txt
text_filename: ruiz-2025-handheld-fixed-xray-image-quality-comparison.txt
tags: [handheld-xray, image-quality, cmos-sensor, intraoral-radiography]
---

## One-line Summary

In-vitro comparative study (acrylic block + aluminum step-wedge phantoms, 2 CMOS sensor systems, 6 exposures/condition, n=48 radiographs total) found handheld portable intraoral X-ray equipment produced significantly higher brightness and lower contrast than fixed intraoral X-ray equipment regardless of sensor (p<0.0001), sensor-dependent noise effects (p<0.05), and no significant uniformity difference (p>0.05).

## 한줄요약

체외(in-vitro) 비교연구(아크릴 블록·알루미늄 스텝웨지 팬텀, CMOS 센서 2종, 조건당 6회 촬영, 총 48장)에서 휴대형(handheld) 구강내 X선 장비는 센서와 무관하게 고정형(fixed) 장비보다 밝기(brightness)가 유의하게 높고 대비(contrast)는 유의하게 낮았으며(p<0.0001), 노이즈(noise)는 센서에 따라 방향이 달랐고(p<0.05) 균일도(uniformity)는 유의한 차이가 없었다(p>0.05).

## Summary

This in-vitro study objectively compared the image quality of a handheld portable intraoral X-ray unit (Eagle X-ray, 60 kVp/2.5 mA/0.45 s, platform-mounted to remove hand-movement variability) against a fixed intraoral X-ray unit (Focus, 60 kVp/7 mA/0.16 s), matched to near-identical mAs. Radiographs of an acrylic block (brightness, noise, uniformity) and an aluminum step-wedge (contrast) were acquired with two CMOS sensor systems (Digora Toto, Snapshot) and analyzed via ImageJ gray-value ROI measurements. Handheld equipment produced significantly higher brightness and lower contrast than fixed equipment on both sensors; noise was higher with handheld equipment on Digora Toto but lower on Snapshot; uniformity did not differ significantly on either sensor. The authors argue these statistically significant differences are likely clinically imperceptible and consistent with prior diagnostic-outcome literature showing handheld equipment does not compromise caries diagnosis, though root resorption/fracture/periodontal bone loss diagnostic performance with handheld equipment remains understudied.

## Key Contributions

- First objective (ImageJ gray-value) rather than subjective/examiner-rated comparison of handheld vs fixed intraoral X-ray image quality across two different CMOS sensor systems.
- Methodologically isolates equipment-intrinsic effects from operator hand-movement/fatigue by platform-mounting the handheld unit.
- Shows noise direction is sensor-dependent (increases with Digora Toto, decreases with Snapshot when using handheld equipment), implicating sensor sensitivity/processing algorithms/scintillator material/detector electronics as interacting variables rather than a uniform handheld noise penalty.
- Provides a reusable step-wedge % contrast-variation quantification method for future handheld-vs-fixed image-quality comparisons.
- Explicitly frames the gap between statistically significant objective gray-value differences and the absence of compromised diagnostic accuracy in prior caries-detection literature.

## Methodology

In-vitro experimental comparative study (no human/animal subjects). Equipment: Eagle X-ray handheld portable unit (60 kVp, 2.5 mA, 0.45 s, 1.125 mAs, platform-mounted) vs Focus fixed intraoral unit (60 kVp, 7 mA, 0.16 s, 1.12 mAs); exposure times pilot-selected by two dentomaxillofacial radiologists (5 years' experience) for matched mAs. Sensors: size-2 CMOS (Digora Toto, Scanora software) and size-1 CMOS (SnapShot, Cliniview software), tested separately. Brightness/noise/uniformity phantom: 30×40×30 mm acrylic block, 6 radiographs per sensor per equipment (24 total), 8-bit TIFF, ImageJ analysis — brightness/noise from a central ROI (16% of image area, mean/SD of gray values); uniformity from a central 4×4 mm ROI plus four symmetric peripheral 4×4 mm ROIs (averaged SDs), ROI placement standardized via ImageJ macros. Contrast phantom: aluminum step-wedge (6 steps, 2–12 mm), same parameters (24 radiographs total); % contrast variation = (Mean ROI at 10 mm step − Mean ROI at 4 mm step) / Mean ROI at 10 mm step × 100. Statistics: Student's t-test, alpha=5%, 95% power, SPSS 25.0. All exposures used a fully charged handheld battery to exclude battery-dependent tube-voltage drift as a confound.

## Results

- **Digora Toto sensor**: brightness handheld 65.41±0.86 vs fixed 57.66±1.04 (p<0.0001); noise handheld 14.48±0.24 vs fixed 13.10±0.27 (p<0.0001, handheld higher); uniformity handheld 9.48±0.23 vs fixed 9.53±0.12 (p=0.661, NS); contrast handheld 31.85%±0.04 vs fixed 32.99%±0.03 (p<0.0001, handheld lower).
- **Snapshot sensor**: brightness handheld 85.38±0.19 vs fixed 68.95±0.27 (p<0.0001); noise handheld 1.05±0.02 vs fixed 1.12±0.01 (p=0.001, handheld lower); uniformity handheld 1.00±0.08 vs fixed 1.03±0.00 (p=0.445, NS); contrast handheld 42.81%±0.18 vs fixed 47.69%±0.02 (p<0.0001, handheld lower).
- Consistent pattern across both sensors: handheld equipment → higher brightness, lower contrast (both p<0.0001). Noise direction is sensor-dependent (higher with Digora Toto, lower with Snapshot, both p<0.05). Uniformity is not significantly affected by equipment type on either sensor (p>0.05).
- Authors interpret the noise-difference magnitude as small relative to brightness/contrast differences and likely clinically imperceptible, consistent with prior literature that handheld-equipment gray-value shifts have not compromised caries-lesion diagnostic accuracy.

## Related Papers

- [[radiology/geibel-2025-mobile-handheld-radiography-quality-nursing-home]] — complementary real-world clinical-quality-criteria assessment of mobile/handheld dental radiography; this paper supplies the controlled objective gray-value mechanism (brightness/contrast/noise/uniformity) behind that paper's clinical-quality observations.
- [[radiology/farman-2010-panoramic-ccd-storage-phosphor-film]] — related methodological precedent for objective digital-sensor image-quality comparison in dental radiography, though for panoramic CCD vs storage-phosphor rather than intraoral CMOS handheld-vs-fixed.
