---
title: "Evaluation of effects of different sizes and shapes of attachments during rotation, tipping, and torquing in clear aligner therapy - A finite element study"
authors: Pede K, Shetty P, Ranjan A, Khan W, Patil H, Mishra H
year: 2024
doi: 10.4103/jos.jos_199_23
category: [orthodontics/clear-aligner]
source_collection: pubmed-text
full_text: true
pmid: "39450220"
pmcid: "PMC11500733"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11500733/
text_path: /Users/oracleneo/llm-wiki/papers/pede-2024-clear-aligner-attachment-rotation-tipping-torquing-fea.txt
text_filename: pede-2024-clear-aligner-attachment-rotation-tipping-torquing-fea.txt
---

## Why Ingested

위키의 투명교정 카테고리는 52편의 논문을 보유하지만, [[orthodontics/clear-aligner/ubuzima-2025-clear-aligner-fixed-anterior-teeth-movement-adults-sr]]·[[overviews/clear-aligner-indications-limitations]]가 반복 지적하는 "회전(rotation)·경사이동(tipping)·토크(torque)가 투명교정의 약점"이라는 명제를 **어태치먼트 레벨에서 정량 검증한 FEA 논문은 드물다** — [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]]는 어태치먼트가 전치부 root torque·회전을 개선한다는 SR 수준 근거만, [[orthodontics/clear-aligner/kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea]]는 원심이동(distalization) 특화 FEA만 제공한다. 본 논문(Pede 2024, J Orthod Sci)은 5종 어태치먼트 형태(spheroidal·rectangular beveled·triangular beveled·vertical rectangular beveled·rectangular power ridge)를 회전·경사이동·토크 3개 이동유형에 직접 대응시켜 변위·응력을 정량화한 단일모델 FEA로, 이 공백을 메운다.

## Three-line Summary

Single-lab finite element analysis (FEA, ANSYS v15) of an upper-right permanent canine + PDL + composite-attachment + aligner assembly, testing 5 attachment shapes across 3 sizes each (15 models total) mapped to rotation (spheroidal vs. rectangular beveled), tipping (triangular beveled vs. vertical rectangular beveled), and torquing (rectangular power ridge) movements under a constant 2.942 N force.

Smaller attachments consistently produced greater tooth displacement than larger attachments of the same shape (inverse size–displacement relationship); across shape pairs, rectangular beveled attachments allowed more rotation than spheroidal, triangular beveled allowed more tipping than vertical rectangular beveled, and the smallest rectangular power ridge (0.5×0.5×5 mm) produced the most torquing displacement; displacement was consistently greatest at the incisal region and least at the root, and PDL/alveolar-bone stress varied by attachment shape and size.

Attachment shape and size are both independent design levers for tailoring rotation/tipping/torque expression during clear aligner therapy, but this is a single-canine-model, constant-force FEA with no clinical validation, and the source text (extracted from PMC full text without original tables/figures rendered) contains internal model-labeling inconsistencies between the Results/Conclusion narrative and the tabulated attachment dimensions that could not be resolved from the text alone.

## 세줄요약

단일 상악 우측 견치+치주인대(PDL)+복합레진 어태치먼트+아라이너 조립체를 대상으로 한 유한요소해석(Finite Element Analysis, FEA, ANSYS v15) — 어태치먼트 5개 형태 × 3개 크기(총 15모델)를 회전(spheroidal vs rectangular beveled), 경사이동/tipping(triangular beveled vs vertical rectangular beveled), 토크(rectangular power ridge) 3개 이동유형에 대응시켜 일정 힘(2.942N) 하 변위·응력을 측정했다.

동일 형태 내에서는 어태치먼트 크기가 작을수록 변위가 일관되게 컸고(크기-변위 역상관), 형태쌍 비교에서는 rectangular beveled가 spheroidal보다 회전을 더 허용, triangular beveled가 vertical rectangular beveled보다 경사이동을 더 허용, 가장 작은 rectangular power ridge(0.5×0.5×5mm)가 토크 변위가 가장 컸으며, 변위는 절단/교합면(incisal) 부위에서 최대·치근 부위에서 최소로 일관되게 나타났고 PDL·치조골 응력은 어태치먼트 형태·크기에 따라 변화했다.

어태치먼트 형태와 크기 모두 회전·경사이동·토크 표현을 조절하는 독립적 설계 변수이지만, 본 연구는 단일 견치 모델·일정 힘 조건의 FEA로 임상검증이 없고, 원문(PMC 전문텍스트, 원본 표·그림 미포함 추출)에서 Results/Conclusion 서술과 표의 어태치먼트 치수 라벨링 간 일부 내부 불일치가 발견되어 텍스트만으로는 완전히 해소되지 않았다.

## 1. Document Information

- **Journal**: Journal of Orthodontic Science (India) — 2024;13:39
- **DOI**: [10.4103/jos.jos_199_23](https://doi.org/10.4103/jos.jos_199_23) · PMID 39450220 · PMCID PMC11500733
- **Published**: 2024-09-17
- **Design**: Finite element analysis (in-vitro/computational)
- **Source**: PubMed Central full text (JATS), retrieved via PubMed MCP. According to PubMed / PMC.

## 2. Key Contributions

- Maps **5 attachment shapes directly onto 3 clinically named movement categories** — rotation (spheroidal, rectangular beveled), tipping (triangular beveled, vertical rectangular beveled), and torquing (rectangular power ridge) — rather than testing shapes in the abstract.
- Quantifies a consistent **inverse relationship between attachment size and tooth displacement**: within every shape family, the smallest-dimension attachment produced the greatest displacement and the largest-dimension attachment the least, across all three movement types.
- Reports **site-specific displacement gradients** (incisal > cervical/CEJ > root) and **PDL/alveolar-bone/cortical-bone stress distributions** by attachment shape and size — giving a mechanistic picture of where force concentrates, not just how much the crown moves.
- Directly identifies **best-performing dimensions per movement type** (per the paper's own Conclusion): a rectangular beveled attachment for maximal rotation, a triangular beveled attachment for maximal tipping, and the smallest rectangular power ridge for maximal torquing — offering attachment-selection guidance keyed to the desired tooth movement.

## 3. Methodology and Architecture

- **Model**: single upper-right permanent canine (CAD/CAM from a scanned STL model, converted to IGES, geometry built in Catia v5r19) with periodontal ligament (PDL, 0.2 mm average thickness), composite attachment, and clear aligner (0.5 mm average thickness) assembled and meshed with tetrahedral elements in ANSYS v15.
- **Contacts**: bonded (no relative movement) at ligament–bone, tooth–ligament, and tooth–attachment interfaces; frictional contact (coefficient 0.2) between aligner and tooth/attachment surfaces, consistent with prior published values.
- **Loading**: constant 2.942 N force applied along all three axes at the attachment's active side; 0.3 mm displacement adjustment; maximum displacement tracked at three monitored sites (incisal, cervical/CEJ, root).
- **Attachment shapes tested** (3 sizes each, 15 models total):
  - **Rotation**: spheroidal (models 1S/2S/3S: 2.5, 3.0, 3.5 mm length/width, 0.9 mm thickness) vs. rectangular beveled (models 1R/2R/3R: 2.5–3.5 mm length/width, 0.8–1.2 mm thickness).
  - **Tipping**: triangular beveled and vertical rectangular beveled — three size classes shared across both shape families (small 5×0.8×2 mm, medium 4.5×1×2.5 mm, large 4×1.2×3 mm length/thickness/width); the source text's Table 2 uses "T"/"V" model-label prefixes inconsistently between the two shape sub-tables and the Results/Conclusion narrative (see Limitations), so shape-to-dimension mapping for tipping models should be treated as approximate pending original-table verification.
  - **Torquing**: rectangular power ridge (models 1P/2P/3P: depth 0.5–1.0 mm, height 0.5–1.0 mm, width 5–6 mm).
- **Analysis**: purely computational/numerical (no statistical testing performed, per the authors, "given the numerical nature of the data").

## 4. Key Results and Benchmarks

| Movement | Attachment comparison | Key finding |
|---|---|---|
| Rotation | Spheroidal vs. rectangular beveled | Spheroidal displacement range 0.000954–0.001173 mm; rectangular beveled range 0.000902–0.001217 mm. Rectangular beveled attachments showed more rotation overall; the paper's Conclusion names the "1R model" (stated dimensions 3.5×1.2×3.5 mm) as producing the most rotation — but Table 1 lists those dimensions under the 3R model, not 1R (1R = 2.5×0.8×2.5 mm per Table 1). This label/dimension mismatch is reported as extracted, not resolved. |
| Tipping | Triangular beveled vs. vertical rectangular beveled | Triangular beveled displacement range 0.002041–0.002236 mm (max at "1T", dimensions 5×0.8×2 mm per Conclusion); vertical rectangular beveled range 0.001158–0.00203 mm. Triangular beveled attachments permitted more tipping under the same applied force. |
| Torquing | Rectangular power ridge sizes | Displacement range 0.000163 mm (3P, 1×1×6 mm) to 0.000239 mm (1P, 0.5×0.5×5 mm) — smallest power ridge produced the most torquing displacement. |
| Displacement by tooth region (all shapes) | Incisal vs. cervical/CEJ vs. root | Sum displacement was consistently greatest at the incisal region and smallest at the root region across every attachment type and size tested. |
| PDL/bone stress | By attachment shape and size | Vertical rectangular beveled attachments showed the highest PDL stress recorded (0.230955 MPa) and highest alveolar/cortical bone stress (0.507355 MPa) among the models compared in the Results text; rectangular power ridge attachments generally showed the lowest stress values reported. Specific model-label attributions for the lowest-stress comparisons are internally inconsistent in the extracted text (see Limitations) and are reported qualitatively here. |
| Size–displacement relationship | Across all shapes | Larger attachment dimensions consistently reduced tooth displacement (less force delivered per unit displacement); smaller attachments consistently increased displacement — an inverse size-vs-displacement relationship observed across all five shape families. |

## 5. Limitations and Future Work

- **Constant-force design**: only a single force magnitude (2.942 N) was tested; the authors explicitly call for future studies varying force levels across attachment designs and sizes.
- **Single-tooth, single-model FEA**: one upper-right canine model, no biological variability, no clinical (in-vivo) validation — findings describe computational tendencies, not guaranteed clinical outcomes.
- **No statistical testing**: the numerical/deterministic nature of FEA output means no confidence intervals or significance testing were reported; comparisons are point-estimate differences between models.
- **Limited shape/size scope**: only 5 attachment shapes and 3 sizes each were modeled; the authors note future work should broaden the range of attachment styles and materials.
- **Source-text internal inconsistencies (this ingest's own limitation, not the authors')**: the PMC full-text extraction available to us renders body text and table cell values as a flat stream without table structure, and cross-referencing the Results/Discussion/Conclusion narrative against the reconstructed Table 1–3 dimension listings surfaced label mismatches — most clearly, the Conclusion's "1R model" rotation dimensions (3.5×1.2×3.5 mm) match Table 1's 3R row, not 1R. Per Rule #1 (no fabrication), these mismatches are flagged rather than silently resolved; a reader needing the exact shape-to-dimension mapping should consult the original PDF/journal tables directly.

## 6. Related Work

- [[wiki/orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — SR-level evidence that composite attachments improve anterior root torque and rotation; this FEA paper supplies mechanistic, shape/size-level quantification underneath that SR's clinical-outcome findings.
- [[wiki/orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr]] — synthesizes 29 FEA studies on how auxiliaries (including attachments) redistribute crown-vs-root stress; this paper is a primary study of the kind that synthesis draws on.
- [[wiki/orthodontics/clear-aligner/kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea]] — sibling single-model FEA comparing attachment geometries, but for maxillary second-molar distalization rather than rotation/tipping/torquing; together the two papers cover complementary movement types with the same FEA methodology.
- [[wiki/orthodontics/clear-aligner/ubuzima-2025-clear-aligner-fixed-anterior-teeth-movement-adults-sr]] — clinical SR finding rotation and torque (third-order root) control are aligners' weak points versus fixed appliances; this FEA paper provides an attachment-design-level mechanistic explanation for that clinical observation.

## 7. Glossary

- **Finite element analysis (FEA)** — computational method that discretizes (meshes) a structure to simulate stress and displacement under applied loads; used here in lieu of clinical trials to compare attachment designs.
- **Composite attachment** — small resin bump bonded to a tooth surface to give a clear aligner an active, gripping surface for directional force/moment application.
- **Rotation, tipping, torquing** — three orthodontic movement categories with distinct biomechanical demands: rotation (movement about the tooth's long axis), tipping (crown movement with the root as a relatively fixed fulcrum), torquing (buccolingual root movement / third-order control).
- **Rectangular power ridge** — an attachment/aligner feature (a raised ridge rather than a discrete bump) designed specifically to generate torque by concentrating pressure at a defined point on the tooth.
- **Force-driven vs. displacement-driven system** — the paper's framework distinguishing simple movements (tipping, small rotations) governed by the aligner's staged shape-matching ("displacement-driven") from complex movements (torque, root movement) governed by attachment/power-ridge-generated pressure points ("force-driven").
- **Von Mises / PDL / alveolar bone stress** — stress metrics measured at the periodontal ligament, alveolar bone, and cortical bone to characterize how force from an attachment is transmitted into supporting structures.
