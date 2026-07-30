---
title: "3D analysis of soft tissue around implant after flap folding suture"
authors: Sae-Young Jung, Dae-Young Kang, Hyun-Seung Shin, Jung-Chul Park
year: 2021
doi: 10.14368/jdras.2021.37.3.130
category: implants/soft-tissue
pdf_path: /Users/oracleneo/llm-wiki/papers/jung-2021-flap-folding-suture-soft-tissue-implant.pdf
pdf_filename: jung-2021-flap-folding-suture-soft-tissue-implant.pdf
source_collection: external
---

## Why Ingested
Provides pilot RCT evidence for a suture-only (no graft, no biomaterial) approach to maintain keratinized mucosa (KM) at implant placement — directly complementing augmentation-focused evidence in [[wiki/implants/soft-tissue/oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma]]. The paramarginal flap + flap folding suture is a low-cost, single-stage alternative relevant to everyday implant surgery.

## Three-line Summary
Pilot RCT (n=15 patients, 18 implants, Dankook University) comparing flap folding suture vs interrupted suture after paramarginal flap at implant placement, measuring peri-implant soft tissue volume change in 3D (intraoral scanner + Boolean subtraction) at post-op, stitch-out, and 3 months.
Flap folding suture maintained higher median soft tissue volume at 3 months (14.8 mm³ [IQR 9.4–19.2] vs 8.7 mm³ [8.1–11.4]) but the between-group difference was not statistically significant (P = 0.262); time effect was significant in both groups (P < 0.001).
Paramarginal flap + flap folding suture preserves more soft tissue volume with no additional graft material, though larger trials are needed to reach significance.

## 세줄요약
단국대 치주과 파일럿 무작위 대조 시험(n=15명, 임플란트 18개): 파라마진 판막 디자인 후 flap folding suture(실험군, n=9) vs interrupted suture(대조군, n=9)를 비교하고, 구내 디지털 스캐너로 임플란트 주위 연조직 부피 변화를 3D로 측정(술 후·봉합사 제거·3개월 후).
3개월 시점에서 flap folding suture군의 연조직 부피 중앙값이 높았으나(14.8 mm³ vs 8.7 mm³) 군간 차이는 통계적 유의성 없음(P = 0.262); 시간에 따른 부피 감소는 양 군 모두 유의(P < 0.001).
이식 없이 paramarginal 판막 + flap folding suture만으로 연조직 부피를 더 잘 유지할 가능성 시사; 유의성 확보를 위한 대규모 연구 필요.

## 1. Document Information
- **Journal**: Journal of Dental Rehabilitation and Applied Science 2021;37(3):130-7
- **DOI**: 10.14368/jdras.2021.37.3.130
- **Institution**: Department of Periodontology, College of Dentistry, Dankook University, Cheonan, Republic of Korea
- **IRB**: DKU-IRB 2019-06-005-001

## 2. Key Contributions
- First 3D volumetric analysis of peri-implant soft tissue changes comparing flap folding suture vs interrupted suture using intraoral scanner Boolean subtraction method
- Demonstrates feasibility of flap folding suture as a graft-free technique for soft tissue volume maintenance at implant placement
- Validates intraoral digital scanning (Medit i500) + 3-matic Medical software pipeline for quantifying soft tissue volume change perioperatively
- Highlights the challenge of scanning immediately post-surgery due to bleeding (clinical protocol recommendation for hemostasis + irrigation before scan)

## 3. Methodology and Architecture
- **Design**: Prospective randomized parallel-group clinical trial (pilot)
- **n**: 15 patients, 18 implants (9 flap folding suture, 9 interrupted suture)
- **Inclusion**: Adults ≥19–<70 years, implant placement without bone graft anticipated, no general contraindications to implant surgery
- **Flap design**: Paramarginal incision ~2 mm from adjacent gingival margin → full-thickness buccal flap elevation
- **Experimental (flap folding suture)**: Mobilized flap pressed horizontally under healing abutment, secured with single knot (5-0 Ethilon)
- **Control (interrupted suture)**: Two interrupted sutures mesially and distally
- **Scan abutment**: PEEK scan body-integrated healing abutment (IOS abutment, Dentium)
- **Scanner**: Medit i500 (iScan v1.2.0.1), 21.0 mm scan depth, level 1 filtering
- **Time points**: Baseline (pre-op), post-op, stitch-out (~2 weeks), 3 months
- **Volume measurement**: 3-matic Medical 13.0 (Materialize) for superimposition; Geomagic Design X (3D Systems) for closed-space volume calculation after Boolean subtraction from baseline scan
- **Statistics**: Nonparametric rank-based analysis (nparLD R package) — mATS/ATS/WTS priority order; post-hoc Wilcoxon signed-rank test with Bonferroni correction (α = 0.0167); RStudio v1.3.1093

## 4. Key Results and Benchmarks
**Soft tissue volume change (median [IQR], mm³):**

| Time point | Flap folding (n=9) | Interrupted (n=9) |
|---|---|---|
| Post-op | 45.4 [38.8–55.5] | 37.0 [30.1–42.1] |
| Stitch-out | 26.7 [19.5–37.3] | 29.7 [17.1–31.1] |
| 3 months | 14.8 [9.4–19.2] | 8.7 [8.1–11.4] |

**Statistical results (nonparametric rank-based, nparLD):**
- Suture effect: mATS P = 0.262 (not significant); ATS P = 0.245; WTS P = 0.245
- Time effect: ATS P < 0.001 (significant)
- Interaction (suture × time): ATS P = 0.175 (not significant)

**Post-hoc (Wilcoxon, Bonferroni α=0.0167):** Both groups showed significant volume decrease between post-op and 3 months, and between stitch-out and 3 months (P < 0.0167).

All 15 patients completed 3-month follow-up with uneventful healing; all implants successfully restored.

## 5. Limitations and Future Work
- Very small sample (n=15 patients, 18 implants) — underpowered for between-group significance
- Short 3-month follow-up — long-term KM width and volume outcomes unknown
- Single center (Dankook University Dental Hospital)
- No keratinized mucosa width measurement — only 3D volume; no direct KM width before/after comparison
- Bleeding at post-op scan reduced accuracy; scanning protocol recommendations remain empirical
- No blinding possible for surgeon; outcome assessor (JCP) performed all scans — potential operator bias
- Dehiscence/pocket formation risk from non-de-epithelialized folded flap not formally assessed

## 6. Related Work
- oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma: SR+MA showing KM augmentation (FGG/CTG/XCM) benefits for functioning implants — this paper offers a graft-free suture-technique alternative
- rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma: XCM vs autograft SR+MA — this study avoids graft material altogether
- montero-2022-soft-tissue-substitutes-vs-autogenous-keratinized-mucosa-sr: Soft tissue substitute SR — this paper's technique bypasses the need for any substitute

## 7. Glossary
- **Paramarginal incision**: Incision placed ~2 mm coronal to the free gingival margin, preserving the attached keratinized band and enabling buccal flap mobilization
- **Flap folding suture**: Novel suture technique pressing the mobilized buccal flap horizontally under the healing abutment with a single knot, stabilizing KM without a graft
- **Boolean subtraction**: 3D volume computation method — subtracting pre-op scan from post-op scan to isolate the incremental soft tissue volume added by surgery
- **nparLD**: R package for nonparametric rank-based analysis of longitudinal data in a repeated-measures factorial design
- **IOS abutment (PEEK)**: Polyether ether ketone scan body-integrated healing abutment enabling digital scanning at multiple time points
- **mATS (modified ANOVA-type statistic)**: Primary test statistic in nparLD; preferred over ATS/WTS for small samples
