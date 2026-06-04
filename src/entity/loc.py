"""FR-LOC — blank cell location (entity)."""

from entity.constants import BLANK_CELL_VALUE, GRID_SIZE


def find_blank_coords(grid):
    coords = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL_VALUE:
                coords.append((row + 1, col + 1))
    return coords
