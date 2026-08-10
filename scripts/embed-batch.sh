#!/bin/bash
# qmd embed를 10개씩 나눠서 완료될 때까지 반복
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki

ROUND=0

while true; do
  ROUND=$((ROUND + 1))
  PENDING=$(qmd status 2>/dev/null | grep "Pending" | grep -o '[0-9]*' | head -1)
  VECTORS=$(qmd status 2>/dev/null | grep "Vectors" | grep -o '[0-9]*' | head -1)
  TS=$(date '+%H:%M:%S')

  echo "[$TS] Round $ROUND — Embedded: ${VECTORS} | Pending: ${PENDING}"

  if [ "${PENDING}" = "0" ]; then
    echo "[$TS] ✓ 완료 — 모든 임베딩 완료 (Total: ${VECTORS})"
    break
  fi

  qmd embed --max-docs-per-batch 10 2>&1 | tail -2
  sleep 3
done
