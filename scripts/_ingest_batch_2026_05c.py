#!/usr/bin/env python3
"""
Third batch ingest for 2026-05-24 session (9 PDFs).
Topics: peri-implantitis (3), KDA implant policy/clinical (4), cracked tooth (1), stamp technique (1).
"""
import os, warnings
warnings.filterwarnings('ignore')

ROOT = '/sessions/trusting-ecstatic-faraday/mnt/llm-wiki'
os.chdir(ROOT)

ENTRIES = {
    'antibiotics-11-01766': dict(
        stem='grusovin-2022-antibiotics-non-surgical-peri-implantitis-ma',
        category='periodontics',
        year=2022, date='2022-12-07',
        authors='Maria Gabriella Grusovin, Alberto Pispero, Massimo Del Fabbro, Matteo Sangiorgi, Massimo Simion, Martina Stefanini, Elena Maria Varoni',
        title='Antibiotics as Adjunctive Therapy in the Non-Surgical Treatment of Peri-Implantitis: A Systematic Review and Meta-Analysis',
        doi='10.3390/antibiotics11121766',
        confidence='sr+ma',
        oneline_kr='SR+MA (6 RCT): 비외과 peri-implantitis 치료에 항생제 adjunct — 국소 항생제는 PPD(-0.6mm), BOP(-0.15), success rate(RR 9.89) 모두 유의 개선; 전신 항생제는 PPD(-1.15mm)·PAL(-1.10mm)만 개선, success는 차이 없음. peri-implantitis resolution은 국소 adjunct 시 20–30%로 여전히 낮음.',
        summary='Cochrane-style SR+MA of 6 RCTs evaluating local vs systemic antibiotic adjuncts to non-surgical peri-implantitis therapy. Reports differential efficacy between routes.',
        key_contrib='Quantifies that local antibiotics yield broader success-rate gains than systemic, but neither route achieves high disease resolution alone — informs case selection and step-up logic.',
        methodology='SR of RCTs comparing antibiotic adjunct (local or systemic) vs non-surgical debridement alone in peri-implantitis. Outcomes: success rate, MBL, PPD, PAL, BOP, peri-implantitis resolution.',
        results='Local antibiotics: PPD -0.6 mm (CI 0.42–0.78), BOP -0.15 (CI 0.10–0.19), success RR 9.89 (CI 2.39–40.84). Systemic antibiotics: PPD -1.15 mm (CI 0.31–1.99), PAL -1.10 mm (CI 0.13–2.08); no significant bone-level or success change. Resolution ~20–30% with local adjunct.',
        limitations='Only 6 RCTs eligible. Heterogeneous antibiotic regimens and debridement protocols. Short follow-up in most studies.',
        related=['periodontics/cha-2024-peri-implantitis-treatment-protocol-flowchart',
                 'periodontics/kim-2024-peri-implant-diseases-consensus-korean-academy-periodontology',
                 'periodontics/kim-2025-management-peri-implantitis-perspectives'],
    ),
    'jkda-2024-62-1-005': dict(
        stem='kwak-2024-endodontic-treatment-cracked-tooth-management',
        category='endodontics',
        year=2024, date='2024-01-01',
        authors='Kwak Youngjun',
        title='Endodontic treatment in the management of cracked tooth',
        doi='10.22974/jkda.2024.62.1.005',
        confidence='narrative-review',
        oneline_kr='Cracked tooth 관리 시 endo 치료의 적응증/시점 정리(KDA, 한국어): 불필요한 endo 회피 — 일시적 cementation 후 추가 conversion이 발생하지 않으면 endo 또는 final prosthesis 결정 가능. Cracked tooth 관리가 "endo originated treatment"로 분류되는 임상 사고 흐름 강조.',
        summary='Narrative practitioner-oriented review (Korean Dental Association) on the decision logic for endodontic treatment in cracked tooth management. Emphasizes a staged approach to avoid premature/unnecessary RCT.',
        key_contrib='Clarifies that "cracked tooth = endo" is an overuse pattern; offers a staged decision algorithm via temporary cementation as a diagnostic step.',
        methodology='Narrative clinical commentary based on author experience and literature.',
        results='Staged protocol: assess fracture extent → temporary cementation → re-evaluate symptoms → decide endo vs prosthesis vs extraction. Many cases need no endo if symptoms resolve.',
        limitations='Narrative review without quantitative outcomes. Practice-pattern based.',
        related=[],
    ),
    'jkda-2024-62-10-003': dict(
        stem='park-2024-dental-implant-utilization-nhis-korea',
        category='implants',
        year=2024, date='2024-10-01',
        authors='Hyang-Ah Park, Ah-ran Pae, Yong-Dae Kwon, Seoung-Jin Hong, Kun-Chul Lee, Jae-In Ryu',
        title='Analysis of the utilization rate of claimed dental implants and related factors',
        doi='10.22974/jkda.2024.62.10.003',
        confidence='retrospective',
        oneline_kr='NHIS Health Checkup Cohort 분석(n=63,880, 75세 대상): 임플란트 급여 이용률 Phase 1 3.4% → Phase 2 6.3% → Phase 3 7.0%로 지속 상승. 연 1회 구강검진자는 임플란트 시술 가능성 2배. 정책 결정 시 청구 추이·요인 검토 필요.',
        summary='Population-level analysis of claimed dental implant utilization in South Korea using NHIS Health Checkup Cohort. Anderson behavioral model applied. Subjects: 63,880 (covered since 2014, age 75 baseline).',
        key_contrib='Quantifies how Korean NHIS implant coverage has shifted utilization patterns over phases and which patient factors (region, insurance type, disability, oral exam habit) predict use — directly informs policy.',
        methodology='Retrospective analysis of NHIS claims. Three coverage phases compared. Fully-adjusted logistic regression on demographic/access variables.',
        results='Utilization rose 3.4% → 6.3% → 7.0% across phases. Significant regional/insurance/disability differences in early phases (p<0.05) — attenuated by Phase 3 (p>0.05). Higher phase: implant odds 1.9×. Annual oral exam attenders: 2× more likely to receive implant.',
        limitations='Single-cohort age (75); administrative-claims data does not capture clinical case selection. Policy environment changes confound time-trend interpretation.',
        related=[],
    ),
    'jkda-2025-63-11-006': dict(
        stem='kim-2025-management-peri-implantitis-perspectives',
        category='periodontics',
        year=2025, date='2025-11-01',
        authors='Sangmin Kim',
        title='Current perspectives on the management of peri-implantitis (임플란트 주위염 치료의 최신 지견)',
        doi='10.22974/jkda.2025.63.11.006',
        confidence='narrative-review',
        oneline_kr='2017 World Workshop 정의 + 2024 대한치주과학회 합의안 기반의 peri-implantitis 분류·치료 종설(KDA): BOP/PPD/주변 골 상태로 분류, 비외과+외과 치료 모두 plaque·calculus 제거 + 염증 통제 + 부착 회복이 목표. 한국 임상 맥락 정리.',
        summary='Narrative review by Korean periodontist summarizing peri-implantitis definition (2017 World Workshop), 2024 Korean Academy of Periodontology consensus classification, and management options in the Korean clinical landscape.',
        key_contrib='Bridges the international consensus (2017 World Workshop, recent reviews) with Korean Academy of Periodontology 2024 consensus classification — useful as the local-language summary for Korean clinicians.',
        methodology='Narrative review. International + Korean guideline synthesis.',
        results='Reviews classification criteria, non-surgical and surgical options, decontamination strategies, and reinforces SPT importance. Concludes with practical perspectives.',
        limitations='Narrative review; no quantitative pooling.',
        related=['periodontics/cha-2024-peri-implantitis-treatment-protocol-flowchart',
                 'periodontics/kim-2024-peri-implant-diseases-consensus-korean-academy-periodontology',
                 'periodontics/grusovin-2022-antibiotics-non-surgical-peri-implantitis-ma'],
    ),
    'jkda-2025-63-12-001': dict(
        stem='yook-2025-single-implant-effects-antagonistic-adjacent-teeth',
        category='implants',
        year=2025, date='2025-12-01',
        authors='Young-Jin Yook, Deuk-Sang Ma, Se-Hee Park, Kyung-Mo Cho, Jin-Woo Kim',
        title='Retrospective study on pathological effects of single implant-supported fixed prosthesis on antagonistic and adjacent teeth',
        doi='10.22974/jkda.2025.63.12.001',
        confidence='retrospective',
        oneline_kr='강원대 후향(n=100, 1년 이상 추적): 단일 구치 implant 보철의 대합치·인접치 영향 — distal 인접치 mobility ↑(p<0.05), 편측저작 환자에서 대합치 periapical lesion·인접치 crack ↑(p<0.05), 당뇨 환자 골 흡수·치료 이력 ↑(p<0.05), 대합 occlusal contact 없으면 골 흡수 ↓이나 인접치 cusp fracture ↑. Implant 보철은 주변 dentition에 측정 가능한 부담 유발.',
        summary='Retrospective observational study (n=100) at Gangneung-Wonju National University Dental Hospital comparing teeth adjacent and antagonistic to single posterior implants vs contralateral controls. Cracks, cusp fractures, alveolar bone, occlusal contact (Shimstock), and systemic disease associations analyzed.',
        key_contrib='Provides direct clinical evidence that single-implant restorations exert non-trivial mechanical and biological stress on neighboring dentition — useful for informed consent and occlusal scheme planning.',
        methodology='Retrospective. 100 single posterior implant patients, ≥1-year follow-up. Adjacent + antagonistic teeth vs contralateral control teeth. Clinical + radiographic comparison. Chi-square (α=0.05).',
        results='Distal adjacent tooth mobility > control (p<0.05). Non-unilateral mastication group: more periapical lesions in antagonistic teeth and cracks in adjacent teeth (p<0.05). Diabetics: more alveolar bone loss and treatment history (p<0.05). No occlusal contact on antagonist: less bone loss but more cusp fractures in adjacent. Males: more cusp fractures and cracks.',
        limitations='Retrospective, single-center, n=100. Cross-sectional pathology measurement without temporal causality. Systemic disease subgroups small.',
        related=[],
    ),
    'jkda-2026-64-2-002': dict(
        stem='kim-2026-stamp-technique-posterior-composite-resin',
        category='resin',
        year=2026, date='2026-02-01',
        authors='Min-Hae Kim, Sung-Ae Son, Jeong-Kil Park',
        title='Stamp technique for posterior teeth composite resin restoration: Report of 2 cases',
        doi='10.22974/jkda.2026.64.2.002',
        confidence='case-report',
        oneline_kr='Stamp technique 2증례: 교합면 해부학이 보존된 깊은 우식 케이스에서 flowable composite으로 인덱스를 미리 떠 두고 최종 적층 시 압인 → 자연스러운 교합면 재현, finishing 시간 단축, chair time 감소. 적응증: Class I + 교합면 보존. 한계: 교합면 결손·중합 수축 응력 집중 우려.',
        summary='Case report (2 cases, mandibular second molars) demonstrating the stamp technique — fabricating a flowable composite index of the intact occlusal surface before cavity preparation and using it to imprint the final composite layer for anatomic accuracy.',
        key_contrib='Practical demonstration of the stamp technique in routine Class I caries with intact occlusal anatomy. Highlights efficiency (less finishing/polishing, reduced chair time) and esthetic gains.',
        methodology='Two-case clinical report. Stamp fabrication with flowable composite over intact occlusal anatomy. Conventional caries removal and incremental composite placement. Stamp applied to final increment before light-curing.',
        results='Both cases: accurate anatomical reproduction, minimal finishing, reduced chair time. Subjective patient satisfaction reported as good.',
        limitations='Case-level evidence (n=2). Technique inapplicable when occlusal anatomy is already destroyed. Single-increment final step may concentrate polymerization stress.',
        related=[],
    ),
    'jkda-2026-64-2-004': dict(
        stem='kim-2026-key-points-private-dental-insurance',
        category='practice-management',
        year=2026, date='2026-02-01',
        authors='Eui-Dong Kim',
        title='Key points on private dental insurance (치과 민간보험 핵심 정리)',
        doi='10.22974/jkda.2026.64.2.004',
        confidence='narrative-review',
        oneline_kr='한국 치과 민간보험 핵심 정리(KDA): 치아보험(주력)·생명보험(특약 골이식)·실손보험(2009년 8월 이후 2세대부터 급여 본인부담 보장)·상해/손해보험(골절 진단금). 면책기간·갱신 등 핵심 약관 정리, 진료기록부·청구서류 작성 시 치과의사가 알아두면 환자 도움.',
        summary='Korean Dental Association practice-management primer on private dental insurance in South Korea: product types, coverage scopes (tooth insurance, life-insurance riders, indemnity, accident/casualty), and key contract features (waiting periods, renewal terms).',
        key_contrib='Compact reference for Korean dental practitioners on the private insurance landscape — useful for accurate paperwork, patient counseling, and avoiding leakage of legitimate patient claims.',
        methodology='Practice-management narrative. Author practitioner perspective.',
        results='Summarized characteristics by product type and a checklist of clauses (waiting periods, renewal, coverage triggers) that frequently affect dental claims.',
        limitations='Narrative; specific to South Korean private insurance market and as of 2026 publication. Product terms change.',
        related=[],
    ),
    'jpis-54-295': dict(
        stem='cha-2024-peri-implantitis-treatment-protocol-flowchart',
        category='periodontics',
        year=2024, date='2024-01-04',
        authors='Jae-Kook Cha et al.',
        title='Up-to-date treatment options for peri-implantitis and a treatment protocol with flowchart based on current evidence',
        doi='10.5051/jpis.2303360168',
        confidence='narrative-review',
        oneline_kr='Peri-implantitis treatment narrative review (J Periodontal Implant Sci): 단계별 의사결정 흐름도 제안 — extraction/failed vs failing 분류 → 비외과(항생제 adjunct 권장) → 외과(resective/access/reconstructive, 결손 형태 기반 선택) → 표면 detoxification(기계·화학·약리 병용) → 유지관리. 성공 기준: PPD ≤5mm, BOP·suppuration·진행성 골 흡수 부재.',
        summary='Narrative review proposing a phased peri-implantitis treatment protocol with a decision flowchart, anchored on contemporary evidence. Treatment goals operationalized via measurable success criteria.',
        key_contrib='Operationalizes peri-implantitis management as a continuous decision cycle (assess → treat → re-evaluate → maintain) rather than a single procedure — directly useful as a clinical SOP.',
        methodology='Narrative review with evidence-anchored treatment flowchart. Phased decision logic (extraction / non-surgical / surgical / maintenance).',
        results='Success criteria: PPD ≤5 mm, no BOP/suppuration, no progressive bone loss. Failed implants → remove. Failing implants → non-surgical first (with antibiotic adjunct), then surgical (resective/access/reconstructive based on defect). Decontamination strategy by surgical purpose. SPT mandatory post-active treatment.',
        limitations='Narrative review; flowchart not yet validated in prospective trial.',
        related=['periodontics/grusovin-2022-antibiotics-non-surgical-peri-implantitis-ma',
                 'periodontics/kim-2024-peri-implant-diseases-consensus-korean-academy-periodontology',
                 'periodontics/kim-2025-management-peri-implantitis-perspectives'],
    ),
    'jpis-54-377': dict(
        stem='kim-2024-peri-implant-diseases-consensus-korean-academy-periodontology',
        category='periodontics',
        year=2024, date='2024-12-30',
        authors='Yun-Jeong Kim, Young Woo Song, Shin-Young Park, Jae-Kook Cha, Jun-Beom Park, Ki-Tae Koo',
        title='Current understanding of the etiology, diagnosis, treatment, and management of peri-implant diseases: a narrative review for the consensus report of the Korean Academy of Periodontology',
        doi='10.5051/jpis.2404630231',
        confidence='consensus',
        oneline_kr='대한치주과학회 합의안 narrative review (J Periodontal Implant Sci 2024): peri-implant mucositis 43% + peri-implantitis 22% 유병률. 위험인자: 구강위생 불량, periodontitis 병력, 당뇨, 흡연. 치료: mucositis는 비외과, peri-implantitis는 mechanical+chemical debridement + 외과 access; 실패한 implant는 제거 후 결손 복원. 한국 임상 가이드 정리.',
        summary='Narrative review backing the Korean Academy of Periodontology consensus report on peri-implant diseases. Covers definition/prevalence/classification, risk indicators, diagnostic criteria, and treatment protocols.',
        key_contrib='Defines the Korean-academy-endorsed framework for peri-implant disease diagnosis and treatment — the local consensus reference for SOPs and patient education in Korean clinics.',
        methodology='Narrative consensus review structured in four sections: (1) definition/prevalence/classification, (2) risk indicators and etiology, (3) diagnostic criteria, (4) treatment protocols.',
        results='Mucositis prevalence 43%, peri-implantitis 22%. Key risks: poor hygiene, periodontitis history, diabetes, smoking. Outcomes influenced by prosthesis design and soft tissue condition. Treatment hierarchy: non-surgical → comprehensive (mechanical/chemical/surgical) → removal + reconstruction. Maintenance critical.',
        limitations='Narrative consensus, not a systematic synthesis; risk-factor estimates from heterogeneous primary literature.',
        related=['periodontics/cha-2024-peri-implantitis-treatment-protocol-flowchart',
                 'periodontics/grusovin-2022-antibiotics-non-surgical-peri-implantitis-ma',
                 'periodontics/kim-2025-management-peri-implantitis-perspectives'],
    ),
}

print(f'Mapping size: {len(ENTRIES)}')

import glob
existing = set()
for p in glob.glob('wiki/**/*.md', recursive=True):
    existing.add(os.path.splitext(os.path.basename(p))[0])
collisions = [e['stem'] for e in ENTRIES.values() if e['stem'] in existing]
print(f'Stem collisions: {collisions}')
assert not collisions

# rename PDFs
for old, e in ENTRIES.items():
    old_p = f'papers/{old}.pdf'
    new_p = f'papers/{e["stem"]}.pdf'
    if os.path.exists(old_p) and old != e['stem']:
        if os.path.exists(new_p):
            print(f'  WARN: {new_p} exists — skipping')
        else:
            os.rename(old_p, new_p)
print(f'  renamed {len(ENTRIES)} PDFs')

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
- **PPD:** Probing Pocket Depth.
- **PAL:** Probing Attachment Level.
- **BOP:** Bleeding on Probing.
- **MBL:** Marginal Bone Loss.
- **SPT:** Supportive Periodontal Therapy.
- **NHIS:** National Health Insurance Service (Korea).
- **KDA:** Korean Dental Association.
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

# index update
from collections import defaultdict
by_cat = defaultdict(list)
for e in ENTRIES.values():
    by_cat[e['category']].append(e)
with open('index.md') as f:
    idx = f.read()
marker = '<!-- BATCH INGEST 2026-05-24c'
if marker not in idx:
    new_block = f'\n\n{marker}: peri-implantitis + KDA implant policy + cracked tooth + stamp + insurance -->\n'
    for cat in sorted(by_cat.keys()):
        new_block += f'\n### {cat} (added 2026-05-24, batch c)\n\n'
        for e in sorted(by_cat[cat], key=lambda x: (x['year'], x['stem'])):
            fa = e['authors'].split(',')[0]
            new_block += f'- [[{cat}/{e["stem"]}]] — {fa} {e["year"]} · {e["confidence"]} · {e["title"]}\n'
    with open('index.md', 'w') as f:
        f.write(idx + new_block)
    print('  index.md updated')

# lint
pdfs = {os.path.splitext(f)[0] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs = {os.path.splitext(f)[0] for f in os.listdir('sources') if f.endswith('.md')}
print(f'\nLINT: papers={len(pdfs)} sources={len(srcs)} orphan_pdfs={len(pdfs-srcs)} orphan_sources={len(srcs-pdfs)}')
