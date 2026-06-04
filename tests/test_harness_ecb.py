"""Harness smoke — ECB layers importable, domain SSOT, Dual-Track dirs exist."""

from pathlib import Path

from entity.constants import (
    BLANK_CELL_VALUE,
    GRID_SIZE,
    MAGIC_CONSTANT,
    MAX_CELL_VALUE,
)


def test_domain_constants_ssot():
    assert GRID_SIZE == 4
    assert MAGIC_CONSTANT == 34
    assert MAX_CELL_VALUE == 16
    assert BLANK_CELL_VALUE == 0


def test_g1_fixture_shape(grid_g1):
    assert len(grid_g1) == 4
    assert all(len(row) == 4 for row in grid_g1)
    assert sum(cell == 0 for row in grid_g1 for cell in row) == 2


def test_dual_track_directories_exist():
    tests_root = Path(__file__).resolve().parent
    for name in ("entity", "control", "boundary"):
        assert (tests_root / name).is_dir(), f"missing tests/{name}/"


def test_ecb_source_packages_exist():
    src_root = Path(__file__).resolve().parents[1] / "src"
    for name in ("entity", "control", "boundary"):
        assert (src_root / name).is_dir(), f"missing src/{name}/"
