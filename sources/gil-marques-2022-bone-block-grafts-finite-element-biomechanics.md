---
title: "A Biomechanical Analysis of the Influence of the Morphology of the Bone Blocks Grafts on the Transfer of Tension or Load to the Soft Tissue by Means of the Finite Elements Method"
authors: Blanca Gil-Marques, Antonio Pallarés-Sabater, Aritza Brizuela-Velasco, Fernando Sánchez Lasheras, Pedro Lázaro-Calvo, María Dolores Gómez-Adrián, Carolina Larrazábal-Morón
year: 2022
doi: 10.3390/ma15249039
category: [bone-regeneration]
pdf_path: /Users/oracleneo/llm-wiki/papers/gil-marques-2022-bone-block-grafts-finite-element-biomechanics.pdf
pdf_filename: gil-marques-2022-bone-block-grafts-finite-element-biomechanics.pdf
source_collection: external
---

## Why Ingested

Part of a recent GBR / wound-closure collection. This finite-element study models how bone-block graft shape (right-angled vs rounded) and suture tension drive soft-tissue displacement and dehiscence risk during split-bone-block regeneration — giving a biomechanical basis for the primary-closure and flap-tension concerns raised in [[suture-wound-closure/marsidi-2020-measuring-forces-suture-techniques-wound-closure]] and [[suture-wound-closure/plonka-2017-flap-designs-flap-advancement-implant-therapy]].

## One-line Summary

Finite-element analysis combining two block-graft designs (right-angled vs rounded) and two suture tensions (0.05 vs 0.2 N): all soft-tissue stress/deformation/displacement increased at 0.2 N; block design did not change transferred stress or deformation, but the right-angled/chamfer design produced ~25% greater mucosal displacement (dehiscence tendency) — so low suture tension and a rounded block are recommended.

## 한줄요약

블록 이식재 형태(직각 vs 라운드)와 봉합장력(0.05 vs 0.2 N)을 조합한 유한요소해석: 0.2 N에서 모든 연조직 응력·변형·변위가 증가했고, 블록 형태는 전달 응력·변형을 바꾸지 않았으나 직각/챔퍼 형태가 점막 변위를 약 25% 더 키워(열개 경향), 낮은 봉합장력과 라운드 형태가 권장된다.

## 1. Document Information

- Type: Finite element analysis (in-vitro / computational biomechanics)
- Journal: Materials (MDPI) 2022; 15(24): 9039
- DOI: 10.3390/ma15249039
- Published 17 December 2022

## 2. Key Contributions

- Presents a novel FEM model to study primary wound closure over **bone-block grafts** (Split Bone Block, SBB, technique) in guided bone regeneration.
- Isolates two independent variables — **block morphology** (right-angled vs rounded) and **suture tension** (0.05 vs 0.2 N) — to predict soft-tissue dehiscence tendency without clinical confounders.

## 3. Methodology and Architecture

- Finite Element Method simulation of the oral mucosa over a block graft on the alveolar ridge during the early (inflammatory) healing phase.
- Two block-graft designs modeled: right-angled (chamfer) and rounded.
- Two suture-tension levels applied: 0.05 N and 0.2 N.
- Outcomes: displacement of the oral mucosa, transferred stress (Von Mises), and soft-tissue deformation.
- Rationale anchored in prior clinical thresholds: De Stavola & Tunkel (2013) found stress <5 g caused no dehiscence tendency; Burkardt & Lang (2009) found 0.01–0.15 N gave lower dehiscence and >0.1 N significantly increased dehiscence.

## 4. Key Results and Benchmarks

- All analyzed variables (displacement, Von Mises stress, deformation) were **greater at 0.2 N** than 0.05 N suture tension.
- **Block design:** no difference in transferred stress or soft-tissue deformation between right-angled and rounded.
- However, **mucosal displacement was ~25% greater for the right-angled/chamfer design** — interpreted as a greater tendency to dehiscence.
- Conclusion: different biomechanical behavior depends on both design and suture tension; the authors recommend **low suture tension and a rounded block design** to minimize dehiscence risk.

## 5. Limitations and Future Work

- Computational model (FEM) — idealized geometry and material assumptions; not a clinical or cadaver validation.
- Two discrete tension levels and two shapes only; physiologic variability not captured.
- Presented as a model framework "for future investigations" — clinical validation needed.

## 6. Related Work

- Cites Khoury & Hanser (2015) Split Bone Block technique, De Stavola & Tunkel (2013), Burkardt & Lang (2009), Jensen & Terheyden (2009) on block morphology and dehiscence.

## 7. Glossary

- **FEM / FEA** — Finite element method / analysis (computational stress modeling).
- **SBB** — Split Bone Block technique (Khoury & Hanser): thin (~1 mm) autologous blocks forming a casing for better vascularization.
- **Von Mises stress** — Scalar combining stress components to predict yielding/failure tendency.
- **Dehiscence** — Wound reopening / loss of primary closure exposing the graft.
- **Chamfer / right-angled design** — Angular block edge; modeled here as higher-displacement/dehiscence-prone.
