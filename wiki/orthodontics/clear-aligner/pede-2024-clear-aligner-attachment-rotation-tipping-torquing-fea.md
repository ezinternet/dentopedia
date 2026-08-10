---
title: "Evaluation of effects of different sizes and shapes of attachments during rotation, tipping, and torquing in clear aligner therapy - A finite element study"
authors: Pede K, Shetty P, Ranjan A, Khan W, Patil H, Mishra H
year: 2024
date: 2024-09-17
doi: 10.4103/jos.jos_199_23
source: pede-2024-clear-aligner-attachment-rotation-tipping-torquing-fea.md
category: [orthodontics/clear-aligner]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "39450220"
pmcid: "PMC11500733"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11500733/
text_path: /Users/oracleneo/llm-wiki/papers/pede-2024-clear-aligner-attachment-rotation-tipping-torquing-fea.txt
text_filename: pede-2024-clear-aligner-attachment-rotation-tipping-torquing-fea.txt
relations:
  - type: reinforces
    target: nucera-2022-composite-attachments-clear-aligners-sr
  - type: reinforces
    target: cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr
  - type: extends
    target: kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea
tags: [clear-aligner, attachment-design, rotation, tipping, torque, finite-element-analysis, biomechanics, composite-attachment, power-ridge]
---

## Three-line Summary

Single-lab finite element analysis (FEA, ANSYS v15) of an upper-right permanent canine + PDL + composite-attachment + aligner assembly, testing 5 attachment shapes across 3 sizes each (15 models total) mapped to rotation (spheroidal vs. rectangular beveled), tipping (triangular beveled vs. vertical rectangular beveled), and torquing (rectangular power ridge) movements under a constant 2.942 N force.

Smaller attachments consistently produced greater tooth displacement than larger attachments of the same shape (inverse size–displacement relationship); across shape pairs, rectangular beveled attachments allowed more rotation than spheroidal, triangular beveled allowed more tipping than vertical rectangular beveled, and the smallest rectangular power ridge (0.5×0.5×5 mm) produced the most torquing displacement; displacement was consistently greatest at the incisal region and least at the root, and PDL/alveolar-bone stress varied by attachment shape and size.

Attachment shape and size are both independent design levers for tailoring rotation/tipping/torque expression during clear aligner therapy, but this is a single-canine-model, constant-force FEA with no clinical validation, and the source text has internal model-labeling inconsistencies between the Results/Conclusion narrative and the tabulated attachment dimensions.

## 세줄요약

단일 상악 우측 견치+치주인대(PDL)+복합레진 어태치먼트+아라이너 조립체를 대상으로 한 유한요소해석(Finite Element Analysis, FEA, ANSYS v15) — 어태치먼트 5개 형태 × 3개 크기(총 15모델)를 회전(spheroidal vs rectangular beveled), 경사이동/tipping(triangular beveled vs vertical rectangular beveled), 토크(rectangular power ridge) 3개 이동유형에 대응시켜 일정 힘(2.942N) 하 변위·응력을 측정했다.

동일 형태 내에서는 어태치먼트 크기가 작을수록 변위가 일관되게 컸고(크기-변위 역상관), 형태쌍 비교에서는 rectangular beveled가 spheroidal보다 회전을 더 허용, triangular beveled가 vertical rectangular beveled보다 경사이동을 더 허용, 가장 작은 rectangular power ridge(0.5×0.5×5mm)가 토크 변위가 가장 컸으며, 변위는 절단면(incisal) 부위에서 최대·치근 부위에서 최소로 일관되게 나타났고 PDL·치조골 응력은 어태치먼트 형태·크기에 따라 변화했다.

어태치먼트 형태와 크기 모두 회전·경사이동·토크 표현을 조절하는 독립적 설계 변수이지만, 본 연구는 단일 견치 모델·일정 힘 조건의 FEA로 임상검증이 없고, 원문 서술과 표의 어태치먼트 치수 라벨링 간 일부 내부 불일치가 있다.

## Summary

This finite element study (Journal of Orthodontic Science, India) built a single upper-right permanent canine model — with periodontal ligament (PDL), composite attachment, and clear aligner — in ANSYS v15 to directly test how attachment **shape and size** affect the three orthodontic movement categories aligners are said to handle least predictably: rotation, tipping, and torquing. Five attachment shapes (spheroidal, rectangular beveled, triangular beveled, vertical rectangular beveled, rectangular power ridge), each in three sizes, were modeled under a constant 2.942 N force — 15 models total. Across every shape family, smaller attachments produced greater tooth displacement than larger ones of the same shape, and shape mattered independently: rectangular beveled attachments out-rotated spheroidal ones, triangular beveled attachments allowed more tipping than vertical rectangular beveled ones, and the smallest rectangular power ridge produced the most torquing displacement. Displacement was consistently largest at the incisal region and smallest at the root across all models, and periodontal-ligament/alveolar-bone stress varied by both attachment shape and size. As a single-tooth, single-force FEA study without clinical replication, findings describe biomechanical tendencies for attachment selection rather than guaranteed clinical outcomes, and this ingest flags a specific internal inconsistency between the paper's Conclusion-stated "best rotation" attachment dimensions and its own Table 1 listing (see Related Papers / source page for detail) that could not be resolved from the extracted full text alone.

## Key Contributions

- Maps **5 attachment shapes directly onto 3 named clinical movement categories** (rotation, tipping, torquing) rather than testing attachment geometry in the abstract — giving movement-specific design guidance.
- Demonstrates a consistent **inverse size–displacement relationship**: within every shape family tested, the smallest attachment produced the greatest tooth displacement and the largest attachment the least, across rotation, tipping, and torquing alike.
- Quantifies **shape-pair comparisons for each movement type**: rectangular beveled > spheroidal for rotation displacement; triangular beveled > vertical rectangular beveled for tipping displacement; smallest rectangular power ridge > larger power ridges for torquing displacement.
- Reports a consistent **incisal > cervical > root displacement gradient** across all attachment types, and PDL/alveolar-bone/cortical-bone stress patterns that vary by attachment shape/size — a mechanistic picture beneath the "attachments improve rotation/torque" SR-level conclusions already in the wiki.

## Methodology

- **Model**: single CAD/CAM-derived upper-right permanent canine (STL → IGES → Catia v5r19 geometry) with PDL (0.2 mm average thickness), composite attachment, and aligner (0.5 mm average thickness); tetrahedral meshing in ANSYS v15.
- **Contacts**: bonded interfaces at ligament–bone, tooth–ligament, tooth–attachment; frictional contact (coefficient 0.2) between aligner and tooth/attachment surfaces.
- **Loading**: constant 2.942 N force along all three axes at the attachment's active side; 0.3 mm displacement adjustment; displacement tracked at incisal, cervical (CEJ), and root sites.
- **15 models across 5 shapes, 3 sizes each**: spheroidal and rectangular beveled (rotation); triangular beveled and vertical rectangular beveled (tipping); rectangular power ridge (torquing).
- **Analysis**: deterministic numerical/computational output (no statistical testing performed, per the authors).

## Results

| Movement | Comparison | Key finding |
|---|---|---|
| Rotation | Spheroidal vs. rectangular beveled | Spheroidal displacement 0.000954–0.001173 mm; rectangular beveled 0.000902–0.001217 mm. Rectangular beveled attachments allowed more rotation overall. |
| Tipping | Triangular beveled vs. vertical rectangular beveled | Triangular beveled 0.002041–0.002236 mm; vertical rectangular beveled 0.001158–0.00203 mm. Triangular beveled attachments permitted more tipping under the same force. |
| Torquing | Rectangular power ridge sizes | 0.000163 mm (largest, 1×1×6 mm) to 0.000239 mm (smallest, 0.5×0.5×5 mm) — smallest power ridge produced the most torquing displacement. |
| By tooth region (all shapes) | Incisal vs. cervical vs. root | Displacement consistently greatest at incisal region, smallest at root region, across every attachment type and size. |
| PDL/bone stress | By shape/size | Vertical rectangular beveled attachments showed the highest recorded PDL stress (0.230955 MPa) and highest alveolar/cortical bone stress (0.507355 MPa) among compared models; rectangular power ridge attachments generally showed the lowest stress values reported. |
| Size vs. displacement | Across all shapes | Larger attachments → less tooth displacement (more force dissipated by the attachment itself); smaller attachments → more displacement — inverse relationship observed across all 5 shape families. |

## Clinical Bottom Line

- Attachment **shape and size are both usable design levers**, independent of each other, for dialing in rotation, tipping, or torquing expression during clear aligner therapy — not just "add an attachment," but which shape and how large.
- When **more rotation or tipping is the treatment goal**, this FEA suggests rectangular beveled (over spheroidal) and triangular beveled (over vertical rectangular beveled) attachments, respectively, and **smaller attachments generally over larger ones** of the same shape.
- For **torquing**, the smallest rectangular power ridge modeled produced the most displacement — consistent with the broader FEA literature ([[orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr]]) that power ridges are the primary force-driven mechanism for torque/root movement, distinct from displacement-driven tipping/rotation.
- Treat exact numeric magnitudes cautiously: this is a single-tooth, single-force, non-clinically-validated FEA model, and specific attachment-dimension attributions in the published Conclusion do not fully match the paper's own tables (see source page for the flagged inconsistency) — use the paper for **directional/mechanistic** guidance, not precise millimeter thresholds.

## Related Papers

- [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — reinforces: SR-level evidence that composite attachments improve anterior root torque and rotation; this FEA paper supplies shape/size-level mechanistic detail underneath that conclusion.
- [[orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr]] — reinforces: synthesizes 29 FEA studies on auxiliary-driven stress redistribution; this paper is a primary study of the kind feeding that synthesis.
- [[orthodontics/clear-aligner/kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea]] — extends: sibling single-model FEA using the same methodology but for maxillary second-molar distalization; together the two papers cover complementary movement types (distalization vs. rotation/tipping/torquing).
- [[orthodontics/clear-aligner/ubuzima-2025-clear-aligner-fixed-anterior-teeth-movement-adults-sr]] — clinical SR finding rotation and torque control are aligners' weak points versus fixed appliances; this FEA paper provides an attachment-design-level mechanistic explanation for that clinical observation.
