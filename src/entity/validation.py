"""FR-VAL — 10-line sum helpers (entity)."""

from entity.constants import GRID_SIZE


def sum_row(grid, row):
    return sum(grid[row][col] for col in range(GRID_SIZE))


def sum_col(grid, col):
    return sum(grid[row][col] for row in range(GRID_SIZE))
