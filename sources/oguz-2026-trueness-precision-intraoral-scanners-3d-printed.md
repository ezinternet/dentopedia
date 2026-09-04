---
title: "Trueness and Precision of Intraoral Scanners for 3D-Printed Orthodontic Models with Attachments: An In Vitro Comparative Study"
authors: Oğuz et al.
year: 2026
doi: 10.3390/bioengineering13060709
category: [digital-workflow]
source_collection: pubmed-text
full_text: true
pmid: "42351953"
pmcid: "PMC13295442"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13295442/
text_path: /Users/oracleneo/llm-wiki/papers/oguz-2026-trueness-precision-intraoral-scanners-3d-printed.txt
text_filename: oguz-2026-trueness-precision-intraoral-scanners-3d-printed.txt
---

## Why Ingested

[[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]] showed that fixed orthodontic appliances (brackets ± wire) flip the intraoral-scanner-vs-alginate accuracy ranking on full-arch impressions. This paper asks the adjacent question for a different appliance type and a different workflow step: once a model has already been 3D-printed with clear-aligner composite attachments, which intraoral scanner (IOS) reproduces that attachment geometry most faithfully — informing the digital re-scan step of in-house aligner refinement rather than the initial impression-vs-scan choice.

## Three-line Summary

In vitro comparative study (İnönü University, Bioengineering 2026) evaluating trueness and precision of five intraoral scanners (Primescan, 3Shape TRIOS 3, iTero Element 2 Plus, iTero Element 5D, Rapideye MI-1000) on 30 3D-printed orthodontic models (15 maxillary, 15 mandibular) bearing clear-aligner composite attachments, using a Smart Optics laboratory scanner as reference.

Primescan and TRIOS 3 showed comparable, best-in-class trueness and precision (Kruskal-Wallis trueness χ²=51.094, precision χ²=77.495, both p<0.001); iTero Element 2 Plus and iTero Element 5D were intermediate but clinically acceptable, while Rapideye MI-1000 was significantly worst on both metrics (p<0.01–0.001 vs all others).

The authors argue scanner error should stay near 50 µm for clear aligner workflows (a single stage's programmed tooth movement is ~250 µm, so 50 µm is ~20% of that), and note greater deviation clustered in interproximal/undercut and attachment regions — plus a limitation from using a laboratory scanner rather than an industrial metrology standard as reference.

## 세줄요약

İnönü대학교 in vitro 비교연구(Bioengineering 2026): 클리어 얼라이너(Clear Aligner) 컴포지트 부착물(Composite Attachment)이 있는 3D 프린팅 교정모형 30개(상악 15·하악 15)를 대상으로 5종 구강스캐너(Intraoral Scanner, IOS)(Primescan·3Shape TRIOS 3·iTero Element 2 Plus·iTero Element 5D·Rapideye MI-1000)의 진정도(Trueness)·정밀도(Precision)를 Smart Optics 실험실 스캐너를 기준으로 비교.

Primescan과 TRIOS 3가 진정도·정밀도 모두 최상위로 동등(Kruskal-Wallis 진정도 χ²=51.094, 정밀도 χ²=77.495, 둘 다 p<0.001); iTero Element 2 Plus·iTero Element 5D는 중간이나 임상 허용범위 내, Rapideye MI-1000은 두 지표 모두 유의하게 최하위(다른 모든 기기 대비 p<0.01~0.001).

저자들은 클리어 얼라이너 워크플로에서 스캐너 오차를 약 50µm 이내로 유지해야 한다고 제안(1단계당 계획 치아이동량이 약 250µm이므로 50µm는 그 20%에 해당)하며, 인접면·언더컷·부착물 부위에서 편차가 더 컸다는 점과 기준 장비가 산업용 계측기가 아닌 실험실 스캐너였다는 한계를 지적.

## 1. Document Information
- **Journal**: Bioengineering (Basel) 2026;13(6):709
- **DOI**: 10.3390/bioengineering13060709
- **Institution**: İnönü University, Malatya, Turkey (Non-Interventional Clinical Research Ethics Committee approval 2025/7144)

## 2. Key Contributions
- First trueness/precision benchmark of 5 current IOS devices specifically on 3D-printed orthodontic models carrying clear-aligner composite attachments, rather than natural teeth, typodonts, or fixed-appliance brackets.
- Primescan and 3Shape TRIOS 3 are statistically indistinguishable top performers on both trueness and precision; Rapideye MI-1000 is significantly worst on both; iTero Element 2 Plus and iTero Element 5D form an intermediate, mutually indistinguishable pair still within a clinically acceptable range.
- Proposes a ~50 µm scanner-accuracy target for clear aligner workflows, reasoned from typical per-stage programmed tooth movement (~250 µm) rather than a generic accuracy cutoff.

## 3. Methodology and Architecture
- **Design**: In vitro comparative study, non-parametric (Kruskal-Wallis + Dunn's post-hoc with Bonferroni correction)
- **n**: 30 single-arch 3D-printed orthodontic models (15 maxillary, 15 mandibular), each scanned twice by each of 5 IOS devices
- **Reference**: Smart Optics Vinyl laboratory scanner (reported accuracy ~6 µm in this study)
- **Outcomes**: RMS deviation (mm) for trueness (vs. reference) and precision (scan-to-scan reproducibility), per ISO 5725-1

## 4. Key Results and Benchmarks
- Kruskal-Wallis: trueness χ²=51.094, p<0.001; precision χ²=77.495, p<0.001 — both null hypotheses rejected.
- Trueness: Primescan best (vs Rapideye MI-1000 and iTero Element 2 Plus, p<0.01; vs iTero Element 5D p=0.086, NS after Bonferroni). TRIOS 3 > Rapideye MI-1000 (p<0.001); TRIOS 3 vs iTero Element 2 Plus (p=0.663), vs iTero Element 5D (p=1.000), vs Primescan (p=0.720) all NS. iTero Element 2 Plus vs iTero Element 5D NS (p=1.000). Primescan, TRIOS 3, iTero Element 5D judged comparable; Rapideye MI-1000 lowest.
- Precision: Primescan > Rapideye MI-1000, iTero Element 2 Plus, iTero Element 5D (all p<0.001). TRIOS 3 > Rapideye MI-1000 (p<0.001), iTero Element 2 Plus (p=0.022), iTero Element 5D (p=0.009). Primescan vs TRIOS 3 NS (p=1.000). iTero Element 2 Plus vs iTero Element 5D NS (p=1.000). Rapideye MI-1000 worst, differs significantly from all others (p<0.01).
- Test-retest reliability: ICC=0.987 (same operator, re-aligned after 1 month).
- Absolute mean±SD RMS values (µm) per scanner were reported in the source's own descriptive-statistics table/figures, but that table was not recoverable from the retrieved PMC plain-text extraction (only narrative ranking and pairwise p-values survived). For calibration, the Discussion cites (not this study's own data): Diker et al. — trueness/precision (µm) Primescan 25/10, TRIOS 40.5/11, Omnicam 41.5/18, Virtuo Vivo 52/37, iTero 70/12, Emerald 73.5/60; Ender et al. — complete-arch trueness 16.3±2.8–89.8±26.1 µm, precision 10.6±3.8–58.6±38.4 µm across CEREC Omnicam/Primescan/TRIOS 3/iTero Element 2/Medit i500/Planmeca Emerald.

## 5. Limitations and Future Work
- Reference device was a dental laboratory scanner (Smart Optics Vinyl, ~6 µm reported accuracy), not an industrial metrology/coordinate-measuring system regarded as a true gold standard.
- RMS was the only deviation metric used; Hausdorff distance and mean absolute difference were not computed.
- In vitro only — no saliva, soft tissue, patient movement, or limited intraoral access; single operator (no inter-operator variability assessed); single institution's models; no subgroup analysis by attachment size/shape/location; scanning duration not recorded; downstream 3D-printing/thermoforming/clinical outcomes not assessed.

## 6. Related Work
- [[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]]: fixed-appliance (bracket/wire) analog of the appliance-geometry-vs-scan-accuracy question, but comparing IOS to alginate rather than IOS-to-IOS.
- [[digital-workflow/alkadi-2023-intraoral-scanner-accuracy-factors]]: narrative review of IOS accuracy factors (arch size, tooth presence, operator, powder) that does not address attachment geometry as a factor.
- [[digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]]: general full-arch IOS trueness benchmark (50–200 µm, industrial CT reference) framing the magnitude of the ~50 µm target proposed here.
- [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]]: umbrella review also ranking TRIOS 3 and Primescan at the top of full-arch IOS accuracy.
- [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]]: covers attachment *biomechanics* (which tooth movements attachments improve); this paper covers the upstream *scanning fidelity* of those same attachment geometries.

## 7. Glossary
- **Trueness**: closeness of a scanned measurement to the true dimensions of the object (ISO 5725-1); here, deviation from the Smart Optics reference scan.
- **Precision**: consistency/reproducibility of repeated measurements of the same object (ISO 5725-1); here, RMS deviation between repeat scans of the same model.
- **RMS (Root Mean Square)**: aggregate deviation metric combining x/y/z coordinate differences between corresponding points on test and reference scans, expressed in mm.
- **Composite attachment**: a small resin bump bonded to a tooth surface to give a clear aligner additional mechanical purchase for a specific tooth movement.
