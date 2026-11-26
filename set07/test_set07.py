# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution07 import (
    count_subarrays_with_sum,
    longest_unique_substring,
    max_window_sum,
    min_window_length,
    range_sums,
)


# 1. max_window_sum
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, 9),
        ([2, -1, 3, -4, 5], 3, 4),
        ([-3, -1, -2], 2, -3),
        ([7], 1, 7),
        ([5, 1, 1, 1], 4, 8),
        ([4, 0, 0, 9], 1, 9),
    ],
)
def test_01_max_window_sum(nums, k, expected):
    assert max_window_sum(nums, k) == expected


# 2. range_sums
@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        ([1, 2, 3, 4, 5], [[0, 2], [1, 3], [4, 4]], [6, 9, 5]),
        ([5, -2, 7], [[0, 2], [1, 1]], [10, -2]),
        ([3], [[0, 0]], [3]),
        ([1, 2, 3], [], []),
        ([1, 2, 3, 4], [[0, 3], [0, 0], [3, 3], [2, 3]], [10, 1, 4, 7]),
    ],
)
def test_02_range_sums(nums, queries, expected):
    assert range_sums(nums, queries) == expected


def test_02_range_sums_large():
    nums = list(range(1, 50001))
    queries = [[0, 49999], [100, 200], [49999, 49999]] * 10000
    result = range_sums(nums, queries)
    assert result[:3] == [1250025000, sum(range(101, 202)), 50000]
    assert len(result) == 30000


# 3. longest_unique_substring
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abba", 2),
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("tmmzuxt", 5),
    ],
)
def test_03_longest_unique_substring(s, expected):
    assert longest_unique_substring(s) == expected


# 4. count_subarrays_with_sum
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([0, 0, 0], 0, 6),
        ([], 0, 0),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
        ([5], 5, 1),
        ([5], 4, 0),
    ],
)
def test_04_count_subarrays_with_sum(nums, k, expected):
    assert count_subarrays_with_sum(nums, k) == expected


# 5. min_window_length
@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", 4),
        ("a", "a", 1),
        ("a", "aa", 0),
        ("aab", "ab", 2),
        ("abc", "d", 0),
        ("abcabdebac", "cda", 4),
        ("aaflslflsldkalskaaa", "aaa", 3),
    ],
)
def test_05_min_window_length(s, t, expected):
    assert min_window_length(s, t) == expected
