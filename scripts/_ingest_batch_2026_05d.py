#!/usr/bin/env python3
"""
Fourth batch ingest for 2026-05 session (3 PDFs).
Topics: osseodensification — Bergamo 2021 stability RCT, Mazor 2024 TSFE perforation, Neiva 2018 Astra TX/EV abstract.
"""
import os, warnings
warnings.filterwarnings('ignore')

ROOT = '/Users/oracleneo/llm-wiki'
os.chdir(ROOT)

ENTRIES = {
    'Bergamo_2021_PMID34047046_OD_PrimarySecondaryStability': dict(
        stem='bergamo-2021-osseodensification-effect-implants-primary-secondary',
        category='implants',
        year=2021, date='2021-05-28',
        authors='Edmara T. P. Bergamo, Abbas Zahoui, Raúl Bravo Barrera, Salah Huwais, Paulo G. Coelho, Edward Dwayne Karateew, Estevam A. Bonfante',
        title='Osseodensification effect on implants primary and secondary stability: Multicenter controlled clinical trial',
        doi='10.1111/cid.13007',
        confidence='prospective',
        oneline_kr='Multicenter controlled clinical trial (56명, 150 임플란트): 골밀도화(Osseodensification, OD) vs 일반 절삭드릴(Subtractive Drilling, SD) — OD가 식립토크(IT)·임플란트 안정성 지수(ISQ) 모두 유의 우위, ISQ가 치유 3주차에 dip 후 6주 회복하는데 OD는 전 기간 ISQ ≥ 68 유지. Short 임플란트는 예외(차이 없음).',
        summary='Multicenter controlled clinical trial comparing osseodensification (OD) to conventional subtractive drilling (SD) for insertion torque and longitudinal ISQ across implant designs and jaw regions.',
        key_contrib='Provides the first multicenter clinical-trial-level evidence that OD elevates and maintains ISQ above the 68 loading threshold throughout the early healing dip — supporting earlier loading protocols. Short implants do not benefit, indicating macrogeometry-dependent ceiling effects.',
        methodology='56 patients each receiving ≥2 implants (n = 150). Stratified by implant diameter (narrow/regular/wide), length (short/regular/long), arch (maxilla/mandible), region (anterior/posterior). ITs recorded with torque indicator; ISQs by RFA at placement, 3 weeks, 6 weeks.',
        results='OD outperformed SD on IT across all pairwise comparisons except short implants. ISQ values significantly higher for OD at all timepoints; ISQ dipped at 3 weeks and returned to baseline at 6 weeks, but for OD the values remained ≥ 68 throughout. Short implants showed no OD–SD difference.',
        limitations='Not randomized despite "controlled" labeling. Only 6 weeks follow-up — no loaded-implant survival data. Healing dip in ISQ for short implants suggests OD may not overcome biomechanical limits when bone engagement is length-limited.',
        related=['implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability',
                 'implants/inchingolo-2021-osseodensification-implant-site-osteotomy-sr-ma',
                 'implants/gaspar-2022-implant-stability-osseodensification-conventional-sr-ma',
                 'implants/isq/althobaiti-2023-osseodensification-conventional-drilling-isq-sr'],
    ),
    'Mazor_2024_PMID39187444_TSFE_MembranePerforation': dict(
        stem='mazor-2024-maxillary-sinus-membrane-perforation-osseodensification',
        category='sinus-lift/transcrestal',
        year=2024, date='2024-08-26',
        authors='Ziv Mazor, Joao Gaspar, Robert Silva, Snjezana Pohl, Yazad Gandhi, Salah Huwais, Edmara Tatiely Pedroso Bergamo, Estevam Augusto Bonfante, Rodrigo Neiva',
        title='Maxillary sinus membrane perforation rate utilizing osseodensification-mediated transcrestal sinus floor elevation: A multicenter clinical study',
        doi='10.1111/cid.13368',
        confidence='cross-sectional',
        oneline_kr='Multicenter cross-sectional (6개 센터, 621명·670 sites): 골밀도화(Osseodensification, OD) 버 기반 경치조골 상악동 거상술(Transcrestal Sinus Floor Elevation, TSFE) — 슈나이더막 천공률 7.31%로 기존 보고치(7–58%) 하단. 잔존 골높이(Residual Bone Height, RBH) ≤3 mm가 천공의 독립 위험인자, 부위(전치/구치)·socket 상태(healed/fresh)는 영향 없음.',
        summary='Largest multicenter clinical study to date evaluating sinus membrane perforation rate during OD-mediated transcrestal sinus floor elevation. 621 patients across 6 international centers.',
        key_contrib='Establishes membrane perforation rate of OD-TSFE at ~7% — comparable to the favorable end of the historical TSFE/lateral-window range — and identifies RBH ≤3 mm (severe atrophy) as the dominant risk factor. Tooth region (premolar vs molar) and socket state (healed vs fresh) were not predictive, simplifying preoperative risk stratification.',
        methodology='Multicenter cross-sectional study at 6 centers (Israel, Portugal, Brazil, Croatia, India, USA). Inclusion: ≥18 y, maxillary posterior tooth missing, RBH 2–6 mm. Standardized OD-TSFE protocol (Densah bur, CCW). CBCT preoperatively. Risk factors analyzed: implant site, premolar/molar, healed/fresh socket, RBH. Statistics: descriptive, χ², logistic regression.',
        results='670 sinus lifts, 621 implants placed in maxilla. 76.87% in molar region, 74.33% healed sites. Average RBH 5.1 mm (range 2–7 mm). Membrane perforation in 49 cases (7.31%). RBH ≤3 mm = significant risk factor, followed by RBH >3 and ≤5 mm. Region (premolar/molar) and site (healed/fresh) not significant.',
        limitations='Cross-sectional — no causal inference on bur protocol vs other techniques. Multicenter heterogeneity in surgeon experience controlled only by protocol standardization. No comparison arm (lateral window or osteotome-TSFE) — perforation rate is reported in isolation. Short-term outcome only (perforation event); no implant survival or bone gain reported.',
        related=['sinus-lift/transcrestal/cobo-vazquez-2025-crestal-sinus-lift-osteotome-vs-osseodensification',
                 'sinus-lift/transcrestal/el-ghobashy-osseodensification-vs-osteotome-transcrestal-sinus',
                 'sinus-lift/transcrestal/farina-2023-minimal-invasiveness-transcrestal-sinus-elevation',
                 'implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability'],
    ),
    'Effects of osseodensification on Astra TX and EV implant systems - Neiva - 2018 - Clinical Oral Implants Research - Wiley Online Library': dict(
        stem='neiva-2018-effects-osseodensification-astra-tx-ev',
        category='implants',
        year=2018, date='2018-10-08',
        authors='Rodrigo Neiva, Bruna Tanello, Wagner Duarte, Paulo Coelho, Lukasz Witek, Fred Silva',
        title='Effects of osseodensification on Astra TX and EV implant systems',
        doi='10.1111/clr.329_13358',
        confidence='animal',
        oneline_kr='EAO 2018 e-poster abstract (sheep, 6마리·hip): Astra TX vs EV 임플란트에 골밀도화(Osseodensification, OD, Densah CCW) vs 표준 절삭(R) vs Densah CW — IT/RFA는 OD가 압도적 우위(시스템 무관), 골-임플란트 접촉률(Bone-to-Implant Contact, BIC)/BAFO는 EV에서 OD가 R보다 크게 우위(TX는 차이 미미). EV가 두 시스템 비교에서 모든 protocol에서 OD 활용도 우월.',
        summary='Conference e-poster abstract (Clinical Oral Implants Research Vol 29 Suppl S17) reporting sheep iliac-bone study comparing osseodensification (Densah CCW), Densah clockwise, and standard subtractive drilling on Astra TX and EV implant systems.',
        key_contrib='Macrogeometry × osteotomy-protocol interaction effect: Astra EV (newer, more aggressive thread) benefits substantially from OD on BIC/BAFO; the older TX system does not. Suggests OD efficacy is implant-design dependent, not universal.',
        methodology='6 male sheep, 3 implants of each type (TX, EV) bilaterally in iliac bone, n=36/system. Three osteotomy protocols per implant: regular drilling (R) with 2.0/3.2/3.8 mm twist drills; Densah CW (2.0/2.8/3.8 mm multifluted, clockwise); Densah CCW (osseodensification). IT and RFA at placement, 6-week healing, histology.',
        results='Densah protocols showed substantially higher IT and RFA than R, independent of implant system. TX: minimal difference between R and Densah on BIC/BAFO. EV: large advantage for Densah over R on BIC/BAFO. EV > TX across all protocols on BIC/BAFO. Histology: autogenous bone chip debris in trabecular spaces and in contact with implant in OD groups, rarely with R.',
        limitations='Conference abstract — no peer-reviewed full paper. Small n (6 animals). Sheep ilium model, not jaw bone. No quantitative values (IT, RFA, BIC%) reported in abstract — qualitative only. 6-week timepoint only; no long-term outcome. No statistical detail beyond "substantially higher".',
        related=['implants/huwais-2017-novel-osseous-densification-osteotomy-primary-stability',
                 'implants/surface/lahens-2019-osseodensification-implant-surface-treatments-sheep',
                 'implants/inchingolo-2021-osseodensification-implant-site-osteotomy-sr-ma'],
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
assert not collisions, f'Collisions: {collisions}'

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
- **OD:** Osseodensification.
- **SD:** Subtractive Drilling (conventional twist-drill osteotomy).
- **IT:** Insertion Torque.
- **ISQ:** Implant Stability Quotient (resonance frequency analysis).
- **BIC:** Bone-to-Implant Contact.
- **BAFO:** Bone-Area-Fraction-Occupancy.
- **RBH:** Residual Bone Height (crestal bone height below the sinus floor).
- **TSFE:** Transcrestal Sinus Floor Elevation.
- **CCW / CW:** Counterclockwise / Clockwise rotation.
- **RFA:** Resonance Frequency Analysis.
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
marker = '<!-- BATCH INGEST 2026-05-28'
if marker not in idx:
    new_block = f'\n\n{marker}: osseodensification — Bergamo 2021 stability RCT + Mazor 2024 TSFE perforation + Neiva 2018 Astra abstract -->\n'
    for cat in sorted(by_cat.keys()):
        new_block += f'\n### {cat} (added 2026-05-28, batch d)\n\n'
        for e in sorted(by_cat[cat], key=lambda x: (x['year'], x['stem'])):
            fa = e['authors'].split(',')[0]
            new_block += f'- [[{cat}/{e["stem"]}]] — {fa} {e["year"]} · {e["confidence"]} · {e["title"]}\n'
    with open('index.md', 'w') as f:
        f.write(idx + new_block)
    print('  index.md updated')

# Lint
pdfs = {os.path.splitext(f)[0] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs = {os.path.splitext(f)[0] for f in os.listdir('sources') if f.endswith('.md')}
print(f'\nLINT: papers={len(pdfs)} sources={len(srcs)} orphan_pdfs={len(pdfs-srcs)} orphan_sources={len(srcs-pdfs)}')
