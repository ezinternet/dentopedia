---
title: "3D analysis of soft tissue around implant after flap folding suture"
authors: Sae-Young Jung, Dae-Young Kang, Hyun-Seung Shin, Jung-Chul Park
year: 2021
date: 2021-09-07
doi: 10.14368/jdras.2021.37.3.130
source: jung-2021-flap-folding-suture-soft-tissue-implant.md
category: implants/soft-tissue
evidence_level: rct
pdf_path: /Users/oracleneo/llm-wiki/papers/jung-2021-flap-folding-suture-soft-tissue-implant.pdf
pdf_filename: jung-2021-flap-folding-suture-soft-tissue-implant.pdf
tags: [implants, soft-tissue, keratinized-mucosa, suture-technique, paramarginal-flap, flap-folding-suture, intraoral-scanner, 3d-volumetry, periodontology, dankook]
relations:
  - target: implants/soft-tissue/oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma
    type: extends
  - target: overviews/keratinized-mucosa-peri-implant-health-overview
    type: reinforces
---

## Three-line Summary
Pilot RCT (n=15 patients, 18 implants, Dankook University) comparing flap folding suture vs interrupted suture after paramarginal flap at implant placement, measuring peri-implant soft tissue volume change in 3D (intraoral scanner + Boolean subtraction) at post-op, stitch-out, and 3 months.
Flap folding suture maintained higher median soft tissue volume at 3 months (14.8 mm³ [IQR 9.4–19.2] vs 8.7 mm³ [8.1–11.4]) but the between-group difference was not statistically significant (P = 0.262); time effect was significant in both groups (P < 0.001).
Paramarginal flap + flap folding suture preserves more soft tissue volume with no additional graft material, though larger trials are needed to reach significance.

## 세줄요약
단국대 치주과 파일럿 무작위 대조 시험(n=15명, 임플란트 18개): 파라마진 판막 디자인 후 플랩 폴딩 봉합술 (Flap Folding Suture, FFS)(실험군) vs 단순 봉합술 (Interrupted Suture, IS)(대조군)을 비교하고, 구내 디지털 스캐너 (Intraoral Scanner, IOS)로 임플란트 주위 연조직 부피 변화를 3차원으로 측정(술 후·봉합사 제거·3개월 후).
3개월 시점에서 FFS군의 연조직 부피 중앙값이 높았으나(14.8 mm³ vs 8.7 mm³) 군간 차이는 통계적 유의성 없음(P = 0.262); 시간에 따른 부피 감소는 양 군 모두 유의(P < 0.001).
이식 없이 파라마진 판막 + FFS만으로 연조직 부피를 더 잘 유지할 가능성 시사; 유의성 확보를 위한 대규모 연구 필요.

## Summary
This Korean single-center pilot RCT investigated whether flap folding suture (FFS) — a novel technique pressing the mobilized paramarginal buccal flap horizontally under the healing abutment — can maintain greater peri-implant soft tissue volume compared with conventional interrupted sutures, without any graft material. Fifteen patients receiving 18 implants (bone graft not required) were randomized to FFS or interrupted suture after paramarginal incision and full-thickness buccal flap elevation. Soft tissue volume change was quantified at three postoperative time points using Medit i500 intraoral scans aligned and Boolean-subtracted from baseline in 3-matic Medical 13.0. At 3 months, FFS maintained numerically higher median volume (14.8 mm³) than the control (8.7 mm³), but nonparametric rank-based analysis did not reach significance (mATS P = 0.262). The study is fundamentally underpowered; the trend favoring FFS is nonetheless clinically noteworthy as it involves no biomaterial cost, no donor-site morbidity, and only marginal surgical complexity. FFS avoided the de-epithelialization step required by classic roll/modified-roll techniques and stabilized the blood clot, enabling rapid re-epithelialization of the incision relief areas. All 18 implants healed uneventfully and were successfully restored.

## Key Contributions
- First 3D volumetric analysis of peri-implant soft tissue using Boolean subtraction between sequential IOS scans to compare suture techniques at implant placement
- Describes flap folding suture in detail: single-knot technique that stabilizes the paramarginal buccal flap horizontally below the healing abutment without de-epithelialization
- Demonstrates that IOS-based 3D volume measurement is feasible perioperatively, with a scanning protocol (hemostasis + saline irrigation before scan) to minimize blood-related artefacts
- Provides a PEEK scan-body–integrated healing abutment (IOS abutment, Dentium) as a stable registration landmark for serial scan superimposition

## Methodology

| Item | Detail |
|---|---|
| Design | Prospective parallel-group RCT (pilot) |
| IRB | DKU-IRB 2019-06-005-001 |
| n | 15 patients, 18 implants |
| Allocation | Random allocation to FFS (n=9) or interrupted suture (n=9) |
| Inclusion | Age 19–70, implant without bone graft anticipated, no systemic contraindications |
| Flap | Paramarginal incision ~2 mm coronal to gingival margin → full-thickness buccal flap |
| Implant | Conventional placement, Dentium IOS PEEK healing abutment placed |
| Suture material | 5-0 Ethilon® (Ethicon/J&J) |
| Scanner | Medit i500 (iScan v1.2.0.1); 21.0 mm depth, level 1 filter |
| Time points | Baseline (pre-op), immediate post-op, stitch-out (~2 wk), 3 months |
| Superimposition | 3-matic Medical 13.0 (Materialize); multi-point alignment on adjacent cusp/fossa/HA |
| Volume software | Geomagic Design X (3D Systems) — closed-space selection after Boolean subtraction |
| Statistics | nparLD R package — mATS/ATS/WTS; post-hoc Wilcoxon + Bonferroni (α = 0.0167) |

## Results

**Soft tissue volume change from baseline (median [IQR], mm³):**

| Time point | FFS (n=9) | Interrupted (n=9) |
|---|---|---|
| Immediate post-op | 45.4 [38.8–55.5] | 37.0 [30.1–42.1] |
| Stitch-out (~2 wk) | 26.7 [19.5–37.3] | 29.7 [17.1–31.1] |
| 3 months | **14.8 [9.4–19.2]** | 8.7 [8.1–11.4] |

**Nonparametric rank-based analysis:**

| Factor | WTS (P) | ATS (P) | mATS (P) |
|---|---|---|---|
| Suture (between groups) | 0.245 | 0.245 | 0.262 |
| Time (within groups) | <0.001* | <0.001* | — |
| Suture × Time | 0.244 | 0.175 | — |

**Post-hoc (Wilcoxon, Bonferroni α=0.0167):** Significant volume reduction in both groups between post-op and 3 months, and between stitch-out and 3 months (P < 0.0167). No significant difference between post-op and stitch-out in either group.

All 18 implants completed 3-month follow-up with uneventful healing and were successfully restored.

## Related Papers
- [[implants/soft-tissue/oh-2024-keratinized-mucosa-augmentation-functioning-implants-sr-ma]] — SR+MA confirming KM augmentation (FGG/CTG/XCM) benefits peri-implant health; this paper offers a suture-only alternative (no graft)
- [[implants/soft-tissue/rios-osorio-2025-xcm-vs-ctg-fgg-implant-soft-tissue-sr-ma]] — XCM vs autograft SR+MA for KM width/mucosal thickness; this study avoids material cost entirely
- [[implants/soft-tissue/montero-2022-soft-tissue-substitutes-vs-autogenous-keratinized-mucosa-sr]] — SR of soft tissue substitutes; paramarginal FFS bypasses substitute entirely
- [[overviews/keratinized-mucosa-peri-implant-health-overview]] — Multi-paper synthesis on KM and peri-implant health that this RCT contributes pilot data to
