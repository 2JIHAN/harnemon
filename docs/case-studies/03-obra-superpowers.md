# Harnedex No.003: Monkin (몽킨) — Fire Type 🔥
> **Archetype**: `obra/superpowers` | **Trait**: The Iron Law Crucible (Strict 4-step debugging)

증상 땜질을 불태우고 오직 근본 원인 규명과 재현 테스트 통과만을 허용하는 엄격한 수련형 하네스의 원형이다.

---

## 1. 개요 및 설계 철학

- **저장소** — [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **핵심 모토** — "No fixes without root-cause investigation first (원인 없는 땜질 금지)"
- **설계 특성** — 에이전트의 '추측 기반 코딩(Guess-and-check thrashing)'을 막기 위해, 문제 해결 과정을 엄격한 단계별 프로토콜로 강제하는 절차 중심 스킬 프레임워크

---

## 2. 구조 분석 (Architecture Breakdown)

```text
superpowers/
├── skills/
│   ├── systematic-debugging/        # • 4단계 원인 규명 우선 디버깅
│   │   ├── SKILL.md                 # • 본체 지침 (The Iron Law)
│   │   └── references/              # • 상황별 세부 디버깅 레퍼런스
│   ├── test-driven-development/     # • TDD 레드-그린-리팩터 사이클 강제
│   ├── verification-before-completion/ # • 증적 기반 완료 검증
│   └── architecture-decision-records/ # • ADR 문서화 스킬
└── commands/                        # 슬래시 커맨드 연동
```

---

## 3. 핵심 혁신 메커니즘

### 1. 디버깅 철칙 (The Iron Law of Debugging)
- **철칙** — **"근본 원인을 증명하기 전에는 단 한 줄의 수정 코드도 제안하거나 작성하지 않는다."**
- **4단계 절차 강제**
  1. **Phase 1 (원인 조사)** — 버그 재현, 스택 트레이스 정밀 추적, 실패하는 테스트 케이스 작성
  2. **Phase 2 (가설 검증)** — 1개 변수만 변경하며 가설 검증, 증거 없는 추측 배제
  3. **Phase 3 (최소 수정)** — 증상 땜질(예: 성급한 null 체크 추가) 금지, 근본 아키텍처 결함 수정
  4. **Phase 4 (회귀 검증)** — 전체 테스트 스위트 통과 실측 및 회귀 방지 테스트 추가

### 2. 증상 패치(Symptom Patching) 차단
- AI 에이전트가 흔히 저지르는 "에러 메시지를 없애기 위해 조건문으로 덮어씌우는 행위"를 금지 항목으로 명시하여 코드베이스 부패 방지

---

## 4. 장점 및 한계점 분석

### 장점 (배울 점)
- **품질의 신뢰성** — 에이전트가 섣부른 추측으로 멀쩡한 코드를 망가뜨리는 현상을 완벽히 근절
- **강력한 규율** — 실패하는 테스트 코드를 먼저 만들게 함으로써 TDD 원칙을 자연스럽게 내재화

### 한계점 (반면교사)
- **상시 주입 시 토큰 낭비** — 스킬 분량이 방대하여 상시 프롬프트로 넣을 경우 비용이 큼 (스킬 라우터를 통한 동적 호출이 필수적)
- **물리적 차단선 부족** — 순수 프롬프트 지침이므로, 모델이 극단적인 압박을 받을 때 스킬을 무시할 가능성이 남아있음

---

## 5. 적용 권장 대상

- 미션 크리티컬한 금융, 백엔드, 코어 인프라 시스템
- 버그 발생 시 정확한 원인 규명과 회귀 테스트 작성이 필수적인 프로젝트
