# LLM Wiki — Dentistry (치과학)

A personal knowledge base of dental research papers, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

```
Original PDF → sources/*.md (LLM summary) → wiki/{category}/*.md (final page)
```

**Language policy**: Wiki body content is in English (RAG-friendly, preserves technical terms). Every wiki page AND every source page carries a **bilingual one-line summary** as two separate sections, in this order: `## One-line Summary` (English) immediately followed by `## 한줄요약` (Korean). On wiki pages this pair sits immediately above `## Summary`; on source pages it sits immediately above `## 1. Document Information`. Both languages are mandatory for new pages. Conversation can be in any language (including Korean).

**Term notation rule**: When using technical/medical terms in conversation, ALWAYS write them as **한국어 (English, 약어)** format. Example: 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC), 골밀도화 (Osseodensification, OD), 임플란트 안정성 지수 (Implant Stability Quotient, ISQ). No exceptions.

---

## THE FOUR RULES (do not violate)

These rules prevent hallucination and keep every claim traceable.

1. **No web search.** Never use `WebSearch` or `WebFetch` to fill gaps. Every answer must be grounded in papers we actually have.
2. **Answer from the wiki first.** Use `sources/` and `wiki/` as the only sources of truth.
3. **If the wiki is insufficient, re-read the PDF.** Go to `papers/{stem}.pdf` and extract more detail with `pypdf`. Then update the wiki.
4. **If the wiki has no paper on the topic, say so.** Tell the user *"I don't have a paper on this — please give me the PDF."* Do not improvise.

These rules apply to **every** response, including overview pages.

---

## Repository Structure

The repo has two layers: **KNOWLEDGE** (papers/sources/wiki — the substrate, reusable knowledge atoms) and **OPERATIONS** (agenda/slides/interactives/peer-review/note-meeting/scripts/logs — where knowledge is converted into outputs).

```
llm-wiki/
├── CLAUDE.md                   # This file — agent行動 rules
├── SOP.md                      # Human-facing operating procedure
├── index.md                    # Page catalog
│
│ ── KNOWLEDGE (the substrate) ──
├── papers/                     # Original PDFs (cp, never symlink)
│   └── {author}-{year}-{title-5-words}.pdf
├── sources/                    # PDF summaries (English)
│   └── {author}-{year}-{title-5-words}.md
├── wiki/                       # Wiki pages (English)
│   ├── implants/               # 임플란트
│   ├── endodontics/            # 근관치료
│   ├── periodontics/           # 치주치료
│   ├── dental-materials/       # 치과재료 (general)
│   ├── glass-ionomer/          # 글래스아이오노머 (GIC/RMGIC/HVGIC)
│   ├── resin/                  # 레진
│   ├── resin-bonding/          # 레진접착
│   ├── sinus-lift/             # 상악동거상술
│   ├── immediate-implant/      # 즉시식립
│   ├── prosthetic-materials/   # 보철재료
│   ├── inlay/                  # 인레이
│   ├── radiology/              # 방사선학
│   ├── oral-medicine/          # 구강내과
│   ├── botulinum-toxin/        # 보툴리눔 독소
│   ├── orthodontics/           # 교정학
│   ├── tmj/                    # 턱관절·악관절장애
│   ├── caries/                 # 우식
│   ├── cracked-tooth/          # 균열치 증후군
│   ├── professional-wellbeing/ # 치과의사 직업적 웰빙
│   ├── dentin-hypersensitivity/ # 상아질 과민증
│   ├── practice-management/    # 치과경영
│   └── overviews/              # Synthesis pages (cross-category)
│
│ ── OPERATIONS (knowledge → output) ──
├── agenda/                     # 작업 명세서 (Goal·Input·Output·Done)
├── interactives/               # HTML 시각화·계산기·의사결정 도구
├── slides/                     # 강의·발표 자료 (wiki가 1차 입력)
├── peer-review/                # 외부 paper 리뷰 (저널 reviewer 의뢰)
├── note-meeting/               # 미팅 기록 (1 미팅 = 1 파일)
├── scripts/                    # 자동화 (ingest watcher, lint)
└── logs/                       # audit 산출 로그
```

## File Naming Convention

All three tiers share the same stem:

```
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces → `-`
- Year is 4 digits
- Example: `jung-2023-immediate-implant-placement-sinus.pdf`

## Categories

| Category folder | Korean | Includes |
|---|---|---|
| `implants` | 임플란트 | Implant design, bone type, survival, failure risk, MBL, soft tissue |
| `implants/isq` | 임플란트·ISQ | ISQ/RFA measurement, stability dip, loading decision thresholds |
| `implants/surface` | 임플란트·표면처리 | SLA, CA, UV surface technology, osseointegration |
| `implants/vertical-ridge-augmentation` | 임플란트·수직골증대 | Vertical ridge augmentation, Ti-mesh / PTFE mesh GBR, vertical bone gain, mesh exposure, customized CAD/CAM mesh |
| `bone-regeneration` | 골재생 | GBR, ridge preservation, socket management, peri-implantitis GBR |
| `immediate-implant` | 즉시식립 | Immediate implant placement protocols, outcomes, esthetic risk |
| `sinus-lift/lateral` | 상악동거상술·측방 | Lateral window approach, membrane, grafting materials |
| `sinus-lift/transcrestal` | 상악동거상술·경치조골 | Transcrestal (osteotome/balloon/osseodensification) approaches |
| `endodontics/eal` | 근관치료·근관장측정 | EAL accuracy, working length, apex locator devices |
| `endodontics/irrigation` | 근관치료·세정 | Irrigant activation (PUI, ANP, sonic), NaOCl protocols |
| `endodontics/anatomy` | 근관치료·해부 | Canal morphology, access cavity, MB2, CBCT-guided access |
| `periodontics` | 치주치료 | Periodontal disease, regeneration, SPT |
| `dental-materials` | 치과재료 | Impression materials, zirconia, ceramics |
| `glass-ionomer` | 글래스아이오노머 | GIC / RMGIC / HVGIC: composition, restorative & preventive use, longevity, bioactivity/remineralization, biocompatibility, fissure sealant |
| `digital-workflow` | 디지털워크플로우 | IOS accuracy, CBCT, CAD/CAM, guided surgery |
| `resin` | 레진 | Composite resin, polymerization, shrinkage |
| `resin-bonding` | 레진접착 | Adhesive systems, bonding mechanisms, dentin adhesion |
| `prosthetic-materials` | 보철재료 | Screw vs cement retention, zirconia crowns, CAD/CAM prosthetics |
| `drug` | 전신질환·약물 | Systemic disease management, drug interactions, MRONJ, anticoagulants |
| `pdrn` | PDRN(폴리뉴클레오티드) | Polydeoxyribonucleotide (PDRN) biology, bone/soft-tissue regeneration with PDRN, peri-implant/sinus/extraction socket adjunct, A2A receptor mechanism |
| `oral-surgery` | 구강외과 | Extractions, nerve injuries, surgical complications |
| `suture-wound-closure` | 봉합·창상폐쇄 | Suture techniques/patterns & biomechanics, primary vs secondary closure, sutureless surgery, tissue adhesives, flap design for tension-free primary closure (PASS, periosteal releasing, advancement flaps) |
| `occlusion` | 교합 | Occlusal analysis (digital/T-Scan vs articulating paper), implant occlusion, occlusal overload, occlusal scheme/adjustment |
| `geriatric-dentistry` | 노년치의학 | Oral frailty, xerostomia/hyposalivation, root caries in elderly, professionally applied fluoride, polypharmacy oral effects |
| `local-anesthesia` | 국소마취·진정 | LA agents (articaine/lidocaine/mepivacaine), IANB/buccal infiltration, N2O & procedural sedation, injection landmarks |
| `inlay` | 인레이 | Inlay/onlay restorations, ceramic inlays |
| `evidence-appraisal` | 근거평가·통계방법론 | EBM/EBD critical appraisal, SR/MA methodology, biostatistics (p-value/CI/OR/RR/HR/NNT), common mistakes |
| `bone-biology` | 골생물학 | Molecular/cellular bone biology — osteoclast/osteoblast signaling (SIK, PTHrP, RANKL), residual ridge resorption pathology, basic socket healing biology |
| `behavioral-dentistry/motivational-interviewing` | 행동치의학·동기면담 | Motivational interviewing (MI/brief MI) efficacy & uptake, behavior-change counseling, oral-health/general-health promotion |
| `behavioral-dentistry/communication-relationship` | 행동치의학·커뮤니케이션 | Dentist–patient communication skills/training, dentist–patient relationship determinants, shared decision-making, patient expectation management |
| `behavioral-dentistry/patient-reported-outcomes` | 행동치의학·환자보고결과 | PRO/PROM/PREM, OHRQoL, patient satisfaction/experience, behavioral assessment of the patient |
| `behavioral-dentistry/dental-anxiety` | 행동치의학·치과불안 | Dental anxiety/fear/phobia assessment & management (pediatric + adult), behavior-rating scales, non-pharmacological strategies |
| `radiology` | 방사선학 | CBCT diagnostic performance, radiation dose/collimation, panoramic, cephalometric, CBCT-guided endodontics/implant, shielding protocols |
| `oral-medicine` | 구강내과 | Oral mucosal diseases — leukoplakia, oral lichen planus, burning mouth syndrome (BMS), recurrent aphthous stomatitis (RAS), malignant transformation risk |
| `orofacial-pain` | 구강안면통증·통증 신경기전 | Nociception/neuropathic-pain molecular mechanisms underlying orofacial pain & BMS — chloride homeostasis (NKCC1/KCC2), GABA-A/glycine disinhibition, peripheral nociceptor ion channels (anoctamin/TMEM16, TRPV1, Nav), T-type Ca²⁺ channels, neurosteroid modulation. (BMS clinical/diagnostic papers → `oral-medicine`) |
| `botulinum-toxin` | 보툴리눔 독소 | Botulinum toxin type A (BoNT-A) for bruxism, TMD/myogenous pain, gummy smile, lip aesthetics; injection landmarks, dosing, longevity |
| `orthodontics` | 교정학 | Orthodontic miniscrews (TADs) — stability, failure risk, reuse; periodontal-orthodontic interactions; force biology |
| `tmj` | 턱관절·악관절장애 | TMD diagnosis & management — arthrocentesis, splint therapy, pharmacotherapy, chronic pain, TMJ osteoarthritis, sleep bruxism |
| `sinus-lift/pseudocyst` | 상악동거상술·슈도시스트 | Antral pseudocyst / mucous retention cyst management in sinus lift context — retention vs removal, outcomes, implant impact |
| `endodontics/vpt` | 근관치료·생활치수요법 | Vital pulp therapy (VPT) — direct pulp capping, partial/full pulpotomy; MTA/Biodentine agents; success criteria; decision thresholds for mature/immature teeth |
| `caries` | 우식 | Caries detection, risk assessment, minimal intervention dentistry, fluoride, fissure sealants, ICDAS, stepwise/selective excavation |
| `cracked-tooth` | 균열치 증후군 | Cracked tooth syndrome — classification (Ellis/Baird), diagnosis, prognosis, restoration design, FEA stress analysis |
| `implants/peri-implantitis` | 임플란트·주위염 | Peri-implantitis prevalence, risk factors, non-surgical/surgical treatment, surface decontamination, GBR for peri-implant defects |
| `endodontics/shaping` | 근관치료·근관성형 | Rotary/reciprocating NiTi instruments, shaping strategies (crown-down, single-file), file separation, canal transportation, apical patency |
| `professional-wellbeing` | 치과의사 직업적 웰빙 | Burnout prevalence, risk factors, protective factors, wellbeing interventions among dental professionals; COVID impact |
| `endodontics/regenerative` | 근관치료·재생근관치료 | Regenerative endodontic procedures (REP) — biologic basis, blood clot scaffold, MTA barrier, outcomes in open-apex teeth |
| `dentin-hypersensitivity` | 상아질 과민증 | Dentinal hypersensitivity — etiology (hydrodynamic theory), in-office and at-home management, desensitizing agents |
| `practice-management` | 치과경영 | Dental practice management — legal/regulatory decisions (헌법재판소 등), operational policies, clinic administration |
| `implants/versah-protocols` | 임플란트·Versah 프로토콜 | Versah osseodensification osteotomy — indications, ISQ outcomes, bone density effects, vs conventional drilling |
| `oral-microbiology` | 구강미생물학 | Oral microbiome ecology & dysbiosis, dental/biofilm matrix (EPS, glucans, eDNA, matrixome), keystone pathogens (P. gingivalis, F. nucleatum), polymicrobial synergy & dysbiosis (PSD) model, Streptococcus/Candida interactions, microbiome–systemic/cancer links |
| `dental-erosion` | 치아침식 | Erosive tooth wear (ETW) — etiology (intrinsic/extrinsic acids, dietary soft drinks/citrus), enamel demineralization/mineral loss chemistry, erosion measurement (profilometry), risk factors & prevention |
| `nccl` | 비우식성 치경부 병소 | Noncarious cervical lesions / abfraction — morphology (saucer/V-shape), progression (D/H ratio), prevalence, multifactorial etiology (stress/friction/biocorrosion schema), demineralization pathophysiology, SEM/stereomicroscopic characterization, monitor-vs-restore decision. (NCCL adhesive-restoration RCTs → `resin-bonding`) |
| `food-impaction` | 식편압입·치간이개 | Food impaction & proximal/interproximal contact loss (PCL/ICL) between implant prostheses (or natural teeth) and adjacent teeth — prevalence, risk factors, mesial>distal pattern, time-progression, clinical implications (caries, periodontal), management. (natural-tooth open contact, plunger cusp, marginal-ridge contour included) |
| `overviews` | 종합 | Synthesis pages spanning multiple categories |

Classify by **method/procedure**, not by disease or anatomy.

---

## Adding a New Paper

Say: *"Add this paper to the wiki: /path/to/paper.pdf"*

The agent will do all four steps automatically.

### Step 0 — Pre-ingest gate (dedup + retraction)

Before copying anything, run two checks. Skipping these is how the wiki accumulates duplicate and discredited pages.

1. **DOI / cross-stem duplicate check.** Extract the paper's DOI, then grep `sources/` for it. `orphan-check.py` only enforces stem-level 1:1 — it does NOT catch the same paper ingested under a different stem (e.g. `gaspar-2022-...` vs `gaspar-2025-...`, `materials-14-...` vs `inchingolo-...-sr-ma`). If the DOI already exists, do NOT create a second page — update the existing one instead. `scripts/doi-duplicate-check.py` (daily-audit signal) reports same-DOI/different-stem groups after the fact.

   ```bash
   grep -rl "10.xxxx/the-doi" sources/    # 결과 있으면 중복 → 기존 페이지 갱신, 신규 ingest 금지
   ```

2. **Retraction check.** Do NOT ingest a retracted article, retraction notice, erratum-only page, or a bare PubMed/publisher listing page as a knowledge page — it propagates discredited claims and violates the living-document/critical-appraisal principle. If a retracted paper must be recorded, make a single explicit "RETRACTED — do not cite" stub, never a normal wiki page. Delete retraction/erratum notice PDFs (they are not ingestable papers).

### Step 1 — Copy PDF to `papers/` and extract text

```bash
cp /path/to/paper.pdf /Users/oracleneo/llm-wiki/papers/{stem}.pdf

python3 -c "
import pypdf, sys
reader = pypdf.PdfReader(sys.argv[1])
text = ''
for page in reader.pages[:15]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print(text[:12000])
" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```

### Step 2 — Write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: [category-folder]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## Why Ingested
## One-line Summary
## 한줄요약
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

**`## Why Ingested` is MANDATORY for sources ingested on/after 2026-05-27** (enforced by `scripts/ingest-rationale-lint.py`). Pre-cutoff sources are grandfathered (no backfill).

Required content of the section:
- 1–2 sentences explaining *why* this paper was ingested now (gap, conflict, new evidence, requested by user, related to current clinical case, etc.)
- At least one `[[wiki/category/stem]]` wikilink to an existing wiki page that this paper reinforces, contradicts, or extends.

Example:
```
## Why Ingested

기존 [[implants/isq/andersson-2019-rfa-factors-5year-neoss-survival]]의 ISQ ≥65 threshold가 5Y-PSZ implant에 적용되는지 의문. 본 RCT (Konuklu 2026)는 5개 osteotomy protocol을 직접 비교해 임계값 보강 근거로 활용.
```

Rationale: a 2-minute cost at ingest turns later overview synthesis from a cold start into a warm assembly. See `agenda/2026-05-26_synthesis-enforcement-setup.md` for the design.

### Step 3 — Write `wiki/{category}/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
date: YYYY-MM-DD       # publication date; fall back to ingest date (YYYY-MM-DD) when unknown
doi: DOI
source: {stem}.md
category: [category-folder]
confidence: sr+ma      # see vocabulary below
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## One-line Summary
(English one-liner: study type, n, key finding)

## 한줄요약
(Korean one-liner: study type, n, key finding in plain Korean)

## Summary
## Key Contributions
## Methodology
## Results
## Related Papers
- [[category/page]] — relationship
```

### `confidence:` vocabulary

Pick the **single best label** for the study type. Ordered roughly from highest to lowest evidence weight:

| Value | Applies to |
|---|---|
| `sr+ma` | Systematic review + meta-analysis (incl. umbrella review) |
| `sr` | Systematic review without meta-analysis |
| `rct` | Randomized controlled trial |
| `prospective` | Prospective cohort / prospective case series |
| `retrospective` | Retrospective cohort / chart review |
| `cross-sectional` | Cross-sectional study, survey |
| `case-report` | Case report or small case series (n < 10) |
| `in-vivo` | In vivo clinical/animal experimental study not covered above |
| `animal` | Animal-only experimental study (dog, rat, etc.) |
| `in-vitro` | Bench / laboratory study |
| `narrative-review` | Narrative review, perspective, expert commentary |
| `consensus` | Consensus statement / position paper |
| `synthesis` | Multi-paper synthesis page (wiki overviews); not external study type |

### `date:` field

- Publication date in `YYYY-MM-DD` format when known (use journal publication or e-pub date).
- `YYYY-01-01` when only year is known.
- If neither is recoverable from the paper, fall back to ingestion date (`YYYY-MM-DD` of when added to wiki).

### `superseded_by:` — living-document supersession (optional field)

The wiki is a living document: a paper page is not an ingest-time snapshot, it gets updated by later evidence. When a newer paper we hold **overturns the clinical bottom line** of an older page we hold, mark the *older* page. This converts the manual prose-update habit into a machine-checkable signal (`scripts/supersession-audit.py`).

**This is a clinical judgment, not a mechanical year comparison.** Newer ≠ superior — a 2026 narrative-review does NOT supersede a 2022 SR+MA. Set the field only when the newer page genuinely beats the older one on evidence weight or currency, and only between pages we actually hold.

**Forward-only trigger (no backfill needed).** At ingest of a new page, ask: *"does this overturn an existing page's bottom line?"* If yes, edit the *older* page — add the field + banner. Pre-existing pages are never bulk-scanned (same grandfather logic as `## Why Ingested`).

Two frontmatter fields on the **superseded (older)** page:

```yaml
superseded_by: tisci-2026-isq-it-mbl-survival-sr-ma   # newer stem(s); comma-separated if >1; must exist in wiki/
superseded_scope: full                                # full | partial
```

- `full` — the older page's conclusion is replaced; prefer the newer page for all current decisions.
- `partial` — only part of the page is outdated, or the page retains standalone value (e.g. first-of-kind synthesis, historical anchor). Use this rather than overstating `full`.

Plus a banner callout at the **top of the body** (right after frontmatter, before `## One-line Summary` / `## 한줄요약`). Obsidian and Quartz both render `[!warning]`/`[!note]` callouts natively — no build change:

```markdown
> [!warning] Superseded (full) → [[tisci-2026-isq-it-mbl-survival-sr-ma]]
> 48-study SR+MA (r=0.44, p<0.001) overturns this 12-study NS result. (set 2026-05-31)
```

For `partial`, use `> [!note] Partially superseded → [[newer-stem]]` and state what the page still offers.

**Decay is computed, never stored.** Do NOT add a decay/staleness field — a stored decay value rots (the same reason `overview-thesis-staleness.py` exists). `supersession-audit.py` computes it each run: high-evidence pages (`sr+ma`/`sr`/`rct`) older than 5y and not superseded are flagged as "verify still current" candidates.

Design: `agenda/2026-05-31_supersession-decay-setup.md`.

### `relations:` — typed entity edges (optional field)

`[[wikilinks]]` encode *that* two pages relate; they don't encode *how*. The `## Why Ingested` section already states the relationship in prose ("X를 보강", "Y로 확장", "Z와 대비"). Lifting that into a structured frontmatter block turns overview synthesis from a cold start (re-read every page to infer relationships) into a warm assembly (the typed graph is already there). `superseded_by` is intentionally NOT part of this — it has its own audited field and banner.

Optional block on the **citing (newer) page**, pointing out to the pages it relates to:

```yaml
relations:
  - type: extends
    target: manfredini-2023-polydeoxyribonucleotides-pre-clinical-findings-bone-healing
  - type: reinforces
    target: ku-2025-polydeoxyribonucleotide-pdrn-dentistry-narrative-review
```

Relation vocabulary (5 types; pick the single best per edge):

| `type` | meaning | Why-Ingested 표현 예 |
|---|---|---|
| `extends` | builds on / expands target's scope or depth | "확장", "deep-dive", "적응증 확장" |
| `reinforces` | independently confirms / strengthens target | "보강", "재확인", "일관", "짝을 이룸" |
| `contradicts` | findings conflict with target | "반박", "상충", "대비되는 결과" |
| `refines` | narrows / qualifies target's conclusion | "한정 시나리오 강화", "조건부", "scope 제한" |
| `applies-to` | clinical/methodological application of target | "프로토콜 적용", "한국 임상 contextualization" |

- `target` must be an existing wiki stem (validated by `scripts/relations-audit.py`).
- Forward-only / grandfather: structure relations for **new** pages at ingest; old pages are not bulk-scanned. The audit reports a machine-readable typed-edge export (`logs/{date}_relations-graph.json`) for Quartz/custom rendering — Obsidian's graph view can't distinguish edge types, so the JSON export is where typed-edge value is harvested.

### Step 4 — Update `index.md`

Add a one-line entry under the correct category.

### Step 5 — Refresh search index (qmd)

A new page is invisible to semantic search until qmd re-indexes and embeds it. Run after the wiki/sources files are written:

```bash
export PATH="/opt/homebrew/bin:$PATH"   # brew node(v25+) 강제 — 구 node v18이 앞서면 ABI 불일치로 qmd 깨짐
cd /Users/oracleneo/llm-wiki
qmd update   # 파일시스템 재스캔 (신규/변경/삭제 반영)
qmd embed    # 신규 문서만 임베딩 (incremental — 1~2편이면 수 초). 전체 재임베딩(-f)은 ~2.5h이므로 금지
```

The MCP daemon picks up new vectors automatically — no restart needed.

---

## PDF Management Rules

- **Always copy, never symlink.** `cp` from Downloads or external into `papers/`.
- `pdf_path` always points inside `/Users/oracleneo/llm-wiki/papers/`. Never use `~/Downloads/`.
- `pdf_filename` must match `basename(pdf_path)`.
- **1:1 matching enforced.** Every PDF in `papers/` must have a matching `sources/{stem}.md`. After any ingest or rename operation, run:
  ```python
  pdfs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('papers/') if f.endswith('.pdf')]}
  srcs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('sources/') if f.endswith('.md')]}
  orphan_pdfs = pdfs - srcs   # → delete these
  orphan_srcs = srcs - pdfs   # → warn (missing PDF)
  ```
  Delete all `orphan_pdfs` immediately. Pre-rename originals and duplicate `(1)` copies count as orphans and must be deleted.

## OPERATIONS — Routing & Cross-link Rules

KNOWLEDGE is the substrate; OPERATIONS is where it gets converted into outputs (slides, calculators, review reports, meeting decisions). Without these rules every output drifts away from its source wiki page.

### 1. Routing — 어디에 만드는가

When creating any new artifact, ask in order:

1. **재사용되는 지식인가?** → `wiki/{category}/` (단일 paper) or `wiki/overviews/` (cross-paper synthesis)
2. **시간·이벤트 기록인가?** → `note-meeting/`
3. **외부 deliverable인가? (슬라이드·인터랙티브·peer review)** → 해당 OPERATIONS 폴더
4. **외부 deliverable의 작업 명세인가?** → `agenda/`

**Hard rule**: `slides/`, `interactives/`, `peer-review/` 산출물은 반드시 `agenda/` 파일이 선행되어야 한다. agenda 없는 산출물은 출처·done 기준 추적이 끊긴다.

### 2. File Naming — OPERATIONS

```
agenda/YYYY-MM-DD_<kebab-case-topic>.md
interactives/YYYY-MM-DD_<kebab-case-topic>.html
slides/YYYY-MM-DD_<event-or-audience>_<topic>.md
peer-review/YYYY-MM_<journal-code>_<topic>.md
note-meeting/YYYY-MM-DD_<meeting-type>.md
```

날짜 prefix는 정렬·검색을 위함. `_template.md` 같은 시스템 파일은 날짜 prefix 면제.

### 3. Frontmatter Cross-link — OPERATIONS 파일 전 필수

```yaml
---
title: "..."
type: agenda | interactive | slides | peer-review | meeting
date: YYYY-MM-DD
status: draft | in-progress | review | done | archived
# 아래 3개 중 최소 하나는 비어있지 않아야 함
source_wiki:                              # 이 산출물의 근거가 된 wiki 페이지들
  - wiki/<category>/<stem>.md
agenda: agenda/<date>_<topic>.md          # slides/interactives/peer-review 필수
output_wiki:                              # 이 산출물이 갱신·생성한 wiki 페이지 (meeting에서 자주 발생)
  - wiki/<category>/<stem>.md
---
```

`source_wiki` · `agenda` · `output_wiki` 세 필드가 모두 비어있는 OPERATIONS 파일은 **orphan**으로 간주하고 lint에서 경고한다.

### 4. agenda Workflow

새 작업은 agenda 파일 1개로 시작:

```bash
cp agenda/_template.md agenda/$(date +%Y-%m-%d)_<topic>.md
```

agenda는 Goal·Input·Output·Done이 박힌 단일 명세서. 진행되며 status 갱신 (`draft` → `in-progress` → `review` → `done` → `archived`).

agenda에서 파생된 산출물(slides·interactive·overview)은 자신의 frontmatter에 `agenda:` 백링크를, 그리고 agenda 파일의 `# Output` 섹션에 산출물 경로를 양쪽으로 박는다.

### 5. note-meeting Workflow

미팅 1회 = 파일 1개. 결정 사항(decisions)이 wiki SOP나 임상 프로토콜에 반영되어야 하는 경우:

- meeting note frontmatter의 `output_wiki:` 에 갱신될 wiki 페이지 경로
- followup이 필요하면 `followup_agenda:` 에 신설할 agenda 파일 경로 (그리고 실제로 agenda 신설)

미팅 → agenda → 산출물의 chain이 끊기면 미팅은 메모로만 남고 클리닉 SOP에 반영이 안 된다.

---

## Knowledge Compounding

The most valuable pages are `wiki/overviews/` pages that synthesize across papers. After a good Q&A session, say:

> *"Save this as an overview page in wiki/overviews/"*

Each session should produce 5–15 new or updated wiki pages.

## Daily Audit

A single entry-point runs all 12 audits and writes their logs to `logs/`:

```bash
python3 scripts/daily-audit.py
```

The 12 audits — 3 classic + 1 rationale (errors block) + 8 signals:

| Audit | Type | Purpose |
|---|---|---|
| `lint.py` | error | wiki frontmatter required fields |
| `operations-lint.py` | error | OPS files (agenda/slides/interactives) cross-link chain |
| `orphan-check.py` | error | PDFs ↔ sources 1:1 matching |
| `synthesis-backlog.py` | signal | sources/ not referenced by any overview, stale ≥30d |
| `ingest-rationale-lint.py` | error (post-cutoff only) | `## Why Ingested` on sources ingested ≥ 2026-05-27 |
| `category-overflow.py` | signal | wiki categories with ≥5 unsynthesized papers → overview candidates |
| `overview-thesis-staleness.py` | signal | overview의 git log를 wikilink-only vs thesis edit으로 분류해 진짜 stale overview 식별 (mtime은 wikilink-only ingest로 갱신돼 부정확) |
| `overview-coverage-lint.py` | signal | overview 본문 cov% (linked paper 중 본문 author·year로 인용된 비율) — 낮으면 thesis 분기·표·결정 트리에 paper 반영 안 됨 |
| `doi-duplicate-check.py` | signal | 동일 DOI·다른 stem 검출 + 제목 정규화 fallback(한쪽 DOI 비거나 불일치라 DOI로 못 잡는 동일논문) — orphan-check가 못 잡는 cross-stem 중복 가시화 |
| `supersession-audit.py` | signal | `superseded_by` 깨진 링크 + 필드↔본문 배너 sync + decay 후보(sr+ma/sr/rct 중 5년↑ 미대체, 카테고리·중심성 집계) — living-document 갱신을 신호화 |
| `relations-audit.py` | signal | `relations:` typed edge target 실존·vocab 검증 + 타입 분포 + typed-edge JSON export(Quartz/custom 렌더용) |
| `link-integrity.py` | signal | 본문 `[[wikilink]]` 깨짐 + index.md 양방향 커버리지 (Astro-Han lint 개념 차용) |

Signals never block. They're a mirror — the principle is that ingest pressure self-corrects via visibility, not via gates (which trigger burnout/avoidance in clinical workflows).

Run daily (manual or cron). The three key compounding metrics over time:
- **synthesis-backlog %**: should trend up (more sources getting linked from overviews).
- **category-overflow count**: should trend down as overviews get written.
- **thesis-staleness warn/info**: should stay low — overview 본문이 정기적으로 refresh되는지 보는 signal.

Design rationale: see `agenda/2026-05-26_synthesis-enforcement-setup.md`.

## Searching the Wiki (QMD)

At ~900 pages plain `grep` starts missing cross-category overview matches, so the wiki uses **QMD** ([tobi/qmd](https://github.com/tobi/qmd)) — an on-device hybrid search engine (BM25 + vector + LLM re-ranking), all local, no cloud.

**QMD does NOT violate Rule #1.** It is local-first: it indexes and searches only the markdown files in this repo (`~/.cache/qmd/index.sqlite`), never the web. It *reinforces* Rule #1 by making local retrieval strong enough that web search is never tempting. QMD is a better `grep`, not a `WebSearch`.

Setup (one-time, run on the Mac): `bash scripts/setup-qmd.sh`. Embedding model is Qwen3 multilingual (CJK/Korean queries supported). MCP runs as an HTTP daemon at `localhost:8181`, exposed to Claude Code as the `qmd` MCP server.

Collections indexed: `wiki/`, `sources/`, `agenda/`, `note-meeting/` (markdown only; `papers/` PDFs are not indexed by QMD).

Search precedence when answering:

1. **QMD `query`** (hybrid, best quality) for concept/synthesis questions — e.g. "ISQ loading threshold across osteotomy protocols".
2. **QMD `search`** (BM25) for exact terms — author names, device names, specific values.
3. Fall back to `grep` / `index.md` only if the QMD daemon is down.

After every ingest (or daily), refresh the index so new pages are searchable:

```bash
qmd update && qmd embed     # re-scan + embed new docs only
```

This pairs cleanly with the daily audit — run it alongside `scripts/daily-audit.py`.

## Browsing with Obsidian

Install [Obsidian](https://obsidian.md/) (free) and open `/Users/oracleneo/llm-wiki` as a Vault. You get graph view, `[[wikilinks]]` navigation, and full-text search. Obsidian only reads files — it does not interfere with agent edits. QMD (search) and Obsidian (browse) layer cleanly: both only read files.

---

## Design Principles

- **3-tier**: Raw PDF (immutable) → sources/*.md → wiki/**/*.md
- **English only** in wiki content (RAG-friendly; Korean conversation is fine)
- **Obsidian compatible**: `[[wikilinks]]`, plain markdown
- **No web search**: rule #1 above

When in doubt, follow rule #1.
