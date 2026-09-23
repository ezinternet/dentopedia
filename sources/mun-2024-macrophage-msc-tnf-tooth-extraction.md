---
title: "Macrophages modulate mesenchymal stem cell function via tumor necrosis factor alpha in tooth extraction model"
authors: "Mun AY et al."
year: 2024
doi: 10.1093/jbmrpl/ziae085
category: [bone-regeneration/ridge-preservation]
source_collection: pubmed-text
---

## Why Ingested

This paper investigates the cellular mechanism by which M1 macrophages drive 간엽줄기세포 (Mesenchymal Stem Cell, MSC) recruitment and osteogenic function via 종양괴사인자-α (Tumor Necrosis Factor-alpha, TNF-α) in the tooth extraction socket healing process — filling the immunology/cellular mechanism gap in the wiki's extraction socket and ridge preservation category. It complements [[bone-regeneration/ridge-preservation/fok-2024-alveolar-socket-healing-evolving-knowledge]] by adding molecular-level detail to the macrophage-MSC axis.

## Three-line Summary

Mouse maxillary first molar extraction model (n=4/group) with macrophage depletion by clodronate liposomes, supplemented by in vitro RNA-seq of TNF-α-stimulated bone marrow MSCs (n=3).

Macrophage depletion significantly reduced bone volume at day 7 (0.01 mm³ vs 0.02 mm³, p<.0001) and bone area (41.97% vs 54.03%, p<.0001); M1-derived TNF-α positively correlated with MSC recruitment, and RNA-seq identified 15 candidate immune-regulatory genes in TNF-α-stimulated MSCs.

Knockdown of Clec4e, Gbp6, and Cxcl10 enhanced MSC osteogenic differentiation in vitro, suggesting these genes negatively regulate osteoblast commitment and represent potential targets in bone regeneration therapy.

## 세줄요약

쥐 상악 제1대구치 발치 모델 (n=4/군): 클로드로네이트 리포솜으로 대식세포를 고갈하고, 체외에서 TNF-α 자극 골수 MSC의 RNA-seq(n=3) 병행.

대식세포 고갈 시 7일째 골부피(0.01 vs 0.02 mm³, p<.0001) 및 신생골 면적(41.97% vs 54.03%, p<.0001) 유의 감소; M1 기원 TNF-α와 MSC 집적이 양의 상관관계; RNA-seq에서 TNF-α 자극 MSC의 15개 면역조절 후보 유전자 동정.

Clec4e·Gbp6·Cxcl10 siRNA 녹다운 시 MSC 조골세포 분화 증가 → 이들 유전자가 골아세포 분화를 음성 조절하며 골재생 치료 표적이 될 수 있음.

## 1. Document Information

- **Journal**: JBMR Plus, 2024; 8(8): ziae085
- **DOI**: 10.1093/jbmrpl/ziae085
- **PMID**: 39086598
- **PMC**: PMC11289833
- **Published**: 2024-07-04

## 2. Key Contributions

- Demonstrates that temporal macrophage depletion delays tooth extraction socket (TES) bone healing in a murine model, with quantitative micro-CT and histomorphometric evidence
- Establishes a positive temporal correlation between M1 macrophages (CD80+), TNF-α-secreting cells, and MSC (PDGFRα+) accumulation at the healing site
- Identifies 15 candidate genes (Mmp3, Gbp6, Cxcl10, Clec4e, Ccl20, Nos2, and others) in TNF-α-stimulated MSCs via bulk RNA-seq that may regulate immunomodulatory capacity
- Shows that in vitro knockdown of Clec4e, Gbp6, and Cxcl10 enhances osteogenic gene expression (Runx2, Alp)

## 3. Methodology and Architecture

- **Animal model**: 5-week-old female C57BL/6J mice; bilateral maxillary first molar extraction; clodronate liposomes (12.5 mg/kg IP) vs saline control; sacrifice at days 1, 3, 5, 7, 10 (n=4/group)
- **Imaging**: Micro-CT (Skyscan 1174, 6.5 µm resolution, 50 kV); bone volume and area quantified in 22 ROI slices
- **Histology**: H&E, Masson's trichrome, TRAP staining, immunofluorescence for CD80 (M1), CD206 (M2), PDGFRα (MSC), TNF-α, RUNX2, Clec4e, Gbp6
- **In vitro**: Bone marrow MSC isolation from femur/tibia; TNF-α stimulation (10 ng/mL, 24 h); bulk RNA-seq (Illumina NovaSeq 6000); DESeq2 analysis (DEGs: |log2FC|>5, FDR<0.05); DAVID enrichment; siRNA knockdown of Clec4e, Gbp6, Cxcl10 followed by osteogenic differentiation

## 4. Key Results and Benchmarks

- **Day 7 bone volume**: Clodronate 0.01 mm³ vs control 0.02 mm³ (p<.0001)
- **Day 7 new bone area**: Clodronate 41.97% vs control 54.03% (p<.0001)
- **CD80+ M1 recovery**: Clodronate group rebounded above control on day 7 (493.3 vs 396.0, p=.0004)
- **PDGFRα+ MSCs**: Reduced days 1–5, rebounded day 7 (593 vs 473, p=.0010)
- **RNA-seq**: 15,534 total genes; 59 with |log2FC|>5; 56 upregulated / 3 downregulated after TNF-α stimulation; 15 high-expression candidates (log2TPM>5)
- **siRNA functional test**: Knockdown of Clec4e, Gbp6, Cxcl10 each significantly increased Runx2 and Alp mRNA (all p<.0001) in osteogenic conditions
