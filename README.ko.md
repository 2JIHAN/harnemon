<div align="center">

# ⚡ HARNEMON (하네몬) ⚡

**포켓몬 스타일의 AI 코딩 에이전트 전용 제로 디펜던시 자율 하네스 컴패니언**

<p align="center">
  <em>"전역 하네몬은 클래스(종/Species)이고, 프로젝트 하네몬은 인스턴스('지우의 피카츄')입니다."</em>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> •
  <a href="README.ko.md"><b>한국어</b></a> •
  <a href="README.ja.md"><b>日本語</b></a> •
  <a href="README.zh-CN.md"><b>简体中文</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#-3대-불변식)
[![Runtime: Pure POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#-3대-불변식)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#-3대-기둥)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#-자율-진화--인큐베이팅-엔진)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (Class / 종 청사진)                     │
       │   ~/.harnemon/ (Nimbleet, Fortoise, Monkin, Yagni 청사진)    │
       └──────────────────────────────────────────────────────────────┘
                    │                                 ▲
     harnemon adopt │                                 │ harnemon register
                    ▼                                 │
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (Instance / 살아있는 파트너)           │
       │   /my-project/.harnemons/ (분양받거나 부화한 하네몬 파트너)  │
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 핵심 철학: 클래스 vs 인스턴스 & 인큐베이터

기존 AI 하네스는 수백 줄짜리 거대한 프롬프트 덩어리를 복사해 붙여넣거나, 무거운 npm/pip 패키지로 프로젝트를 오염시켰습니다. **하네몬은 객체 지향 프로그래밍의 클래스(Class)와 인스턴스(Instance) 개념, 그리고 포켓몬 설정을 결합하여 이 문제를 명쾌하게 해결합니다.**

### 1. 전역 하네몬은 클래스 (종 / Species)
- 개발자의 전역 벨트인 `~/.harnemon`에 상주합니다.
- **피카츄, 꼬부기, 파이리, 이상해씨**가 고유한 종의 유전자 청사진이듯, 전역 하네몬은 개별 프로젝트에 오염되지 않은 순수한 **3기둥 DNA(규칙, 스킬, 훅 아키텍처)**를 보관합니다.

### 2. 프로젝트 하네몬은 인스턴스 ('지우의 피카츄')
- 임의의 저장소에서 `harnemon adopt`를 실행하면 해당 워크스페이스에 결속된 **고유하고 살아있는 하네몬 인스턴스**가 생성됩니다.
- **지우의 피카츄**가 지우와 함께 여행하며 독창적인 전투 기술을 습득하듯, 분양된 하네몬은 **해당 레포지토리의 도메인 규칙, 아키텍처 특성, 버그 해결 내역을 스스로 흡수하여 자율 진화(Self-Evolution)**합니다.
- **제로 디펜던시 무결성**: `package.json`, `Cargo.toml`, `pyproject.toml`에 **0바이트**의 흔적도 남기지 않습니다. 순수 POSIX Bash와 표준 Git만으로 완결 동작합니다.

### 3. 하네몬 인큐베이터 (빈 알 🥚)
- 미리 만들어진 규칙이 부담스럽다면 `harnemon incubate`로 **완전 빈 알(Blank Egg)**에서 시작할 수 있습니다.
- 코딩 세션을 진행하며 피드백(2회 교정 규칙)을 주면, 알이 3기둥 규칙과 스킬을 스스로 합성하며 경험치(EXP)를 쌓습니다.
- 부화 준비가 완료되면 `harnemon hatch <종이름>`으로 성체 종을 탄생시키고, `harnemon register`로 전역 하네덱스에 등재할 수 있습니다.

---

## 📖 하네덱스 (Harnedex) — 1세대 4대 전설의 아키타입

클래식 1세대 스타팅 포켓몬에서 영감을 얻은 4대 정예 하네몬 종입니다:

| No. | 종 (Species) | 속성 (Type) | 현실 기반 원형 | 핵심 특성 및 보유 기술 |
| :---: | :--- | :--- | :--- | :--- |
| **No.000** | **[하네몬 알](docs/harnemon-incubator.md)** | `Incubating 🌱` | `Harnemon Incubator` | **특성: 빈 도화지 (Blank Canvas)**<br>사전 규칙이 없는 0-Rule 스타터입니다. 개발자의 코딩 습관과 2회 교정 피드백을 스스로 학습하여 고유한 종으로 부화합니다. |
| **No.001** | **[님블리트 (Nimbleet)](docs/case-studies/01-jihan-harness.md)** | `Electric ⚡` | `2JIHAN/jihan-harness` | **특성: 번개 라우터 (Lightning Router)**<br>초고속 50토큰 스킬 라우터. 번개 같은 응답 속도, 제로 디펜던시 루트 클린 기동. |
| **No.002** | **[포토이즈 (Fortoise)](docs/case-studies/02-everything-claude-code.md)** | `Water 💧` | `affaan-m/everything-claude-code` | **특성: 쉘 가디언 (Config-Guard Shell)**<br>288개 기술의 거대 요새. AI가 린터/포맷터 설정을 임의로 약화시키는 시도를 원천 물리 차단. |
| **No.003** | **[몽킨 (Monkin)](docs/case-studies/03-obra-superpowers.md)** | `Fire 🔥` | `obra/superpowers` | **특성: 철칙의 도가니 (The Iron Law Crucible)**<br>엄격한 *The Iron Law* 규율. 추측 코딩을 불태우고 원인 증명 전까지 코드 수정을 철저히 금지. |
| **No.004** | **[야그니 (Yagni)](docs/case-studies/04-dietrich-ponytail.md)** | `Grass 🍃` | `DietrichGebert/ponytail` | **특성: 게으름의 사다리 (Ladder of Laziness)**<br>군더더기를 쳐내는 천재 게으름뱅이. 불필요한 코드 삭감(`-N줄`), 표준 라이브러리 우선, 부채 장부화. |

---

## 🏛️ 3대 기둥 (The 3 Pillars)

하네몬의 신체 구조는 방대한 단일 프롬프트 대신 서로 직교하는 **3대 공학적 기둥**으로 조립됩니다:

```text
       ┌──────────────────────────────────────────────────┐
       │                 하네몬 신체 구조                 │
       └──────────────────────────────────────────────────┘
             │                  │                  │
             ▼                  ▼                  ▼
      [ 기둥 1: Rule ]   [ 기둥 2: Skill ]  [ 기둥 3: Hook ]
      • 상시 특성 (Abilities) • 보유 기술 (Moves)  • 장착 도구 (Held Items)
      • 상시 인지 제약   • 온디맨드 전문 역량 • 물리 하드 게이트
      • (~50토큰 허브)   • (상세 매뉴얼)      • (exit 0 / exit 1)
```

1. **상시 특성 (`rules/`)**: 매 대화 턴마다 주입되는 최소한의 제약 (`fluent-korean`, `task-execution-protocol`, `skill-routing`).
2. **보유 기술 (`skills/`)**: 특정 작업이 발생했을 때만 모델이 온디맨드로 로드하는 실전 매뉴얼 (`ponytail`, `systematic-debugging`, `writing-docs`).
3. **장착 도구 (`hooks/`)**: 모델의 자의적 판단을 믿지 않고, OS/Git 런타임에서 결정론적으로 위반을 차단하는 스크립트 (`commit-msg`, `pre-commit`).

---

## 🔒 3대 불변식 (The 3 Invariants)

하네몬의 모든 도구와 규칙은 아래 3가지 시스템 불변식을 100% 준수합니다:

- **1. 멱등성 (Idempotency)** — `harnemon adopt`를 1번 실행하든 100번 실행하든 시스템의 최종 상태는 항상 동일합니다.
- **2. 자동 배선 (Auto-wiring)** — 새로 습득한 기술이나 규칙은 `.agents/AGENTS.md` 및 AI 클라이언트 설정(`.claude`, `.gemini`)에 즉시 자동 연결됩니다.
- **3. 제로 디펜던시 (Zero-dependency)** — Node.js, Python, Cargo 등 외부 런타임 패키지에 의존하지 않고 오직 Bash와 Git만으로 구동됩니다.

---

## ⚡ 빠른 시작 (Quickstart)

### 1. 전역 도구 설치
```bash
# 전역 벨트에 클론 후 PATH 심링크 연결
git clone https://github.com/2JIHAN/harnemon.git ~/.harnemon
ln -sf ~/.harnemon/bin/harnemon ~/.local/bin/harnemon
```

### 2. 스타팅 하네몬 분양 또는 빈 알 인큐베이팅
원하는 프로젝트 폴더로 이동합니다:
```bash
cd /path/to/my-project

# 방법 A: 완전 빈 알에서 시작 (인큐베이팅 모드 — 코딩하며 자율 진화):
harnemon incubate

# 방법 B: 대화형 오키드 박사 스타팅 선택 다이얼로그:
harnemon adopt

# 방법 C: 특정 종 직접 분양:
harnemon adopt nimbleet   # 전기 타입 ⚡ (초경량 스킬 라우터)
harnemon adopt fortoise   # 물 타입 💧   (설정 방어 요새)
harnemon adopt monkin     # 불 타입 🔥   (The Iron Law 디버깅)
harnemon adopt yagni      # 풀 타입 🍃   (게으름의 사다리)
```

### 3. 성체 부화 및 전역 하네덱스 등록
인큐베이팅된 알이 성숙도에 도달하면:
```bash
# 고유한 성체 종으로 공식 부화:
harnemon hatch "Supabird" --type "Database ⚡" --desc "Supabase RLS & Edge Function Master"

# 전역 하네덱스에 등록하여 다른 모든 프로젝트에서도 분양 가능하도록 저장:
harnemon register
```

### 4. 파트너 상태 및 건강 진단
```bash
# 1. 분양된 파트너 프로필 또는 알 부화 진척도 확인
harnemon status

# 2. 토큰 건전성, 룰 비대화, 훅 실행 권한 정밀 진단
harnemon audit

# 3. 전설의 하네덱스 아키타입 및 커스텀 종 도감 열람
harnemon dex
```

---

## 🧬 자율 진화 & 인큐베이팅 엔진

입양된 하네몬은 정적으로 멈춰있지 않고, 함께 코딩하는 과정에서 지속적으로 진화합니다:

```text
[코딩 세션] ──2회 반복 교정──▶ [패턴 감지] ──Hermes 루프──▶ [자율 SKILL.md 작성]
                                                                        │
[진화 완료] ◀── 헬스 체크 감사 ◀── skill-routing.md 자동 배선 ─────────┘
```

- **2회 교정 각인 규칙 (The 2-Correction Rule)**: 개발자가 특정 스타일이나 컨벤션을 2번 이상 교정하면 하네몬이 이를 즉시 감지하여 룰화합니다.
- **Hermes 자율 합성**: 해결책을 추상화하여 `skills/<new-move>/SKILL.md`를 스스로 작성합니다.
- **상호 수분 (`sync`)**: 프로젝트 A에서 새로 습득한 기술을 전역 벨트로 동기화하여 다른 레포의 하네몬에게도 전파할 수 있습니다:
  ```bash
  harnemon sync
  ```

---

## 📂 저장소 구조

```text
harnemon/
├── bin/
│   └── harnemon                             # 전역 트레이너 CLI
├── rules/                                   # [상시 특성: Rule]
│   ├── fluent-korean.md                     # • 자연스러운 한국어 소통 규칙
│   ├── harness-evolution.md                 # • 자율 진화 및 하네스 소유권 규칙
│   ├── skill-routing.md                     # • 50토큰 스킬 신호등 라우터 허브
│   ├── task-execution-protocol.md           # • 태스크 사이징, 안티폴링, 실측검증
│   └── terminal-response-format.md          # • 터미널 시각 레이아웃 표준
├── skills/                                  # [보유 기술: Skill]
│   ├── harness-evolution/                   # • 자율 스킬 합성 및 라우터 플레이북
│   ├── systematic-debugging/                # • 근본 원인 추적 4단계 디버깅
│   ├── ponytail/                            # • 미니멀 코딩 & 게으름의 사다리
│   ├── ponytail-review/                     # • diff 복잡도 사냥 리뷰
│   ├── ponytail-audit/                      # • 전체 리포 코드 군더더기 감사
│   ├── ponytail-debt/                       # • 지연된 숏컷 부채 장부 수확
│   ├── delegate-to-aside/                   # • Aside AI 브라우저 GUI 위임
│   ├── writing-docs/                        # • 영문 기술 문서 작성 표준
│   └── writing-docs-in-korean/              # • 국문 기술 문서 작성 표준
├── hooks/                                   # [장착 도구: Hook]
│   ├── commit-msg/                          # • 72자 제한 및 AI 서명 차단 게이트
│   └── pre-commit/                          # • 설정 약화 및 시크릿 유출 차단 게이트
├── templates/                               # [템플릿 및 인큐베이터]
│   └── egg/                                 # • 제로 베이스 빈 알 스타터
├── docs/                                    # [하네덱스 및 이론]
│   ├── what-is-a-harness.md                 # • 하네스의 정의 및 프롬프트와의 차이
│   ├── maturity-model.md                    # • 하네스 5단계 성숙도 모델
│   ├── three-pillars-and-invariants.md      # • 3대 기둥 및 3대 불변식 설계론
│   ├── harnemon-incubator.md                # • 인큐베이터 및 부화 시스템 상세 가이드
│   └── case-studies/                        # • 하네덱스 아키타입별 상세 분석집
└── README.md
```

---

## 👥 기여자 (Contributors)

하네몬(Harnemon) 생태계에 기여해 주신 모든 분들께 감사드립니다:

<a href="https://github.com/2JIHAN/harnemon/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=2JIHAN/harnemon" alt="Harnemon Contributors" />
</a>

버그 수정, 신규 하네몬 종(Species) 제출, 문서 개선 등 모든 기여를 환영합니다! 기여 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해 주세요.

---

## 📄 라이선스

Harnemon은 [MIT 라이선스](LICENSE) 하에 오픈소스로 공개되어 있습니다.
