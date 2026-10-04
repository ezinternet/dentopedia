---
title: "The interplay between bone healing and remodeling around dental implants"
authors: Irandoust S, Müftü S
year: 2020
date: 2020-01-01
doi: 10.1038/s41598-020-60735-7
source: irandoust-2020-interplay-bone-healing-remodeling-dental.md
category: implants
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/irandoust-2020-interplay-bone-healing-remodeling-dental.pdf
pdf_filename: irandoust-2020-interplay-bone-healing-remodeling-dental.pdf
source_collection: external
tags: [bone-healing, bone-remodeling, mechano-regulatory-model, implant-micromotion, immediate-loading, computational-modeling, poroelastic, stress-shielding]
---

## Three-line Summary
Computational mechano-regulatory model simulating bone healing (30 days) and remodeling (15,000 days) around immediately loaded implants with controlled initial micromotion (5, 10, 20 μm).
At 5 and 10 μm micromotion, ~95–100% immature/trabecular bone formed by day 30 but 35% resorbed by day 15,000 due to stress shielding; at 20 μm, only 45% bone formed initially with 16% fibrous tissue, and steady-state cortical bone not fully established at 15,000 days.
Implant micromotion during early healing critically determines long-term bone volume and quality — an optimal patient-specific micromotion range exists for desired functional outcomes.

## 세줄요약
메카노-조절 세포분화 모델로 즉시부하 임플란트 주위 골치유(30일)와 골리모델링(15,000일)을 연속 시뮬레이션 — 초기 마이크로모션 5, 10, 20 μm 조건 비교.
5·10 μm에서 30일째 미성숙/해면골 ~95–100% 형성되나 15,000일째 스트레스 실딩(스트레스 차폐)으로 35% 흡수; 20 μm에선 초기 골형성 45%·섬유조직 16%, 피질골 정상상태 미도달.
초기 힐링 단계 마이크로모션이 장기 골용적·질 결정 — 환자 맞춤 최적 마이크로모션 범위 설계 가능성 제시.

## Summary
This computational study used a mechano-regulatory cellular differentiation model to consecutively simulate bone healing (days 1–30) and bone remodeling (up to 15,000 days) around an immediately loaded dental implant with no initial bone-to-implant contact. All tissue types were modeled as poroelastic during healing, with material properties updated after each loading cycle. The study examined three levels of initial implant micromotion (5, 10, and 20 μm) during the healing phase, followed by remodeling under 100 N mastication force. Key findings include: (1) tissue between implant threads consistently differentiates into bone during healing but resorbs during remodeling due to stress shielding regardless of micromotion magnitude; (2) larger micromotion (20 μm) promotes fibrous and cartilaginous tissue formation during healing, reducing initial bone volume; (3) at 15,000 days, total bone tissue volume (trabecular + cortical) was 65%, 63%, and 33% for 5, 10, and 20 μm micromotion respectively; (4) the remaining bone in the 20 μm group developed higher cortical bone density (15% vs 7%), partially compensating for lower overall volume. The authors conclude that an optimal range of initial implant micromotion can be designed per patient to achieve desired long-term functional properties.

## Key Contributions
- First computational model to consecutively simulate both bone healing and bone remodeling phases using a unified mechano-regulatory framework
- Quantified the critical interplay between early healing-phase micromotion and long-term (15,000-day) bone volume and quality outcomes
- Demonstrated stress shielding as the mechanism for thread-region bone resorption during remodeling, independent of initial micromotion
- Provided quantitative benchmarks: 65%/63%/33% long-term bone TV for 5/10/20 μm micromotion, with cortical bone TIC of 10%/10%/8%

## Methodology
Axisymmetric finite element model of a dental implant placed in an osteotomy gap without initial bone contact. Healing phase (30 days): poroelastic tissue model, mechano-regulatory differentiation rules based on solid stimulus (octahedral shear strain) and fluid stimulus (fluid velocity), material properties updated per loading cycle, implant micromotion controlled at 5/10/20 μm. Remodeling phase (15,000 days): bone apparent density adapts toward homeostatic remodeling stimulus under 100 N masticatory load. Outcomes tracked: tissue volume (TV), tissue-to-implant contact (TIC), elastic modulus distribution, solid/fluid stimuli maps.

## Results
| Outcome | 5 μm | 10 μm | 20 μm |
|---|---|---|---|
| **Day 30 — Immature/Trabecular Bone TV** | ~100% | 95% | 45% |
| **Day 30 — Fibrous Tissue TV** | 0% | ~0% | 5% |
| **Day 30 — Cartilaginous Tissue TV** | 0% | 0% | 45.8% |
| **Day 15,000 — Total Bone TV (trabecular + cortical)** | 65% | 63% | 33% |
| **Day 15,000 — Cortical Bone TV** | 7% | ~7% | 15% |
| **Day 15,000 — Fibrous Tissue TV** | 35% | ~35% | 16% |
| **Day 15,000 — TIC (Cortical Bone)** | 10% | ~10% | 8% |

Key mechanistic insights:
- Regions between implant threads experience lowest solid stimulus (shear strain) and lowest fluid velocity → faster initial healing but later resorption (stress shielding)
- High fluid velocity in coronal region (due to low cortical bone permeability) drives soft tissue development
- At 20 μm micromotion, high shear stress on vertical gap sides promotes cartilaginous/fibrous tissue
- Remodeling redistributes bone quality: 20 μm case converts 46% woven/trabecular bone (day 30) to 18% trabecular + 15% cortical bone (day 15,000)

## Related Papers
- [[implants/loading-protocol]] — Loading timing protocols for conventionally placed implants; this paper models the immediate loading scenario
- [[bone-biology/rowe-2023-physiology-bone-remodeling]] — Canonical physiology of bone remodeling stimulus and cellular mechanisms
- [[implants/osseodensification]] — Bone condensing techniques that alter primary stability and initial micromotion environment