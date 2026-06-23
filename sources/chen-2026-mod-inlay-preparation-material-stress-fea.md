---
title: "The impact of preparation dimensions and material choice on stress distribution in MOD inlays: a 3D finite element study"
authors: Sensen Chen, Ruizhen Chen, Yao Chen, Zhiqiang Zheng, Jie Lin
year: 2026
doi: 10.1186/s12903-025-07613-8
category: [inlay]
source_collection: pubmed-text
full_text: true
pmid: "41519748"
pmcid: "PMC12882518"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12882518/
text_path: /Users/oracleneo/llm-wiki/papers/chen-2026-mod-inlay-preparation-material-stress-fea.txt
text_filename: chen-2026-mod-inlay-preparation-material-stress-fea.txt
---

## Why Ingested

Existing inlay FEA/preparation-design pages ([[inlay/hofsteenge-2023-preparation-design-fracture-strength-disilicate-inlay]], [[inlay/wang-2025-foundation-restoration-onlay-mandibular-molar-endodontic-fea]]) examine fracture strength and onlay foundation stress, but none systematically crosses inlay *material elastic modulus* with *preparation depth × width* for MOD inlays. This 36-model FEA fills that gap, quantifying the material-geometry interaction and giving a concrete inlay-vs-onlay depth threshold (≤4 mm inlay / >4 mm onlay). It also extends the zirconia-inlay biomechanics theme of [[inlay/al-fodeh-2026-monolithic-zirconia-inlays-cement-aging]] by showing zirconia's cervical stress-concentration tradeoff.

## One-line Summary

3D FEA (36 models, mandibular first molar, 100 N vertical + 30° oblique) showing MOD-inlay stress depends on material × preparation-dimension interaction: low-modulus resin-based ceramics distribute stress most uniformly (lowest inlay stress but highest remaining-tooth stress), zirconia is the opposite (highest inlay/cervical stress, lowest tooth stress); d=4 mm/w=4 mm is generally the lowest-inlay-stress configuration; authors propose inlay ≤4 mm depth, onlay >4 mm.

## 한줄요약

3D 유한요소분석 (36개 모델, 하악 제1대구치, 100 N 수직 + 30° 사면하중) — MOD 인레이 응력은 재료 탄성계수 × 와동 깊이·폭 상호작용으로 결정. 저탄성 레진세라믹(RBCs)은 응력을 가장 균일하게 분산(인레이 응력 최저·잔존치질 응력 최고), 지르코니아는 정반대(인레이/치경부 응력 최고·잔존치질 응력 최저). 인레이 응력은 대개 깊이 4 mm/폭 4 mm에서 최소이며, 저자는 깊이 ≤4 mm 인레이·>4 mm 온레이를 제안.

## 1. Document Information

- **Type**: In-vitro 3D finite element analysis (FEA) — biomechanical simulation, no human/animal subjects
- **Journal**: BMC Oral Health 2026;26(1):259
- **Affiliation**: Department of VIP Dental Service, Fujian Medical University (School & Hospital of Stomatology); co-author at Nippon Dental University, Tokyo
- **Model**: Mandibular first molar from anonymized CBCT; enamel/dentin/pulp + resin cement (50 μm, ISO 4049) + simplified cortical alveolar bone cuboid (15×16×11 mm)
- **Software**: Mimics 21.0 → Geomagic Studio 2021 → SolidWorks 2021 → Ansys Workbench 24.0 (SOLID187 ten-node tetrahedral elements)

## 2. Key Contributions

- Crosses **4 materials × 3 depths × 3 widths = 36 MOD-inlay FE models** — the first systematic factorial of material modulus against both preparation dimensions for MOD inlays.
- Quantifies the **inverse stress partition**: high-modulus restorations shield tooth structure but concentrate stress in the restoration (and cervically); low-modulus restorations do the opposite.
- Translates findings into a **clinical decision pathway**: select restoration by defect depth (inlay ≤4 mm, onlay >4 mm), then material by remaining tooth structure.

## 3. Methodology and Architecture

- **Materials (Young's modulus / Poisson ratio)**: Zirconia 210,000 MPa/0.31; LD 95,000/0.21; GA (gold alloy) 90,000/0.31; RBCs (resin-based ceramics) 37,800/0.24. Reference tissues: enamel 80,000, dentin 15,000, pulp 2, cortical bone 13,700, resin cement 8,000 MPa.
- **Preparation**: MOD cavity; depth d = 2/4/6 mm, width w = 2/4/6 mm.
- **Loading**: static 100 N vertical to occlusal center; plus 100 N at 30° oblique on the same central patch.
- **Outcome**: peak Maximum Principal Stress (MPS, σ₁) in inlay, enamel, dentin, and remaining tooth structure; stress contour plots.
- **Assumptions**: all materials homogeneous, isotropic, linear elastic; bonded interfaces (no sliding); small deformation; bone top/bottom fixed.

## 4. Key Results and Benchmarks

- **Material ranking (peak inlay MPS, vertical, d=2/w=2)**: Zirconia 143.2 > GA 128.3 ≈ LD 127.9 > RBCs 115.5 MPa. Oblique: Zirconia 127.9 > LD 111.6 ≈ GA 108.8 > RBCs 95.6 MPa.
- **Inverse on remaining tooth (vertical, d=2/w=2)**: RBCs highest (45.9 MPa), Zirconia lowest (35.9 MPa); LD/GA intermediate.
- **Stress location**: concentrated at the loaded contact surface and the bottom of the inlay. Zirconia stress concentrates in the **inlay neck (cervical)**; RBCs distribution is the most **uniform**.
- **Geometry (inlay stress, vertical)**: lowest generally at **w = 4 mm** and **d = 4 mm** (e.g., Zirconia d=4: w2 95.9 → w4 72.4 → w6 77.7 MPa). Material-specific exceptions: LD at d=2 mm lowest at w=6 mm (93.2); Zirconia at w=2 mm lowest at d=6 mm (94.4).
- **Geometry (remaining tooth)**: at d=2 mm, tooth MPS falls as width increases; at d=4/6 mm, minimum at w=4 mm. Tooth MPS generally falls as depth increases — but **deep narrow prep (d=6/w=2)** gives high stress concentration (echoes Yang et al.).
- **Lowest-tooth-stress / "dangerous optimization"**: d=6 mm/w=4 mm can minimize MPS but forms a deeply embedded rigid core that erodes cervical peripheral dentin → occult root-fracture risk the model cannot capture. Authors advise high-strength zirconia (best at d=4/w=4) or switching to onlay/full crown for such deep cases.

## 5. Limitations and Future Work

- Simplified cortical-only alveolar bone; **no cancellous bone, no periodontal ligament (PDL)** → may overestimate bone-supported stress.
- All tissues/materials homogeneous, isotropic, linear elastic; mainly static loading; oblique analysis limited in scope; no cyclic/dynamic fatigue, no thermal effects.
- Single tooth, single CBCT geometry, generic (non-brand) material properties.
- Numerical simulation only — requires in-vitro and long-term clinical validation.

## 6. Related Work

- Yang et al.: MOD cavity generates highest stress vs MO/O; increased depth/width → more stress concentration.
- Durand et al.: thicker inlay favors stress distribution; low-modulus base raises inner-ceramic stress concentration.
- Chen et al. (prior): larger isthmus width reduces peak MPS. Mei et al.: increasing inlay width raises inlay stress. Present study partially agrees with both — relationship is non-linear and material-dependent.

## 7. Glossary

- **MOD inlay**: mesial-occlusal-distal intracoronal indirect restoration.
- **MPS (Maximum Principal Stress, σ₁)**: largest normal tensile (or least compressive) stress at a point; FEA tensile-failure proxy.
- **RBCs (Resin-Based Ceramics)**: hybrid/resin-ceramic CAD-CAM materials with elastic modulus (~38 GPa) close to dentin.
- **LD (Lithium Disilicate)**, **GA (Gold Alloy)**: medium-modulus restorative materials.
- **FEA (Finite Element Analysis)**: numerical stress simulation by discretizing geometry into elements.

---

*Source: PubMed / PubMed Central. DOI: [10.1186/s12903-025-07613-8](https://doi.org/10.1186/s12903-025-07613-8)*
