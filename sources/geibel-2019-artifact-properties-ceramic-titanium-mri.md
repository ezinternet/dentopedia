---
title: "Artifact Properties of Dental Ceramic and Titanium Implants in MRI"
authors: Margit-Ann Geibel, Benjamin Gelißen, Anna-Katinka Bracher, Volker Rasche
year: 2019
doi: 10.1055/a-0755-2374
category: [radiology/mri]
pdf_path: /Users/oracleneo/llm-wiki/papers/geibel-2019-artifact-properties-ceramic-titanium-mri.pdf
pdf_filename: geibel-2019-artifact-properties-ceramic-titanium-mri.pdf
source_collection: external
---

## Why Ingested
This is the first MRI-implant-artifact evidence page in the wiki's radiology/mri category, providing the core quantitative datum that ceramic (zirconia) implants are MRI-compatible while titanium implants are not — the reference numbers behind any future claim that ceramic implants can be monitored with MRI. It extends the zirconia-implant evidence base ([[wiki/overviews/zirconia-implant-clinical-outcomes]]) and the titanium-vs-zirconia comparison ([[wiki/implants/surface/shetty-2026-titanium-vs-zirconia-implants-umbrella]]) onto the MR-imaging axis, which neither page covers.

## Three-line Summary
- In-vitro study: 21 dental implants (7 ceramic/zirconia, 14 titanium) embedded in agarose, scanned at 3 T with three isotropic 3D sequences (FFE, TSE/SE, UTE); implant volumes were segmented and compared to manufacturer theoretical volumes (relative error).
- Ceramic implants were artifact-free with mean relative volume errors of 5.4 ± 2.3% (UTE) to 6.5 ± 4.3% (FFE) and no significant difference between sequences; titanium implants produced mean errors of 1314 ± 350% (FFE), 1398 ± 562% (UTE) and 2157 ± 810% (SE), with the implant periphery non-evaluable in every case.
- MRI is a viable radiation-free alternative for imaging ceramic implants (peri-implantitis diagnosis, healing monitoring) but is not suitable for titanium implants; UTE offered no significant artifact improvement over FFE.

## 세줄요약
- 체외 실험: 아가로오스에 매립한 치과용 임플란트 21개(세라믹/지르코니아 7, 티타늄 14)를 3T에서 등방성 3차원 시퀀스 3종(FFE, TSE/SE, UTE)으로 스캔, 분할 부피를 이론적 부피와 비교(상대오차)했다.
- 세라믹 임플란트는 아티팩트 없이 관찰되어 평균 부피 오차가 FFE 6.5±4.3% ~ UTE 5.4±2.3%였고 시퀀스 간 차이가 없는 반면, 티타늄은 FFE 1314±350%, UTE 1398±562%, SE 2157±810%로 전례에서 주변부 평가가 불가능했다.
- MRI는 세라믹 임플란트 평가(치주임플란트주위염 진단·치유 모니터링)에는 방사선 없는 대안이 될 수 있으나 티타늄에는 부적합하며, UTE가 FFE보다 아티팩트 개선에 유의한 이득은 없었다.

## 1. Document Information
- **Journal**: RöFo — Fortschritte auf dem Gebiet der Röntgenstrahlen und der Nuklearmedizin 2019; 191: 433–441
- **DOI**: 10.1055/a-0755-2374
- **Institution**: Department of Oral and Maxillofacial Surgery, Ulm University, Ulm, Germany; Internal Medicine II, Ulm University (no radiologist co-author conflicts — German-language original with English abstract)

## 2. Key Contributions
- Direct quantitative comparison of MRI artifact severity between dental ceramic (zirconia) and titanium implants using volume-error measurement rather than visual artifact scoring.
- Showed titanium implant artifacts were localized (unlike CBCT streak artifacts) but so severe (volume errors >1000%) that implant periphery was never evaluable, across all three sequences.
- Showed ceramic implants were visually artifact-free with only ~5–6.5% volume error, and position/orientation-independent (minimal SD) — establishing MRI as a candidate alternative for ceramic-implant follow-up.
- Demonstrated UTE provided no significant artifact advantage over a standard steady-state gradient echo (FFE) for either material (p = 0.47 for titanium).

## 3. Methodology and Architecture
- **Design**: In-vitro experimental comparison (agarose tissue-mimicking phantom; 3T clinical scanner)
- **Implants**: 21 total, 8 types (Table 1). Ceramic: #1 Ziterion ZI510H (5.0 × 10 mm) + 6× BreDent white sky SKY4512C (4.5 × 12 mm, two lots). Titanium: BreDent bSKY series #2–7 (#3 ×7, #6 ×3). Implants sterilized and embedded in agarose (Serva, 0.5 g/tablet, molecular biology grade).
- **MRI**: Philips Achieva 3 T; implants fixed to a 2×2-channel carotid coil segment in random orientation; three spatially isotropic 3D sequences, 0.5 mm³ voxels: T1-weighted turbo spin echo (SE, TR/TE 419/11 ms, 4 echoes, BW 444.6 Hz, 25 min 8 s), steady-state gradient echo FFE (TR/TE 5.5/2.0 ms, BW 1883.2 Hz, 2 min 38 s), and UTE (TR/TE 12/0.14 ms, 3× oversampled, BW 656.5 Hz, 31 min 41 s).
- **Outcome**: Implant volume segmented semiautomatically (region-growing, ITK-Snap 2.2.0, manual seeds); relative error vs manufacturer theoretical volume; two-sided paired Student's t-test, significance at p < 0.05.

## 4. Key Results and Benchmarks
- **Ceramic (n = 7)**: mean relative volume error FFE 6.5 ± 4.3%, SE 6.4 ± 2%, UTE 5.4 ± 2.3% (abstract; discussion reports UTE 5.3 ± 2.3%). No significant difference between sequences. Implant–agarose transition artifact-free in all cases; periphery fully evaluable, limited only by 0.5 mm³ spatial resolution.
- **Titanium (n = 14)**: mean relative volume error FFE 1314 ± 350%, SE 2157 ± 810%, UTE 1398 ± 562%. Significant: FFE vs SE p < 0.001; UTE vs SE p < 0.01; FFE vs UTE p = 0.47 (ns). Periphery never evaluable; artifacts localized to immediate implant vicinity; strong orientation dependence (e.g., #6C SE error 3513.4%, #6A 1607.3%).
- **Measured vs theoretical volume**: titanium significant for all sequences (p < 0.001); ceramic significant for FFE (p < 0.05) and SE (p < 0.05) but not UTE (p = 0.06).
- **Mean error for replicate implant series (Table 7)**: #3 titanium FFE 1265 ± 855%, SE 2183 ± 1817%, UTE 1487 ± 867%; #6 titanium FFE 1825 ± 108%, SE 2853 ± 1080%, UTE 1750 ± 867%; #8 ceramic FFE 5.6 ± 3.8%, SE 6.0 ± 1.7%, UTE 5.1 ± 2.4%. Greatest titanium variability in SE, least in FFE.

## 5. Limitations and Future Work
- Implant position/orientation relative to the static B0 field was not systematically varied (orientation dependence inferred only from result variability).
- Volume-based evaluation did not quantify spatial distortion — a distorted implant of identical volume would escape detection (not observed visually, but not excluded).
- Sequences used (especially SE and UTE) are not routine clinical sequences; no parallel imaging/undersampling, and up to ~31 min scan times are clinically impractical.
- In-vitro agarose environment does not capture in-vivo bone/tissue susceptibility behavior.

## 6. Related Work
- Duttenhoefer et al. 2014 (Clin Oral Implants Res): MRI vs OPG/CBCT/CT accuracy for titanium and zirconia implants in vitro — imaging quality equal preoperatively; significant titanium distortion postoperatively, not for ceramic.
- Matsuura et al. 2002 (J Neurosurg): quantified susceptibility artifacts of ceramics, pure titanium and titanium alloys on high-field MRI — all ceramics produced far smaller artifacts than metals; ceramic judged the best artifact-reducing biomaterial.
- Hilgenfeld et al. 2016 (Eur J Oral Implantol): implant-supported single crowns — crown material composition dramatically affects artifact volume in dental MRI.
- [[wiki/overviews/zirconia-implant-clinical-outcomes]] and [[wiki/implants/surface/shetty-2026-titanium-vs-zirconia-implants-umbrella]] — zirconia implant clinical outcomes: this paper adds the MR-imaging axis to the zirconia-vs-titanium comparison.

## 7. Glossary
- **FFE (Fast Field Echo)**: steady-state 3D gradient-echo sequence (TR/TE 5.5/2.0 ms); the standard clinical GE alternative here.
- **UTE (Ultra-short Echo Time)**: sequence with extremely short TE (~0.14 ms) intended to capture short-T2 signal and reduce metal-induced signal cancellation.
- **Relative volume error**: (segmented MR volume − theoretical implant volume) / theoretical × 100%.
- **Susceptibility artifact**: signal loss/distortion from magnetic field inhomogeneity caused by the material's magnetic-susceptibility mismatch with tissue.
- **TSE (Turbo Spin Echo / SE)**: multi-echo T1-weighted spin-echo sequence (TR/TE 419/11 ms, 4 echoes); low receive bandwidth (444.6 Hz) worsens metal artifacts.
- **Agarose phantom**: tissue-mimicking embedding gel (Serva tablets, molecular biology grade) used to suspend the implants during scanning.