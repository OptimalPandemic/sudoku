from itertools import product


def check_sudoku(grid):
    """Validate a sudoku solution.

    Given a grid as a list of lists, return None if it is ill-formed,
    False if it is invalid, or True if it is a valid solution.
    """
    assert isinstance(grid, list)

    # Check that the grid is 9x9.
    if len(grid) != 9 or not all(len(row) == 9 for row in grid):
        return None

    digits = set(range(1, 10))
    threes = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

    def correct(groups):
        return all(set(group) == digits for group in groups)

    rows = grid
    columns = zip(*grid)
    squares3x3 = [
        [grid[r][c] for r, c in product(row_block, col_block)]
        for row_block, col_block in product(threes, threes)
    ]

    return correct(rows) and correct(columns) and correct(squares3x3)