---
title: "Translating the A1C Assay Into Estimated Average Glucose Values"
authors: Nathan DM, Kuenen J, Borg R, Zheng H, Schoenfeld D, Heine RJ, A1c-Derived Average Glucose Study Group
year: 2008
doi: 10.2337/dc08-0545
category: drug
pdf_path: /Users/oracleneo/llm-wiki/papers/nathan-2008-translating-a1c-assay-estimated-average.pdf
pdf_filename: nathan-2008-translating-a1c-assay-estimated-average.pdf
source_collection: external
---

## One-line Summary
International multicenter prospective study (n=507; 268 T1DM, 159 T2DM, 80 non-diabetic) establishing the linear regression equation eAG (mg/dL) = 28.7 × A1C − 46.7 (R²=0.84), enabling reporting of HbA1c as estimated Average Glucose (eAG).

## 1. Document Information
- **Title**: Translating the A1C Assay Into Estimated Average Glucose Values
- **Authors**: David M. Nathan, Judith Kuenen, Rikke Borg, Hui Zheng, David Schoenfeld, Robert J. Heine, for the A1c-Derived Average Glucose (ADAG) Study Group
- **Journal**: Diabetes Care 31(8):1473–1478
- **Publication Date**: August 2008
- **DOI**: 10.2337/dc08-0545
- **License**: CC BY-NC-ND (educational, non-profit use allowed)
- **Study Type**: International multicenter prospective observational
- **Sample**: n=507 adults (18–70y), 10 centers (US, Europe, Africa, Asia)

## 2. Key Contributions
- Established the **definitive linear regression equation** between A1C and average glucose: **eAG (mg/dL) = 28.7 × A1C − 46.7**, R²=0.84, p<0.0001 (slope/intercept also reported in mmol/L: eAG mmol/L = 1.59 × A1C − 2.59).
- Demonstrated that the regression equation does **not differ significantly** across subgroups based on age, sex, diabetes type (T1 vs T2), race/ethnicity, or smoking status.
- Provided basis for ADA/EASD recommendation to report HbA1c results **alongside eAG** in same units used for self-monitoring of blood glucose (SMBG), reducing patient/provider confusion between % units and mg/dL units.
- Generated reference eAG values: A1C 5% = 97, 6% = 126, 7% = 154, 8% = 183, 9% = 212, 10% = 240, 11% = 269, 12% = 298 mg/dL.

## 3. Methodology and Architecture
- **Glucose measurement (3 modalities combined)**:
  1. Continuous Glucose Monitoring (CGM, Medtronic Minimed CGMS) every 5 min — 2+ days at baseline and every 4 weeks for 12 weeks.
  2. Eight-point capillary self-monitoring (premeal, 90 min postprandial, prebed, 3 AM) with HemoCue 201 Plus during CGM days for calibration.
  3. Seven-point fingerstick SMBG (OneTouch Ultra) ≥3 days/week throughout 12-week period (no 3 AM).
- **A1C measurement**: Central laboratory, four DCCT-aligned assays (Tosoh G7 HPLC, Roche A1C, Roche Tina-quant immunoassay, Primus Ultra-2 affinity); intra/inter-assay CV <2.5%; mean of four assays used.
- **AG calculation**: Weighted arithmetic mean of CGM (corrected ×1.05 for capillary equivalence) and Lifescan fingerstick values; each measurement weighted inversely to total daily measurements.
- **Sample**: ~2,700 glucose values per subject over 3 months.
- **Statistical model**: Linear regression preferred over quadratic (no improvement, p=0.82); heteroschedasticity correction with variance as increasing function of A1C; 90% prediction intervals calculated.
- **Exclusions**: hemoglobinopathies, anemia (Hct <39% men, <36% women), high erythrocyte turnover, transfusion, CKD, liver disease, high-dose vitamin C, erythropoietin — to isolate the A1C–glucose relationship from RBC lifespan confounders.

## 4. Key Results and Benchmarks
- **Primary regression**: eAG (mg/dL) = 28.7 × A1C − 46.7; R²=0.84; p<0.0001.
- **Equivalent in mmol/L**: eAG (mmol/L) = 1.59 × A1C − 2.59.
- **eAG correspondence table**:
  | A1C (%) | eAG (mg/dL) | eAG (mmol/L) | 95% CI (mg/dL) |
  |---|---|---|---|
  | 5 | 97 | 5.4 | 76–120 |
  | 6 | 126 | 7.0 | 100–152 |
  | 7 | 154 | 8.6 | 123–185 |
  | 8 | 183 | 10.2 | 147–217 |
  | 9 | 212 | 11.8 | 170–249 |
  | 10 | 240 | 13.4 | 193–282 |
  | 11 | 269 | 14.9 | 217–314 |
  | 12 | 298 | 16.5 | 240–347 |
- **Subgroup consistency**: No significant difference in slope/intercept across T1DM vs T2DM, age (<50 vs ≥50), sex, race (Caucasian, Black, Hispanic, Asian), smoking — supporting universal application of the equation.

## 5. Limitations and Future Work
- **Exclusion of unstable glycemia**: Subjects required to have stable A1C (two values within 1% point in 6 months) — equation may not apply to acutely changing glycemia.
- **Exclusion of RBC-altering conditions**: Anemia, hemoglobinopathy, CKD, transfusion all excluded — eAG equation not validated in these populations; alternative biomarkers (fructosamine, CGM) needed.
- **Sparse data at high A1C range (>10%)**: Prediction intervals widen; equation extrapolation beyond A1C 11–12% less reliable.
- **Race/ethnicity sample**: Despite no statistical difference, sample of African-American subjects relatively small; later studies (Bergenstal 2017) suggested race effect on A1C–AG relationship persists at finer resolution.
- **Future**: Validation in pediatric, pregnancy, CKD, hemoglobinopathy populations; integration with CGM-derived time-in-range metrics (later operationalized by 2019 International Consensus on CGM).

## 6. Related Work
- **DCCT** (Diabetes Control and Complications Trial, 1993): established A1C as outcome surrogate for microvascular complications in T1DM.
- **UKPDS** (UK Prospective Diabetes Study, 1998): same in T2DM.
- **National Glycohemoglobin Standardization Program (NGSP)**: assay standardization framework that ADAG built upon.
- **IFCC reference method** (Hoelzel 2004): proposed parallel standardization producing values 1.5–2.0 percentage points lower than NGSP, motivating the eAG approach to reduce patient confusion.
- **Bergenstal 2017** (DCCT/ADAG re-analysis): identified race-specific A1C–AG differences that complicate universal eAG application.

## 7. Glossary
- **A1C / HbA1c**: Glycated hemoglobin — Hb β-chain N-terminal valine covalently bound to glucose via Amadori rearrangement. Reflects ~2–3 month average glycemia.
- **eAG (estimated Average Glucose)**: A1C translated to glucose concentration units (mg/dL or mmol/L) via Nathan 2008 equation.
- **NGSP**: National Glycohemoglobin Standardization Program — US-led A1C assay standardization tied to DCCT.
- **IFCC**: International Federation of Clinical Chemistry — alternative reference method producing values ~1.5–2.0% lower than NGSP.
- **CGM**: Continuous Glucose Monitoring — interstitial glucose sensor sampling every 1–5 min.
- **SMBG**: Self-Monitoring of Blood Glucose — fingerstick capillary measurement.
- **AG**: Average Glucose — arithmetic mean of measured glucose values over defined period.
- **DCCT**: Diabetes Control and Complications Trial — landmark RCT establishing A1C–complication relationship.
