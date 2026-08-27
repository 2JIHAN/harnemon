# MHM (My Harness Manager) 문서 목차

AI 코딩 하네스의 정의, 진화 방향성, 그리고 대표적인 하네스 아키텍처 분석 사례집을 집대성한 지식 베이스다.

---

## 1. 핵심 사상 및 설계론

- **[`what-is-a-harness.md`](what-is-a-harness.md)** — **하네스의 정의**
  - 프롬프트 vs 에이전트 vs 하네스의 근본적 차이
  - 단순 프롬프트 엔지니어링이 필연적으로 실패하는 4대 공학적 이유
  - 모던 하네스의 3대 필수 구성요소
- **[`maturity-model.md`](maturity-model.md)** — **하네스 발전 5단계 성숙도 모델**
  - Level 0 (Ad-hoc) ➔ Level 1 (Monolithic) ➔ Level 2 (3-Pillar) ➔ Level 3 (Router & Gate) ➔ Level 4 (Meta-Governed)
  - 자가 진단 체크리스트 및 단계별 탈출 조건
- **[`three-pillars-and-invariants.md`](three-pillars-and-invariants.md)** — **3대 기둥과 3대 불변식**
  - 기둥 1: Rule (상시 인지 제약 & 라우팅)
  - 기둥 2: Skill (온디맨드 역량)
  - 기둥 3: Hook (물리적 차단 게이트)
  - 3대 불변식: 멱등성(Idempotency), 자동 배선(Auto-wiring), 무의존성(Zero-dependency)

---

## 2. 대표 하네스 아키텍처 분석 사례집 (Case Studies)

- **[`01-jihan-harness.md`](case-studies/01-jihan-harness.md)** — **Jihan Harness (`2JIHAN/jihan-harness`)**
  - 린(Lean) 3기둥 아키텍처, 스킬 라우터 패턴, 제로 디펜던시 루트 클린 배선
- **[`02-everything-claude-code.md`](case-studies/02-everything-claude-code.md)** — **ECC (`affaan-m/everything-claude-code`)**
  - 거대 종합 Agentic OS, 런타임 수명주기 훅(`PreToolUse`/`Stop`), linter 설정 약화 차단(`config-protection`)
- **[`03-obra-superpowers.md`](case-studies/03-obra-superpowers.md)** — **Superpowers (`obra/superpowers`)**
  - 철칙(The Iron Law) 기반의 원인 규명 우선 디버깅, TDD 사이클 및 증상 땜질 차단
- **[`04-dietrich-ponytail.md`](case-studies/04-dietrich-ponytail.md)** — **Ponytail (`DietrichGebert/ponytail`)**
  - 과잉 엔지니어링 억제, 게으름의 사다리(Ladder of Laziness), diff 복잡성 사냥 및 지름길 부채 관리
