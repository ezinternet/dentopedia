#!/usr/bin/env python3
"""
wiki/category-map.md 자동 생성기.

이 스크립트가 카테고리 지도의 **단일 진실원천(SSOT)**이다.
6단계 임상 동선 그룹핑·각 행의 라벨/경로/비고(손으로 쓴 prose)는 아래 STRUCTURE에
박혀 있고, '페이지' 열의 숫자는 빌드 때마다 wiki/{path}/*.md 를 실제로 세서 채운다.
→ 논문을 ingest 하면 폴더 개수가 늘고, 다음 배포에서 지도 숫자가 자동으로 따라온다.

실행: python3 scripts/build-category-map.py   (repo 루트 무관, 스크립트 위치 기준)
출력: wiki/category-map.md  (덮어쓰기, AUTO-GENERATED)

설계 원칙(build-overviews-map.py 와 동일):
- 숫자는 손으로 만지지 않는다 — 빌드가 폴더에서 센다.
- 카테고리를 추가/이동/문구수정하려면 이 파일의 STRUCTURE만 고친다 (.md 직접편집 금지).
- STRUCTURE 에 없는 새 카테고리 폴더가 wiki/ 에 생기면 빌드가 경고를 찍어
  invisible(지도 누락)을 막는다. (overviews-map 의 FALLBACK 버킷과 같은 역할)

배포: .github/workflows/deploy-pages.yml 에서 "Copy wiki/ into quartz/content/" **이전**에
실행해야 한다 (category-map.md 는 Quartz 가 빌드하는 markdown 이므로).
"""

import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT = WIKI / "category-map.md"

# 카테고리 디렉토리가 아닌 시스템/보조 폴더 — 완전성 검사에서 제외.
NON_CATEGORY = {"_lint", "__pycache__"}

# ── SSOT: 6단계 임상 동선 ─────────────────────────────────────────────
# 각 단계 = (제목, 한줄 설명(blockquote), [행...]).
# 각 행 = ([(라벨, 경로), ...], 비고).
#   - 한 행에 (라벨,경로) 가 여러 개면 '페이지' 셀이 "n · m · ..." 로 묶인다
#     (예: 구강내과 49 · 점막염 3 · OPMD 2).
#   - 경로는 wiki/ 기준 상대경로 + 끝 슬래시. 숫자는 그 폴더의 직속 *.md 개수.
STRUCTURE = [
    ("1 · 진단 · 기초 · 근거 (Diagnosis · Foundations · Evidence)",
     "환자를 읽고, 근거의 무게를 판단하는 단계. 병인·병리·영상·구강내과.",
     [
        ([("근거평가·통계방법론 (Evidence Appraisal)", "evidence-appraisal/")], "모든 단계 횡단 — SR/MA·비뚤림·통계"),
        ([("인공지능·기계학습 (AI/ML)", "artificial-intelligence/")], "진단 성능·영상 CNN"),
        ([("방사선학 (Radiology)", "radiology/")], "CBCT·선량·영상기하"),
        ([("구강미생물학 (Oral Microbiology)", "oral-microbiology/")], "dysbiosis·바이오필름 매트릭스"),
        ([("골생물학 (Bone Biology)", "bone-biology/")], "분자·세포 골생물학 (→ 2단계 골재생 기반)"),
        ([("우식 (Caries)", "caries/")], "검출·위험평가·MID·불소"),
        ([("치아침식 (Dental Erosion)", "dental-erosion/")], "산성 탈회 화학"),
        ([("비우식성 치경부병소 (NCCL/Abfraction)", "nccl/")], "형태·병인·monitor-vs-restore"),
        ([("균열치 증후군 (Cracked Tooth)", "cracked-tooth/")], "분류·진단·예후"),
        ([("상아질 과민증 (Dentin Hypersensitivity)", "dentin-hypersensitivity/")], "수역학설·desensitizer"),
        ([("구강내과 (Oral Medicine)", "oral-medicine/"), ("점막염", "oral-medicine/mucositis/"), ("OPMD", "oral-medicine/opmd/")], "점막질환·BMS·악성전환"),
        ([("구강안면통증 (Orofacial Pain)", "orofacial-pain/")], "통증 신경기전 (→ BMS 임상은 구강내과)"),
        ([("악관절장애 (TMJ/TMD)", "tmj/")], "진단·splint·관절강세척"),
        ([("구취 (Halitosis)", "halitosis/")], "VSC·측정·관리"),
     ]),
    ("2 · 경조직 수술 · 골재생 (Hard-Tissue Surgery · Bone Regeneration)",
     "발치·치조골 처리·골/연조직 토대 만들기. 임플란트 식립 *이전*의 외과 단계.",
     [
        ([("구강외과 (Oral Surgery)", "oral-surgery/")], "발치·신경손상·합병증"),
        ([("외상치학 (Dental Trauma)", "dental-trauma/")], "치아탈구·재식·splint·IADT"),
        ([("봉합·창상폐쇄 (Suture / Wound Closure)", "suture-wound-closure/")], "flap design·tension-free 1차폐쇄"),
        ([("골재생 (Bone Regeneration / GBR)", "bone-regeneration/"), ("치조제보존 (ARP)", "bone-regeneration/ridge-preservation/")], "차폐막·이식재·수평/수직 증대"),
        ([("상악동거상술·측방 (Sinus Lift: Lateral)", "sinus-lift/lateral/")], "측방창·막·이식재"),
        ([("상악동거상술·경치조골 (Transcrestal)", "sinus-lift/transcrestal/")], "osteotome·OD·balloon"),
        ([("상악동거상술·슈도시스트 (Pseudocyst)", "sinus-lift/pseudocyst/")], "점액낭종 관리"),
        ([("PDRN (Polydeoxyribonucleotide)", "pdrn/")], "골/연조직 재생 biologic 보조 (→ 3단계 약물과 교차)"),
     ]),
    ("3 · 치주 · 약물 · 전신 (Periodontics · Pharmacology · Systemic)",
     "연조직 건강·전신 관리·임상 약리. 모든 시술을 가능케 하는 의학적 토대.",
     [
        ([("치주치료 (Periodontics)", "periodontics/")], "치주질환·재생·SPT"),
        ([("치간 청소 (Interdental Cleaning)", "interdental-cleaning/")], "치실·치간칫솔·물세정기"),
        ([("국소마취·진정 (Local Anesthesia / Sedation)", "local-anesthesia/")], "articaine·IANB·N₂O"),
        ([("약물·진통소염제 (Analgesics)", "drug/analgesics/")], "NSAID·preemptive"),
        ([("약물·항생제 (Antibiotics)", "drug/antibiotics/")], "처방·예방·stewardship"),
        ([("약물·항응고·지혈 (Anticoagulants)", "drug/anticoagulants/")], "warfarin·DOAC·항혈소판"),
        ([("약물·MRONJ", "drug/mronj/")], "항흡수제·staging"),
        ([("약물·전신질환관리 (Systemic Disease)", "drug/systemic-disease/")], "당뇨·심혈관·약물상호작용"),
     ]),
    ("4 · 보존 · 근관 · 재료 (Conservative · Endodontics · Restorative Materials)",
     "치아를 살리고 채우는 단계. 직접/간접 수복재료 + 근관치료.",
     [
        ([("치과재료 (Dental Materials)", "dental-materials/"), ("지르코니아", "dental-materials/zirconia/")], "일반 수복재 + 지르코니아 재료과학 (→ 5단계 보철과 교차)"),
        ([("레진 (Resin)", "resin/")], "복합레진·중합·수축"),
        ([("레진접착 (Resin Bonding)", "resin-bonding/")], "접착시스템·상아질 접착"),
        ([("글래스아이오노머 (GIC/RMGIC)", "glass-ionomer/")], "조성·bioactivity·sealant"),
        ([("인레이·온레이 (Inlay)", "inlay/")], "간접 수복"),
        ([("포스트앤코어 (Post-and-Core)", "post-and-core/")], "ETT 수복·ferrule"),
        ([("치아미백 (Tooth Whitening)", "tooth-whitening/")], "vital/non-vital bleaching"),
        ([("근관치료 (Endodontics)", "endodontics/")], "일반"),
        ([("근관·해부 (Anatomy)", "endodontics/anatomy/")], "MB2·access·형태"),
        ([("근관·진단 (Diagnosis)", "endodontics/diagnosis/")], "치수·치근단 진단"),
        ([("근관·근관장 (EAL)", "endodontics/eal/")], "apex locator"),
        ([("근관·세정 (Irrigation)", "endodontics/irrigation/")], "PUI·NaOCl·activation"),
        ([("근관·성형 (Shaping)", "endodontics/shaping/")], "NiTi·crown-down"),
        ([("근관·생활치수치료 (VPT)", "endodontics/vpt/")], "직접복수·pulpotomy·MTA"),
        ([("근관·재생근관치료 (REP)", "endodontics/regenerative/")], "open-apex·blood clot"),
        ([("근관·냉플라즈마 (Cold Plasma)", "endodontics/cold-plasma/")], "CAP·E. faecalis"),
        ([("근관·내원횟수 (Visit Protocol)", "endodontics/visit-protocol/")], "single vs multi-visit"),
     ]),
    ("5 · 보철 · 임플란트 (Prosthodontics · Implants)",
     "형태·기능 회복. 고정성/가철성 보철 + 임플란트 식립·로딩.",
     [
        ([("보철재료 (Prosthetic Materials)", "prosthetic-materials/")], "screw vs cement·crown"),
        ([("총의치·가철성보철 (Complete Denture)", "complete-denture/")], "OVD·jaw relation"),
        ([("비니어·라미네이트 (Veneers)", "veneers/")], "ceramic/composite veneer"),
        ([("교합 (Occlusion)", "occlusion/")], "T-Scan·임플란트 교합·overload"),
        ([("식편압입·치간이개 (Food Impaction / PCL)", "food-impaction/")], "proximal contact loss"),
        ([("디지털워크플로우 (Digital Workflow)", "digital-workflow/")], "IOS·CAD/CAM·guided (→ 4·5 전반 횡단)"),
        ([("임플란트 일반 (Implants)", "implants/")], "디자인·생존·실패위험·MBL"),
        ([("임플란트·ISQ", "implants/isq/")], "RFA·안정성·로딩 임계값"),
        ([("임플란트·주위염 (Peri-implantitis)", "implants/peri-implantitis/")], "유병률·비수술/수술·제염"),
        ([("임플란트·연조직 (Soft Tissue)", "implants/soft-tissue/")], "KM 폭·연조직 증대"),
        ([("임플란트·표면처리 (Surface)", "implants/surface/"), ("플라즈마", "implants/surface/plasma/")], "SLA·UV·골유착"),
        ([("임플란트·Versah 프로토콜", "implants/versah-protocols/")], "osseodensification"),
        ([("임플란트·수직골증대 (VRA)", "implants/vertical-ridge-augmentation/")], "Ti-mesh·PTFE GBR"),
        ([("임플란트·비타민 D", "implants/vitamin-d/")], "골유착"),
        ([("즉시식립 (Immediate Implant)", "immediate-implant/")], "type 1·프로토콜·socket healing"),
        ([("즉시식립·심미연조직", "immediate-implant/esthetic-soft-tissue/")], "즉시 임시·CTG·PES"),
        ([("즉시식립·소켓실드 (Socket Shield)", "immediate-implant/socket-shield/")], "PET·root shield"),
     ]),
    ("6 · 교정 · 행동 · 경영 · 특수 (Orthodontics · Behavioral · Practice · Specialty)",
     "교정, 환자 행동·커뮤니케이션, 클리닉 운영, 장비·감염관리·역사.",
     [
        ([("교정학 (Orthodontics)", "orthodontics/")], "미니스크류·TAD·force biology"),
        ([("교정·투명교정 (Clear Aligner)", "orthodontics/clear-aligner/")], "CAT 적응증·한계"),
        ([("교정·근기능/탄성교정 (Myofunctional)", "orthodontics/myofunctional/")], "EF Line·성장기"),
        ([("보툴리눔 독소 (BoNT-A)", "botulinum-toxin/")], "bruxism·TMD·gummy smile"),
        ([("행동·동기면담 (Motivational Interviewing)", "behavioral-dentistry/motivational-interviewing/")], "행동변화 상담"),
        ([("행동·커뮤니케이션 (Communication)", "behavioral-dentistry/communication-relationship/")], "관계·shared decision"),
        ([("행동·환자보고결과 (PRO/PROM)", "behavioral-dentistry/patient-reported-outcomes/")], "OHRQoL·만족도"),
        ([("행동·치과불안 (Dental Anxiety)", "behavioral-dentistry/dental-anxiety/")], "불안·공포 관리"),
        ([("행동·신체이형장애 (BDD)", "behavioral-dentistry/body-dysmorphic-disorder/")], "심미시술 환자선택"),
        ([("직업적 웰빙 (Professional Wellbeing)", "professional-wellbeing/")], "번아웃·보호요인"),
        ([("치과경영 (Practice Management)", "practice-management/")], "법규·운영"),
        ([("환자 민원·컴플레인 (Complaint Management)", "complaint-management/")], "분류·service recovery"),
        ([("노년치의학 (Geriatric Dentistry)", "geriatric-dentistry/")], "oral frailty·xerostomia"),
        ([("치과 핸드피스·엔진 (Dental Handpiece)", "dental-handpiece/")], "aerosol·감염관리"),
        ([("감염관리 (Infection Control)", "infection-control/")], "멸균·소독·교차감염"),
        ([("치과 역사 (Dental History)", "dental-history/")], "인물·milestone"),
     ]),
]

# 단계에 종속되지 않는 횡단 카드(별도 섹션, blockquote 없음).
CROSS_CUTTING = [
    ([("종합 (Overviews)", "overviews/")], "여러 카테고리를 가로지르는 synthesis 페이지 — 단계에 종속되지 않음. 별도 브라우저: `interactives/overviews-map.html`"),
]


def count(path):
    """wiki/{path} 의 직속 *.md 개수 (재귀 아님)."""
    d = WIKI / path.rstrip("/")
    return len(list(d.glob("*.md")))


def render_row(cells, note):
    cat = " · ".join(f"[{label}]({path})" for label, path in cells)
    pages = " · ".join(str(count(path)) for _, path in cells)
    return f"| {cat} | {pages} | {note} |"


def render_table(rows):
    out = ["| 카테고리 | 페이지 | 비고 |", "|---|---|---|"]
    out += [render_row(cells, note) for cells, note in rows]
    return "\n".join(out)


def covered_paths():
    paths = set()
    for _, _, rows in STRUCTURE:
        for cells, _ in rows:
            for _, p in cells:
                paths.add(p.rstrip("/"))
    for cells, _ in CROSS_CUTTING:
        for _, p in cells:
            paths.add(p.rstrip("/"))
    return paths


def find_uncovered():
    """wiki/ 안에서 직속 *.md 를 가지지만 STRUCTURE 에 없는 카테고리 경로."""
    covered = covered_paths()
    uncovered = []
    for d in sorted(WIKI.rglob("*")):
        if not d.is_dir():
            continue
        rel = d.relative_to(WIKI).as_posix()
        if any(part in NON_CATEGORY for part in d.relative_to(WIKI).parts):
            continue
        if not list(d.glob("*.md")):
            continue
        if rel not in covered:
            uncovered.append((rel, len(list(d.glob("*.md")))))
    return uncovered


def main():
    total = sum(count(p) for p in covered_paths())
    stamp = date.today().isoformat()

    parts = [
        '---',
        'title: "Category Map — 임상 동선 카테고리 지도"',
        'tags: [navigation, category-map]',
        'note: "AUTO-GENERATED by scripts/build-category-map.py — 손으로 편집하지 말 것. 페이지 수는 빌드가 폴더에서 센다. 카테고리 추가/문구수정은 스크립트의 STRUCTURE를 고친다."',
        '---',
        '',
        '> [!info] 이 페이지는 **탐색용 지도 레이어**입니다 (폴더 구조 변경 아님)',
        '> 위키의 실제 폴더는 **method/procedure 기준 카테고리**로 그대로 유지됩니다 (`category:` frontmatter · 위키링크 · qmd 임베딩 무손상). 이 지도는 그 위에 **임상 동선(진단→수술→치주·약물→보존·근관→보철·임플란트→교정·특수) 6단계**를 얹어, "지금 이 환자 단계에서 볼 카테고리"를 한눈에 찾게 해줍니다. 한 카테고리가 두 단계에 걸치면 주(主) 동선에 배치하고 비고에 교차점을 적었습니다. **괄호 숫자는 빌드 때마다 폴더에서 자동 집계** (마지막 갱신: ' + stamp + ').',
        '',
        '## One-line Summary',
        '',
        'Navigation layer grouping the method-based wiki categories under a 6-stage clinical workflow (diagnosis → hard-tissue surgery → perio/pharmacology → conservative/endodontics → prosthodontics/implants → orthodontics/specialty); folders are unchanged. Page counts are auto-tallied from each folder at every deploy build.',
        '',
        '## 한줄요약',
        '',
        'method-based 카테고리를 임상 동선 6단계로 그룹핑한 탐색 지도 — 폴더는 그대로 두고 그 위에 얹은 레이어. 페이지 수는 매 배포 빌드에서 폴더로부터 자동 집계. (진단→경조직수술→치주·약물→보존·근관→보철·임플란트→교정·특수)',
        '',
        '---',
        '',
    ]

    for title, desc, rows in STRUCTURE:
        parts.append(f"## {title}")
        parts.append("")
        parts.append(f"> {desc}")
        parts.append("")
        parts.append(render_table(rows))
        parts.append("")

    parts.append("## 교차 — 종합 (Cross-cutting · Synthesis)")
    parts.append("")
    parts.append(render_table(CROSS_CUTTING))
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("> [!note] 분류 축에 대한 메모")
    parts.append('> 위키의 폴더 분류 원칙은 **"질병·해부가 아니라 method/procedure로 분류"**(CLAUDE.md)입니다. 이 지도의 6단계는 그와 **다른 축(임상 동선)**이며 충돌하지 않습니다 — 폴더는 method로 안정적으로 유지되고, 이 레이어는 그 위에서 "환자 진료 흐름"으로 재조망합니다. 이 페이지는 `scripts/build-category-map.py`가 **자동 생성**하며, 페이지 수는 매 배포 빌드에서 폴더로부터 집계됩니다. 카테고리 추가·이동·문구수정은 스크립트의 `STRUCTURE`를 고치세요 (이 .md 직접편집 금지 — 덮어써집니다).')
    parts.append("")

    OUT.write_text("\n".join(parts), encoding="utf-8")

    n_rows = sum(len(rows) for _, _, rows in STRUCTURE) + len(CROSS_CUTTING)
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(STRUCTURE)} stages, {n_rows} rows, {total} pages tallied)")

    uncovered = find_uncovered()
    if uncovered:
        print("\n⚠️  STRUCTURE 에 없는 카테고리 폴더(지도 누락) — STRUCTURE 에 행을 추가하세요:")
        for rel, c in uncovered:
            print(f"     - {rel} ({c})")
    else:
        print("✓ wiki/ 의 모든 카테고리 폴더가 지도에 포함됨")


if __name__ == "__main__":
    main()
