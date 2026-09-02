# Incubation Kernel (상시 부화 감시 규칙)

- **경청 및 피드백 포착 (Active Listening)**: 사용자의 어투나 서식 지시, 라이브러리 선호, 아키텍처 원칙, 실수 교정 사항을 포착한다.
- **2회 교정 각인 규칙 (The 2-Correction Rule)**: 동일한 피드백이 2회 이상 관찰되면 3기둥으로 승격한다.
  - 상시 규칙 ➔ `rules/<name>.md` 생성 및 라우터 배선
  - 온디맨드 스킬 ➔ `skills/<name>/SKILL.md` 생성 및 `INDEX.md` 색인
  - 절대 차단 게이트 ➔ `hooks/` 스크립트 작성
- **부화 진척 고지 (Hatching Notice)**: 하네스에 새 지식을 반영할 때마다 턴 말미에 1줄로 고지한다 (`🌱 [하네몬 인큐베이팅] <내용> (부화도: N%)`).
