---
title: "Denosumab Dosage and Tooth Extraction Predict Medication-Related Osteonecrosis of the Jaw in Patients with Breast Cancer and Bone Metastases"
authors: Suguru Yokoo, Shinichiro Kubo, Daisuke Yamamoto, Masahiko Ikeda, Tetsumasa Yamashita, Kumiko Yoshikawa, Hiroshi Mese, Sakiko Ohara
year: 2025
doi: 10.3390/cancers17132242
category: [drug/mronj]
pdf_path: /Users/oracleneo/llm-wiki/papers/yokoo-2025-denosumab-mronj-breast-cancer-bone.pdf
pdf_filename: yokoo-2025-denosumab-mronj-breast-cancer-bone.pdf
source_collection: external
---

## One-line Summary
Retrospective cohort (n=324, breast cancer+bone metastases, Xgeva® 120 mg q4w): MRONJ 31.2%; ROC-derived threshold ≥32 cumulative doses (AUC 0.83); tooth extraction history OR 4.40; each additional dose adds 4.7% to MRONJ odds.

## 1. Document Information
- **Journal**: Cancers 2025, 17, 2242
- **Institution**: Fukuyama City Hospital (Orthopedic + Breast Surgery + Dental/Oral Surgery), Japan
- **Study period**: May 2012 – August 2024
- **Study design**: Retrospective cohort (IRB approval 595, 21 May 2021)

## 2. Key Contributions
- First study using ROC analysis to define a specific cumulative dose threshold for denosumab-associated MRONJ in breast cancer
- Threshold of 32 cumulative doses (= ~32 months of monthly dosing) identified; AUC 0.83
- Tooth extraction history independently multiplies MRONJ risk by 4.4×
- High MRONJ incidence (31.2%) in oncology-dose setting reflects oncology dose (120 mg q4w), not osteoporosis dose (60 mg q6mo)
- Diabetes and hormone therapy lost significance in multivariate analysis

## 3. Methodology
- 324 female patients with confirmed breast cancer + bone metastases on denosumab (Ranmark/Xgeva®)
- Age range 29–100 years (median 61.6)
- All received comprehensive dental evaluation before and during therapy
- Variables: cumulative doses, DM, smoking, cumulative prednisolone dose, chemotherapy, hormone therapy, molecular-targeted therapy, VEGF inhibitors, everolimus, tooth extraction history, oral hygiene
- Analysis: univariate (Mann-Whitney U, Fisher's exact), multivariate logistic regression, ROC analysis, internal validation (bootstrap n=1000)

## 4. Key Results

**MRONJ incidence by cumulative dose**:
- ≤10 doses: 19.6% (21/107)
- 11–30 doses: 37.5% (39/104)
- >30 doses: 36.0% (41/114)
- Overall: 31.2% (101/324)

**ROC analysis** (cumulative doses):
- AUC 0.83 (95% CI 0.78–0.88), p<0.0001
- Optimal cutoff: 32 doses
- Sensitivity 71.3%, Specificity 81.6%
- PPV 63.7%, NPV 86.3%
- Bootstrap validation: mean AUC 0.83±0.02, mean threshold 27.8±5.7 doses

**Multivariate logistic regression**:
- Cumulative doses: OR 1.047 (1.033–1.061), p<0.001 → 4.7% increase in MRONJ odds per additional dose
- Tooth extraction history: OR 4.402 (2.225–8.711), p<0.001
- Diabetes mellitus: OR 1.500 (0.834–2.697), p=0.176 (NS)
- Hormone therapy: OR 1.279 (0.639–2.562), p=0.487 (NS)
- Poor oral hygiene: OR 1.517 (0.792–2.907), p=0.209 (NS)

## 5. Limitations
- Single-center, retrospective design
- All-female cohort (breast cancer); may not generalize to other cancers or osteoporosis patients
- No standardized dental intervention during denosumab therapy
- Does not control for prior bisphosphonate use in some patients

## 6. Related Work
- Prior SR/MA: MRONJ incidence 0.5–2.1% (year 1), 1.1–3.0% (year 2), 1.3–3.2% (year 3) in oncology setting
- Ruggiero 2022 — AAOMS position paper (MRONJ definition/staging)
- Jung 2022 — osteoporosis-dose denosumab MRONJ (4.1%)

## 7. Glossary
- **Xgeva®/Ranmark®**: Denosumab 120 mg SC q4w (oncology bone metastasis dose)
- **ROC**: Receiver Operating Characteristic analysis
- **AUC**: Area Under the Curve (0.83 = high discriminative ability)
- **mTOR inhibitor**: Everolimus (Afinitor®); tested but not significant in multivariate
- **VEGF inhibitor**: Bevacizumab; not significant in multivariate
