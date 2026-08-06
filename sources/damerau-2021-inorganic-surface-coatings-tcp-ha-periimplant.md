---
title: "A systematic review on the effect of inorganic surface coatings in large animal models and meta-analysis on tricalcium phosphate and hydroxyapatite on periimplant bone formation"
authors: Jeanne-Marie Damerau, Susanne Bierbaum, Daniel Wiedemeier, Paula Korn, Ralf Smeets, Gregor Jenny, Johanna Nadalini, Bernd Stadlinger
year: 2021
doi: 10.1002/jbm.b.34899
category: [implants/surface]
source_collection: pubmed-text
full_text: true
pmid: "34272804"
pmcid: "PMC9292919"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9292919/
text_path: /Users/oracleneo/llm-wiki/papers/damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant.txt
text_filename: damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant.txt
---

## Why Ingested

This is the most direct head-to-head evidence in the wiki for the "SLA/CA/HA 표면처리별 BIC 비교 (surface-treatment-by-BIC comparison)" question that motivated this batch: a systematic review (40 large-animal studies) + meta-analysis (15 studies) comparing tricalcium phosphate (TCP) and hydroxyapatite (HA) coatings directly against **uncoated rough titanium** on bone-to-implant contact (BIC) at three healing time points. It qualifies the wiki's existing CaP/HA-coating narrative — [[implants/surface/yamada-2012-nanopolymorphic-hydroxyapatite-titanium-implant]] found HA coating significantly *increased* BIC over uncoated microroughened titanium at 2 and 4 weeks in a rat model; this meta-analysis, pooling 15 large-animal studies, found HA coating BIC significantly *lower* than uncoated rough titanium at 14 days (−6.94 percentage points, p=.001) and not significantly different thereafter. This is a genuine head-on conflict on the same question (does HA coating beat uncoated rough Ti in early healing?), not merely a different angle — see the `relations:` edge on the wiki page.

## Three-line Summary
Systematic review (40 large-animal studies, dog/goat/sheep/pig, 2003–2016) plus random-effects meta-analysis (15 studies) comparing TCP- and HA-coated titanium implants against uncoated rough titanium reference surfaces on bone-to-implant contact (BIC) at 14 days, 21–28 days, and 42–84 days of healing.

TCP-coated implants showed lower BIC than reference at 14 days (−3.48 pp, NS) and 21–28 days (−0.85 pp, NS), then higher BIC at 42–84 days (+13.79 pp, NS, high variability); HA-coated implants showed significantly lower BIC than reference at 14 days (−6.94 pp, 95% CI −11.18 to −2.70, p=.001) and small non-significant differences later (+1.53 pp at 21–28d, +1.57 pp at 42–84d).

Neither TCP nor HA coating produced a statistically robust BIC advantage over uncoated moderately-rough titanium in large-animal short-term healing — the authors attribute this to the reference surfaces already being roughened (SLA/DAE-type), which may overshadow any osteoconductive benefit from the calcium-phosphate coating chemistry.

## 세줄요약
대형동물모델 40편(개·염소·양·돼지, 2003–2016) 체계적 문헌고찰 + 15편 무작위효과 메타분석 — 삼인산칼슘 (Tricalcium Phosphate, TCP) 및 수산화인회석 (Hydroxyapatite, HA) 코팅 임플란트를 비코팅 거친 티타늄 대조군과 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC)로 14일·21-28일·42-84일 시점 비교.

TCP군은 14일(−3.48%p, 비유의)·21-28일(−0.85%p, 비유의)에 대조군보다 낮았다가 42-84일에 높아졌으나(+13.79%p, 비유의, 변이 큼) 비유의; HA군은 14일에 대조군보다 유의하게 낮음(−6.94%p, 95% CI −11.18~−2.70, p=.001), 이후 21-28일(+1.53%p)·42-84일(+1.57%p) 모두 비유의.

대형동물 단기 데이터에서 TCP·HA 코팅 모두 이미 거친 비코팅 티타늄 대비 통계적으로 견고한 BIC 우위를 보이지 않음 — 저자들은 기준 표면 자체가 이미 조도처리(SLA/DAE류)되어 있어 CaP 코팅의 골전도 이점을 가릴 수 있다고 해석.

## 1. Document Information
- **Journal**: Journal of Biomedical Materials Research Part B: Applied Biomaterials 2022;110(1):157-175 (epub 2021-07-16)
- **DOI**: 10.1002/jbm.b.34899
- **Institution**: University of Zurich (Center of Dental Medicine) and University Medical Center Hamburg-Eppendorf, Germany/Switzerland
- **PMID**: 34272804 / **PMCID**: PMC9292919

## 2. Key Contributions
- First statistical meta-analysis (not just narrative review) of TCP vs HA coating effect on periimplant BIC in large animals, restricted to studies using a *rough* (not smooth/machined) uncoated titanium reference — a stricter, more clinically relevant comparator than prior reviews used
- Three-timepoint framework (T1: 14 days, T2: 21–28 days, T3: 42–84 days) lets the coating-effect trajectory be tracked across early healing rather than a single snapshot
- Explicit finding that surface roughness of the reference surface may overshadow any CaP-coating chemistry benefit — reframes decades of "CaP coating improves osseointegration" literature that mostly compared against smooth/machined controls
- Species-level pattern: dog models tended to favor the uncoated reference surface, while goat/sheep/pig models tended to show a small effect favoring the coated test surface — a confound the authors flag rather than resolve

## 3. Methodology and Architecture
- **Design**: Systematic review (PRISMA-compliant) + random-effects meta-analysis (R, `metafor` package)
- **Databases**: Biosis, Medline (Ovid), Scopus; search period January 2003 – December 2016
- **n**: 4,174 titles → 2,815 after dedup → 40 studies in SR (mean 10.5 animals/study, 66.5 implants/study) → 15 studies in meta-analysis (TCP and HA subgroups)
- **Inclusion criteria**: large animal (dog/goat/sheep/pig), ≥6 systemically healthy animals, English language, inorganic coating vs uncoated titanium reference implant, published 2003–2016
- **Exclusion criteria**: human, rodent, rabbit, in-vitro studies, reviews, defect models, organic-only coatings, smooth/machined (non-rough) reference surfaces
- **Outcomes**: BIC (% points), difference between coated test surface and uncoated rough-titanium reference surface, at T1/T2/T3

## 4. Key Results and Benchmarks

| Coating | Timepoint | BIC difference vs reference | 95% CI | p-value | Significant? |
|---|---|---|---|---|---|
| TCP | 14 days (T1) | −3.48 pp (lower) | −7.62, 0.67 | .1 | No |
| TCP | 21–28 days (T2) | −0.85 pp (lower) | −6.46, 4.77 | .76 | No |
| TCP | 42–84 days (T3) | +13.79 pp (higher) | −1.83, 29.41 | .08 | No |
| HA | 14 days (T1) | −6.94 pp (lower) | −11.18, −2.70 | **.001** | **Yes — favors reference** |
| HA | 21–28 days (T2) | +1.53 pp (higher) | −4.28, 7.34 | .61 | No |
| HA | 42–84 days (T3) | +1.57 pp (higher) | −5.02, 8.17 | .64 | No |

Individual-study outliers: Danna et al. (TCP, +12 pp at 21d, significant) and Junker et al. / Danna et al. (TCP, +38.10 pp / +25.00 pp at 42–84d, significant) favored the coated surface; Abrahamsson et al. (TCP, −9.40 pp at 28d) and Xiropaidis et al. (TCP, −14.10 pp at 56d) favored the reference. HA meta-analysis at T1 rests on only 2 studies (caution flagged by authors). No systematic publication bias detected by funnel plot, except heterogeneity noted in TCP 21–28d and 42–84d groups.

40-study SR breakdown: dog (30 studies), goat (5), sheep (3), pig (1), mini-pig (1); 20 intraoral / 20 extraoral implant sites; mean T1 healing 17.2 days, mean T2 63.4 days, mean T3 113.2 days.

## 5. Limitations and Future Work
- Strict inclusion criteria (rough reference only) limited the meta-analysis pool to 15 studies — small subgroup sizes, especially HA at T1 (n=2 studies)
- High heterogeneity across CPP-coating fabrication methods (plasma spray, ion-beam, sputter, electrostatic deposition) not fully separable in the pooled analysis
- Species heterogeneity (dog vs goat/sheep/pig) confounds the coating-effect estimate — bone turnover rate differs by species and may explain part of the directional split
- Short observation window (2 weeks–3 months) — no data on longer-term (>84 days) coating stability/resorption behavior or biomechanical (not just histomorphometric) performance
- BIC as an outcome does not necessarily track biomechanical fixation; sample preparation/staining/sectioning variability across the pooled studies further limits precision
- Animal-model results may not directly translate to human clinical outcomes

## 6. Related Work
- yamada-2012 (nanopolymorphic HA coating, rat femur): found HA coating *increased* BIC vs uncoated microroughened Ti at 2–4 weeks — opposes this meta-analysis's pooled finding of *lower* HA BIC at 14 days; see `relations:` edge on the wiki page for the contradiction rationale
- bonfante-2012 (plasma-spray ACP vs PSHA, beagle radius): compares two CaP coating chemistries to each other (no uncoated Ti arm), so it does not directly test the same coated-vs-uncoated question this meta-analysis addresses — related by topic (CaP coating characterization) but not a direct comparator
- A different Bonfante et al. 2013 paper (mandibular dog study, not the wiki's bonfante-2012) is itself one of the 15 studies pooled into this meta-analysis and is cited in-text as showing a significant −7.00 pp effect favoring the uncoated reference at 14 days — consistent with this paper's pooled HA-T1 result

## 7. Glossary
- **BIC (Bone-to-Implant Contact)**: histomorphometric percentage of implant surface in direct contact with mineralized bone, no soft-tissue interposition
- **TCP (Tricalcium Phosphate)**: Ca/P ratio 1.5 calcium phosphate ceramic coating; more resorbable than HA, especially the β-TCP allotrope
- **HA (Hydroxyapatite)**: Ca/P ratio 1.67 calcium phosphate ceramic coating; the most common and least resorbable CPP coating
- **CPP (Calcium Phosphate Phase)**: umbrella term for the family of calcium-phosphate-based inorganic implant surface coatings (HA, TCP, and others)
- **Rough (uncoated) titanium reference**: the comparator arm in this meta-analysis — SLA/dual-acid-etched/alumina-blasted-type roughened but non-coated titanium, distinct from smooth/machined reference surfaces used in older CaP-coating literature
