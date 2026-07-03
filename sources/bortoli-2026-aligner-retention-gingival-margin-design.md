---
title: "Retention of orthodontic aligners with different gingival margin designs on three-dimensionally printed models representing varying degrees of marginal tissue recession"
authors: Natália Angela Bortoli, Guilherme Picolli Bernd, Hélio Radke Bittencourt, Ana Maria Spohr, João Batista Blessmann Weber
year: 2026
doi: "10.4041/kjod25.269"
category: [orthodontics/clear-aligner]
source_collection: pubmed-text
full_text: true
pmid: "42045106"
pmcid: "PMC13213253"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13213253/
text_path: /Users/oracleneo/llm-wiki/papers/bortoli-2026-aligner-retention-gingival-margin-design.txt
text_filename: bortoli-2026-aligner-retention-gingival-margin-design.txt
---

## Why Ingested

기존 [[orthodontics/clear-aligner/nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr]] SR은 trimline(straight/extended margin)이 force delivery·retention을 개선한다고 종합했으나, 건강한 치열 모델에서만 평가됐다는 한계가 있었다. 본 in-vitro 연구(Bortoli 2026, Korean Journal of Orthodontics)는 치은퇴축·치조골 소실 정도(Class I–IV)를 3D 프린팅으로 재현해 그 한계를 직접 메꾸며, retention이 margin design뿐 아니라 치주 상태에도 좌우됨을 처음으로 보임 — trimline SR의 적용 범위를 치주질환 환자로 확장.

## One-line Summary

In-vitro pull-off test (n=3/group, 3D-printed models, Classes I–IV marginal tissue recession × 3 aligner trimline designs): scalloped-extended (52.3N) and straight (47.9N) margins retain significantly more than scalloped margins (33.1N), and retention rises sharply with recession severity (Class IV 82.2N vs control 26.8N).

## 한줄요약

3D 프린팅 모델 pull-off test in-vitro 연구(group당 n=3, 치은퇴축 Class I–IV × 3가지 trimline 디자인): scalloped-extended(52.3N)·straight(47.9N) margin이 scalloped margin(33.1N)보다 유의하게 큰 유지력을 보였고, 치은퇴축이 심할수록(Class IV 82.2N vs control 26.8N) 유지력이 급증.

## 1. Document Information

- Journal: Korean Journal of Orthodontics, 2026;56(3):200-206
- DOI: [10.4041/kjod25.269](https://doi.org/10.4041/kjod25.269)
- PMID: 42045106, PMCID: PMC13213253
- Source: PubMed/PMC full text (open access), retrieved via PubMed MCP `get_full_text_article`
- No funding/COI statement extracted in available full text.

## 2. Key Contributions

- First study to simulate marginal tissue recession (periodontal disease models) when testing clear aligner gingival margin (trimline) retention — prior trimline-retention studies used only healthy-arch models.
- Quantifies retention force (N) across a 3×5 factorial design: 3 trimline designs (scalloped, scalloped-extended, straight) × 5 recession conditions (control, Class I–IV).
- Shows a two-way ANOVA-significant main effect of both factors (P<0.001 each) with no significant interaction (P=0.105) — i.e., the trimline-design retention hierarchy holds regardless of recession severity, but recession independently multiplies retention force.
- Establishes that minor recession (Class I–II) does not meaningfully change retention vs. a healthy control, but advanced recession with interdental bone loss (Class III–IV) does.

## 3. Methodology and Architecture

- Digital mandibular model (iTero Element 2 scan) manipulated in Meshmixer to create 4 standardized marginal-tissue-recession classes: Class I (1.3mm recession, no bone loss), Class II (2.5mm recession, no bone loss), Class III (3.0mm recession + 1.4mm interdental bone/soft tissue loss), Class IV (3.0mm recession + 2.5mm interdental bone/soft tissue loss), plus an unaltered control.
- 9 models 3D-printed per recession class (Form 2 SLA printer); one 0.6mm PETG (ClickFlex 3.0) thermoformed aligner per model, no tooth-movement setup (retention-only study, not a tooth-movement simulation).
- 3 gingival margin designs per model: scalloped (follows gingival zenith contour), scalloped-extended (contour +2mm beyond zenith), straight (flat cut at zenith level).
- Pull-off test: EMIC DL-2000 universal testing machine, stainless-steel hook at buccal mandibular first-molar level, crosshead speed 10mm/min, 500N load cell; each aligner pulled 10× and averaged. Sample size: n=3/group (power 80%, pooled SD 9.25N, intergroup difference 20N).
- Statistics: two-way ANOVA (margin design × recession class) + Tukey post-hoc, α=0.05; normality confirmed via Kolmogorov–Smirnov.

## 4. Key Results and Benchmarks

- Margin design main effect (P<0.001): scalloped-extended 52.3N ≈ straight 47.9N (not significantly different from each other) both > scalloped 33.1N.
- Recession main effect (P<0.001): Class IV 82.2N (highest) > Class III 54.4N > {Class II 33.2N ≈ Class I 25.6N ≈ control 26.8N} (no significant difference among these three).
- Interaction term not significant (P=0.105) — design ranking is consistent across recession severities; recession amplifies retention multiplicatively rather than altering which design is more retentive.
- No established clinical retention threshold exists to define "excessive" force causing patient discomfort — the study reports mechanical force only, not a validated comfort/pain correlate.

## 5. Limitations and Future Work

- Laboratory model cannot replicate intraoral conditions: body temperature, saliva, and cyclic loading all materially affect aligner mechanical properties and were not simulated.
- Both "tooth" and "gingiva" were printed from the same rigid resin — cannot reproduce clinical soft-tissue compliance/deformation during insertion-removal, likely overestimating true intraoral retention differences from the recession geometry alone.
- Small per-cell sample size (n=3) driven by a priori power calculation; single mandibular model, single-operator testing.
- No tooth-movement setup was programmed, so results speak only to retention/removal force, not to force delivery or biomechanical efficacy (addressed separately by trimline-biomechanics literature, e.g., [[orthodontics/clear-aligner/nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr]]).
- Authors explicitly call for future studies correlating measured retention force with actual patient-reported discomfort thresholds, and for testing in both healthy and periodontally compromised patients in vivo.

## 6. Related Work

- Cowley et al. (cited) — established that straight/extended trimlines out-retain scalloped trimlines on healthy-arch models; this study extends that finding to recession models.
- Elshazly et al. (cited) — scalloped margins reduce force transmission near the gingival region due to material flexibility/weakening, limiting complex tooth movements (bodily translation).
- A cited split-arch clinical study found straight trimlines extending 3mm beyond the gingival margin worsened gingival/plaque indices vs. scalloped trimlines — flags a retention-vs-periodontal-health tradeoff for extended designs.
- Takara et al. (cited) — proposed that harder-to-remove aligners imply higher gripping/corrective force on teeth, though the retention–force-delivery relationship itself remains unvalidated in the literature.

## 7. Glossary

- **Trimline / gingival margin design**: the cut-line geometry of an aligner's border relative to the gingival margin — scalloped (follows contour), scalloped-extended (contour +2mm), straight (flat at zenith level).
- **Marginal tissue recession Class (I–IV, this study's own scheme)**: a 3D-printed simulation gradient combining gingival recession depth with interdental bone/soft-tissue loss, not to be confused with the Miller or Cairo recession classifications.
- **Pull-off test**: mechanical test measuring the peak force (N) required to dislodge an aligner from a model, used as a proxy for clinical insertion/removal difficulty.
- **PETG (polyethylene terephthalate glycol)**: thermoplastic material used for the aligners in this study (ClickFlex 3.0, 0.6mm).
