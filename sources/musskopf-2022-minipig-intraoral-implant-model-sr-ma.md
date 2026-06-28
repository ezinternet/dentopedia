---
title: "The minipig intraoral dental implant model: A systematic review and meta-analysis"
authors: Musskopf ML, Finger Stadler A, Wikesjo UME, Susin C
year: 2022
doi: 10.1371/journal.pone.0264475
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/musskopf-2022-minipig-intraoral-implant-model-sr-ma.pdf
pdf_filename: musskopf-2022-minipig-intraoral-implant-model-sr-ma.pdf
source_collection: external
---

## Why Ingested

미니피그 동물모델 임플란트 연구의 해석 기준을 확립하기 위해 수집. 표면처리, 골유착 기전, 수술 프로토콜 관련 동물 연구를 평가할 때 BIC 기준값 및 모델 특성을 알아야 하므로, [[wiki/implants/bosshardt-2017-osseointegrated-titanium-zirconia-review]]의 골유착 기전 리뷰를 보완하는 전임상 모델 메타데이터 기반으로 활용.

## One-line Summary

SR+MA of 55 minipig intraoral implant studies (n≈550 animals): mean BIC 59.88% (95% CI 57.43–62.33), increasing significantly over time, with high heterogeneity (I²>90%) explained by observation interval and implant surface.

## 한줄요약

미니피그 구내 임플란트 모델 55편 SR+MA: 평균 골-임플란트 접촉률(BIC) 59.88%, 관찰기간 및 임플란트 표면에 따라 유의한 차이, 이종성 매우 높음(I²>90%).

## 1. Document Information

- **Journal**: PLOS ONE
- **Published**: February 28, 2022
- **Study type**: Systematic review + meta-analysis (PRISMA)
- **Databases**: PubMed/MEDLINE, EMBASE (through June 2021)
- **Funding**: Nobel Biocare AG (no role in design/analysis)
- **Institution**: University of North Carolina at Chapel Hill, Adams School of Dentistry

## 2. Key Contributions

1. Establishes normative BIC benchmarks for the minipig intraoral implant model (mean 59.88%)
2. Quantifies time-dependent BIC progression: 40.93% at 2 wks → 58.37% at 4 wks → 66.33% beyond 4 wks
3. Identifies key sources of heterogeneity: post-extraction and post-implant observation intervals, implant surface type
4. Documents the standard minipig model protocol (premolar/molar extraction, 12±4 wk healing, 3 narrow implants per quadrant, 8 wk osseointegration)
5. Reveals pervasive quality-of-reporting gaps in preclinical animal studies (ARRIVE checklist)

## 3. Methodology and Architecture

**Inclusion criteria**:
- Original articles using minipigs, intraoral sites, titanium dental implants
- Histological evaluation of osseointegration in native alveolar bone
- Central tendency + variability data required

**Exclusion**: implants in augmented bone, concomitant GBR (control-group data used when applicable); no proper statistical analysis

**Primary outcome**: Bone-implant contact (BIC %)
**Secondary outcomes**: First BIC (distance implant platform → first bone contact), crestal bone level

**Statistical approach**:
- Random-effects meta-analysis (Stata 17)
- Meta-regression for heterogeneity moderators: animal strain/age, extraction healing, implant placement healing, staging, loading, implant surface
- Restricted maximum likelihood (REML) method
- Heterogeneity: I² statistic (cut-offs: 25%/50%/75%)
- Publication bias: funnel plots + Egger's test

**Quality assessment**: ARRIVE checklist (selected items, scored 0/1/2 per item)

## 4. Key Results and Benchmarks

**Study selection**: 279 publications identified → 125 full-text reviewed → 55 studies included

**Typical model protocol**:
- Gottingen minipig most common strain (30.9%)
- Mandibular premolar + first molar extraction
- 12 wk post-extraction healing (most common)
- 3 implants per jaw quadrant, 3.5mm diameter, 8mm length
- Submerged healing (64%), transmucosal healing (36%)
- 8 wk osseointegration period (average)

**BIC results**:
- Overall mean BIC: **59.88%** (95% CI: 57.43–62.33)
- 2 wks: 40.93% (95% CI: 34.95–46.90)
- 4 wks: 58.37% (95% CI: 54.38–62.36)
- Beyond 4 wks: 66.33% (95% CI: 63.45–69.21)
- Time effect significant (p<0.001)
- Heterogeneity: I²>90% for all analyses

**Key moderators** (meta-regression):
- Post-extraction observation interval: significant
- Post-implant observation interval: significant
- Implant surface: significant

**Quality of reporting**: Generally low; frequent omissions — animal characteristics, examiner masking/calibration, sample size calculations

**Comparison with other models**: BIC values comparable to canine and human histological studies; bone formation in gap defects 1.2–1.5 mm/day (minipig) vs 1.0–1.5 mm/day (humans)

## 5. Limitations and Future Work

- High heterogeneity (I²>90%) limits precision of pooled estimates
- Quality of reporting in included studies generally poor
- Grey literature not searched
- Only titanium implants in native alveolar bone included (limits generalizability to augmented-bone scenarios)
- Publication bias possible (funnel plot asymmetry not formally tested for all outcomes)

## 6. Related Work

- Bosshardt 2017: osseointegration titanium vs zirconia — provides human/clinical BIC context
- Albrektsson 1981: original osseointegration criteria
- Pilawski 2021 (cited): maxillary alveolar bone structure comparison minipig vs human (histology/IHC/radiography — similar collagen, osteocyte density, mineral apposition rate)

## 7. Glossary

- **BIC** (Bone-to-Implant Contact): % of implant surface in direct contact with bone; primary histometric outcome of osseointegration
- **First BIC**: distance from implant platform to most coronal bone-implant contact point (crestal adaptation indicator)
- **Crestal bone level**: distance from implant platform to most coronal alveolar bone extent
- **ARRIVE checklist**: Animal Research: Reporting of In Vivo Experiments — quality/reporting standard for animal studies
- **REML**: Restricted Maximum Likelihood — statistical method for heterogeneity estimation in random-effects meta-analysis
- **Gottingen minipig**: most commonly used minipig strain in dental implant research; well-characterized bone/oral anatomy
- **Cutting-grinding technique**: histologic preparation method for undecalcified bone sections; allows BIC measurement
