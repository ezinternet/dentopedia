---
title: "Comparative efficacy of electric toothbrush technologies in plaque and gingivitis reduction: a network meta-analysis"
authors: Chenchen Luo et al.
year: 2026
date: 2026-06-03
doi: 10.1007/s00784-026-06955-z
source: luo-2026-electric-toothbrush-technologies-plaque-gingivitis-nma.md
category: [periodontics]
confidence: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "42234020"
pmcid: "PMC13233912"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13233912/
text_path: /Users/oracleneo/llm-wiki/papers/luo-2026-electric-toothbrush-technologies-plaque-gingivitis-nma.txt
text_filename: luo-2026-electric-toothbrush-technologies-plaque-gingivitis-nma.txt
tags: [electric-toothbrush, oscillating-rotating, sonic, plaque-control, gingivitis, network-meta-analysis, oral-hygiene, orthodontic]
relations:
  - type: extends
    target: jo-2008-management-of-dental-biofilm-through
  - type: reinforces
    target: jakubovics-2021-dental-plaque-biofilm-matrix
---

## One-line Summary

Frequentist network meta-analysis (19 RCTs, 1996–2025) ranking electric toothbrush technologies: oscillating-rotating ranks first for both plaque (SUCRA 89.2%) and gingivitis (86.5%), followed by sonic > ultrasonic > other electric > manual; all electric types beat manual, with largest benefits in orthodontic patients and children and a non-significant effect in the elderly.

## 한줄요약

빈도주의 네트워크 메타분석 (19개 RCT, 1996–2025): 전동칫솔 기술 순위 — 진동회전형(oscillating-rotating)이 치면세균막(SUCRA 89.2%)·치은염(86.5%) 모두 1위, 이어 음파(sonic) > 초음파(ultrasonic) > 기타 전동 > 수동 순. 모든 전동칫솔이 수동보다 우수하며 교정 환자·소아에서 효과 최대, 노인에서는 유의하지 않음.

## Summary

Pairwise meta-analyses had long established that electric toothbrushes outperform manual ones for plaque removal, but they could not tell a clinician or patient *which* electric technology to choose. Luo et al. (2026, Clinical Oral Investigations) close that gap with a frequentist network meta-analysis (NMA) of 19 RCTs (published 1996–2025; sample sizes 23–150) that ranks five interventions — manual, oscillating-rotating (O-R), sonic, ultrasonic, and "other electric" — for both plaque and gingivitis reduction.

The network is connected through the manual common comparator, supplemented by two direct O-R-vs-sonic head-to-head trials. Using Surface Under the Cumulative Ranking (SUCRA), **oscillating-rotating brushes rank first** for both outcomes, with manual brushes last. The ranking is robust across a duration-stratified analysis (short-term single-use vs longer-term home-use) and across sensitivity analyses excluding small or high-risk-of-bias studies.

## Key Contributions

- First NMA to deliver a **direct quantitative ranking among electric toothbrush subtypes**, not just electric vs manual — reframing the question from "whether to use electric" to "which electric technology."
- Connected 5-node network (Manual, O-R, Sonic, Ultrasonic, Other Electric) combining direct head-to-head and indirect evidence.
- Robustness shown through duration-stratified NMA and sensitivity analyses.
- Mechanistic rationale: O-R's 3D oscillation+rotation generates focused shear forces that disrupt biofilm at concave surfaces, fissures, and the gingival margin more efficiently than sonic (lateral sweep) or ultrasonic (microstreaming) actions.

## Methodology

- **Design**: Systematic review + frequentist random-effects NMA (PRISMA-NMA; PROSPERO CRD420251273484), R 4.5.0 `netmeta`.
- **Search**: PubMed, Embase, Cochrane CENTRAL, Web of Science, ClinicalTrials.gov; inception → June 2025; English only.
- **PICOS**: children/adults (permanent or mixed dentition); electric (O-R / sonic / ultrasonic / other) vs manual; outcome = validated Plaque Index and/or Gingivitis Index; RCTs (parallel + crossover).
- **Effect measure**: Standardized Mean Difference (SMD) with 95% CI (varied indices). Index prioritization: author-designated primary → RMNPI (plaque) / MGI (gingivitis) → whole-mouth over site-specific. Longest follow-up per study.
- **Ranking**: SUCRA. Inconsistency assessed by node-splitting (global + local). Transitivity checked via baseline plaque severity, brushing supervision, follow-up duration (no substantial imbalance).
- **RoB**: Cochrane RoB 2.0 → 12 low, 5 some concerns, 2 high.
- **Prespecified subgroups**: age (children/adults/elderly), orthodontic patients, follow-up duration; plus duration-stratified NMA (single-use k=7 vs home-use ≥1 week k=12).
- **Selection**: 1,852 records → 124 full-text → **19 RCTs**.

## Results

**Plaque reduction — SUCRA ranking:**

| Rank | Technology | SUCRA |
|---|---|---|
| 1 | Oscillating-Rotating | 89.2% |
| 2 | Sonic | 72.4% |
| 3 | Ultrasonic | 54.1% |
| 4 | Other Electric | 45.3% |
| 5 | Manual | 18.3% |

- O-R vs manual SMD **-1.24** (95% CI -1.56 to -0.92); sonic vs manual SMD -0.87 (-1.15 to -0.59) — all electric significantly > manual.
- Absolute (RMNPI 0–1 scale): O-R vs manual difference **-0.18** (95% CI -0.24 to -0.12) ≈ **18% greater plaque reduction**.

**Gingivitis reduction — SUCRA ranking:**

| Rank | Technology | SUCRA |
|---|---|---|
| 1 | Oscillating-Rotating | 86.5% |
| 2 | Sonic | 70.1% |
| 3 | Ultrasonic | 52.8% |
| 4 | Other Electric | 43.9% |
| 5 | Manual | 16.7% |

- Absolute (MGI 0–4 scale): O-R vs manual difference **-0.32** (95% CI -0.45 to -0.19).
- Overall electric vs manual gingivitis: SMD **0.82** (95% CI 0.65 to 0.98, p<0.001) — moderate beneficial effect.

**Duration-stratified NMA:**

- Short-term single-use (k=7): O-R SUCRA 91.5%; O-R vs manual SMD -1.52 (95% CI -1.98 to -1.06) — larger immediate mechanical advantage.
- Longer-term home-use (k=12): O-R SUCRA 86.7%; O-R vs manual SMD -0.96 (95% CI -1.35 to -0.57) — more modest (compliance/behavioral factors).
- Ranking order identical across strata → robust.

**Subgroups & robustness:**

- Largest effects in **orthodontic patients and children** (O-R navigates brackets/archwires; "skill-equalizer" for children with limited dexterity).
- **Elderly subgroup effect non-significant** — grip strength, arthritis, cognitive/visual deficits compromise device use; superiority of the technology does not auto-translate to effectiveness.
- Adult gingivitis subgroup CI crosses null (NS; few studies).
- Only **2 direct O-R-vs-sonic RCTs** (Van der Weijden 1996; Erbe 2019); Erbe 2019 found O-R-with-ortho-head superior to sonic (p=0.017).
- Publication bias: no significant evidence; p-curve right-skewed (χ²=43.0, p=0.03); sensitivity excluding studies <50 left rankings virtually unchanged (max ΔSUCRA 3.2%) — though tests underpowered (k<10).

**Caveats:** "Other electric" rests on only 2 small studies (NS vs manual in home-use stratum) — interpret with extreme caution. SUCRA reflects probability of top rank, not magnitude of benefit. Limited direct electric-vs-electric evidence makes the ranking **provisional**. Most trials were industry-sponsored (potential bias).

**Bottom line:** Oscillating-rotating electric toothbrushes have the highest probability of being among the most effective interventions for mechanical plaque and gingivitis control, and should be preferentially considered where manual brushing is challenging — especially orthodontic patients and children.

## Related Papers

- [[periodontics/jo-2008-management-of-dental-biofilm-through]] — extends: professional care raising patient plaque-control capability; this NMA quantifies the home-care tool (brush-technology) axis of plaque control.
- [[oral-microbiology/jakubovics-2021-dental-plaque-biofilm-matrix]] — reinforces: biofilm matrix biology that the O-R 3D shear-force mechanical disruption rationale acts upon.
- [[periodontics/cyris-2024-guided-biofilm-therapy-versus-conventional]] — related: professional biofilm removal in NSPT; complements home-care device ranking here.
