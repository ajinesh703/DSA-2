from collections import deque

def rottenOranges(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0

    while q:
        r, c, time = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, time + 1))

    return time if fresh == 0 else -1

# Usage
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rottenOranges(grid))  # Output: 4
