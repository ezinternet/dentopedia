---
title: "Nomogram for 5-Year Tooth-Loss Prediction After RCT in Cracked Teeth with Irreversible Pulpitis"
authors: "Dong Q, Guo S, et al."
year: 2026
date: 2026-08-07
doi: "10.2340/aos.v85.46624"
source: dong-2026-nomogram-cracked-tooth-rct-5year-survival.md
category: [cracked-tooth]
evidence_level: retrospective
source_collection: pubmed-abstract
tags: [nomogram, prognosis, RCT, cracked-tooth, survival, probing-depth, crown-restoration, irreversible-pulpitis, LASSO, logistic-regression]
relations:
  - type: extends
    target: zhang-2024-cracked-teeth-treatment-outcomes-sr-ma
  - type: reinforces
    target: ferracane-2023-cracked-tooth-registry-3year-network
---

## Three-line Summary

Retrospective cohort (Acta Odontol Scand 2026): 295 patients with cracked tooth + chronic irreversible pulpitis underwent RCT; 5-year tooth survival was 89.9%; LASSO + logistic regression identified three independent predictors of tooth loss.

Probing depth >5 mm was the only risk-increasing predictor (OR 2.99, 95%CI 1.26–7.09); crown restoration (OR 0.28) and single-visit RCT were protective; nomogram AUC 0.73 with good calibration (H-L p=0.682).

Periodontal involvement is the dominant prognostic driver in cracked teeth after RCT — a probing depth threshold of 5 mm should trigger guarded prognosis regardless of crack severity classification.

## 세줄요약

후향적 코호트 (Acta Odontol Scand 2026): 치수염 동반 균열치 RCT 295례; 5년 생존율 89.9%; LASSO+로지스틱 회귀로 3개 독립예측인자 확인.

탐침깊이 >5mm가 유일한 위험 증가인자(OR 2.99); 크라운 보철(OR 0.28)·단회 방문 RCT는 보호적; 노모그램 AUC 0.73, 보정 양호.

치주 침범이 RCT 후 균열치 예후의 핵심 변수 — 탐침 5mm를 임상 분기 기준으로 사용해야 한다.

## Summary

Dong et al. (Acta Odontol Scand 2026) conducted a retrospective analysis of 295 cracked teeth with chronic irreversible pulpitis treated with RCT at Nanjing Stomatological Hospital (2017–2020). Over 5 years, 89.9% of teeth were retained. LASSO screening followed by binary logistic regression identified three independent predictors for the nomogram: probing depth >5 mm (hazard toward loss), multi-visit RCT (also associated with loss — likely confounded by case complexity), and crown restoration (protective). The nomogram achieved AUC 0.73 with good calibration. Decision curve analysis confirmed clinical utility across the 4–68% risk threshold range.

## Key Contributions

- Probing depth >5 mm triples the odds of 5-year tooth loss (OR 2.99) — quantifies the periodontal boundary for extraction vs retain decisions
- Crown restoration after RCT reduces tooth loss odds by 72% (OR 0.28) — confirms critical role of definitive coronal seal
- Nomogram provides clinicians with individualized risk estimates for patient-level shared decision-making
- 5-year survival of 89.9% provides baseline reference for cracked tooth + irreversible pulpitis prognosis
- Multi-visit RCT is confounded by case complexity — not a direct effect of visit number per se

## Methodology

Retrospective case analysis; single center (Nanjing University); n=295 patients, 295 teeth; cracked tooth + chronic irreversible pulpitis; RCT outcome assessed at 5 years; LASSO for variable selection; binary logistic regression; nomogram via R 'rms'; ROC, H-L calibration, decision curve analysis.

## Results

| Predictor | OR | 95% CI | p |
|---|---|---|---|
| Probing depth >5 mm | 2.99 | 1.26–7.09 | <0.05 |
| 2–3 RCT visits | 0.15 | 0.05–0.50 | <0.05 |
| Crown restoration | 0.28 | 0.09–0.83 | <0.05 |

- 5-year tooth survival: 89.9% (265/295)
- Nomogram AUC: 0.73 (95%CI 0.62–0.84)
- H-L p = 0.682 (well calibrated)
- DCA risk threshold: 4–68%

## Related Papers

- [[cracked-tooth/zhang-2024-cracked-teeth-treatment-outcomes-sr-ma]] — SR+MA of cracked tooth outcomes; broader evidence base
- [[cracked-tooth/ferracane-2023-cracked-tooth-registry-3year-network]] — registry data on 3-year cracked tooth outcomes; complementary longitudinal view
- [[cracked-tooth/gioti-2026-symptomatic-cracked-tooth-management-survey]] — parallel 2026 study: clinical decision-making patterns from international survey
