# TDD RED — 실패 테스트 먼저

MagicSquare_1004 **Dual-Track TDD** — **RED 단계만**. 구현(`src/`)은 건드리지 않고, pytest **FAIL**을 확인한다.

## 필수 선언

응답 **첫 줄**에 반드시 다음 형식으로 선언한다:

```text
Phase: red | Layer: entity|control|boundary | Track: Logic|UI | Test ID: D-* 또는 U-*
```

예:

```text
Phase: red | Layer: entity | Track: Logic | Test ID: D-LOC-01
```

- **Logic Track:** `tests/entity/test_d_*.py` 또는 `tests/control/`
- **UI Track:** `tests/boundary/test_u_*.py`
- 헌법: `.cursorrules` · 절차: Skill `magic-square-tdd` · D-* 목록: `reference.md`

## 절차

1. **ID 확인** — 이번 RED 1묶음의 Test ID 1개, PRD/C2C, 대상 파일 경로 확정
2. **AAA 설계** — Given (`grid_g1` 등) / When (호출) / Then (기대값·E004 줄·1-index)
3. **테스트 작성** — `tests/` **만** 수정 · `pytest.fail("RED: <Test ID> …")` 스켈레톤 허용
4. **10선 체크** — Logic이면 행·열·`\`·`/` 누락 없는지 (Mom Test SC-1)
5. **pytest FAIL** — 대상 노드만 실행, traceback 저장
6. **보고** — 아래 보고 항목 출력

## pytest 예시 (bash)

프로젝트 루트(`MagicSquare_XX/`)에서:

```bash
# Logic — D-LOC-01 예시
python -m pytest tests/entity/test_d_loc_01.py -v

# Logic — 특정 노드만
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v

# UI — U-IN-01 예시
python -m pytest tests/boundary/test_u_in_01.py -v

# 수집만 (파일 생성 직후)
python -m pytest tests/entity/test_d_val_03.py --collect-only
```

**기대:** exit code ≠ 0 · `FAILED` / `ImportError` / `pytest.fail` — **PASS면 RED 미완료**

## 보고

| 항목 | 내용 |
|------|------|
| **테스트 ID** | `D-*` 또는 `U-*` |
| **FAIL 요약** | 1~3줄 (assert 메시지 / ImportError / RED fail 문자열) |
| **변경 파일** | `tests/` 아래만 (경로 목록) |
| **pytest 명령** | 실행한 명령줄 + exit code |
| **다음** | GREEN 시 구현할 `src/` 함수 1줄 (제안만, 구현 금지) |

## 금지

- `src/` **구현 추가·수정** (entity / control / boundary 전부)
- **Logic Track**에서 entity·control **Domain Mock** (`unittest.mock`, monkeypatch 대체)
- `pytest.skip`, `xfail`, assert **삭제·완화**로 FAIL 숨기기
- RED 없이 GREEN 구현 · 여러 Test ID를 한 RED 묶음 없이 테스트만 양산
- `34`/`16` 리터럴을 테스트에 하드코딩 (필요 시 `entity.constants` 또는 fixture 상수)
