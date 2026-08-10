---
title: "Evaluation of the effects of the third molar on distalization and the effects of attachments on distalization and expansion with clear aligners: Three-dimensional finite element study"
authors: Kuguoglu A, Akarsu-Guven B
year: 2024
doi: 10.4041/kjod24.202
category: [orthodontics/clear-aligner]
source_collection: pubmed-text
full_text: true
pmid: "39849968"
pmcid: "PMC11788183"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11788183/
text_path: /Users/oracleneo/llm-wiki/papers/kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea.txt
text_filename: kuguoglu-2024-clear-aligner-attachment-third-molar-distalization-fea.txt
---

## Why Ingested

기존 [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]]가 어태치먼트 일반론(SR)을, [[orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr]]가 FEA 문헌 전체를 종합하지만, **어태치먼트 형태별(수직 사각형·복합 반타원형·대합 반타원형) 직접 비교 + 제3대구치 존재 여부**를 같은 3D FEA 모델 안에서 정량 비교한 단일 논문은 부재했다. 본 Korean Journal of Orthodontics 논문(Kuguoglu 2024)은 대합 반타원형(구협측+구개측) 어태치먼트가 가장 평행한 원심이동을 만든다는 것과, 완전맹출 제3대구치가 원심이동을 10–22% 저해한다는 정량치를 제시해 임상 어태치먼트 선택·발치 판단에 직접 근거를 제공한다.

## Three-line Summary

3D finite-element study (single CBCT/IOS-based adult maxillary model) comparing three attachment designs — vertical rectangular, combined semi-elliptical, opposed (buccal+palatal) semi-elliptical — for maxillary second-molar distalization, with and without simultaneous expansion, and testing the effect of a present erupted third molar.

The opposed semi-elliptical attachment gave the most parallel distal movement (least tipping/rotation, ~75% of the distalization of the other designs); a present third molar reduced maximum total distal displacement by 17% (10–22% at crown points) and increased distopalatal rotation; adding expansion to distalization roughly doubled/tripled distal-buccal displacement but with proportionally more tipping/rotation, especially for the opposed design.

Attachment geometry materially trades off distalization magnitude against parallel (bodily) control — a palatal attachment component reduces unwanted tipping/rotation but a fully-erupted third molar should be factored into distalization planning (slower movement, higher aligner/attachment stress); findings are single-model FEA and require clinical validation.

## 세줄요약

CBCT/구강스캔 기반 단일 성인 상악 모델의 3차원 유한요소해석(Finite Element Analysis, FEA)으로 상악 제2대구치 원심이동(distalization)에서 3가지 어태치먼트(수직 사각형·복합 반타원형·협측+구개측 대합 반타원형) 디자인을 비교하고, 동시 확장(expansion) 적용 여부 및 완전맹출 제3대구치 존재 여부의 영향을 평가했다.

협측+구개측 대합 반타원형 어태치먼트가 가장 평행한 원심이동(최소 경사·회전, 타 디자인 대비 약 75% 이동량)을 보였고, 제3대구치가 있으면 최대 총 변위가 17%(치관점 기준 10–22%) 감소하며 원심구개측(DP) 회전은 증가; 확장을 동시 적용하면 원심·협측 변위가 2–3배 증가하나 특히 대합 반타원형 디자인에서 경사·회전도 비례해 증가.

어태치먼트 형태에 따라 이동량과 평행이동(치체이동) 제어 사이 trade-off가 뚜렷하며, 구개측 요소가 있는 디자인이 원치 않는 경사·회전을 줄이지만 완전맹출 제3대구치가 있으면 원심이동 계획을 더 신중히 세워야 하고(이동 지연, 어태치먼트·아라이너 응력 증가) — 단일모델 FEA 결과로 임상검증이 필요하다.

## 1. Document Information

- **Journal**: Korean Journal of Orthodontics (한국교정학회지) — 2024;55(1):69–81
- **DOI**: [10.4041/kjod24.202](https://doi.org/10.4041/kjod24.202) · PMID 39849968 · PMCID PMC11788183
- **Design**: 3D finite element analysis (in-vitro/computational)
- **Institution**: Department of Orthodontics, Hacettepe University, Ankara, Türkiye (IRB #GO 22/693)
- **Source**: PubMed Central full text (JATS), retrieved via PubMed MCP. According to PubMed / PMC.

## 2. Key Contributions

- First head-to-head FEA comparison of **three attachment geometries** (vertical rectangular, combined semi-elliptical, opposed semi-elliptical) for the **same** maxillary molar distalization + expansion scenario in one model.
- Quantifies the **third-molar effect on distalization**: 10–22% reduced distal displacement at crown points, 17% reduced maximum total displacement, increased distopalatal rotation.
- Shows the **opposed (buccal+palatal) semi-elliptical attachment** yields the most parallel (bodily-like) movement at the cost of ~25% less total distalization magnitude.
- Demonstrates a **tipping/rotation vs. displacement-magnitude trade-off** when combining expansion with distalization — informs staging decisions in complex molar movement cases.

## 3. Methodology

- **Model source**: single 29-year-old adult female patient, CBCT (Hacettepe archives) + iTero Element 2 intraoral scan, superimposed (DICOM + STL); mirrored half-jaw for symmetry.
- **Software**: Materialise Mimics/3-Matic → Ansys SpaceClaim (solid model) → Ansys 19.2 (FEA solver); PDL modeled as 0.25 mm shell; aligner 0.625 mm thick.
- **Attachment dimensions**: rectangular 3×2×1 mm (vertical); combined semi-elliptical Ø2.0×0.8 mm (buccal, opposing flat faces ⊥ occlusal plane); opposed semi-elliptical Ø2.0×0.8 mm (buccal 45° + palatal 135° to occlusal plane).
- **6 models**: I (rectangular), II (rectangular + 3rd molar present), III (combined semi-elliptical), IV (opposed semi-elliptical) — all scenario 1 (0.25 mm distalization only); V (III + 0.50 mm expansion), VI (IV + 0.50 mm expansion) — scenario 2.
- **Boundary/contact**: maxilla fixed at pterygomaxillary suture; frictional contact (teeth↔aligner, aligner↔attachment, 2nd↔3rd molar μ=0.2); bonded contact (teeth↔PDL, bone↔PDL, attachment↔tooth). Transient dynamic, non-linear (geometric/contact/material) analysis.
- **Outcomes**: displacement/rotation at defined cusp/root-apex landmarks (3 planes: buccal tipping, distal tipping, DB/DP rotation); aligner deformation; von Mises stress on teeth/attachment.

## 4. Key Results

| Comparison | Finding |
|---|---|
| Model I vs II (± 3rd molar) | 3rd molar present → distal displacement ↓10–22% (crown points), max total displacement ↓17%, DP rotation ↑, distal tipping ↓ |
| Models I, III, IV (attachment types, distalization only) | Model IV (opposed semi-elliptical) = most parallel movement, least tipping/rotation, ~75% of the distalization magnitude of I/III; Models I & III similar to each other, III showed more DP rotation than I |
| Models V vs VI (+ expansion) | Model VI (opposed) > Model V (combined) in distal/buccal displacement and tipping/rotation; Model VI = highest stress of all 6 models |
| Aligner deformation | Models I/III (no palatal attachment) → more aligner deformation, esp. palatal side; Model IV → deformation concentrated distally, most uniform in scenario 2 (V/VI) |

## 5. Limitations

- **Single-patient FEA model** — no biological variability, no clinical replication; findings are computational, not in-vivo.
- Simulation excludes saliva, chewing forces, soft tissue, and bone metabolism — real intraoral conditions could alter force transmission.
- Third-molar morphology varies (size/shape/position) — a single model cannot capture this variability.
- Only a single time-point (initial force application) simulated — cumulative/long-term effects of third-molar resistance not modeled.
- No comparison against clinical (in-vivo) tracking data for validation.

## 6. Related Work

- [[wiki/orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — general composite-attachment SR; Kuguoglu supplies head-to-head geometric comparison data this SR could not.
- [[wiki/orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr]] — FEA-literature synthesis; Kuguoglu is a primary study feeding this evidence base.
- [[wiki/orthodontics/clear-aligner/bhate-2025-cat-maxillary-molar-distalization-class-ii-sr]] — clinical molar-distalization outcomes SR; Kuguoglu supplies the underlying biomechanical/attachment-design rationale.
- [[wiki/orthodontics/clear-aligner/nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr]] — aligner design/biomechanics context (trimline vs attachment as complementary force-transmission levers).

## 7. Glossary

- **Finite element analysis (FEA)** — computational method simulating stress/displacement in a discretized (meshed) model; used here to predict tooth/aligner/attachment behavior without clinical trials.
- **Composite attachment** — small resin bump bonded to a tooth to give the aligner an active surface to grip and apply directional force/moment.
- **Semi-elliptical (combined vs opposed) attachment** — ellipsoid-based attachment shapes; "combined" = buccal-only opposing flat faces; "opposed" = buccal + palatal components for bilateral force control.
- **Distopalatal (DP) / distobuccal (DB) rotation** — unwanted rotational components of tooth movement in the transverse-sagittal plane, indicating tipping rather than pure bodily translation.
- **Von Mises stress** — a scalar stress metric used in FEA to identify likely sites of material yielding/failure (here: attachment debonding or aligner deformation risk).
- **Pterygomaxillary suture (boundary constraint)** — fixed anatomical reference used to anchor the FEA model, preventing rigid-body movement of the whole maxilla in the simulation.
