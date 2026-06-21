---
title: "Effectiveness of deep dry needling versus manual therapy in the treatment of myofascial temporomandibular disorders: a systematic review and network meta-analysis"
authors: Menéndez-Torre Á, Martín Pintado-Zugasti A, Cuenca Zaldivar JN, García-Bermejo P, Gómez-Costa D, Molina-Álvarez M, Arribas-Romano A, Fernández-Carnero J
year: 2023
doi: 10.1186/s12998-023-00489-x
category: [tmj]
pdf_path: /Users/oracleneo/llm-wiki/papers/menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma.pdf
pdf_filename: menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma.pdf
source_collection: external
---

## Why Ingested

Part of a TMD physical-therapy ingest batch. This is the only systematic review/NMA we hold that *directly* pits dry needling against manual therapy for myofascial TMD pain — it answers the clinician's "which conservative modality is better" question with a head-to-head (indirect) ranking, complementing the procedure-level evidence on each technique. It shares senior co-author Aitor Martín Pintado-Zugasti with [[wiki/tmj/martin-pintado-2014-spray-stretch-postneedling-soreness-rct]] (post-needling soreness RCT), and reinforces the manual-therapy efficacy signal in [[wiki/tmj/gonzalez-sanchez-2023-tmj-physiotherapy-treatment-sr]]. It also frames the dry-needling-vs-stretch comparison in [[wiki/tmj/ustun-2024-dry-needling-cold-spray-stretching-rct]] and the conservative-care section of [[wiki/tmj/chan-2022-myogenous-tmd-diagnosis-treatment-review]], and feeds [[wiki/overviews/spray-and-stretch-tmd-myofascial-synthesis]].

## One-line Summary

Frequentist network meta-analysis (17 RCTs qualitative, 8 in NMA, n=556) of myofascial TMD pain: indirect dry-needling-vs-manual-therapy comparison showed NO significant difference (MD −0.263 [−1.517, 0.992] on 10-point VAS), but manual therapy ranked most likely to reduce pain (SUCRA 0.932) ahead of deep dry needling (0.775); low-quality, heterogeneous evidence.

## 한줄요약

근막성 측두하악장애(TMD) 통증에 대한 빈도주의 네트워크 메타분석 (정성 17 RCT, NMA 8편, n=556): 건침(dry needling) 대 도수치료(manual therapy)의 간접 비교는 유의차 없음 (MD −0.263 [−1.517, 0.992], 10점 VAS)이었으나, 통증 감소 가능성 순위는 도수치료(SUCRA 0.932)가 심부건침(0.775)보다 높음 — 근거 질은 낮고 프로토콜 이질성이 큼.

## 1. Document Information

- **Title**: Effectiveness of deep dry needling versus manual therapy in the treatment of myofascial temporomandibular disorders: a systematic review and network meta-analysis
- **Authors**: Ángela Menéndez-Torre, Aitor Martín Pintado-Zugasti, Juan Nicolás Cuenca Zaldivar (corresponding), Paula García-Bermejo, Diego Gómez-Costa, Miguel Molina-Álvarez, Alberto Arribas-Romano, Josué Fernández-Carnero
- **Journal**: Chiropractic & Manual Therapies 2023;31:46
- **DOI**: 10.1186/s12998-023-00489-x
- **Type**: Systematic review + frequentist network meta-analysis (NMA)
- **Registration**: PROSPERO CRD42020186470 (originally registered as a pairwise MA on 2020-05-28; switched to NMA because no head-to-head RCTs existed)
- **Received / Accepted**: 31 May 2022 / 1 June 2023
- **Funding**: None
- **Affiliation**: Universidad Rey Juan Carlos, Universidad San Pablo-CEU, and partner institutions (Madrid, Spain)

## 2. Key Contributions

1. **First NMA to isolate dry needling (DN) vs manual therapy (MT) for myofascial TMD.** No prior RCT had compared DN and MT head-to-head in this population, so an indirect comparison via a shared comparator network was the only available route.
2. **Pain-ranking hierarchy of 5 interventions** (deep dry needling, manual therapy, cognitive therapy, botulinum toxin, placebo) for short-term (1–3 month) TMJ pain on a 10-point VAS, using SUCRA.
3. **Bottom line**: DN and MT do not differ significantly on indirect comparison, but MT is the top-ranked conservative modality; botulinum toxin ranks lowest (below placebo).
4. **Heterogeneity / quality caveat** quantified: large heterogeneity (I²=65.3%), publication-bias signal on funnel plot, and high protocol variability in both DN and MT application.

## 3. Methodology and Architecture

- **Databases**: PubMed, PEDro, CINAHL, Web of Science, Scopus, Cochrane, Google Scholar, EMBASE (searched May–June 2020). 3190 records → 17 RCTs (qualitative) → 8 RCTs in NMA.
- **Population**: adults (≥18 y) with myofascial TMD, diagnosed by DC/TMD or active myofascial trigger point (MTrP) criteria. Arthrogenous TMD excluded.
- **Interventions in network**: deep dry needling, manual therapy, cognitive therapy (information/education/self-care), botulinum toxin, placebo — 5 nodes, 6 designs, 10 pairwise comparisons, 556 patients (median 47±25/study).
- **Primary NMA outcome**: pain intensity on a 10-point VAS at short-term follow-up (1–3 months) — the only outcome consistently reported by ≥3 DN and ≥3 MT studies over a matched timescale. (PPT, chewing pain, disability, mouth-opening could not be pooled.)
- **Statistics**: frequentist random-effects NMA, DerSimonian-Laird estimator, R 4.0.5 with `netmeta` and `dmetar`; effect size = mean difference (MD). Median/IQR converted to mean/SD via Wan/Luo formulas.
- **Network integrity checks**: transitivity (covariate balance for age and sex ratio), inconsistency (node-splitting + design-by-treatment interaction model), heterogeneity (Cochrane Q, I²), contribution matrix, SUCRA + rankogram + league table, publication bias (comparison-adjusted funnel plot; Egger, Begg–Mazumdar, Thompson–Sharp).
- **Quality assessment**: PEDro scale (0–10; ≥6 = acceptable). 13/17 trials ≥6; 4 low-quality; range 4–9; mean 6.71.
- **NMA pooled studies**: MT [Reynolds, Corum, De Laat, Guarda-Nardini, Kalamir]; DN [Lopez-Martos, Kütük, Gonzalez-Perez].

## 4. Key Results and Benchmarks

**Primary indirect comparison (DN vs MT), 10-point VAS, short term:**
- MD −0.263 [95% CI −1.517, 0.992] → **no significant difference** (CI crosses 0).

**SUCRA ranking** (higher = more likely to reduce pain). Note: the abstract and the body/conclusion report slightly different SUCRA values (the league table is "ordered by SUCRA"); both are recorded as published:

| Intervention | SUCRA (abstract) | SUCRA (body/conclusion) | Rank |
|---|---|---|---|
| Manual therapy | 0.932 | 0.902 | 1 (best) |
| Deep dry needling | 0.775 | 0.807 | 2 |
| Cognitive therapy | — | 0.398 | 3 |
| Placebo | — | 0.290 | 4 |
| Botulinum toxin | — | 0.103 | 5 (worst) |

**League table — significant pairwise effects (MD [95% CI]), favouring the row over column:**
- MT vs cognitive therapy: −1.085 [−1.782, −0.389] (favours MT)
- MT vs placebo: −1.322 [−2.188, −0.455] (favours MT)
- MT vs botulinum toxin: −1.720 [−3.083, −0.357] (favours MT)
- DN vs botulinum toxin: −1.457 [−2.676, −0.239] (favours DN)
- DN vs MT: −0.263 [−1.517, 0.992] (NS)
(Conclusion text additionally cites MT vs cognitive therapy as −1.805 — minor internal discrepancy with the league table value −1.085.)

**Inconsistency / heterogeneity**: Cochrane Q X²(5)=14.421, p=0.013; I²=65.3% (95% CI 16.8–85.6%) → large heterogeneity. Intra-study heterogeneity significant (p=0.019); between-study inconsistency non-significant (p=0.091; p=0.36 under full random-effects design-by-treatment model). Node-splitting showed no significant direct–indirect disagreement.
**Publication bias**: Egger t=−2.269 p=0.053, Begg–Mazumdar Z=−0.268 p=0.788, Thompson–Sharp t=−2.008 p=0.079 (all NS), but funnel plot was visually asymmetric with studies outside the bands → authors flag probable publication bias.

## 5. Limitations and Future Work

- **No direct DN-vs-MT RCT exists** — the headline comparison is entirely indirect, weakening any superiority claim.
- **Small, heterogeneous evidence base**: only 8 RCTs in the NMA; large variability in number of sessions, target muscles, DN/MT modality, and follow-up timing.
- **Only one outcome (short-term VAS pain) poolable**; PPT, chewing pain, disability, and mouth-opening could not be meta-analysed.
- **Low study quality** (4/17 below PEDro 6) and **publication-bias signal**.
- **Confounding**: male/female ratio was imbalanced in MT-vs-BTX, MT-vs-cognitive, and placebo-vs-cognitive/DN comparisons.
- **Monotherapy focus**: only isolated therapies analysed; authors note multimodal MT + exercise is likely more effective in practice.
- **Future work**: adequately powered, low-risk-of-bias RCTs directly comparing DN and MT, with standardised dosing and longer follow-up.

## 6. Related Work

- Al-Moraissi et al. 2021 — prior NMA of 10 treatments for myogenous TMD; also ranked manual therapy #1, dry needling lower (6th) and below botulinum toxin (contrast with this NMA where DN > BTX).
- Vier et al. 2019 — SR/MA: dry needling superior to placebo for PPT and to other interventions for short-term pain.
- Al-Moraissi et al. 2020 — NMA of needling therapies for masticatory-muscle pain: effectiveness independent of needling modality (wet/dry) or injected substance.
- Herrera-Valencia et al. 2020 — MA: manual therapy yields short/medium-term pain improvement that decays over time.
- Lew et al. 2021 — neck-pain SR/MA: DN and trigger-point manual therapy equivalent (neither superior).

## 7. Glossary

- **TMD (Temporomandibular Disorder, 측두하악장애)**: pain/dysfunction of the TMJ and associated structures; ~5–12% prevalence.
- **Myofascial TMD (근막성 TMD)**: extra-articular muscular subtype; ~42% of TMD diagnoses; involves myofascial trigger points.
- **MTrP (Myofascial Trigger Point, 근막성 발통점)**: hypersensitive spot in a taut band of skeletal muscle.
- **Dry needling / Deep dry needling (DN/DDN, 건침)**: insertion of a solid fine needle into an MTrP without injectate.
- **Manual therapy (MT, 도수치료)**: soft-tissue/joint mobilization, stretching, manual compression, massage, exercise.
- **NMA (Network Meta-Analysis, 네트워크 메타분석)**: synthesis allowing indirect comparison of interventions via shared comparators.
- **SUCRA (Surface Under the Cumulative Ranking curve, 누적순위곡선하면적)**: 0–1 probability-based ranking metric; higher = more likely to be the better treatment.
- **League table (리그 테이블)**: matrix of all pairwise NMA effect estimates.
- **Node-splitting (노드 분할)**: method to detect inconsistency between direct and indirect evidence.
- **PEDro scale**: 0–10 methodological-quality scale for physiotherapy RCTs; ≥6 = acceptable quality.
- **VAS (Visual Analogue Scale, 시각상사척도)**: here a 10-point pain rating.
- **PPT (Pressure Pain Threshold, 압력통증역치)**: minimum pressure eliciting pain.
