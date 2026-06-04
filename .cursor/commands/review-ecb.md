# ECB · 계약 리뷰

MagicSquare_1004 **ECB·Dual-Track 계약** 정적 리뷰. **코드 수정 금지** — 위반만 표로 보고한다.

## 필수 선언

응답 **첫 줄**:

```text
Phase: review | Scope: src/ tests/ | Track: Logic|UI|both
```

예:

```text
Phase: review | Scope: src/entity tests/entity | Track: Logic
```

- 헌법: `.cursorrules`
- **Read/Grep만** 사용 · Write/Edit **금지**

## 절차

1. **범위 확인** — 리뷰 대상 경로 (`src/entity/`, `tests/boundary/` 등)
2. **5항목 점검** — 아래 체크리스트별 Read·Grep
3. **위반 표 작성** — 발견된 항목만 행 추가 · 없으면 `위반 없음`
4. **P0/P1 요약** — P0 = 반드시 수정 전 제거 · P1 = 권고
5. **보고** — 표 + 다음 액션 1줄 (구현은 하지 않음)

## 체크리스트 (5항목)

| # | 항목 | 기준 | 탐색 힌트 |
|---|------|------|-----------|
| 1 | **import 방향** | `boundary→control→entity` · **entity가 control/boundary import 금지** | `grep` `from boundary`, `from control` in `src/entity/` |
| 2 | **entity E001~E005** | entity에서 E001~E005 **raise/return/catch/문자열 처리 금지** | `grep` `E00[1-5]` in `src/entity/` |
| 3 | **int[6] 1-index** | 성공 출력 `[r1,c1,n1,r2,c2,n2]` · 좌표 **1-index** (0-index 혼용 금지) | `find_blank_coords`, solution 반환, 테스트 Then |
| 4 | **MagicConstant SSOT** | `34`/`16` 리터럴 **산재 금지** → `entity.constants` | `grep` `\b34\b`, `\b16\b` in `src/` `tests/` (constants·주석 제외 판단) |
| 5 | **Logic Domain Mock** | `tests/entity/`, `tests/control/`에서 entity·control **mock/patch 금지** | `grep` `@patch`, `MagicMock`, `monkeypatch` in `tests/entity/` |

추가 참고 (표에 넣을 때 P1):

- `pytest.skip` / `xfail` / assert 완화 — TDD Loop 우회
- boundary에 10선 판정 로직 누수 — entity 책임 침범

## 보고 형식 (위반 표)

**코드 변경 없이** 아래 표만 출력:

| P | 항목 | 파일:줄 (또는 파일) | 위반 내용 | 권고 |
|---|------|---------------------|-----------|------|
| P0 | import 방향 | `src/entity/foo.py:3` | `from boundary import …` | entity에서 제거 |
| P0 | MagicConstant SSOT | `src/entity/bar.py:12` | 리터럴 `34` | `MAGIC_CONSTANT` 사용 |

- **위반 0건:** `위반 없음 (P0 0건)` 한 줄 + 5항목 ✅ 요약
- **pytest 실행:** 이 Command에서 **필수 아님** (정적 리뷰). 필요 시 사용자가 별도 요청

## P0 / P1 정의

| 등급 | 의미 |
|------|------|
| **P0** | ECB·계약 파괴 — RED/GREEN 전 **반드시** 해소 |
| **P1** | 스타일·중복·문서 — REFACTOR 또는 별도 이슈 |

**P0 예:** entity→boundary import · entity에서 E004 raise · Logic Track `@patch('entity.loc…')` · src에 매직넘버 `34`

## 금지

- **코드 수정** — `src/`, `tests/` Write/Edit/자동 fix **전면 금지**
- 위반을 고치기 위한 **GREEN/REFACTOR 선행**
- **git commit** — 사용자 요청 시만 (이 Command에서 commit 금지)
- 리뷰 없이 “통과” 단정 — 5항목 스캔 근거 없는 ✅ 금지

## Grep 예시 (bash)

```bash
# 1. entity 상위 import
rg "from (boundary|control)" src/entity/

# 2. entity E001~E005
rg "E00[1-5]" src/entity/

# 4. 리터럴 34 (constants 제외하고 수동 판단)
rg "\b34\b" src/ tests/

# 5. Logic Mock
rg "@patch|MagicMock|monkeypatch" tests/entity/ tests/control/
```
