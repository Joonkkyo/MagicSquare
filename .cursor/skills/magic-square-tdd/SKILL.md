---
name: magic-square-tdd
description: MagicSquare_1004 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차
---

# magic-square-tdd

MagicSquare(4×4 부분 마방진, 10선=34) **Dual-Track TDD + ECB** 작업 시 이 Skill을 따른다. 헌법: 프로젝트 루트 `.cursorrules`. Test ID SSOT: [reference.md](reference.md).

## 언제 이 Skill을 켜는지

| 상황 | Skill 적용 |
|------|------------|
| `/tdd-red`, `/green-minimal`, `/red-skeleton`, `/refactor-safe` 등 TDD Command 사용 | **필수** |
| `tests/entity/test_d_*`, `tests/boundary/test_u_*` 작성·수정 | **필수** |
| `src/entity`, `control`, `boundary` 구현·리팩터 | **필수** |
| Mom Test·PRD·Report만 작성 (코드·pytest 없음) | 선택 |
| 일반 질문·문서만 | 불필요 |

작업 시작 시 **한 줄 선언:** `Phase: red|green|refactor` · `Layer: entity|control|boundary` · `Track: Logic|UI` · `Test ID: D-* 또는 U-*`

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| **Layer** | entity, control | boundary |
| **Test ID** | `D-*` | `U-*` |
| **디렉터리** | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| **파일명** | `test_d_*.py` | `test_u_*.py` |
| **Mock** | entity/control/domain **금지** | entity·control **Mock 허용** |
| **검증 초점** | 10선=34, 빈칸 좌표, 해 판정 | 입력 검증, E001~E007 표현, 출력 형식 |
| **RED 시 src/** | entity/control **수정 금지** | boundary **수정 금지** |

---

## ECB · Mock · 오류 코드

### 의존 방향

`boundary → control → entity` · **entity → 상위 import 금지**

### Mock

- **Logic:** `unittest.mock`, monkeypatch로 domain 함수 **대체 금지**
- **UI:** boundary 테스트에서 entity/control **stub·mock 허용** (I/O·에러 매핑 검증)

### E001~E007 (entity 금지 구간)

| 코드 | boundary | entity |
|------|----------|--------|
| E001~E005 | 처리·반환 | **raise/catch/매핑 금지** |
| E006~E007 | 사용자 메시지 매핑 | 판정 결과만 (emit) |

entity는 **순수 판정·풀이**만. `34`/`16` 리터럴 금지 → `entity.constants` SSOT.

---

## RED (5~7단계)

1. **선언** — Phase=red, Track, Layer, Test ID 1개(또는 RED 1묶음), PRD/C2C 확인 → [reference.md](reference.md)
2. **ID·경로** — `tests/entity/test_d_*.py` 또는 `tests/boundary/test_u_*.py` 확정
3. **AAA 설계** — Given(`grid_g1` 등 conftest) / When / Then (10선·1-index·E004 줄 식별)
4. **테스트만 작성** — `src/` **구현·수정 금지** · `pytest.fail("RED: …")` 스켈레톤 허용
5. **10선 체크** — 행·열·`\`·`/` 누락 없는지 설계표 점검 (Mom Test SC-1)
6. **pytest 실행** — 대상 파일/노드만 `-v` → **FAIL** traceback 캡처
7. **완료 보고** — (아래 보고 항목) FAIL 유형: ImportError / assert / RED fail

**금지:** skip, xfail, assert 삭제·완화로 FAIL 숨기기

---

## GREEN (5~7단계)

1. **선언** — Phase=green, 동일 Test ID(RED 1묶음)
2. **브랜치** — `green` 권장 (프로젝트 규약)
3. **최소 구현** — RED를 통과시키는 **최소** 코드만 `src/` 해당 Layer
4. **SSOT** — `MAGIC_CONSTANT` 등 constants 사용 · E001~E005 entity 처리 금지 유지
5. **pytest 실행** — 동일 테스트 노드 → **PASS**
6. **범위 검증** — Logic 전체 또는 `tests/entity/` 회귀 (선택)
7. **완료 보고** — PASS 로그 · 변경 파일 · 공개 API 1줄

**금지:** RED 묶음 밖 기능 선행 구현 · skip/xfail

---

## REFACTOR (5~7단계)

1. **선언** — Phase=refactor · **모든 관련 테스트 PASS 전제**
2. **스멜 탐지** — 중복(10선 합 등), 긴 함수, 책임 혼재 (분석만 가능)
3. **safe 변경** — 계약·golden·Test ID 동작 **불변**
4. **pytest** — `tests/entity/` (+ golden 노드) **전부 PASS**
5. **golden** — 변경 시 `UPDATE_GOLDEN=1` **의도적 1회만** · 임의 갱신 금지
6. **ECB 리뷰** — entity 상위 import 없음 · boundary에 도메인 규칙 누수 없음
7. **완료 보고** — 리팩터 요약 · pytest 결과 · golden matched/해당없음

**금지:** 동작 변경 · RED/GREEN 섞어 진행

---

## Test / Review Loop — pytest 언제 돌리는지

| 시점 | 명령 (프로젝트 루트) | 기대 |
|------|---------------------|------|
| RED 직후 | `python -m pytest <test_file>::<node> -v` | **FAIL** |
| GREEN 직후 | 동일 노드 `-v` | **PASS** |
| REFACTOR 후 | `python -m pytest tests/entity/ -v` | **PASS** |
| Harness 확인 | `python -m pytest tests/test_harness_ecb.py -v` | PASS (smoke) |
| UI Track RED | `python -m pytest tests/boundary/test_u_*.py -v` | FAIL → GREEN PASS |
| Golden (D-SOL 등) | `python -m pytest tests/entity/test_d_sol_01.py::<node> -v` | matched |
| Golden 갱신 (의도적) | `UPDATE_GOLDEN=1 python -m pytest …` | 1회만 |

**Review Loop (정적):** REFACTOR 전·후 `/review-ecb` — P0: entity E001~E005, entity→상위 import, Logic Mock, 34 리터럴 산재

---

## 완료 보고 항목 (매 Phase 종료 시)

1. **선언** — Phase / Layer / Track / Test ID
2. **파일** — 생성·수정 목록 (`tests/` vs `src/` 구분)
3. **pytest** — 명령줄 + exit code + passed/failed 수
4. **FAIL/PASS** — 핵심 traceback 1~3줄 또는 "matched"
5. **규칙 준수** — RED 시 src 미수정 / Mock / E001~E005 / 10선·1-index
6. **다음** — 다음 Test ID 1개 제안 (reference.md 기준)

---

## C2C · 10선 체크리스트 (RED 설계 시)

- [ ] PRD FR ↔ Test ID ↔ 함수명 연결
- [ ] Given: G1 `grid_g1` 또는 명시 격자
- [ ] Then: 10선 중 검증 대상 줄 명시 (`\`, `/` 포함)
- [ ] 실패 시 E004 + **줄 종류·인덱스** (Mom Test SC-2)
- [ ] 좌표 **1-index** (D-LOC, 출력 `int[6]`)

---

## 관련 파일

| 파일 | 역할 |
|------|------|
| `.cursorrules` | 도메인·ECB·TDD 헌법 |
| `docs/PRD.md` | FR-* · SC-* |
| [reference.md](reference.md) | Logic `D-*` ID 목록 |
| `tests/conftest.py` | `grid_g1` |
| `tests/_approval.py` | Golden Master |

**Command** (`/tdd-red` 등)는 별도 `.cursor/commands/` — 이 Skill은 절차 SSOT.
