# 신규 3종(Pixiel · Reactyl · Hexadrake) 작업 인계

웹 프론트 디자이너, 웹 프론트 기능개발자, 백엔드 아키텍트를 담당하는 하네몬 3종을 홈 벨트에 추가하는 작업의 현재 상태를 기록한다. 작업은 토큰 절약을 위해 중간에 일시 중지했으며, 이 문서만 읽으면 이어서 진행할 수 있다.

## 1. 대상 3종

| 종 | 타입 | 역할 | 담당 범위 |
| :--- | :--- | :--- | :--- |
| **Pixiel** | Fairy ✨ | Design System Warden | 시각 디자인, 디자인 토큰, 색상 스케일, 타이포그래피, 접근성 |
| **Reactyl** | Sky 🕊️ | Frontend Feature Flyer | 컴포넌트와 상태 구조, 서버/클라이언트 경계, 데이터 페칭, 프론트엔드 테스트 |
| **Hexadrake** | Dragon 🐉 | Ports & Adapters Architect | 헥사고날 구조, DDD, API 계약, 마이그레이션 안전성, 관측성과 보안 |

세 종은 하나의 팀으로 읽히도록 동일한 두상 기하 구조와 광원 방향을 공유하며, 색 계열과 소품으로만 구별한다.

## 2. 완료된 작업

### 2.1 종 골격

`species/pixiel`, `species/reactyl`, `species/hexadrake` 세 폴더를 생성했다. 사용자 요청에 따라 `templates/egg` 스캐폴드를 쓰지 않고, 기존 종인 `nimbleet`에서 공용 자산을 그대로 불러왔다.

- **공용 규칙 5개** — `fluent-korean`, `harness-evolution`, `skill-routing`, `task-execution-protocol`, `terminal-response-format`
- **훅 3개** — `commit-msg`, `pre-commit`, `install.sh`
- **공용 스킬 1개** — `harness-evolution/SKILL.md`

### 2.2 종별 고유 상시 규칙

검증을 통과한 조사 자료에 근거하여 종마다 서명 규칙 한 개씩을 작성했다. 세 파일 모두 100줄 제한을 만족한다.

- `species/pixiel/rules/design-system-discipline.md` (48줄) — 토큰 전용 스타일링, 4pt 그리드, 12단계 시맨틱 색상, WCAG 2.2 출시 차단 기준
- `species/reactyl/rules/frontend-architecture-discipline.md` (47줄) — 기능 단위 분할, 단방향 의존, `'use client'` 경계, 상태 유니온, 역할 우선 통합 테스트
- `species/hexadrake/rules/backend-architecture-discipline.md` (57줄) — 포트와 어댑터, 식별자 수준의 의존성 규칙, 트랜잭션당 애그리게이트 하나, 확장 후 축소 마이그레이션, 안정성 패턴

### 2.3 픽셀아트

내장 절차적 생성기(`sprite_write`)를 쓰지 않고 32×32 스프라이트 세 장을 한 픽셀씩 배치했다. 좌상단 단일 광원을 공유하고, 그림자는 차가운 쪽으로 하이라이트는 따뜻한 쪽으로 색상을 틀었다(휴 시프트).

- 산출물 — 각 종 폴더의 `sprite.json`과 `avatar.svg`
- 작성 스크립트 — `species/draw-trio-sprites.py` (행 단위 스팬 배치, 좌우 대칭 헬퍼 포함)
- 색 수 — Pixiel 13색, Reactyl 10색, Hexadrake 10색
- 식별 소품 — Pixiel은 금색 펜촉 볏과 하늘색에서 분홍으로 이어지는 색상 램프 날개, Reactyl은 젖혀진 볏과 주황 부리와 보라색 상태 궤도 표식, Hexadrake는 강철 뿔과 호박색 세로 동공과 가슴의 용융 육각 코어
- 검증 — 밝은 배경과 어두운 배경 양쪽에서 실루엣이 읽히는지 대비 시트를 렌더링하여 육안으로 확인함

### 2.4 메타데이터와 문서

- 종별 `partner.json` — `species`, `avatar`, `name`, `type`, `role`, `description` 기재
- 종별 `README.md` — 3기둥 구성, 실제 출처, 스프라이트 설명, 입양 명령
- 종별 `skills/INDEX.md` — 현재 존재하는 스킬만 등재하여 다크 스킬을 만들지 않았다

### 2.5 CLI 결함 수정 3건

`bin/harnemon`에서 신규 종이 정상 동작하지 못하게 막던 문제를 고쳤다. 세 수정 모두 기존 경로를 폴백으로 남겨 두어 기존 종의 동작은 바뀌지 않는다.

1. **손으로 그린 스프라이트가 입양 시 덮어쓰이던 문제** — `cmd_feed`가 종 폴더의 `sprite.json`을 무시하고 언제나 절차적 생성기를 호출했다. 종 폴더에 `sprite.json`이 있으면 그것을 복사하도록 바꿨다.
2. **종 전용 훅이 설치되지 않던 문제** — `cmd_feed`가 존재하지 않는 `$SCRIPT_DIR/hooks`만 참조하여 훅 설치가 조용히 실패했다. 종 폴더의 `hooks/`를 우선 참조하고 실행 권한을 부여하도록 바꿨다.
3. **커스텀 종이 목록과 입양에서 누락되던 문제** — `cmd_adopt`와 `cmd_recruit`의 메타데이터 조회가 `catalog/`만 보았고, `cmd_dex`는 내장 4종만 출력했다. 조회 경로에 `species/`를 추가하고, `dex`가 `species/`의 커스텀 종을 자동으로 나열하도록 바꿨다.

### 2.6 검증 결과

빈 git 저장소에서 `harnemon adopt pixiel`을 실행하여 다음을 확인했다.

- 종 이름과 타입과 설명이 `partner.json`에서 정확히 읽힌다
- 입양된 `sprite.json`이 손으로 그린 원본과 바이트 단위로 동일하다
- `.git/hooks/commit-msg`와 `.git/hooks/pre-commit`이 실제로 설치된다
- 규칙 6개가 `.agents/AGENTS.md`에 자동으로 연결된다
- `harnemon audit`이 3기둥 무결성 검사를 모두 통과한다

## 3. 조사 자료

11개 조사 축을 병렬로 수행하고, 인용된 URL을 각각 실제로 열어 존재 여부와 설명의 정확성을 반증 방식으로 검증했다. 워크플로는 종합 단계 직전에 중지했으나 조사와 검증 결과는 모두 회수했다.

- **위치** — `docs/research/trio-research-pool.json`
- **구성** — 검증 통과 76건(`pool`), 수집했으나 검증 단계에 도달하지 못한 98건(`unverified`), 하네스 형식에 관한 교훈 113건(`formatLessons`)
- **항목 구조** — `name`, `url`, `origin`, `whatItIs`, `concreteDirective`, `shellGate`, `pillar`, `targetSpecies`, `famousBecause`
- **분포** — 종별로 Reactyl 29건, 공용 22건, Hexadrake 14건, Pixiel 11건이며, 기둥별로 규칙 34건, 훅 23건, 스킬 19건

`concreteDirective`는 그대로 규칙 문장으로 옮길 수 있는 형태로 작성되어 있고, `shellGate`는 POSIX sh 훅으로 옮길 수 있는 구현 스케치를 담고 있다.

## 4. 남은 작업

아래 순서대로 진행하면 된다. 모든 근거는 `docs/research/trio-research-pool.json`에 이미 들어 있으므로 재조사는 필요하지 않다.

1. **종별 스킬 작성** — 조사 자료에서 `pillar`가 `skill`인 19건을 종별로 묶어 `skills/<이름>/SKILL.md`로 작성한다. YAML frontmatter의 `name`과 `description`은 필수이며, `description`은 언제 로드해야 하는지 알 수 있도록 트리거 어휘를 3인칭으로 담는다.
   - Pixiel 후보 — 접근성 감사 절차, 디자인 토큰 정의와 이관 절차, 시각 회귀 검사 절차
   - Reactyl 후보 — 통합 테스트 작성 절차, 서버 컴포넌트 이관 절차, 번들 예산 진단 절차
   - Hexadrake 후보 — ADR 작성 절차, API 계약 파괴 변경 진단 절차, 확장 후 축소 마이그레이션 절차
2. **`skills/INDEX.md` 갱신** — 새로 만든 스킬을 이름과 트리거 조건과 한 줄 설명으로 등재한다. 등재하지 않은 스킬은 호출되지 않으므로 반드시 원자적으로 함께 갱신한다.
3. **종별 `skill-routing.md` 교체** — 현재는 `nimbleet`의 공용 라우팅 표가 그대로 복사되어 있어 `ponytail`과 `systematic-debugging` 등 다른 종의 스킬을 가리킨다. 각 종이 자기 스킬로 분기하도록 다시 쓴다.
4. **종별 전용 훅 추가** — 조사 자료의 `shellGate` 23건 가운데 zero-dependency로 구현 가능한 것을 골라 `hooks/pre-commit`에 병합하거나 별도 훅으로 추가한다. `hooks/install.sh`는 현재 `commit-msg`와 `pre-commit`만 설치하므로 훅을 늘리면 이 목록도 함께 넓혀야 한다.
5. **README의 3기둥 목록 갱신** — 1번부터 4번까지의 결과를 반영한다.
6. **`harnemon audit` 재실행** — 종마다 빈 저장소에 입양하여 규칙 줄 수, 스킬 명세, 훅 권한을 다시 검증한다.
7. **문서 다국어화** — 공개 문서를 건드릴 경우 EN, KO, JA, ZH 네 벌을 원자적으로 동기화한다.

## 5. 알려진 미해결 사항

- **프로젝트 사본의 명령어가 낡았다** — `~/general-ai/.harnemons/` 아래 세 종(`nimbleet`, `monkin`, `yagni`)의 `harness-evolution.md`와 `skill-routing.md`와 `harness-evolution/SKILL.md`가 존재하지 않는 `mhm audit` 명령을 지시한다. 글로벌 벨트에는 이미 `harnemon audit`으로 고쳐져 있으므로 `harnemon update`로 동기화하거나 해당 파일을 직접 고치면 된다.
- **CLI 수정이 커밋되지 않았다** — `bin/harnemon`의 수정 3건과 신규 종 3개는 작업 트리에만 있다. 원본은 필요하면 git으로 되돌릴 수 있다.
- **워크플로 종합 단계가 미완이다** — 조사와 검증은 끝났으나 종별 하네스 설계 종합과 완결성 비평 단계는 실행되지 않았다. 4번 항목의 스킬과 훅 작성은 조사 자료를 직접 읽어 진행하는 편이 재실행보다 저렴하다.

## 6. 관련 경로

| 대상 | 경로 |
| :--- | :--- |
| 홈 벨트 | `~/.harnemon` (`~/harnemon`을 가리키는 심볼릭 링크이므로 저장소는 하나뿐이다) |
| 신규 종 | `species/pixiel`, `species/reactyl`, `species/hexadrake` |
| 스프라이트 작성 스크립트 | `species/draw-trio-sprites.py` |
| 조사 자료 | `docs/research/trio-research-pool.json` |
| 수정된 CLI | `bin/harnemon` |
