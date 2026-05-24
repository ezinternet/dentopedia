#!/usr/bin/env python3
"""
Second batch ingest for 2026-05-24 session (8 PDFs).
Topics: short implants (5), ARP review (1), BMS (1), free-flap reconstruction (1).
"""
import os, warnings
warnings.filterwarnings('ignore')

ROOT = '/sessions/trusting-ecstatic-faraday/mnt/llm-wiki'
os.chdir(ROOT)

ENTRIES = {
    '40729_2022_Article_438': dict(
        stem='anitua-2022-short-vs-longer-implants-single-crown',
        category='implants',
        year=2022, date='2022-09-26',
        authors='Eduardo Anitua, Mohammad Hamdan Alkhraisat, Asier Eguia',
        title='Single-crown restorations in premolar–molar regions: short (≤ 6.5) vs longer implants: retrospective cohort study',
        doi='10.1186/s40729-022-00438-y',
        confidence='retrospective',
        oneline_kr='STROBE 후향 cohort (n=88+88, follow-up 11–117개월): 단일 크라운 보철에서 short(≤6.5mm) vs long(≥7.5mm) 임플란트 사이 survival·MBL·보철 합병증 차이 없음 — short implant가 후방 단일 보철에서 합리적 옵션.',
        summary='STROBE-compliant retrospective cohort comparing short (≤6.5 mm) vs longer (≥7.5 mm) implants supporting single-crown restorations in posterior premolar/molar regions. Same surgeon, same prosthetic concept (transepithelial abutment + screw-retained crown).',
        key_contrib='Single-operator/single-protocol design isolates implant length as the variable. Provides medium-term evidence that short implants are non-inferior for single-crown indications in posterior regions.',
        methodology='Retrospective cohort following STROBE. 88 short + 88 long implants. Outcomes: survival, marginal bone level changes, prosthetic complications.',
        results='No statistical differences. Median follow-up 31 (short) vs 35 (long) months. Prosthetic complications: screw loosening 2 vs 5, ceramic chipping 1 vs 0. MBL ≥2 mm in 1/88 vs 3/88 (p=0.312).',
        limitations='Retrospective; non-randomized; single surgeon; medium follow-up. Inclusion bias possible.',
        related=['implants/yu-2021-extra-short-vs-longer-implants-ma',
                 'implants/sivolella-2025-extra-short-5-6mm-implants-5year',
                 'implants/barausse-2024-4mm-short-implants-posterior-atrophic-8year'],
    ),
    '40729_2025_Article_592': dict(
        stem='sivolella-2025-extra-short-5-6mm-implants-5year',
        category='implants',
        year=2025, date='2025-01-15',
        authors='Stefano Sivolella et al.',
        title='Extra-short (5–6 mm) implants under immediate loading: 5-year survival, MBL, and the impact of intermediate abutment use',
        doi='10.1186/s40729-025-00592-z',
        confidence='retrospective',
        oneline_kr='5–6 mm extra-short implant 5년 추적(n=56/34명): 전체 survival 89% (즉시부하 94% vs conventional 87%), 즉시부하는 MBL ↑(+0.21mm), intermediate abutment는 MBL ↓(-0.23mm) — 부하 프로토콜과 abutment 선택이 MBL에 직접 영향.',
        summary='Five-year clinical and radiological follow-up of extra-short (5–6 mm) implants in posterior maxilla/mandible. Compares conventional vs immediate loading and assesses the role of intermediate abutments. 56 implants in 34 patients.',
        key_contrib='Quantifies the interaction of two prosthetic choices (immediate-loading + intermediate abutment) on extra-short implant MBL over 5 years.',
        methodology='Retrospective clinical and radiological 5-year follow-up. Univariate and multivariable analysis of MBL by loading protocol and abutment configuration.',
        results='5-year survival 89% overall (87% conventional, 94% immediate). Immediate loading associated with higher MBL (+0.21 mm; p=0.02). Intermediate abutment associated with lower MBL (-0.23 mm; p=0.003). Multivariable analysis confirmed immediate loading effect.',
        limitations='Single-center retrospective; small n (56 implants); 4 failures clustered in one patient skewed loss rate.',
        related=['implants/anitua-2022-short-vs-longer-implants-single-crown',
                 'implants/yu-2021-extra-short-vs-longer-implants-ma',
                 'implants/barausse-2024-4mm-short-implants-posterior-atrophic-8year'],
    ),
    '41598_2021_Article_87507': dict(
        stem='yu-2021-extra-short-vs-longer-implants-ma',
        category='implants',
        year=2021, date='2021-04-15',
        authors='Xiaoran Yu, Ruogu Xu, Zhengchuan Zhang, Yang Yang, Feilong Deng',
        title='A meta-analysis indicating extra-short implants (≤ 6 mm) as an alternative to longer implants (≥ 8 mm) with bone augmentation',
        doi='10.1038/s41598-021-87507-1',
        confidence='sr+ma',
        oneline_kr='SR+MA (21 RCT): extra-short ≤6mm vs long ≥8mm — 1·3년 survival 차이 없음, 5년에는 longer가 우세(RR 0.970). 단 augmentation 동반 5년 비교에서는 short가 비열등. MBL과 biological complications는 short가 유리. 결론: short implant는 augmentation 대안으로 수용 가능.',
        summary='Meta-analysis of 21 RCTs comparing extra-short (≤6 mm) vs longer (≥8 mm) implants. AMSTAR-2 + GRADE quality appraisal. Outcomes: survival, MBL, biological/prosthetic complications.',
        key_contrib='High-quality SR+MA establishing the time-horizon-dependent equivalence/non-inferiority profile of extra-short implants vs augmentation+long implants.',
        methodology='SR of PubMed/WoS/EMBASE/Cochrane through Nov 2020. Only RCTs with ≥1-year follow-up. Cochrane RoB 2 + GRADE. Quantitative meta-analysis.',
        results='No survival difference at 1y (RR 1.002) or 3y (RR 0.996). Longer implants higher survival at 5y (RR 0.970, p<0.05) — but parity in subgroup with bone augmentation. MBL favored extra-short (WMD -0.22). Biological complications favored extra-short (RR 0.321). No difference in MBL from prosthesis or prosthetic complications.',
        limitations='Heterogeneity across implant systems and protocols. Low-quality evidence on some MBL endpoints.',
        related=['implants/anitua-2022-short-vs-longer-implants-single-crown',
                 'implants/sivolella-2025-extra-short-5-6mm-implants-5year',
                 'implants/barausse-2024-4mm-short-implants-posterior-atrophic-8year'],
    ),
    '41598_2025_Article_1012': dict(
        stem='hockova-2025-short-implants-microvascular-free-flaps',
        category='implants',
        year=2025, date='2025-01-01',
        authors='Barbora Hocková, Rastislav Slávik, Dušan Poruban, Estevam A. Bonfante, Rolf Ewers, Adam Stebel, Yu-Chi Cheng',
        title='Quality of life of patients receiving short dental implants in microvascular free flaps: a five year prospective study',
        doi='10.1038/s41598-025-01012-x',
        confidence='prospective',
        oneline_kr='5년 전향 연구(n=13명, 44 implants): 두경부 종양 후 microvascular free flap 재건부에 short implant 식립 — survival 97.1% (95% CI 80.9–99.6%), success 88.2%, QoL(저작·언어) 유의 개선. 종양 재건 환자에서 short implant의 임상적 유효성 입증.',
        summary='Five-year prospective study of 13 head-and-neck cancer patients (44 implants) who received short dental implants in microvascular bone free flaps (fibula/iliac crest/scapula). Assesses survival, success, and quality-of-life.',
        key_contrib='First substantial prospective QoL data for short implants placed in free-flap-reconstructed jaws — directly informs oncologic-reconstruction prosthodontic protocols.',
        methodology='Prospective cohort; 13 patients, 44 implants in 4 free-flap types. 63-month follow-up. QoL questionnaires at multiple time points.',
        results='Survival 97.1% (95% CI: 80.9–99.6%) at 63 months. Success 88.2% (95% CI: 71.6–95.4%). QoL improved especially in food intake and articulation.',
        limitations='Small sample (n=13); heterogeneous flap types; no comparator arm.',
        related=['implants/yu-2021-extra-short-vs-longer-implants-ma',
                 'oral-surgery/cebrian-carretero-2014-free-flap-implant-guided-surgery',
                 'implants/barausse-2024-4mm-short-implants-posterior-atrophic-8year'],
    ),
    'CLR-35-1607': dict(
        stem='barausse-2024-4mm-short-implants-posterior-atrophic-8year',
        category='implants',
        year=2024, date='2024-07-30',
        authors='Carlo Barausse, Roberto Pistilli, Lorenzo Bonifazi, Subhi Tayeb, Gerardo Pellegrino, Andrea Ravidà, Pietro Felice',
        title='Four-mm-short implants in the rehabilitation of posterior atrophic jaws: A retrospective study on 212 patients with a mean follow-up of 8.02 years',
        doi='10.1111/clr.14349',
        confidence='retrospective',
        oneline_kr='4mm short implant 후향 연구(n=212명, 496 implants, 평균 8년): survival 95.36% (CI 93.12–97.04). 상악 실패율 ↑(p=0.02), 정기 hygiene 세션 많을수록 실패율 ↓(p<0.001). 1년 MBL 0.47mm → 10년 0.59mm. 후방 위축악 재활에서 4mm short implant는 장기간 안정적 옵션.',
        summary='Long-term retrospective study of 4-mm short implants in 212 patients (496 implants) with posterior severe vertical atrophy, mean follow-up 8.02 years.',
        key_contrib='Largest long-term cohort data for 4-mm-short implants. Identifies maxilla and hygiene-session frequency as outcome modifiers — actionable for case selection and SPT design.',
        methodology='Retrospective. Minimum 3-year follow-up post-loading. MBL per implant, failures, complications tracked. Multivariate analysis of failure predictors.',
        results='Survival 95.36% at mean 8 years. Maxillary > mandibular failures (p=0.02). More hygienic sessions per year → fewer failures (p<0.001). MBL 0.47 mm at 1y → 0.59 mm at 10y, with no significant increase after 3 years.',
        limitations='Retrospective; single-team; selection bias possible (only treated cases analyzed).',
        related=['implants/anitua-2022-short-vs-longer-implants-single-crown',
                 'implants/sivolella-2025-extra-short-5-6mm-implants-5year',
                 'implants/yu-2021-extra-short-vs-longer-implants-ma'],
    ),
    'jkda-2024-62-5-003': dict(
        stem='lee-2024-burning-mouth-syndrome-clinical-treatment',
        category='drug',
        year=2024, date='2024-05-01',
        authors='Eunjin Lee, Hee-Kyung Park',
        title='A retrospective study on the clinical characteristics and treatment outcomes of patients with burning mouth syndrome',
        doi='10.22974/jkda.2024.62.5.003',
        confidence='retrospective',
        oneline_kr='SNU 구강내과 후향(n=248, 여 217·남 31, 평균 64.7세): BMS 1차 방문 시 parafunctional habit control + 타액대체 + 심리 안정 상담만으로 NRS 유의 감소; 2~4차 방문에서 clonazepam·zinc 보충제 추가로 추가 감소. 19.35%가 혈청 zinc ≤70 μg/dL — zinc 결핍 동반 비율이 무시못함.',
        summary='Retrospective study of 248 burning mouth syndrome (BMS) patients at Seoul National University Department of Oral Medicine. Stepwise treatment protocol with parafunctional habit control, saliva substitutes, psychological counseling, then clonazepam and zinc supplements. NRS as outcome.',
        key_contrib='Korean-population BMS clinical profile and a documented stepwise treatment protocol — practical reference for the oral medicine treatment of BMS, including the role of zinc supplementation.',
        methodology='Retrospective chart review. 248 patients, mean age 64.7 ± 11.2, 87.5% female. Stepwise protocol applied. NRS measured at each visit. Serum zinc evaluated.',
        results='Significant NRS reduction after visit-1 (non-pharmacologic only). Further reduction with clonazepam / zinc supplements at visits 2–4. 19.35% (48/248) had serum zinc ≤70 μg/dL — sub-threshold for biochemical deficiency in many references.',
        limitations='Retrospective; single-center; no comparator arm; NRS subject to recall and reporting bias.',
        related=[],
    ),
    'jkda-2024-62-8-001': dict(
        stem='che-2024-alveolar-ridge-preservation-review',
        category='bone-regeneration',
        year=2024, date='2024-08-01',
        authors='Sung-Ah Che, Soo-Hwan Byun, Sang-Min Yi, Sang-Yoon Park, Byoung-Eun Yang',
        title='Navigating Alveolar Ridge Preservation: Techniques, Materials, and Clinical Implications',
        doi='10.22974/jkda.2024.62.8.001',
        confidence='narrative-review',
        oneline_kr='ARP 종설(한림대 OMFS): 발치 후 alveolar bone 흡수를 최소화하기 위한 ARP의 술기·이식재·socket sealing 검토 — granulation 제거 → 적절 이식재 → socket sealing이 ideal protocol, 그러나 이식재·임플란트 식립 timing에 대한 명확 가이드라인은 아직 부재.',
        summary='Narrative review of alveolar ridge preservation (ARP) techniques, graft materials, and clinical implications. Korean Dental Association journal.',
        key_contrib='Compact ARP procedural and material overview suitable as a reference primer for clinicians considering ARP indications before implant placement.',
        methodology='Literature review. ARP techniques, available graft materials, and socket-sealing options synthesized. Implications for subsequent implant placement discussed.',
        results='Ideal ARP = granulation tissue removal → suitable graft → socket sealing. Demonstrated to minimize invasiveness at subsequent implant placement. Lacks consensus on optimal graft type and implant-placement timing.',
        limitations='Narrative review (not systematic); no quantitative pooling; published guidelines still missing.',
        related=[],
    ),
    'medoral-19-e605': dict(
        stem='cebrian-carretero-2014-free-flap-implant-guided-surgery',
        category='oral-surgery',
        year=2014, date='2014-11-01',
        authors='José-Luis Cebrian-Carretero, Jorge Guiñales-Díaz de Cevallos, José-Andrés Sobrino, Tomás Yu, Miguel Burgueño-García',
        title='Predictable dental rehabilitation in maxillomandibular reconstruction with free flaps. The role of implant guided surgery',
        doi='10.4317/medoral.19873',
        confidence='narrative-review',
        oneline_kr='악골 재건(fibula/iliac crest/scapula free flap) 환자에서 guided implant surgery의 역할 종설 — flap의 가장 골조건 좋은 영역과 osteosynthesis 자재를 회피하는 위치 선정에 guided 방식이 필수, esthetic+functional 결과의 예측가능성을 끌어올림.',
        summary='Narrative review on guided implant surgery for dental rehabilitation in patients reconstructed with microvascular free flaps after maxillomandibular oncologic resection.',
        key_contrib='Articulates why guided surgery is essential (not optional) in free-flap-reconstructed jaws: bone variability + osteosynthesis hardware + biomechanical demands require pre-planning.',
        methodology='Narrative review summarizing free flap options (fibula, iliac crest, scapula) and the planning workflow for implant-guided surgery in this context.',
        results='Guided surgery enables (1) implant positioning in the highest-quality bone regions, (2) avoidance of osteosynthesis hardware, (3) prosthetically-driven planning despite anatomic constraints.',
        limitations='Narrative review; case-illustration based; no quantitative outcome synthesis.',
        related=['implants/hockova-2025-short-implants-microvascular-free-flaps'],
    ),
}

print(f'Mapping size: {len(ENTRIES)}')

# Verify no stem collisions with existing wiki
import glob
existing = set()
for p in glob.glob('wiki/**/*.md', recursive=True):
    existing.add(os.path.splitext(os.path.basename(p))[0])
collisions = [e['stem'] for e in ENTRIES.values() if e['stem'] in existing]
print(f'Stem collisions: {collisions}')
assert not collisions, 'Stem collision detected'

# ── 1. Rename PDFs ────────────────────────────────────────────────
for old, e in ENTRIES.items():
    old_path = f'papers/{old}.pdf'
    new_path = f'papers/{e["stem"]}.pdf'
    if os.path.exists(old_path) and old != e['stem']:
        if os.path.exists(new_path):
            print(f'  WARN: {new_path} exists — skipping rename')
        else:
            os.rename(old_path, new_path)
print(f'  renamed {len(ENTRIES)} PDFs')


# ── 2. Generate sources/ and wiki/ ────────────────────────────────
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
- **MBL:** Marginal Bone Loss.
- **CBCT:** Cone-Beam Computed Tomography.
- **SR+MA:** Systematic Review + Meta-Analysis.
- **RCT:** Randomized Controlled Trial.
- **ARP:** Alveolar Ridge Preservation.
- **BMS:** Burning Mouth Syndrome.
- **NRS:** Numeric Rating Scale (pain).
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
    if not rels: return '- (none)'
    return '\n'.join(f'- [[{r}]]' for r in rels)

for old, e in ENTRIES.items():
    common = dict(e, related_md=fmt_related(e.get('related', [])))
    with open(f'sources/{e["stem"]}.md', 'w') as f:
        f.write(SOURCES_TPL.format(**common))
    cat_dir = f'wiki/{e["category"]}'
    os.makedirs(cat_dir, exist_ok=True)
    with open(f'{cat_dir}/{e["stem"]}.md', 'w') as f:
        f.write(WIKI_TPL.format(**common))

print(f'  wrote {len(ENTRIES)} sources/ files')
print(f'  wrote {len(ENTRIES)} wiki/ files')

# ── 3. Append to index.md ─────────────────────────────────────────
from collections import defaultdict
by_cat = defaultdict(list)
for e in ENTRIES.values():
    by_cat[e['category']].append(e)

with open('index.md') as f:
    idx = f.read()

marker = '<!-- BATCH INGEST 2026-05-24b'
if marker not in idx:
    new_block = f'\n\n{marker}: short implants + ARP + BMS + free-flap -->\n'
    for cat in sorted(by_cat.keys()):
        new_block += f'\n### {cat} (added 2026-05-24, batch b)\n\n'
        for e in sorted(by_cat[cat], key=lambda x: (x['year'], x['stem'])):
            first_author = e['authors'].split(',')[0]
            new_block += f'- [[{cat}/{e["stem"]}]] — {first_author} {e["year"]} · {e["confidence"]} · {e["title"]}\n'
    with open('index.md', 'w') as f:
        f.write(idx + new_block)
    print('  index.md updated')
else:
    print('  index.md already contains this batch')

# ── 4. Lint ───────────────────────────────────────────────────────
pdfs = {os.path.splitext(f)[0] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs = {os.path.splitext(f)[0] for f in os.listdir('sources') if f.endswith('.md')}
op = pdfs - srcs
os_ = srcs - pdfs
print(f'\nLINT: papers={len(pdfs)} sources={len(srcs)} orphan_pdfs={len(op)} orphan_sources={len(os_)}')
if op: print(f'  orphan PDFs: {sorted(op)}')
if os_: print(f'  orphan sources: {sorted(os_)}')
