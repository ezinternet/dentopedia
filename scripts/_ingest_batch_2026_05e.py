#!/usr/bin/env python3
"""
Fifth batch ingest for 2026-05 session (5 research + 5 Versah manuals).
"""
import os, warnings
warnings.filterwarnings('ignore')

ROOT = '/Users/oracleneo/llm-wiki'
os.chdir(ROOT)

# Delete (1) duplicates first
DUPES = [
    "Watermark_Densah Lift I-10179 REV09 (1).pdf",
    "Combied_Upper_Molar_Septum_Protocol (1).pdf",
    "Immediate_Implant_Placement_Protocol (1).pdf",
]
for f in DUPES:
    p = f"papers/{f}"
    if os.path.exists(p):
        os.remove(p); print(f"DEL dup {f}")

ENTRIES = {
    # ===== RESEARCH PAPERS (5) =====
    'Mohammadi_2025_PMC12659130_OD_vs_CD_LowDensityBone_MetaAnalysis': dict(
        stem='mohammadi-2025-osseodensification-conventional-low-density-bone-sr-ma',
        category='implants',
        year=2025, date='2025-01-01',
        authors='Maryam Mohammadi, Marzie Mohamadi Moghadam, Morteza Arab-Zozani',
        title='Primary and secondary stability in implants placed in low-density bone using conventional vs. osseodensification technique: a systematic review and meta-analysis',
        doi='10.1186/s12903-025-07201-w',
        confidence='sr+ma',
        oneline_kr='SR+MA (7개 연구): 저밀도골에서 골밀도화(Osseodensification, OD) vs 일반 절삭드릴(Conventional Drilling, CD) — 임플란트 안정성 지수(Implant Stability Quotient, ISQ) 기준 1차(MD=4.13, p=0.13)·2차(MD=1.78, p=0.11) 안정성 모두 유의차 없음. 변연골소실(Marginal Bone Loss, MBL)·치태지수(Plaque Index, PI)도 차이 없음. 12개월 prob depth(Probing Depth, PD)만 OD 유의 낮음, 구개측 치조정골(Crestal Bone Level, CBL)도 OD 유리. 결론: 장기 우월성 입증 부족 — 더 많은 RCT 필요.',
        summary='Systematic review and meta-analysis of 7 studies comparing osseodensification vs conventional drilling specifically in low-density bone, using ISQ-based stability outcomes plus periodontal indices.',
        key_contrib='Demonstrates that OD does not show statistically significant superiority over CD for primary or secondary implant stability in low-density bone — challenging the marketing narrative that OD universally improves stability. Significant benefit appears only on 12-month PD and palatal CBL, narrowing OD\'s defensible advantage to soft-tissue/late-bone outcomes.',
        methodology='PubMed, Scopus, Web of Science, EMBASE, Google Scholar searched up to Jan 2024. Inclusion: dental implants in low-density bone, OD vs CD, ISQ outcome. Outcomes: primary/secondary stability (ISQ), MBL, CBL, PD, PI. Random-effects model, mean differences with 95% CI. Subgroup by follow-up time and anatomic site.',
        results='7 studies eligible (follow-up 4, 6, 8, 12 months). Primary stability: MD=4.13, P=0.13 (NS). Secondary stability: MD=1.78, P=0.11 (NS). MBL, PI: no significant differences. PD at 12 months: OD significantly lower. CBL: OD favored only at palatal site.',
        limitations='Only 7 studies — small evidence base. Heterogeneity in follow-up periods. Mixed implant systems and surgical protocols. PD/CBL subgroup findings hypothesis-generating, not confirmatory. Authors call for more standardized RCTs with longer follow-up.',
        related=['implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability',
                 'implants/inchingolo-2021-osseodensification-implant-site-osteotomy-sr-ma',
                 'implants/gaspar-2022-implant-stability-osseodensification-conventional-sr-ma',
                 'implants/bergamo-2021-osseodensification-effect-implants-primary-secondary'],
    ),
    'Bio -Temperature Changes in Correlation with Number of Implant Osteotomy Preparations in Human Cadaver Tibiae': dict(
        stem='soldatos-2024-temperature-changes-osseodensification-cadaver-tibiae-cw-ccw',
        category='implants',
        year=2024, date='2024-08-22',
        authors='Nikolaos Soldatos, Amanda Heydari, LeRoy Horton, Shayda Sarrami, Luke Nordlie, Dongseok Choi, Robin Weltman',
        title='Temperature Changes (ΔT) in Correlation with Number of Implant Osteotomy Preparations in Human Cadaver Tibiae, Comparing Osseodensification (OD) Burs in Clockwise (CW) versus Counterclockwise (CCW) Mode',
        doi='10.3390/jfb15080237',
        confidence='in-vitro',
        oneline_kr='Cadaver tibiae 4요인 분석 (360 osteotomy, n=human cadaver): Densah® 버 시계방향(CW) vs 반시계방향(CCW, 골밀도화 모드) — CCW 모드에서 3.0/4.0 버를 23회 이상 사용 + 800/1200 RPM 조합 시 ΔT가 47°C 초과(골괴사 임계치). 1000 RPM이 두 모드 모두에서 최저 발열. 임상 시사: 버 재사용 횟수와 RPM이 발열 위험의 결정적 요인 — 23회는 권장 교체 기준.',
        summary='Four-way interaction analysis of bur usage count, rotation mode, bur diameter, and rotational speed on temperature rise during osseodensification in human cadaver tibiae.',
        key_contrib='Quantifies the temperature-failure threshold of Densah® burs: after 23 osteotomies in CCW mode with larger (3.0/4.0) burs at non-1000-RPM speeds, ΔT exceeds the 47°C bone-necrosis threshold with audible chatter. Argues for bur replacement after 23 uses and 1000 RPM as the safe operating speed.',
        methodology='360 osteotomies prepared at 12 mm depth in human cadaver tibiae. Four variables: bur diameter (multiple), rotation mode (CW vs CCW), RPM (800/1000/1200), and number of prior osteotomies. ΔT measured per established prior protocol from the same group. Four-way interaction statistical model.',
        results='Four-way interaction in CCW mode. 1000 RPM minimized ΔT in both modes. In CCW: 3.0 and 4.0 burs after 23+ uses showed significant ΔT increase vs CW + significant chatter. ΔT increased significantly with bur diameter at 800 and 1200 RPM. Combination of larger burs + CCW + 23+ uses + non-1000 RPM produced ΔT > 47°C.',
        limitations='Ex-vivo human cadaver tibiae — not living jaw bone (no irrigation perfusion, no vascular cooling). Tibial cortical/cancellous architecture differs from maxilla/mandible. Single research group methodology — independent replication needed. No correlation to clinical outcomes (implant survival).',
        related=['implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability',
                 'implants/chauhan-2018-biomechanical-factors-heat-generation-osteotomy',
                 'implants/kosior-2025-histological-histomorphometric-implant-bed-preparation',
                 'implants/inchingolo-2021-osseodensification-implant-site-osteotomy-sr-ma'],
    ),
    'CID-27-0': dict(
        stem='gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review',
        category='sinus-lift/transcrestal',
        year=2025, date='2025-01-01',
        authors='João Gaspar, Ziv Mazor, Estevam A. Bonfante',
        title='Osseodensification technique in crestal maxillary sinus elevation — A narrative review',
        doi='10.1111/cid.13399',
        confidence='narrative-review',
        oneline_kr='경치조골 상악동 거상술(Transcrestal Sinus Floor Elevation, TSFE) + 골밀도화(Osseodensification, OD) 종합 서술리뷰 — 잔존 골높이(Residual Bone Height, RBH) 기반 3가지 프로토콜 제안(≥2 mm까지 적용). RBH ≤2–3 mm가 슈나이더막 천공 위험인자. 측방창 대비 환자보고결과(Patient-Reported Outcome Measures, PROMs) 우수, 합병증률 낮음 — paradigm shift로 평가.',
        summary='Narrative review by lead OD-TSFE researchers proposing three RBH-stratified protocols (matched to Versah Sinus Lift I/II and Combined approaches) and synthesizing biomechanical, histologic, and clinical evidence.',
        key_contrib='Crystallizes the OD-TSFE protocol landscape into three RBH-stratified pathways and identifies RBH ≤2–3 mm as the dominant perforation risk threshold — providing a clinical decision framework for sinus floor elevation by RBH.',
        methodology='Narrative literature review. Synthesizes published evidence on OD bur mechanics, sinus floor histology, and clinical TSFE outcomes; integrates with author group\'s multicenter clinical data ([[mazor-2024-maxillary-sinus-membrane-perforation-osseodensification]]).',
        results='Three RBH-stratified protocols proposed: (1) Sinus Lift I for RBH ≥6 mm, (2) Sinus Lift II for RBH 4–5 mm, (3) extended approaches for RBH 2–3 mm. RBH ≤2–3 mm identified as primary perforation risk factor. PROMs (pain, edema, satisfaction) favor OD-TSFE over lateral window.',
        limitations='Narrative — no formal evidence grading. Authors heavily involved in OD development (potential conflict of interest). Protocols are proprietary (Versah Densah® burs). Long-term implant survival data still maturing.',
        related=['sinus-lift/transcrestal/mazor-2024-maxillary-sinus-membrane-perforation-osseodensification',
                 'sinus-lift/transcrestal/cobo-vazquez-2025-crestal-sinus-lift-osteotome-vs-osseodensification',
                 'sinus-lift/transcrestal/el-ghobashy-osseodensification-vs-osteotome-transcrestal-sinus',
                 'sinus-lift/transcrestal/farina-2023-minimal-invasiveness-transcrestal-sinus-elevation'],
    ),
    'JPER-96-519': dict(
        stem='wang-2025-ao-aap-consensus-peri-implant-diseases-conditions',
        category='periodontics',
        year=2025, date='2025-05-01',
        authors='Hom-Lay Wang, Gustavo Avila-Ortiz, Alberto Monje, Purnima Kumar, Javier Calatrava, Tara Aghaloo, Shayan Barootchi, Joseph P. Fiorellini, Maria Elisa Galarraga-Vinueza, Joseph Kan, Guo-Hao Lin, Andrea Ravida, Muhammad H.A. Saleh, Lorenzo Tavelli, AO/AAP Consensus Participants, Paul S. Rosen',
        title='AO/AAP consensus on prevention and management of peri-implant diseases and conditions: Summary report',
        doi='10.1002/JPER.25-0270',
        confidence='consensus',
        oneline_kr='Academy of Osseointegration / American Academy of Periodontology (AO/AAP) 2024 합의 (Oak Brook, Illinois, 2024-08): peri-implant disease (PID) 예방 + 관리 통합 framework. Group 1=위험인자(전신·국소), Group 2=치료(비외과·외과). 핵심 risk: 치주염 병력, 흡연, 조절 불량 당뇨, 비만, 임플란트 malposition, 부적절 보철, 얇은 점막 phenotype. Peri-implant mucositis는 비외과적 데브리망 + 위험인자 통제로 치료 가능 — peri-implantitis 1차 치료의 출발점. 진행 사례는 개별화된 외과 (비재건적/재건적).',
        summary='AO/AAP 2024 international consensus (Oak Brook, Illinois) synthesizing 8 systematic reviews into unified evidence-based recommendations for peri-implant disease prevention and management. Published in J Periodontol May 2025.',
        key_contrib='Provides the most current AO/AAP joint position on peri-implant diseases — integrating systemic, behavioral, local, and prosthetic risk factors with a staged treatment algorithm (mucositis → non-surgical → surgical reconstruction). Supersedes earlier 2017/2018 consensus on practical management points.',
        methodology='Eight pre-commissioned systematic reviews grouped into two domains: (Group 1) risk factors for mucositis, peri-implantitis, soft tissue deformities, prosthetic factors and MBL; (Group 2) therapeutic strategies — non-surgical debridement, surface decontamination, surgical interventions (non-reconstructive + reconstructive). Structured consensus discussions Aug 14–16, 2024.',
        results='Key risk factors identified: periodontitis history, smoking, uncontrolled diabetes, poor biofilm control, obesity, implant malposition, unfavorable prosthetics, suboptimal peri-implant soft tissue phenotype. Mucositis: non-surgical debridement + risk factor control effective. Peri-implantitis: starts with mucositis-style approach; advanced cases require surgery (non-reconstructive or reconstructive depending on defect morphology).',
        limitations='Consensus-based — does not generate new primary data. Reflects expert weighting where evidence is mixed. Treatment algorithms still acknowledge low predictability for advanced peri-implantitis surgical outcomes. Some protocol recommendations remain industry-influenced.',
        related=['periodontics/cha-2024-peri-implantitis-treatment-protocol-flowchart',
                 'periodontics/kim-2024-peri-implant-diseases-consensus-korean-academy-periodontology',
                 'periodontics/kim-2025-management-peri-implantitis-perspectives',
                 'periodontics/grusovin-2022-antibiotics-non-surgical-peri-implantitis-ma'],
    ),

    # ===== VERSAH MANUFACTURER PROTOCOLS (5) =====
    'Watermark_Densah Lift I-10179 REV09': dict(
        stem='versah-densah-sinus-lift-i-protocol-rbh-6mm-minimum',
        category='implants/versah-protocols',
        year=2024, date='2026-05-28',
        authors='Versah LLC',
        title='Osseodensification-Facilitated Crestal Sinus Lift Protocol I (Densah® Lift I, REV09)',
        doi='(manufacturer document)',
        confidence='narrative-review',
        oneline_kr='Versah Densah® 골밀도화(Osseodensification, OD) 경치조골 상악동 거상(Crestal Sinus Lift) 프로토콜 I — 잔존 골높이(Residual Bone Height, RBH) ≥6 mm, 치조정 폭 ≥4 mm 적응. 순서: pilot drill(상악동 1 mm 아래) → Densah 2.0 OD(CCW 1000 rpm, irrigation) → 3.0/4.0/5.0 단계적 확장(상악동 바닥 3 mm 통과까지). Compaction autografting으로 점진 막 거상.',
        summary='Versah Densah® manufacturer-issued clinical protocol card (2-page, REV09) for crestal sinus floor elevation using osseodensification mode in residual bone height ≥6 mm.',
        key_contrib='Vendor reference protocol defining the bur sequence (2.0 → 3.0 → 4.0 → 5.0), rotation mode (CCW Densifying), and depth control (≤3 mm past sinus floor) for the Sinus Lift I scenario.',
        methodology='Step-by-step clinical protocol (5 steps). Not a research methodology — manufacturer-published technique guide synthesized from internal clinical experience and supporting peer-reviewed literature.',
        results='Protocol outcome: gentle sinus membrane lift via compaction autografting; suitable for cases where ≥6 mm of crestal bone allows pilot drill access. Maximum bur advancement past sinus floor 3 mm per stage to limit perforation risk.',
        limitations='Manufacturer marketing document — not peer-reviewed. No quantitative outcomes. Use with cross-reference to peer-reviewed sinus-lift literature ([[mazor-2024-maxillary-sinus-membrane-perforation-osseodensification]], [[gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review]]). Densah® burs proprietary — protocol non-generalizable to other bur systems.',
        related=['sinus-lift/transcrestal/mazor-2024-maxillary-sinus-membrane-perforation-osseodensification',
                 'sinus-lift/transcrestal/gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review',
                 'implants/versah-protocols/versah-densah-sinus-lift-ii-protocol-rbh-4-5mm',
                 'implants/versah-protocols/versah-combined-molar-septum-expansion-sinus-lift-protocol'],
    ),
    'Watermark_Densah LIFT II Protocol_ 10211 REV08': dict(
        stem='versah-densah-sinus-lift-ii-protocol-rbh-4-5mm',
        category='implants/versah-protocols',
        year=2024, date='2026-05-28',
        authors='Versah LLC',
        title='Osseodensification-Facilitated Crestal Sinus Lift Protocol II (Densah® LIFT II, REV08)',
        doi='(manufacturer document)',
        confidence='narrative-review',
        oneline_kr='Versah Densah® OD 경치조골 상악동 거상 프로토콜 II — 잔존 골높이(Residual Bone Height, RBH) 4–5 mm, 치조정 폭 ≥5 mm 적응. **Pilot drill 사용 안 함** (Lift I과 차이) — 처음부터 Densah 2.0 OD 모드(CCW 1000 rpm)로 상악동 바닥까지 진입. 3.0~5.0 버 단계적 확장 + 추가 막 거상 시 마지막 버 저속(150 rpm, no irrigation)으로 hydrated allograft 가압.',
        summary='Versah Densah® manufacturer-issued clinical protocol card (2-page, REV08) for crestal sinus floor elevation in residual bone height 4–5 mm — eliminates pilot drill step and adds allograft propulsion.',
        key_contrib='Vendor reference protocol distinguishing the Lift II indication (RBH 4–5 mm) from Lift I (RBH ≥6 mm) by: (1) omitting pilot drill, (2) adding final-bur slow-speed allograft propulsion (150 rpm, no irrigation) when additional lift >3 mm is needed.',
        methodology='Step-by-step clinical protocol (4 steps, no pilot drill). Manufacturer-published technique guide.',
        results='Protocol outcome: avoids pilot-drill-induced perforation in thin residual bone; propels well-hydrated allograft to extend membrane lift beyond 3 mm when needed.',
        limitations='Manufacturer marketing document — not peer-reviewed. Higher-risk indication (thinner RBH) than Lift I; perforation risk per Mazor 2024 ([[mazor-2024-maxillary-sinus-membrane-perforation-osseodensification]]) elevates at RBH ≤3 mm. Densah®-specific.',
        related=['sinus-lift/transcrestal/mazor-2024-maxillary-sinus-membrane-perforation-osseodensification',
                 'sinus-lift/transcrestal/gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review',
                 'implants/versah-protocols/versah-densah-sinus-lift-i-protocol-rbh-6mm-minimum',
                 'implants/versah-protocols/versah-combined-molar-septum-expansion-sinus-lift-protocol'],
    ),
    'Watermark_IDR-II_10419 REV06': dict(
        stem='versah-idr-ii-immediate-dentoalveolar-restoration-protocol',
        category='implants/versah-protocols',
        year=2024, date='2026-05-28',
        authors='Versah LLC',
        title='Osseodensification Immediate Dentoalveolar Restoration (IDR) II Technique (REV06)',
        doi='(manufacturer document)',
        confidence='narrative-review',
        oneline_kr='Versah IDR II 프로토콜 — 협측골 완전 소실 + 얇은 치주 biotype/gingival recession 임플란트 즉시식립. **상악 결절(maxillary tuberosity)에서 triple graft 채취**(골+연조직) → OD 버로 식립와 준비 → palatal wall에 임플란트 정착 → triple graft로 gap 충전 → 즉시 screw-retained 임시보철(cement 보철 금지) → 최소 4개월 치유 후 최종 porcelain crown(screw-retained).',
        summary='Versah Immediate Dentoalveolar Restoration II manufacturer protocol (2-page, REV06) for severely compromised sockets with full buccal wall loss and thin/recessed soft tissue — single-procedure implant + bone/soft-tissue graft + provisional.',
        key_contrib='Vendor reference protocol for the IDR II indication: severe socket compromise (no buccal wall + thin biotype + recession). Differs from IDR I by harvesting a combined bone + soft tissue (triple) graft from maxillary tuberosity, with mandatory screw-retained provisional (cemented contraindicated).',
        methodology='Six-step clinical protocol: atraumatic extraction + degranulation → Densah OD prep → palatal wall anchorage → triple graft harvest → screw-retained provisional → 4-month healing → screw-retained final crown.',
        results='Protocol outcome: single-stage rehabilitation of high-risk esthetic socket; relies on palatal wall implant anchorage and triple graft for buccal wall reconstruction. Cemented restorations explicitly contraindicated.',
        limitations='Manufacturer marketing document — not peer-reviewed. Highly operator-dependent (triple graft harvest from tuberosity, primary stability solely from palatal wall). Outcome variance not quantified in protocol. Cross-reference [[darosa-2019-immediate-dentoalveolar-restoration-osseodensification-periodontal]] for the peer-reviewed clinical IDR rationale.',
        related=['immediate-implant/darosa-2019-immediate-dentoalveolar-restoration-osseodensification-periodontal',
                 'immediate-implant/bleyan-2021-molar-septum-expansion-osseodensification-immediate-implant',
                 'implants/versah-protocols/versah-immediate-implant-placement-protocol',
                 'implants/versah-protocols/versah-combined-molar-septum-expansion-sinus-lift-protocol'],
    ),
    'Combied_Upper_Molar_Septum_Protocol': dict(
        stem='versah-combined-molar-septum-expansion-sinus-lift-protocol',
        category='implants/versah-protocols',
        year=2024, date='2026-05-28',
        authors='Versah LLC',
        title='Osseodensification Combined Upper Molar Septum Expansion with Crestal Sinus Lift Protocol',
        doi='(manufacturer document)',
        confidence='narrative-review',
        oneline_kr='Versah 상악 구치부 즉시식립 + 동시 상악동 거상 프로토콜 — 상악 구치 septum 폭 ≥4 mm 적응. CBCT로 ridge 폭·상악동까지 높이 측정 → flapless 무외상 발치(septum 보존) → Densah OD 버(CCW, 800–1500 rpm, irrigation) 단계 확장으로 septum expansion + 슈나이더막 거상 동시 → 임플란트 식립 → 골이식 충전 → wide healing abutment로 소켓 sealing.',
        summary='Versah manufacturer protocol (2-page) for the combined molar septum expansion + crestal sinus lift workflow in upper molar sites with intact ≥4 mm interradicular septum.',
        key_contrib='Vendor reference for the combined-indication scenario where molar extraction socket with thick septum allows simultaneous bone expansion and sinus lift — eliminating staged sinus augmentation. Backed by the Bleyan 2021 septum-OD case series.',
        methodology='Six-step clinical protocol: CBCT diagnosis → flapless septum-preserving extraction → Densah CCW expansion + simultaneous sinus lift → implant placement → graft fill → wide healing abutment.',
        results='Protocol outcome: single-procedure rehabilitation of upper molar with simultaneous septum expansion (lateral) and sinus floor elevation (apical); requires ≥4 mm septum width.',
        limitations='Manufacturer marketing document — not peer-reviewed. Requires precise CBCT planning and septum integrity. See [[bleyan-2021-molar-septum-expansion-osseodensification-immediate-implant]] for clinical outcome data including the molar socket classification this protocol implicitly uses.',
        related=['immediate-implant/bleyan-2021-molar-septum-expansion-osseodensification-immediate-implant',
                 'sinus-lift/transcrestal/mazor-2024-maxillary-sinus-membrane-perforation-osseodensification',
                 'implants/versah-protocols/versah-densah-sinus-lift-ii-protocol-rbh-4-5mm',
                 'implants/versah-protocols/versah-immediate-implant-placement-protocol'],
    ),
    'Immediate_Implant_Placement_Protocol': dict(
        stem='versah-immediate-implant-placement-protocol',
        category='implants/versah-protocols',
        year=2024, date='2026-05-28',
        authors='Versah LLC',
        title='Osseodensification Immediate Implant Placement Protocol',
        doi='(manufacturer document)',
        confidence='narrative-review',
        oneline_kr='Versah OD 즉시식립 프로토콜 — 핵심 원칙: **임플란트 직경은 발치치 apex보다 약간 큼**, **마지막 Densah® 버는 발치와 apex 직경 ≥** (apical engagement 우선). 발치 → pilot drill(CW) → Densah OD 모드(CCW 800–1500 rpm) 점진 확장 → 70/30 cancellous/cortical hydrated composite allograft로 소켓 충전 → 마지막 버보다 한 단계 작은 버로 allograft densify → 1차 안정성은 소켓 apical 부분에서 확보.',
        summary='Versah manufacturer protocol (2-page) for immediate implant placement into extraction sockets using osseodensification, emphasizing apical anchorage and compaction allografting.',
        key_contrib='Vendor reference codifying the apical-engagement principle: implant diameter > tooth apex + final Densah bur ≥ socket apex. Pairs with composite 70/30 cancellous/cortical allograft compacted by the second-to-last bur.',
        methodology='Three-step protocol with explicit selection rules for implant diameter and final bur diameter based on socket apex dimensions.',
        results='Protocol outcome: primary stability provided by apical socket (not coronal walls); standardized allograft selection (70/30 mix) and compaction technique.',
        limitations='Manufacturer marketing document — not peer-reviewed. Apical-anchorage principle requires sufficient apical bone (not all socket morphologies). Allograft selection ratio (70/30) not validated against alternatives in this document.',
        related=['immediate-implant/bleyan-2021-molar-septum-expansion-osseodensification-immediate-implant',
                 'immediate-implant/darosa-2019-immediate-dentoalveolar-restoration-osseodensification-periodontal',
                 'implants/versah-protocols/versah-idr-ii-immediate-dentoalveolar-restoration-protocol',
                 'implants/versah-protocols/versah-combined-molar-septum-expansion-sinus-lift-protocol'],
    ),
}

print(f'Mapping size: {len(ENTRIES)}')

# Collision check
import glob
existing = set()
for p in glob.glob('wiki/**/*.md', recursive=True):
    existing.add(os.path.splitext(os.path.basename(p))[0])
collisions = [e['stem'] for e in ENTRIES.values() if e['stem'] in existing]
print(f'Stem collisions: {collisions}')
assert not collisions

# Rename PDFs
for old, e in ENTRIES.items():
    old_p = f'papers/{old}.pdf'
    new_p = f'papers/{e["stem"]}.pdf'
    if os.path.exists(old_p) and old != e['stem']:
        if os.path.exists(new_p):
            print(f'  WARN: {new_p} exists — skipping')
        else:
            os.rename(old_p, new_p)
            print(f'  renamed → {e["stem"]}.pdf')

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
- **OD:** Osseodensification.
- **CD / SD:** Conventional / Subtractive Drilling.
- **IT:** Insertion Torque.
- **ISQ:** Implant Stability Quotient.
- **BIC:** Bone-to-Implant Contact.
- **BAF / BAFO:** Bone-Area-Fraction (Occupancy).
- **MBL:** Marginal Bone Loss.
- **CBL:** Crestal Bone Level.
- **PD:** Probing Depth.
- **PI:** Plaque Index.
- **RBH:** Residual Bone Height.
- **TSFE:** Transcrestal Sinus Floor Elevation.
- **CCW / CW:** Counterclockwise / Clockwise.
- **PROMs:** Patient-Reported Outcome Measures.
- **PID:** Peri-Implant Diseases.
- **IDR:** Immediate Dentoalveolar Restoration.
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
    return '\n'.join(f'- [[{r}]]' for r in rels) if rels else '- (none)'

for old, e in ENTRIES.items():
    common = dict(e, related_md=fmt_related(e.get('related', [])))
    with open(f'sources/{e["stem"]}.md', 'w') as f:
        f.write(SOURCES_TPL.format(**common))
    cat_dir = f'wiki/{e["category"]}'
    os.makedirs(cat_dir, exist_ok=True)
    with open(f'{cat_dir}/{e["stem"]}.md', 'w') as f:
        f.write(WIKI_TPL.format(**common))

print(f'  wrote {len(ENTRIES)} sources/')
print(f'  wrote {len(ENTRIES)} wiki/')

# Index update
from collections import defaultdict
by_cat = defaultdict(list)
for e in ENTRIES.values():
    by_cat[e['category']].append(e)
with open('index.md') as f:
    idx = f.read()
marker = '<!-- BATCH INGEST 2026-05-28e'
if marker not in idx:
    new_block = f'\n\n{marker}: 5 OD research papers + 5 Versah manufacturer protocols -->\n'
    for cat in sorted(by_cat.keys()):
        new_block += f'\n### {cat} (added 2026-05-28, batch e)\n\n'
        for e in sorted(by_cat[cat], key=lambda x: (x['year'], x['stem'])):
            fa = e['authors'].split(',')[0]
            new_block += f'- [[{cat}/{e["stem"]}]] — {fa} {e["year"]} · {e["confidence"]} · {e["title"]}\n'
    with open('index.md', 'w') as f:
        f.write(idx + new_block)
    print('  index.md updated')

# Lint summary
import unicodedata
def norm(s): return unicodedata.normalize('NFC', s)
pdfs = {norm(os.path.splitext(f)[0]) for f in os.listdir('papers') if f.endswith('.pdf')}
srcs = {norm(os.path.splitext(f)[0]) for f in os.listdir('sources') if f.endswith('.md')}
print(f'\nLINT: papers={len(pdfs)} sources={len(srcs)} orphan_pdfs={len(pdfs-srcs)} orphan_sources={len(srcs-pdfs)}')
for s in sorted(pdfs-srcs): print(f'  orphan_pdf: {s}')
for s in sorted(srcs-pdfs): print(f'  orphan_source: {s}')
