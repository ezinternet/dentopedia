---
title: "Trueness and Precision of Intraoral Scanners for 3D-Printed Orthodontic Models with Attachments: An In Vitro Comparative Study"
authors: Oğuz et al.
year: 2026
date: 2026-01-01
doi: 10.3390/bioengineering13060709
source: oguz-2026-trueness-precision-intraoral-scanners-3d-printed.md
category: [digital-workflow]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "42351953"
pmcid: "PMC13295442"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13295442/
text_path: /Users/oracleneo/llm-wiki/papers/oguz-2026-trueness-precision-intraoral-scanners-3d-printed.txt
text_filename: oguz-2026-trueness-precision-intraoral-scanners-3d-printed.txt
tags: [intraoral-scanner, ios, trueness, precision, in-vitro, 3d-printed-model, clear-aligner, composite-attachment, additive-manufacturing, digital-workflow]
relations:
  - type: extends
    target: schlenz-2022-transfer-accuracy-digital-conventional-full-arch
    note: "extends the appliance-geometry-degrades-scan-fidelity axis from fixed orthodontic appliances (brackets/wire on natural teeth, IOS-vs-alginate) to clear-aligner composite attachments on already-3D-printed models (inter-IOS trueness/precision, no alginate arm)"
---

## Three-line Summary

In vitro comparative study (İnönü University, Bioengineering 2026) evaluating trueness and precision of five intraoral scanners (Primescan, 3Shape TRIOS 3, iTero Element 2 Plus, iTero Element 5D, Rapideye MI-1000) on 30 3D-printed orthodontic models (15 maxillary, 15 mandibular) bearing clear-aligner composite attachments, using a Smart Optics laboratory scanner as reference.

Primescan and TRIOS 3 showed comparable, best-in-class trueness and precision (Kruskal-Wallis trueness χ²=51.094, precision χ²=77.495, both p<0.001); iTero Element 2 Plus and iTero Element 5D were intermediate but clinically acceptable, while Rapideye MI-1000 was significantly worst on both metrics (p<0.01–0.001 vs all others).

The authors argue scanner error should stay near 50 µm for clear aligner workflows (a single stage's programmed tooth movement is ~250 µm, so 50 µm is ~20% of that), and note greater deviation clustered in interproximal/undercut and attachment regions — plus a limitation from using a laboratory scanner rather than an industrial metrology standard as reference.

## 세줄요약

İnönü대학교 in vitro 비교연구(Bioengineering 2026): 클리어 얼라이너(Clear Aligner) 컴포지트 부착물(Composite Attachment)이 있는 3D 프린팅 교정모형 30개(상악 15·하악 15)를 대상으로 5종 구강스캐너(Intraoral Scanner, IOS)(Primescan·3Shape TRIOS 3·iTero Element 2 Plus·iTero Element 5D·Rapideye MI-1000)의 진정도(Trueness)·정밀도(Precision)를 Smart Optics 실험실 스캐너를 기준으로 비교.

Primescan과 TRIOS 3가 진정도·정밀도 모두 최상위로 동등(Kruskal-Wallis 진정도 χ²=51.094, 정밀도 χ²=77.495, 둘 다 p<0.001); iTero Element 2 Plus·iTero Element 5D는 중간이나 임상 허용범위 내, Rapideye MI-1000은 두 지표 모두 유의하게 최하위(다른 모든 기기 대비 p<0.01~0.001).

저자들은 클리어 얼라이너 워크플로에서 스캐너 오차를 약 50µm 이내로 유지해야 한다고 제안(1단계당 계획 치아이동량이 약 250µm이므로 50µm는 그 20%에 해당)하며, 인접면·언더컷·부착물 부위에서 편차가 더 컸다는 점과 기준 장비가 산업용 계측기가 아닌 실험실 스캐너였다는 한계를 지적.

## Summary

This in vitro study (İnönü University, Turkey; ethics approval 2025/7144) evaluated the trueness and precision of five intraoral scanners (IOS) — Primescan, 3Shape TRIOS 3, iTero Element 2 Plus, iTero Element 5D, and Rapideye MI-1000 — on 30 3D-printed single-arch orthodontic models (15 maxillary, 15 mandibular) sourced from real patients undergoing in-house clear-aligner production, each bearing composite attachment geometries. Each model was scanned twice per device and superimposed in CloudCompare against a Smart Optics Vinyl laboratory-scanner reference (reported accuracy ~6 µm) per ISO 5725-1's trueness/precision framework, with RMS deviation as the outcome metric. Non-parametric Kruskal-Wallis testing (normality/homogeneity assumptions were violated) found significant inter-scanner differences for both trueness (χ²=51.094, p<0.001) and precision (χ²=77.495, p<0.001); Dunn's post-hoc with Bonferroni correction placed Primescan and TRIOS 3 as statistically indistinguishable top performers on both metrics, iTero Element 2 Plus and iTero Element 5D as an intermediate, mutually indistinguishable pair, and Rapideye MI-1000 as significantly worst across nearly every pairwise comparison. The authors frame a ~50 µm scanner-error ceiling as clinically meaningful for aligner workflows, since a single treatment stage typically programs only ~250 µm of tooth movement, and note that deviations clustered in interproximal/undercut areas and around the attachments themselves — a geometry-capture challenge specific to aligner-refinement scanning that prior full-arch IOS accuracy literature (typodonts, natural teeth, fixed appliances) has not directly modeled.

## Key Contributions

- First trueness/precision benchmark of 5 current IOS devices specifically on 3D-printed orthodontic models carrying clear-aligner composite attachments (rather than natural teeth, typodonts, or fixed-appliance brackets), directly modeling the digital re-scan step of in-house aligner refinement.
- Primescan and 3Shape TRIOS 3 are statistically indistinguishable top performers on both trueness and precision; Rapideye MI-1000 is significantly the worst performer on both metrics; iTero Element 2 Plus and iTero Element 5D form an intermediate, mutually indistinguishable pair still within a clinically acceptable range.
- Proposes a ~50 µm scanner-accuracy target for clear aligner workflows, reasoned from typical per-stage programmed tooth movement (~250 µm) rather than a generic accuracy cutoff.
- Qualitative/visual observation: Primescan reproduced attachment geometry with the densest mesh detail; embedded numerical markings were most legible on TRIOS 3, Primescan, and iTero Element 5D scans.
- Identifies interproximal and undercut regions (adjacent to attachments) as the specific sites of greatest scan deviation, attributed partly to the laboratory reference scanner's own limited multi-angle access.

## Methodology

In vitro comparative study. n=30 single-arch 3D-printed orthodontic models (15 maxillary, 15 mandibular) digitally planned in Autolign 3D (Diorco Co.) from real in-house aligner patients, each with composite attachment geometries; printed on an Ackuretta SOL LCD printer (eSUN orthodontic resin), post-processed with a standardized 2×5 min isopropyl-alcohol ultrasonic wash + 10 min post-cure. Each model was scanned twice by each of 5 IOS (Primescan, 3Shape TRIOS 3, iTero Element 2 Plus, iTero Element 5D, Rapideye MI-1000) using a fixed scan path (upper-left distal molar → occlusal → palatal → buccal); a Smart Optics Vinyl laboratory scanner served as the reference standard. Datasets were superimposed in CloudCompare (≥4-point initial alignment + fine registration); RMS deviation quantified trueness (vs. reference) and precision (scan-to-scan reproducibility) per ISO 5725-1, visualized with ±0.1 mm color maps/histograms. An a priori power analysis (G*Power, repeated-measures ANOVA, f=0.25, α=0.05, power=90%) called for ≥26 samples; the final analysis instead used non-parametric Kruskal-Wallis (assumptions violated) with Dunn's post-hoc + Bonferroni correction. Test-retest reliability (same operator, re-aligned after 1 month) gave ICC=0.987.

## Results

Absolute mean±SD RMS values (µm) per scanner were reported in the source's own descriptive-statistics table/figures, but that table did not survive the retrieved PMC plain-text extraction — only narrative ranking and pairwise Dunn's-test p-values are recoverable. The comparative structure below is built entirely from those p-values; no numeric RMS figure quoted for Oğuz 2026 itself should be assumed to exist beyond this.

| Scanner | Trueness | Precision | Overall (paper's own conclusion) |
|---|---|---|---|
| Primescan | Best; > Rapideye MI-1000, iTero Element 2 Plus (p<0.01); > iTero Element 5D but NS after Bonferroni (p=0.086) | Best; > Rapideye MI-1000, iTero Element 2 Plus, iTero Element 5D (all p<0.001) | Favorable, top performer |
| 3Shape TRIOS 3 | Comparable to Primescan (p=0.720); > Rapideye MI-1000 (p<0.001); NS vs iTero Element 2 Plus (p=0.663) and iTero Element 5D (p=1.000) | Comparable to Primescan (p=1.000); > Rapideye MI-1000 (p<0.001), iTero Element 2 Plus (p=0.022), iTero Element 5D (p=0.009) | Favorable, top performer |
| iTero Element 5D | Comparable to Primescan (p=0.086, NS) and TRIOS 3 (p=1.000) | Significantly worse than Primescan (p<0.001) and TRIOS 3 (p=0.009); NS vs iTero Element 2 Plus (p=1.000) | Moderate, clinically acceptable |
| iTero Element 2 Plus | Significantly worse than Primescan (p<0.01); NS vs TRIOS 3 (p=0.663) and iTero Element 5D (p=1.000) | Significantly worse than Primescan (p=0.001) and TRIOS 3 (p=0.022); NS vs iTero Element 5D | Moderate, clinically acceptable |
| Rapideye MI-1000 | Worst; significantly lower than all other scanners (p<0.001–p<0.01) | Worst; significantly lower than all other scanners (p<0.01–p<0.001) | Poorest, less suitable for this application |

Overall test statistics: Kruskal-Wallis trueness χ²=51.094 (p<0.001); precision χ²=77.495 (p<0.001) — both null hypotheses (no difference among scanners) rejected. Reference device (Smart Optics Vinyl laboratory scanner) reported accuracy ~6 µm in this study (similar devices reported ~4 µm elsewhere). Test-retest reliability ICC=0.987. Scanner errors within ~50 µm are framed by the authors as generally clinically acceptable for orthodontic diagnosis/treatment planning, versus a typical ~250 µm per-stage aligner tooth movement.

For calibration only (not this study's own measured values, cited by the authors in Discussion from other in vitro comparisons): Diker et al. — trueness/precision (µm) Primescan 25/10, TRIOS 40.5/11, Omnicam 41.5/18, Virtuo Vivo 52/37, iTero 70/12, Emerald 73.5/60; Ender et al. — complete-arch trueness 16.3±2.8–89.8±26.1 µm, precision 10.6±3.8–58.6±38.4 µm across CEREC Omnicam/Primescan/TRIOS 3/iTero Element 2/Medit i500/Planmeca Emerald.

## Related Papers

- [[digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch]] — extends the "appliance geometry degrades scan fidelity" axis from fixed orthodontic appliances (metal/ceramic brackets ± wire on a natural-tooth phantom model, IOS-vs-alginate full-arch transfer accuracy) to clear-aligner composite attachments on an already-3D-printed model (inter-IOS trueness/precision only, no alginate comparator). Schlenz found IOS beats alginate once brackets are present (IOS mean deviation 28–141 µm vs. CAI 103–212 µm) while alginate remains most accurate on unadorned natural teeth (21±20 µm); Oğuz's study cannot speak to that IOS-vs-alginate question at all, but its top performers (Primescan, TRIOS 3) match Schlenz's own strongest IOS devices, and both papers converge on attachment/bracket geometry as a distinct accuracy-limiting factor worth isolating from plain full-arch scanning.
- [[digital-workflow/alkadi-2023-intraoral-scanner-accuracy-factors]] — this narrative review catalogs arch size, tooth presence, operator experience, and powder as IOS accuracy factors but does not address attachment or appliance geometry; Oğuz's interproximal/undercut/attachment-region deviation findings add a factor not covered there.
- [[digital-workflow/buhl-2025-intraoral-scanner-full-arch-accuracy-invitro]] — Buhl's general full-arch IOS trueness benchmark (50–200 µm range, industrial CT reference, no orthodontic appliances) frames the magnitude against which Oğuz's proposed ~50 µm aligner-specific target should be read — it sits at the accurate end of what current-generation IOS devices achieve on plain full-arch scans.
- [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] — this umbrella review of 10 SRs also ranks TRIOS 3 and Primescan at the top of full-arch IOS accuracy across ordinary (non-appliance) scanning conditions; Oğuz's data suggest that ranking largely holds even when the scan target adds clear-aligner attachment geometry.
- [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — Nucera's SR addresses attachment *biomechanics* (which tooth movements — torque, rotation, anchorage — attachments actually improve); Oğuz addresses the upstream *scanning fidelity* question of whether current IOS devices can faithfully capture the attachment geometry that Nucera's biomechanical effects depend on. Different research questions (mechanics vs. digitization); linked here in prose rather than as a typed edge.
