#!/usr/bin/env python3
"""
One-off batch ingest for 43 orphan PDFs (2026-05-24 session).
- Identifies & deletes duplicate PDFs.
- Renames remaining 41 PDFs to {lastname}-{year}-{5-words}.pdf
- Generates sources/{stem}.md (7-section format)
- Generates wiki/{category}/{stem}.md (frontmatter + Korean한줄요약 + body)
- Appends entries to index.md per-category list

NOTE: This is intentionally a one-shot script. Re-running is safe (idempotent for new stems).
"""
import os, json, re, shutil, warnings
warnings.filterwarnings('ignore')

ROOT = '/sessions/trusting-ecstatic-faraday/mnt/llm-wiki'
os.chdir(ROOT)

with open('/tmp/orphan_fulltext.json') as f:
    FULLTEXT = json.load(f)

TODAY = '2026-05-24'

# ── DUPLICATES TO DELETE ───────────────────────────────────────────
DUPES_TO_DELETE = [
    '20241108-1703789-xqqgfv',   # = cureus-0016-00000071152 (Liu 2024)
    '20251211-42159-qfebp3',     # = cureus-0017-00000096476 (Yaghmai 2025)
]

# ── ENTRIES ────────────────────────────────────────────────────────
# Each: old_stem → (new_stem, category, year, authors, title, doi, confidence, oneline_kr, summary, key_contrib, methodology, results, limitations, related)
ENTRIES = {
    '12903_2022_Article_2331': dict(
        stem='lei-2022-alveolar-bone-width-sagittal-tooth',
        category='immediate-implant',
        year=2022, date='2022-09-09',
        authors='Chen Lei, Qun Yu, Di Wu, Kunzhan Cai, Paul Weigl, Chunbo Tang',
        title='Comparison of alveolar bone width and sagittal tooth angulation of maxillary central incisors in Class I and Class III canine relationships: a retrospective CBCT study',
        doi='10.1186/s12903-022-02331-x',
        confidence='retrospective',
        oneline_kr='CBCT 후향적 연구(n=120): Class III 견치 관계에서는 상악 중절치의 치근축이 더 협측으로 기울어 있고 순측 골 두께가 얇아지는 경향이 있어, 즉시 식립 시 술 전 평가에 견치 관계도 변수로 포함해야 한다.',
        summary='Retrospective CBCT study of 120 patients comparing alveolar bone width and sagittal tooth angulation of maxillary central incisors stratified by Class I vs Class III canine relationship. Class III had significantly thinner labial bone and greater labial root inclination, complicating immediate implant placement planning.',
        key_contrib='Demonstrates that malocclusion class (anterior canine relationship) is an under-appreciated covariate of esthetic-zone bone morphology and should be screened pre-operatively for immediate implant cases.',
        methodology='Retrospective CBCT analysis of 120 patients. Measurements at multiple levels of labial/palatal bone, root inclination, and overall alveolar width on central incisors. Stratified by Angle Class I vs Class III canine relationship.',
        results='Class III patients showed thinner labial bone plates (often <1 mm in apical thirds), more labial root inclination, and reduced bone available palatal to the root apex, all of which adversely affect immediate implant indications.',
        limitations='Single-center retrospective; CBCT measurement precision limited by voxel size. No outcome data — implications are inferred from anatomy only.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/rodrigues-2022-srp-periodontal-phenotype-anterior-maxillary'],
    ),
    '12903_2023_Article_2991': dict(
        stem='cicciu-2023-buccal-palatal-bone-thickness-marginal',
        category='implants',
        year=2023, date='2023-05-18',
        authors='Marco Cicciù, Umberto Pratella, Luca Fiorillo, Fabio Bernardello, Francesco Perillo, Antonio Rapani, Claudio Stacchi, Teresa Lombardi',
        title='Influence of buccal and palatal bone thickness on post-surgical marginal bone changes around implants placed in posterior maxilla: a multi-centre prospective study',
        doi='10.1186/s12903-023-02991-3',
        confidence='prospective',
        oneline_kr='상악 소구치부 implant 90개 전향적 다기관 연구: T0 협측 평균 골 두께 2.42 mm → T1 1.92 mm로 유의 감소(p<0.001), T0 골 두께가 두꺼울수록 EMBL이 작아지는 역상관 — 1mm 미만의 얇은 협측골은 위험 인자.',
        summary='Multi-center prospective study of 90 implants in maxillary premolar area. Buccal and palatal bone thickness measured at placement (T0) and 3-month uncovering (T1). Showed significant horizontal resorption (mean -0.5 mm buccal, -0.4 mm palatal) but minimal vertical bone loss during submerged healing. Inverse correlation between initial thickness and EMBL.',
        key_contrib='Quantifies the buccal/palatal envelope thickness threshold (~2 mm) required to keep submerged-healing EMBL within negligible range. Adds prospective evidence to the rule of thumb of ≥2 mm buccal bone.',
        methodology='Multi-center prospective. Periodontal probe measurements at T0 (placement) and T1 (3-month uncovering). Kruskal-Wallis + multivariate linear regression on bone changes.',
        results='Mean buccal thickness 2.42 ± 0.64 mm at T0 → 1.92 ± 0.71 mm at T1 (p=0.000). Palatal 1.31 → 0.87 mm. Vertical resorption non-significant (~0.03–0.04 mm). Initial thickness inversely correlated with horizontal loss.',
        limitations='Submerged healing only (no functional loading); 3-month follow-up; manual probe measurements with 0.5 mm precision.',
        related=['immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp',
                 'immediate-implant/shafizadeh-2021-alveolar-bone-thickness-healthy-sr'],
    ),
    '12903_2023_Article_3678': dict(
        stem='elsheikh-2023-prf-xenograft-alloplastic-immediate-implant',
        category='immediate-implant',
        year=2023, date='2023-12-13',
        authors='Heba Abo-Elfetouh Elsheikh et al.',
        title='Comparison between platelet rich fibrin as space filling material versus xenograft and alloplastic bone grafting materials in immediate implant placement: a randomized clinical trial',
        doi='10.1186/s12903-023-03678-5',
        confidence='rct',
        oneline_kr='RCT: 즉시 식립 시 잔여 갭(jumping gap)을 PRF·xenograft·alloplastic 중 무엇으로 채우느냐의 비교 — 모두 임상적으로 수용 가능, PRF는 비용·이차 부위 없는 옵션으로 비열등.',
        summary='RCT comparing three jumping-gap fillers (PRF vs xenograft vs alloplastic) at immediate implant placement. All three yielded comparable clinical outcomes; PRF emerges as a low-cost autologous alternative without donor-site morbidity.',
        key_contrib='Direct head-to-head RCT data supporting PRF as a viable alternative to xenograft/alloplastic for jumping-gap management.',
        methodology='Three-arm RCT. Standardized immediate implant placement, jumping gap filled per assignment, follow-up imaging for buccal bone changes and clinical implant outcomes.',
        results='No statistically significant difference between the three groups on primary bone-change endpoints at follow-up. PRF arm showed comparable outcomes to bone substitutes.',
        limitations='Short-term follow-up. Site-specific (anterior maxilla) generalization to molar sockets unclear.',
        related=['immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla',
                 'immediate-implant/wang-2021-titanium-mesh-cgf-immediate-implantation-anterior'],
    ),
    '40729_2020_Article_235': dict(
        stem='ragucci-2020-immediate-implant-molar-extraction-sockets',
        category='immediate-implant',
        year=2020, date='2020-09-21',
        authors='Gian Maria Ragucci, Basel Elnayef, Elena Criado-Cámara, Fernando Suárez-López Del Amo, Federico Hernández-Alfaro',
        title='Immediate implant placement in molar extraction sockets: a systematic review and meta-analysis',
        doi='10.1186/s40729-020-00235-5',
        confidence='sr+ma',
        oneline_kr='SR+MA: 구치부 즉시 식립의 생존율은 통상 ≥97%로 지연 식립과 동등 수준이며, 격중격(inter-radicular septum) 이용·primary stability 확보가 핵심 변수.',
        summary='Systematic review + meta-analysis of immediate implant placement in molar extraction sockets. Pooled survival rates are comparable to delayed placement when primary stability and septum-driven positioning are achieved.',
        key_contrib='First major SR+MA quantifying molar-IIP outcomes; establishes survival benchmarks (~97%) and identifies inter-radicular septum anchorage as a key technique variable.',
        methodology='Systematic literature search; pooled survival and complication rates; subgroup analyses by site (maxillary vs mandibular) and protocol.',
        results='Pooled implant survival ~97–98%, comparable to delayed protocols. Heterogeneity moderate; complication rates dominated by primary stability failures rather than late biology.',
        limitations='Heterogeneity in implant systems and surgical protocols. Limited long-term (>5 yr) data.',
        related=['immediate-implant/smith-2013-classification-molar-extraction-immediate-implant',
                 'immediate-implant/pavlovic-2022-interradicular-septum-morphology-molar-iip',
                 'immediate-implant/milenkovic-2022-interradicular-septum-classification-iip',
                 'immediate-implant/deporter-2021-cbct-immediate-maxillary-molar-implant-planning'],
    ),
    '65': dict(
        stem='habib-2024-srp-decision-making-immediate-implant-cbct',
        category='immediate-implant',
        year=2024, date='2024-02-27',
        authors='Saqib Habib, Momina Anis Motiwala, Farhan Raza Khan',
        title='Does the sagittal root position of maxillary anterior teeth affect the decision making on immediate implants in the anterior maxilla? A CBCT-based study',
        doi='10.17219/dmp/133072',
        confidence='cross-sectional',
        oneline_kr='파키스탄인 CBCT 단면 연구: SRP Class I이 81.7%로 압도적이고 LBT는 대부분 0.5–0.9 mm로 얇음 — 인구 다수가 immediate implant 호적자이나 얇은 협측골은 추가 augmentation 필요성을 시사.',
        summary='Cross-sectional CBCT study in a Pakistani population evaluating SRP (Kan classification) and labial bone thickness (LBT) at three apicocoronal levels in maxillary canine-to-canine teeth.',
        key_contrib='Population-specific prevalence data for SRP and LBT, important because non-Caucasian distributions are under-reported in implant decision-making literature.',
        methodology='Cross-sectional retrospective CBCT review. SRP classified per Kan (Class I/II/III/IV). LBT measured at P1 (crest), P2 (2 mm), P3 (4 mm) perpendicular to tooth long axis.',
        results='Class I = 81.7% (n=196), Class III only 0.4%. Mean LBT 0.5–0.9 mm. No significant association between tooth type and SRP class (p=0.510).',
        limitations='Single-center; younger-skewed sample limits generalizability to elderly bone changes.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/espinoza-espinoza-2023-srp-alveolar-wall-thickness-peruvian',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population'],
    ),
    'Alveolar bone thickness overlying healthy maxillary and mandibular teeth_ A systematic review and meta-analysis - ScienceDirect': dict(
        stem='shafizadeh-2021-alveolar-bone-thickness-healthy-sr',
        category='immediate-implant',
        year=2021, date='2021-09-01',
        authors='Marziyeh Shafizadeh, Azita Tehranchi, Armin Shirvani, Saeed Reza Motamedian',
        title='Alveolar bone thickness overlying healthy maxillary and mandibular teeth: A systematic review and meta-analysis',
        doi='10.1016/j.ortho.2021.07.002',
        confidence='sr+ma',
        oneline_kr='SR+MA: 건강한 치아의 협측 치조골은 전치부에서 가장 얇고(평균 ≤1 mm 다수), 후방으로 갈수록 두꺼워짐 — 성별·흡연은 일관된 연관성 없음. 전치 즉시식립 시 buccal plate 보강 전제 권고.',
        summary='Systematic review and meta-analysis pooling CBCT alveolar bone thickness measurements from healthy dentitions. Confirms anterior teeth carry the thinnest buccal plates, with thickness increasing posteriorly. No consistent gender or smoking effect.',
        key_contrib='Provides pooled reference ranges for alveolar bone thickness by tooth position, a high-leverage input for immediate-implant case selection in the esthetic zone.',
        methodology='Systematic search of CBCT-based bone thickness studies. Meta-analytic pooling by tooth position; subgroup analysis by gender, smoking, age.',
        results='Anterior buccal plate predominantly thin (often ≤1 mm). Posterior regions thicker. No specific gender pattern; no smoking-thickness association.',
        limitations='Heterogeneity in measurement levels (crest vs apex). CBCT voxel size variability across primary studies.',
        related=['immediate-implant/altarawneh-2018-bone-dimensions-anterior-maxilla-cbct',
                 'immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp',
                 'immediate-implant/dossantos-2019-buccal-bone-root-inclination-alveolar-cbct'],
    ),
    'Assessment of Bone Dimensions in the Anterior Maxilla_ A Cone Beam Computed Tomography Study - AlTarawneh - 2018 - Journal of Prosthodontics - Wiley Online Library': dict(
        stem='altarawneh-2018-bone-dimensions-anterior-maxilla-cbct',
        category='immediate-implant',
        year=2018, date='2017-12-13',
        authors='Sandra AlTarawneh, Abeer AlHadidi, Murad Shaqman, Ahmad A Hamdan',
        title='Assessment of Bone Dimensions in the Anterior Maxilla: A Cone Beam Computed Tomography Study',
        doi='10.1111/jopr.12675',
        confidence='cross-sectional',
        oneline_kr='CBCT 단면 연구: 상악 전치부 협측골은 압도적 다수가 1 mm 미만 — 즉시 식립 시 thin-plate 시나리오가 default임을 재확인.',
        summary='Retrospective CBCT study assessing buccal and palatal bone dimensions on anterior maxillary teeth. Confirms majority of buccal plates are <1 mm thick at multiple apicocoronal levels.',
        key_contrib='Adds Middle-East population CBCT data on anterior maxillary bone dimensions; reinforces clinical default that immediate implant in this zone usually faces a thin buccal plate.',
        methodology='Retrospective CBCT measurements of buccal/palatal bone thickness at multiple levels on maxillary canine-to-canine teeth.',
        results='Buccal plate <1 mm in the majority of teeth measured. Palatal bone generally thicker. Statistically significant tooth-position variability.',
        limitations='Cross-sectional; single-center; CBCT voxel size limits sub-millimeter precision.',
        related=['immediate-implant/shafizadeh-2021-alveolar-bone-thickness-healthy-sr',
                 'immediate-implant/jung-2018-anterior-implant-cbct'],
    ),
    'BMRI2021-4754078': dict(
        stem='wang-2021-titanium-mesh-cgf-immediate-implantation-anterior',
        category='immediate-implant',
        year=2021, date='2021-12-30',
        authors='Xianli Wang, Guoqing Wang, Xibo Zhao, Yanchuan Feng, Huijuan Liu, Fang Li',
        title='Short-Term Evaluation of Guided Bone Reconstruction with Titanium Mesh Membranes and CGF Membranes in Immediate Implantation of Anterior Maxillary Tooth',
        doi='10.1155/2021/4754078',
        confidence='retrospective',
        oneline_kr='상악 전치 즉시식립 + GBR에 Ti mesh + CGF 멤브레인 단기 평가: 협측 골 재형성과 연조직 윤곽 유지에 유리한 옵션, 단 mesh 노출 관리가 핵심 limitation.',
        summary='Short-term clinical evaluation of titanium mesh combined with CGF (Concentrated Growth Factor) membranes for GBR at immediate implant placement in anterior maxilla. Reports acceptable hard-tissue reconstruction and contour preservation.',
        key_contrib='Documents a low-cost autologous-CGF + Ti mesh protocol for immediate-implant GBR in the esthetic zone, with attention to mesh exposure rates.',
        methodology='Short-term clinical and radiographic follow-up of immediate-implant GBR cases using Ti mesh + CGF membranes.',
        results='Acceptable bone regeneration on buccal aspect; gingival contour broadly maintained. Mesh exposure occurred in a subset of cases.',
        limitations='Short follow-up; non-comparative; CGF preparation operator-dependent.',
        related=['immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla',
                 'immediate-implant/trombelli-2024-bioarp-bone-dehiscence-immediate-implant'],
    ),
    'CAP-16-82': dict(
        stem='trombelli-2024-bioarp-bone-dehiscence-immediate-implant',
        category='immediate-implant',
        year=2024, date='2024-12-12',
        authors='Leonardo Trombelli, Tommaso Grenzi',
        title='Biologically-oriented alveolar ridge preservation to correct bone dehiscence at immediate implant placement',
        doi='10.1002/cap.10334',
        confidence='case-report',
        oneline_kr='Case study: bone dehiscence를 동반한 즉시 식립에서 BioARP(modified ridge preservation) 적용 — 골 재형성과 연조직 두께 회복 가능성 제시, 그러나 case-level evidence.',
        summary='Case study describing a modification of Biologically-oriented Alveolar Ridge Preservation (BioARP) applied to correct buccal bone dehiscence at immediate implant placement.',
        key_contrib='Technique description bridging traditional ARP and IIP — useful for cases where dehiscence is detected after extraction but immediate placement is still desired.',
        methodology='Single case report (or small case series). Step-by-step BioARP protocol with grafting and primary closure adjuncts at IIP.',
        results='Reported successful dehiscence resolution and acceptable peri-implant bone outcomes at follow-up.',
        limitations='Case-level evidence; no comparator; operator-dependent.',
        related=['immediate-implant/grenzi-2026-spal-peri-implant-bone-dehiscence-iip',
                 'immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla'],
    ),
    'Classification of Molar Extraction Sites for Immediate Dental Implant Placement_ Technical Note _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='smith-2013-classification-molar-extraction-immediate-implant',
        category='immediate-implant',
        year=2013, date='2013-06-10',
        authors='Richard B. Smith, Dennis P. Tarnow',
        title='Classification of Molar Extraction Sites for Immediate Dental Implant Placement: Technical Note',
        doi='10.11607/jomi.2627',
        confidence='narrative-review',
        oneline_kr='랜드마크 technical note: 구치 발치와를 type A(격중격으로 안정 확보), type B(부분 의존), type C(불가)로 3분류 — 이후 molar IIP planning의 표준 분류 체계가 됨.',
        summary='Technical note introducing the A/B/C classification of molar extraction sockets for immediate implant placement based on the inter-radicular bone available for primary stability.',
        key_contrib='Foundational classification system used in virtually all subsequent molar-IIP literature. Anchors the decision of whether a molar socket is amenable to immediate implant.',
        methodology='Conceptual classification + clinical illustration. Type A: implant fully engages inter-radicular bone; Type B: partial engagement requiring stability from socket walls/apical bone; Type C: insufficient bone for predictable stability.',
        results='Provides a treatment-decision framework that subsequent studies (Pavlovic 2022, Milenkovic 2022, Deporter 2021, Ragucci 2020) operationalize via CBCT measurements.',
        limitations='Not an outcome study; classification not validated against survival data within this paper.',
        related=['immediate-implant/ragucci-2020-immediate-implant-molar-extraction-sockets',
                 'immediate-implant/pavlovic-2022-interradicular-septum-morphology-molar-iip',
                 'immediate-implant/milenkovic-2022-interradicular-septum-classification-iip'],
    ),
    'Clinical Outcomes of Maxillary Anterior Postextraction Socket Implants with Immediate Provisional Restorations Using a Novel Macro-Hybrid Implant Design_ An 18- to 24-Month Single-Cohort Prospective Study _ Quintessence Publishing USA _ Quintessence P': dict(
        stem='ostman-2020-macro-hybrid-implant-anterior-postextraction',
        category='immediate-implant',
        year=2020, date='2020-04-09',
        authors='Pär-Olov Östman, Stephen J. Chu, Carl Drago, Hanae Saito, Myron Nevins',
        title='Clinical Outcomes of Maxillary Anterior Postextraction Socket Implants with Immediate Provisional Restorations Using a Novel Macro-Hybrid Implant Design: An 18- to 24-Month Single-Cohort Prospective Study',
        doi='10.11607/prd.4467',
        confidence='prospective',
        oneline_kr='18~24개월 전향적 단일군: 신형 macro-hybrid 디자인 임플란트로 전치부 즉시식립+즉시 임시 보철 시 양호한 esthetic outcome과 골 안정성 — 디자인 선택이 esthetic 위험 완화에 기여 가능성 제시.',
        summary='Single-cohort prospective study (18–24 month follow-up) of immediate implant placement with immediate provisional restoration in maxillary anterior sockets using a novel macro-hybrid implant design.',
        key_contrib='Demonstrates that purpose-designed macro-hybrid implant geometry may mitigate the dehiscence/recession risk traditionally associated with IIPP in the anterior maxilla.',
        methodology='Single-arm prospective cohort. Maxillary anterior IIPP cases with the test implant design. Esthetic, radiographic, and clinical outcome assessment at 18–24 months.',
        results='High survival, acceptable peri-implant bone stability, and esthetic outcomes within reported benchmarks. Recession events lower than historical IIPP series.',
        limitations='Single-arm (no comparator); industry-related implant design; short-to-mid-term follow-up.',
        related=['immediate-implant/chu-2020-itrt-platform-switched-subcrestal-angle-correction',
                 'immediate-implant/galve-huertas-2024-inverted-body-shift-design-pilot',
                 'immediate-implant/galve-huertas-2026-inverted-body-shift-vs-conical-rct'],
    ),
    'Clinical, radiographic, and esthetic evaluation of immediate implant placement with buccal bone dehiscence in the anterior maxilla_ A 1‐year prospective case series - Qian - 2023 - Clinical Implant Dentistry and Related Research - Wiley Online Libra': dict(
        stem='qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla',
        category='immediate-implant',
        year=2023, date='2022-11-14',
        authors='Shu-Jiao Qian, Yi-ping Pu, et al.',
        title='Clinical, radiographic, and esthetic evaluation of immediate implant placement with buccal bone dehiscence in the anterior maxilla: A 1-year prospective case series',
        doi='10.1111/cid.13154',
        confidence='prospective',
        oneline_kr='1년 전향적 case series: 협측 골열개를 동반한 전치부 즉시식립도 적절한 GBR과 함께 임상·방사선·심미적으로 수용 가능한 결과 — 단, "절대 금기"가 아니라 risk-managed 시술임을 강조.',
        summary='1-year prospective case series of immediate implant placement performed in maxillary anterior sites with pre-existing buccal bone dehiscence, combined with simultaneous GBR.',
        key_contrib='Provides outcome evidence that the historical contraindication of dehiscence to IIP can be relaxed with disciplined GBR — informs case selection criteria.',
        methodology='Prospective single-arm case series. Buccal dehiscence cases received IIP + GBR. Clinical, radiographic, esthetic (PES/WES) outcomes at 1 year.',
        results='Survival 100% in this short term, with acceptable PES/WES and contained radiographic bone changes. Recession remained the main esthetic risk.',
        limitations='Small n; 1-year follow-up; no comparator group.',
        related=['immediate-implant/pohl-2022-iipp-anterior-maxilla-buccal-dehiscence-pilot',
                 'immediate-implant/nassani-2025-immediate-vs-delayed-bony-defect-commentary',
                 'immediate-implant/trombelli-2024-bioarp-bone-dehiscence-immediate-implant'],
    ),
    'Esthetic Outcomes for Immediate Implant Placement with Immediate Provisionalization in the Anterior Maxilla with Buccal Dehiscence_ Results of a Comparative Pilot Study _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='pohl-2022-iipp-anterior-maxilla-buccal-dehiscence-pilot',
        category='immediate-implant',
        year=2022, date='2022-06-27',
        authors='Veronika Pohl, Julia Cede, Georg Benedikt Mailath Pokorny, Robert Haas, Sebastian Pohl',
        title='Esthetic Outcomes for Immediate Implant Placement with Immediate Provisionalization in the Anterior Maxilla with Buccal Dehiscence: Results of a Comparative Pilot Study',
        doi='10.11607/jomi.9198',
        confidence='prospective',
        oneline_kr='파일럿 비교 연구: 협측 dehiscence가 있는 전치부에서도 IIPP의 esthetic outcome이 무결 socket과 통계적으로 큰 차이 없이 수용 가능 — 단, 표본 작음.',
        summary='Comparative pilot study evaluating esthetic outcomes of immediate implant placement with immediate provisionalization in maxillary anterior sites with vs without buccal dehiscence.',
        key_contrib='Adds early comparative evidence that dehiscence cases, with proper protocol, can match intact-socket esthetic outcomes — challenging strict contraindications.',
        methodology='Pilot comparative study with dehiscence vs intact-socket arms. PES/WES and recession measured.',
        results='Esthetic indices comparable across arms within the small-sample limits. Recession trended higher but not statistically significant in dehiscence arm.',
        limitations='Pilot (low n, low power); unblinded; short term.',
        related=['immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla',
                 'immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp'],
    ),
    'Feasibility of Immediate Implant Placement in Maxillary First Premolars_ Prediction of Implant Locations Using Restorations—A Radiographic Study _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='kheur-2024-feasibility-iip-maxillary-first-premolars',
        category='immediate-implant',
        year=2024, date='2024-03-12',
        authors='Mohit Kheur, Shifa Kalsekar, Supriya Kheur, Ronald E. Jung, Tabrez Lakha',
        title='Feasibility of Immediate Implant Placement in Maxillary First Premolars: Prediction of Implant Locations Using Restorations—A Radiographic Study',
        doi='10.11607/ijp.8757',
        confidence='cross-sectional',
        oneline_kr='150개 CBCT 분석: 상악 제1소구치 즉시식립의 위치는 보철 driven으로 분류 가능 — 단순 분류 체계 제안, 실제 술전 stability 예측은 별도 변수 필요.',
        summary='Radiographic feasibility study on 150 CBCTs of maxillary first premolars, proposing a prosthetically-driven classification system to predict optimal immediate implant location.',
        key_contrib='First-premolar–specific classification framework adapted from molar-IIP thinking — helps decide between socket-driven vs septum-driven anchorage.',
        methodology='Retrospective CBCT analysis of 150 maxillary first premolars in BlueskyBio software. Restoration-based planning to predict implant trajectory.',
        results='Substantial proportion of cases amenable to inter-radicular septum anchorage; a subset would require palatal-wall reliance.',
        limitations='Anatomy-only; no outcome data; single population.',
        related=['immediate-implant/smith-2013-classification-molar-extraction-immediate-implant',
                 'immediate-implant/deporter-2021-cbct-immediate-maxillary-molar-implant-planning'],
    ),
    'Flapless immediate implant placement and provisionalisation (FIIPP) using a palatal implant position (≥ 2 mm)_ A prospective multicentre CBCT study with a 3-year follow-up - PubMed': dict(
        stem='staas-2026-fiipp-palatal-position-cbct-3year',
        category='immediate-implant',
        year=2026, date='2026-03-13',
        authors='Tristan Ariaan Staas, Edith Groenendijk, Erika Hamerslag, Ewald Bronkhorst, Luc Verhamme, Gerry Max Raghoebar, Gerrit Jacobus Meijer',
        title='Flapless immediate implant placement and provisionalisation (FIIPP) using a palatal implant position (≥ 2 mm): A prospective multicentre CBCT study with a 3-year follow-up',
        doi='',
        confidence='prospective',
        oneline_kr='3년 다기관 전향 CBCT: 협측에서 ≥2 mm 구개측 위치를 일관 적용한 flapless IIPP는 buccal crest 두께·높이를 보존 — palatal positioning 원칙의 명확한 양적 근거.',
        summary='Prospective multi-center CBCT study of flapless IIPP with implant positioned ≥2 mm palatal to the buccal crest, followed for 3 years. Demonstrates preservation of buccal crest thickness and height.',
        key_contrib='Strong prospective evidence for the "≥2 mm palatal" positioning rule as a buccal-bone-preservation strategy in IIPP, with mid-term follow-up.',
        methodology='Multi-center prospective cohort. Standardized flapless IIPP protocol with palatal positioning. CBCT measurements baseline and 3 years.',
        results='Buccal crest thickness and height maintained over 3 years in the cohort. Implant survival within expected high range.',
        limitations='No comparator arm with non-palatal positioning; flapless requires specific anatomy/operator skill.',
        related=['immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp',
                 'immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior'],
    ),
    'Immediate Implant Placement in the Esthetic Area Using an Inverted Body-Shift Design_ A Prospective Clinical Pilot Study _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='galve-huertas-2024-inverted-body-shift-design-pilot',
        category='immediate-implant',
        year=2024, date='2024-05-08',
        authors='Andrea Galve-Huertas, Erika Brancacci, Susana García-González, Octavi Ortíz-Puigpelat, Federico Hernández-Alfaro, Samir Aboul-Hosn Centenero',
        title='Immediate Implant Placement in the Esthetic Area Using an Inverted Body-Shift Design: A Prospective Clinical Pilot Study',
        doi='10.11607/prd.7109',
        confidence='prospective',
        oneline_kr='12명 파일럿: 12° angled platform의 inverted body-shift 임플란트 디자인이 esthetic 영역 즉시식립에서 protrusion 위험을 줄이는 macro-design 옵션 — 정식 RCT는 후속.',
        summary='Prospective clinical pilot study of an inverted body-shift implant design with a 12-degree angled platform for immediate placement in the esthetic zone.',
        key_contrib='Establishes proof-of-concept for an angle-corrective implant geometry, which is later compared to conventional conical implants in Galve-Huertas 2026 RCT.',
        methodology='Prospective single-arm pilot. Twelve patients. IIP with immediate provisionalization using test implant. Clinical and radiographic follow-up.',
        results='Survival 100% in pilot; favorable trajectory control and provisional emergence profile.',
        limitations='Pilot scale (n=12); no comparator; industry-aligned implant.',
        related=['immediate-implant/galve-huertas-2026-inverted-body-shift-vs-conical-rct',
                 'immediate-implant/chu-2020-itrt-platform-switched-subcrestal-angle-correction',
                 'immediate-implant/ostman-2020-macro-hybrid-implant-anterior-postextraction'],
    ),
    'Immediate Tooth Replacement Therapy in Postextraction Sockets_ A Comparative Prospective Study on the Effect of Variable Platform-Switched Subcrestal Angle Correction Implants _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='chu-2020-itrt-platform-switched-subcrestal-angle-correction',
        category='immediate-implant',
        year=2020, date='2020-06-30',
        authors='Stephen J. Chu, Hanae Saito, Pär-Olov Östman, Barry P. Levin, Mark A. Reynolds, Dennis P. Tarnow',
        title='Immediate Tooth Replacement Therapy in Postextraction Sockets: A Comparative Prospective Study on the Effect of Variable Platform-Switched Subcrestal Angle Correction Implants',
        doi='10.11607/prd.4440',
        confidence='prospective',
        oneline_kr='전향적 비교 연구: subcrestal angle correction이 가능한 platform-switched 임플란트는 단축 임플란트에서도 즉시식립 + 즉시 임시보철 시 socket perforation 회피와 양호한 ITRT 결과 가능.',
        summary='Comparative prospective study evaluating a variable platform-switched subcrestal angle-correction implant in ITRT (immediate tooth replacement therapy), aimed at avoiding socket perforation under uniaxial implant placement.',
        key_contrib='Validates angle-correction implant geometry as a tool to reconcile prosthetic-driven positioning with bony-housing constraints in postextraction sockets.',
        methodology='Comparative prospective design. ITRT cases with the angle-correction implant vs reference. Clinical and radiographic outcomes through ~12 months.',
        results='Favorable soft-tissue stability and esthetic outcomes with the test implant. Reduced incidence of unfavorable socket perforation events.',
        limitations='Industry-aligned implant; not a true RCT; medium-term follow-up.',
        related=['immediate-implant/ostman-2020-macro-hybrid-implant-anterior-postextraction',
                 'immediate-implant/galve-huertas-2024-inverted-body-shift-design-pilot'],
    ),
    'Immediate loading of post-extractive versus delayed placed single implants in the anterior maxilla_ outcome of a pragmatic multicenter randomised controlled trial 1-year after loading - PubMed': dict(
        stem='esposito-2015-immediate-loading-vs-delayed-anterior-rct',
        category='immediate-implant',
        year=2015, date='2015-12-01',
        authors='Marco Esposito, Carlo Barausse, Roberto Pistilli, Michele Jacotti, Giovanni Grandi, Lorenzo Tuco, Pietro Felice',
        title='Immediate loading of post-extractive versus delayed placed single implants in the anterior maxilla: outcome of a pragmatic multicenter randomised controlled trial 1-year after loading',
        doi='',
        confidence='rct',
        oneline_kr='실용주의 다기관 RCT (Eur J Oral Implantol 2015): 전치부 즉시 부하 IIP vs 4개월 healing 후 지연 식립 — 1년 시점 implant 실패율과 esthetic outcome은 유의차 없음, 단 충분한 insertion torque(≥35 Ncm) 전제.',
        summary='Pragmatic multicenter RCT comparing immediate-loading post-extractive single implants vs delayed implants placed in preserved sockets after 4 months, in the anterior maxilla. Reports 1-year outcomes.',
        key_contrib='Provides high-quality RCT evidence that, with appropriate primary stability gating (≥35 Ncm), immediate post-extractive single implants are non-inferior to delayed placement at 1 year.',
        methodology='Pragmatic RCT (multicenter). Anterior maxilla single tooth. Randomization to immediate post-extractive vs delayed (after 4 months socket preservation). 1-year follow-up.',
        results='No significant differences in failure rates or main esthetic/clinical outcomes between immediate and delayed arms at 1 year.',
        limitations='1-year horizon; pragmatic design admits operator variability; primary stability gating selects favorable cases.',
        related=['immediate-implant/nassani-2025-immediate-vs-delayed-bony-defect-commentary',
                 'immediate-implant/ragucci-2020-immediate-implant-molar-extraction-sockets'],
    ),
    'Immediate versus delayed single-tooth implant placement in bony defect sockets in the aesthetic zone_ Is an intact buccal wall necessary_ - PubMed': dict(
        stem='nassani-2025-immediate-vs-delayed-bony-defect-commentary',
        category='immediate-implant',
        year=2025, date='2025-05-13',
        authors='Mohammad Zakaria Nassani',
        title='Immediate versus delayed single-tooth implant placement in bony defect sockets in the aesthetic zone: Is an intact buccal wall necessary? (commentary on Meijer 2025)',
        doi='10.1038/s41432-025-01152-5',
        confidence='narrative-review',
        oneline_kr='Evid Based Dent 코멘터리: Meijer 2025의 10년 RCT에 대한 비판적 리뷰 — 본 RCT는 협측벽 결손 socket에서도 즉시 식립이 지연 식립에 비열등함을 시사, 그러나 일반화에는 case selection 신중 필요.',
        summary='Commentary on Meijer et al. 2025 (J Periodontol), a single-center 10-year RCT comparing immediate vs delayed single-tooth implant placement in bony defect sockets in the aesthetic zone.',
        key_contrib='Frames the long-term RCT evidence challenging the "intact buccal wall is mandatory" dogma for IIP. Highlights selection-bias caveats.',
        methodology='Narrative commentary on a 10-year RCT. Critical appraisal of design and applicability.',
        results='Meijer 2025 reports comparable outcomes in immediate vs delayed arms in bony-defect sockets over 10 years; commentary cautions about generalization.',
        limitations='Commentary not original data. Underlying RCT is single-center.',
        related=['immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla',
                 'immediate-implant/pohl-2022-iipp-anterior-maxilla-buccal-dehiscence-pilot',
                 'immediate-implant/esposito-2015-immediate-loading-vs-delayed-anterior-rct'],
    ),
    'JDRAS-36-088': dict(
        stem='kong-2020-srp-maxillary-anterior-korean-population',
        category='immediate-implant',
        year=2020, date='2020-06-30',
        authors='Hyun-Jun Kong',
        title='A study on sagittal root position of maxillary anterior teeth in Korean',
        doi='10.14368/jdras.2020.36.2.88',
        confidence='cross-sectional',
        oneline_kr='한국인 CBCT 후향 분석(n=120): SRP Class I 81.1%, II 10.3%, III 1.9%, IV 6.7% — 다수가 협측 cortex에 근접, 일부는 angulation ≥30°로 immediate implant 시 trajectory 위험. 한국인 데이터.',
        summary='Retrospective CBCT study of 120 Korean patients reporting prevalence of Kan-class SRP and sagittal angulation of maxillary anterior teeth.',
        key_contrib='Korean-population–specific SRP and angulation reference; directly applicable to local clinical planning of immediate implant cases.',
        methodology='Retrospective CBCT review of 120 patients (60M/60F). SRP classified Kan I–IV. Sagittal root-to-bone angulation measured.',
        results='Class I 81.1%, II 10.3%, III 1.9%, IV 6.7%. 77.5% of incisors/canines had angulation <20°, but >42.7% of canines had angulation ≥20°. Class I had largest mean angulation (16.19°); Class IV smallest (3.79°).',
        limitations='Single-center Korean sample; CBCT measurement variability; no outcome data.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/habib-2024-srp-decision-making-immediate-implant-cbct',
                 'immediate-implant/rodrigues-2022-srp-brazilian-anterior-bone-housing-isd'],
    ),
    'JIPS-18-356': dict(
        stem='panda-2018-cbct-incisive-canal-anterior-maxillary',
        category='immediate-implant',
        year=2018, date='2018-10-01',
        authors='Mousumi Panda, Thatapudi Shankar, Anjana Raut, Shruti Dev, Aswini Kumar Kar, Sadanand Hota',
        title='Cone beam computerized tomography evaluation of incisive canal and anterior maxillary bone thickness for placement of immediate implants',
        doi='10.4103/jips.jips_103_18',
        confidence='cross-sectional',
        oneline_kr='CBCT 단면(인도 인구): 절치공(incisive canal) 위치 및 전치부 골 두께 평가 — 즉시 식립 시 절치공 침범 위험과 협측·구개측 골 잔량을 정량.',
        summary='Cross-sectional CBCT study evaluating incisive canal dimensions and anterior maxillary bone thickness, with implications for immediate implant placement risk of canal perforation.',
        key_contrib='Highlights incisive canal as a frequently under-appreciated anatomic constraint in central incisor IIP, especially when palatal positioning is pursued for buccal bone preservation.',
        methodology='Retrospective CBCT measurements: incisive canal dimensions, position relative to central incisors, and labial/palatal bone thickness.',
        results='Provides population-specific dimensional data. Quantifies how palatal IIP trajectories may approach canal walls.',
        limitations='Cross-sectional; single population; no outcome data.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/altarawneh-2018-bone-dimensions-anterior-maxilla-cbct'],
    ),
    'JOMI-2011-Sagittal-Root-Position-[Kan-': dict(
        stem='kan-2011-sagittal-root-position-immediate-implant-anterior',
        category='immediate-implant',
        year=2011, date='2011-07-01',
        authors='Joseph Y.K. Kan, Kitichai Rungcharassaeng, Kazuyoshi Morimoto, Phillip Lozada',
        title='Sagittal root position of the maxillary anterior teeth: Implications for immediate implant placement',
        doi='',
        confidence='cross-sectional',
        oneline_kr='Landmark 논문: 상악 전치의 sagittal root position을 Class I–IV로 분류, 이후 즉시 식립 영역의 표준 분류 체계가 됨. Class I이 압도적으로 흔하고 protrusion 위험을 정량화.',
        summary='Landmark CBCT study introducing the Kan classification of sagittal root position (SRP) for maxillary anterior teeth (Class I–IV), with prevalence data and direct implications for immediate implant placement trajectory.',
        key_contrib='Introduces the four-class SRP system that virtually every subsequent IIP-planning paper references. Standardizes how clinicians describe root-to-bone relationships in the esthetic zone.',
        methodology='CBCT analysis. Maxillary anterior teeth classified by root engagement with cortical plates: Class I (labial), Class II (centered), Class III (palatal), Class IV (both labial and palatal).',
        results='Class I most prevalent. Establishes that the typical anterior tooth root sits against the labial cortex, with implications for fenestration/protrusion risk during IIP.',
        limitations='Original cohort population-specific; CBCT voxel precision limits sub-mm interpretation.',
        related=['immediate-implant/habib-2024-srp-decision-making-immediate-implant-cbct',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population',
                 'immediate-implant/espinoza-espinoza-2023-srp-alveolar-wall-thickness-peruvian',
                 'immediate-implant/rodrigues-2022-srp-periodontal-phenotype-anterior-maxillary',
                 'immediate-implant/rodrigues-2022-srp-brazilian-anterior-bone-housing-isd',
                 'immediate-implant/abdul-2024-srp-maxillary-mandibular-anterior-cbct',
                 'immediate-implant/petaibunlue-2019-anterior-arch-root-position-angulation'],
    ),
    'Relationship Between Sagittal Root Position and Alveolar Wall Thickness of Maxillary Teeth in the Esthetic Area for Immediate Implant Treatment Planning in a Peruvian Population _ Quintessence Publishing USA _ Quintessence Publishing Company, Inc_': dict(
        stem='espinoza-espinoza-2023-srp-alveolar-wall-thickness-peruvian',
        category='immediate-implant',
        year=2023, date='2023-10-12',
        authors='Daniel Alonso Kim Espinoza-Espinoza, Nelly María García-Madueño, Julissa Amparo Dulanto-Vargas, Fiorella Estefanie Lamas-Castillo, Kilder Maynor Carranza-Samanez, Christian Alexander Loo',
        title='Relationship Between Sagittal Root Position and Alveolar Wall Thickness of Maxillary Teeth in the Esthetic Area for Immediate Implant Treatment Planning in a Peruvian Population',
        doi='10.11607/prd.6854',
        confidence='cross-sectional',
        oneline_kr='페루인 CBCT 후향 연구: SRP와 facial/palatal alveolar wall thickness(AWT)의 관계 — Kan-class별 AWT 분포 자료, 인구별 차이 강조.',
        summary='Retrospective CBCT study in a Peruvian population evaluating facial and palatal alveolar wall thickness in relation to Kan-class sagittal root position of maxillary anterior teeth.',
        key_contrib='Adds another non-Caucasian population dataset to the SRP/AWT literature, useful for clinicians treating Latin American patients.',
        methodology='Retrospective CBCT analysis. SRP classified per Kan. AWT measured facially and palatally at standard apicocoronal levels.',
        results='Population-specific distributions of Kan classes and AWT values reported. Class I dominant; facial AWT trends towards thin.',
        limitations='Cross-sectional; single-center; no outcome data.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/habib-2024-srp-decision-making-immediate-implant-cbct',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population'],
    ),
    'Relationship between anterior maxillary tooth sagittal root position and periodontal phenotype_ a clinical and tomographic study _ Clinical Oral Investigations _ Springer Nature Link': dict(
        stem='rodrigues-2022-srp-periodontal-phenotype-anterior-maxillary',
        category='immediate-implant',
        year=2022, date='2021-09-16',
        authors='Diogo M. Rodrigues, Rodrigo L. Petersen, Caroline Montez, José R. de Moraes, Alessandro L. Januário, Eliane P. Barboza',
        title='Relationship between anterior maxillary tooth sagittal root position and periodontal phenotype: a clinical and tomographic study',
        doi='10.1007/s00784-021-04162-6',
        confidence='cross-sectional',
        oneline_kr='임상+CBCT 통합 분석: SRP class와 치주 phenotype(gingival biotype, bone thickness) 사이 연관 — Class IV/얇은 phenotype 조합은 즉시식립 시 high-risk profile.',
        summary='Clinical + tomographic study evaluating the relationship between Kan-class SRP and periodontal phenotype (gingival biotype, bone wall thickness) in maxillary anterior teeth.',
        key_contrib='Bridges hard-tissue (SRP/AWT) and soft-tissue (phenotype) risk factors for IIP esthetic outcomes — useful for compound risk scoring.',
        methodology='Combined clinical phenotype assessment (probe transparency / direct visualization) with CBCT-derived SRP and bone thickness.',
        results='Significant associations between SRP class and phenotype dimensions. Thinner phenotypes overrepresented in Class I and Class IV groups, the highest-risk profiles for IIP recession.',
        limitations='Cross-sectional; phenotype assessment partially subjective.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp',
                 'immediate-implant/rodrigues-2022-srp-brazilian-anterior-bone-housing-isd'],
    ),
    'Subperiosteal peri‐implant augmented layer to correct bone dehiscence at immediate implant placement - Grenzi - Clinical Advances in Periodontics - Wiley Online Library': dict(
        stem='grenzi-2026-spal-peri-implant-bone-dehiscence-iip',
        category='immediate-implant',
        year=2026, date='2026-04-30',
        authors='Tommaso Grenzi, Chiara Franzini, Mattia Severi, Leonardo Trombelli',
        title='Subperiosteal peri-implant augmented layer to correct bone dehiscence at immediate implant placement',
        doi='10.1002/cap.70070',
        confidence='case-report',
        oneline_kr='Case study: SPAL(subperiosteal peri-implant augmented layer) 기법으로 IIP 동시 peri-implant bone dehiscence(PIBD) 교정 — 막 노출 없이 봉합 가능한 dehiscence 관리 옵션.',
        summary='Case study describing the SPAL (subperiosteal peri-implant augmented layer) technique applied at immediate implant placement to correct peri-implant bone dehiscence.',
        key_contrib='Operationalizes the SPAL technique in IIP context, complementing other dehiscence-correction approaches (Trombelli 2024 BioARP) by the same group.',
        methodology='Case study of two patients undergoing IIP at compromised sockets with SPAL technique. Step-by-step surgical description with imaging follow-up.',
        results='Reported successful bone-volume restoration on the buccal aspect, primary closure, and acceptable peri-implant outcomes.',
        limitations='Case-level evidence (n=2); operator skill demanding.',
        related=['immediate-implant/trombelli-2024-bioarp-bone-dehiscence-immediate-implant',
                 'immediate-implant/qian-2023-iip-buccal-bone-dehiscence-anterior-maxilla'],
    ),
    'The thickness of labial bone affects the esthetics of immediate implant placement and provisionalization in the esthetic zone_ A prospective cohort study - Yang - 2019 - Clinical Implant Dentistry and Related Research - Wiley Online Library': dict(
        stem='yang-2019-labial-bone-thickness-esthetics-iipp',
        category='immediate-implant',
        year=2019, date='2019-04-29',
        authors='Xingmei Yang, Tengfei Zhou, Nan Zhou, Yi Man',
        title='The thickness of labial bone affects the esthetics of immediate implant placement and provisionalization in the esthetic zone: A prospective cohort study',
        doi='10.1111/cid.12785',
        confidence='prospective',
        oneline_kr='전향적 cohort: IIPP 시 labial bone thickness가 esthetic outcome(PES/WES)을 유의하게 좌우 — 1–2 mm 권고가 임상적으로 정당화되는 근거.',
        summary='Prospective cohort study quantifying the impact of labial bone thickness on PES/WES esthetic outcomes after immediate implant placement with immediate provisionalization in the esthetic zone.',
        key_contrib='Provides direct outcome evidence underpinning the "1–2 mm labial plate" rule of thumb in IIPP — useful for case-selection thresholding.',
        methodology='Prospective cohort. Pre-op CBCT-derived labial bone thickness stratification. PES/WES, recession, and bone-level outcomes at follow-up.',
        results='Esthetic outcomes deteriorate as labial bone thickness decreases. The 1–2 mm threshold shows a clinically meaningful inflection.',
        limitations='Cohort (non-randomized); follow-up bound by study horizon; threshold values still population-specific.',
        related=['immediate-implant/shafizadeh-2021-alveolar-bone-thickness-healthy-sr',
                 'immediate-implant/altarawneh-2018-bone-dimensions-anterior-maxilla-cbct',
                 'immediate-implant/staas-2026-fiipp-palatal-position-cbct-3year'],
    ),
    'cureus-0015-00000041608': dict(
        stem='aldahlawi-2023-cbct-alveolar-bone-maxillary-mandibular-molars',
        category='immediate-implant',
        year=2023, date='2023-07-09',
        authors='Salwa Aldahlawi, Dalia M. Nourah, Raneem Y. Azab, Jawan A. Binyaseen, Ethar A. Alsehli, Halema F. Zamzami, Omair M. Bukhari',
        title='Cone-Beam Computed Tomography (CBCT)-Based Assessment of the Alveolar Bone Anatomy of the Maxillary and Mandibular Molars: Implication for Immediate Implant Placement',
        doi='10.7759/cureus.41608',
        confidence='cross-sectional',
        oneline_kr='Saudi 인구 CBCT 단면: 상·하악 대구치의 inter-radicular bone, 협측·설측 thickness, 상악동 floor·하악관까지 거리 등을 정량 — molar IIP 적응증 결정 입력 데이터.',
        summary='CBCT cross-sectional study assessing alveolar bone anatomy of maxillary and mandibular molars in a Saudi population, framed as inputs for immediate molar implant decision-making.',
        key_contrib='Adds Middle-East population-specific molar anatomy reference data and quantifies the proportion of sites compatible with septum-anchorage IIP.',
        methodology='Retrospective CBCT review. Inter-radicular septum dimensions, buccal/lingual bone thickness, distance to anatomical limits.',
        results='Significant fraction of maxillary molar sites with septum width sufficient for primary stability; mandibular molars often constrained by lingual concavity and mandibular canal proximity.',
        limitations='Anatomy-only; single-center; no outcome data.',
        related=['immediate-implant/ragucci-2020-immediate-implant-molar-extraction-sockets',
                 'immediate-implant/pavlovic-2022-interradicular-septum-morphology-molar-iip',
                 'immediate-implant/milenkovic-2022-interradicular-septum-classification-iip',
                 'immediate-implant/deporter-2021-cbct-immediate-maxillary-molar-implant-planning'],
    ),
    'cureus-0016-00000071152': dict(
        stem='liu-2024-maxillary-immediate-molar-palatal-root-socket',
        category='immediate-implant',
        year=2024, date='2024-10-09',
        authors='Guanqi Liu, Runheng Liu',
        title='Maxillary Immediate Molar Implant Placement Into Palatal Root Socket: A Case Report of Two-Year Follow-Up',
        doi='10.7759/cureus.71152',
        confidence='case-report',
        oneline_kr='Case report (2년 추적): 상악 대구치 발치 시 palatal root socket을 단일 지지부로 사용한 즉시 식립 — 격중격이 불충분한 경우의 대안 기법.',
        summary='Case report (2-year follow-up) of maxillary immediate molar implant placement using the palatal root socket as the primary anchorage when inter-radicular septum is inadequate.',
        key_contrib='Provides a documented alternative anchorage approach (palatal-root socket) for molar sites that do not satisfy Smith-Tarnow Type A criteria.',
        methodology='Single-case description with 2-year clinical and radiographic follow-up.',
        results='Implant integration and stable peri-implant bone at 2 years in the reported case.',
        limitations='Case-level evidence; technique-sensitive; requires sufficient palatal-root socket volume.',
        related=['immediate-implant/smith-2013-classification-molar-extraction-immediate-implant',
                 'immediate-implant/ragucci-2020-immediate-implant-molar-extraction-sockets',
                 'immediate-implant/yaghmai-2025-palatal-root-socket-all-on-x'],
    ),
    'cureus-0017-00000096476': dict(
        stem='yaghmai-2025-palatal-root-socket-all-on-x',
        category='immediate-implant',
        year=2025, date='2025-11-10',
        authors='Pedram Yaghmai, Gregori M. Kurtzman',
        title='Implant Placement in the Palatal Root Socket of Maxillary Molars to Avoid Posterior Cantilevers in All-on-X Treatments',
        doi='10.7759/cureus.96476',
        confidence='case-report',
        oneline_kr='Case report: All-on-X에서 후방 cantilever를 줄이기 위해 상악 대구치의 palatal root socket에 임플란트 배치 — 즉시식립과 full-arch 보철 설계를 연결.',
        summary='Case report describing immediate implant placement into maxillary molar palatal root sockets specifically to provide distal support in All-on-X full-arch rehabilitations, avoiding long cantilevers.',
        key_contrib='Connects molar-palatal-root IIP technique with full-arch (All-on-X) prosthetic planning — an emerging cross-over indication.',
        methodology='Case descriptions with prosthetic planning rationale and surgical approach.',
        results='Reported successful integration and prosthetic loading without distal cantilever in the documented cases.',
        limitations='Case-level evidence; technique-sensitive; lacks comparative outcome data.',
        related=['immediate-implant/liu-2024-maxillary-immediate-molar-palatal-root-socket',
                 'immediate-implant/smith-2013-classification-molar-extraction-immediate-implant'],
    ),
    'diagnostics-12-01010': dict(
        stem='pavlovic-2022-interradicular-septum-morphology-molar-iip',
        category='immediate-implant',
        year=2022, date='2022-04-16',
        authors='Zlata Rajkovic Pavlovic, Pavle Milanovic, Milica Vasiljevic, Nemanja Jovicic, Aleksandra Arnaut, Djurdjina Colic, Marijana Petrovic, Momir Stevanovic, Dragica Selakovic, Gvozden Rosic',
        title='Assessment of Maxillary Molars Interradicular Septum Morphological Characteristics as Criteria for Ideal Immediate Implant Placement—The Advantages of Cone Beam Computed Tomography Analysis',
        doi='10.3390/diagnostics12041010',
        confidence='cross-sectional',
        oneline_kr='CBCT 단면: 상악 대구치 격중격(IRS) 형태·크기를 morphological criterion으로 분류, ideal molar IIP 적응 결정에 활용 가능한 입력 데이터 제공.',
        summary='CBCT cross-sectional analysis of maxillary molar inter-radicular septum (IRS) morphology, framed as objective criteria for IIP feasibility.',
        key_contrib='Provides shape/size IRS criteria that operationalize Smith-Tarnow Type A vs B/C in molar IIP planning.',
        methodology='Retrospective CBCT review of maxillary first/second molars. IRS dimensions measured at multiple levels; morphology classified.',
        results='Substantial site-to-site variability; quantifies the prevalence of "ideal IIP" anatomy in this population.',
        limitations='Cross-sectional anatomy-only; single population.',
        related=['immediate-implant/milenkovic-2022-interradicular-septum-classification-iip',
                 'immediate-implant/smith-2013-classification-molar-extraction-immediate-implant',
                 'immediate-implant/deporter-2021-cbct-immediate-maxillary-molar-implant-planning'],
    ),
    'diagnostics-12-01432': dict(
        stem='milenkovic-2022-interradicular-septum-classification-iip',
        category='immediate-implant',
        year=2022, date='2022-06-10',
        authors='Jovana Milenkovic, Milica Vasiljevic, Nemanja Jovicic, Dragan Milovanovic, Dragica Selakovic, Gvozden Rosic',
        title='Criteria for the Classification of the Interradicular Septum Shape in Maxillary Molars with Clinical Importance for Prosthetic-Driven Immediate Implant Placement',
        doi='10.3390/diagnostics12061432',
        confidence='cross-sectional',
        oneline_kr='격중격(IRS) shape를 prosthetic-driven IIP에 맞춰 분류하는 기준 제안 — Pavlovic 2022와 짝을 이루어 molar IIP planning 체계화에 기여.',
        summary='CBCT-based proposal of classification criteria for inter-radicular septum shape in maxillary molars, with explicit linkage to prosthetic-driven IIP planning.',
        key_contrib='Translates anatomical IRS variations into a clinical taxonomy that supports prosthetic-driven placement decisions — bridge between Smith-Tarnow and modern digital workflow.',
        methodology='Retrospective CBCT review. IRS shape categorization and association with optimal implant trajectory derived from prosthetic plan.',
        results='Defines shape categories and quantifies their prevalence; identifies categories most amenable to predictable IIP.',
        limitations='Anatomy-only; classification not validated against outcome data within this paper.',
        related=['immediate-implant/pavlovic-2022-interradicular-septum-morphology-molar-iip',
                 'immediate-implant/smith-2013-classification-molar-extraction-immediate-implant',
                 'immediate-implant/deporter-2021-cbct-immediate-maxillary-molar-implant-planning'],
    ),
    'diagnostics-14-02756': dict(
        stem='abdul-2024-srp-maxillary-mandibular-anterior-cbct',
        category='immediate-implant',
        year=2024, date='2024-12-06',
        authors='Rawa Jamal Abdul, Darwn Saeed Abdulateef, Ara Omer Fattah, Ranjdar Mahmood Talabani',
        title='Analysis of the Sagittal Root Position of the Maxillary and Mandibular Anterior Teeth in the Alveolar Bone Using Cone-Beam Computed Tomography',
        doi='10.3390/diagnostics14232756',
        confidence='cross-sectional',
        oneline_kr='SRP 평가를 mandibular anterior까지 확장한 CBCT 단면 — 하악 전치에서도 Kan-style class 분포를 정량, 하악 IIP 계획에 시사점.',
        summary='CBCT cross-sectional study extending SRP analysis to both maxillary and mandibular anterior teeth — a rare combined dataset.',
        key_contrib='One of the few datasets that explicitly applies SRP classification to mandibular anterior teeth, useful for the less-studied mandibular esthetic-zone IIP.',
        methodology='Retrospective CBCT review. SRP class and root-to-bone angulation measured for maxillary and mandibular anterior teeth.',
        results='Prevalence distributions reported for both arches. Mandibular anterior teeth often show distinct patterns vs maxillary, with implications for trajectory planning.',
        limitations='Cross-sectional anatomy-only; single population.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population'],
    ),
    'isd-49-123': dict(
        stem='petaibunlue-2019-anterior-arch-root-position-angulation',
        category='immediate-implant',
        year=2019, date='2019-06-01',
        authors='Suweera Petaibunlue, Pravej Serichetaphongse, Atiphan Pimkhaokham',
        title='Influence of the anterior arch shape and root position on root angulation in the maxillary esthetic area',
        doi='10.5624/isd.2019.49.2.123',
        confidence='cross-sectional',
        oneline_kr='CBCT(n=98): anterior arch shape와 SRP의 조합이 root-to-bone angulation 예측력 ↑ — 단일 변수보다 두 변수 조합이 임상 의사결정에 유리.',
        summary='CBCT cross-sectional study evaluating how anterior arch form combined with Kan-class SRP relates to root-to-bone angulation in the maxillary esthetic zone.',
        key_contrib='Demonstrates that SRP alone is insufficient — combining arch form gives a more predictive model of root-to-bone angulation, refining IIP planning.',
        methodology='Retrospective CBCT review of 98 anterior arches. SRP and AA arch classification; mid-sagittal root vs bone angulation measured.',
        results='SRP carries a larger effect than arch form alone, but combined model (SRP × arch form) outperforms either variable individually (p<0.05).',
        limitations='Cross-sectional; single population; arch classification still operator-judged.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population'],
    ),
    'japid-13-49': dict(
        stem='deporter-2021-cbct-immediate-maxillary-molar-implant-planning',
        category='immediate-implant',
        year=2021, date='2021-11-21',
        authors='Douglas Deporter, Maziar Ebrahimi Dastgurdi, Azadeh Rahmati, Eshetu G. Atenafu, Mohammad Ketabi',
        title='CBCT data relevant in treatment planning for immediate maxillary molar implant placement',
        doi='10.34172/japid.2021.016',
        confidence='cross-sectional',
        oneline_kr='CBCT 다사이트 분석(n=427): 상악 1·2 대구치 IRS의 협구개·근원심 폭, furcation–sinus floor 거리, 근첨–sinus 거리 정량 — 5 mm 직경 IMI 호환 부위 분포.',
        summary='Cross-sectional CBCT review of 427 maxillary molar sites measuring inter-radicular septum width, furcation–sinus-floor distance, and root-to-sinus distances for immediate molar implant planning.',
        key_contrib='Large-n CBCT dataset that quantifies the proportion of maxillary molar sites that can fully accommodate a 5 mm-diameter IMI without sinus elevation.',
        methodology='Retrospective CBCT analysis of 427 sites from 223 patients. Buccopalatal/mesiodistal IRS width at three levels; furcation-sinus distances; per-root sinus intrusion rates.',
        results='Coronal-most IRS width: 6.52/7.33 mm (1st molar) vs 5.85/6.86 mm (2nd molar; p=0.008). 61.7% of 1st molars and 34% of 2nd molars had IRS broad enough for a 5 mm IMI. Mean FSD ~9 mm; mean root-apex-to-SF <3 mm.',
        limitations='Anatomy-only; ethnic homogeneity in cohort; threshold thresholds tied to one implant geometry (5 mm).',
        related=['immediate-implant/ragucci-2020-immediate-implant-molar-extraction-sockets',
                 'immediate-implant/pavlovic-2022-interradicular-septum-morphology-molar-iip',
                 'immediate-implant/milenkovic-2022-interradicular-septum-classification-iip',
                 'immediate-implant/aldahlawi-2023-cbct-alveolar-bone-maxillary-mandibular-molars'],
    ),
    'jomr-10-e4': dict(
        stem='dossantos-2019-buccal-bone-root-inclination-alveolar-cbct',
        category='immediate-implant',
        year=2019, date='2019-03-30',
        authors='Joana Gomes dos Santos, Ana Paula Oliveira Reis Durão, António Cabral de Campos Felino, Ricardo Manuel Casaleiro Lobo de Faria de Almeida',
        title='Analysis of the Buccal Bone Plate, Root Inclination and Alveolar Bone Dimensions in the Jawbone. A Descriptive Study Using Cone-Beam Computed Tomography',
        doi='10.5037/jomr.2019.10104',
        confidence='cross-sectional',
        oneline_kr='CBCT 기술 연구: 상하악 buccal bone plate 두께, root inclination, alveolar dimension 종합 매핑 — IIP 부위별 위험 데이터 제공.',
        summary='Descriptive CBCT study mapping buccal plate thickness, root inclination, and alveolar bone dimensions across the jaws, intended as a planning reference for immediate implants.',
        key_contrib='Comprehensive per-site reference data combining bone plate thickness with root inclination — relevant to fenestration and dehiscence risk in IIP.',
        methodology='Retrospective CBCT measurements at multiple sites along both arches. Buccal plate thickness at standard levels; tooth root inclination relative to alveolar long axis.',
        results='Quantifies site-by-site variation; buccal plate predominantly thin in anterior maxilla; varying root inclinations correlate with relative buccal/palatal bone distribution.',
        limitations='Descriptive; no outcome correlation; single-center cohort.',
        related=['immediate-implant/shafizadeh-2021-alveolar-bone-thickness-healthy-sr',
                 'immediate-implant/altarawneh-2018-bone-dimensions-anterior-maxilla-cbct'],
    ),
    'medoral-31-02-e297': dict(
        stem='galve-huertas-2026-inverted-body-shift-vs-conical-rct',
        category='immediate-implant',
        year=2026, date='2026-03-01',
        authors='Andrea Galve-Huertas, Susana García-González, Louis Decadt, Octavi Ortíz-Puigpelat, Federico Hernández-Alfaro, Samir Aboul-Hosn Centenero',
        title='Immediate implant using an inverted body-shift design versus a conventional conical implant: A randomized clinical trial with 1 year follow-up',
        doi='10.4317/medoral.27220',
        confidence='rct',
        oneline_kr='1년 RCT: inverted body-shift design vs 통상 conical implant in IIP — 디자인 차이가 esthetic outcome과 buccal bone 변화에 미치는 영향 비교, 통상 conical 대비 비열등성 입증을 목표.',
        summary='Randomized clinical trial (1-year follow-up) comparing an inverted body-shift implant design vs a conventional conical implant for immediate placement in the esthetic zone.',
        key_contrib='Provides RCT-level evidence for the novel inverted body-shift implant design (pilot in Galve-Huertas 2024) versus standard implants in IIP.',
        methodology='Randomized clinical trial. Anterior IIP patients allocated to test (inverted body-shift) vs control (conical) arm. 1-year clinical, radiographic, esthetic outcomes.',
        results='Comparable survival between arms; design-specific differences in trajectory control and buccal bone preservation reported.',
        limitations='1-year follow-up; industry-aligned implant; single-site team.',
        related=['immediate-implant/galve-huertas-2024-inverted-body-shift-design-pilot',
                 'immediate-implant/chu-2020-itrt-platform-switched-subcrestal-angle-correction',
                 'immediate-implant/ostman-2020-macro-hybrid-implant-anterior-postextraction'],
    ),
    'null': dict(
        stem='rodrigues-2022-srp-brazilian-anterior-bone-housing-isd',
        category='immediate-implant',
        year=2022, date='2022-06-01',
        authors='Diogo Moreira Rodrigues, Rodrigo Lima Petersen, Caroline Montez, Eliane Porto Barboza',
        title='Tomographic sagittal root position in relation to maxillary anterior bone housing in a Brazilian population',
        doi='10.5624/isd.20210226',
        confidence='cross-sectional',
        oneline_kr='브라질 인구 CBCT(420 치아/70명): Class I 65.2%, II 9.3%, III 0.7%, IV 24.8% — Kan 원본 대비 Class IV 비율 ↑, 인구별 SRP 분포는 case-by-case 평가가 필요함을 강조.',
        summary='Cross-sectional CBCT study of 420 maxillary anterior teeth in 70 Brazilian patients reporting Kan-class SRP distribution.',
        key_contrib='Brazilian-population SRP distribution data complementing Kan 2011 — notably higher Class IV prevalence, indicating need for individualized planning.',
        methodology='Retrospective CBCT review of 70 patients. Kan I–IV classification for each maxillary anterior tooth.',
        results='Class I 65.2%, II 9.3%, III 0.7%, IV 24.8%. Sex not associated (p=0.307); age distribution differed across classes (p=0.004).',
        limitations='Cross-sectional; single-center; younger-skewed cohort.',
        related=['immediate-implant/kan-2011-sagittal-root-position-immediate-implant-anterior',
                 'immediate-implant/rodrigues-2022-srp-periodontal-phenotype-anterior-maxillary',
                 'immediate-implant/habib-2024-srp-decision-making-immediate-implant-cbct',
                 'immediate-implant/kong-2020-srp-maxillary-anterior-korean-population'],
    ),
    's12903-025-07122-8': dict(
        stem='ziada-2025-abutment-material-stress-distribution-fea',
        category='prosthetic-materials',
        year=2025, date='2025-12-01',
        authors='Ahmed Ziada, Marwa Beleidy',
        title='Influence of different customized abutment materials on stress distribution of different internal implant-abutment connections: finite element analysis',
        doi='10.1186/s12903-025-07122-8',
        confidence='in-vitro',
        oneline_kr='3D FEA: 내부 connection 두 종류(star tube-in-tube vs Morse+internal hex) × abutment 재료 네 종(Ti, Co-Cr, Co-Cr-S, Zr) 조합 시 응력 분포 비교 — Ti abutment가 일관되게 응력 최저, 가장 안정적.',
        summary='3D finite element analysis comparing peri-implant and implant-component stresses across two internal connection geometries and four abutment materials under axial and oblique loading.',
        key_contrib='Provides FEA evidence ranking abutment-material × connection combinations for implant-supported single crowns, useful when prosthetic material is a free design parameter.',
        methodology='3D FEA. Two implant-abutment connections (S = star tube-in-tube; H = Morse + hex). Four abutment materials. Axial 200 N and oblique 100 N @45° loads. Principal stresses and von Mises analyzed.',
        results='Stresses concentrated in crestal cortical bone. Oblique loading > axial. Highest oblique stress 99.06 MPa (H Co-Cr). Titanium abutments consistently lowest stress. Peak implant von Mises 135 MPa (S Co-Cr oblique).',
        limitations='FEA assumptions (linear elasticity, idealized geometry, no microgaps); single bone-model. Not a clinical outcome study.',
        related=['prosthetic-materials/chan-2026-fea-cad-cam-zirconia-3d-printed-hybrid',
                 'implants/baki-2025-all-on-4-trefoil-five-implant-fea'],
    ),
    's12903-025-07404-1': dict(
        stem='baki-2025-all-on-4-trefoil-five-implant-fea',
        category='implants',
        year=2025, date='2025-12-15',
        authors='Nagehan Baki, Güler Yıldırım Avcu, Mesut Tuzlali',
        title='Biomechanical evaluation of three full-arch immediate loading protocols in the mandible via finite element analysis: All-on-4, Trefoil, and Five-implant design',
        doi='10.1186/s12903-025-07404-1',
        confidence='in-vitro',
        oneline_kr='하악 무치악 3D FEA: 5-implant > All-on-4 > Trefoil 순으로 응력·strain 우수. All-on-4 oblique loading 시 cortical strain 4180 με로 pathological overload 임계치(4000) 초과 — 위치 선택과 식립 수 영향을 정량.',
        summary='Finite element comparison of three full-arch immediate loading protocols in the edentulous mandible: All-on-4, Trefoil, and a Five-implant design. Five-implant design shows the most favorable stress-strain profile.',
        key_contrib='Adds quantitative FEA reference for the immediate-loading full-arch trade-off, including a warning about All-on-4 oblique cortical strain crossing pathological thresholds.',
        methodology='3D FEA edentulous mandible. Three implant configurations modeled. Axial and 45° oblique 100 N loads on first molar. Coefficient 0.30 for immediate non-osseointegrated interface.',
        results='Trefoil: highest prosthetic stress (156.48 MPa axial, 119.32 oblique). All-on-4: cortical strain 4180 με oblique > 4000 με threshold. Five-implant: lowest stresses and strains, physiological range.',
        limitations='FEA idealizations; immediate-loading friction coefficient is a model assumption; no clinical outcome translation.',
        related=['prosthetic-materials/ziada-2025-abutment-material-stress-distribution-fea',
                 'implants/ozturk-2026-stress-distribution-anterior-implant-fea'],
    ),
    's12903-026-07684-1': dict(
        stem='chan-2026-fea-cad-cam-zirconia-3d-printed-hybrid',
        category='prosthetic-materials',
        year=2026, date='2026-04-01',
        authors='Wan Wan Chan, Muaiyed Mahmoud Buzayan, Eshamsul Sulaiman, Nur Diyana Mohamed Radzi, Mohammed Rafiq Abdul Kadir, Mahmoud Z. Ibrahim',
        title='Comparative finite element analysis of stress distribution of different implant-supported crown and abutment materials',
        doi='10.1186/s12903-026-07684-1',
        confidence='in-vitro',
        oneline_kr='3D FEA: CAD/CAM zirconia crown + 3D-printed ceramic-filled hybrid abutment 조합이 custom abutment 응력 -90%, Ti-base 응력 -27%로 가장 우수. cortical/cancellous bone 응력은 그룹 간 큰 차이 없음.',
        summary='Comparative 3D FEA evaluating stress distribution across five combinations of CAD/CAM zirconia and 3D-printed ceramic-filled hybrid materials for crown and CAD/CAM custom abutment on mandibular molar implants.',
        key_contrib='Documents that abutment-material selection drives most of the stress redistribution at the prosthetic complex, while peri-implant bone stress is relatively insensitive — practical for material selection decisions.',
        methodology='3D FEA on bone-level implant with Ti-base abutment. Five crown-abutment combinations. Vertical 600 N and oblique 225 N @ 45° loads. Von Mises analysis on each component.',
        results='Crown VMS 102–214 MPa; CAD/CAM custom abutment 45–423 MPa; abutment screw 158–225 MPa; Ti-base 242–580 MPa; fixture 201–461 MPa; cortical bone 122–204 MPa. Zirconia crown + 3D-printed hybrid abutment reduced custom-abutment VMS by 90% and Ti-base by 27%.',
        limitations='FEA idealizations; linear elasticity; bone stress relatively flat across groups limits clinical conclusions on bone biology.',
        related=['prosthetic-materials/ziada-2025-abutment-material-stress-distribution-fea',
                 'implants/baki-2025-all-on-4-trefoil-five-implant-fea'],
    ),
    's12903-026-08405-4_reference': dict(
        stem='ozturk-2026-stress-distribution-anterior-implant-fea',
        category='implants',
        year=2026, date='2026-04-15',
        authors='Elif Öztürk, Nadine Graefin Krockow, Ricardo Curcio',
        title='Stress distribution of an anteriorly placed single implant in different clinical scenarios: a 3D finite element analysis',
        doi='10.1186/s12903-026-08405-4',
        confidence='in-vitro',
        oneline_kr='3D FEA: 전치부 단일 임플란트의 임상 시나리오(골량·loading angle·protocol)에 따른 응력 분포 — 전치부 IIP 결정 시 biomechanical input.',
        summary='3D finite element analysis of stress distribution for a single implant placed in the anterior maxilla across different clinical scenarios (bone availability, loading angle, restoration protocol).',
        key_contrib='Adds biomechanical reference for anterior single-implant scenarios that inform IIP versus delayed-placement trade-offs.',
        methodology='3D FEA. Anterior maxilla model with varying bone configurations and loading conditions. Stress distribution in cortical/cancellous bone and implant components.',
        results='Stress patterns sensitive to bone thickness and loading angle; identifies high-risk geometric scenarios from a mechanics standpoint.',
        limitations='Pre-publication version (article in press); FEA idealizations; not clinical outcome.',
        related=['implants/baki-2025-all-on-4-trefoil-five-implant-fea',
                 'immediate-implant/yang-2019-labial-bone-thickness-esthetics-iipp'],
    ),
}

print(f'Mapping size: {len(ENTRIES)} entries')
print(f'Duplicates to delete: {len(DUPES_TO_DELETE)}')
print(f'Total = {len(ENTRIES) + len(DUPES_TO_DELETE)}')

# Verify all orphans accounted for
all_orphans = set(FULLTEXT.keys())
accounted = set(ENTRIES.keys()) | set(DUPES_TO_DELETE)
missing = all_orphans - accounted
extra = accounted - all_orphans
print(f'Orphans not in mapping: {missing}')
print(f'Mapping entries not orphans: {extra}')
assert not missing and not extra, 'Mapping incomplete'


# ── 1. Delete duplicate PDFs ───────────────────────────────────────
for d in DUPES_TO_DELETE:
    p = f'papers/{d}.pdf'
    if os.path.exists(p):
        os.remove(p)
        print(f'  deleted dupe PDF: {p}')

# ── 2. Rename PDFs to new stems ────────────────────────────────────
for old, e in ENTRIES.items():
    old_path = f'papers/{old}.pdf'
    new_path = f'papers/{e["stem"]}.pdf'
    if os.path.exists(old_path) and old != e['stem']:
        if os.path.exists(new_path):
            print(f'  WARN: {new_path} already exists — skipping rename of {old_path}')
        else:
            os.rename(old_path, new_path)
print(f'  renamed {sum(1 for e in ENTRIES.values())} PDFs')


# ── 3. Generate sources/{stem}.md (7-section) ──────────────────────
SOURCES_TPL = """---
title: "{title}"
authors: {authors}
year: {year}
doi: {doi}
category: [{category}]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## One-line Summary
{summary}

## 1. Document Information
- **Title:** {title}
- **Authors:** {authors}
- **Year:** {year}
- **DOI:** {doi}
- **Study type:** {confidence}

## 2. Key Contributions
{key_contrib}

## 3. Methodology and Architecture
{methodology}

## 4. Key Results and Benchmarks
{results}

## 5. Limitations and Future Work
{limitations}

## 6. Related Work
{related_md}

## 7. Glossary
- **IIP:** Immediate Implant Placement — placement at the time of tooth extraction.
- **IIPP:** Immediate Implant Placement and Provisionalization — IIP combined with same-visit provisional restoration.
- **SRP:** Sagittal Root Position — Kan I/II/III/IV classification of root-to-bone relationship.
- **CBCT:** Cone-Beam Computed Tomography.
- **PES/WES:** Pink/White Esthetic Score — esthetic outcome indices for anterior implants.
- **EMBL:** Early Marginal Bone Loss.
"""

WIKI_TPL = """---
title: "{title}"
authors: {authors}
year: {year}
date: {date}
doi: {doi}
source: {stem}.md
category: [{category}]
confidence: {confidence}
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## 한줄요약
{oneline_kr}

## Summary
{summary}

## Key Contributions
{key_contrib}

## Methodology
{methodology}

## Results
{results}

## Limitations
{limitations}

## Related Papers
{related_md}
"""

def fmt_related(rels):
    if not rels:
        return '- (none)'
    return '\n'.join(f'- [[{r}]]' for r in rels)

for old, e in ENTRIES.items():
    related_md = fmt_related(e.get('related', []))
    common = dict(e, related_md=related_md)
    # sources
    src_path = f'sources/{e["stem"]}.md'
    with open(src_path, 'w') as f:
        f.write(SOURCES_TPL.format(**common))
    # wiki
    cat_dir = f'wiki/{e["category"]}'
    os.makedirs(cat_dir, exist_ok=True)
    wiki_path = f'{cat_dir}/{e["stem"]}.md'
    with open(wiki_path, 'w') as f:
        f.write(WIKI_TPL.format(**common))

print(f'  wrote {len(ENTRIES)} sources/ files')
print(f'  wrote {len(ENTRIES)} wiki/ files')


# ── 4. Update index.md ─────────────────────────────────────────────
# Append a section for each category with the new entries.
from collections import defaultdict
by_cat = defaultdict(list)
for e in ENTRIES.values():
    by_cat[e['category']].append(e)

# Read existing index.md
with open('index.md') as f:
    idx = f.read()

stamp = '\n\n<!-- BATCH INGEST 2026-05-24: immediate-implant + related FEA -->\n'
if '<!-- BATCH INGEST 2026-05-24' not in idx:
    new_block = stamp
    for cat in sorted(by_cat.keys()):
        new_block += f'\n### {cat} (added 2026-05-24)\n\n'
        for e in sorted(by_cat[cat], key=lambda x: (x['year'], x['stem'])):
            authors_first = e['authors'].split(',')[0]
            new_block += f'- [[{cat}/{e["stem"]}]] — {authors_first} {e["year"]} · {e["confidence"]} · {e["title"]}\n'
    with open('index.md', 'w') as f:
        f.write(idx + new_block)
    print('  index.md updated with new entries')
else:
    print('  index.md already contains this batch — skipping')


# ── 5. Lint: 1:1 matching ─────────────────────────────────────────
pdfs = {os.path.splitext(f)[0] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs = {os.path.splitext(f)[0] for f in os.listdir('sources') if f.endswith('.md')}
orphan_pdfs = pdfs - srcs
orphan_srcs = srcs - pdfs
print()
print(f'LINT: papers={len(pdfs)}, sources={len(srcs)}')
print(f'LINT: orphan_pdfs = {sorted(orphan_pdfs)}')
print(f'LINT: orphan_srcs = {sorted(orphan_srcs)}')

