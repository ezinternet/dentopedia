---
title: "Evaluation of the accuracy, occlusal contact and clinical applications of zirconia crowns using artificial intelligence design versus human design"
authors: Liu CM, Lu TY, Wang CS, Feng SW, Lin YC, Lee SY, Lin WC
year: 2025
doi: 10.1016/j.jds.2025.03.016
category: [occlusion]
source_collection: pubmed-text
full_text: true
pmid: "40654460"
pmcid: "PMC12254778"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12254778/
text_path: /Users/oracleneo/llm-wiki/papers/liu-2025-accuracy-occlusal-contact-zirconia-ai-design.txt
text_filename: liu-2025-accuracy-occlusal-contact-zirconia-ai-design.txt
---

## Why Ingested

The wiki holds AI-in-prosthodontics reviews ([[artificial-intelligence/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry]], [[digital-workflow/najeeb-2025-ai-restorative-dentistry-review]]) that stop at detection/identification accuracy, and zirconia marginal-fit SR+MAs ([[prosthetic-materials/harimkar-2025-zirconia-peek-marginal-fit-cad-cam]]) that compare materials but never the *design* step. This paper is the missing primary head-to-head: technician-free AI-generated crown design vs the same technician's digital design, with occlusal contact and margin-gap numbers on both a standard model and three patients — the exact evidence needed to judge where automation stops and chairside adjustment begins.

→ [[occlusion/liu-2025-accuracy-occlusal-contact-zirconia-ai-design]]

## Three-line Summary

In-vitro model study (mandibular left first molar model; 10 AI-designed vs 10 technician-designed zirconia crowns, same PrintIn DentDesign software) plus a 3-patient / 6-crown clinical pilot, comparing 3D surface accuracy (RMS), proximal contact, occlusal space and margin gap.

Model: AI design was 3.46× lower in STL RMS (13±3 vs 45±3 µm, p=.0047) and ~6.6× lower in scan-file RMS (18±2 vs 120±15 µm, p=.0001); model occlusal space was 1.8× greater with AI (p<.05); model margin gaps were 57–92 µm in both groups (clinical threshold <120 µm).

Chairside, the technician-adjusted digital crowns needed a *smaller* measured space and the AI crowns gave 332–376 µm vs 276–341 µm margin gaps, so neither workflow eliminated occlusal/marginal adjustment — the dentist remains the final adjuster.

## 세줄요약

체외 모델 연구(하악 좌측 제1대구치 모델; 동일 PrintIn DentDesign 소프트웨어로 AI 설계 10개 vs 치과기공사 디지털 설계 10개) + 3명 환자·6개 크라운 임상 예비시험: 3D 표면 정확도 (Root Mean Squared, RMS)·인접면 접촉·교합면 공간 (Occlusal Space)·변연 간격 (Margin Gap) 비교.

모델: AI 설계가 STL 파일 RMS 3.46배 낮음(13±3 vs 45±3 µm, p=.0047), 스캔 파일 RMS 약 6.6배 낮음(18±2 vs 120±15 µm, p=.0001); 모델 교합면 공간은 AI가 1.8배 큼(p<.05); 모델 변연 간격은 양군 모두 57–92 µm(임상 기준 <120 µm 충족).

임상에서는 기공사가 조정한 디지털 크라운의 공간이 더 작았고 AI 크라운의 변연 간격이 332–376 µm vs 디지털 276–341 µm로, 어느 워크플로우도 교합·변연 조정을 없애지 못했다 — 최종 교합 조정은 여전히 치과의사 몫이다.

## 1. Document Information

- **Journal**: Journal of Dental Sciences 2025;20(3):1665–1672 (Original Article; open access, CC BY)
- **DOI**: 10.1016/j.jds.2025.03.016 · **PMID**: 40654460 · **PMCID**: PMC12254778
- **Institution**: Department of Dentistry, Wan-Fang Hospital / School of Dentistry & School of Dental Technology, Taipei Medical University, Taipei, Taiwan (co-authors also Vilnius University, Lithuania and IMU University, Malaysia)
- **Ethics**: Taipei Medical University Joint Institutional Review Board, TMU-JIRB No. N202109061
- **Artifact**: PubMed/PMC full text (`papers/…txt`); no PDF held

## 2. Key Contributions

- First head-to-head of **AI-generated** crown design (margin line and all settings computed by the software's statistical model, **no technician intervention** on margin gap, occlusion or contact) against **human digital** design produced by the *same* dental technician, using the *same* software (PrintIn DentDesign, Printin3D) and the same milled/sintered zirconia workflow.
- Separates two accuracy questions the earlier AI-prosthodontics literature conflates: *reproducibility of the design process itself* (intra-group RMS across 10 repeats) and *agreement between the two design philosophies* (inter-group RMS).
- Adds an occlusal-contact and margin-gap dimension that AI reviews do not report, on both a standard model and **in the mouth** (3 patients, 3 AI + 3 digital crowns, per-patient both designs).
- Documents a **model-to-mouth direction reversal**: AI crowns had more occlusal space on the model, but the digitally designed crowns had less space in vivo and therefore needed *more* intraoral adjustment time.

## 3. Methodology and Architecture

- **Design**: laboratory (in-vitro) design-accuracy comparison + small prospective clinical applicability pilot (not randomized, no blinding reported).
- **Model**: mandibular left first molar full-crown preparation (Nissin Dental study model); identical model and abutment for both groups.
- **Allocation**: 10 AI-designed + 10 digitally designed crowns on the model (n=20); 3 patients × 2 designs = 6 clinical crowns.
- **Software / CAD**: PrintIn DentDesign (Printin, Printin3D, Taoyuan, Taiwan). Digital (control) arm — the same dental technician repeated the design 10 times. AI arm — software computed the design from statistical models, including margin-line setting and modification.
- **Fabrication**: zirconia ST-Color (Upcera, Guangdong, China), milled on Ceramill Motion 2 DNA (Amann Girrbach), densely sintered 1530 °C for 8 h, then staining/glazing. Technicians removed supports and did surface staining/glazing in **both** arms; only the digital arm received technician adjustment of marginal gap, occlusion and contact.
- **Digitization / measurement**: desktop scanner Medit T510; comparison in Medit Compare. Mean RMS of surface deviation computed from STL files and from post-milling scan files (overall surface difference, trueness/agreement). Sagittal slicing used to measure margin gap, prosthesis-to-adjacent-tooth distance (mesial/distal contact) and occlusal height/space.
- **Clinical pilot**: ages 20–70 needing a molar crown due to caries; excluded if the abutment had root canal treatment or severe structural damage, lacked adjacent natural teeth on both sides, or had no opposing dentition. Abutments prepared with ~1.5 mm average reduction. Each participant received both an AI-designed and a digitally designed crown. Intraoral photographs (Galaxy Note20) and periapical radiographs (Bel-Ray II, 70 kVp, 10 mAs) for qualitative assessment.
- **Statistics**: JMP 16; two-way ANOVA with Tukey HSD post-hoc; α=.05. Data as mean ± SD of 10 replicates.

## 4. Key Results and Benchmarks

**Model — surface accuracy (mean RMS, µm)**

| Group | STL file | Scan file | p (within group STL vs scan) |
|---|---|---|---|
| AI design | 13 (±3) | 18 (±2) | .2712 (ns) |
| Digital design | 45 (±3) | 120 (±15) | .0001 |
| p (AI vs digital) | .0047 | .0001 | — |

- Overall surface-difference range across all groups: 13–120 µm.
- Paper's own ratio statement: STL and scan RMS of the AI group were **3.46×** and (Results text) "66-times" lower than the digital group. The Abstract states **3.4× and 6.6×**; those match the table means (45/13 = 3.46; 120/18 = 6.67), so "66-times" is a typographical error in the Results paragraph.
- 3D-accuracy colour maps: AI crowns showed near-uniform green (little difference) inside and on the surface; the main inter-design differences sat on the crown surface.
- The paper also prints an "AI design vs digital design" row of 30 (±4) µm (STL) and 71 (±7) µm (scan), p=.0001 — reported as the pairwise difference between the two designs.

**Model — contacts and margins**

- Proximal/distal edge contact range: 48–52 µm for both designs; **distal** contact of AI crowns significantly greater than digital (p<.05).
- Occlusal space: AI design **1.8× greater** than digital (p<.05); absolute values appear only in Fig. 2C, not tabulated in text.
- Margin gap: 57–92 µm across tooth orientations for both groups; both within the paper's cited clinical requirement of **<120 µm**.

**Clinical pilot (3 patients, 3 AI + 3 digitally designed crowns)**

| Outcome | AI design | Digital design | p |
|---|---|---|---|
| RMS per case (I / II / III) | 202 (±10) / 252 (±13) / 189 (±11) µm | not separately tabulated (range 189–252 µm) | .0001 |
| Mesial contact | −30 to 115 µm | −79 to 4 µm | .0001 |
| Distal contact | −56 to 16 µm | −53 to 23 µm | .0001 |
| Occlusal contact/space | −356 to −141 µm | −184 to 134 µm | .0001 |
| Margin gap | 332 (±32) / 376 (±37) / 366 (±16) µm | 276 (±25) / 341 (±24) / 293 (±18) µm | .0001 |

(Negative values = excessive contact; positive = gap. Table 2 reports one RMS value per case under a heading that compares the two designs, without splitting the groups.)

- Clinical RMS (189–252 µm) was an order of magnitude above model RMS (13–120 µm); the authors attribute this to the uneven natural abutment surface and to positional change of natural teeth over time.
- Qualitative: intraoral photographs showed the AI crown closely resembling the human-designed counterpart in size and morphology, with more colour-distribution difference on buccal and lingual surfaces; radiographs showed no excessive marginal gaps in either group.
- The authors' stated hypothesis (no significant difference between AI and digital design) was **rejected** because spatial design discrepancies existed — yet both designs met clinical thresholds.

## 5. Limitations and Future Work

- **Clinical n=3** (authors' own stated limitation) — the pilot cannot establish general clinical feasibility; the authors call for further clinical validation.
- **Single tooth type, single model, single software build, single technician** — no operator or software generalizability; digital arm is one technician's 10 repeats, so "human" here is one operator, not technicians in general.
- **No blinding, no randomization, no time measurement** — the design-time advantage of AI is asserted from prior literature, not measured here.
- **Internal number inconsistency**: Results text says "3.46- and 66-times"; the Abstract says 3.4× and 6.6×, and Table 1 means (45/13, 120/18) support 3.46× / 6.67×. Treated as a typographical error, the tabulated means are used here.
- **Discussion vs Table 3 inconsistency**: the Discussion states both groups "met clinical requirements, measuring <90 µm in all four dimensions (Table 3)", but Table 3's in vivo margin gaps are 276–376 µm. The <90 µm figure matches the *model* range (57–92 µm). The in vivo margin gaps as tabulated would exceed the <120 µm threshold the paper itself cites, so the model and in vivo fit claims should not be read as interchangeable.
- **Model occlusal-space values are not tabulated** (only the 1.8× ratio and Fig. 2C), so the occlusal finding cannot be checked numerically from the text.
- Comparison isolates "AI design left untouched" vs "technician-adjusted digital design" — clinically realistic, but it means the in vivo differences partly reflect the *absence of any pre-finishing adjustment* in the AI arm rather than the AI algorithm alone.
- No long-term outcome data (survival, fracture, secondary caries, patient-reported comfort) — purely fit/contact/accuracy endpoints.

## 6. Related Work

- **Chau et al.** (cited ref 18) — accuracy and feasibility of AI-designed single-molar prostheses; this study extends it from feasibility to a controlled same-technician, same-software comparison with an in vivo pilot.
- **Ding et al.** (cited ref 19) — 3D-DCGAN crown morphology generation replicating natural tooth morphology/biomechanics; this paper measures fit and contact rather than morphology fidelity.
- **Previous AI-design reproducibility work** (cited ref 20) — asserted time-saving and good reproducibility of AI-designed crowns; this study quantifies reproducibility as intra-group RMS (13 µm AI vs 45 µm human).
- INGEST-note cross-links held in this wiki: [[artificial-intelligence/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry]] (umbrella review, AI primarily on detection/segmentation), [[prosthetic-materials/harimkar-2025-zirconia-peek-marginal-fit-cad-cam]] (zirconia CAD/CAM marginal fit within <120 µm), [[digital-workflow/han-2023-software-automated-tooth-preparation-evaluation]] (automated software assessment of the *preparation* step that precedes crown design).

## 7. Glossary

- **RMS (Root Mean Squared)**: root mean squared deviation between two superimposed 3D surfaces; the paper's primary trueness/agreement metric (mean overall surface difference in µm).
- **Trueness vs precision**: trueness = agreement with a reference surface; precision = repeatability among identical repeats. This paper's intra-group RMS across 10 repeats is effectively a precision measure.
- **STL file**: tessellated surface file exported from the CAD design; "scan file" here refers to the digitized post-milling/sintering crown surface.
- **Occlusal space / clearance**: vertical distance between the restoration's occlusal surface and the opposing dentition; the paper cites an ideal clinical reference of ~460–520 µm and a 40-µm articulating-paper slide test.
- **Margin gap**: vertical discrepancy at the crown–abutment finish line; the paper cites a clinical requirement of <120 µm (and reports <90 µm in all four dimensions on the model).
- **Tukey HSD**: post-hoc multiple-comparison test after two-way ANOVA, controlling family-wise error between group means (used here at α=.05).
