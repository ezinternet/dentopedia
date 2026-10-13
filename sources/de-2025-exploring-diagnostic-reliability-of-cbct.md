---
title: "Exploring Diagnostic Reliability of CBCT for Vertical Root Fractures: A Systematic Review and Meta-Analytical Approach"
authors: de Lima Dias-Junior LC, de Souza DL, Bezerra AP, Correa M, da Silveira Teixeira C, Bortoluzzi EA, da Fonseca Roberti Garcia L
year: 2025
doi: 10.1155/ijod/8824867
category: [cracked-tooth]
source_collection: pubmed-text
full_text: true
pmid: "40726824"
pmcid: "PMC12303641"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12303641/
text_path: /Users/oracleneo/llm-wiki/papers/de-2025-exploring-diagnostic-reliability-of-cbct.txt
text_filename: de-2025-exploring-diagnostic-reliability-of-cbct.txt
---

## Why Ingested

The cracked-tooth category holds narrative reviews and a consensus statement that say CBCT is limited for detecting the VRF line itself ([[wiki/cracked-tooth/patel-2022-present-status-future-directions-vertical]], [[wiki/cracked-tooth/liao-2021-vertical-root-fracture-non-endodontically-treated]], [[wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures]]) but no pooled quantitative estimate. This 100-study diagnostic-accuracy SR+MA supplies the numbers (fracture pattern, metal post, voxel size) behind those qualitative statements and complements the indirect bone-pattern approach of [[wiki/cracked-tooth/alaugaily-2022-cbct-patterns-bone-loss-clinical]]; it also gives the endodontic FOV/voxel guidance in [[wiki/overviews/cbct-diagnostic-performance-overview]] a VRF-specific evidence base.

## Three-line Summary

Systematic review and diagnostic-accuracy meta-analysis (PROSPERO CRD42020207094; PRISMA-DTA, QUADAS-2, GRADE) of 100 in vitro studies (5808 extracted human teeth; 46 low/moderate risk-of-bias studies entered the pooled analyses, 54 high-risk studies excluded) on factors affecting CBCT detection of laboratory-induced vertical root fractures (VRF).

Complete VRFs were detected with higher sensitivity than incomplete VRFs (summary sensitivity, SSe 0.749 vs 0.522; specificity not different, 0.842 vs 0.786); metal posts lowered both sensitivity and specificity versus empty canals (SSe 0.560 vs 0.763; SSp 0.719 vs 0.841), and in metal-post teeth a voxel size of 0.16 mm or smaller raised sensitivity (SSe 0.632 vs 0.482) without changing specificity.

All pooled comparisons carried very-low GRADE certainty (in vitro indirectness plus high heterogeneity, I2 about 55-90%), so the numbers are best-case laboratory estimates: CBCT is least reliable for incomplete fractures and metal-post teeth, where artifacts can mimic fracture lines, and a result there should be confirmed (e.g., by direct visualization at surgery).

## 세줄요약

체계적 문헌고찰 및 진단정확도 메타분석 (PROSPERO CRD42020207094; PRISMA-DTA, QUADAS-2, GRADE) - 체외 연구 100편 (추출 인간 치아 5808개; 편향위험 낮음/중간 46편만 합성, 높음 54편 제외)을 대상으로 실험적으로 유발한 수직치근파절 (Vertical Root Fracture, VRF)의 콘빔 CT (Cone-Beam CT, CBCT) 검출 정확도에 영향을 주는 인자를 분석.

완전 VRF가 불완전 VRF보다 민감도가 높았고 (종합 민감도 Summary Sensitivity, SSe 0.749 vs 0.522; 특이도는 차이 없음 0.842 vs 0.786), 금속 포스트는 빈 근관 대비 민감도·특이도를 모두 낮췄으며 (SSe 0.560 vs 0.763; 종합 특이도 Summary Specificity, SSp 0.719 vs 0.841), 금속 포스트 치아에서 복셀 0.16 mm 이하는 특이도 변화 없이 민감도를 높임 (SSe 0.632 vs 0.482).

모든 합성 결과의 근거 확실성은 GRADE 매우 낮음 (체외 연구의 간접성 + 높은 이질성, I2 약 55-90%)이므로 수치는 실험실 최선 추정치다: 불완전 파절과 금속 포스트 치아에서 CBCT 신뢰도가 가장 낮고 아티팩트가 파절선을 모방할 수 있어, 이 경우 결과는 수술적 직접 확인 등으로 교차 확인해야 한다.

## 1. Document Information

- **Journal**: International Journal of Dentistry 2025;2025:8824867 (published 2025-07-21)
- **DOI**: 10.1155/ijod/8824867
- **Institution**: Federal University of Santa Catarina (UFSC), Florianopolis, Brazil; University of Louisville, USA

## 2. Key Contributions

- First diagnostic-accuracy meta-analysis dedicated to in vitro CBCT detection of VRF, pooling only low/moderate risk-of-bias studies and reporting GRADE certainty per factor.
- Quantifies three drivers of CBCT accuracy: fracture pattern (complete vs incomplete), intracanal material (none, gutta-percha, metal post, fiberglass post) and voxel size.
- Concludes that image enhancement filters and metal artifact reduction (MAR) algorithms do not reliably improve VRF diagnosis (qualitative synthesis; no pooled estimate possible).
- Qualitative synthesis only: small field of view (FOV) and central tooth position within the FOV improve accuracy; tube current/voltage and CBCT device give inconsistent results.

## 3. Methodology and Architecture

- **Design**: SR + bivariate random-effects diagnostic accuracy meta-analysis with meta-regression (glmer, lme4/R 4.1.3); PROSPERO CRD42020207094; PRISMA-DTA (adapted for in vitro); QUADAS-2 (adapted); GRADE per factor.
- **Databases**: PubMed, Embase, Scopus, Web of Science, Lilacs to 12 May 2025, plus ProQuest, LIVIVO, Google Scholar, reference lists, experts; no date/language limits.
- **n**: 4505 records, 2695 screened after de-duplication, 97 + 3 (gray literature/reference lists) = 100 studies; 5808 teeth; publication years 2009-2025. Risk of bias: 24 low, 22 moderate, 54 high; only low/moderate studies were meta-analysed.
- **Index test / reference**: CBCT scans vs visual inspection (with or without magnification, transillumination, stains) or micro-CT of extracted human teeth with laboratory-induced fractures (hammer-and-pin/chisel, universal testing machine, etc.).
- **Outcomes**: summary sensitivity (SSe) and specificity (SSp) with 95% CI; likelihood-ratio tests between covariate models; I2 heterogeneity.

## 4. Key Results and Benchmarks

| Comparison | Result |
|---|---|
| Complete vs incomplete VRF (all teeth) | SSe 0.749 (0.675-0.811) vs 0.522 (0.424-0.618), p=0.0003; SSp 0.842 vs 0.786, p=0.219 (4863 images, I2 79-86%) |
| Complete vs incomplete, empty canals | SSe 0.867 (0.721-0.942) vs 0.585 (0.367-0.775); SSp 0.906 vs 0.869 (ns) |
| Complete vs incomplete, root-filled canals / metal posts | No significant difference (SSe 0.695 vs 0.561, p=0.066; metal posts 0.588 vs 0.444, p=0.062) |
| Empty canal vs gutta-percha (all fractures) | SSe 0.726 vs 0.688, p=0.615; SSp 0.870 vs 0.789, p=0.082 (ns); for complete VRF SSe 0.862 vs 0.710, p=0.035 |
| Empty canal vs metal post | SSe 0.763 vs 0.560 (p=0.0046); SSp 0.841 vs 0.719 (p=0.0058); also significant within complete VRF (SSe 0.867 vs 0.558) and incomplete VRF (SSe 0.655 vs 0.439) |
| Empty canal vs fiberglass post | No difference (SSe 0.786 vs 0.773; SSp 0.841 vs 0.855; p=0.77) |
| Voxel size, empty or gutta-percha canals | No difference at thresholds 0.2, 0.16, 0.125 or 0.1 mm |
| Voxel size, metal posts | 0.2 mm threshold ns; 0.16 mm: SSe 0.632 vs 0.482 (p=0.011); 0.125 mm: 0.665 vs 0.502 (p=0.008); 0.1 mm: 0.654 vs 0.517 (p=0.025); SSp unchanged |
| Filters / MAR | Sharpness filters: no benefit (5 studies); artifact-reduction filters: device-dependent; MAR: 7 studies no difference, 5 improvement, 4 worse |
| FOV / position | Small FOV better in all 5 studies; central position better in all 3 studies |
| Metallic objects in FOV | 5 of 7 studies: reduced accuracy (zirconia implants lowered specificity); 2 no effect |
| GRADE | Very low certainty for fracture pattern, voxel size and intracanal material |

## 5. Limitations and Future Work

- Only in vitro (ex vivo) studies: no soft-tissue attenuation, motion or patient factors, so image quality is better than clinical and accuracy is likely overestimated (authors state this explicitly).
- High heterogeneity (I2 roughly 55-90%) and GRADE very low certainty for all pooled comparisons; 54 of 100 studies were high risk of bias and excluded from pooling.
- Image filters, MAR, device, FOV, position, tube current/voltage could not be meta-analysed (few studies, heterogeneous designs).
- Accuracy is for detecting the fracture line only, not the secondary bone-loss signs (J-shaped lesion) that make up much of clinical CBCT diagnosis.
- Authors note publication bias cannot be fully excluded; in vivo validation is needed.

## 6. Related Work

- [[wiki/cracked-tooth/patel-2022-present-status-future-directions-vertical]]: narrative review stating CBCT does not reliably show the fracture line in root-filled teeth; this SR quantifies the limits.
- [[wiki/cracked-tooth/liao-2021-vertical-root-fracture-non-endodontically-treated]]: narrative review noting CBCT is limited by intracanal metal and radiopaque fillings; this SR gives pooled numbers.
- [[wiki/cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures]]: ESE statement recommending selective CBCT.
- [[wiki/cracked-tooth/alaugaily-2022-cbct-patterns-bone-loss-clinical]]: CBCT bone-loss pattern (indirect) approach in vivo.
- [[wiki/overviews/cbct-diagnostic-performance-overview]]: endodontic FOV/voxel guidance.

## 7. Glossary

- **VRF (vertical root fracture)**: longitudinal fracture of the root, complete (through both walls) or incomplete.
- **SSe / SSp**: summary sensitivity / specificity from the bivariate random-effects model.
- **MAR (metal artifact reduction)**: CBCT reconstruction algorithm that corrects metal-induced streaking.
- **Beam hardening / partial volume effect**: artifact mechanisms from dense materials (metal posts) that can obscure or mimic fracture lines.
- **QUADAS-2 / GRADE**: risk-of-bias tool for diagnostic accuracy studies / certainty-of-evidence framework.
