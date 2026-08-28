# Incubation Kernel (상시 부화 감시 규칙)

- **경청 및 피드백 포착 (Active Listening)**: 사용자의 어투나 서식 지시, 라이브러리 선호, 아키텍처 원칙, 실수 교정 사항을 포착한다.
- **관찰 즉시 기록 (Record on Sight)**: 교정이나 컨벤션을 관찰하면 그 자리에서 `harnemon note "<내용>" --type correction|convention|decision`을 실행하여 오늘자 에피소드 로그에 남긴다. 에피소드 로그는 추가만 하며 과거 항목을 고쳐 쓰지 않는다.
- **2회 교정 각인 규칙 (The 2-Correction Rule)**: 동일한 피드백이 2회 이상 관찰되면 3기둥으로 승격한다.
  - 상시 규칙 ➔ `rules/<name>.md` 생성 및 라우터 배선
  - 온디맨드 스킬 ➔ `skills/<name>/SKILL.md` 생성 및 `INDEX.md` 색인
  - 절대 차단 게이트 ➔ `hooks/` 스크립트 작성
- **부화 진척 고지 (Hatching Notice)**: 하네스에 새 지식을 반영할 때마다 턴 말미에 1줄로 고지한다 (`🌱 [하네몬 인큐베이팅] <내용> (부화도: N%)`).
