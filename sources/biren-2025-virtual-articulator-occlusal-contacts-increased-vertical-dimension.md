---
title: "Evaluation of relative deviations in virtual articulators for simulating occlusal contacts at increased vertical dimensions"
authors: Biren E, Saygılı S, Bilgen B, Sülün T
year: 2025
doi: 10.4047/jap.2025.17.6.339
pmid: "41536754"
pmcid: "PMC12798328"
category: [occlusion]
source_collection: pubmed-text
full_text: true
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12798328/
text_path: /Users/oracleneo/llm-wiki/papers/biren-2025-virtual-articulator-occlusal-contacts-increased-vertical-dimension.txt
text_filename: biren-2025-virtual-articulator-occlusal-contacts-increased-vertical-dimension.txt
---

## Why Ingested

[[complete-denture/satin-2023-occlusal-vertical-dimension-transfer-cad-cam-dentures]]는 CAD-CAM 완전틀니의 OVD(occlusal vertical dimension) 전사 과정에서 체계적 수직 오차가 나타남을 보고했으나, 그 오차가 어느 단계(가상 교합기 자체? 안궁이전?)에서 유입되는지는 다루지 않았다. 본 실험 연구(Biren 2025, n=18, 참가자당 스플린트 8개)는 정확히 그 지점을 통제 실험으로 해부한다 — 가상 교합기(virtual articulator)가 OVD 증가량(2mm/5mm)·방법(교합기/구강내)·가상 안궁이전(virtual facebow) 유무를 조합해 교합접촉의 공간적 편차를 측정, "접촉 개수는 그대로인데 위치는 이동한다"는 반직관적 결과와 "가상 안궁이전이 편차를 줄이지 못한다"는 상업적으로도 중요한 부정적 소견을 보고한다. digital VD workflow의 오차 원인을 좁히는 근거로 satin-2023을 보강.

## Three-line Summary

Prospective within-subject experimental study (18 dentate adults, Angle Class I occlusion, 21 recruited/3 dropped out; each participant received 8 occlusal splints varying OVD increase method [articulator-based vs intraoral], amount [2 mm vs 5 mm], and virtual facebow use [yes/no]) evaluating whether a virtual-articulator workflow reproduces occlusal contacts accurately when the occlusal vertical dimension (OVD) is increased, using Group D (2 mm intraoral increase, no facebow) as the reference baseline.

The number of occlusal contacts was not significantly affected by OVD increase amount, method, or virtual facebow use — but spatial deviations of those same contacts were: no significant X (lateral) deviation, but significant Y (anteroposterior) and Z (superoinferior) deviations in several groups, most pronounced with a 5 mm intraoral increase (Z effect sizes moderate-to-large, d = 0.57–1.20); articulator-based 5 mm increase produced fewer deviations than intraoral, and the virtual facebow did not substantially reduce deviations in any comparison.

Contact count is an insensitive metric that can mask real spatial drift — the same number of contacts land in different places as OVD increases, particularly vertically at 5 mm — and because deviations are measured relative to Group D rather than a validated ground truth, the study quantifies inter-method disagreement, not absolute accuracy.

## 세줄요약

전향적 개체-내(within-subject) 실험 연구(치열 있는 성인 18명, Angle Class I, 21명 모집·3명 탈락; 참가자당 교합 스플린트 8개 — OVD 증가 방법[교합기 vs 구강내] × 증가량[2mm vs 5mm] × 가상 안궁이전(virtual facebow) 사용 여부[유/무] 조합) — Group D(구강내 2mm 증가, 가상 안궁이전 없음)를 기준선으로 가상 교합기(virtual articulator) 워크플로가 수직고경(OVD) 증가 시 교합접촉을 정확히 재현하는지 평가.

교합접촉 개수는 OVD 증가량·방법·가상 안궁이전 사용 여부에 유의한 영향을 받지 않았으나, 같은 접촉점의 공간적 편차는 유의했다 — X(측방) 방향 유의차 없음, Y(전후방)·Z(수직) 방향은 여러 군에서 유의한 편차(특히 구강내 5mm 증가에서 두드러짐, Z방향 효과크기 중간~큼 d=0.57–1.20); 교합기 기반 5mm 증가가 구강내 방식보다 편차가 적었고, 가상 안궁이전은 어느 비교에서도 편차를 유의하게 줄이지 못했다.

접촉 개수는 실제 공간적 이동을 놓칠 수 있는 둔감한 지표다 — OVD가 증가할수록(특히 구강내 5mm·수직 방향) 접촉점 개수는 그대로여도 위치는 이동한다. 모든 편차는 검증된 ground truth가 아니라 Group D 대비 상대값이므로, 이 연구는 절대 정확도가 아니라 방법 간 불일치(disagreement)를 정량화한 것이다.

## 1. Document Information

- **Title**: Evaluation of relative deviations in virtual articulators for simulating occlusal contacts at increased vertical dimensions
- **Authors**: Biren E, Saygılı S, Bilgen B, Sülün T
- **Journal**: Journal of Advanced Prosthodontics, 2025;17(6):339–353 (2025-12-15)
- **DOI**: 10.4047/jap.2025.17.6.339
- **PMID**: 41536754 / **PMCID**: PMC12798328
- **Study type**: Prospective, within-subject experimental (crossover-style, each participant serving as own control across 8 splint conditions)
- **Setting**: Istanbul University Faculty of Dentistry, Dept. of Prosthodontics, Turkey; Istanbul Medipol University Ethics Committee protocol 10840098-604.01.01-E.9705

## 2. Key Contributions

1. **Isolates where digital OVD-increase workflows introduce error.** Rather than just reporting an accuracy number, the factorial design (method × amount × facebow) lets each factor's contribution to occlusal-contact deviation be read separately.
2. **Decouples contact count from contact position.** Number of occlusal contacts was statistically unaffected by any factor — but spatial position (Y and Z) was significantly affected, showing that "same number of contacts" is not the same as "same occlusion."
3. **Directional error pattern matches arc-of-closure mechanics.** No X (lateral) deviation, but Y (anteroposterior) and Z (superoinferior) deviation that grows with OVD increase amount — internally coherent with mandibular rotation about the condylar axis during opening.
4. **Negative finding on virtual facebow.** The virtual facebow (based on Beyron arbitrary hinge-axis points transferred via facial scan) did not significantly reduce deviations in any group comparison — a commercially relevant result given the facebow's entire rationale is to make the arc of closure transferable.
5. **Explicit relative-not-absolute framing.** No group is validated against a ground truth; Group D (2 mm intraoral, no facebow) is a clinically reasoned reference baseline, not a gold standard — the paper measures inter-method disagreement.

## 3. Methodology and Architecture

- **Design**: Prospective, single-center, within-subject (each of 18 participants received all 8 splint conditions), Istanbul University Faculty of Dentistry.
- **Sample size**: G*Power 3.1.9.2, one-tailed test, Cohen's d = 0.8, 80% power, α = .05 → 16 participants needed; 21 recruited to allow for dropout. 3 dropped (2 scheduling, 1 gag reflex during splint placement) → **18 completed** (14 F / 4 M, 18–35 y, undergraduate dental students, Angle Class I occlusion, no missing teeth, no TMD).
- **Baseline records**: Trios 3 wireless IOS (3Shape) — MIP scan bilaterally canine-to-molar ("MIP-0"). OVD increased intraorally with tin foil (Gerber Resilience Test technique), folded to 2.0 ± 0.05 mm or 5.0 ± 0.07 mm (verified with digital caliper, minimal post-load compressibility <0.1 mm), placed symmetrically under first-premolar buccal cusps → scanned as MIP-2 and MIP-5.
- **Facial scan / virtual facebow**: AFT System One (Bellus3D Face Camera Pro + intraoral transfer fork stabilized with PVS putty); Beyron's arbitrary hinge-axis points marked bilaterally on skin; 3 repeat scans per participant for quality; transfer fork also scanned on a desktop lab scanner.
- **8 splint groups (A–H)**, factorial across method × amount × facebow:

  | Group | OVD method | Amount | Virtual facebow |
  |---|---|---|---|
  | A | Articulator | 2 mm | Yes |
  | B | Articulator | 2 mm | No |
  | C | Intraoral | 2 mm | Yes |
  | D | Intraoral | 2 mm | **No — reference/control baseline** |
  | E | Articulator | 5 mm | Yes |
  | F | Articulator | 5 mm | No |
  | G | Intraoral | 5 mm | Yes |
  | H | Intraoral | 5 mm | No |

- **Design/fabrication**: Exocad 2.4 OS design module; models mounted on Artex CR semi-adjustable virtual articulator (dynamic occlusion features disabled — average values used, to isolate the facebow's static-occlusion effect). Articulator-based groups (A/B/E/F) opened the incisal pin from the MIP-0 baseline; intraoral groups (C/D/G/H) transferred the tin-foil MIP-2/MIP-5 records directly. Splints: 0.1 mm offset, 1 mm minimum wall, 3D-printed (Formlabs Form 2, Dental LT Clear Resin), QC-inspected before and after post-processing.
- **Contact recording**: CR contacts (bilateral manipulation, deprogrammed) marked with 40-µm blue Artifol; MIP contacts (unguided closure) marked with 40-µm red Artifol; contact points counted and photographed. Scannable PVS bite material (Occlufast Rock) applied after a 5-minute deprogramming period, then scanned (TRIOS 3) and exported as STL.
- **Superimposition/analysis**: Geomagic Control X; all splints oriented in common X/Y/Z; Group D used as control for global best-fit registration (10,000-point alignment) against each test group; color-coded deviation maps (max 0.1 mm, critical 0.01 mm). For each subject, the most prominent occlusal contact landmark on teeth 4–7 (bilateral) was measured in X (lateral), Y (anteroposterior), Z (superoinferior); values averaged across the 8 posterior teeth per subject before statistics. Single calibrated examiner; reproducibility confirmed on a subset before proceeding to single measurements.
- **Statistics**: SPSS 25.0. Friedman test for omnibus group differences; Wilcoxon signed-rank post-hoc with Bonferroni correction (28 pairwise comparisons → adjusted α < .0018). Spearman's rho for correlations. Cohen's d effect sizes (small 0.2 / medium 0.5 / large 0.8).

## 4. Key Results and Benchmarks

- **X-direction (lateral)**: No significant differences among groups (p > .05). Group F smallest deviation, Group H largest; effect sizes negligible (d = −0.10 to 0.05 vs. control) → minimal clinical impact.
- **Y-direction (anteroposterior)**: Significant differences among groups. Group C smallest Y-change, significantly different from Group G (largest anterior deviation; negative mean indicates Group G's contact shifted slightly posteriorly relative to control). Most effect sizes small (d < 0.3) except Groups G (d = 0.49) and H (d = 0.45), which were moderate.
- **Z-direction (superoinferior)**: Significant differences among groups. Group C least deviation (moderate effect, d = 0.77, relative to control), Group F medium effect (d = 0.57), Groups G and H large effects (d > 1.1) — the largest deviations recorded overall.
- **Smallest-deviation group**: Group C (2 mm intraoral + facebow) — 0.014 mm mean Y-deviation, 0.031 mm mean Z-deviation from control.
- **Largest-deviation group**: Group G (5 mm intraoral + facebow) recorded the highest absolute Z-deviation (0.466 mm); its non-facebow 5 mm intraoral counterpart was comparable (0.438 mm) — i.e., adding the virtual facebow did **not** meaningfully reduce the deviation.
- **Contact count (CR and MIP)**: Friedman test showed **no significant difference in the number of occlusal contacts** among any of the 8 groups (p > .05), and no significant correlation between deviation magnitude (any direction) and number of contacts — deviations and contact counts are independent phenomena.
- **Clinical thresholds cited**: AAO-defined clinically acceptable threshold < 0.5 mm; other literature cites deviations < 1 mm as non-critical. Observed deviations were generally within these bounds, but the consistent moderate-to-large Z-direction effect sizes at 5 mm were flagged as the clinically relevant exception.
- **Comparator literature cited in Discussion**: Morneburg & Pröschel reported articulator-based 2 mm OVD increase → up to 0.4 mm occlusal deviation in premolars/molars; 4 mm → 0.3–0.8 mm deviation in 44% of cases.

## 5. Limitations and Future Work

- **No absolute accuracy claim** — no objective gold standard existed; all deviations are relative to Group D (a clinically reasoned, not validated, baseline). Findings describe inter-group/inter-method disagreement, not ground-truth error.
- **Flat-surfaced occlusal splints** (not tooth-morphology surfaces) were used due to CAD software limitations — may have limited the assessment of the virtual facebow's full effect, since the facebow's rationale (transferring cusp-tip-to-condyle distances) is most relevant to cusp-fossa relationships that flat splints don't replicate.
- **Virtual facebow used average/arbitrary Beyron hinge-axis points**, not a true kinematically-recorded axis — reported literature cites 4–6° condylar-parameter deviation without true kinematic registration, which can produce clinically significant anteroposterior discrepancy at higher OVD increases.
- **Static occlusion only** — dynamic articulator features were deliberately disabled; digitally recorded contacts represent static relationships and may not generalize to mastication/parafunction.
- **Single intraoral scanner (TRIOS 3)** for reference acquisition — laboratory scanners generally offer superior full-arch trueness/precision; chosen for clinical-workflow relevance, not maximum accuracy.
- **Single-point contact selection per tooth** by one examiner — reproducibility confirmed on a subset only, no formal ICC analysis; per-subject deviation values were averaged across the 8 posterior teeth, which may obscure tooth-specific patterns.
- **Homogeneous sample** — young (18–35y), dental-student, Angle Class I, no TMD, minimal occlusal wear population. Explicitly not generalizable to Angle II/III, TMD, or edentulous/complete-denture VD-determination populations.
- **Future work suggested**: button-like markers scanned at multiple mandibular opening positions as an alternative to kinematic facebow; tooth-level (rather than averaged) deviation analysis; ICC/region-of-interest reproducibility testing; dynamic occlusal simulation; diverse clinical samples (TMD, developmental anomalies).

## 6. Related Work

- **Abdu** — a 5 mm OVD increase does not cause significant/irreversible condylar-position changes, supporting biomechanical safety of increases up to 5 mm.
- **Inoue** — no significant vertical differences at premolar gingival margins across 0/3/5 mm OVD increases on a virtual articulator — aligns with this paper's conclusion that up to 5 mm is clinically acceptable for anatomically healthy patients.
- **Morneburg & Pröschel** — articulator-based OVD increases (2 mm, 4 mm) produce measurable occlusal deviation (0.3–0.8 mm in a substantial proportion of 4 mm cases), underscoring hinge-axis accuracy as the limiting factor.
- **Revilla-León** — maxillomandibular records at 2–3 mm interocclusal gap show better trueness/precision than records taken at MIP — supports the tin-foil deprogramming approach used for Group D.

## 7. Glossary

- **OVD** — Occlusal vertical dimension.
- **Virtual articulator** — Software-simulated mechanical articulator (here: Artex CR via Exocad) that mounts digital maxillary/mandibular models and simulates mandibular movement/opening.
- **Virtual facebow** — Facial-scan-based transfer of the maxilla's spatial relationship to an (arbitrary/average) hinge axis, replacing an analog mechanical facebow.
- **Beyron point** — Arbitrary/average hinge-axis reference point used when a true kinematic hinge axis is not recorded.
- **CR / MIP** — Centric relation / maximum intercuspal position.
- **Group D** — This study's reference baseline: 2 mm intraoral OVD increase, no virtual facebow. A clinically reasoned control, not a validated ground truth.
- **X / Y / Z directions** — Lateral (mediolateral) / anteroposterior / superoinferior displacement axes, defined by Geomagic Control's best-fit global registration.
