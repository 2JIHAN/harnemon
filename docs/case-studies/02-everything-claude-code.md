# 사례 분석 2: ECC (`affaan-m/everything-claude-code`)

거대한 기능 스택과 런타임 수명주기 훅(Lifecycle Hooks)을 활용하여 에이전트를 운영체제 수준으로 통제하려는 종합 하네스의 대표 사례다.

---

## 1. 개요 및 설계 철학

- **저장소** — [github.com/affaan-m/ECC](https://github.com/affaan-m/everything-claude-code) (Everything Claude Code)
- **핵심 모토** — "The Agentic OS & Performance Optimization System"
- **설계 특성** — 280개 이상의 스킬, 70개의 서브에이전트, 90개의 슬래시 커맨드를 패키징하여, 에이전트를 전방위 소프트웨어 엔지니어링 시스템으로 전환하려는 거대 모놀리스 아키텍처

---

## 2. 구조 분석 (Architecture Breakdown)

```text
everything-claude-code/
├── agents/                          # 70+ 역할별 서브에이전트 프롬프트 (architect, reviewer 등)
├── commands/                        # 96+ 유저 진입점 슬래시 커맨드 (/tdd, /plan, /e2e 등)
├── skills/                          # 288+ 방대한 온디맨드 도메인 지식
├── rules/                           # 25개 언어/프레임워크별 모듈형 규칙 (common/, ts/, python/ 등)
├── hooks/
│   └── hooks.json                   # PreToolUse, PostToolUse, Stop, SessionStart 가로채기 맵
├── scripts/hooks/                   # Node.js 기반 런타임 훅 구현체
│   ├── config-protection.js         # • 린터/포맷터 설정 약화 차단
│   ├── stop-format-typecheck.js     # • Stop 시점 일괄 포맷팅 및 tsc
│   └── check-console-log.js         # • 잔여 console.log 경고
└── scaffolds/                       # 다중 에이전트 도구 설정 (.claude, .cursor, .codex 등)
```

---

## 3. 핵심 혁신 메커니즘

### 1. 런타임 생명주기 훅 (Runtime Lifecycle Hooks)
- Git 커밋 시점에만 개입하는 Git 훅과 달리, 에이전트의 도구 호출 직전(`PreToolUse`)과 발화 종료 직후(`Stop`)를 가로챔
- **`config-protection`** — 에이전트가 린트 에러를 무마하기 위해 `.eslintrc`, `.prettierrc`, `biome.json`을 수정하려는 순간 즉시 `exit 2`로 도구 실행을 취소
- **배치 포맷팅 & 타입체크** — 매 파일 수정마다 포맷터를 돌리지 않고, 모델이 응답을 마치는 `Stop` 이벤트 때 변경된 파일만 모아 일괄 포맷팅(Biome/Prettier)과 `tsc --noEmit` 수행

### 2. 언어 스택별 모듈식 규칙 격리
- `rules/`를 단일 파일로 두지 않고 `rules/typescript/`, `rules/python/`, `rules/golang/`으로 분리하여 프로젝트 언어에 맞춰 선택 적재

---

## 4. 장점 및 한계점 분석

### 장점 (배울 점)
- **설정 파일 방어벽** — 에이전트의 잔머리(린트 룰 끄기)를 시스템 레벨에서 원천 차단
- **배치 실행 효율** — 턴 진행 중 포맷터 실행 지연을 막고 `Stop` 시점에 한 번만 처리하는 최적화 패턴
- **보안 베이스라인** — 프롬프트 인젝션, 제로 너비 유니코드 트릭, 시크릿 유출 방지 조항이 훌륭하게 문서화됨

### 한계점 (반면교사)
- **극단적인 비대화 (Extreme Bloat)** — 스킬 288개, 패키지 락 10만 줄로 인해 개발자나 에이전트가 전체 구조를 파악하기 불가능 (Ponytail 관점의 안티패턴)
- **무거운 Node.js 의존성** — 훅 하나를 돌리기 위해 Node.js 프로세스를 띄워야 하므로 환경에 따라 훅이 깨질 위험 상존
- **설치의 복잡성** — 플러그인 설치와 규칙 복사가 분리되어 있어 멱등적 자동 배선에 실패

---

## 5. 적용 권장 대상

- 대규모 엔터프라이즈 환경에서 정밀한 감사와 생명주기 제어가 필요한 팀
- 복잡한 풀스택 언어군을 다루며 Claude Code 생태계에 깊이 종속된 프로젝트
