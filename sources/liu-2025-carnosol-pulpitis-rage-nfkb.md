---
title: "Carnosol exerts anti-inflammatory effects in pulpitis by inhibiting the RAGE/NF-κB signalling pathway"
authors: "Xinpai Liu, Chunhui Zhao, Xirun Zong, Wenjing Fang, Jing Zhang, Wei He, Wuli Li"
year: 2025
doi: 10.1038/s41598-025-28542-0
journal: "Scientific Reports"
stem: liu-2025-carnosol-pulpitis-rage-nfkb
evidence_level: controlled-lab-study
---

## Why Ingested

Linked to [[endodontics/vpt]] — first study demonstrating carnosol (a natural phenolic diterpenoid from rosemary/sage) suppresses pulpal inflammation via the RAGE/NF-κB signalling pathway, both in vitro (hDPCs, LPS model) and in vivo (SD rat pulpitis model). Directly relevant to vital pulp preservation research and identification of novel natural anti-inflammatory agents for pulpitis management.

## Three-line Summary

Carnosol (CA), a natural diterpenoid from rosemary and sage, dose-dependently suppresses IL-1β, IL-6, and TNF-α in LPS-stimulated human dental pulp cells (hDPCs) and reduces pulpal inflammation in an SD rat pulpitis model. The mechanism operates through RAGE/NF-κB: CA downregulates RAGE mRNA transcription, reduces NF-κB phosphorylation, and blocks p65 nuclear translocation; RAGE siRNA knockdown abolishes CA's anti-inflammatory effects, confirming RAGE as the obligate upstream mediator. CA modulates RAGE at the transcriptional level (not via protein stability), and at 10 µM reduces cytokine levels to near-baseline, suggesting potential as a pharmacological agent for pulpitis management.

## 세줄요약

카르노솔(CA)은 로즈마리·세이지 유래 천연 페놀성 디테르페노이드로, LPS 자극된 인간 치수세포(hDPCs)에서 IL-1β, IL-6, TNF-α를 농도의존적으로 억제하며 SD 쥐 치수염 모델에서도 염증을 감소시켰다. 기전은 RAGE/NF-κB 경로: CA가 RAGE mRNA 전사를 억제하고 NF-κB 인산화·p65 핵이동을 차단하며, RAGE siRNA 처리 시 CA의 항염 효과가 소실되어 RAGE가 필수 상위 매개체임이 확인됐다. CA는 단백질 안정성이 아닌 전사 수준에서 RAGE를 조절하며, 10 µM에서 사이토카인을 정상 수준에 가깝게 억제해 치수염 치료제 후보로서의 가능성을 시사한다.

---

## Study Design

- **Type**: In vitro + in vivo controlled laboratory study
- **In vitro model**: Human dental pulp cells (hDPCs) isolated from third molars or orthodontically extracted healthy teeth
  - LPS stimulation: 1 µg/mL, 6 hours
  - CA treatment: 2.5, 5, 10 µM (concurrent with LPS)
  - Baseline viability confirmed (CCK-8, no significant cytotoxicity at all three doses)
- **In vivo model**: Sprague-Dawley (SD) rats, 4 groups:
  - Drilled (pulp exposure, no treatment)
  - CA-treated (50 µM, 3 µL applied to exposed pulp)
  - DMSO-treated (vehicle control)
  - Intact control
- **Outcomes measured**:
  - Pro-inflammatory cytokines: IL-1β, IL-6, TNF-α (qRT-PCR, ELISA, Western blot)
  - RAGE expression (qRT-PCR, Western blot, immunohistochemistry)
  - NF-κB pathway: p-p65 phosphorylation (WB), p65 nuclear translocation (immunofluorescence)
  - RAGE mechanism: siRNA knockdown (si-RAGE), cycloheximide (CHX) protein stability assay
  - Histology: HE staining, immunohistochemistry (RAGE, p-p65, IL-1β)
  - RNA-seq with GO and KEGG enrichment analyses

## Key Results

### Cytotoxicity
CA at 2.5, 5, 10 µM showed no significant cytotoxicity to hDPCs (with or without LPS), P > 0.05 by two-way ANOVA.

### Anti-inflammatory Efficacy (In Vitro)
- CA dose-dependently reduced IL-6, IL-1β, and TNF-α mRNA levels in LPS-treated hDPCs (qRT-PCR)
- At 10 µM, protein levels of all three cytokines reduced to near-control levels (WB + ELISA)
- RNA-seq confirmed downregulation of IL-6, TNF-α, IL-1β in LPS+CA vs LPS group

### RAGE Pathway
- LPS induced RAGE expression; CA pre-treatment dose-dependently reduced RAGE mRNA and protein
- At 10 µM CA: RAGE expression returned to near-control levels
- GO/KEGG enrichment of RNA-seq data implicated AGE-RAGE and NF-κB pathways as primary CA mechanisms

### NF-κB Suppression
- CA significantly reduced NF-κB phosphorylation (p-p65) in LPS-stimulated hDPCs
- At 5 µM CA: NF-κB p65 phosphorylation nearly completely inhibited
- Immunofluorescence: CA blocked LPS-induced p65 nuclear translocation

### RAGE as Obligate Mediator (siRNA Validation)
- si-RAGE knockdown alone: RAGE protein significantly reduced; IL-6, IL-1β, TNF-α levels approached control
- si-RAGE + LPS + CA: CA's modulatory effects on cytokines were abolished — RAGE silencing negated CA's additional anti-inflammatory benefit
- Immunofluorescence: CA did not further reduce p65 nuclear translocation in si-RAGE-transfected cells
- Conclusion: RAGE is the required upstream target through which CA exerts anti-inflammatory effects

### Mechanism of RAGE Regulation
- CHX (protein synthesis inhibitor) protein stability assay: RAGE protein degradation rate was NOT significantly different between CHX alone vs CHX + CA (P > 0.05)
- Conclusion: CA reduces RAGE primarily at the transcriptional level, not through post-translational protein stability modulation

### In Vivo Validation (SD Rat Pulpitis Model)
- HE staining: drilled + CA group showed reduced neutrophil infiltration, more organised odontoblast layer, minimal vasodilation vs drilled control
- Immunohistochemistry: drilled + CA group had markedly weaker RAGE, p-p65, and IL-1β staining intensity vs drilled + DMSO group
- Quantitative IHC confirmed significant reduction in RAGE, p-p65, IL-1β expression in CA-treated pulps

## Carnosol Background

- Phenolic diterpenoid naturally derived from rosemary (Rosmarinus officinalis) and sage (Salvia officinalis) plants
- First characterised by Brieskorn et al.
- Known properties: antioxidant, anti-inflammatory, antimicrobial, immunomodulatory, anticancer
- Prior clinical applications: dermatitis, rheumatoid arthritis, autoimmune encephalomyelitis
- European herbal medicine: sage tea used for oral inflammation, gingivitis, sore throat
- Rosemary toothpaste (randomised double-blind RCT): effective in treating gingivitis
- This study is the first to demonstrate CA's anti-inflammatory effects in pulpitis via RAGE/NF-κB

## RAGE Biology Relevant to Pulpitis

- RAGE (receptor for advanced glycation end products): pattern recognition receptor, Ig superfamily
- Ligands: HMGB1, advanced glycation end products (AGEs)
- Expression: low under normal physiological conditions; markedly upregulated during chronic inflammation (ligand accumulation)
- RAGE-ligand axis implicated in: diabetic complications, cardiovascular disease, neurodegeneration, cancer, inflammatory conditions
- RAGE → NF-κB activation → oxidative stress → pro-inflammatory cytokine production
- Prior studies (cited as refs 31, 32): elevated RAGE expression in inflamed human pulpal tissues correlates with pulpitis progression
- This study establishes the RAGE/NF-κB axis as a mechanistic target for pharmacological pulpitis intervention

## Limitations

- In vitro LPS model (gram-negative bacterial endotoxin) may not fully replicate polymicrobial clinical pulpitis
- Rat model with mechanical pulp exposure ≠ caries-induced pulpitis
- CA concentrations (2.5–10 µM in vitro; 50 µM in vivo) not validated for clinical delivery or bioavailability
- No evaluation of CA's effect on pulp repair or dentin bridge formation (only inflammation suppression)
- No comparison to existing VPT medicaments (MTA, Biodentine, corticosteroids)
- Single time-point analysis (6h LPS stimulation); no long-term pulp outcome data

## Clinical Relevance

- Establishes RAGE/NF-κB as a druggable pathway in pulpitis
- Carnosol as a natural-origin anti-inflammatory candidate with known safety profile in other conditions
- Potential application: anti-inflammatory adjunct in vital pulp therapy, direct pulp capping, partial pulpotomy contexts
- Research direction: need delivery vehicle development (e.g., incorporation into pulp-capping materials or intracanal medicaments) before clinical translation
