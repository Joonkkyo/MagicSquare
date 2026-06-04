# TODO_RED — RED 단계 선행 · 실행 체크리스트

> **목적:** `/tdd-red`·`/red-skeleton`에 들어가기 **전**(Ask·설계)과 RED **실행** 시 해야 할 일을 한곳에서 추적한다.  
> **SSOT:** `.cursorrules` · Skill `magic-square-tdd` · [reference.md](.cursor/skills/magic-square-tdd/reference.md)  
> **참고 설계:** [MagicSquare_1004 Report/03](../src/MagicSquare_1004/Report/03.MagicSquare_Session4_RED_TestPlan_Report.md) (`/red-test-plan` 산출)

**마지막 갱신:** 2026-06-04

---

## 0. RED 선행 vs RED 실행

| 구분 | Command / 단계 | 산출물 | `src/` 수정 |
|------|----------------|--------|-------------|
| **선행 (Ask)** | Mom Test · PRD · `/red-test-plan` | 설계표 · C2C · pytest 계획 | **금지** |
| **실행** | `/red-skeleton` → `/tdd-red` | `tests/`만 · pytest **FAIL** | **금지** |
| **다음** | `/green-minimal` | 최소 구현 | 허용 |

---

## 1. 프로젝트 기반 (RED 전체 공통)

Harness·규칙이 없으면 RED 설계·FAIL 검증이 성립하지 않는다.

### 1.1 도메인 · 문서

- [x] Mom Test · 진질 문제 한 문장 ([README.md](README.md))
- [ ] `docs/PRD.md` (로컬 SSOT) — 현재 [1004 PRD](../src/MagicSquare_1004/docs/PRD.md) 참조만
- [ ] `Report/01` — 문제 정의 보고서 (로컬)
- [x] 도메인 규약: 4×4 · 빈칸 2 · 10선=34 · 출력 `int[6]` **1-index** (`.cursorrules`)

### 1.2 Cursor · ECB Harness

- [x] `.cursorrules` (ECB · Dual-Track · E001~E007)
- [x] Skill `magic-square-tdd` + `reference.md` (Logic `D-*` 7개)
- [x] Command `/tdd-red`, `/review-ecb`
- [ ] Command `/red-test-plan`, `/red-skeleton` (1004에 있음 · XX 미추가)
- [x] `pyproject.toml` · `pythonpath = ["src"]`
- [x] ECB 골격: `src/{entity,control,boundary}/`, `tests/{entity,control,boundary}/`
- [x] `src/entity/constants.py` (MAGIC_CONSTANT 등 SSOT)
- [x] `tests/conftest.py` — fixture `grid_g1` (G1, 빈칸 1-index `(2,3)`, `(4,4)`)
- [x] `tests/test_harness_ecb.py` (smoke 4건 — venv·`pip install -e ".[dev]"` 후 실행)
- [x] `tests/_approval.py` · `tests/golden/` (Golden Master 준비)

### 1.3 개발 환경

- [ ] venv 생성 · `pip install -e ".[dev]"`
- [ ] `python -m pytest tests/test_harness_ecb.py -v` → **4 passed** 확인

---

## 2. RED 묶음 1건당 선행 (Ask · `/red-test-plan`)

**한 RED 묶음 = Test ID 1개**(또는 UI에서 명시한 2 ID 묶음, 예: U-IN-01+02).  
아래를 **모두** 체크한 뒤 `/red-skeleton` 또는 `/tdd-red`로 넘긴다.

### 2.1 선언 · C2C

- [ ] 응답/보고 첫 줄: `Phase: red | Layer: … | Track: Logic|UI | Test ID: …`
- [ ] PRD `FR-*` ↔ Test ID ↔ 대상 함수명 연결
- [ ] To-Do 함수 시그니처·레이어 확정 (`entity` / `boundary.input` 등)
- [ ] **Given** — `grid_g1` 또는 명시 4×4 격자 (R-01~R-03)
- [ ] **When** — 호출 식 1개
- [ ] **Then** — 기대값 (좌표는 **1-index**, 상수는 `entity.constants` — `34`/`16` 리터럴 금지)

### 2.2 Track별 설계표

**Logic (`D-*`)**

- [ ] RED 설계표: Test ID · 함수 · Given→Then · Invariant
- [ ] 10선 체크: 검증 대상이면 행·열·`\`·`/` 누락 없음 (Mom Test SC-1)
- [ ] entity **E001~E005 emit 금지** 확인
- [ ] Domain Mock **금지** 확인
- [ ] 테스트 파일 경로: `tests/entity/test_d_<id>.py` · 함수명 `test_d_*`
- [ ] pytest 명령줄 확정 (노드 단위 `-v`)

**Boundary (`U-*`)**

- [ ] RED 설계표: Test ID · Given · Then · Expected RED Failure
- [ ] When 공통: `validate_input(grid)` (`boundary.input`) 등
- [ ] Then: `"E00x"` 문자열 · **control/entity 미호출** (GREEN에서 mock 검증)
- [ ] UI Track — control/entity **Mock 허용** 명시
- [ ] 테스트 파일: `tests/boundary/test_u_*.py`

### 2.3 금지 사항 (선행 단계에서도)

- [ ] `src/` 구현 추가·수정 없음
- [ ] GREEN / REFACTOR 혼입 없음
- [ ] `pytest.skip` / `xfail` / assert 완화 계획 없음

---

## 3. RED 묶음별 진행 상태

설계(선행) → 스켈레톤 → `/tdd-red` FAIL 순으로 표시한다.

### 3.1 Logic — D-LOC-01 (우선 묶음 · 설계 확정)

| 단계 | 항목 | 상태 |
|------|------|------|
| 선행 | C2C · AAA · G1→`[(2,3),(4,4)]` · [Report/03 D-LOC-01](../src/MagicSquare_1004/Report/03.MagicSquare_Session4_RED_TestPlan_Report.md) | [x] |
| 선행 | 10선: 해당 없음 (좌표만) | [x] |
| 선행 | pytest: `tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major` | [x] |
| 실행 | `tests/entity/test_d_loc_01.py` 스켈레톤 | [ ] |
| 실행 | pytest **FAIL** (exit ≠ 0) | [ ] |
| 다음 | `/green-minimal` → `entity.loc.find_blank_coords` | [ ] |

### 3.2 Boundary — U-IN-01 + U-IN-02 (2 ID 1 묶음)

| 단계 | 항목 | 상태 |
|------|------|------|
| 선행 | U-IN-01: `None` → `"E003"` | [x] |
| 선행 | U-IN-02: 3×3 → `"E001"` | [x] |
| 선행 | When: `validate_input(grid)` | [x] |
| 실행 | `tests/boundary/test_u_in_01.py`, `test_u_in_02.py` | [ ] |
| 실행 | pytest **FAIL** | [ ] |
| 다음 | `/green-minimal` → `boundary.input.validate_input` | [ ] |

### 3.3 Logic — D-VAL (Mom Test · 설계 예정)

권장 RED 순서: **D-VAL-03** → **D-VAL-05** → D-VAL-01/02/04 → D-SOL-01

| Test ID | PRD | 선행 설계표 | RED 실행 |
|---------|-----|-------------|----------|
| D-VAL-03 | FR-VAL-03 | [ ] | [ ] |
| D-VAL-05 | FR-VAL-05 | [ ] | [ ] |
| D-VAL-01 | FR-VAL-01 | [ ] | [ ] |
| D-VAL-02 | FR-VAL-02 | [ ] | [ ] |
| D-VAL-04 | FR-VAL-04 | [ ] | [ ] |
| D-SOL-01 | FR-SOL-01 | [ ] | [ ] |

### 3.4 Boundary — U-IN-03~05 · U-OUT (설계 예정)

| Test ID | PRD | 선행 설계표 | RED 실행 |
|---------|-----|-------------|----------|
| U-IN-03 | FR-IN-03 | [ ] | [ ] |
| U-IN-04 | FR-IN-04 | [ ] | [ ] |
| U-IN-05 | FR-IN-05 | [ ] | [ ] |
| U-OUT-01 | FR-OUT-01 | [ ] | [ ] |
| U-OUT-02 | FR-OUT-02 | [ ] | [ ] |

---

## 4. RED 실행 체크리스트 (`/red-skeleton` · `/tdd-red`)

선행(§2) 완료 후에만 진행.

- [ ] 수정 범위 **`tests/`만** (경로 목록 기록)
- [ ] Logic: Domain Mock·patch **미사용**
- [ ] 스켈레톤 허용 시 `pytest.fail("RED: <Test ID> …")` 또는 assert Then
- [ ] 대상 노드만 pytest `-v` 실행
- [ ] exit code ≠ 0 · FAIL traceback 1~3줄 보관
- [ ] PASS면 RED 미완료 — assert 완화·skip 금지
- [ ] 완료 보고: Phase/Layer/Track/Test ID · 명령줄 · 다음 GREEN 함수 1줄

---

## 5. C2C · 10선 빠른 점검 (Logic RED 설계 시)

Skill `magic-square-tdd` — RED 설계 시 매번 확인:

- [ ] PRD FR ↔ Test ID ↔ 함수명
- [ ] Given: `grid_g1` 또는 명시 격자
- [ ] Then: 10선 중 검증 줄 명시 (`\`, `/` 포함)
- [ ] 실패 시 boundary 관점 E004 + 줄 종류·인덱스 (Mom Test SC-2) — **entity emit 아님**
- [ ] 좌표 **1-index** (D-LOC, `int[6]`)

---

## 6. 권장 다음 작업 (한 번에 1묶음)

1. [ ] §1.3 venv · harness **4 passed**
2. [ ] §3.1 D-LOC-01 — `/red-skeleton` → `/tdd-red` → FAIL 로그
3. [ ] §3.2 U-IN-01/02 — boundary RED 스켈레톤 → FAIL
4. [ ] §3.3 D-VAL-03 — `/red-test-plan` AAA 작성 후 RED

---

## 7. 완료 정의 (RED 선행만)

다음이면 **해당 Test ID의 RED 선행(Ask) 완료**:

- §2 체크리스트 전부 [x]
- §3 해당 행 «선행» 열 [x]
- `src/` 미수정 · GREEN/REFACTOR 미착수

**RED 실행 완료**는 §4 + §3 «실행» 열 [x] + pytest FAIL 증거까지 포함한다.
