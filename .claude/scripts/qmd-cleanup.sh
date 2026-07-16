#!/usr/bin/env bash
# llm-wiki qmd 인덱스 고아 벡터 청소 (launchd 매주 월 08:30 구동).
# launchd plist: ~/Library/LaunchAgents/com.llmwiki.qmd-cleanup.plist
#
# 왜 필요한가: 파일을 수정하면 해시가 바뀌어 새 벡터가 생기는데, 옛 벡터는
# 아무도 지우지 않는다. `qmd update`는 고아 *본문*만 치우고 고아 *벡터*는
# 손대지 않는다 (dist/store.js:1022). 벡터를 지우는 것은 `qmd cleanup`뿐이다.
#
# 왜 signal이 아니라 자동화인가: 검색이 조용히 망가진다. qmd는 전체 벡터에서
# 후보를 limit*3개 뽑은 뒤 살아있는 문서로 걸러낸다 (store.js:2681 — sqlite-vec가
# JOIN과 같이 쓰면 멈추는 버그 우회). 고아가 쌓이면 그 3배수 여유를 시체가
# 먹어치워 산 문서가 밀려난다. 에러는 안 난다 — 그래서 감사로는 안 잡힌다.
# 2026-07-17 실측: 고아 66.5%(40,513/60,960), 후보의 70%가 시체, 20개 요청 쿼리의
# 절반이 개수 미달, 최악은 후보 60개 중 생존 2개.
#
# 안전성: 살아있는 임베딩은 건드리지 않는다 (clearAllEmbeddings 미호출) —
# 재임베딩 불필요. 데몬(com.oracleneo.qmd-mcp)을 켠 채로 VACUUM 가능함을 실측 확인.
# 부작용은 llm_cache 삭제(알아서 재생성)와, 파일을 옛 버전으로 되돌릴 때
# 그 부분만 재임베딩(캐시가 식는 정도).

set -euo pipefail
export PATH="/opt/homebrew/bin:/Users/oracleneo/.local/bin:/usr/local/bin:/usr/bin:/bin"
WIKI_DIR="/Users/oracleneo/llm-wiki"
LOG_FILE="$WIKI_DIR/.claude/scripts/qmd-cleanup.log"
DB="$HOME/.cache/qmd/index.sqlite"
cd "$WIKI_DIR"

orphan_count() {
  sqlite3 "$DB" "SELECT COUNT(*) FROM content_vectors cv
    WHERE NOT EXISTS (SELECT 1 FROM documents d WHERE d.hash = cv.hash AND d.active = 1);" 2>/dev/null || echo "?"
}
live_count() {
  sqlite3 "$DB" "SELECT COUNT(*) FROM content_vectors cv
    WHERE EXISTS (SELECT 1 FROM documents d WHERE d.hash = cv.hash AND d.active = 1);" 2>/dev/null || echo "?"
}

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] qmd-cleanup start"
  before_orphan=$(orphan_count)
  before_live=$(live_count)
  echo "  before: 고아 ${before_orphan} / 산 벡터 ${before_live}"

  qmd cleanup

  after_orphan=$(orphan_count)
  after_live=$(live_count)
  echo "  after:  고아 ${after_orphan} / 산 벡터 ${after_live}"

  # 산 벡터가 줄었으면 사고다 — cleanup은 산 벡터를 건드리면 안 된다.
  if [ "$before_live" != "?" ] && [ "$after_live" != "?" ] && [ "$after_live" -lt "$before_live" ]; then
    echo "  ⚠️ 경고: 산 벡터가 ${before_live} → ${after_live} 로 줄었다. 예상 밖 — 확인 요망."
  else
    echo "  ✓ 산 벡터 보존 확인 (재임베딩 불필요)"
  fi
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] qmd-cleanup done"
} >> "$LOG_FILE" 2>&1
