---
title: "Relative performance of various biomaterials used for maxillary sinus augmentation: A Bayesian network meta-analysis"
authors: Bálint Trimmel, Noémi Gede, Péter Hegyi, Zsolt Szakács, Gyöngyi Anna Mezey, Eszter Varga, Márton Kivovics, Lilla Hanák, Zoltán Rumbus, György Szabó
year: 2021
doi: 10.1111/clr.13690
category: [sinus-lift/lateral]
source_collection: pubmed-text
full_text: true
pmid: "33230862"
pmcid: "PMC8247032"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8247032/
text_path: /Users/oracleneo/llm-wiki/papers/trimmel-2021-relative-performance-various-biomaterials.txt
text_filename: trimmel-2021-relative-performance-various-biomaterials.txt
---

## Why Ingested

Surveillance hit (bone-graft-material topic): a Bayesian network meta-analysis (NMA) of 34 RCTs that ranks 28 sinus-graft biomaterial subgroups (including composites with autologous bone, platelet concentrates and bone marrow concentrate) by histomorphometric new bone percentage, and reports that autologous bone alone is not the top-ranked graft. This sits in direct tension with [[sinus-lift/lateral/somngam-2025-new-bone-formation-biphasic-calcium]] (NMA in which autograft ranks first) and [[sinus-lift/lateral/thomas-2026-alloplastic-biologic-grafts-sinus-sr]] (SR with autograft highest), and adds a histomorphometric dimension to the survival-only comparison in [[sinus-lift/lateral/del-fabbro-2025-sinus-augmentation-materials-lateral-approach]].

## Three-line Summary
Bayesian network meta-analysis (PRISMA-NMA, PROSPERO CRD42019137740) of 34 RCTs (842 two-stage lateral maxillary sinus augmentations, crestal core biopsy after 5-8 months) ranking 28 biomaterial subgroups by histomorphometric new bone percentage (NB%).
Only 2 of 378 pairwise comparisons were significant (bovine xenograft + bone marrow concentrate [BMC] superior to allograft and to biodegradable copolymer membrane); SUCRA ranked bovine + BMC first (81%), bovine + PRP second (77%), bioactive glass + autologous bone 1:1, nanocrystalline HA in silica gel and bioactive glass 70% each, and autologous bone alone twelfth (57%).
Autologous bone alone was not confirmed as the gold standard at 5-8 months and composites reduce the autograft volume needed, but certainty was low to very low (9 of 34 trials at high risk of bias, 12 subgroups below the optimal information size).

## 세줄요약
베이지안 네트워크 메타분석 (Bayesian Network Meta-Analysis, NMA; PRISMA-NMA, PROSPERO 등록): 측방 접근 2단계 상악동 거상술 (Maxillary Sinus Augmentation, MSA) 무작위 대조 시험 (Randomized Controlled Trial, RCT) 34편, 842개 부위, 5-8개월 치유 후 치조정 코어 생검의 신생골 비율 (New Bone %, NB%)로 28개 이식재 하위군 순위화.
378개 쌍 비교 중 유의한 것은 2건뿐 (이종골 + 골수농축액 (Bone Marrow Concentrate, BMC)이 동종골 및 생분해성 공중합체 막보다 우수); 누적순위곡선하면적 (Surface Under the Cumulative Ranking, SUCRA) 1위 이종골 + BMC 81%, 2위 이종골 + 혈소판풍부혈장 (Platelet-Rich Plasma, PRP) 77%, 자가골 단독은 12위 (57%).
5-8개월 치유 기준 자가골 단독이 표준 (gold standard)임은 확인되지 않았고 복합이식재가 자가골 필요량을 줄일 수 있으나, 근거 확실성은 낮음~매우 낮음 (34편 중 9편 고위험 편향, 12개 하위군이 최적정보크기 미달).

## 1. Document Information
- **Journal**: Clinical Oral Implants Research 2021 (Epub 2020)
- **DOI**: 10.1111/clr.13690
- **PMID / PMCID**: 33230862 / PMC8247032
- **Institution**: not stated in the retrieved text (corresponding group: Trimmel, Hegyi, Szabó et al.)

## 2. Key Contributions
- First Bayesian NMA to rank sinus-graft biomaterials by crestal-core-biopsy NB% in RCTs only, using 28 granular subgroups (processing method and composite composition) rather than broad xenograft/allograft/alloplast classes.
- Separates healing time into early (2-5 mo), normal (5-8 mo) and late (>8 mo) windows; only the 5-8 month window had a connected network.
- Rejects the null hypothesis that autologous bone alone yields the highest NB% at 5-8 months.
- Notes that biomaterial + autologous bone / autologous cell concentrate composites are a feasible way to reduce autograft harvest volume.

## 3. Methodology and Architecture
- **Design**: Bayesian random-effects NMA of RCTs, reported per PRISMA-NMA; protocol registered a priori (PROSPERO CRD42019137740).
- **Databases**: Cochrane CENTRAL, EBSCO, Embase, MEDLINE (PubMed), Web of Science core collection, to 1 October 2019, plus hand search of cited/citing papers.
- **Eligibility**: RCTs of two-stage lateral-approach MSA with autologous bone or biomaterial and histomorphometry on crestal bone core biopsy; one-stage/non-lateral MSA and MSA combined with vertical/horizontal augmentation excluded.
- **n**: 69 studies met criteria; 34 RCTs with 5-8 month healing (842 MSAs) formed the connected network; 28 biomaterial subgroups (42 originally formed).
- **Outcome**: NB% as mean difference with 95% credible interval; SUCRA ranking; node-splitting for consistency; funnel plot and Egger test; elements of GRADE; Cochrane RoB tool. Software: R gemtc/netmeta with JAGS, STATA 16.

## 4. Key Results and Benchmarks
- Risk of bias: low in 5 studies, unclear in 20, high in 9.
- Significant comparisons: bovine xenograft + BMC > biodegradable copolymer membrane, and bovine xenograft + BMC > allograft (albumin-impregnated DFDBA, one RCT); the other 376 comparisons were not significant.
- SUCRA (NB%, 5-8 months): bovine + BMC 81%, bovine + PRP 77%, bioactive glass + AB 1:1 70%, nanocrystalline HA in silica gel 70%, bioactive glass 70%; autologous bone alone 12th (57%).
- Subgroup sizes: bovine xenograft 16 trials/174 MSAs; autologous bone 7 trials/76 MSAs; BCP 7/121; beta-TCP 7/106; allograft 1 trial/12 MSAs; bovine + BMC 3 trials/21 MSAs.
- Consistency: node-splitting p = .48 (beta-TCP vs BCP), .47 (bovine vs BCP), .49 (bovine vs beta-TCP); Egger test p = .138 (no publication bias evidence).
- Certainty of evidence: low to very low for all comparisons (risk of bias, indirectness, imprecision).

## 5. Limitations and Future Work
- Study-level, not patient-level data; most comparisons indirect; potential intransitivity from different residual ridge height and sinus width (often incompletely reported).
- Optimal information size set at 11 MSAs per group (from Nizam 2018); 12 of the biomaterial subgroups did not reach it, so their ranks should be read with great caution; many nodes rest on single RCTs.
- Confounders not controlled: lateral window technique, handling of the lateral wall, membrane coverage, histomorphometric similarity of new bone and residual graft in the autologous bone group.
- Early (<5 mo) and late (>8 mo) healing windows could not be pooled (too few and poorly connected RCTs).
- Authors call for RCTs powered to the optimal information size with a unified biopsy protocol; outcomes other than NB% (implant survival, volume stability) were not assessed.

## 6. Related Work
- Danesh-Sani 2017 (SR of 136 trials) and Starch-Jensen 2018: autologous bone highest NB and lowest residual graft; contrasted with this NMA's inclusion of RCTs with crestal biopsy only.
- Al-Moraissi 2020 (frequentist NMA, 11 pooled classes): autologous bone best only at <6 months, biomaterials similar after longer healing; Trimmel et al. used 28 finer subgroups and excluded lateral biopsy.
- Stumbras 2019 (narrative review, 18 articles): platelet concentrates with biomaterials enhance bone formation.

## 7. Glossary
- **NMA (Network Meta-Analysis)**: synthesizes direct and indirect comparisons across several interventions in one model.
- **SUCRA**: surface under the cumulative ranking curve; 0-100% summary of how likely an intervention is to rank among the best.
- **Credible interval (CrI)**: Bayesian analogue of a confidence interval.
- **BMC (bone marrow concentrate)**: autologous bone marrow cell concentrate mixed with the graft.
- **OIS (optimal information size)**: minimum sample for adequate precision; below it a node is considered imprecise.
- **NB%**: percentage of newly formed bone in a crestal core biopsy of the grafted sinus.
