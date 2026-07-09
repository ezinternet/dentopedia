---
title: "Bibliometric analysis of implant abutment research from 2005 to 2024"
authors: Jingkun Zhang, Guangwei Chen, Jiamin Chen, Youcheng Luo
year: 2026
doi: 10.1016/j.prosdent.2026.03.003
category: [prosthetic-materials]
pdf_path: /Users/oracleneo/llm-wiki/papers/zhang-2026-bibliometric-implant-abutment-research-2005-2024.pdf
pdf_filename: zhang-2026-bibliometric-implant-abutment-research-2005-2024.pdf
source_collection: external
---

## Why Ingested

위키는 지대주(abutment) 기전 근거를 깊게 보유한다 — 나사 예압([[prosthetic-materials/bulaqi-2015-dynamic-nature-abutment-screw-retightening]], [[prosthetic-materials/lee-2025-abutment-screw-design-torque-loss-fatigue]]), 마이크로갭([[prosthetic-materials/angermair-2024-microgap-abutment-displacement-implant-connection]]), 하이브리드 지대주([[prosthetic-materials/sterzenbach-2025-hybrid-abutment-crowns-zirconia-titanium-implants]]), emergence profile([[overviews/abutment-emergence-profile-peri-implant-tissue-overview]]). 그러나 *분야 전체가 어디로 집중되는지*를 보여주는 지도는 없었다. 이 계량서지학(bibliometric) 논문(Zhang 2026)은 WOSCC 2051편(2005–2024)을 매핑해, 위키가 이미 커버하는 abutment 연구 클러스터(sealing material·platform switching·fracture resistance·zirconia·CAD-CAM)와 아직 ingest하지 않은 클러스터를 드러내는 **커버리지 감사(coverage audit)** 도구로 유용하다. 방법론적 형제 논문 [[immediate-implant/socket-shield/fang-2025-socket-shield-ai-bibliometric-analysis]]와 같은 계량서지학 기법을 다른 주제(지대주 전반)에 적용한 것. 임상 효과 근거가 아니라 연구 활동 지형도임을 명확히 한다.

## Three-line Summary

Bibliometric analysis of 2051 implant-abutment publications (Web of Science Core Collection, SCI-EXPANDED, 2005–2024; 1906 articles + 145 reviews) using VOSviewer, CiteSpace, Biblioshiny/bibliometrix, Pajek, and Excel.

Both publications and citations followed quadratic growth (R²=0.998 / 0.985; publication–citation r=0.883, P<.01); the USA led volume (462 pubs, H-index 75, 13 502 citations), São Paulo University led institutional output and Zurich/Bern led citation impact, Canullo and Sailer were the key authors, and IJOMI + JPD were the top journals; themes evolved from titanium/stress distribution (2005–2010) → platform switching/FEA (2011–2019) → zirconia/microbial leakage/stability (2020–2024).

This maps *research activity*, not clinical effectiveness — a surge in zirconia and digital-workflow keywords reflects evolving clinical priorities and persistent uncertainty (e.g., limited long-term zirconia data), NOT established consensus, and must not be read as evidence of what works.

## 세줄요약

계량서지학(bibliometric) 분석: Web of Science Core Collection(SCI-EXPANDED)에서 임플란트 지대주 논문 2051편(2005–2024; 원저 1906 + 리뷰 145)을 VOSviewer·CiteSpace·bibliometrix·Pajek로 매핑.

출판·피인용 모두 2차 함수 성장(R²=0.998/0.985; 상관 r=0.883, P<.01); 미국이 최다(462편, H-index 75, 피인용 13,502), 상파울루대 출판량 1위·취리히/베른대 피인용 임팩트 1위, 핵심 저자는 Canullo·Sailer, 최다 저널은 IJOMI·JPD; 주제는 티타늄/응력분포(2005–2010) → platform switching/유한요소분석(2011–2019) → 지르코니아/미생물 누출/안정성(2020–2024)으로 진화.

이는 *연구 활동*의 지형도이지 임상 효과가 아니다 — 지르코니아·디지털 워크플로우 키워드 급증은 임상 우선순위 변화와 지속되는 불확실성(예: 지르코니아 장기 데이터 부족)을 반영할 뿐 합의가 아니며, "무엇이 효과 있다"는 근거로 읽으면 안 된다.

## 1. Document Information

- **Type**: Bibliometric / scientometric analysis (RESEARCH AND EDUCATION section, J Prosthet Dent).
- **Journal**: The Journal of Prosthetic Dentistry, 2026;136(1):e185–e197 (July 2026).
- **DOI**: 10.1016/j.prosdent.2026.03.003.
- **Affiliation**: Affiliated Stomatology Hospital of Guangzhou Medical University, Guangzhou, PR China.
- **Funding**: Guangdong Province higher-education and medical research grants. No conflict of interest declared.

## 2. Key Contributions

- First comprehensive, **abutment-specific** bibliometric map (prior implant bibliometrics covered overall implants, overdentures, survival/failure, or prosthetic complications — not the abutment as an independent domain).
- Quantifies the field's 20-year trajectory: leading countries, institutions, authors, journals, co-citation clusters, keyword clusters, and citation bursts.
- Identifies the material narrative shift (titanium → zirconia → hybrid) and the digital-workflow surge (CAD-CAM, intraoral scanning, additive manufacturing) as the two dominant thematic currents.

## 3. Methodology and Architecture

- **Database**: Web of Science Core Collection Expanded (WOSCC), Science Citation Index Expanded (SCI-EXPANDED). Searched **February 2025**.
- **Query**: `TS=("implant abutment*")`; initial 2351 records → restricted to 2005–2024, articles + reviews only, English → **2051 publications** (1906 articles, 145 reviews).
- Pilot terms `"prosthetic abutment*"` / `"custom abutment*"` tested; a comparison search retrieved 149 extra records but most were not abutment-focused, so the analysis kept the single standardized term for coherence.
- Two independent screeners (J.Z., G.C.); discrepancies resolved by a third (Y.L.).
- **Software**: VOSviewer v1.6.20 (co-authorship networks); Pajek v5.16 (layout); CiteSpace v6.4.R1 (co-citation, keyword co-occurrence, citation-burst detection, clustering, dual-map overlay; Pathfinder pruning); Bibliometrix v4.3.0 / Biblioshiny (descriptive metrics); Excel v16.76; SPSS v26 (Pearson correlation). Impact indicators from Clarivate JCR 2025.

## 4. Key Results and Benchmarks

**Growth**
- Annual publications rose 23 (2005) → 156 (2023/2024). Cumulative-publication fit y=3.24x²+43.16x−76.95, **R²=0.9977**; citation fit y=9.58x²+158.68x−485.96, **R²=0.9852**. Publication–citation correlation **r=0.8831, P<.01**. Annual growth rate 10.6%.
- Corpus indicators (Biblioshiny): 6312 authors, 3072 author keywords, 29 171 references, 217 sources, 180 single-authored docs; 30.38% international co-authorship; avg 25.2 citations/doc; 5.06 co-authors/doc; average document age 8.21 y.

**Countries (Table 3)** — USA #1: 462 pubs, H-index 75, 13 502 citations, total link strength 383. Then Brazil (311; 6077 cit), Germany (281; 8343 cit), Italy (228; 7055 cit), Spain (179), China (160), Switzerland (146 — highest **avg citation/article 38.52**, via Straumann industry ties), Turkey (119), Republic of Korea (108), Japan (87). USA is the collaboration hub; MCPs rose over time but SCPs still predominate.

**Institutions (Table 2)** — São Paulo University (Brazil) #1 by volume (92 pubs, ~30% of Brazil's output); Zurich (58 pubs, 2959 cit) and Bern (52 pubs, 2351 cit) highest citation impact; New York, Washington, Ohio State (USA); G. d'Annunzio (Italy); Geneva, Complutense Madrid; **Seoul National University (Korea) — 40 pubs, H-index 29**.

**Authors (Table 1)** — Dual-pathway impact: high output (Luigi Canullo, 37 pubs, 1350 cit, link 58) vs high citation influence (Irena Sailer, 31 pubs, **1931 cit**, link 64). Both Switzerland-based. Others: Coelho, Yilmaz, Piattelli (highest link strength 71), Bonfante, Ribeiro, Kern, Revilla-León, Do Nascimento.

**Journals (Table 4)** — Int J Oral & Maxillofacial Implants (259 pubs, IF 1.7 Q3), J Prosthet Dent (207; IF 4.8 Q1), Clin Oral Implants Res (173; IF 5.3 Q1, highest avg 45 cit/article), Clin Implant Dent Relat Res (97), J Prosthodont (85), Int J Prosthodont, Materials, J Oral Implantol, Implant Dentistry, Int J Periodontics Restorative Dent.

**Reference co-citation clusters (Table 5)** — #0 sealing material (mean 2018), #1 fracture resistance (2012), #2 platform switching (2008), #3 abutment selection (2021), #4 mechanical stability (2018), #5 two-piece zirconia (2004), #6 using titanium (2012), #7 platform switching (2014), #8 bacterial leakage (2010), #9 dental prostheses (2014). Citation paths run from #0 sealing material → fracture resistance / platform switching / mechanical stability / bacterial leakage. Strongest reference burst: Jung RE (2008); longest sustained: Canullo L (2010).

**Keyword clusters (Table 6)** — #0 dental implants, #1 fracture resistance, #2 finite element analysis, #3 complication rates, #4 bacterial leakage, #5 translucency, #6 strength, #7 platform switching, #8 titanium implants, #9 implant abutments.

**Temporal theme shift** — Early (2005–2010): titanium implants, stress distribution. Mid (2011–2019): platform switching, finite element analysis. Recent (2020–2024): zirconia abutments, microbial leakage, stability. Strongest historical keyword burst "System" (2005–2013, strength 27.31); recent bursts "zirconia," "stability," "connection," "microbial leakage."

## 5. Limitations and Future Work

- **Maps research activity, not clinical effectiveness.** Keyword prominence (zirconia, digital workflow) reflects evolving priorities and *unresolved uncertainty*, not consensus — authors explicitly note limited long-term zirconia clinical evidence and sparse dynamic-loading mechanical data.
- Single database (WOSCC only) → omits publications indexed elsewhere.
- Standardized single-term query (`implant abutment*`) may miss nonstandard terminology.
- Excludes non-peer-reviewed literature (conference abstracts, theses, patents), which often carry the earliest emerging trends.
- English-only restriction.

## 6. Related Work

- Prior implant bibliometrics: implant-retained overdentures (Borges 2023/2024), industry partnership in implant research (Pereira 2024), international collaboration in oral implantology (Dini 2024), 25 years of clinical implant dentistry (Hsu 2024), implant failure (Khan 2022), prosthetic complications (Khan 2023). This paper is the first abutment-specific one.
- Methodological sibling in this wiki: [[immediate-implant/socket-shield/fang-2025-socket-shield-ai-bibliometric-analysis]].

## 7. Glossary

- **Bibliometric analysis**: Quantitative mapping of a research field's productivity, collaboration, and thematic structure via citation and keyword data.
- **Total link strength (TLS)**: VOSviewer metric of an entity's total co-authorship/co-citation connection weight.
- **Citation burst**: CiteSpace-detected interval of abnormally rapid citation increase for a reference or keyword — a marker of emerging/hot topics.
- **Co-citation cluster**: Group of references frequently cited together, labeled by shared theme (silhouette = cluster homogeneity).
- **SCP / MCP**: Single-Country vs Multiple-Country Publications (collaboration indicator).
- **Platform switching**: Using an abutment narrower than the implant platform to shift the microgap inward and preserve marginal bone.
