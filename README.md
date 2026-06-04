# MagicSquare_XX

4×4 **부분 마방진**(빈칸 2개) 과제에서 **10선(행·열·대각선) 합=34** 판정을 빠짐없이 검증하기 위한 TDD 프로젝트입니다.

> **Mom Test:** 빈칸 2개를 채운 뒤 행·열·대각선 합 확인에 시간이 많이 들고, 합이 34가 아닐 때 **어느 칸·어느 수정**이 틀렸는지 바로 알기 어렵다 → **기계적·재현 가능한 10선 판정**으로 바꾼다.

## 진짜 문제 (한 문장)

마지막에 10선 합이 34가 아니었을 때, **몇 번째로 수정한 칸에서 틀렸는지** 바로 알 수 없었고, 빈칸 2개를 채운 뒤 **행·열·대각선** 합을 손으로 확인하는 데 **시간이 많이 들었다**.

## 페르소나 · Mom Test 증거

| 항목 | 내용 |
|------|------|
| **페르소나** | 4×4 격자, 빈칸 2개(`0`), 1~16, 합 **34**를 맞추는 **학습자** |
| **증거 1** | 마지막으로 빈칸 2개를 채운 뒤 |
| **증거 2** | 행·열·대각선 합 확인에 **시간이 많이 든다** |
| **증거 3** | 합이 34가 안 맞을 때 **어느 칸·어느 수정**이 원인인지 특정하기 어렵다 |
| **표면 문제 (금지)** | 「검증/풀이 **프로그램**」·「PyQt **완성 앱**」을 만든다 — 솔루션 섞인 정의 |

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 빈칸 | **정확히 2개** (`0`) |
| 마법 상수 | **34** (= 4×(16+1)/2) |
| 검증 대상 | **10선** — 행 4 + 열 4 + `\` + `/` |
| 성공 출력 | `int[6]` → `[r1, c1, n1, r2, c2, n2]` (좌표 **1-index**) |

## 성공 기준 (Mom Test)

| ID | 기준 | Mom Test 연결 |
|----|------|---------------|
| SC-1 | **10선 합 전부** 계산·검증 (행·열만 X) | 확인 시간·누락 방지 |
| SC-2 | 한 줄이라도 ≠34 → **실패 + 깨진 줄 식별** | 어느 칸·수정 후보 좁히기 |
| SC-3 | 동일 유형에서 원인 특정 **1분 이내** | 수동 재검산 시간 절감 |

## 아키텍처

- **ECB:** `boundary → control → entity`
- **Dual-Track TDD:** Logic Track (`entity`, `control`) + UI Track (`boundary`)
- **RED 우선:** pytest FAIL 확인 → GREEN → REFACTOR

| Track | Layer | 테스트 ID | 디렉터리 | Mock |
|-------|-------|-----------|----------|------|
| Logic | entity, control | `D-*` | `tests/entity/`, `tests/control/` | Domain Mock **금지** |
| UI | boundary | `U-*` | `tests/boundary/` | entity/control Mock **허용** |

## 개발 환경

```powershell
Set-Location "c:\Users\usejen_id\study\CursorAI\src\MagicSquare_XX"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python -m pytest tests/ -v
```

| Phase | pytest 예시 |
|-------|-------------|
| entity 전체 | `python -m pytest tests/entity/ -v` |
| RED 1건 | `python -m pytest tests/entity/test_d_loc_01.py -v` |
| Golden (의도적 갱신만) | `UPDATE_GOLDEN=1 python -m pytest <대상> -v` |

## Cursor 워크플로 (세션 3+)

| Command | 역할 |
|---------|------|
| `/red-test-plan` | RED 설계표 · C2C · pytest 계획 |
| `/red-skeleton` | RED 스켈레톤 — `tests/`만 |
| `/tdd-red` | AAA 실패 테스트 → pytest FAIL |
| `/green-minimal` | RED 1묶음 최소 GREEN |
| `/golden-master` | Approval Test |
| `/refactor-smell` | 스멜 탐지 (분석만) |
| `/refactor-safe` | 구조 개선 (계약·golden 유지) |
| `/review-ecb` | ECB·계약 리뷰 |
| `/export-session` | Report · Transcript Export |

## 테스트 ID (C2C 요약)

| ID | PRD | 요약 | 상태 |
|----|-----|------|------|
| D-VAL-01~05 | FR-VAL-01~05 | 행·열·`\`·`/`·10선 합 = 34 | ⏳ |
| D-LOC-01 | FR-LOC-01 | 빈칸 2곳 좌표 (1-index) | ⏳ |
| D-SOL-01 | FR-SOL-01 | 빈칸 대입 풀이 | ⏳ |
| U-IN-01~05 | FR-IN-01~05 | 입력 검증 | ⏳ |
| U-OUT-01~02 | FR-OUT-01~02 | 성공/실패 출력 | ⏳ |

## 프로젝트 구조 (목표)

```
MagicSquare_XX/
├── .cursorrules
├── pyproject.toml
├── README.md
├── docs/PRD.md
├── Report/
├── Prompting/
├── .cursor/
├── src/entity|control|boundary/
└── tests/entity|control|boundary/
```

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | PRD (이 폴더에 작성 예정) |
| [Report/01](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test · R-G-I-O (작성 예정) |
| [MagicSquare_1004 PRD](../MagicSquare_1004/docs/PRD.md) | 참고 SSOT |
| [MagicSquare_1004 Report/01](../MagicSquare_1004/Report/01.MagicSquare_ProblemDefinition_Report.md) | 참고 Mom Test 보고서 |

## 범위

**In:** 4×4·빈칸 2·10선=34 · 깨진 줄 식별 · Dual-Track TDD · ECB · Cursor 워크플로

**Out:** PyQt 완성 앱·배포 · 3×3/5×5 · 수동 “대충 맞음”만으로 완료

## 에러 코드

| 코드 | 의미 | 담당 |
|------|------|------|
| E001 | 잘못된 격자 크기 | boundary |
| E002 | 빈칸 개수 ≠ 2 | boundary |
| E003 | Null / 범위 / 중복 | boundary |
| E004 | 줄 합 ≠ 34 | boundary |
| E005 | 입·출력 계약 위반 | boundary |
| E006 | 해 없음 | entity → boundary |
| E007 | 해 다중 | entity → boundary |

## 현재 상태 · 다음 단계

| 항목 | 상태 |
|------|------|
| README | ✅ |
| PRD · Report/01 · 코드 · 테스트 | ⏳ |

1. Mom Test → Report/01 · PRD  
2. 세션 3 — Rule · Command · Skill · Test Loop  
3. `/red-test-plan` → `/red-skeleton` → `/tdd-red`
