#!/usr/bin/env python3
"""PMID -> PMC full text -> papers/{stem}.txt  (ingest-paper Step 1-T prep).

Usage:  python3 scripts/pubmed-fetch-fulltext.py <PMID> [<PMID> ...]

For each PMID with a PMC record, writes the JATS body as plain text to
papers/{stem}.txt (stem = firstauthor-year-first-5-title-words). PMIDs without a
PMC record get no file (build an abstract-only .txt by hand; see INGEST.md
Step 1-T full_text: false). A manifest of pmid/pmcid/doi/stem/body_len is written
to /tmp/pubmed-stems/manifest.json. Read-only against NCBI (E-utilities, PMC ID
converter); does not touch sources/, wiki/ or git.
"""
import urllib.request, urllib.parse, ssl, json, re, sys, os, time
from xml.etree import ElementTree as ET

CTX = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (llm-wiki)"}
PAPERS = "/Users/oracleneo/llm-wiki/papers"
OUTDIR = "/tmp/pubmed-stems"
EMAIL = "aramid@naver.com"  # NCBI E-utilities contact (same as scripts/fetch-oa.py)


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90, context=CTX).read()


def slugify_title(title, n=5):
    words = re.findall(r"[A-Za-z0-9]+", (title or "").lower())
    return "-".join(words[:n]) or "untitled"


def make_stem(meta):
    author = (meta.get("sortfirstauthor") or "anon").split()
    author = re.sub(r"[^a-z0-9]", "", (author[0].lower() if author else "anon"))
    year = (meta.get("pubdate") or "")[:4] or "0000"
    return f"{author}-{year}-{slugify_title(meta.get('title', ''))}"


def txt(e):
    return "".join(e.itertext())


def jats_to_text(root):
    out = []
    art = root.find('.//article')
    if art is None:
        art = root
    out.append("TITLE: " + txt(art.find('.//article-title')))
    authors = []
    for c in art.findall('.//contrib'):
        sn = c.find('.//surname'); gn = c.find('.//given-names')
        if sn is not None:
            authors.append((txt(sn) + (" " + txt(gn) if gn is not None else "")).strip())
    out.append("AUTHORS: " + ", ".join(authors))
    j = art.find('.//journal-title')
    out.append("JOURNAL: " + (txt(j) if j is not None else ""))
    for k in art.findall('.//article-id'):
        out.append(f"ID[{k.get('pub-id-type')}]: {txt(k)}")
    out.append("")
    ab = art.find('.//abstract')
    if ab is not None:
        out.append("## ABSTRACT")
        for el in ab:
            t = txt(el).strip()
            if t:
                out.append(t)
        out.append("")
    body = art.find('.//body')
    if body is None:
        return "\n".join(out)
    for sec in body.findall('sec'):
        render_sec(sec, out, 2)
    return "\n".join(out)


def render_sec(sec, out, level):
    title = sec.find('title')
    if title is not None and txt(title).strip():
        out.append("#" * level + " " + txt(title).strip())
        out.append("")
    for child in sec:
        tag = child.tag
        if tag == 'title':
            continue
        elif tag == 'sec':
            render_sec(child, out, min(level + 1, 6))
        elif tag in ('p', 'list', 'statement', 'disp-quote', 'boxed-text'):
            t = txt(child).strip()
            if t:
                out.append(t)
                out.append("")
        elif tag == 'table-wrap':
            cap = child.find('caption')
            if cap is not None and txt(cap).strip():
                out.append("[TABLE] " + txt(cap).strip())
            tb = child.find('.//table')
            if tb is not None:
                for row in tb.iter('tr'):
                    cells = [txt(c).strip() for c in row.iter('td')]
                    if cells:
                        out.append(" | ".join(cells))
            out.append("")
        elif tag == 'fig':
            cap = child.find('caption')
            if cap is not None and txt(cap).strip():
                out.append("[FIGURE] " + txt(cap).strip())
                out.append("")


def main(pmids):
    os.makedirs(OUTDIR, exist_ok=True)
    ids = ",".join(pmids)
    res = json.loads(get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={ids}&tool=llm-wiki&email={EMAIL}"))["result"]
    u = f"https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?tool=llm-wiki&email={EMAIL}&ids={ids}&format=json"
    conv = {str(r.get("pmid")): {"pmcid": r.get("pmcid"), "doi": r.get("doi")} for r in json.loads(get(u)).get("records", [])}
    manifest = []
    for pmid in pmids:
        d = res.get(pmid) or {}
        c = conv.get(pmid, {})
        stem = make_stem(d)
        pid = c.get("pmcid")
        body_len = 0
        if pid:
            x = get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pid}&rettype=xml&tool=llm-wiki&email={EMAIL}")
            root = ET.fromstring(x)
            text = jats_to_text(root)
            body = root.find('.//body')
            body_len = len("".join(body.itertext())) if body is not None else 0
            with open(os.path.join(PAPERS, stem + ".txt"), "w") as f:
                f.write(text)
        manifest.append({
            "pmid": pmid, "pmcid": pid, "doi": c.get("doi"), "stem": stem,
            "title": d.get("title", ""), "authors": d.get("sortfirstauthor", ""),
            "journal": d.get("source", ""), "year": (d.get("pubdate") or "")[:4],
            "date": d.get("pubdate", ""), "body_len": body_len,
        })
        print(f"{pmid} {stem}  pmcid={pid} body={body_len}")
        time.sleep(0.4)
    with open(os.path.join(OUTDIR, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)


if __name__ == "__main__":
    main(sys.argv[1:])
