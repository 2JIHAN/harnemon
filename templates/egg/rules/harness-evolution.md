# Self-Evolution & Ownership Protocol (자율 진화 규칙)

- **하네스 소유권 (Harness Ownership)**: 에이전트는 프로젝트 하네스(`.harnemons/`, `.agents/`)의 유지보수 주체로서 지속적으로 스스로의 룰과 스킬을 정제함.
- **관찰 즉시 기록 (Record on Sight)** — 교정, 컨벤션, 결정 사항을 관찰하면 그 자리에서 `harnemon note "<내용>" --type correction|convention|decision`을 실행하여 오늘자 에피소드 로그(`memory/episodes/`)에 남긴다. 에피소드 로그는 알과 성체를 가리지 않고 항상 유지하며, 추가만 하고 과거 항목은 고쳐 쓰지 않는다.
- **Hermes 자율 합성 (Autonomous Skill Synthesis)**:
  1. 반복 피드백 발생 시 `skills/<skill-name>/SKILL.md` 작성
  2. `skills/INDEX.md` 카탈로그 갱신
  3. 착수 조건이 명확한 스킬이라면 `rules/skill-routing.md`를 그때 신설하여 1줄짜리 신호등 트리거를 배선
- **빈 알 원칙 (Zero-Base Principle)**: 알은 학습 커널 외의 상시 룰을 미리 갖지 않음. 서식, 언어, 작업 절차 규약은 사용자 교정으로 습득한 뒤에만 `rules/`로 승격함.
- **상시 룰 다이어트**: 상시 `rules/` 파일은 항상 100줄 미만(50~100토큰)의 초경량 상태를 유지함.
- **문서 다국어화(i18n) 상시 기본**: 공개 문서 및 README 작성·수정 시 항상 4개 국어(EN, KO, JA, ZH) 세트를 원자적으로 동기화함.
