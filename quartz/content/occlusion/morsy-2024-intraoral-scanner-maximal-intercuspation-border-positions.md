---
title: "Recording maximal intercuspation and border positions of the mandible with intraoral scanner using the acquisition software's multi-occlusion function"
authors: Morsy N, Hammad I
year: 2024
date: 2024-08-20
doi: "10.4047/jap.2024.16.4.221"
source: morsy-2024-intraoral-scanner-maximal-intercuspation-border-positions.md
category: [occlusion]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "39221415"
pmcid: "PMC11361818"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11361818/
text_path: /Users/oracleneo/llm-wiki/papers/morsy-2024-intraoral-scanner-maximal-intercuspation-border-positions.txt
text_filename: morsy-2024-intraoral-scanner-maximal-intercuspation-border-positions.txt
tags: [intraoral-scanner, virtual-articulation, multi-occlusion-function, sensitivity-specificity, border-positions, diagnostic-accuracy, mesh-perforation, in-vitro]
relations:
  - type: extends
    target: didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance
  - type: refines
    target: rovira-lastra-2026-articulating-paper-accuracy-occlusal-points
  - type: reinforces
    target: qadeer-2023-occlusal-contacts-maximum-intercuspation-dentate
  - type: reinforces
    target: wang-2024-trueness-three-intraoral-scanners-maximal-intercuspal-position
---

## Three-line Summary

In-vitro accuracy study: full-dentate 3D-printed master casts mounted on a semi-adjustable articulator, marked with 12 µm articulating paper as the reference standard, versus a Medit i700 intraoral scanner (IOS) using the acquisition software's multi-occlusion function to capture nine virtual interocclusal records (VIRs) per position for maximal intercuspation (MIP), protrusive, and left/right lateral mandibular border positions.

Split verdict by diagnostic accuracy (sensitivity / specificity / PPV / NPV): MIP was excellent (100% / 99% / 99% / 100%), protrusive was acceptable (100% / 83% / 86% / 100%), but lateral positions fell below the clinically acceptable minimum (sensitivity ≥70%, specificity ≥90%) — sensitivity only 28% and NPV only 56% (specificity 93%, PPV 79%) — meaning the scanner missed roughly three of every four true occlusal contacts identified by articulating paper in lateral excursion.

Mesh perforations (virtual overlap artifacts) were far larger in lateral VIRs (up to 455 µm) than protrusive (42 µm) or MIP (148 µm), consistent with a posterior tilting effect during virtual articulation when only 3 reference occlusal stops are available — the mechanistic explanation for why the software's best-fit algorithm fails specifically in lateral excursion.

## 세줄요약

시험관내(in-vitro) 정확도 연구: 완전 치열 3D 프린트 모형을 반조절성 교합기(semi-adjustable articulator)에 장착하고 12 µm 교합지(articulating paper)를 기준(reference)으로 삼아, Medit i700 구강스캐너(Intraoral Scanner, IOS)의 다중교합(multi-occlusion) 기능으로 최대교두감합위(Maximal Intercuspation, MIP)·전방운동위(protrusive)·좌우측방운동위(lateral)마다 가상교합기록(Virtual Interocclusal Record, VIR) 9회씩을 채득해 비교했다.

진단정확도(민감도·특이도·양성예측도 PPV·음성예측도 NPV)는 위치별로 **엇갈린 결과**를 보였다 — MIP는 우수(100%/99%/99%/100%), 전방운동은 허용 가능(100%/83%/86%/100%)했으나, **측방운동은 임상 허용 최소기준(민감도 ≥70%, 특이도 ≥90%)에 못 미쳐 민감도 28%·NPV 56%(특이도 93%, PPV 79%)에 그쳤다** — 즉 교합지가 찾아낸 실제 교합접촉의 약 4분의 3을 스캐너가 놓친다는 뜻이다.

메쉬 관통(mesh perforation, 가상 모형 간 겹침 오류)은 측방 VIR에서 최대 455 µm로, 전방운동(42 µm)·MIP(148 µm)보다 훨씬 컸다 — 측방에서는 교합 기준점(SOC)이 3개뿐이라 소프트웨어의 최적맞춤(best-fit) 알고리즘이 후방으로 기울어지는 효과(tilting effect)가 발생하며, 이것이 측방 민감도가 급락하는 기전적 설명이다.

## Summary

According to PubMed, this in-vitro study ([DOI](https://doi.org/10.4047/jap.2024.16.4.221); PMID 39221415; PMCID PMC11361818) tested the accuracy of a specific intraoral-scanner (IOS) software feature — the acquisition software's "multi-occlusion function" — for recording not only maximal intercuspation (MIP), which prior literature had already validated, but also the mandible's protrusive and lateral border positions as virtual interocclusal records (VIRs) for virtual articulation. The multi-occlusion function lets an IOS capture MIP and border-position bite records directly, aiming to replace conventional mechanical mounting on a physical articulator.

The headline result is a **split verdict, not a pass**. Diagnostic accuracy was assessed with four standard measures against an articulating-paper reference marked on the master casts: sensitivity and NPV (ability to detect/not-miss true contacts), and specificity and PPV (ability to avoid introducing false contacts at sites of clearance). For MIP, accuracy was excellent (sensitivity 100%, NPV 100%, specificity 99%, PPV 99%). For protrusive position, accuracy was acceptable (sensitivity 100%, NPV 100%, PPV 86%, specificity 83%). But for lateral positions, specificity (93%) and PPV (79%) remained high while **sensitivity (28%) and NPV (56%) fell well below the clinically acceptable minimum** (the study cites sensitivity ≥70% and specificity ≥90% as the minimum for clinically acceptable registration). In plain terms: in lateral excursion, when the scanner says "no contact," it is right just over half the time, and it correctly flags true contacts only about 28% of the time — it systematically **misses** contacts rather than fabricating false ones. A reader must not come away thinking "IOS records occlusion accurately" without qualification; that is true for MIP and protrusive, but demonstrably false for lateral.

The mechanistic explanation offered is mesh perforation — virtual overlap between the articulated maxillary and mandibular casts, an artifact of the software's best-fit alignment algorithm tilting the casts when too few interocclusal reference stops are available. Perforations reached up to 455 µm in lateral VIRs (only 3 reference SOCs available: canine + first/second premolar on the working side) versus 42 µm in protrusive (6 anterior SOCs) and 148 µm in MIP (9 bilateral posterior SOCs) — fewer reference stops, worse alignment, more missed contacts.

## Key Contributions

- **First formal accuracy quantification of the IOS "multi-occlusion function" across border positions** — sensitivity, specificity, PPV, and NPV calculated separately for MIP, protrusive, and left/right lateral VIRs, not just MIP.
- **Clean split verdict**: MIP and protrusive meet clinically acceptable minimums; **lateral does not**, despite acceptable specificity/PPV — the scanner's failure mode in lateral excursion is *missing* true contacts, not inventing false ones.
- **Mechanistic link to mesh perforation**: lateral VIRs show the largest virtual-cast overlap (up to 455 µm), tied to having only 3 reference occlusal stops versus 6 (protrusive) or 9 (MIP), explaining why fewer reference points degrade the best-fit alignment specifically in lateral excursion.
- **Tightly controlled in-vitro design** (3D-printed master casts, semi-adjustable articulator, locked condylar elements for MIP, custom DuraLay-stabilized incisal tables for protrusive/lateral border paths) isolates the acquisition software's own registration accuracy from clinical confounders — but that isolation is also the study's central limitation (see below).

## Methodology

- **Design**: in-vitro, controlled, repeated-measures (9 VIRs per position) diagnostic-accuracy study; no patients.
- **Master casts**: full-dentate maxillary/mandibular 3D-printed casts, hand-articulated in MIP and mounted on a semi-adjustable articulator (condylar inclination 30°, Bennett angle 15°).
- **Reference standard (articulating paper, not ground truth)**: 12 µm Bausch Arti-Fol marking sites of occlusal contact (SOC) on the master casts for each of 4 positions — MIP (condyles locked, 9 bilateral posterior SOCs), protrusive (custom incisal table along the programmed protrusive path, 6 anterior SOCs), left/right lateral (custom incisal table along the programmed lateral path, 3 SOCs — canine + first/second premolar, working side).
- **Test method**: Medit i700 IOS, multi-occlusion acquisition function, single operator; full-arch scans plus 9 independently captured VIRs per position under a standardized 50 N static load, each producing a separately re-articulated virtual cast pair (STL).
- **Comparison**: reference and virtual SOCs/clearance sites compared in CloudCompare v2.7 via signed nearest-neighbor inter-arch distance (green 0–100 µm = contact, blue <0 µm = mesh perforation, gray >100 µm = clearance) → TP/TN/FP/FN → sensitivity, specificity, PPV, NPV.
- **Reference-standard caveat**: articulating paper is itself an imperfect standard — it is liable to false positives/negatives from variable biting force and saliva; a static load was used here to reduce that limitation, but this study measures agreement against an *imperfect* physical reference, not against a validated ground truth (see [[occlusion/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points]], which independently found articulating paper achieves only ~81% true-positive detection with a ~15% false-positive rate against a scanned-registration reference).
- **Note (source-data-issue, not corrected)**: the published Methods states "specificity = TP/(TP+FP)," textually identical to its own PPV formula; the standard definition is TN/(TN+FP). The reported Results values are internally distinct (e.g. lateral specificity 93% ≠ lateral PPV 79%), so the error appears confined to the formula listing, not the numbers reported.

## Results

| Position | Sensitivity | Specificity | PPV | NPV | Verdict |
|---|---|---|---|---|---|
| MIP | 100% | 99% | 99% | 100% | Excellent — exceeds acceptable minimums |
| Protrusive | 100% | 83% | 86% | 100% | Acceptable — meets minimums |
| Lateral (L & R) | **28%** | 93% | 79% | **56%** | **Below acceptable — misses ~72% of true contacts** |

- **Mesh perforation (virtual overlap, µm)**: MIP up to 148; protrusive up to 42; **lateral up to 455**, concentrated at the last molars (posterior tilting effect).
- Findings align with prior reports that IOS VIRs are generally accurate but can miss contacts (Abdulateef), and that fewer interocclusal reference points reduce virtual-articulation accuracy (Arslan) — this study is the first to quantify that relationship specifically for *dynamic* (border-position) IOS registration.

## Related Papers

- [[occlusion/didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance]] — extends: didier found poor IOS-occlusogram-vs-carbon-paper agreement (κ 0.07–0.20) but tested only MIP with a single agreement metric; this in-vitro study adds formal diagnostic-accuracy metrics across MIP, protrusive, and lateral, showing the same "IOS alone is not sufficient" conclusion generalizes to dynamic border positions — and that MIP itself, tested here with a cleaner in-vitro protocol, is actually highly accurate.
- [[occlusion/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points]] — refines: this study's own reference standard (articulating paper) is independently shown to have ~81% sensitivity and ~15% false-positive rate against a scanned reference, meaning this paper's reported IOS accuracy is agreement against an imperfect standard, not against true ground truth.
- [[occlusion/qadeer-2023-occlusal-contacts-maximum-intercuspation-dentate]] — reinforces: systematised review of MIP occlusal-contact counts and recording-method reliability; consistent with this study's finding that MIP is the position most reliably recorded, whether by conventional or digital means.
- [[occlusion/wang-2024-trueness-three-intraoral-scanners-maximal-intercuspal-position]] — reinforces: clinical (n=10) trueness study finding three different IOS systems comparable to conventional facebow + bite-registration mounting for MIP specifically; corroborates this study's MIP-is-excellent finding from a clinical rather than in-vitro angle.
