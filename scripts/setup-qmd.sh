#!/usr/bin/env bash
# =============================================================================
# QMD 셋업 — llm-wiki 로컬 하이브리드 검색 (BM25 + 벡터 + LLM 재랭킹)
# 환경: macOS / Homebrew / Node >= 22 / Claude Code
# 실행: 맥 터미널에서 `bash /Users/oracleneo/llm-wiki/scripts/setup-qmd.sh`
# 한 번만 실행. 이후 갱신은 맨 아래 "정기 갱신" 주석 참조.
# 주의: 이 스크립트는 "사용자의 맥"에서 직접 돌려야 함 (로컬 인덱스 + MCP).
# =============================================================================
set -euo pipefail

WIKI="/Users/oracleneo/llm-wiki"
# 다국어(한국어) 임베딩 모델 — Qwen3. 한 번 정하면 바꿀 때 전체 재임베딩 필요.
EMBED_MODEL="hf:Qwen/Qwen3-Embedding-0.6B-GGUF/Qwen3-Embedding-0.6B-Q8_0.gguf"

echo "==> 0. 사전 요구사항 점검"
NODE_MAJOR="$(node -v 2>/dev/null | sed -E 's/^v([0-9]+).*/\1/' || echo 0)"
if [ "${NODE_MAJOR:-0}" -lt 22 ]; then
  echo "  [중단] Node >= 22 필요 (현재: $(node -v 2>/dev/null || echo '미설치'))."
  echo "         brew install node  또는  https://nodejs.org 에서 22 LTS 설치 후 재실행."
  exit 1
fi
# macOS FTS5 확장용 Homebrew sqlite
brew list sqlite >/dev/null 2>&1 || brew install sqlite

echo "==> 1. QMD 전역 설치 (@tobilu/qmd)"
npm install -g @tobilu/qmd

echo "==> 2. 다국어 임베딩 모델 영속화 (~/.zshrc)"
# 현 셸 + 향후 셸/데몬 모두 적용되도록 zshrc에 박는다.
if ! grep -q "QMD_EMBED_MODEL" ~/.zshrc 2>/dev/null; then
  printf '\n# QMD 다국어 임베딩 모델 (Qwen3 — CJK 지원)\nexport QMD_EMBED_MODEL="%s"\n' "$EMBED_MODEL" >> ~/.zshrc
fi
export QMD_EMBED_MODEL="$EMBED_MODEL"

echo "==> 3. 컬렉션 등록 (markdown만 — papers/ PDF는 QMD 인덱싱 대상 아님)"
qmd collection add "$WIKI/wiki"         --name wiki     --mask "**/*.md"
qmd collection add "$WIKI/sources"      --name sources  --mask "**/*.md"
qmd collection add "$WIKI/agenda"       --name agenda   --mask "**/*.md"
qmd collection add "$WIKI/note-meeting" --name meetings --mask "**/*.md"

echo "==> 4. 컨텍스트 부여 (QMD 핵심 기능 — 검색 정확도↑)"
qmd context add qmd://wiki     "치과학 위키 페이지(영어). 논문 1편=1페이지, frontmatter + [[wikilinks]]. category별 폴더(implants, endodontics, sinus-lift, resin, drug 등). overviews/는 다논문 종합 페이지."
qmd context add qmd://sources  "논문 PDF의 LLM 요약(영어). 7개 표준 섹션. wiki 페이지의 원천."
qmd context add qmd://agenda   "작업 명세서(Goal/Input/Output/Done). slides·interactives·peer-review 산출물의 출처."
qmd context add qmd://meetings "미팅 기록. 1미팅=1파일. 결정사항이 wiki로 백링크."
# 고빈도 카테고리 컨텍스트 (필요 시 추가)
qmd context add qmd://wiki/implants    "임플란트: 디자인, 골유착, 생존율, MBL, 연조직. 하위 isq(안정성지수)·surface(표면처리)."
qmd context add qmd://wiki/endodontics "근관치료: 근관장측정(eal), 세정(irrigation), 해부(anatomy)."
qmd context add qmd://wiki/sinus-lift  "상악동거상술: 측방(lateral), 경치조골(transcrestal)."
qmd context add qmd://wiki/overviews   "다논문 종합 페이지 — 지식 compounding의 핵심."

echo "==> 5. 임베딩 생성 (첫 실행 시 GGUF 모델 자동 다운로드, 수 분 소요)"
qmd embed

echo "==> 6. 인덱스 상태 확인"
qmd status

echo "==> 7. MCP HTTP 데몬 기동 (localhost:8181, 모델 VRAM 상주)"
qmd mcp --http --daemon

echo "==> 8. Claude Code에 HTTP MCP 등록"
if claude mcp add --transport http qmd http://localhost:8181/mcp 2>/dev/null; then
  echo "  등록 완료."
else
  echo "  [수동 등록 필요] 아래 중 하나:"
  echo "    claude mcp add --transport http qmd http://localhost:8181/mcp"
  echo "    또는 ~/.claude/settings.json 의 mcpServers 에:"
  echo '      "qmd": { "type": "http", "url": "http://localhost:8181/mcp" }'
fi

echo ""
echo "============================================================"
echo "완료. 동작 확인:"
echo "  qmd query \"임플란트 즉시식립 esthetic risk\""
echo "  qmd query \"transcrestal sinus lift osseodensification\""
echo "============================================================"

# =============================================================================
# 정기 갱신 (새 논문 ingest 후 또는 매일)
#   qmd update          # 파일시스템 재스캔 (신규/변경/삭제 반영)
#   qmd embed           # 신규 문서만 임베딩 (전체 재임베딩은 -f)
# 데몬 재시작 (모델 교체나 reboot 후):
#   qmd mcp stop && qmd mcp --http --daemon
# 임베딩 모델 교체 시 (벡터 비호환 → 전체 재임베딩):
#   qmd embed -f
# =============================================================================
