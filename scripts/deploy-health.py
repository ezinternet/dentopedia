#!/usr/bin/env python3
"""
deploy-health.py — GitHub Pages 배포 상태를 로컬에 표면화 (signal, never blocks)

왜 있는가 (2026-08-25)
----------------------
overview 하나의 `date:` 키 중복으로 Pages 배포가 **하루 넘게** 실패했는데
아무도 몰랐다. 로컬 감사 21개도 CI Wiki Lint도 전부 초록불이었고 — 배포만
따로 죽어 있었다. 발견 경로는 사람이 우연히 사이트를 확인하러 들어간 것뿐이었다.

`.github/workflows/deploy-pages.yml`의 `notify-failure` 잡이 실패 시 리포에
이슈를 남기지만(영구 기록), 그것도 **누가 GitHub을 봐야** 보인다. 이 감사는
같은 상태를 **매일 도는 로컬 감사 출력에** 끌어와, 세션에서 바로 눈에 띄게 한다.
두 겹인 이유가 이것이다 — 한쪽은 사라지지 않고, 한쪽은 찾아오지 않아도 보인다.

의존성은 `gh` CLI 하나뿐이고, 없거나 인증이 안 됐거나 네트워크가 없으면
**조용히 SKIP하고 exit 0**. 감사는 거울이지 gate가 아니다 (CLAUDE.md 설계원칙).

Usage:
    python3 scripts/deploy-health.py
"""

# PEP604(`str | None`) 힌트가 구 python3(3.9)에서 죽는다 — AUDITS.md의 알려진 함정.
# 이 감사는 PATH에 뭐가 앞서든 돌아야 하므로 annotation을 지연 평가시킨다.
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / f"{date.today().isoformat()}_deploy-health.log"
WORKFLOW = "Deploy Quartz site to GitHub Pages"
LIMIT = 10


def run_gh(args: list[str]) -> str | None:
    try:
        r = subprocess.run(["gh", *args], capture_output=True, text=True,
                           timeout=25, cwd=REPO)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    lines: list[str] = [f"# Deploy Health — {date.today().isoformat()}", ""]

    def emit(s: str = "") -> None:
        lines.append(s)

    if shutil.which("gh") is None:
        print("[deploy-health] SKIP — gh CLI 없음 (signal only, 차단 안 함)")
        emit("SKIP: gh CLI not installed")
        LOG.write_text("\n".join(lines) + "\n")
        return 0

    out = run_gh(["run", "list", "--workflow", WORKFLOW, "--limit", str(LIMIT),
                  "--json", "databaseId,status,conclusion,headSha,createdAt,url"])
    if out is None:
        print("[deploy-health] SKIP — gh 조회 실패 (미인증/오프라인). signal only")
        emit("SKIP: gh query failed (unauthenticated or offline)")
        LOG.write_text("\n".join(lines) + "\n")
        return 0

    try:
        runs = json.loads(out)
    except json.JSONDecodeError:
        print("[deploy-health] SKIP — gh 응답 파싱 실패")
        emit("SKIP: could not parse gh output")
        LOG.write_text("\n".join(lines) + "\n")
        return 0

    done = [r for r in runs if r.get("status") == "completed"]
    if not done:
        inflight = len(runs)
        print(f"[deploy-health] 진행 중 — 완료된 배포 실행 없음 (in-flight {inflight})")
        emit(f"IN FLIGHT: {inflight} run(s), none completed yet")
        LOG.write_text("\n".join(lines) + "\n")
        return 0

    latest = done[0]
    concl = latest.get("conclusion") or "unknown"
    sha = (latest.get("headSha") or "")[:7]

    emit(f"latest completed run : {latest.get('databaseId')}")
    emit(f"conclusion           : {concl}")
    emit(f"commit               : {sha}")
    emit(f"url                  : {latest.get('url')}")
    emit("")

    if concl == "success":
        print(f"🌐  Deploy health: 최신 배포 성공 ({sha})")
        emit("✅ 최신 배포 성공")
    else:
        # 연속 실패 구간을 세어 "언제부터 깨졌는지"를 알려준다 — 하루 넘게
        # 방치됐던 것이 2026-08-25 사고의 본질이었다.
        streak, first_bad = 0, None
        for r in done:
            if (r.get("conclusion") or "") != "success":
                streak += 1
                first_bad = r
            else:
                break
        age = ""
        if first_bad and first_bad.get("createdAt"):
            try:
                t = datetime.fromisoformat(first_bad["createdAt"].replace("Z", "+00:00"))
                hours = (datetime.now(timezone.utc) - t).total_seconds() / 3600
                age = f", {hours:.0f}시간째"
            except ValueError:
                pass
        print(f"🚨  Deploy health: 최신 배포 실패 — {concl} ({sha}), 연속 {streak}회{age}")
        print(f"      {latest.get('url')}")
        print(f"      먼저 확인: python3 scripts/lint.py  (둘째 줄 build-safety)")
        emit(f"🚨 실패 — 연속 {streak}회{age}")
        emit("가장 흔한 원인: wiki/ frontmatter 키 중복 (PyYAML은 통과, Quartz js-yaml만 죽음)")
        emit("확인: python3 scripts/lint.py → build-safety 줄")

    LOG.write_text("\n".join(lines) + "\n")
    print(f"      → {LOG.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
