# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution06 import (
    largest_number,
    lower_bound,
    min_meeting_rooms,
    min_ship_capacity,
    sort_words,
)


# 1. sort_words
@pytest.mark.parametrize(
    "words, expected",
    [
        (["banana", "apple", "kiwi", "fig"], ["fig", "kiwi", "apple", "banana"]),
        (["bb", "a", "ab", "b"], ["a", "b", "ab", "bb"]),
        (["aa", "a", "aa"], ["a", "aa", "aa"]),
        (["abc", "ab", "abd", "aa"], ["aa", "ab", "abc", "abd"]),
        (["z"], ["z"]),
        ([], []),
    ],
)
def test_01_sort_words(words, expected):
    assert sort_words(words) == expected


def test_01_sort_words_does_not_modify_input():
    words = ["b", "a"]
    assert sort_words(words) == ["a", "b"]
    assert words == ["b", "a"]


# 2. lower_bound
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 3, 5], 3, 1),
        ([1, 3, 3, 5], 4, 3),
        ([1, 3, 3, 5], 0, 0),
        ([1, 3, 3, 5], 6, 4),
        ([1, 3, 5, 7], 7, 3),
        ([2, 2, 2], 2, 0),
        ([], 1, 0),
    ],
)
def test_02_lower_bound(nums, target, expected):
    assert lower_bound(nums, target) == expected


# 3. largest_number
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 2], "210"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([121, 12], "12121"),
        ([824, 8247], "8248247"),
        ([0, 0], "0"),
        ([0], "0"),
        ([1], "1"),
    ],
)
def test_03_largest_number(nums, expected):
    assert largest_number(nums) == expected


# 4. min_ship_capacity (마지막 케이스는 짐이 많아서 효율적인 풀이가 필요해요)
@pytest.mark.parametrize(
    "weights, days, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
        ([5], 1, 5),
        ([1, 2, 3], 1, 6),
        ([1, 2, 3], 3, 3),
        ([1] * 200_000, 4, 50_000),
    ],
)
def test_04_min_ship_capacity(weights, days, expected):
    assert min_ship_capacity(weights, days) == expected


# 5. min_meeting_rooms
@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [5, 10]], 1),
        ([[1, 5], [2, 6], [3, 7]], 3),
        ([[1, 4], [4, 5], [2, 3]], 2),
        ([[1, 10], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 2]], 1),
        ([], 0),
    ],
)
def test_05_min_meeting_rooms(intervals, expected):
    assert min_meeting_rooms(intervals) == expected
