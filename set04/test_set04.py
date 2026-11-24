# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution04 import (
    count_primes,
    group_anagrams,
    most_common_char,
    sum_even_squares,
    two_sum,
)


# 1. sum_even_squares
@pytest.mark.parametrize("nums, expected", [([1, 2, 3, 4], 20), ([1, 3, 5], 0), ([], 0), ([-2, 3, 4], 20), ([10], 100)])
def test_01_sum_even_squares(nums, expected):
    assert sum_even_squares(nums) == expected


# 2. most_common_char
@pytest.mark.parametrize("s, expected", [("abracadabra", "a"), ("banana", "a"), ("abcabc", "a"), ("zzyyx", "y"), ("q", "q")])
def test_02_most_common_char(s, expected):
    assert most_common_char(s) == expected


# 3. group_anagrams
@pytest.mark.parametrize(
    "words, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "cab", "bca", "xyz"], [["abc", "bca", "cab"], ["xyz"]]),
        ([], []),
    ],
)
def test_03_group_anagrams(words, expected):
    assert group_anagrams(words) == expected


# 4. two_sum
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 5, 9, 14], 23, [2, 3]),
    ],
)
def test_04_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


# 5. count_primes (n이 크므로 효율적인 풀이가 필요해요)
@pytest.mark.parametrize("n, expected", [(1, 0), (2, 1), (10, 4), (100, 25), (1_000_000, 78498)])
def test_05_count_primes(n, expected):
    assert count_primes(n) == expected
