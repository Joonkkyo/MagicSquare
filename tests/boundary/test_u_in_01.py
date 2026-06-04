"""U-IN-01 — FR-IN-01: grid is None → E003. RED skeleton."""

import pytest


def test_u_in_01_none_grid_returns_e003():
    # Given: grid = None (FR-IN-01)
    grid = None
    # When: validate_input(grid)  # RED: 호출은 GREEN/tdd-red에서
    # Then: "E003" — control/entity 미호출 (GREEN에서 mock 검증)
    pytest.fail("RED: U-IN-01 — 구현 없음, 의도적 실패")
