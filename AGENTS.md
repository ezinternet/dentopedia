# AGENTS.md — LLM Wiki (치과학)

이 파일은 **`AGENTS.md` 규약을 쓰는 에이전트**(OpenCode 등)의 진입점입니다.
OpenCode V2는 `CLAUDE.md`를 대체 파일로 읽지 않습니다 — `AGENTS.md` 전용입니다.
그래서 이 파일이 존재합니다.

## 0. 먼저 읽을 것 — 행동 규칙은 `CLAUDE.md`에 있다

**행동 규칙의 정본(single source of truth)은 `CLAUDE.md`** 입니다. 이 파일에 복제하지 않습니다
(두 벌은 반드시 drift한다 — `CLAUDE.md` 자신의 원칙).

작업 시작 전에 `CLAUDE.md`를 읽으십시오. 여기 들어 있는 것:

- **THE FOUR RULES** — 환각 방지·출처 원칙. 특히 **Rule #1: 답변은 인제스트된 지식에서만.**
  이 리포에서 Rule #1은 일반 "웹 검색 우선" 정책을 **덮어씁니다**.
- **Output rules** — 세션 확신도 태그(`[확인]`/`[미검증]`), 용어 표기 규칙, 언어 정책,
  overview 한국어 요약.

보조 문서(각 영역의 정본, 내용을 `AGENTS.md`에 복사하지 말 것):

| 문서 | 언제 |
|---|---|
| `INGEST.md` | 논문을 위키에 추가 (인제스트). 파이프라인·필드·템플릿 규칙 |
| `OPERATIONS.md` | `agenda/`·`slides/`·`interactives/`·`peer-review/`·`note-meeting/` 생성 |
| `AUDITS.md` | 감사 추가/변경, `logs/` 해석 |
| `SOP.md` | 사람이 읽는 운영 절차 |
| `wiki/_meta/categories.md` | 카테고리 선택 |

## 1. 환자 식별 표기 (mandatory — 안전 규칙, 예외 없음)

환자·보호자·직원의 **성명을 응답·산출물·위키 어디에도 쓰지 않습니다.**
식별이 필요하면 **차트번호**로 합니다 (덴트웹에서 그대로 조회 가능).
생년월일·연락처·주민등록번호·이메일도 동일하게 취급합니다.

**범위를 반드시 구분하십시오 — 리포는 공개 Pages 배포입니다:**

| 범위 | 성명 | 차트번호 | 표기 |
|---|---|---|---|
| **커밋되는 파일** (`wiki/`·`note-meeting/`·`interactives/`·`slides/`) | ⛔ 금지 | ⛔ **금지** | `환자 A`, `59세 여` |
| **커밋되지 않는 로컬 작업·대화** (`~/dentweb-analysis` 등) | ⛔ 금지 | ✅ 허용 | `차트 NNNNNNN` 형식 |

- 공개 리포 쪽 근거: `note-meeting/_template.md`의 익명화 규칙 +
  `scripts/pii-guard.py`의 `CHART` 정규식이 차트번호 패턴을 **차단**합니다.
- **왜 코드가 아니라 행동 규칙인가**: `pii-guard.py`는 주민번호·전화·이메일·차트번호만
  잡고 **성명은 못 잡습니다**(한국어 이름은 결정론적 패턴 매칭이 불가능). 따라서
  이름 금지는 정규식으로 강제할 수 없고, 이 규칙이 유일한 방어선입니다.
- 되돌릴 수 없는 유일한 실패 모드입니다 — 공개된 환자 식별정보는 git 히스토리·
  Pages 캐시·검색엔진 색인에 남습니다.

`python3 scripts/pii-guard.py`로 커밋 전 검사를 돌리십시오.

## 2. `CLAUDE.md`를 자동으로 로드시키려면 (선택)

`AGENTS.md`는 자동 로드되지만 `CLAUDE.md`는 그렇지 않습니다. 리포 설정에서 명시하면
두 파일이 함께 로드됩니다 (`opencode.jsonc`):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["CLAUDE.md"],
}
```

지정하지 않으면 위 §0의 지시대로 `CLAUDE.md`를 **직접 읽어야** 합니다.
