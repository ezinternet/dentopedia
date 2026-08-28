---
epoch: 1787416732000
mode: agent
backendId: opencode
projectId: "e1f03dfc-a65b-4d9c-aa84-dda3925935be"
sessionId: "ses_fd5a9af1effemuhFGMvlPw9oy2"
agentLabel: "Evernote MCP 연결 설정"
lastAccessedAt: 1787417437872
usage: '{"usedTokens":36062,"contextWindow":200000,"updatedAt":1787417382180}'
tags:
  - copilot-conversation
---

**user**: evernote  mcp 연결하고 싶어   연결해줘
[Timestamp: 2026/08/23 01:38:52]

**ai**: 
[Timestamp: 2026/08/23 01:38:52]

**user**: https://dev.evernote.com/ko-kr/mcp
[Timestamp: 2026/08/23 01:41:23]

**ai**: 공식 페이지 확인 완료 [확인] — Evernote는 원격(remote) MCP 서버(`https://mcp.evernote.com/mcp`)로 제공되고 OAuth 자동 인증 방식이네요. 범용 클라이언트 연결 가이드도 확인하겠습니다.원격 서버 방식(Streamable HTTP + OAuth)이 확인됐습니다 [확인]. 이제 opencode 설정 스키마에서 원격 MCP 필드 형식을 검증하고 설정 파일을 작성하겠습니다.
[Timestamp: 2026/08/23 01:41:23]

**user**: 멈춘건가
[Timestamp: 2026/08/23 01:46:14]

**ai**: 아니요, 멈춘 게 아니라 제 마지막 응답이 잘렸습니다 — 죄송합니다. 준비는 다 끝났고 이제 설정 파일만 쓰면 됩니다. 바로 진행할게요.

지금까지 확인된 사항:

- Evernote MCP는 원격(remote) 서버 방식: `https://mcp.evernote.com/mcp`, 인증은 OAuth 자동 처리(동적 클라이언트 등록, Dynamic Client Registration 지원) [확인]
- opencode 스키마에 원격 MCP + OAuth 필드가 정확히 대응됨 (`type: "remote"`, `url`, `oauth`) [확인]
- 기존 opencode.json은 전역·프로젝트 어디에도 없음 — 새로 만들어도 충돌 없음 [확인]

이 Evernote 프로젝트 전용으로 프로젝트 레벨 설정에 넣겠습니다:
[Timestamp: 2026/08/23 01:46:14]

**user**: ㅏ멈춘건가 또
[Timestamp: 2026/08/23 01:49:05]

**ai**: 죄송합니다, 응답이 두 번이나 잘렸네요. 이번엔 바로 파일부터 씁니다.완료됐습니다. 설정 파일을 방금 썼습니다 [확인]:

- **파일**: `/Users/oracleneo/llm-wiki/copilot/projects/Evernote/opencode.json` — 이 Evernote 프로젝트 전용
- **내용**: 원격 MCP 서버 `https://mcp.evernote.com/mcp` + OAuth 활성화 [확인] (URL·OAuth 방식은 공식 문서에서, 필드 형식은 opencode 공식 스키마에서 검증함)

**다음 단계 — 재시작이 필요합니다:**

1. 지금 세션은 이미 로드된 설정을 쓰고 있어서, **opencode(이 대화)를 종료하고 다시 시작**해야 MCP가 붙습니다.
2. 재시작 후 처음 연결될 때 **브라우저에 Evernote 로그인 화면이 뜹니다** — 승인하면 OAuth 토큰이 저장되고, 그 다음부턴 자동 연결됩니다. (API 키 복사 같은 건 필요 없는 구조입니다)
3. 재시작 뒤에 "내 에버노트 노트북 목록 보여줘" 같은 걸로 물어보면 도구가 실제로 붙었는지 바로 확인됩니다.

참고: Evernote MCP는 베타라서 노트·노트북·태그·작업 위주로 지원 범위가 점점 바뀌는 중이라고 공식 문서에 명시돼 있습니다 [확인].

전역(모든 Copilot 프로젝트)에서 쓰고 싶어지면, 같은 내용을 `~/.config/opencode/opencode.json`으로 옮기면 됩니다 — 원하시면 말씀만 주세요.
[Timestamp: 2026/08/23 01:49:05]