# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution05 import (
    is_valid_brackets,
    josephus,
    largest_rectangle,
    next_greater,
    remove_adjacent_duplicates,
)


# 1. is_valid_brackets
@pytest.mark.parametrize(
    "s, expected",
    [
        ("()[]{}", True),
        ("{[]}", True),
        ("", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        (")(", False),
    ],
)
def test_01_is_valid_brackets(s, expected):
    assert is_valid_brackets(s) == expected


# 2. remove_adjacent_duplicates
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("aaa", "a"),
        ("abba", ""),
        ("abc", "abc"),
        ("", ""),
    ],
)
def test_02_remove_adjacent_duplicates(s, expected):
    assert remove_adjacent_duplicates(s) == expected


# 3. josephus (마지막 케이스는 n이 커서 deque 같은 효율적인 풀이가 필요해요)
@pytest.mark.parametrize(
    "n, k, expected",
    [
        (1, 1, 1),
        (7, 3, 4),
        (5, 2, 3),
        (6, 1, 6),
        (10, 2, 5),
        (5, 5, 2),
        (100_000, 2, 68929),
    ],
)
def test_03_josephus(n, k, expected):
    assert josephus(n, k) == expected


# 4. next_greater
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 2, 4, 3], [4, 2, 4, -1, -1]),
        ([1, 2, 3], [2, 3, -1]),
        ([3, 2, 1], [-1, -1, -1]),
        ([1, 1, 1], [-1, -1, -1]),
        ([5], [-1]),
        ([], []),
        ([1, 3, 2, 4], [3, 4, 4, -1]),
    ],
)
def test_04_next_greater(nums, expected):
    assert next_greater(nums) == expected


# 5. largest_rectangle
@pytest.mark.parametrize(
    "heights, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([], 0),
        ([5, 5, 5, 5], 20),
        ([6, 2, 5, 4, 5, 1, 6], 12),
        ([0, 0], 0),
    ],
)
def test_05_largest_rectangle(heights, expected):
    assert largest_rectangle(heights) == expected
