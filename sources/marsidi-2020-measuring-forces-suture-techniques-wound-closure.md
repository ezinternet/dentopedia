---
title: "Measuring Forces in Suture Techniques for Wound Closure"
authors: Nick Marsidi, Sofieke A.M. Vermeulen, Tim Horeman, Roel E. Genders
year: 2020
doi: 10.1016/j.jss.2020.05.033
category: [suture-wound-closure]
pdf_path: /Users/oracleneo/llm-wiki/papers/marsidi-2020-measuring-forces-suture-techniques-wound-closure.pdf
pdf_filename: marsidi-2020-measuring-forces-suture-techniques-wound-closure.pdf
source_collection: external
---

## Why Ingested

Part of a focused collection on suture techniques & primary wound closure (suture-biomechanics sub-batch). This bench study quantifies the pulling force required by five common suture techniques in a standardized high-tension wound model, providing the force baseline that pairs with strength/tension-dispersion data in [[suture-wound-closure/knoell-2011-basic-lattice-stitch-quantitative-efficacy]] and [[suture-wound-closure/look-2022-novel-superficial-suture-pattern-tensile-strength]]. It informs intraoral flap-closure technique selection alongside [[suture-wound-closure/pabst-2024-cyanoacrylate-tissue-adhesive-coronally-advanced-flap]].

## One-line Summary

Ex-vivo biomechanical bench study (5 suture techniques × 10 reps × 3 operators on a 5 N standardized neoprene wound model): the pulley suture required the least pulling force (3.46 N) to close a high-tension wound vs single (5.69 N), vertical mattress (7.25 N), and horizontal mattress (8.11 N, highest).

## 한줄요약

생체외 역학 벤치 연구 (5가지 봉합법 × 각 10회 × 술자 3명, 5 N 표준화 네오프렌 창상 모델): 풀리 봉합(pulley suture)이 고장력 창상을 닫는 데 필요한 견인력이 가장 낮았고(3.46 N), 단순봉합(5.69 N)·수직매트리스(7.25 N)·수평매트리스(8.11 N, 최고)보다 적었음.

## 1. Document Information

- Journal: Journal of Surgical Research, November 2020, vol 255, pp 135-143
- DOI: 10.1016/j.jss.2020.05.033 (open access, CC BY-NC-ND)
- Affiliations: Dept. of Dermatology, Leiden University Medical Center; Dept. of Biomechanical Engineering, TU Delft, Netherlands
- Study type: ex-vivo standardized-model biomechanical study (suture-force quantification)

## 2. Key Contributions

- First quantitative comparison of the **pulling force** required by five suture techniques (single interrupted, vertical mattress, horizontal mattress, pulley, modified pulley) in a standardized high-tension wound model.
- Demonstrates the pulley suture is mechanically the most "efficient" — closes the same 5 N wound defect with the least applied force, implying less surgeon effort and potentially less risk of edge ischemia from overtightening.
- Provides a validated force-measurement methodology (ForceTRAP platform + Hook-in-Force sensor).

## 3. Methodology and Architecture

- **Wound model:** Standardized neoprene pad (9.5 × 9.5 cm, 3.5 mm thick), laser-cut elliptical 2 cm defect, 30° wound-edge angle (width 3.14 mm). Mounted in a ForceTRAP-modified rig pretensioned to **5 N ± 0.1** to mimic a high-tension wound (e.g., scalp/lower leg).
- **Hardware:** ForceTRAP system (MediShield, Delft) measures forces 0-20 N in three dimensions (accuracy 0.1 N) — captures change in wound tension on the skin substitute. Hook-in-Force (HiF) sensor (TU Delft), working range 0-15 N, accuracy 0.5 N — measures pulling force in the suture strand during the first throw.
- **Suture material:** Ethilon 3-0 monofilament nylon (Ethicon) for every technique.
- **Operators:** medical student, dermatology resident, and expert dermsurgeon — each repeated all 5 techniques 10 times (new suture + new pad each rep).
- Software: two MATLAB user interfaces (TU Delft) logging at minimum 30 Hz.
- Single interrupted entry 4 mm from edge, exit 4 mm opposite; vertical mattress = far-far-near-near; other techniques per standard descriptions.

## 4. Key Results and Benchmarks

Mean maximum pulling force (HiF) ± SD:

| Technique | Mean max pulling force (N) | SD |
|---|---|---|
| Pulley | 3.46 | 0.61 |
| Modified pulley | 4.52 | 0.67 |
| Single interrupted | 5.69 | 0.88 |
| Vertical mattress | 7.25 | 1.33 |
| Horizontal mattress | 8.11 | 1.00 |

- Mean force increase transmitted to the skin substitute ranged 0.80 N (pulley) to 0.96 N (vertical mattress) — a narrow band, i.e. all techniques delivered similar tension to the wound edges despite very different pulling forces.
- Conclusion: the **pulley suture requires the least pulling force** to close a high-tension wound; mechanical properties should factor into technique choice.

## 5. Limitations and Future Work

- Neoprene skin substitute, not human/animal tissue — does not capture viscoelastic creep, tissue tearing, or vascular response of real skin.
- Only the first-throw pulling force was measured; knot security and long-term tension decay not assessed.
- No clinical/healing endpoints (dehiscence, necrosis, scar) — mechanical inference only.
- Operator posture standardized "as good as practically possible" but human variability remains.

## 6. Related Work

- Builds on prior ForceTRAP/Hook-in-Force validation work (refs 13-14 in paper) for surgical-skill force measurement.
- Companion to dermatologic suture-strength literature (Knoell lattice stitch; cadaveric tensile-strength studies).

## 7. Glossary

- **Pulley suture:** a tension-relieving interrupted variant in which the strand loops back through the tissue, creating a 2:1 mechanical advantage that reduces the pulling force needed.
- **Modified pulley:** a variant of the pulley suture tested here (force 4.52 N).
- **ForceTRAP:** validated 3D force-measurement platform (0-20 N) used for surgical-skills training/assessment.
- **Hook-in-Force (HiF):** force sensor (0-15 N) measuring tension in the suture strand.
- **High-tension wound:** wound where edge tension after excision is high (e.g., scalp, lower leg); modeled here as 5 N.
