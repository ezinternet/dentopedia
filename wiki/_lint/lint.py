#!/usr/bin/env python3
"""
LLM Wiki Structural Lint
- Wiki 정합성 16개 체크 항목 실행
- v2 (2026-05-22): source field .md suffix 자동, N/A/unknown null 동치,
                   wikilink relative path 정확한 resolution,
                   synthesis confidence 추가, navigation stub 면제
"""
import os
import re
import sys
import json
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

WIKI = os.path.join(ROOT, 'wiki')
SRCS = os.path.join(ROOT, 'sources')
PAPERS = os.path.join(ROOT, 'papers')
INDEX = os.path.join(ROOT, 'index.md')

CONFIDENCE_VOCAB = {
    'sr+ma', 'sr', 'rct', 'prospective', 'retrospective', 'cross-sectional',
    'case-report', 'in-vivo', 'animal', 'in-vitro', 'narrative-review',
    'consensus', 'synthesis'
}
REQUIRED_FIELDS_PAPER = [
    'title', 'authors', 'year', 'date', 'source', 'category',
    'confidence'
]
# 아티팩트 필드: PDF 논문 vs PubMed-text 논문(PMC 전문을 .txt로 보관)
PDF_FIELDS = ['pdf_path', 'pdf_filename']
TEXT_FIELDS = ['text_path', 'text_filename']
REQUIRED_FIELDS_OVERVIEW = [
    'title', 'authors', 'year', 'date', 'category', 'confidence'
]
NULL_VALUES = {'', 'null', 'None', 'N/A', 'unknown', 'n/a', 'NA'}

WIKILINK_RE = re.compile(r'\[\[([^\]\|#]+?)(?:#[^\]]+)?(?:\|[^\]]+)?\]\]')

def parse_fm(text):
    if not text.startswith('---'):
        return None
    end = text.find('\n---', 4)
    if end < 0:
        return None
    fm = text[4:end]
    d = {}
    for line in fm.split('\n'):
        if ':' in line and not line.startswith(' ') and not line.startswith('-'):
            k, _, v = line.partition(':')
            d[k.strip()] = v.strip().strip('"').strip("'")
    return d

def is_null(v):
    return v is None or v in NULL_VALUES

def normalize_source(field):
    """source field 'foo' or 'foo.md' or 'synthesis' → expected sources/ filename or None for synthesis."""
    if not field or field in NULL_VALUES or field == 'synthesis':
        return None
    if field.endswith('.md'):
        return field
    return field + '.md'

def is_navigation_stub(rel_path):
    """wiki/index.md type navigation stubs exempt from paper-field checks."""
    return os.path.basename(rel_path) == 'index.md'

def lint():
    if not os.path.isdir(WIKI):
        print(f"ERROR: {WIKI} not found"); sys.exit(1)

    wiki_files = []
    for root, dirs, files in os.walk(WIKI):
        if '_lint' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                wiki_files.append(os.path.join(root, f))

    src_files = [f for f in os.listdir(SRCS) if f.endswith('.md')]
    pdf_files = [f for f in os.listdir(PAPERS) if f.endswith('.pdf')]
    txt_files = [f for f in os.listdir(PAPERS) if f.endswith('.txt')]  # PubMed-text 아티팩트

    with open(INDEX) as fh:
        index_content = fh.read()
    indexed_links = set(WIKILINK_RE.findall(index_content))

    # wiki_link_set: set of stems available via wiki/{cat}/{stem} or wiki/{stem}
    wiki_link_set = set()
    for wp in wiki_files:
        rel = os.path.relpath(wp, WIKI)[:-3].replace('\\', '/')
        wiki_link_set.add(rel)
        # also bare stem (last segment) - some links use bare stem within same category
        wiki_link_set.add(os.path.basename(rel))

    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P = [[] for _ in range(16)]

    # 아티팩트 = PDF ∪ TXT(PubMed-text). orphan 판정을 두 형식 모두로 확장.
    artifact_stems = {os.path.splitext(f)[0] for f in pdf_files} | {os.path.splitext(f)[0] for f in txt_files}
    src_stems = {os.path.splitext(f)[0] for f in src_files}
    H[:] = sorted(artifact_stems - src_stems)
    I[:] = sorted(src_stems - artifact_stems)

    for root, dirs, files in os.walk(ROOT):
        if any(skip in root for skip in ['/.git', '/.obsidian', '/_lint']):
            continue
        for f in files:
            if f.endswith('.bak') or f.endswith('.bak.md') or f.endswith('~'):
                M.append(os.path.relpath(os.path.join(root, f), ROOT))

    title_map = defaultdict(list)
    doi_map = defaultdict(list)

    for wp in wiki_files:
        rel = os.path.relpath(wp, WIKI)
        stem_with_dir = rel[:-3]
        cat = stem_with_dir.replace('\\', '/').split('/')[0]
        rel_norm = stem_with_dir.replace('\\', '/')
        wp_rel = os.path.relpath(wp, ROOT)

        with open(wp) as fh:
            text = fh.read()

        fm = parse_fm(text)
        if fm is None:
            L.append(wp_rel)
            continue

        # Field requirements depend on type
        is_overview = (cat == 'overviews')
        is_nav = is_navigation_stub(rel)

        if is_nav:
            req = ['title']  # navigation stubs minimal
        elif is_overview:
            req = REQUIRED_FIELDS_OVERVIEW
        else:
            is_pubmed_text = fm.get('source_collection', '').strip() == 'pubmed-text'
            req = REQUIRED_FIELDS_PAPER + (TEXT_FIELDS if is_pubmed_text else PDF_FIELDS)

        missing = [k for k in req if k not in fm or is_null(fm.get(k, ''))]
        if missing:
            C.append((wp_rel, missing))

        # 한줄요약: papers + overviews require, nav stubs require too (we kept ours)
        if '## 한줄요약' not in text:
            D.append(wp_rel)

        # confidence vocab
        conf = fm.get('confidence', '').strip()
        if conf and not is_null(conf) and conf not in CONFIDENCE_VOCAB:
            K.append((wp_rel, conf))

        # 아티팩트 path / filename (PDF 또는 PubMed-text의 .txt)
        if not is_overview and not is_nav:
            is_pubmed_text = fm.get('source_collection', '').strip() == 'pubmed-text'
            if is_pubmed_text:
                pp = fm.get('text_path', ''); pn = fm.get('text_filename', '')
            else:
                pp = fm.get('pdf_path', ''); pn = fm.get('pdf_filename', '')
            if pp and pn and not is_null(pp) and not is_null(pn):
                if os.path.basename(pp) != pn:
                    J.append((wp_rel, pp, pn))

            # F: sources file
            src_field = normalize_source(fm.get('source', ''))
            if src_field is not None:
                if not os.path.exists(os.path.join(SRCS, src_field)):
                    F.append((wp_rel, src_field))

            # G: papers file (PDF 또는 TXT 아티팩트)
            if pn and not is_null(pn):
                if not os.path.exists(os.path.join(PAPERS, pn)):
                    G.append((wp_rel, pn))

        # title dup
        t = fm.get('title', '').strip()
        if t and not is_null(t):
            title_map[t].append(wp_rel)

        # doi
        doi = fm.get('doi', '').strip()
        if doi and not is_null(doi):
            doi_map[doi].append(wp_rel)
            # incomplete DOI pattern
            if not re.match(r'^10\.\d{4,9}/[\w\.\-_;()/:]+$', doi):
                P.append((wp_rel, doi))

        # E: wikilinks resolution
        for link in WIKILINK_RE.findall(text):
            link_norm = link.replace('.md', '').strip()
            # external link forms to skip
            if link_norm.startswith(('feedback_', 'user_', 'project_', 'reference_')):
                continue
            # bare category-only links (ends with / or no slash but a known category)
            if link_norm.endswith('/'):
                continue
            # full path form
            if '/' in link_norm:
                candidate = os.path.join(WIKI, link_norm + '.md')
                if os.path.exists(candidate):
                    continue
                # also try without parent dirs (some links use full slug w/o subdir)
                if link_norm in wiki_link_set:
                    continue
                E.append((wp_rel, link))
            else:
                # same-category bare link
                same_cat = os.path.join(WIKI, cat, link_norm + '.md')
                if os.path.exists(same_cat):
                    continue
                # try without category
                if link_norm in wiki_link_set:
                    continue
                # try anywhere in wiki
                found = False
                for wk in wiki_link_set:
                    if wk.endswith('/' + link_norm) or wk == link_norm:
                        found = True; break
                if found:
                    continue
                E.append((wp_rel, link))

        # A: indexed?
        if is_nav:
            pass  # nav stub not required in index
        else:
            if rel_norm not in indexed_links:
                A.append((wp_rel, rel_norm))

    for t, ps in title_map.items():
        if len(ps) > 1:
            N.append((t, ps))
    for d, ps in doi_map.items():
        if len(ps) > 1:
            O.append((d, ps))

    for link in indexed_links:
        link_norm = link.replace('.md', '').strip()
        if link_norm.startswith(('feedback_', 'user_', 'project_')):
            continue
        if link_norm.endswith('/'):
            continue
        candidate = os.path.join(WIKI, link_norm + '.md')
        if not os.path.exists(candidate):
            if link_norm not in wiki_link_set:
                B.append(link_norm)

    return {
        'wiki_count': len(wiki_files),
        'sources_count': len(src_files),
        'pdf_count': len(pdf_files),
        'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H,
        'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P,
    }

def report(r):
    labels = {
        'A': 'wiki 페이지가 index.md에 미등재',
        'B': 'index.md 링크인데 wiki 없음',
        'C': 'frontmatter 필수 필드 누락',
        'D': '한줄요약 누락',
        'E': '깨진 wikilink',
        'F': 'sources/ 파일 누락',
        'G': 'papers/ 파일 누락',
        'H': 'orphan PDF',
        'I': 'orphan source',
        'J': 'pdf_path vs pdf_filename 불일치',
        'K': 'confidence 어휘 위반',
        'L': 'frontmatter 자체 없음',
        'M': '.bak 잔존',
        'N': '중복 title',
        'O': '중복 DOI',
        'P': '불완전 DOI (cosmetic)',
    }
    print(f"Wiki={r['wiki_count']}  Sources={r['sources_count']}  PDFs={r['pdf_count']}")
    print()
    for key in 'ABCDEFGHIJKLMNOP':
        items = r[key]
        flag = '✅' if not items else '⚠️ '
        print(f"[{key}] {labels[key]}: {len(items)} {flag}")

    print()
    for key in 'ABCDEFGHIJKLMNOP':
        items = r[key]
        if items:
            print(f"\n=== [{key}] {labels[key]} ({len(items)}) ===")
            for x in items[:30]:
                print(f"  {x}")
            if len(items) > 30:
                print(f"  ... +{len(items)-30} more")

if __name__ == '__main__':
    r = lint()
    report(r)
    if '--json' in sys.argv:
        with open(os.path.join(os.path.dirname(__file__), 'lint-latest.json'), 'w') as fh:
            json.dump(r, fh, indent=2, default=str)
