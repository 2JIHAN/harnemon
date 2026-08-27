<div align="center">

# ⚡ HARNEMON (하네몬) ⚡

**The Pokémon-Style, Zero-Dependency Autonomous Harness Companion for AI Coding Agents**

<p align="center">
  <em>"글로벌 하네몬은 '종(Class)'이고, 프로젝트에 분양된 하네몬은 '지우의 피카츄(Instance)'다."</em>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#3-하네몬의-3대-불변식-3-invariants)
[![Shell: POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#architecture)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#2-하네몬의-3대-기둥-3-pillars)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#5-자가-진화-엔진-powered-by-hermes--grok-bot)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (Class / Species)                       │
       │   ~/.harnemon/ (루티스, 바스티온, 아이로닉, 야그니 종족 원형)│
       └──────────────────────────────────────────────────────────────┘
                                      │
                   harnemon adopt     │  (분양 / 인스턴스화)
                                      ▼
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (Instance / Individual)                │
       │   /my-project/.agents/ (이 레포에 특화되어 진화하는 내 파트너)│
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 핵심 사상: 클래스(Class)와 인스턴스(Instance)

기존의 AI 하네스는 프로젝트마다 똑같은 텍스트 프롬프트를 복붙하거나, 무거운 패키지를 중복 설치하는 비효율에 갇혀 있었습니다. **`Harnemon(하네몬)`은 객체지향의 클래스와 인스턴스, 그리고 포켓몬의 '종'과 '개체' 개념으로 이 문제를 완벽히 해결합니다.**

### 1. 글로벌 하네몬은 '종 (Species / Class)'입니다
- 트레이너(개발자)의 글로벌 홈(`~/.harnemon`)에 상주하는 원형 클래스입니다.
- 포켓몬 세계에 **피카츄, 파이리, 꼬부기**라는 종이 존재하듯, 글로벌 하네몬은 **기본 DNA(규칙, 스킬, 훅의 설계도)**를 보관합니다.
- 특정 프로젝트의 코드나 의존성에 오염되지 않는 순수한 마스터 카탈로그입니다.

### 2. 프로젝트에 분양된 하네몬은 '개체 (Individual / Instance)'입니다
- 개발자가 특정 프로젝트 폴더에서 `harnemon adopt`를 실행하면, 글로벌 종의 DNA를 물려받은 **단 하나의 독립된 하네몬 개체**가 해당 레포지토리에 분양됩니다.
- 마치 전 세계 수많은 피카츄 중 **'지우의 피카츄'**가 지우와 모험하며 번개 기술을 연마하듯, 분양된 하네몬은 **그 프로젝트의 코드베이스, 도메인 규칙, 팀 컨벤션, 버그 히스토리를 먹고 자라며 독자적으로 진화(Self-Evolution)**합니다.
- **프로젝트 무의존성 (Zero Footprint)**: 프로젝트의 `package.json`, `Cargo.toml`, `pyproject.toml`에 단 1줄의 외부 패키지도 요구하지 않으며, 오직 순수 POSIX Bash와 Git 표준 도구로 0ms만에 구동됩니다.

---

## 📖 하네덱스 (Harnedex) — 전설의 4대 하네몬 종족

`Harnemon`은 서로 다른 엔지니어링 철학을 대표하는 4대 전설의 하네몬 종족을 내장하고 있습니다. 프로젝트 성격에 맞춰 원하는 종족을 분양받을 수 있습니다.

| 번호 | 종족명 | 타입 | 상징 아키텍처 | 종족 특성 및 핵심 기술 |
| :---: | :--- | :--- | :--- | :--- |
| **No.001** | **[루티스 (Routis)](docs/case-studies/01-jihan-harness.md)** | `민첩 / 강철` | `2JIHAN/jihan-harness` | **특성: 경량화 (Lightweight)**<br>상시 컨텍스트를 50토큰으로 묶어두는 스킬 라우터 장착. 불필요한 코드를 날카롭게 베어내는 미니멀 종족 |
| **No.002** | **[바스티온 (Bastion)](docs/case-studies/02-everything-claude-code.md)** | `바위 / 드래곤` | `affaan-m/everything-claude-code` | **특성: 설정 수호 (Config Guard)**<br>288개 기술을 지닌 거대 요새. 린트/포맷터 설정을 약화하려는 잔머리를 0초 만에 물리 차단하는 수호 종족 |
| **No.003** | **[아이로닉 (Ironik)](docs/case-studies/03-obra-superpowers.md)** | `격투 / 에스퍼` | `obra/superpowers` | **특성: 근본 간파 (Root Seeker)**<br>The Iron Law(철칙) 수련생. 원인을 완벽히 규명하기 전에는 단 한 줄의 코드도 수정하지 않는 디버깅 종족 |
| **No.004** | **[야그니 (Yagni)](docs/case-studies/04-dietrich-ponytail.md)** | `노말 / 풀` | `DietrichGebert/ponytail` | **특성: 게으름의 사다리 (Ladder of Laziness)**<br>가장 짧은 코드로 문제를 해결하는 나무늘보. 복잡성을 삭제하고(`-N lines`) 지름길 부채를 수확하는 다이어트 종족 |

---

## 🏛️ 하네몬의 3대 기둥 (The 3 Pillars)

모든 하네몬은 단일 프롬프트 파일에 의존하지 않고, 완벽히 직교하는 3대 기둥으로 신체를 구성합니다.

```text
       ┌──────────────────────────────────────────────────┐
       │                 하네몬의 신체 구조                │
       └──────────────────────────────────────────────────┘
             │                  │                  │
             ▼                  ▼                  ▼
      [ 기둥 1: Rule ]   [ 기둥 2: Skill ]   [ 기둥 3: Hook ]
      • 본능 & 특성       • 습득 기술머신     • 물리 지닌물건
      • 상시 인지 제약    • 온디맨드 전문역량 • Git 하드 게이트
      • (~50토큰 라우터)  • (100~500줄 매뉴얼)• (exit 0 / exit 1)
```

1. **특성 (Ability) ➔ `rules/` (상시 규칙)**: 매 턴 모델의 눈앞에 상주하는 최소한의 표현 및 행동 제약 (`fluent-korean`, `task-execution-protocol`, `skill-routing`)
2. **기술 (Moves) ➔ `skills/` (온디맨드 역량)**: 특정 작업(디버깅, 리팩터링, 문서화) 시에만 호출되는 전문 플레이북 (`ponytail`, `systematic-debugging`, `writing-docs`)
3. **지닌물건 (Held Items) ➔ `hooks/` (물리 게이트)**: 모델의 지능을 맹신하지 않고, 커밋 메시지 위반이나 설정 약화를 OS/Git 레벨에서 차단하는 결정론적 방패 (`commit-msg`, `pre-commit`)

---

## 🔒 3대 불변식 (The 3 Invariants)

Harnemon 생태계의 모든 도구와 룰은 다음 3가지 시스템 불변식을 영구히 준수합니다.

- **1. 멱등성 (Idempotency)** — `harnemon adopt`를 1번 실행하든 100번 실행하든 최종 시스템 상태는 100% 동일합니다.
- **2. 자동 배선 (Auto-wiring)** — 룰이나 스킬이 추가되면 `.agents/AGENTS.md` 및 AI 도구 설정에 0초 만에 자동 연결됩니다.
- **3. 제로 디펜던시 (Zero-dependency)** — `package.json`, `Cargo.toml`, `requirements.txt`에 의존성을 0바이트도 남기지 않습니다.

---

## ⚡ 빠른 시작 (Quickstart)

### 1. 트레이너 글로벌 도구 설치
```bash
# 글로벌 PATH에 harnemon CLI 심링크 등록
git clone https://github.com/2JIHAN/harnemon.git ~/.harnemon
ln -sf ~/.harnemon/bin/harnemon ~/.local/bin/harnemon
```

### 2. 프로젝트에 하네몬 분양받기 (`adopt`)
원하는 프로젝트 디렉터리로 이동하여 명령 한 줄로 하네몬을 분양합니다:
```bash
cd /path/to/my-project  # Rust, Go, Python, React, 빈 폴더 어디든 무관

# 글로벌 DNA를 연결하며 무의존성 방랑 모드로 분양 (권장)
harnemon adopt

# 또는 특정 전설의 종족(루티스, 바스티온 등)을 지정하여 분양
harnemon adopt routis
```

### 3. 내 하네몬 진단 및 도감 열람
```bash
# 1. 분양된 하네몬의 상태창 (특성, 배운 기술, 지닌물건)
harnemon status

# 2. 하네몬 건강 검진 (토큰 비대화, 규칙 결함 진단)
harnemon audit

# 3. 전설의 4대 하네몬 도감(Harnedex) 열람
harnemon dex
```

---

## 🧬 자가 진화 엔진 (Self-Evolution Loop)

분양된 하네몬은 트레이너와의 실전 코딩 세션을 거치며 스스로 진화합니다.

```text
[실전 코딩 세션] ──교정 2회 발생──▶ [패턴 포착] ──헤르메스식 합성──▶ [새로운 SKILL.md 자체 집필]
                                                                        │
[자가 진화 완료] ◀── mhm audit 자가 검진 ──◀── skill-routing 라우터 각인 ─┘
```

- **2회 반복의 법칙** — 트레이너가 특정 스타일이나 주의사항을 2번 이상 교정하면, 하네몬이 이를 포착하여 새로운 스킬 등록을 스스로 제안합니다.
- **자율 스킬 합성 (Hermes Closed Loop)** — 하네몬이 자신의 경험을 추상화하여 `.agents/skills/<신기술>/SKILL.md`를 자체 생성하고 라우터에 각인합니다.
- **크로스 프로젝트 역분양 (`sync`)** — 특정 프로젝트에서 연마한 훌륭한 신기술을 글로벌 마스터 도감으로 올려보내, 다른 모든 프로젝트의 하네몬에게 가르칠 수 있습니다:
  ```bash
  harnemon sync
  ```

---

## 📂 디렉터리 구조

```text
harnemon/
├── bin/
│   └── harnemon                             # 글로벌 트레이너 CLI
├── rules/                                   # [특성: 상시 규칙]
│   ├── fluent-korean.md                     # • 한국어 자연어 문맥 규약
│   ├── harness-evolution.md                 # • 하네몬 자가 진화 및 오너십 규약
│   ├── skill-routing.md                     # • 작업별 온디맨드 기술 라우팅
│   ├── task-execution-protocol.md           # • 태스크 착수·폴링차단·실측검증
│   └── terminal-response-format.md          # • 터미널/대화창 시각 레이아웃
├── skills/                                  # [기술: 온디맨드 역량]
│   ├── harness-evolution/                   # • 자율 스킬 합성 및 리팩터링 플레이북
│   ├── systematic-debugging/                # • 원인 규명 우선 4단계 디버깅
│   ├── ponytail/                            # • 미니멀 코딩 (게으름의 사다리)
│   ├── ponytail-review/                     # • diff 복잡성 사냥 리뷰
│   ├── ponytail-audit/                      # • 레포 전수 과잉 엔지니어링 감사
│   ├── ponytail-debt/                       # • 지름길 부채 장부 수확
│   ├── delegate-to-aside/                   # • Aside 브라우저 실시간 GUI 연동
│   ├── writing-docs/                        # • 영문 기술 문서 작성 표준
│   └── writing-docs-in-korean/              # • 국문 기술 문서 작성 표준
├── hooks/                                   # [지닌물건: 물리 게이트]
│   ├── commit-msg/                          # • 72자 제한 및 AI 서명 차단
│   └── pre-commit/                          # • 린터 설정 약화 및 시크릿 유출 차단
├── docs/                                    # [학문 체계 및 도감]
│   ├── what-is-a-harness.md                 # • 하네스의 정의와 프롬프트 한계
│   ├── maturity-model.md                    # • 하네스 발전 5단계 성숙도 모델
│   ├── three-pillars-and-invariants.md      # • 3대 기둥과 3대 불변식 설계론
│   └── case-studies/                        # • 전설의 4대 하네몬 도감 엔트리
└── README.md
```

---

## 📄 라이선스 (License)

Harnemon은 [MIT License](LICENSE) 하에 자유롭게 사용, 수정, 배포할 수 있습니다.
