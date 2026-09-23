---
title: "Macrophages modulate mesenchymal stem cell function via tumor necrosis factor alpha in tooth extraction model"
authors: "Mun AY et al."
year: 2024
date: 2024-07-04
doi: 10.1093/jbmrpl/ziae085
source: mun-2024-macrophage-msc-tnf-tooth-extraction.md
category: [bone-regeneration/ridge-preservation]
evidence_level: animal
source_collection: pubmed-text
tags: [macrophage, MSC, TNF-alpha, extraction-socket, bone-healing, inflammation, immunology, RNA-seq, clodronate, osteogenic-differentiation]
relations:
  - type: extends
    target: fok-2024-alveolar-socket-healing-evolving-knowledge
---

## Three-line Summary

Mouse maxillary first molar extraction model (n=4/group) with macrophage depletion by clodronate liposomes, supplemented by in vitro RNA-seq of TNF-α-stimulated bone marrow MSCs (n=3).

Macrophage depletion significantly reduced bone volume at day 7 (0.01 mm³ vs 0.02 mm³, p<.0001) and new bone area (41.97% vs 54.03%, p<.0001); M1-derived TNF-α positively correlated with MSC (PDGFRα+) recruitment, and RNA-seq identified 15 candidate immune-regulatory genes highly upregulated in TNF-α-stimulated MSCs.

Knockdown of Clec4e, Gbp6, and Cxcl10 enhanced osteogenic differentiation of MSCs in vitro, suggesting these genes negatively regulate osteoblast commitment and may represent molecular targets for promoting extraction socket bone regeneration.

## 세줄요약

쥐 상악 제1대구치 발치 모델 (n=4/군): 클로드로네이트 리포솜으로 대식세포를 고갈하고, 체외에서 TNF-α 자극 골수 MSC의 RNA-seq(n=3) 병행.

대식세포 고갈 시 7일째 골부피(0.01 vs 0.02 mm³, p<.0001) 및 신생골 면적(41.97% vs 54.03%, p<.0001) 유의 감소; M1 기원 TNF-α와 MSC 집적이 양의 상관관계; RNA-seq에서 TNF-α 자극 MSC의 15개 면역조절 후보 유전자 동정.

Clec4e·Gbp6·Cxcl10 siRNA 녹다운 시 MSC 조골세포 분화 증가 → 이들 유전자가 골아세포 분화를 음성 조절하며 골재생 치료 표적이 될 수 있음.

## Summary

This study used a mouse maxillary first molar tooth extraction (TES) model to investigate how M1 macrophages regulate 간엽줄기세포 (Mesenchymal Stem Cell, MSC) recruitment and function through 종양괴사인자-α (Tumor Necrosis Factor-alpha, TNF-α) during jawbone healing. Macrophage depletion was achieved by intraperitoneal injection of clodronate liposomes (12.5 mg/kg) in 5-week-old C57BL/6J mice one day prior to bilateral maxillary first molar extraction. Animals were sacrificed at days 1, 3, 5, 7, and 10 (n=4/group) and evaluated by micro-CT, H&E, Masson's trichrome, TRAP staining, and immunofluorescence for CD80+ M1, CD206+ M2, PDGFRα+ MSC, TNF-α, and RUNX2.

Macrophage depletion transiently reduced M1, M2, MSC, and TNF-α cell counts in the healing socket during days 1–5, followed by a rebound on day 7 where the clodronate group exceeded control for CD80+ M1 cells (493.3 vs 396.0, p=.0004) and PDGFRα+ MSCs (593 vs 473, p=.0010). Despite this compensatory rebound, the cumulative effect of early macrophage depletion produced significantly lower bone regeneration: at day 7, bone volume was 0.01 mm³ vs 0.02 mm³ (p<.0001) and new bone area was 41.97% vs 54.03% (p<.0001) in the clodronate group.

To elucidate the downstream molecular effects of TNF-α on MSCs, bone marrow-derived MSCs were stimulated with 10 ng/mL TNF-α for 24 hours and subjected to bulk RNA-sequencing (Illumina NovaSeq 6000, n=3). DESeq2 identified 59 genes with |log2FC|>5 (FDR<0.05), of which 56 were upregulated and 3 downregulated. Functional enrichment analysis (DAVID) and expression filtering (log2TPM>5) yielded 15 candidate genes predominantly involved in immune regulation: Mmp3, Gbp6, Cxcl10, Clec4e, Ccl20, Nos2, and others. In vivo immunofluorescence confirmed that Clec4e and Gbp6 proteins peak during the inflammatory stage (day 3) and decline as bone formation proceeds (day 5). siRNA knockdown of Clec4e, Gbp6, and Cxcl10 individually in MSCs followed by one week of osteogenic induction significantly increased Runx2 and Alp expression (all p<.0001), indicating these genes negatively regulate osteoblast differentiation and are important for maintaining MSC immunomodulatory stemness.

## Key Contributions

- Provides in vivo evidence that M1 macrophage-derived TNF-α is a critical upstream signal for MSC recruitment and activation in the tooth extraction socket
- Establishes a temporal correlation between M1 macrophages, TNF-α secretion, and MSC accumulation — with a "rebound" dynamic observable on day 7 after transient depletion
- Identifies 15 candidate MSC genes responsive to TNF-α stimulation (RNA-seq, mouse jawbone context) — Clec4e, Gbp6, Cxcl10, Mmp3, Ccl20, Nos2 among the most relevant
- Demonstrates functionally that Clec4e, Gbp6, and Cxcl10 act as negative regulators of osteoblast differentiation in MSCs; their knockdown accelerates osteogenic commitment

## Methodology

- **Animal model**: C57BL/6J female mice (5 weeks old); clodronate liposome IP injection (12.5 mg/kg) 24 h prior to bilateral maxillary first molar extraction; sacrifice at days 1, 3, 5, 7, 10 (n=4/group)
- **Imaging**: Micro-CT (Skyscan 1174, 6.5 µm resolution, 50 kV, 22 ROI slices); 2D bone area quantified by ImageJ; 3D bone volume by CtAn
- **Histology**: H&E, Masson's trichrome, TRAP for osteoclasts, immunofluorescence with anti-CD80, anti-CD206, anti-PDGFRα, anti-TNF-α, anti-RUNX2
- **In vitro RNA-seq**: Bone marrow MSC isolation (femur/tibia flush), TNF-α stimulation (10 ng/mL, 24 h), Illumina NovaSeq 6000; DESeq2 (|log2FC|>5, FDR<0.05); DAVID functional enrichment; bubble plots in R v4.22
- **siRNA knockdown**: Lipofectamine RNAiMAX transfection of Clec4e, Gbp6, Cxcl10 siRNAs in MSCs; osteogenic differentiation for 1 week; RT-PCR validation

## Results

| Outcome | Clodronate | Control | p |
|---|---|---|---|
| Day 7 bone volume | 0.01 mm³ | 0.02 mm³ | <.0001 |
| Day 7 new bone area | 41.97% | 54.03% | <.0001 |
| Day 5 CD80+ M1 cells | 306.5 | 558.8 | <.0001 |
| Day 7 CD80+ M1 cells | 493.3 | 396.0 | .0004 (rebound) |
| Day 5 PDGFRα+ MSCs | 365.0 | 633.0 | <.0001 |
| Day 7 PDGFRα+ MSCs | 593 | 473 | .0010 (rebound) |

RNA-seq findings: 15 high-expression upregulated genes after TNF-α stimulation; 6 of these (Mmp3, Gbp6, Cxcl10, Clec4e, Ccl20, Nos2) significantly downregulated during osteogenic differentiation of MSCs, suggesting roles in maintaining stemness/immunomodulatory state.

## Related Papers

- [[bone-regeneration/ridge-preservation/fok-2024-alveolar-socket-healing-evolving-knowledge]] — extends: socket healing biology framework; this paper adds M1/MSC/TNF-α cellular mechanism detail to the evolving socket healing model
