# 8세트 모범 답안 (다 풀고 나서 확인하세요)
from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def spiral_order(matrix):
    if not matrix:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        for r in range(top + 1, bottom + 1):
            result.append(matrix[r][right])
        if top < bottom and left < right:
            for c in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][c])
            for r in range(bottom - 1, top, -1):
                result.append(matrix[r][left])
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    return result


def rotate_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def count_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                visited[r][c] = True
                queue = deque([(r, c)])
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in DIRECTIONS:
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and grid[nr][nc] == 1 and not visited[nr][nc]):
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    return count


def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and not visited[nr][nc]):
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1


def rotting_days(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    seen = [row[:] for row in grid]  # 원본은 건드리지 않아요
    days = 0
    while queue and fresh > 0:
        days += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and seen[nr][nc] == 1:
                    seen[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
    return days if fresh == 0 else -1
