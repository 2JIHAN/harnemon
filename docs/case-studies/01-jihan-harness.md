# Harnedex No.001: Nimbleet (님블릿) — Electric Type ⚡
> **Archetype**: `2JIHAN/jihan-harness` | **Trait**: Lightning Router (50-token ultralight speedster)

린(Lean) 3기둥 구조, 50토큰 스킬 라우터 패턴, 그리고 제로 디펜던시 무결성을 구현한 현대적 미니멀 하네스의 원형이다.

---

## 1. 개요 및 설계 철학

- **저장소** — [github.com/2JIHAN/jihan-harness](https://github.com/2JIHAN/jihan-harness)
- **핵심 모토** — "군더더기 없는(Zero Fluff) 고밀도 실용 하네스"
- **설계 특성** — 방대한 수백 개의 기능을 욱여넣지 않고, 실제 코딩과 검증에 필수적인 정예 규칙과 스킬만을 3대 기둥으로 조립하여 극단적으로 가볍고 빠른 실행 속도를 유지

---

## 2. 구조 분석 (Architecture Breakdown)

```text
jihan-harness/
├── rules/                           # [기둥 1] 상시 적용 규칙 (초경량)
│   ├── fluent-korean.md             # • 한국어 자연어 문맥 규약
│   ├── skill-routing.md             # • 작업별 온디맨드 스킬 라우팅 테이블
│   ├── task-execution-protocol.md   # • 태스크 착수·폴링차단·실측검증 절차
│   └── terminal-response-format.md  # • 터미널/대화창 시각 레이아웃 규격
├── skills/                          # [기둥 2] 온디맨드 스킬 (정예 8종)
│   ├── systematic-debugging/        # • 원인 규명 우선 디버깅
│   ├── ponytail/                    # • 미니멀 코딩 (게으름의 사다리)
│   ├── ponytail-review/             # • diff 복잡성 사냥 리뷰
│   ├── ponytail-audit/              # • 레포 전수 과잉 엔지니어링 감사
│   ├── ponytail-debt/               # • 지름길 부채 장부 수확
│   ├── delegate-to-aside/           # • 브라우저 실시간 GUI 위임
│   ├── writing-docs/                # • 영문 기술 문서 작성 표준
│   └── writing-docs-in-korean/      # • 국문 기술 문서 작성 표준
├── hooks/                           # [기둥 3] 물리 하드 게이트 (Git Hooks)
│   ├── commit-msg/                  # • 72자 제한 및 AI 서명 차단
│   └── pre-commit/                  # • 린터 설정 약화 및 시크릿 유출 차단
├── install.sh                       # 멱등적 자동 배선 마스터 설치기
└── README.md
```

---

## 3. 핵심 혁신 메커니즘

### 1. 스킬 라우터 패턴 (Skill Dispatcher Pattern)
- **문제** — 상시 규칙(`rules/`)에 복잡한 가이드를 다 넣으면 토큰이 낭비되고, 스킬로만 빼두면 모델이 스킬을 읽지 않고 자의적으로 코딩을 진행함
- **해법** — `rules/skill-routing.md`에 단 50토큰 분량의 '작업별 신호등'만 상시 적재:
  - 코딩 착수 시 ➔ `ponytail` 스킬 필수 로드
  - 버그 발생 시 ➔ `systematic-debugging` 스킬 필수 로드
  - 문서 작업 시 ➔ `writing-docs` 스킬 필수 로드
  - 복잡성 리뷰 시 ➔ `ponytail-review` 스킬 필수 로드
- **효과** — 상시 토큰 소모를 최소화하면서도, 모델이 중요한 순간에 스킬 매뉴얼을 반드시 읽고 실행하도록 100% 행동 유도

### 2. 제로 디펜던시 루트 클린 배선 (Zero-dependency & Clean Root)
- Node.js나 파이썬 등 외부 런타임 없이 **순수 POSIX Bash 스크립트**만으로 동작
- 프로젝트 루트를 어지럽히지 않고 `.agents/`에 격리한 뒤, `.claude/`와 `.gemini/` 등이 같은 원본을 참조하도록 자동 심링크 및 `@` 임포트 배선

---

## 4. 장점 및 배울 점 (Takeaways)

- **극도의 토큰 효율성** — 상시 주입되는 룰의 크기가 작아 모델의 주의력 저하가 전혀 발생하지 않음
- **물리 게이트의 실효성** — 모델이 린트 에러를 피하기 위해 `.eslintrc`를 건드리거나 커밋 메시지에 AI 티를 내는 행위를 0ms만에 차단
- **범용 호환성** — Claude Code, Cursor, Antigravity, Gemini CLI 등 모든 에이전트 환경에서 동일하게 작동

---

## 5. 적용 권장 대상

- 빠르고 가벼운 턴 속도를 원하는 1인 개발자 및 스타트업
- 상시 프롬프트 토큰 비용을 최소화하고 싶은 조직
- 순수 Git 표준 워크플로를 준수하고자 하는 팀
