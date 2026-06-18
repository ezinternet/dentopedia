#!/usr/bin/env python3
"""literature-surveillance 상태/중복/큐 I/O.

PubMed MCP 호출은 Claude(MCP)가 담당하고, 이 스크립트는 상태 파일과
인제스트 큐의 읽기/쓰기·중복 제거·집계만 맡는다. MCP를 직접 호출하지 않는다.

서브커맨드:
  init     .surveillance/ 와 state.json / queue.md 초기화 (시드 토픽 포함)
  load     활성 토픽·last_run_edat·seen 개수 출력 (검색 파라미터 구성용)
  dedup    --topic T --pmids a,b,c  →  seen·큐에 없는 신규 PMID만 JSON 출력
  enqueue  --json FILE              →  후보를 queue.md에 append, seen·last_run 갱신
  status   토픽별 신규/누적, OA 분포, 큐 총량 요약
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

# allowedDirectory 기준. 필요 시 --base 로 덮어쓸 수 있다.
DEFAULT_BASE = Path("/Users/oracleneo/llm-wiki/.surveillance")

# init 시 깔아둘 시드 토픽 (쿼리식은 references/topic-queries.md 와 동기화해서 운영)
SEED_TOPICS = {
    "implant": {
        "query": "(dental implant OR osseointegration OR peri-implantitis)",
        "ptyp": ["RCT", "SR", "MA"],
        "last_run_edat": None,
    },
    "endo": {
        "query": "(root canal OR endodontic OR pulp capping)",
        "ptyp": ["RCT", "SR", "MA"],
        "last_run_edat": None,
    },
    "perio": {
        "query": "(periodontitis OR scaling root planing OR keratinized mucosa)",
        "ptyp": ["RCT", "SR", "MA"],
        "last_run_edat": None,
    },
}

PTYP_TAG = {
    "RCT": "Randomized Controlled Trial[Publication Type]",
    "SR": "Systematic Review[Publication Type]",
    "MA": "Meta-Analysis[Publication Type]",
    "GUIDE": "Guideline[Publication Type]",
    "COHORT": "Cohort Studies[MeSH Terms]",
}


def state_path(base: Path) -> Path:
    return base / "state.json"


def queue_path(base: Path) -> Path:
    return base / "queue.md"


def load_state(base: Path) -> dict:
    p = state_path(base)
    if not p.exists():
        sys.exit(f"[에러] 상태 파일 없음: {p}\n먼저 `init` 을 실행하세요.")
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(base: Path, state: dict) -> None:
    state_path(base).write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def today() -> str:
    return dt.date.today().strftime("%Y/%m/%d")


def queue_pmids(base: Path) -> set:
    """큐에 이미 들어간 PMID 집합 (안전장치용)."""
    p = queue_path(base)
    if not p.exists():
        return set()
    found = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        # 형식: "- [ ] PMID 38123456 | ..."
        if "PMID " in line:
            try:
                found.add(line.split("PMID ", 1)[1].split(" ", 1)[0].strip())
            except IndexError:
                pass
    return found


def cmd_init(args):
    base = Path(args.base)
    base.mkdir(parents=True, exist_ok=True)
    if state_path(base).exists():
        print(f"[skip] 이미 존재: {state_path(base)}")
    else:
        save_state(base, {"topics": SEED_TOPICS, "seen_pmids": []})
        print(f"[생성] {state_path(base)} (시드 토픽 {len(SEED_TOPICS)}개)")
    if not queue_path(base).exists():
        queue_path(base).write_text(
            "# Ingest Queue (literature-surveillance)\n\n", encoding="utf-8"
        )
        print(f"[생성] {queue_path(base)}")
    else:
        print(f"[skip] 이미 존재: {queue_path(base)}")


def cmd_load(args):
    base = Path(args.base)
    state = load_state(base)
    out = {
        "seen_count": len(state.get("seen_pmids", [])),
        "topics": [],
    }
    for name, t in state["topics"].items():
        tags = " OR ".join(PTYP_TAG[k] for k in t.get("ptyp", []) if k in PTYP_TAG)
        out["topics"].append(
            {
                "topic": name,
                "query": t["query"],
                "ptyp_clause": f"({tags})" if tags else "",
                "last_run_edat": t.get("last_run_edat"),
                "suggested_query": f"{t['query']} AND ({tags})" if tags else t["query"],
            }
        )
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_dedup(args):
    base = Path(args.base)
    state = load_state(base)
    seen = set(state.get("seen_pmids", [])) | queue_pmids(base)
    incoming = [p.strip() for p in args.pmids.split(",") if p.strip()]
    new = [p for p in incoming if p not in seen]
    print(
        json.dumps(
            {"topic": args.topic, "incoming": len(incoming), "new": new},
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_enqueue(args):
    base = Path(args.base)
    state = load_state(base)
    candidates = json.loads(Path(args.json).read_text(encoding="utf-8"))
    if isinstance(candidates, dict):
        candidates = [candidates]

    seen = set(state.get("seen_pmids", []))
    already = queue_pmids(base)
    lines, added, touched_topics = [], 0, {}

    for c in candidates:
        pmid = str(c["pmid"])
        if pmid in seen or pmid in already:
            continue
        oa = c.get("oa", "none")
        oa_str = f"OA:{oa}"
        if oa == "PMC" and c.get("pmcid"):
            lic = f" ({c['license']})" if c.get("license") else ""
            oa_str = f"OA:PMC {c['pmcid']}{lic}"
        topic = c.get("topic", "?")
        lines.append(
            f"- [ ] PMID {pmid} | {c.get('ptyp','?')} | {oa_str} | {topic} | edat {c.get('edat','?')}\n"
            f"      \"{c.get('title','(제목없음)')}\" — {c.get('journal','?')}\n"
        )
        seen.add(pmid)
        added += 1
        touched_topics[topic] = c.get("edat") or today()

    if added:
        with queue_path(base).open("a", encoding="utf-8") as f:
            f.write("".join(lines))
    state["seen_pmids"] = sorted(seen)
    # 적립된 토픽의 last_run_edat 를 오늘로 갱신 (다음 sweep 기준점)
    for topic in touched_topics:
        if topic in state["topics"]:
            state["topics"][topic]["last_run_edat"] = today()
    save_state(base, state)
    print(
        json.dumps(
            {"added": added, "skipped": len(candidates) - added, "queue": str(queue_path(base))},
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_status(args):
    base = Path(args.base)
    state = load_state(base)
    pending = sum(
        1 for ln in queue_path(base).read_text(encoding="utf-8").splitlines()
        if ln.startswith("- [ ] PMID")
    ) if queue_path(base).exists() else 0
    done = sum(
        1 for ln in queue_path(base).read_text(encoding="utf-8").splitlines()
        if ln.startswith("- [x] PMID")
    ) if queue_path(base).exists() else 0
    print(
        json.dumps(
            {
                "seen_total": len(state.get("seen_pmids", [])),
                "queue_pending": pending,
                "queue_done": done,
                "topics": {
                    n: t.get("last_run_edat") for n, t in state["topics"].items()
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def main():
    ap = argparse.ArgumentParser(description="literature-surveillance 상태/큐 I/O")
    ap.add_argument("--base", default=str(DEFAULT_BASE), help="상태 루트 경로")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")
    sub.add_parser("load")
    sub.add_parser("status")

    d = sub.add_parser("dedup")
    d.add_argument("--topic", required=True)
    d.add_argument("--pmids", required=True, help="콤마 구분 PMID 목록")

    e = sub.add_parser("enqueue")
    e.add_argument("--json", required=True, help="후보 객체(배열) JSON 파일 경로")

    args = ap.parse_args()
    {
        "init": cmd_init,
        "load": cmd_load,
        "dedup": cmd_dedup,
        "enqueue": cmd_enqueue,
        "status": cmd_status,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
