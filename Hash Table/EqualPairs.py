from collections import Counter

def equalPairs(grid):
    n = len(grid)
    row_count = Counter(tuple(row) for row in grid)
    col_count = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
    return sum(row_count[row] * col_count[row] for row in row_count)
