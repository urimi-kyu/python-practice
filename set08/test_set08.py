# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution08 import (
    count_islands,
    rotate_clockwise,
    rotting_days,
    shortest_path,
    spiral_order,
)


# 1. spiral_order
@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[5, 6, 7]], [5, 6, 7]),
        ([[9]], [9]),
        ([], []),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
         [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]),
    ],
)
def test_01_spiral_order(matrix, expected):
    assert spiral_order(matrix) == expected


# 2. rotate_clockwise
@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [[4, 1], [5, 2], [6, 3]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[7]], [[7]]),
        ([], []),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[3, 2, 1]]),
    ],
)
def test_02_rotate_clockwise(matrix, expected):
    assert rotate_clockwise(matrix) == expected


def test_02_rotate_clockwise_keeps_original():
    matrix = [[1, 2], [3, 4]]
    assert rotate_clockwise(matrix) == [[3, 1], [4, 2]]
    assert matrix == [[1, 2], [3, 4]]


# 3. count_islands
@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1]], 2),
        ([[1, 0], [0, 1]], 2),
        ([[0, 0], [0, 0]], 0),
        ([[1, 1, 1]], 1),
        ([], 0),
        ([[1], [0], [1], [0], [1]], 3),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
    ],
)
def test_03_count_islands(grid, expected):
    assert count_islands(grid) == expected


# 4. shortest_path
@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0]], 5),
        ([[0, 1], [1, 0]], -1),
        ([[0]], 1),
        ([[1, 0], [0, 0]], -1),
        ([[0, 0], [0, 1]], -1),
        ([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 6),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 5),
    ],
)
def test_04_shortest_path(grid, expected):
    assert shortest_path(grid) == expected


# 5. rotting_days
@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[1]], -1),
        ([[0]], 0),
        ([[2, 1, 2]], 1),
        ([[2, 1, 1, 1, 2]], 2),
    ],
)
def test_05_rotting_days(grid, expected):
    assert rotting_days(grid) == expected
