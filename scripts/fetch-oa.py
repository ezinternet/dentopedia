#!/usr/bin/env python3
"""fetch-oa.py — PMID 리스트로 OA 논문 PDF를 papers/에 자동 저장.

흐름: PMID → (NCBI idconv) PMCID·DOI 해석 → (esummary) 서지정보로 stem 생성
  Tier1: PMC OA subset (NCBI oa.fcgi, tgz/pdf)
  Tier2: Unpaywall (DOI → repository/preprint 무료본)
  Tier3: 실패 → '수동 입수 필요'로 리포트 (RISS·기관복사). 불법경로 미사용.

사용: python3 scripts/fetch-oa.py 27684792 32515409 ...
"""
import sys, os, re, json, io, tarfile, ssl
import urllib.request, urllib.parse
from xml.etree import ElementTree as ET

EMAIL = "aramid@naver.com"
TOOL = "llm-wiki"
PAPERS = "/Users/oracleneo/llm-wiki/papers"
UA = {"User-Agent": "Mozilla/5.0 (llm-wiki fetch-oa)"}
CTX = ssl.create_default_context()


def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read()

def slugify_title(title, n=5):
    words = re.findall(r"[A-Za-z0-9]+", (title or "").lower())
    return "-".join(words[:n]) or "untitled"

def make_stem(meta):
    author = (meta.get("sortfirstauthor") or "anon").split()
    author = re.sub(r"[^a-z0-9]", "", (author[0].lower() if author else "anon"))
    year = (meta.get("pubdate") or "")[:4] or "0000"
    return f"{author}-{year}-{slugify_title(meta.get('title',''))}"

def esummary(pmids):
    ids = ",".join(pmids)
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
           f"?db=pubmed&id={ids}&retmode=json&tool={TOOL}&email={EMAIL}")
    return json.loads(http_get(url)).get("result", {})

def idconv(pmids):
    ids = ",".join(pmids)
    url = ("https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
           f"?tool={TOOL}&email={EMAIL}&ids={ids}&format=json")
    data = json.loads(http_get(url))
    return {str(r.get("pmid")): {"pmcid": r.get("pmcid"), "doi": r.get("doi")}
            for r in data.get("records", [])}


def tier1_pmc(pmcid):
    """oa.fcgi → tgz/pdf 링크. PDF bytes 반환 or None."""
    url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmcid}"
    root = ET.fromstring(http_get(url))
    links = {l.get("format"): l.get("href") for l in root.iter("link")}
    if "pdf" in links:
        b = http_get(links["pdf"].replace("ftp://", "https://"))
        if b[:4] == b"%PDF":
            return b
    if "tgz" in links:
        tb = http_get(links["tgz"].replace("ftp://", "https://"))
        with tarfile.open(fileobj=io.BytesIO(tb), mode="r:gz") as tar:
            pdfs = [m for m in tar.getmembers() if m.name.lower().endswith(".pdf")]
            if pdfs:
                pdfs.sort(key=lambda m: m.size, reverse=True)
                b = tar.extractfile(pdfs[0]).read()
                if b[:4] == b"%PDF":
                    return b
    return None

def tier2_unpaywall(doi):
    if not doi:
        return None
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    try:
        data = json.loads(http_get(url))
    except Exception:
        return None
    locs = list(data.get("oa_locations") or [])
    # publisher-hosted를 우선 (봇차단 약하고 PDF 직링크 가능성 높음)
    locs.sort(key=lambda l: 0 if l.get("host_type") == "publisher" else 1)
    for loc in locs:
        pdf_url = loc.get("url_for_pdf")
        if not pdf_url:
            continue
        try:
            b = http_get(pdf_url)
            if b[:4] == b"%PDF":
                return b
        except Exception:
            continue
    return None


def main(pmids):
    os.makedirs(PAPERS, exist_ok=True)
    meta = esummary(pmids)
    idmap = idconv(pmids)
    ok, manual = [], []
    for pmid in pmids:
        m = meta.get(pmid, {})
        stem = make_stem(m) if m else f"pmid-{pmid}"
        ids = idmap.get(pmid, {})
        pmcid, doi = ids.get("pmcid"), ids.get("doi")
        pdf, tier = None, None
        if pmcid:
            try:
                pdf = tier1_pmc(pmcid)
                if pdf:
                    tier = f"PMC OA ({pmcid})"
            except Exception as e:
                print(f"  ! tier1 {pmcid} 오류: {e}")
        if not pdf:
            pdf = tier2_unpaywall(doi)
            if pdf:
                tier = "Unpaywall"
        if pdf:
            path = os.path.join(PAPERS, stem + ".pdf")
            with open(path, "wb") as fh:
                fh.write(pdf)
            ok.append((pmid, stem, tier, len(pdf)))
            print(f"[OK]     {pmid}  {tier:20}  {len(pdf)//1024:>5} KB  {stem}.pdf")
        else:
            manual.append((pmid, doi, stem))
            print(f"[MANUAL] {pmid}  paywall/OA없음  doi={doi}")
    print("\n=== 요약 ===")
    print(f"자동 {len(ok)}편 / 수동 필요 {len(manual)}편")
    for pmid, doi, stem in manual:
        print(f"  수동: PMID {pmid}  https://doi.org/{doi}")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.strip()]
    if not args:
        print("usage: python3 fetch-oa.py PMID [PMID ...]")
        sys.exit(1)
    main(args)
