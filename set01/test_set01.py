# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution01 import (
    count_vowels,
    filter_positive,
    fizzbuzz,
    grade,
    is_even,
    is_palindrome,
    max_of_three,
    reverse_string,
    second_largest,
    sum_to_n,
)


# 1. is_even
@pytest.mark.parametrize("n, expected", [(4, True), (7, False), (0, True), (-2, True), (-3, False)])
def test_01_is_even(n, expected):
    assert is_even(n) == expected


# 2. max_of_three
@pytest.mark.parametrize(
    "a, b, c, expected",
    [(1, 5, 3, 5), (9, 2, 3, 9), (1, 2, 8, 8), (-1, -5, -3, -1), (7, 7, 7, 7), (2.5, 2.4, 1, 2.5)],
)
def test_02_max_of_three(a, b, c, expected):
    assert max_of_three(a, b, c) == expected


# 3. sum_to_n
@pytest.mark.parametrize("n, expected", [(10, 55), (1, 1), (100, 5050), (0, 0), (-5, 0)])
def test_03_sum_to_n(n, expected):
    assert sum_to_n(n) == expected


# 4. count_vowels
@pytest.mark.parametrize(
    "s, expected",
    [("hello", 2), ("PYTHON", 1), ("", 0), ("rhythm", 0), ("AEIOUaeiou", 10), ("Hello World", 3)],
)
def test_04_count_vowels(s, expected):
    assert count_vowels(s) == expected


# 5. reverse_string
@pytest.mark.parametrize("s, expected", [("abc", "cba"), ("파이썬", "썬이파"), ("", ""), ("a", "a"), ("ab cd", "dc ba")])
def test_05_reverse_string(s, expected):
    assert reverse_string(s) == expected


# 6. grade
@pytest.mark.parametrize(
    "score, expected",
    [(100, "A"), (95, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C"), (70, "C"), (69, "D"), (60, "D"), (59, "F"), (0, "F")],
)
def test_06_grade(score, expected):
    assert grade(score) == expected


# 7. filter_positive
@pytest.mark.parametrize(
    "nums, expected",
    [([3, -1, 0, 5, -2], [3, 5]), ([], []), ([-1, -2, 0], []), ([1, 2, 3], [1, 2, 3])],
)
def test_07_filter_positive(nums, expected):
    assert filter_positive(nums) == expected


def test_07_filter_positive_does_not_change_input():
    nums = [3, -1, 5]
    assert filter_positive(nums) == [3, 5]
    assert nums == [3, -1, 5], "원래 리스트를 바꾸지 말고 새 리스트를 만들어 돌려주세요"


# 8. fizzbuzz
def test_08_fizzbuzz_5():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_08_fizzbuzz_15():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
        "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]


def test_08_fizzbuzz_0():
    assert fizzbuzz(0) == []


# 9. second_largest
@pytest.mark.parametrize(
    "nums, expected",
    [([3, 1, 4, 1, 5], 4), ([5, 5, 4], 4), ([1, 2], 1), ([-3, -1, -2], -2), ([10, 10, 9, 9, 8], 9)],
)
def test_09_second_largest(nums, expected):
    assert second_largest(nums) == expected


# 10. is_palindrome
@pytest.mark.parametrize(
    "s, expected",
    [("level", True), ("Never odd or even", True), ("python", False), ("Aa", True), ("a", True), ("ab", False)],
)
def test_10_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
