# Evidence Ladder — 근거 등급 단일 참조표

이 파일이 유일한 정식 등급 정의다. `SOP.md`·`CLAUDE.md`·`supersession-audit.py`의 인라인 설명은 모두 이 표를 따른다.

## 근거 등급 (confidence 값 단일 partial-order)

| `confidence` 값 | 설명 | Supersession 판단 기준 |
|---|---|---|
| `sr+ma` | Systematic review + meta-analysis (umbrella review 포함) | 사다리 최상위 |
| `sr` | Systematic review (MA 없음) | |
| `rct` | Randomized controlled trial | |
| `prospective` | Prospective cohort / prospective case series | |
| `retrospective` | Retrospective cohort / chart review | |
| `cross-sectional` | Cross-sectional study, survey | |
| `case-report` | Case report / small case series (n < 10) | |
| `in-vivo` | In vivo clinical/animal experimental (위 카테고리 미해당) | |
| `animal` | Animal-only experimental | |
| `in-vitro` | Bench / laboratory study | |
| `narrative-review` | Narrative review, perspective, expert commentary | 사다리 최하위 (expert opinion) |
| `consensus` | Consensus statement / position paper | narrative-review와 동등 취급 |
| `synthesis` | Wiki overview (cross-paper synthesis) — 외부 연구 유형 아님 | supersession 미적용 |

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
confidence: rct
rob: some-concerns
```

## 주의

- `synthesis` 등급의 overview 페이지는 supersession 대상이 아니다 — 외부 논문이 아니므로.
- 같은 등급 안에서 발행연도만으로 대체하지 않는다. 반드시 결론 충돌을 먼저 확인.
- `rob:` 필드가 없어도 lint 에러 아님 — 추론 보조 목적.
