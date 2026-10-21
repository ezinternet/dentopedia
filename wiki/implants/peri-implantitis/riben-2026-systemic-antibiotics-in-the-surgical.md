---
title: "Systemic Antibiotics in the Surgical Treatment of Peri-Implantitis: Impact on the Salivary Microbiome"
authors: Riben Grundström C, Lund B, Bostanci N, Silbereisen A, Pennhag A, Koistinen IS, Zha Y, Damdimopoulos A, Belibasakis GN, Hultin M
year: 2026
date: 2026-05-25
doi: 10.1111/jcpe.70143
source: riben-2026-systemic-antibiotics-in-the-surgical.md
category: [implants/peri-implantitis]
evidence_level: rct
source_collection: pubmed-text
full_text: true
pmid: "42184963"
pmcid: "PMC13371835"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13371835/
text_path: /Users/oracleneo/llm-wiki/papers/riben-2026-systemic-antibiotics-in-the-surgical.txt
text_filename: riben-2026-systemic-antibiotics-in-the-surgical.txt
tags: [peri-implantitis, systemic-antibiotics, salivary-microbiome, whole-genome-sequencing, amoxicillin, metronidazole, penicillin-V, antimicrobial-stewardship, alpha-diversity, resective-surgery]
relations:
  - type: extends
    target: antonoglou-2025-do-systemic-antibiotics-offer-benefits
---

## Three-line Summary
Exploratory, blinded, single-centre two-arm analysis (a randomised subset of the NCT02185209 RCT) of 27 patients receiving resective surgery for peri-implantitis plus 7 days of systemic amoxicillin + metronidazole (group A, n = 14) or phenoxymethylpenicillin + metronidazole (group B, n = 13); unstimulated saliva at baseline, 8 d, 14 d, 6 mo and 12 mo analysed by whole genome shotgun sequencing.
Species richness fell significantly at Day 8 versus baseline in both groups, with recovery signs by Day 14 and recovery by 6 months; alpha and beta diversity did not differ between regimens at any timepoint (richness ANOVA q intervention = 0.762), although species-level differences existed (78 species lower and 38 higher in A vs B at Day 8); 12-month treatment success was 83% (A) vs 69% (B), p = 0.645.
The narrow-spectrum penicillin V regimen did not disturb the salivary microbiome less in a measurable community-level way, so the data give no microbiological or clinical basis to prefer one regimen; limitations are small n, no placebo arm and concurrent chlorhexidine rinsing.

## 세줄요약
임플란트주위염 외과수술(resective surgery) + 7일 전신 항생제를 받은 27명(A군 amoxicillin+metronidazole 14명, B군 phenoxymethylpenicillin+metronidazole 13명)의 탐색적·눈가림 단일기관 2군 하위분석(NCT02185209 RCT의 무작위 하위집단); 침을 수술 전·8일·14일·6개월·12개월에 채취해 전장 유전체 시퀀싱 (Whole Genome Shotgun Sequencing, WGS) 분석.
두 군 모두 8일째 종 풍부도(richness)가 기저 대비 유의하게 감소하고 14일째 회복 조짐, 6개월째 회복; 알파·베타 다양성은 어느 시점에서도 군 간 차이 없음(richness ANOVA q intervention = 0.762), 다만 종 수준 차이는 존재(8일째 A군이 B군보다 78종 낮고 38종 높음); 12개월 치료 성공률 A 83% vs B 69%, p = 0.645.
협범위 penicillin V 레짐이 군집 수준에서 침 미생물총 교란을 더 줄인다는 근거는 없어 어느 쪽을 선호할 미생물학적·임상적 근거가 없으며, 한계는 소규모 n·위약군 부재·병용 클로르헥시딘 가글.

## Summary
This exploratory microbiome analysis nested in a placebo-controlled Swedish RCT followed 27 surgically treated peri-implantitis patients who received either amoxicillin or phenoxymethylpenicillin, each combined with metronidazole for 7 days. Salivary species richness dropped at Day 8 in both groups and recovered by 6 months, and no alpha- or beta-diversity difference between regimens was detected over 12 months. Species-level abundance differed between groups at several timepoints, but the authors attribute part of this to small sample size and individual variation. Treatment success at 12 months did not differ (83% vs 69%, p = 0.645). The paper offers no regimen recommendation; it only suggests that narrow-spectrum agents may merit consideration on stewardship grounds.

## Key Contributions
- First WGS-based comparison (per the authors) of amoxicillin + metronidazole versus phenoxymethylpenicillin + metronidazole effects on the salivary microbiome after peri-implant surgery.
- Documents an ecological cost of the adjunctive antibiotic course (richness loss at Day 8 with recovery by 6 months) that is comparable between a broad- and a narrow-spectrum penicillin partner.
- Complements the clinical-benefit evidence on adjunctive systemic antibiotics with microbiome-disturbance data.

## Methodology
Blinded, single-centre, two-armed exploratory study (Uppsala, Sweden) nested in a three-armed placebo-controlled RCT of 84 patients; the 27-patient subset came from the two antibiotic arms (40 implants). Group A: amoxicillin 500 mg + metronidazole 400 mg three times daily; group B: phenoxymethylpenicillin 800 mg x 2 + metronidazole 400 mg three times daily; 7 days each. Surgery was resective with titanium-curette/ultrasonic decontamination plus 3% hydrogen peroxide and saline, followed by 0.12% chlorhexidine (CHX) rinses twice daily for 14 days. Unstimulated saliva was self-collected at baseline, 8 d, 14 d, 6 mo and 12 mo (126 samples; 23 patients complete). Shotgun sequencing (DNBSEQ G400, 150 bp paired-end), MetaPhlAn4 profiling, mixed models for diversity, PERMANOVA for beta diversity and edgeR with FDR q < 0.05 for differential species. Secondary outcome: 12-month treatment success (PPD <= 5 mm, BOP at <= 1 site, no SOP, no additional bone loss > 0.5).

## Results
| Outcome | Result |
|---|---|
| Sequencing yield | mean 35.7 million (+/- 8.2 million) counts; 498 species, 194 genera, 16 phyla |
| Richness vs baseline | significantly reduced at Day 8 in both groups; richness increased by Day 14 (A q < 0.05; B q > 0.05); recovery evident at 6 months |
| Richness ANOVA | q time = 0.00002; q time-intervention = 0.557; q intervention = 0.762 |
| Beta diversity (PERMANOVA) | changed over time (q = 0.00004), not between interventions |
| Within-group differential species | 21 species in A, 37 in B, 11 shared |
| Between-group, Day 8 | 78 species lower and 38 higher in A vs B |
| Between-group, Day 14 | 80 species higher and 50 lower in A vs B |
| Species differing at >= 3 timepoints | 7 (e.g. Alloprevotella tannerae lower in A throughout; Neisseria sicca higher in A up to 6 months) |
| 12-month treatment success | A 10 (83%) vs B 9 (69%); total 19 (76%) of 25; p = 0.645 |
| Baseline imbalance | current smokers A 7 (50.0%) vs B 2 (15.4%), p = 0.057; modified-surface implants A 18 vs B 10, p = 0.023 for surface distribution |

## Related Papers
- [[implants/peri-implantitis/antonoglou-2025-do-systemic-antibiotics-offer-benefits]] — SR+MA that included this trial's parent RCT (Riben Grundström 2024) for clinical benefit; this paper adds the microbiome-disturbance side
- [[implants/peri-implantitis/herrera-2023-prevention-treatment-peri-implant-efp]] — EFP S3 guideline whose non-recommendation of systemic antibiotics cites microbiome dysbiosis and resistance concerns
- [[implants/peri-implantitis/ramanauskaite-2026-factors-influencing-effectiveness-surgical-therapy]] — surgical-therapy factors review that left the adjunctive-antibiotic benefit unresolved
- [[implants/peri-implantitis/zhou-2026-surgical-protocols-peri-implantitis-cohort]] — retrospective cohort with a confounded antibiotic association
- [[implants/peri-implantitis/smeets-2014-peri-implantitis-definition-etiology-review]] — biofilm-dysbiosis etiology background
- [[implants/peri-implantitis/kotsakis-2025-microbial-dysbiosis-titanium-release-peri-implantitis]] — dysbiosis framing in peri-implantitis, with a non-microbial (titanium particle) co-driver
