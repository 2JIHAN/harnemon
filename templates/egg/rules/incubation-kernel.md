# Incubation Kernel (상시 부화 감시 규칙)

- **경청 및 피드백 포착 (Active Listening)**: 사용자의 어투/서식 지시, 라이브러리 선호, 아키텍처 원칙, 실수 교정 사항을 포착함.
- **2회 교정 각인 규칙 (The 2-Correction Rule)**:
  - 동일한 피드백이나 지침이 2회 이상 관찰되면 즉시 `memory/incubation-log.md`에 기록하고 EXP를 갱신하며 3기둥(Rule, Skill, Hook)으로 승격함.
  - 상시 규칙 ➔ `rules/<name>.md` 생성 및 라우터 배선
  - 온디맨드 스킬 ➔ `skills/<name>/SKILL.md` 생성 및 `INDEX.md` 색인
  - 절대 차단 게이트 ➔ `hooks/` 스크립트 작성
- **부화 진척 고지 (Hatching Notice)**: 새로운 지식을 학습하여 하네스에 반영할 때마다 턴 말미에 1줄 고지 (`🌱 [하네몬 인큐베이팅] <내용> (부화도: N%)`).
