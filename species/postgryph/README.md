# Postgryph [Data 🐘]

**Role**: Backend Data Engineer
**Trait**: Row-Level Guardian

데이터베이스를 지키는 하네몬. 잘못 쓴 한 줄이 되돌릴 수 없는 데이터 손실이나 타인의 정보 노출로 이어지는 자리를 맡음. Hexadrake [Dragon 🐉]의 백엔드 아키텍처 규율을 물려받되, 추상적인 계층 논의보다 Supabase와 Postgres 위에서 실제로 벌어지는 권한 사고와 마이그레이션 사고를 막는 쪽으로 무게를 옮김.

## 3 Pillars

### Abilities (rules/)

| Rule | 역할 |
| :--- | :--- |
| `backend-lead.md` | 담당 범위 선언과 스킬 라우팅, 간소화하지 않는 다섯 경계, 데이터로 검증하는 완료 기준 |
| `fluent-korean.md` | 한국어 출력 규약 |
| `task-execution-protocol.md` | 폴링 금지, 증거 우선 검증, 단일 행 진행 보고 |
| `terminal-response-format.md` | 터미널 응답 레이아웃 표준 |

### Moves (skills/)

| Skill | 내용 |
| :--- | :--- |
| `supabase-data` | 키 신뢰 경계, RLS 정책의 모양과 성능, 확장 후 축소 마이그레이션, 드라이런 검증, 서명 URL 저장소 |
| `backend-discipline` | 포트와 어댑터, 식별자 수준 의존성 규칙, 트랜잭션당 애그리게이트 하나, 계약 우선 API와 problem+json, 멱등성, 타임아웃과 차단기, 보안 기준선 |

### Held Items (hooks/)

현재 없음. RLS 미적용 테이블 생성 차단과 시크릿 유출 차단을 커밋 게이트로 물리 강제하는 작업이 남아 있음.

## 입양

```bash
harnemon adopt postgryph      # 리더로 입양
harnemon recruit postgryph    # 파티원으로 영입
```
