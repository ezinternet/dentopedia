---
title: "Effectiveness of deep dry needling versus manual therapy in the treatment of myofascial temporomandibular disorders: a systematic review and network meta-analysis"
authors: Menéndez-Torre Á, Martín Pintado-Zugasti A, Cuenca Zaldivar JN, García-Bermejo P, Gómez-Costa D, Molina-Álvarez M, Arribas-Romano A, Fernández-Carnero J
year: 2023
date: 2023-10-01
doi: 10.1186/s12998-023-00489-x
source: menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma.md
category: [tmj]
confidence: sr+ma
pdf_path: /Users/oracleneo/llm-wiki/papers/menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma.pdf
pdf_filename: menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma.pdf
source_collection: external
tags: [dry-needling, manual-therapy, network-meta-analysis, myofascial-tmd, sucra, orofacial-pain, systematic-review]
relations:
  - type: reinforces
    target: martin-pintado-2014-spray-stretch-postneedling-soreness-rct
  - type: reinforces
    target: gonzalez-sanchez-2023-tmj-physiotherapy-treatment-sr
---

## One-line Summary

Systematic review + frequentist network meta-analysis (17 RCTs qualitative, 8 in NMA, n=556) of myofascial TMD pain: the indirect dry-needling-vs-manual-therapy comparison was non-significant (MD −0.263 [−1.517, 0.992] on 10-point VAS), yet manual therapy ranked the most likely modality to reduce short-term pain (SUCRA 0.932) ahead of deep dry needling (0.775); evidence is low-quality and protocol-heterogeneous.

## 한줄요약

근막성 측두하악장애(TMD) 통증에 대한 체계적 문헌고찰 + 빈도주의 네트워크 메타분석 (정성 17 RCT, NMA 8편, n=556): 건침 대 도수치료의 간접 비교는 유의차 없음 (MD −0.263 [−1.517, 0.992], 10점 VAS)이었으나, 단기 통증 감소 가능성 순위는 도수치료(SUCRA 0.932)가 심부건침(0.775)보다 앞섬 — 근거 질이 낮고 프로토콜 이질성이 큼.

## Summary

This Spanish (Universidad Rey Juan Carlos) SR/NMA addressed a question that no single RCT could answer: is **deep dry needling (DN)** or **manual therapy (MT)** the better conservative treatment for **myofascial TMD** pain? Because the literature search (8 databases, 3190 records) found **no head-to-head RCT** comparing DN and MT, the authors built a frequentist random-effects network with five nodes — DN, MT, cognitive therapy, botulinum toxin (BTX), and placebo — to compare DN and MT *indirectly* via shared comparators. Of 17 RCTs included qualitatively, **8 (n=556 patients)** had pooled data for the only consistently reported outcome: pain intensity on a 10-point VAS at short term (1–3 months).

**Verdict**: DN and MT do **not differ significantly** on the indirect comparison (MD −0.263, 95% CI −1.517 to 0.992), but the SUCRA ranking placed **manual therapy first** (SUCRA 0.932; body text 0.902) and **deep dry needling second** (0.775; body text 0.807), well above cognitive therapy, placebo, and botulinum toxin (worst). MT significantly beat placebo, BTX, and cognitive therapy; DN significantly beat BTX. The authors stress caution: large heterogeneity (I²=65%), a publication-bias signal, low PEDro quality in 4 trials, and wide variability in how DN and MT were applied.

**Clinical takeaway**: for myofascial TMD, manual therapy and dry needling are both reasonable short-term pain modalities with no proven superiority of one over the other; manual therapy edges the ranking, and both clearly outperform botulinum toxin in this network.

## Key Contributions

- First NMA to **isolate the DN-vs-MT question** for myofascial TMD (an indirect comparison, since no direct RCT exists).
- Short-term (1–3 mo) VAS-pain **hierarchy of five interventions** by SUCRA.
- Establishes that **botulinum toxin ranks last** (below placebo) for myofascial TMD pain in this network — DN significantly outperformed BTX.
- Quantifies the **fragility of the evidence**: I²=65%, funnel-plot asymmetry, protocol heterogeneity → "interpret with caution."

## Methodology

- **Design**: SR + frequentist random-effects NMA (DerSimonian-Laird), R `netmeta`/`dmetar`; PRISMA-NMA; PROSPERO CRD42020186470.
- **Search**: PubMed, PEDro, CINAHL, Web of Science, Scopus, Cochrane, Google Scholar, EMBASE (May–June 2020); 3190 → 17 RCTs → 8 in NMA.
- **Population**: adults with myofascial TMD (DC/TMD or active MTrP). Arthrogenous TMD, crossover, single-arm designs excluded.
- **Network**: 5 nodes (DN, MT, cognitive therapy, BTX, placebo), 6 designs, 10 pairwise comparisons, 556 patients.
- **Outcome**: pain on 10-point VAS at short term (1–3 mo) — only outcome with ≥3 DN and ≥3 MT studies on a matched timescale; effect size = mean difference.
- **Checks**: transitivity (age/sex covariate balance), inconsistency (node-splitting + design-by-treatment model), heterogeneity (Cochrane Q, I²), SUCRA + rankogram + league table, publication bias (comparison-adjusted funnel; Egger/Begg/Thompson-Sharp).
- **Quality**: PEDro scale — 13/17 ≥6, range 4–9, mean 6.71.

## Results

**Indirect DN vs MT (10-point VAS, short term): MD −0.263 [95% CI −1.517, 0.992] → non-significant.**

SUCRA ranking (higher = more likely to reduce pain). The abstract and the body/conclusion report slightly different SUCRA values; both are recorded as published.

| Rank | Intervention | SUCRA (abstract) | SUCRA (body) |
|---|---|---|---|
| 1 | Manual therapy | 0.932 | 0.902 |
| 2 | Deep dry needling | 0.775 | 0.807 |
| 3 | Cognitive therapy | — | 0.398 |
| 4 | Placebo | — | 0.290 |
| 5 | Botulinum toxin | — | 0.103 |

League table — significant pairwise MDs [95% CI] (negative favours the better treatment):

| Comparison | MD [95% CI] | Favours |
|---|---|---|
| DN vs MT | −0.263 [−1.517, 0.992] | NS (no difference) |
| MT vs cognitive therapy | −1.085 [−1.782, −0.389] | Manual therapy |
| MT vs placebo | −1.322 [−2.188, −0.455] | Manual therapy |
| MT vs botulinum toxin | −1.720 [−3.083, −0.357] | Manual therapy |
| DN vs botulinum toxin | −1.457 [−2.676, −0.239] | Dry needling |

**Inconsistency/heterogeneity**: Cochrane Q X²(5)=14.421, p=0.013; I²=65.3% (95% CI 16.8–85.6%) = large. Between-study inconsistency NS (p=0.091; p=0.36 under full random-effects design-by-treatment model); node-splitting showed no direct–indirect disagreement. **Publication bias**: statistical tests NS (Egger p=0.053, Begg p=0.788, Thompson-Sharp p=0.079) but funnel plot visually asymmetric → probable bias.

## Related Papers

- [[tmj/martin-pintado-2014-spray-stretch-postneedling-soreness-rct]] — shares senior co-author Aitor Martín Pintado-Zugasti; the dry-needling side of the same myofascial-TMD literature (post-needling soreness management).
- [[tmj/gonzalez-sanchez-2023-tmj-physiotherapy-treatment-sr]] — reinforces the manual-therapy/physiotherapy efficacy signal that tops this NMA's ranking.
- [[tmj/calixtre-2015-manual-therapy-tmd-pain-rom-sr]] — earlier SR of manual therapy for TMD (pain/MMO/PPT); this NMA extends it with a head-to-head DN-vs-MT comparative ranking.
- [[tmj/ustun-2024-dry-needling-cold-spray-stretching-rct]] — RCT comparing dry needling vs cold-spray-and-stretch; this NMA frames the DN-vs-other-conservative-modality question.
- [[tmj/chan-2022-myogenous-tmd-diagnosis-treatment-review]] — myogenous-TMD review; this NMA supplies the comparative-effectiveness ranking for its conservative-care section.
- [[overviews/spray-and-stretch-tmd-myofascial-synthesis]] — synthesis page that this NMA's DN-vs-MT ranking feeds into.
