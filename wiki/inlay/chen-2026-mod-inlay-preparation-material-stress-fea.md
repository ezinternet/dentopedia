---
title: "The impact of preparation dimensions and material choice on stress distribution in MOD inlays: a 3D finite element study"
authors: Sensen Chen, Ruizhen Chen, Yao Chen, Zhiqiang Zheng, Jie Lin
year: 2026
date: 2026-01-10
doi: 10.1186/s12903-025-07613-8
source: chen-2026-mod-inlay-preparation-material-stress-fea.md
category: [inlay]
confidence: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "41519748"
pmcid: "PMC12882518"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12882518/
text_path: /Users/oracleneo/llm-wiki/papers/chen-2026-mod-inlay-preparation-material-stress-fea.txt
text_filename: chen-2026-mod-inlay-preparation-material-stress-fea.txt
tags: [inlay, MOD, FEA, finite-element, stress-distribution, zirconia, lithium-disilicate, resin-based-ceramics, gold-alloy, preparation-design]
relations:
  - type: extends
    target: hofsteenge-2023-preparation-design-fracture-strength-disilicate-inlay
  - type: reinforces
    target: al-fodeh-2026-monolithic-zirconia-inlays-cement-aging
---

## One-line Summary

3D FEA (36 models, mandibular first molar, 100 N vertical + 30° oblique) showing MOD-inlay stress depends on a material × preparation-dimension interaction: low-modulus resin-based ceramics (RBCs) distribute stress most uniformly (lowest inlay stress, highest remaining-tooth stress), zirconia is the opposite (highest inlay/cervical stress, lowest tooth stress); d=4 mm/w=4 mm generally minimizes inlay stress; authors propose inlay ≤4 mm depth, onlay >4 mm.

## 한줄요약

3D 유한요소분석 (36개 모델, 하악 제1대구치, 100 N 수직 + 30° 사면하중) — MOD 인레이 응력은 재료 탄성계수 × 와동 깊이·폭 상호작용으로 결정. 저탄성 레진세라믹(RBCs)은 응력을 가장 균일하게 분산(인레이 응력 최저·잔존치질 응력 최고), 지르코니아는 정반대(인레이/치경부 응력 최고·잔존치질 응력 최저). 인레이 응력은 대개 깊이 4 mm/폭 4 mm에서 최소이며, 저자는 깊이 ≤4 mm 인레이·>4 mm 온레이를 제안.

## Summary

Chen et al. built **36 finite-element models** of a mandibular first molar MOD inlay (4 materials × 3 depths × 3 widths) loaded statically with 100 N vertically and at a 30° oblique angle, scoring peak **Maximum Principal Stress (MPS)** in the inlay, enamel, dentin, and remaining tooth structure. The central finding is that no single preparation rule fits all materials: stress distribution is governed by the **interaction** between the restorative material's elastic modulus and the preparation geometry (depth × width).

A consistent **inverse stress partition** emerged. High-modulus **zirconia** (210 GPa) carries more of the load itself — highest internal inlay stress, concentrated at the **inlay neck (cervical region)** — while shielding the surrounding tooth (lowest remaining-tooth MPS). Low-modulus **resin-based ceramics** (RBCs, ~38 GPa, close to dentin) do the opposite: the most **uniform** stress field and the lowest internal inlay stress, but they pass more stress into the tooth. LD and gold alloy sit in between.

The clinically actionable geometry signal is that **d = 4 mm / w = 4 mm** is the most common lowest-inlay-stress configuration, with material-specific exceptions. Deep narrow preparations (d=6/w=2) concentrate stress; and although d=6/w=4 can minimize MPS numerically, the authors flag this as a "dangerous optimization" that undermines cervical dentin and risks occult root fracture — for such deep defects they recommend a high-strength material or switching to an **onlay/full crown**.

## Key Contributions

- First systematic **factorial** of inlay material modulus against both preparation depth and width for MOD inlays (36 models).
- Demonstrates the **modulus-driven inverse stress partition** between restoration and tooth, and that zirconia concentrates stress cervically while RBCs distributes uniformly.
- Proposes a concrete **decision pathway**: pick restoration type by defect depth (inlay ≤4 mm / onlay >4 mm), then material by remaining tooth structure — prioritizing dentin-compatible modulus (RBCs) over raw strength.

## Methodology

- **Model**: anonymized-CBCT mandibular first molar (enamel, dentin, pulp) + 50 μm resin cement (ISO 4049) + simplified cortical alveolar-bone cuboid (15×16×11 mm). Mimics 21.0 → Geomagic 2021 → SolidWorks 2021 → Ansys Workbench 24.0 (SOLID187 ten-node tetrahedral elements; 1.55M–3.98M nodes).
- **Materials (E / ν)**: Zirconia 210,000 MPa/0.31; LD 95,000/0.21; GA 90,000/0.31; RBCs 37,800/0.24.
- **Preparation**: MOD cavity, depth 2/4/6 mm × width 2/4/6 mm.
- **Loading**: static 100 N vertical (occlusal center) and 100 N at 30° oblique on the same patch.
- **Outcome**: peak MPS (σ₁) per component; contour plots. Bonded interfaces; homogeneous/isotropic/linear-elastic assumptions.

## Results

- **Material ranking — peak inlay MPS (vertical, d=2/w=2)**: Zirconia 143.2 > GA 128.3 ≈ LD 127.9 > RBCs 115.5 MPa. Oblique: Zirconia 127.9 > LD 111.6 ≈ GA 108.8 > RBCs 95.6 MPa. **RBCs lowest, zirconia highest internal stress across most combinations.**
- **Remaining tooth (vertical, d=2/w=2)** — inverse: RBCs highest (45.9), Zirconia lowest (35.9 MPa); LD/GA intermediate.
- **Stress location**: loaded contact surface + bottom of inlay; **zirconia → inlay neck/cervical concentration**, **RBCs → uniform**.
- **Width effect (inlay, vertical)**: generally lowest at **w = 4 mm** (Zirconia d=4: 95.9 → 72.4 → 77.7 MPa for w=2/4/6). Exception: LD at d=2 mm lowest at w=6 mm (93.2).
- **Depth effect (inlay, vertical)**: generally lowest at **d = 4 mm** (LD w=2: 127.9 → 102.9 → 105.6 for d=2/4/6). Exception: Zirconia at w=2 mm lowest at d=6 mm (94.4).
- **Remaining tooth**: tooth MPS generally falls as depth increases and (at d≥4) is minimized at w=4 mm; under oblique loading the depth→lower-tooth-stress trend held for every material, but width effects were material-specific (no universal rule).
- **Material/dimension that minimized stress**: **RBCs** minimized internal inlay stress and gave the most uniform field (lowest tooth-fracture risk per authors); **zirconia at d=4 mm/w=4 mm** minimized inlay stress among high-modulus options and best protected tooth tissue but with cervical concentration. The d=4/w=4 geometry was the broadly favorable configuration.

## Clinical Implications

- Favor **biomechanical compatibility with dentin over raw strength**: RBCs (modulus near dentin) give uniform stress and lower fracture risk — but lower wear resistance, so balance against longevity.
- **Zirconia** raises cervical stress concentration → use cautiously; if used in deep cases, d=4/w=4 is the least-stress geometry.
- Target **~4 mm depth and width** for high-modulus ceramics; avoid excessively deep preparations.
- Decision pathway: **inlay for defect depth ≤4 mm, onlay/full crown for >4 mm**, then choose material by remaining tooth structure.

## Limitations

In-vitro FEA only — simplified cortical-only bone (no cancellous bone/PDL, may overestimate bone-borne stress), homogeneous/isotropic/linear-elastic assumption, predominantly static loading (limited oblique scope, no fatigue/thermal), single tooth/geometry, generic material properties. Needs in-vitro and clinical validation.

## Related Papers

- [[inlay/hofsteenge-2023-preparation-design-fracture-strength-disilicate-inlay]] — extends: that study links preparation design to fracture strength of lithium-disilicate inlays; this adds the modulus × depth × width stress-distribution map.
- [[inlay/al-fodeh-2026-monolithic-zirconia-inlays-cement-aging]] — reinforces: corroborates the zirconia-inlay biomechanics theme; here zirconia shows highest internal/cervical stress with tooth-shielding.
- [[inlay/wang-2025-foundation-restoration-onlay-mandibular-molar-endodontic-fea]] — companion FEA on mandibular-molar foundation/onlay stress; supports the >4 mm → onlay/cuspal-coverage rationale.
- [[inlay/griffis-2022-tooth-cusp-preservation-lithium-disilicate-onlay-fatigue]] — relates inlay-vs-onlay/cuspal-coverage decision to fatigue behavior.
