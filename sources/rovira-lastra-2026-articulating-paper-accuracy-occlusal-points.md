---
title: "Clinical Strategies to Improve the Accuracy of Articulating Paper for Detecting Occlusal Contact Points in Adults with Natural Dentitions"
authors: "Bernat Rovira-Lastra, Sanaa ElOtmani-Sabiri, Mireia Ustrell-Barral, Laura Khoury-Ribas, Jordi Martinez-Gomis"
year: 2026
doi: "10.3390/diagnostics16101450"
category: [occlusion]
source_collection: pubmed-text
full_text: true
pmid: "42196816"
pmcid: "PMC13206378"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13206378/
text_path: /Users/oracleneo/llm-wiki/papers/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points.txt
text_filename: rovira-lastra-2026-articulating-paper-accuracy-occlusal-points.txt
---

## Why Ingested

교합지(articulating paper)의 정확도 자체를 silicone 기준표준에 대해 정량화한 임상연구. 기존 [[occlusion/didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance]]가 carbon paper와 IOS 일치도를 다뤘다면, 본 논문은 교합지 단독의 true-positive/false-positive를 두께(100 vs 200 µm)·술식(pulling)·악궁(상악 vs 하악)별로 분해해, "교합지는 81%만 검출하고 15%는 위양성"이라는 실측치를 제공한다 — 임상에서 교합지를 어떻게 써야 하는지(200 µm 사용, 양악 일치 확인) 직접적 권고 근거.

## One-line Summary

Cross-sectional test–retest validity study (n=32 natural dentitions, silicone registration as reference standard): articulating paper detected 81% of posterior occlusal contacts (true-positive) with a 15% false-positive rate; 200 µm paper gave fewer false positives (9.4%) than 100 µm (20.6%), the mandibular arch outperformed the maxillary, and the pulling technique made no difference.

## 한줄요약

단면 test–retest 타당도 연구(n=32 자연치열, 실리콘 인기 = 기준표준): 교합지는 구치부 교합접촉의 81%만 검출(진양성)하고 15%는 위양성이었으며, 200 µm 교합지(위양성 9.4%)가 100 µm(20.6%)보다 정확하고 하악궁이 상악궁보다 우수했으며 당기기(pulling) 기법은 차이가 없었다.

## 1. Document Information

- Journal: Diagnostics (Basel), 2026;16(10):1450
- Publication date: 2026-05-10
- DOI: [10.3390/diagnostics16101450](https://doi.org/10.3390/diagnostics16101450) · PMID 42196816 · PMCID PMC13206378
- Design: cross-sectional test–retest criterion-validity study (STROBE)
- Setting: University of Barcelona Dental Hospital, Spain
- Funding/COI: not stated in retrieved full text (MDPI open access)

## 2. Key Contributions

- Quantifies articulating paper validity against a high-fidelity reference standard (scanned silicone Occlufast Rock registration): 81% true-positive, 15% false-positive for posterior contact-point detection.
- Shows 200 µm paper is more accurate than 100 µm — fewer false-positive contacts (9.4% vs 20.6%) and fewer cusp-tip false positives (0.61 vs 1.75/hemiarch) — reversing the intuition that thinner paper = more precise.
- Demonstrates that requiring blue marks to COINCIDE on both maxillary and mandibular arches collapses false positives from 15% to 2.0%.
- Identifies the cusp tip as the dominant false-positive site: ~66% of false positives are blue marks on cusp tips from incidental rubbing.
- Finds the "pulling" technique provides no accuracy benefit; mandibular arch examination yields ~5% more true positives than maxillary.

## 3. Methodology and Architecture

- Population: 32 adults (25 F / 7 M), mean age 24.5 y, ≥24 natural teeth, no edentulous spaces; 3 of 35 excluded for poor image quality.
- Reference standard: polyvinyl siloxane occlusal registration (Occlufast Rock), 1-min max-force clench at intercuspal position, flatbed-scanned, thresholded to 100 µm interocclusal contact areas.
- Test conditions (4 registrations/participant): 100 vs 200 µm Bausch blue paper × passive ("hold") vs active ("pull") technique, per hemiarch; marks scanned with TRIOS 3.
- Image analysis (FIJI/ImageJ): CIELab grayscale conversion, TurboReg alignment to silicone mask, contact point ≥100 px² (~0.5 mm); true-positive = paper point overlapping a silicone black pixel; false-positive = no overlap. Cusp-tip false positives classified separately.
- Reproducibility: full protocol repeated at 2 weeks (test–retest); inter-rater by a second image analyst.
- Statistics: 3 GLM with repeated measures (factors: session, thickness, pulling, arch); ICC for reliability; α=0.05. Sample size powered for sensitivity 70% (precision 7.5%).

## 4. Key Results and Benchmarks

- True positives: overall 81%; significantly higher in mandibular than maxillary arch (~+5%, p<0.001). Thickness, session, technique: no effect on true positives.
- False positives: 200 µm 9.4% vs 100 µm 20.6% (p<0.001); ~15% per single arch → 2.0% when requiring coincidence on both arches.
- Cusp-tip false positives: mean 1.2/hemiarch; 65.9% (95%CI 59.6–72.3) of all false positives on cusp tips; 200 µm 0.61 vs 100 µm 1.75/hemiarch (p<0.001).
- Reliability (ICC): silicone reference inter-rater 0.999 / test–retest 0.976; articulating paper inter-rater 0.56–0.88 / test–retest 0.54–0.82. Test–retest of TP%/FP%/cusp-tip-FP% = 0.571 / 0.615 / 0.247.

## 5. Limitations and Future Work

- Posterior teeth only; anterior detection likely less accurate (more sensitive to mandibular position).
- Young, healthy natural dentitions — not generalizable to extensive restorations, removable/implant-supported prostheses, or occlusal disorders.
- Manual image-correction steps may bias toward overestimating paper accuracy.
- Thinner papers/films (8–40 µm) not tested; digital systems (T-Scan, OccluSense, ModJaw, IOS) not compared head-to-head here.

## 6. Related Work

- Builds on prior work measuring articulating-paper occlusal contact AREA (vs this study's contact-POINT detection focus).
- Complements digital concordance studies (IOS vs carbon paper) and T-Scan reliability literature (good test–retest, excellent inter-rater, but higher false-positive localization).
- Kerstein & Radke / Sutter: subjective interpretation of paper-mark intensity for occlusal FORCE is unreliable — consistent with this study's finding that the expected light-blue/dark-halo chromatic pattern was largely absent.

## 7. Glossary

- True positive: articulating-paper mark coinciding with a silicone reference contact (genuine occlusal contact).
- False positive: paper mark with no corresponding reference contact (e.g., incidental cusp-tip rub).
- Cusp-tip false positive: false-positive blue mark located on a cusp prominence.
- ICC: intra-class correlation coefficient (reliability/agreement).
- GLM-RM: general linear model with repeated measures.
- Coincidence criterion: counting a contact only when marks appear on BOTH arches at the same site.
