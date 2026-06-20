---
title: "Incidence of sinus membrane perforation in transcrestal graftless maxillary sinus augmentation: a meta-analysis"
authors: Huang ZC, Wang XL, Jin QQ, Chen ML, Zhao YQ
year: 2026
doi: 10.2340/aos.v85.46021
category: [sinus-lift/transcrestal]
source_collection: pubmed-text
full_text: true
pmid: "42240171"
pmcid: "PMC13241954"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13241954/
text_path: /Users/oracleneo/llm-wiki/papers/huang-2026-graftless-transcrestal-sinus-membrane-perforation-ma.txt
text_filename: huang-2026-graftless-transcrestal-sinus-membrane-perforation-ma.txt
---

## Why Ingested

Quantifies the Schneiderian membrane perforation rate specific to **graftless** transcrestal sinus elevation — a complication endpoint that osseodensification-focused syntheses like [[sinus-lift/transcrestal/starch-jensen-2025-transcrestal-sinus-osseodensification-meta-analysis]] report less cleanly. It reinforces the favourable safety profile of graftless transcrestal techniques while flagging a critical technique-dependent exception (motor-driven OD), and it directly contextualizes the single-cohort 7.2% perforation finding of [[sinus-lift/transcrestal/mazor-2024-maxillary-sinus-membrane-perforation-osseodensification]] within a 14-study pooled estimate.

## One-line Summary

SR+MA (14 studies, 2119 graftless transcrestal sinus-lift sites): pooled Schneiderian membrane perforation incidence 1% (95% CI 0–6%), early implant failure ≤12mo 1%, no postoperative sinusitis/epistaxis; subgroup shows motor-driven OD 34% perforation vs conventional osteotome 0% (GRADE very low).

## 한줄요약

SR+MA (14편, 무이식 경치조골 상악동거상 부위 2119곳): 슈나이더막 천공 발생률 통합 1% (95% CI 0–6%), 12개월 내 조기 임플란트 실패 1%, 술후 부비동염·비출혈 보고 없음. 단 모터구동 골밀도화(OD) 34% 천공 vs 전통 osteotome 0%로 술식 의존성 큼 (GRADE 매우 낮음).

## 1. Document Information

- **Title**: Incidence of sinus membrane perforation in transcrestal graftless maxillary sinus augmentation: a meta-analysis
- **Authors**: Huang ZC, Wang XL, Jin QQ, Chen ML, Zhao YQ
- **Journal**: Acta Odontologica Scandinavica 2026;85:311–320
- **Year**: 2026 (e-pub 2026-06-04)
- **DOI**: 10.2340/aos.v85.46021
- **PMID**: 42240171 | **PMCID**: PMC13241954
- **Study type**: Systematic review + meta-analysis (PRISMA 2020)

## 2. Key Contributions

- First meta-analysis to isolate Schneiderian membrane perforation incidence in **graftless** transcrestal (crestal) maxillary sinus floor elevation, excluding grafted and lateral-window procedures.
- Pooled Schneiderian membrane perforation incidence **1% (95% CI 0–6%)** across 14 studies / 2119 sites (raw count 95/2119 = 4.48%).
- Identifies **surgical technique** as the dominant driver of perforation heterogeneity (explains 66.9% of between-study variance), not residual bone height (RBH) — motor-driven osseodensification (OD) 34% perforation vs conventional OSFE 0%.
- Confirms favourable secondary outcomes: early implant failure ≤12 months pooled **1%** (95% CI 0–6%), and **no** reported postoperative complications (acute sinusitis, epistaxis).

## 3. Methodology and Architecture

- **Design**: Systematic review + random-effects meta-analysis; PRISMA 2020.
- **Databases**: PubMed, Embase, Cochrane (CENTRAL), Web of Science, Scopus — inception to May 2025; English only; hand-search of references.
- **Eligibility**: Adults undergoing graftless transcrestal sinus floor elevation (OSFE, OD-TSFE, MISE); RCTs, prospective/retrospective cohorts; ≥10 sinus-lift sites in the graftless arm. Excluded: bone grafting, lateral window, animal/cadaveric, paediatric/mixed.
- **Unit of analysis**: site (bilateral = 2 sites); only graftless arms extracted from multi-arm studies.
- **Outcomes**: primary = Schneiderian membrane perforation; secondary = early implant failure (≤12 mo) and postoperative complications (acute sinusitis, epistaxis).
- **Statistics**: R `meta` package; random-effects with Freeman–Tukey double-arcsine transformation; heterogeneity by Cochran Q + I²; subgroup (design, technique, follow-up), meta-regression (RBH, technique, year), Egger test, trim-and-fill, leave-one-out sensitivity.
- **RoB**: Cochrane RoB 2.0 (RCTs), ROBINS-I (non-randomised) — all 14 studies rated low risk.
- **Certainty**: GRADE — rated **very low** for primary and secondary outcomes (heterogeneity, imprecision, indirectness).

## 4. Key Results and Benchmarks

- **Included**: 1820 records → 14 studies (4 RCTs + 10 non-randomised cohorts), published 2012–2024; 1370 patients, **2119 crestal sinus-lift sites**.
- **Technique mix**: OSFE 10/14; OD-TSFE 1; motor-driven/MISE 2; ISFE 1. Mean pre-op RBH 2.4–7.4 mm; 28.5% of sites RBH ≤5 mm. Follow-up 0 mo–10 y (median 24 mo).
- **Primary — Schneiderian membrane perforation**: pooled **1% (95% CI 0–6%)**; raw 95/2119 (4.48%); I²=80.6%. 95% prediction interval 0–6%.
- **Secondary — early implant failure ≤12 mo**: pooled **1% (95% CI 0–6%)**, 711 implants, I²=0% (no heterogeneity). Highest individual: Si 7.3%, Alzoubi 10.3%.
- **Secondary — postoperative complications**: **none reported** (no acute sinusitis, no epistaxis) across the included literature.
- **Subgroup by design**: prospective 4% (0–24%), retrospective 1% (0–17%), RCTs 0% (0–1%) — not a significant moderator (p=0.592).
- **Subgroup by technique** (significant, p<0.001): conventional **OSFE 0%** (0–4%), **motor-driven OD 34%** (18–54%), OD-TSFE 7%, MISE 0%.
- **Subgroup by follow-up**: ≤12 mo 1% vs >12 mo 1% — no difference (p=0.750).
- **Meta-regression**: RBH non-significant (β=−0.0064, p=0.760, R²=0%); technique categorical model optimal (AIC −13.2, R²=66.9%); MISE and OSFE independently associated with reduced perforation.
- **Publication bias**: no asymmetry for perforation or implant failure (Egger p>0.05; trim-and-fill imputed 0 studies); funnel plot for overall complications asymmetric (caution — true rate may be higher).

## 5. Limitations and Future Work

- High heterogeneity (I²=80.6%) and **GRADE very low** certainty for all outcomes; few events for secondary endpoints.
- RBH categorisation often based on cohort mean (misclassification risk at thresholds).
- Variable follow-up and inconsistent reporting of secondary outcomes; possible publication bias for complications.
- Newer protocols (motor-driven OD, OD-TSFE) under-represented (<3 studies for some subgroups) → wide CIs.
- Authors note sinus width (Stacchi et al.: ~15× higher perforation in wide vs narrow sinuses) and membrane thickness as anatomical predictors not captured here; recommend CBCT-based pre-op width assessment and standardised multicentre RCTs.

## 6. Related Work

- Starch-Jensen et al. 2025 — transcrestal sinus osseodensification meta-analysis (osseodensification-focused crestal synthesis).
- Mazor et al. 2024 — single-cohort OD-TSFE perforation study (18/249 = 7.2%) included in this MA.
- Stacchi et al. 2022 — transcrestal sinus complications at low RBH; sinus width as perforation predictor.

## 7. Glossary

- **OSFE** — osteotome sinus floor elevation (Summers technique; manual malleting).
- **OD-TSFE** — osseodensification transcrestal sinus floor elevation (Densah burs).
- **Motor-driven OD** — motor-driven crestal lift/osseodensification (high-speed counterclockwise, 1100 rpm bouncing).
- **MISE** — minimally invasive sinus elevation.
- **RBH** — residual (sub-antral) bone height.
- **Schneiderian membrane** — the sinus mucosal lining elevated during sinus augmentation.
- **GRADE** — Grading of Recommendations Assessment, Development and Evaluation.
