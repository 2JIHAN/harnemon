# 하네몬 파티 시스템 (Harnemon Party System)

단일 하네몬 운영을 넘어, 한 프로젝트 내에 **최대 6마리의 전문 하네몬으로 팀을 구성**하여 작업 성격에 따라 선발 파트너를 교체하거나 서브에이전트에게 역할을 위임하는 멀티 하네몬 아키텍처를 정의한다.

---

## 🌟 핵심 개념: 포켓몬 파티 & 전문 분업

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🐾 PROJECT HARNEMON PARTY (.harnemons/)                    │
       │   ├── ⚡ Nimbleet  (Active Lead: 50-token 빠른 기동 & 라우팅)│
       │   ├── 🔥 Monkin    (Specialist: The Iron Law 철칙 디버깅)    │
       │   ├── 🍃 Yagni     (Specialist: Ladder of Laziness 코드 삭감)│
       │   └── 💧 Fortoise  (Specialist: 린트/보안 방어 요새)         │
       └──────────────────────────────────────────────────────────────┘
```

- **선발 리드 (Active Lead)** — 평소 대화와 코딩 턴을 주도하며 턴 마지막에 고유 서명(`-하네몬 {이름} {아이콘}-`)을 출력
- **파티 멤버 (Party Members)** — 특정 난제(디버깅, 대규모 리팩토링, 배포 보안) 발생 시 교체 출전(`switch`)하거나 서브에이전트로 호출

---

## 🛠️ 파티 관리 CLI 명령어

### 1. 파티 현황 조회 (`party`)
현재 프로젝트에 영입된 하네몬 엔트리와 현재 선발 리드를 확인합니다:
```bash
harnemon party
```

### 2. 새 하네몬 영입 (`recruit`)
기존 설정을 덮어쓰지 않고 새로운 전문 하네몬을 파티 멤버로 추가합니다:
```bash
harnemon recruit monkin     # 몽킨 🔥 영입 (디버깅)
harnemon recruit yagni      # 야그니 🍃 영입 (코드 정리)
harnemon recruit fortoise   # 포토이즈 💧 영입 (보안/CI)
```

### 3. 선발 리드 교체 (`switch`)
작업 성격에 맞춰 현재 대화와 배선을 주도할 선발 하네몬을 즉시 전환합니다:
```bash
# 디버깅 세션 집중을 위해 몽킨으로 선발 전환:
harnemon switch monkin
# ➔ 이후 턴 메시지 끝에 -하네몬 몽킨 🔥- 서명 출력

# 코드 리팩토링을 위해 야그니로 선발 전환:
harnemon switch yagni
# ➔ 이후 턴 메시지 끝에 -하네몬 야그니 🍃- 서명 출력
```

### 4. 파티 멤버 방출 (`dismiss`)
더 이상 필요하지 않은 멤버를 파티에서 정리합니다:
```bash
harnemon dismiss fortoise
```

---

## 🔒 파티 시스템 불변식

1. **상시 격리성** — 각 하네몬은 `.harnemons/<species>/`에 자신의 3기둥(Rule/Skill/Hook)을 독립 격리 보관합니다.
2. **원클릭 배선 전환** — `harnemon switch` 한 번으로 `.agents/`와 AI 클라이언트 설정이 0초 만에 해당 하네몬으로 동기화됩니다.
3. **제로 디펜던시** — 파티 생성, 영입, 스위칭 모두 순수 POSIX Bash로 100% 동작합니다.
