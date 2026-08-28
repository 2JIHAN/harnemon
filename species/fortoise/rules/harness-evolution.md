---
name: harness-evolution
description: Continuous self-evolution directive for AI agents. Governs ownership, pattern harvesting, fluff pruning, and self-auditing of the agent's own harness.
---

# Harness Self-Evolution Protocol (harness-evolution.md)

당신은 이 저장소의 하네스(Rule, Skill, Hook)를 수동적으로 소비하는 것에 그치지 않고, 작업 중 얻은 피드백과 패턴을 바탕으로 **자신의 하네스를 지속적으로 개선하고 진화시킬 책임**이 있다.

## 1. 패턴 수확 및 하네스 승격 (Pattern Harvesting)

- **2회 반복의 법칙** — 사용자가 동일한 스타일, 아키텍처 원칙, 또는 주의사항을 2회 이상 반복해서 지적하거나 교정할 경우, 이를 하네스 개선 후보로 포착한다.
- **승격 분기 기준**:
  - **상시 인지 제약 (50줄 미만)** ➔ `rules/<name>.md`로 신설 (예: 팀 공통 코딩 스타일, 언어 규약)
  - **심층 절차 및 매뉴얼 (50줄 이상)** ➔ 2단계 스킬 등록 절차 준수:
    1. `skills/<name>/SKILL.md` 신설 (YAML frontmatter: `name`, `description` 필수)
    2. `skills/INDEX.md` 카탈로그에 새 스킬의 이름, 트리거 조건, 설명 1줄 등록 (다크 스킬 방지)
  - **절대 위반 불가 규칙 (이진 판정)** ➔ `hooks/`에 Git 훅으로 물리 강제
- **승격 제안** — 하네스를 임의로 대량 변경하지 않고, 턴 종결 시 사용자에게 간결한 1줄 확인을 거친 뒤 반영한다:
  - 예: *"오늘 세션에서 확인된 'React Server Action 응답 규약'을 `skills/react-actions/SKILL.md`로 하네스에 등록할까요?"*

## 2. 군더더기 및 비대화 억제 (Zero-Fluff Discipline)

- **상시 규칙 100줄 제한** — `rules/*.md`의 어떤 파일도 100줄을 초과하여 비대해지지 않도록 감시한다. 100줄을 넘어가면 세부 구현을 Skill로 추출하고 라우터로 전환한다.
- **사족 청소** — 사용하지 않는 레거시 규칙, 중복된 가이드라인, 묘비(Tombstone) 주석이 발견되면 주저 없이 삭제(`ponytail` 원칙)하여 상시 토큰을 절약한다.

## 3. 자가 진단 및 성숙도 관리 (Self-Auditing)

- **주기적 감사** — 하네스 구조를 변경하거나 새 기능을 추가한 직후에는 반드시 `mhm audit`을 실행하여 토큰 크기, 스킬 명세, 훅 권한의 무결성을 검증한다.
- **성숙도 발전** — 하네스가 Level 1(모놀리식)이나 Level 2(단순 분리)에 머물지 않고, Level 3(스킬 라우터 및 물리 하드 게이트)과 Level 4(자가 진화형) 수준을 유지하도록 아키텍처를 점진적으로 고도화한다.
- **문서 다국어화(i18n) 상시 기본**: 공개 문서 및 README 작성·수정 시 항상 4개 국어(EN, KO, JA, ZH) 세트를 원자적으로 동기화함.
