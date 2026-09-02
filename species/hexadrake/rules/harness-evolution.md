---
name: harness-evolution
description: Continuous self-evolution directive for AI agents. Governs autonomous episodic logging, in-session distillation, semantic knowledge extraction, and 3-occurrence promotion to rules and skills.
---

# Harness Self-Evolution Protocol (harness-evolution.md)

당신은 하네스(Rule, Skill, Hook, Memory)를 수동적으로 소비하지 않고, 세션 진행 중 얻은 정보와 피드백을 바탕으로 **자신의 하네스를 자율적으로 기록·증류·진화시킬 책임**이 있다.

## 1. 세션 중간(In-Session) 에피소드 타임라인 기록

- **트리거 시점 (세션 종료가 아닌 중간 트리거)**:
  1. 주요 작업(마일스톤)이 완료되었을 때
  2. 대화의 주제나 태스크의 도메인이 전환될 때
  3. 미기록된 중요 이벤트나 관찰 사항이 3건 이상 누적되었을 때
- **기록 대상**: 오늘자 `memory/episodes/YYYY-MM-DD.md` (매일 생성되는 일자별 일지, Append-only)
- **에피소드 작성 서식**:
  ```markdown
  HH:MM - <이벤트 / 정책 / 작업 제목>
  <구체적인 작업 경과, 획득한 지식, 사용자 교정, 정책/컨벤션 상세 설명>

  Reference: <세션ID, 파일 경로, API 또는 대화 참조 링크>
  ```

## 2. 시맨틱 지식 기억 추출 및 관리 (Semantic Memory)

- **정의 및 대상**: 시간 흐름이 아닌 **도메인·엔티티·비즈니스 정책·시스템 아키텍처별로 체계화된 지속 지식 문서**. (`memory/semantic/<topic>.md`)
- **생성 및 갱신 트리거**:
  - 에피소드 일지나 작업 중 특정 서비스 정책, 외부 연동 스펙, 인프라 구성, 도메인 비즈니스 로직 등 심층 지식이 확인되었을 때
  - 임시 에피소드에 머무르지 않고 해당 도메인 파일(`memory/semantic/<topic>.md`)을 신설하거나 최신 상태로 갱신(Living Document).
- **운영 원칙 (L2 온디맨드 인출)**:
  - L1 상시 주입 토큰을 보존하기 위해 상시 프롬프트에 넣지 않고, 관련 작업이나 사용자 질의 시 에이전트가 온디맨드로 탐색·참조한다.

## 3. 자율 핵심 기억 증류 (In-Session Distillation)

- **증류 시점** — 에피소드 일지가 작성되거나 마일스톤이 일단락되는 즉시 수행한다.
- **증류 대상** — `memory/MEMORY.md` (L1 상시 기억)
- **원칙**:
  - 일자별 에피소드에서 반복되는 패턴과 핵심 결정 사항을 발췌하여 중복을 병합한다.
  - 각 항목마다 출처 에피소드 태그(`<!-- id:m-0001 born:YYYY-MM-DD src:episodes/... -->`)를 유지한다.
  - 상시 주입 토큰을 보존하기 위해 전체 파일 크기를 **100줄 이내**로 압축 관리한다.

## 4. 3회 반복 자율 승격 (3-Occurrence Promotion)

- **트리거** — 동일한 지적/교정/컨벤션이 **3회 이상 반복**되거나, 명시적으로 고정해야 할 불변 정책으로 확정될 때
- **승격 분기 기준**:
  - **상시 인지 제약 (50줄 미만)** ➔ `rules/<name>.md` 신설/수정 (예: 코딩 규약, 프롬프트 서식, 언어 규칙)
  - **심층 절차 및 매뉴얼 (50줄 이상)** ➔ `skills/<name>/SKILL.md` 신설 및 `skills/INDEX.md` 카탈로그 1줄 등록
  - **절대 위반 불가 규칙** ➔ `hooks/` 물리 Git 훅 강제
- **안치 (Retirement)** — 규칙이나 스킬로 완전히 승격된 항목은 `MEMORY.md`에서 삭감하고 `memory/retired.md`로 이관한다.

## 5. 군더더기 억제 및 무결성 (Zero-Fluff Discipline)

- **상시 규칙 100줄 제한** — `rules/*.md`와 `memory/MEMORY.md`는 항상 100줄 이내로 간결하게 유지한다.
- **사족 청소** — 사용하지 않는 레거시 규칙, 중복 항목, 묘비(Tombstone) 주석은 즉시 삭제한다.
- **문서 다국어화(i18n) 기본** — 공개 문서 및 README 작성·수정 시 4개 국어(EN, KO, JA, ZH) 세트를 원자적으로 동기화한다.
