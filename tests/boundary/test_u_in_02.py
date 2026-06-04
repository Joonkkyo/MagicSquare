"""U-IN-02 — FR-IN-02: 크기 ≠ 4×4 → E001. RED skeleton."""

import pytest


def test_u_in_02_wrong_size_returns_e001():
    # Given: 3×3 격자 (FR-IN-02)
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # When: validate_input(grid)  # RED: 호출은 GREEN/tdd-red에서
    # Then: "E001" — control/entity 미호출 (GREEN에서 mock 검증)
    pytest.fail("RED: U-IN-02 — 구현 없음, 의도적 실패")
