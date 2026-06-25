---
title: "Three-dimensional position changes of unopposed molars before implant rehabilitation: a short-term retrospective cohort analysis"
authors: Anqi Wang, Jie Cao, Haoyun Zhang, Bo Zhang, Gang Yang, Wenjie Hu, Kwok-Hung Chung
year: 2022
doi: 10.1186/s12903-022-02619-y
category: [occlusion]
source_collection: pubmed-text
full_text: true
pmid: "36463135"
pmcid: "PMC9719205"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9719205/
text_path: /Users/oracleneo/llm-wiki/papers/wang-2022-unopposed-molar-overeruption-implant-cbct.txt
text_filename: wang-2022-unopposed-molar-overeruption-implant-cbct.txt
---

## Why Ingested

임상 질문: 대합치가 없는 치아(unopposed tooth)의 정출(overeruption)이 보철 계획에 얼마나 영향을 주는가, 그리고 그 정출이 endo치(실활치) vs 생활치에 따라 달라지는가. 기존 occlusion 카테고리에는 [[occlusion/mao-2024-occlusal-changes-implant-supported-single-crowns]](임플란트 단관의 시간 경과 교합접촉 변화)는 있으나 **대합치 상실 자체로 인한 자연치 정출의 정량 데이터**가 없었다. 본 CBCT 코호트(Wang 2022)는 발치~임플란트 보철 사이 ~9개월 동안 unopposed molar가 평균 0.43 mm(최대 0.75 mm) 정출함을 3D로 측정해 그 공백을 메운다. 정출이 치수 생활력(pulp vitality)이 아니라 치주인대(PDL)·치조골 매개 현상임을 뒷받침하는 근거로도 활용 — 어떤 측정도 endo/vital을 층화하지 않았다.

## One-line Summary

Retrospective CBCT cohort (59 patients, 68 unopposed molars): unopposed molars over-erupted a mean 0.43 mm (max 0.75 mm) and tipped 1.7° buccally within ~9 months between antagonist extraction and implant restoration — overeruption is fastest early and is a true 3D movement (vertical + tipping + rotation).

## 한줄요약

후향적 CBCT 코호트(환자 59명·대합치 없는 대구치 68개): 대합치 발치부터 임플란트 보철까지 약 9개월 사이 대합치 없는 대구치가 평균 0.43 mm(최대 0.75 mm) 정출하고 협측으로 1.7° 경사 — 정출은 초기에 가장 빠르며 수직 이동·경사·회전이 섞인 3차원 움직임이다.

## 1. Document Information

- **Type**: Retrospective cohort study (CBCT superimposition, tooth-level analysis)
- **Journal**: BMC Oral Health 2022;22(1):562 (2022-12-03)
- **PMID**: 36463135 / **PMCID**: PMC9719205
- **DOI**: 10.1186/s12903-022-02619-y
- **Setting**: Dept. of Periodontology, Peking University School and Hospital of Stomatology; cases 2013–2020
- **n**: 59 patients, 68 unopposed molars (target teeth); all patients had periodontitis (69.5% stage 3 grade C)
- **Follow-up**: mean 9.1 months (SD 4.3) between antagonist extraction (T0 CBCT) and pre-restoration (T1 CBCT)

## 2. Key Contributions

1. **3D CBCT superimposition method** for measuring overeruption — captures crown + root + alveolar bone, not just crown landmarks like 2D film/panoramic studies.
2. **Quantifies overeruption within the implant-restoration window (~9 months)**, a gap previous studies (which used 6.9–12 year follow-ups) had not filled.
3. Shows overeruption is a **compound spatial movement**: vertical migration + buccal tipping (1.7°) + rotation, not pure vertical extrusion.

## 3. Methodology and Architecture

- Pre-op CBCT (New Tom 9000) within 3 months before antagonist extraction = T0; post-op CBCT before definitive restoration = T1.
- Mimics 20.0 multi-threshold segmentation (Crown / Root / Alveolar bone) → STL; superimposition by iterative-closest-point best-fit (Geomagic Control 2015) on stable crowns + stable alveolar bone.
- Coordinate system (Chen et al.): Occlusal / Mesio-Distal / Bucco-Lingual planes; z-axis = occlusal direction.
- Parameters: mean overeruption of cusps (OEmean, z-displacement of cusp-tip centroid), maximum overeruption of cusps (OEmax), bucco-lingual & mesio-distal tipping change (cBLT, cMDT).
- Reliability: ICC 0.965 (OEmean), 0.973 (OEmax); Dahlberg error 0.074–0.092 mm. STROBE-compliant.

## 4. Key Results and Benchmarks

- **OEmean = 0.432 mm** (p < 0.001); **OEmax = 0.753 mm** over mean 9.2 months.
- **72.1% of teeth had OEmax < 1 mm**; two upper second molars exceeded 2 mm (largest 2.555 mm in only 9 months).
- **Tipping**: 1.717° buccal on average; 69.1% tipped buccally; 90% within 5°. OEmax predominantly at lingual/palatal cusps.
- No significant difference in overeruption among molar types (one-way ANOVA).
- Negative OE values corresponded to large cBLT (tipping explains apparent "negative" vertical movement).
- Authors infer overeruption is **fastest in the initial period** (0.43 mm in ~9 months here vs ~0.8–0.9 mm over 6.9–12 years in older cohorts).

## 5. Limitations and Future Work

- Small sample; descriptive only — precludes multivariate prediction (age, periodontal parameters could not be modeled).
- **All participants had periodontitis** → overeruption may be larger than in periodontally healthy patients; not generalizable to all unopposed teeth.
- **No stratification by pulp vitality / endodontic status, restoration type, or crown presence** — the paper does not address whether endo-treated vs vital teeth over-erupt differently.
- Short follow-up (≤ ~1 year); only molars studied.

## 6. Related Work

- Craddock & Youngson (Br Dent J 2004): 83% of unopposed posterior teeth over-erupt (0.5–5.4 mm), retrospective cast study.
- Greenstein et al. (2018): narrative review — ~20% of unopposed posterior teeth extrude ≥2 mm; most extrusion minor; second-molar replacement is patient-preference-driven.
- Fujita & Kiliaridis (J Periodontal Res 2009, rat): periodontitis amplifies overeruption of unopposed molars; eruption is PDL/alveolar-bone mediated.
- Denes & Kiliaridis (Int J Prosthodont 2020, rat): young unopposed molars erupt faster (172 µm/day early) than adult; clinical crown height rises.

## 7. Glossary

- **Overeruption / supraeruption (정출, over-eruption)**: occlusal-direction migration of a tooth that has lost its antagonist contact.
- **Unopposed tooth (대합치 없는 치아)**: a tooth with no occluding antagonist in the opposing arch.
- **Tipping (경사)**: angular change of the tooth axis (here predominantly buccal).
- **CBCT superimposition**: registering two CBCT volumes on stable structures to measure 3D positional change over time.
