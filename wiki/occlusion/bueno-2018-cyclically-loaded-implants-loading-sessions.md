---
title: "Bone healing response in cyclically loaded implants: Comparing zero, one, and two loading sessions per day"
authors: Renan de Barros e Lima Bueno, Ana Paula Dias, Katia J. Ponce, Rima Wazen, John B. Brunski, Antonio Nanci
year: 2018
date: 2018-05-01
doi: 10.1016/j.jmbbm.2018.05.044
source: bueno-2018-cyclically-loaded-implants-loading-sessions.md
category: [occlusion]
confidence: animal
pdf_path: /Users/oracleneo/llm-wiki/papers/bueno-2018-cyclically-loaded-implants-loading-sessions.pdf
pdf_filename: bueno-2018-cyclically-loaded-implants-loading-sessions.pdf
source_collection: external
tags: []
---

## One-line Summary

Rat tibia animal study (n=27) demonstrating that doubling daily cyclic loading sessions (2× vs 1×, 60 cycles × 1.5 N axial, 7 days) significantly reduces BIC and increases bone-implant distance at the gap interface, while a single session per day is indistinguishable from unloaded controls.

## 한줄요약

쥐 경골 동물 실험(n=27, 3군, 7일)에서 하루 2회 반복 하중군만 BIC 유의 감소·골-임플란트 거리 유의 증가를 보이며, 1회군은 무하중군과 차이 없어 누적 미세동요의 용량 의존적 골치유 악화 효과를 규명하였다.

## Summary

This mechanobiology study (J Mech Behav Biomed Mater 2018, Bueno, Brunski, Nanci et al.) investigated how the number of daily cyclic loading sessions affects bone healing at the implant-bone gap interface using the rat tibia BIGI (Bone Implant Gap Interface) model. Machined screw-shaped cp-Ti implants (1.7 mm diameter) were placed in 2.0 mm holes in rat tibiae, creating a circumferential gap, and secured with a custom bone plate. Three groups (n=9/group) received zero, one, or two daily sessions of 60 cycles at 1.5 N axial force for 7 days.

Histomorphometric analysis at day 7 showed that the 2× loading group had significantly lower bone-to-implant contact (BIC), larger bone-implant distance (BID), and reduced bone formation area close to the implant surface (BFAo) compared to both the 1× and unloaded groups (p<0.05). Critically, the 1× group was statistically indistinguishable from unloaded controls on all measures. This dose-dependent pattern indicates a threshold between 1 and 2 sessions per day at this force level, beyond which cumulative tissue deformation becomes detrimental.

Finite element analysis revealed ~94 μm axial implant displacement in fibrin-filled gaps, with principal compressive strains reaching 60% at thread crests and ~30% beneath the apex. DNA microarray (GeneChip Rat Gene 2.0 ST) showed the inflammatory/immune pathway as predominant across all groups, with heightened expression in the 2× group. Histologically, the 2× group exhibited fibrous connective tissue deposition along the implant surface, and a single case showed fibrocartilage formation at the thread flank — consistent with local compressive/distortional strain patterns from FEA.

The authors conclude that even at a force magnitude that is otherwise "acceptable" in a single daily session, doubling the loading sessions leads to cumulative interfacial tissue damage and an exacerbated inflammatory response that impairs osseointegration.

## Key Contributions

1. **Dose-response for loading frequency**: First direct experimental evidence that daily loading session count — not just peak force — governs early peri-implant bone healing quality at the gap interface.
2. **Threshold identification**: One daily session of 60 cycles at 1.5 N = no significant effect vs. unloaded; two sessions = significant BIC reduction and BID increase. Defines an experimental loading tolerance threshold.
3. **FEA characterization**: Quantifies micromotion (~94 μm axial displacement in fibrin) and strain concentrations at thread geometry, linking mechanical environment to histological outcomes.
4. **Inflammatory mechanism**: Gene expression data implicates immune/inflammatory pathway accumulation as the primary mechanobiological driver of 2×-group impairment, suggesting targeted anti-inflammatory intervention as a future therapeutic direction.
5. **Fibrocartilage as overload marker**: Observation of fibrocartilage in the 2× group, consistent with FEA-predicted strain states, provides a tissue-level histological correlate of mechanical overload.

## Methodology

| Parameter | Detail |
|---|---|
| Animal | Male Wistar rats, 200–225 g, n=27 (9/group) |
| Model | Rat tibia BIGI: 1.7 mm implant in 2.0 mm hole (~0.15 mm gap) |
| Implant | Machined cp-Ti Grade 2 screw, 7 mm × 1.7 mm |
| Groups | Unloaded / Micromotion 1× (60 cyc/day) / Micromotion 2× (120 cyc/day) |
| Force | 1.5 N axial per cycle, ~1 Hz (manual), 7 days |
| Duration | 7 days post-surgery |
| Histomorphometry | BIC, BID, BFAo, BFAt (n=5/group, 3 sections/animal) |
| Molecular | DNA microarray n=4/group; fold-change ≥2, p<0.05 |
| FEA | 3D composite cylinder model, properties varied by tissue type and healing stage |

## Results

### Histomorphometric Outcomes (day 7)

| Outcome | Unloaded | 1× | 2× |
|---|---|---|---|
| BFAo (near-implant bone area) | Reference | = Unloaded (NS) | Significantly lower (p<0.05) |
| BFAt (total trephine area) | Reference | = Unloaded (NS) | = Unloaded (NS) |
| BIC (%) | Reference | = Unloaded (NS) | Significantly lower (p<0.05) |
| BID (mean gap) | Reference | = Unloaded (NS) | Significantly larger (p<0.05) |

- 2× group: fibrous connective tissue layer along implant surface; single case of fibrocartilage
- 1× and Unloaded: trabecular bone deposition in marrow; no significant inflammatory infiltrate

### FEA Results

- Axial implant displacement: ~94 μm in fibrin-filled gap at 1.5 N
- Max compressive strain: ~60% at thread crests, ~30% beneath apex
- Healing tissue stiffening would reduce strain — 2× loading disrupts this self-protective stiffening progression

### Gene Expression

- All groups: inflammatory/immune pathway dominant
- 2× group: heightened inflammatory gene up-regulation vs. other groups
- Unknown gene categories differ across all three groups

## Related Papers

- [[occlusion/implant-occlusion-loading-biomechanics-overview]] — synthesis of implant occlusion biomechanics; this study provides animal-model dose-response evidence for loading frequency thresholds
- [[occlusion/romanos-2003-bone-implant-interface-loading-conditions-monkey]] — histomorphometric comparison of loading effects (monkey model); supports detrimental loading effects at higher loads in primary vs. secondary healing
- [[occlusion/podaropoulos-2016-bone-reactions-progressive-static-load-dogs]] — progressive static load in dogs; complements this cyclic-load study by contrasting static vs. cyclic loading mechanisms
- [[implants/arghami-2021-immediate-early-loading-hydroxyapatite-coated]] — immediate/early loading clinical data; this study provides basic mechanobiology underpinning the biological rationale for loading protocols
