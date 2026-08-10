---
title: "Daily-audit 신호 → 모닝브리핑 배지 브릿지"
type: agenda
date: 2026-07-15
status: draft
source_wiki: []          # 인프라 작업(코드 파이프라인)이라 근거 wiki 페이지 없음 — 의도적 공란
agenda: null
output_wiki: []
---

# Goal

`daily-audit.py`가 `logs/`에 쌓는 15개 감사 신호가 **읽히지 않으면 복리가 안 된다**. 현재 신호→행동 연결이 사람의 기억에 의존하는 게 유일한 약한 고리다. 이미 운영 중인 morning-briefing 파이프라인(Dentweb SQL → Supabase → Netlify)에 **감사 요약 배지 한 줄**을 물려, 아침에 `logs/`를 열지 않아도 그날의 top 신호가 표면화되게 한다.

이 요청이 제대로 처리되었다면: 아침 브리핑 상단에 `🔍 위키 감사: STALE overview N · category-overflow N · BROKEN link N` 형태의 배지가 뜨고, 0건이면 배지가 숨는다(노이즈 억제).

# Input

- `logs/{date}_*.md` — daily-audit 15개 산출 로그 (특히 signal 계열)
- morning-briefing 렌더 템플릿 (v2, six-badge system — 여섯 번째 슬롯 또는 신규 슬롯)
- 우선 표면화할 신호 3종 확정 필요:
  1. `overview-thesis-staleness` warn 건수 (진짜 stale overview)
  2. `category-overflow` 후보 건수 (overview 미작성 누적)
  3. `link-integrity` BROKEN 건수 (깨진 wikilink — 즉시 수리 대상)
  - 후보 확장: `supersession-audit` decay 후보, `find-contradiction-candidates` Tier1

# Output

- `scripts/audit-badge.py` (신규) — 최신 `logs/` 산출을 파싱해 배지 JSON 1개 emit. daily-audit 뒤에 실행.
- morning-briefing 템플릿에 배지 슬롯 추가 (masking gate 이후 단계 — 환자정보와 무관하므로 마스킹 영향 없음)
- 배포 순서: `daily-audit.py` → `audit-badge.py` → briefing 렌더

# Design constraints

- **Signal, not gate**: 배지는 알림일 뿐 브리핑 생성을 막지 않는다. 파싱 실패 시 배지만 생략, 브리핑은 정상 발행.
- **0건 = 숨김**: 매일 "이상 없음"을 띄우면 배지가 벽지가 된다. 신호가 있을 때만 렌더.
- **읽기 전용**: 배지는 `logs/`를 읽기만 한다. 감사 신호를 자동으로 "해결" 처리하지 않는다(임상 수치 자동 재작성 = Rule #1 위배와 같은 이유).
- 임계: category-overflow는 ≥5 누적일 때만 이미 후보이므로 그대로. staleness는 warn만(info 제외).

# Done (성공 기준)

- [ ] 표면화 신호 3종 확정 (위 3 + 확장 후보 중 택)
- [ ] `audit-badge.py`가 로그 부재/파싱 실패에도 non-zero exit 없이 빈 배지 emit
- [ ] 브리핑에 배지 슬롯 렌더 확인 (신호 有→표시, 0건→숨김)
- [ ] 배포 파이프라인 순서 반영
- [ ] 하루 실제 운영해 노이즈/과알림 여부 점검

# Notes

CLAUDE.md의 Daily Audit 섹션 "Closing the loop — audit signals → morning briefing" 문단이 이 agenda를 백링크한다. 브리핑 파이프라인 세부(Supabase 프로젝트, Netlify, 마스킹 게이트)는 별도 인프라 문서 소관 — 여기선 배지 슬롯 삽입 지점만 다룬다.
