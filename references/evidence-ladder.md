# Evidence Ladder — Supersession 판단 참조표

> **필드명 (2026-07-15):** 이 축의 frontmatter 필드는 `evidence_level:`이다 (구 `confidence:`, grandfather). 아래 설명의 "등급 값"은 모두 `evidence_level` 값을 가리킨다.

> **값 목록의 단일 출처는 `INGEST.md`의 "`evidence_level:` vocabulary" 표다.** 어떤 라벨이 유효한지(13개 study type + 4개 non-research 라벨)는 그곳에서 관리한다. 이 파일은 그 값들 사이의 **supersession 판단 규칙**(어느 등급이 어느 등급을 이기는가)과 보조 `rob:` 필드만 정의한다. `SOP.md`·`supersession-audit.py`의 인라인 설명은 판단 규칙에 관해 이 파일을 따른다. (`CLAUDE.md`는 인라인 설명 없이 `INGEST.md`로만 라우팅 — 이 파일을 직접 참조하지 않는다.)

## 근거 사다리 (partial-order, 높은 근거 → 낮은 근거)

```
sr+ma  >  sr  >  rct  >  prospective  >  retrospective
       >  cross-sectional  >  case-report  >  in-vivo / animal / in-vitro
       >  narrative-review  ≈  consensus        (expert opinion 최하위)
```

- `synthesis` (wiki overview): 외부 연구 유형이 아니므로 supersession 미적용.
- `regulation` / `official-qa` / `manual` / `patent`: non-research 문서 — 사다리에 올리지 않는다 (근거 무게 비교 대상 아님).
- 각 값의 정확한 정의는 `INGEST.md` 표 참조.

## Supersession 적용 규칙

**새 논문이 기존 페이지를 대체하려면 두 관문을 통과해야 한다:**

1. **같은 임상 질문에 반대 결론인가?**  
   - 범위 확장(`extends`) · 조건 한정(`refines`) · 결론 일치(`reinforces`) → 대체 아님

2. **새 쪽이 사다리에서 더 위인가?**  
   - 위 → 대체 강력 후보  
   - 같은 등급이면 규모(n) + 출판연도로 판단  
   - 아래 → **대체 불가** (2026 narrative-review는 2022 SR+MA를 이기지 못한다)

## Risk of Bias (rob) 보조 필드

고근거 논문(`rct` 이상)에서 동등 등급끼리 충돌할 때 RoB로 우선순위를 조정할 수 있다.

| `rob` 값 | 의미 |
|---|---|
| `low` | Low risk of bias |
| `some-concerns` | Some concerns |
| `high` | High risk of bias |
| *(생략)* | 미평가 (의무 아님) |

**적용 시나리오**: 같은 등급(`rct`) 두 편이 충돌 + 한쪽이 `rob: high` → 낮은 편을 우선하되 대체 판정은 신중.

**필드는 옵션.** `rob: high`인 논문이 `rob: low` 논문을 supersede하는 건 지양. 단, 규모가 압도적으로 크면 등급 내 규모 기준 적용.

```yaml
# 예시 (wiki frontmatter)
evidence_level: rct
rob: some-concerns
```

## 주의

- `synthesis` 등급의 overview 페이지는 supersession 대상이 아니다 — 외부 논문이 아니므로.
- 같은 등급 안에서 발행연도만으로 대체하지 않는다. 반드시 결론 충돌을 먼저 확인.
- `rob:` 필드가 없어도 lint 에러 아님 — 추론 보조 목적.
