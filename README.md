# MHM (My Harness Manager)

> **"하네스를 위한 하네스 (The Meta-Harness for AI Coding Agents)"**

MHM(My Harness Manager)은 개발자와 엔지니어링 팀이 남의 하네스를 무비판적으로 복제하는 대신, **자신만의 고유한 3대 기둥(Rule, Skill, Hook) AI 하네스를 정의하고, 스캐폴딩하고, 감사하며 진화시킬 수 있도록 돕는 메타 도구이자 지식 허브**입니다.

---

## 1. MHM이 해결하는 문제

AI 코딩 어시스턴트(Claude Code, Cursor, Codex, Antigravity)를 도입할 때 대부분의 팀은 두 가지 극단적인 실패 모드에 빠집니다:

1. **Level 1의 모놀리식 프롬프트 비대화** — `CLAUDE.md`나 `.cursorrules` 하나에 수백 줄의 지침을 몰아넣어 상시 토큰이 폭발하고 모델이 지침을 잊어버림
2. **복잡한 거대 하네스 무비판적 복제** — 수백 개의 스킬과 무거운 Node.js 런타임을 요구하는 거대 하네스(예: ECC)를 그대로 가져와 감당할 수 없는 복잡성(Over-engineering)에 직면함

MHM은 **"가장 작고, 가장 단단하며, 완벽히 직교하는 나만의 하네스"**를 설계할 수 있도록 명확한 학문적 체계와 도구를 제공합니다.

---

## 2. 핵심 문서 체계 (`docs/`)

- **[`what-is-a-harness.md`](docs/what-is-a-harness.md)** — **하네스의 정의**
  - 프롬프트 vs 에이전트 vs 하네스의 차이 및 프롬프트 엔지니어링의 한계
- **[`maturity-model.md`](docs/maturity-model.md)** — **하네스 발전 5단계 성숙도 모델**
  - Level 0 (Ad-hoc) ➔ Level 1 (Monolithic) ➔ Level 2 (3-Pillar) ➔ Level 3 (Router & Gate) ➔ Level 4 (Meta-Governed)
- **[`three-pillars-and-invariants.md`](docs/three-pillars-and-invariants.md)** — **3대 기둥과 3대 불변식**
  - 기둥 1: Rule (상시 규칙 및 라우터)
  - 기둥 2: Skill (온디맨드 역량)
  - 기둥 3: Hook (물리적 차단 게이트)
  - 3대 불변식: 멱등성(Idempotency), 자동 배선(Auto-wiring), 무의존성(Zero-dependency)

---

## 3. 대표 하네스 아키텍처 분석 사례집 (`docs/case-studies/`)

- **[사례 1: Jihan Harness](docs/case-studies/01-jihan-harness.md)** — 린(Lean) 3기둥 구조, 스킬 라우터 패턴, 제로 디펜던시 루트 클린 배선
- **[사례 2: ECC (Everything Claude Code)](docs/case-studies/02-everything-claude-code.md)** — 거대 Agentic OS, 수명주기 훅(`PreToolUse`/`Stop`), linter 설정 약화 차단
- **[사례 3: Superpowers (obra)](docs/case-studies/03-obra-superpowers.md)** — 철칙(The Iron Law) 기반의 원인 규명 우선 디버깅, TDD 사이클
- **[사례 4: Ponytail (Dietrich Gebert)](docs/case-studies/04-dietrich-ponytail.md)** — 과잉 엔지니어링 억제, 게으름의 사다리, diff 복잡성 사냥 및 지름길 부채 관리

---

## 4. 메타 하네스 CLI (`mhm`)

MHM은 의존성(Zero-dependency) 없이 즉시 실행 가능한 Bash 기반 CLI를 제공합니다.

### 1. 나만의 하네스 스캐폴딩 (`mhm init`)
```bash
# 3대 기둥과 자동 배선 설치기가 포함된 커스텀 하네스 생성
./bin/mhm init my-team-harness
```

### 2. 하네스 품질 및 토큰 감사 (`mhm audit`)
```bash
# 특정 하네스 또는 프로젝트의 규칙 크기, 스킬 명세, 훅 실행성 진단
./bin/mhm audit /path/to/my-harness
```

### 3. 대표 사례 목록 조회 (`mhm cases`)
```bash
./bin/mhm cases
```

---

## 5. 글로벌 설치 및 사용법

```bash
# 로컬 PATH에 심링크 등록 (어디서나 mhm 호출 가능)
ln -sf "$(pwd)/bin/mhm" /usr/local/bin/mhm
```
