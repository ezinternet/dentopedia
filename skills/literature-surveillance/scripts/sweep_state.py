#!/usr/bin/env python3
"""literature-surveillance 상태/중복/큐 I/O.

PubMed MCP 호출은 Claude(MCP)가 담당하고, 이 스크립트는 상태 파일과
인제스트 큐의 읽기/쓰기·중복 제거·집계만 맡는다. MCP를 직접 호출하지 않는다.

서브커맨드:
  init             .surveillance/ 와 state.json / queue.md 초기화 (시드 토픽 포함)
  load             활성 토픽·last_run_edat·seen 개수 출력 (검색 파라미터 구성용)
  dedup            --topic T --pmids a,b,c [--watermark|--watermark-value N]
                     seen·screened·큐에 없는 신규 PMID만 JSON. water-mark 옵션은
                     max(seen) PMID 초과분만 신규로 컷(죽은 edat 필터 대체).
  enqueue          --json FILE   →  후보를 queue.md에 append, seen·last_run 갱신
  screen-out       --json FILE   →  Haiku가 탈락시킨 후보를 screened_out 버킷에 기록
  review-screened  [--older-than D] [--topic T]  →  재심 대상 screened_out 출력
  restore-screened --pmids a,b,c →  screened_out 에서 빼내 다음 sweep 때 재부상
  status           토픽별 신규/누적, screened, 큐 총량 요약

세 가지 PMID 상태(불변식):
  · unseen       → sweep 에서 부상해야 함
  · seen_pmids   → 이미 ingest 결정 (영구 재부상 금지)
  · screened_out → Haiku 탈락 (별도 버킷·복구 가능; 루틴 재부상 금지, review 로 재심)
경계선(borderline) 판정은 어느 버킷에도 넣지 않는다 — 그 sweep 안에서 상위 모델이 직접 판정.
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


def water_mark(state: dict) -> int:
    """max(seen_pmids) — PMID 등재순 단조증가를 edat 프록시로 쓰는 water-mark.

    PubMed MCP search_articles가 date_from/datetype=edat를 무시하는 것이 확인돼
    (2026-07-14 sweep), 이 water-mark 초과분만 '지난 sweep 이후 진짜 신규'로 본다.
    seen이 비면 0 → 필터 무효(모두 신규). 자세한 배경은 SKILL.md '알려진 결함'.
    """
    pmids = [int(p) for p in state.get("seen_pmids", []) if str(p).isdigit()]
    return max(pmids) if pmids else 0


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
        save_state(base, {"topics": SEED_TOPICS, "seen_pmids": [], "screened_out": {}})
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
        "watermark": water_mark(state),  # sweep 시작 시 이 값을 dedup --watermark-value 로 고정
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
    screened = set(state.get("screened_out", {}))
    seen = set(state.get("seen_pmids", [])) | queue_pmids(base)
    incoming = [p.strip() for p in args.pmids.split(",") if p.strip()]
    # water-mark: date_from/edat 필터가 죽어 있으므로 max(seen) PMID 초과분만 진짜
    # 신규로 본다. --watermark-value 로 스냅샷을 고정하면 sweep 중 enqueue 로 seen 이
    # 커져도 토픽별 dedup 기준이 흔들리지 않는다(권장). --watermark 는 호출 시점 max(seen).
    wm = None
    if args.watermark_value is not None:
        wm = args.watermark_value
    elif args.watermark:
        wm = water_mark(state)

    def below_wm(p):
        return wm is not None and p.isdigit() and int(p) <= wm

    # 루틴 sweep 은 screened_out 도 제외 — 탈락분이 매번 재부상해 재스크리닝 비용이
    # 반복되는 것을 막는다. 복구가 필요하면 restore-screened 로 명시적으로 되살린다.
    new = [p for p in incoming if p not in seen and p not in screened and not below_wm(p)]
    out = {
        "topic": args.topic,
        "incoming": len(incoming),
        "new": new,
        "excluded_seen": len([p for p in incoming if p in seen]),
        "excluded_screened": len([p for p in incoming if p in screened and p not in seen]),
    }
    if wm is not None:
        out["watermark"] = wm
        out["excluded_below_watermark"] = len(
            [p for p in incoming if below_wm(p) and p not in seen and p not in screened]
        )
    print(json.dumps(out, ensure_ascii=False, indent=2))


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


def cmd_screen_out(args):
    """Haiku 관련성 스크리닝에서 exclude 판정된 후보를 screened_out 버킷에 기록.

    입력 JSON 항목: {pmid, topic, edat, reason, verdict?, screened_by?}
    이미 seen(=ingest 결정)이거나 이미 screened 된 PMID 는 건너뛴다.
    seen_pmids 에는 넣지 않는다 — 이게 false-negative 영구 소실을 막는 핵심.
    """
    base = Path(args.base)
    state = load_state(base)
    entries = json.loads(Path(args.json).read_text(encoding="utf-8"))
    if isinstance(entries, dict):
        entries = [entries]
    screened = dict(state.get("screened_out", {}))
    seen = set(state.get("seen_pmids", []))
    added, skipped, log_lines = 0, 0, []
    for e in entries:
        pmid = str(e["pmid"])
        if pmid in seen or pmid in screened:
            skipped += 1
            continue
        screened[pmid] = {
            "topic": e.get("topic", "?"),
            "edat": e.get("edat", "?"),
            "reason": e.get("reason", ""),
            "verdict": e.get("verdict", "exclude"),
            "screened_by": e.get("screened_by", "haiku"),
            "screened_on": today(),
        }
        added += 1
        log_lines.append(
            f"- PMID {pmid} | {e.get('topic','?')} | edat {e.get('edat','?')} | "
            f"screened {today()} | {e.get('reason','')}\n"
        )
    state["screened_out"] = screened
    save_state(base, state)
    if log_lines:
        with (base / "screened-out.md").open("a", encoding="utf-8") as f:
            f.write("".join(log_lines))
    print(
        json.dumps(
            {"screened_out_added": added, "skipped": skipped, "screened_total": len(screened)},
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_review_screened(args):
    """재심 대상 screened_out 항목 출력 (상위 모델이 읽고 restore 여부 판단).

    --older-than D : 스크리닝된 지 D일 이상 지난 것만 (기본: 전체).
    --topic T      : 특정 토픽만.
    False-negative 복구 루프의 진입점 — supersession decay 와 같은 '저장 안 하고 계산' 철학.
    """
    base = Path(args.base)
    state = load_state(base)
    screened = state.get("screened_out", {})
    cutoff = None
    if args.older_than is not None:
        cutoff = dt.date.today() - dt.timedelta(days=args.older_than)
    out = []
    for pmid, meta in screened.items():
        if args.topic and meta.get("topic") != args.topic:
            continue
        if cutoff is not None:
            try:
                so = dt.datetime.strptime(meta.get("screened_on", ""), "%Y/%m/%d").date()
            except ValueError:
                so = None
            if so is not None and so > cutoff:
                continue  # 아직 재심 주기 도달 전
        out.append({"pmid": pmid, **meta})
    out.sort(key=lambda x: x.get("screened_on", ""))
    print(json.dumps({"count": len(out), "candidates": out}, ensure_ascii=False, indent=2))


def cmd_restore_screened(args):
    """screened_out 에서 PMID 를 빼낸다. seen 에는 없으므로 다음 dedup 때 재부상한다.

    Haiku 오탈락(false negative)을 상위 모델이 재심에서 뒤집을 때 사용.
    """
    base = Path(args.base)
    state = load_state(base)
    screened = dict(state.get("screened_out", {}))
    targets = [p.strip() for p in args.pmids.split(",") if p.strip()]
    restored = [p for p in targets if screened.pop(p, None) is not None]
    state["screened_out"] = screened
    save_state(base, state)
    print(
        json.dumps(
            {
                "restored": restored,
                "not_found": [p for p in targets if p not in restored],
                "screened_total": len(screened),
            },
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
    screened = state.get("screened_out", {})
    screened_by_topic = {}
    for meta in screened.values():
        tpc = meta.get("topic", "?")
        screened_by_topic[tpc] = screened_by_topic.get(tpc, 0) + 1
    print(
        json.dumps(
            {
                "seen_total": len(state.get("seen_pmids", [])),
                "watermark": water_mark(state),
                "screened_total": len(screened),
                "screened_by_topic": screened_by_topic,
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
    d.add_argument("--watermark", action="store_true",
                   help="max(seen) PMID 초과분만 신규로 (죽은 edat 필터 대체)")
    d.add_argument("--watermark-value", type=int, default=None,
                   help="water-mark 스냅샷 값 직접 지정 (sweep 시작 시 load/status 의 watermark 로 고정, 권장)")

    e = sub.add_parser("enqueue")
    e.add_argument("--json", required=True, help="후보 객체(배열) JSON 파일 경로")

    so = sub.add_parser("screen-out")
    so.add_argument("--json", required=True, help="탈락 후보(배열) JSON 파일 경로")

    rv = sub.add_parser("review-screened")
    rv.add_argument("--older-than", type=int, default=None, help="스크리닝 후 경과일 하한")
    rv.add_argument("--topic", default=None, help="특정 토픽만")

    rs = sub.add_parser("restore-screened")
    rs.add_argument("--pmids", required=True, help="복구할 콤마 구분 PMID 목록")

    args = ap.parse_args()
    {
        "init": cmd_init,
        "load": cmd_load,
        "dedup": cmd_dedup,
        "enqueue": cmd_enqueue,
        "screen-out": cmd_screen_out,
        "review-screened": cmd_review_screened,
        "restore-screened": cmd_restore_screened,
        "status": cmd_status,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
