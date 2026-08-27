# ⚡ Harnemon (하네몬) ⚡

> **"포켓몬처럼 폴더에 알약(Pill)을 먹여 하네몬을 깨우고, 함께 코딩하며 진화시킨다."**
>
> *The Pokémon-Style Harness Companion System for AI Coding Agents*

`Harnemon(하네몬)`은 개발자와 엔지니어링 팀이 남의 하네스를 무비판적으로 복제하는 대신, **각자의 프로젝트와 Git 레포지토리에 꼭 맞는 3대 기둥(Rule, Skill, Hook) AI 동반 생명체를 깨우고, 훈련시키며, 진화시킬 수 있도록 돕는 메타 하네스 시스템**입니다.

---

## 1. 하네몬(Harnemon)의 세계관

- **알(Egg) 상태의 폴더** — 아무것도 없는 빈 Git 폴더는 잠들어 있는 무생물입니다.
- **하네스 알약(Pill) 투약** — 개발자가 이 폴더에 `harnemon feed`로 알약을 먹이면, 폴더는 자아를 가진 **하네몬(Harnemon)**으로 부화합니다.
- **하네몬의 3대 스펙**:
  - **특성 (Ability)** ➔ **`rules/` (상시 규칙)**: 패시브로 항상 켜져 있는 본능과 원칙
  - **기술머신 (Moves)** ➔ **`skills/` (온디맨드 역량)**: 필요할 때 꺼내 쓰는 전문 전투 기술
  - **지닌물건 (Held Items)** ➔ **`hooks/` (물리 게이트)**: 커밋 시 적(버그, 시크릿 유출, 린트 약화)의 침입을 0초 만에 튕겨내는 방어 아이템
- **자가 진화 (Evolution)** — 트레이너(개발자)의 세션 피드백을 먹고 스스로 하네스를 개선하여 메가진화합니다.

---

## 2. 하네덱스 (Harnedex) — 전설의 4대 하네몬 도감

| 번호 | 하네몬 이름 | 타입 | 상징 하네스 | 주요 특징 |
| :--- | :--- | :--- | :--- | :--- |
| **No.001** | **[루티스 (Routis)](docs/case-studies/01-jihan-harness.md)** | `민첩 / 강철` | `2JIHAN/jihan-harness` | 50토큰 스킬 라우터, 제로 디펜던시, 루트 클린 |
| **No.002** | **[바스티온 (Bastion)](docs/case-studies/02-everything-claude-code.md)** | `바위 / 드래곤` | `affaan-m/everything-claude-code` | 288개 기술 장착, 린트 설정 수호(Config Guard) |
| **No.003** | **[아이로닉 (Ironik)](docs/case-studies/03-obra-superpowers.md)** | `격투 / 에스퍼` | `obra/superpowers` | 철칙(The Iron Law)의 디버깅, TDD 연속 콤보 |
| **No.004** | **[야그니 (Yagni)](docs/case-studies/04-dietrich-ponytail.md)** | `노말 / 풀` | `DietrichGebert/ponytail` | 게으름의 사다리, 복잡성 삭제 베기, 지름길 부채 수확 |

---

## 3. 핵심 문서 체계 (`docs/`)

- **[`what-is-a-harness.md`](docs/what-is-a-harness.md)** — **하네스의 정의**
  - 프롬프트 vs 에이전트 vs 하네스의 차이 및 프롬프트 엔지니어링의 한계
- **[`maturity-model.md`](docs/maturity-model.md)** — **하네스 발전 5단계 성숙도 모델 (진화 트리)**
  - Level 0 (알) ➔ Level 1 (기본형) ➔ Level 2 (1진화) ➔ Level 3 (2진화 라우터) ➔ Level 4 (메가진화 자가 진화형)
- **[`three-pillars-and-invariants.md`](docs/three-pillars-and-invariants.md)** — **3대 기둥과 3대 불변식**
  - 특성(Rule), 기술(Skill), 지닌물건(Hook)과 멱등성, 자동 배선, 무의존성

---

## 4. 트레이너 CLI (`harnemon`)

```bash
# 1. 잠든 폴더에 알약을 먹여 하네몬 부화시키기
harnemon feed /path/to/my-repo

# 2. 하네몬 도감(Harnedex) 열람하기
harnemon dex

# 3. 하네몬 컨디션 진단 (토큰 비대화 및 규칙 결함 검진)
harnemon audit

# 4. 새로운 커스텀 하네몬 종족 스캐폴딩
harnemon init my-new-species
```

---

## 5. 글로벌 설치

```bash
# 로컬 PATH에 심링크 등록 (어디서나 harnemon 호출 가능)
ln -sf "$(pwd)/bin/harnemon" /usr/local/bin/harnemon
```
