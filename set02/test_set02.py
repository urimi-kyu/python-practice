# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution02 import (
    absolute_value,
    average,
    caesar_cipher,
    capitalize_words,
    common_elements,
    count_char,
    count_digits,
    count_words,
    factorial,
    fibonacci,
    is_leap_year,
    is_prime,
    matrix_sum,
    min_of_list,
    most_common_char,
    multiplication_table,
    primes_up_to,
    remove_duplicates,
    sum_of_digits,
    transpose,
)


# ---------- A. 숫자 다루기 ----------

# 1. absolute_value
@pytest.mark.parametrize("n, expected", [(-5, 5), (3, 3), (0, 0), (-2.5, 2.5)])
def test_01_absolute_value(n, expected):
    assert absolute_value(n) == expected


# 2. is_leap_year
@pytest.mark.parametrize(
    "year, expected",
    [(2024, True), (2023, False), (1900, False), (2000, True), (2100, False), (2400, True)],
)
def test_02_is_leap_year(year, expected):
    assert is_leap_year(year) == expected


# 3. factorial
@pytest.mark.parametrize("n, expected", [(5, 120), (0, 1), (1, 1), (10, 3628800)])
def test_03_factorial(n, expected):
    assert factorial(n) == expected


# 4. count_digits
@pytest.mark.parametrize("n, expected", [(12345, 5), (7, 1), (0, 1), (10, 2), (1000000, 7)])
def test_04_count_digits(n, expected):
    assert count_digits(n) == expected


# 5. sum_of_digits
@pytest.mark.parametrize("n, expected", [(1234, 10), (0, 0), (9, 9), (1005, 6), (99999, 45)])
def test_05_sum_of_digits(n, expected):
    assert sum_of_digits(n) == expected


# 6. is_prime
@pytest.mark.parametrize(
    "n, expected",
    [(2, True), (3, True), (7, True), (97, True), (0, False), (1, False), (4, False), (9, False), (25, False), (-7, False)],
)
def test_06_is_prime(n, expected):
    assert is_prime(n) == expected


# 7. primes_up_to
@pytest.mark.parametrize(
    "n, expected",
    [(10, [2, 3, 5, 7]), (1, []), (2, [2]), (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])],
)
def test_07_primes_up_to(n, expected):
    assert primes_up_to(n) == expected


# 8. fibonacci
@pytest.mark.parametrize(
    "n, expected",
    [(7, [0, 1, 1, 2, 3, 5, 8]), (1, [0]), (0, []), (2, [0, 1]), (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])],
)
def test_08_fibonacci(n, expected):
    assert fibonacci(n) == expected


# ---------- B. 리스트 다루기 ----------

# 9. min_of_list
@pytest.mark.parametrize("nums, expected", [([3, 1, 4, 1, 5], 1), ([-2, -8, 0], -8), ([42], 42), ([5, 4, 3, 2, 1], 1)])
def test_09_min_of_list(nums, expected):
    assert min_of_list(nums) == expected


# 10. average
@pytest.mark.parametrize("nums, expected", [([1, 2, 3, 4], 2.5), ([], 0), ([5], 5), ([-1, 1], 0), ([1, 2], 1.5)])
def test_10_average(nums, expected):
    assert average(nums) == expected


# 11. remove_duplicates
@pytest.mark.parametrize(
    "nums, expected",
    [([3, 1, 3, 2, 1], [3, 1, 2]), ([], []), ([1, 1, 1], [1]), ([5, 4, 3], [5, 4, 3]), ([2, 1, 2, 1, 3], [2, 1, 3])],
)
def test_11_remove_duplicates(nums, expected):
    assert remove_duplicates(nums) == expected


def test_11_remove_duplicates_does_not_change_input():
    nums = [3, 1, 3]
    assert remove_duplicates(nums) == [3, 1]
    assert nums == [3, 1, 3], "원래 리스트를 바꾸지 말고 새 리스트를 만들어 돌려주세요"


# 12. common_elements
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4], [4, 3, 5], [3, 4]),
        ([1, 1, 2], [1], [1]),
        ([1, 2], [3, 4], []),
        ([], [1], []),
        ([5, 3, 5, 1], [1, 5, 5], [5, 1]),
    ],
)
def test_12_common_elements(a, b, expected):
    assert common_elements(a, b) == expected


# 13. multiplication_table
def test_13_multiplication_table_3():
    assert multiplication_table(3) == [
        "3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9",
        "3 x 4 = 12", "3 x 5 = 15", "3 x 6 = 18",
        "3 x 7 = 21", "3 x 8 = 24", "3 x 9 = 27",
    ]


def test_13_multiplication_table_9():
    result = multiplication_table(9)
    assert len(result) == 9
    assert result[0] == "9 x 1 = 9"
    assert result[-1] == "9 x 9 = 81"


# ---------- C. 문자열 다루기 ----------

# 14. count_char
@pytest.mark.parametrize(
    "s, ch, expected",
    [("banana", "a", 3), ("Banana", "b", 0), ("", "a", 0), ("hello world", " ", 1), ("aaa", "a", 3)],
)
def test_14_count_char(s, ch, expected):
    assert count_char(s, ch) == expected


# 15. capitalize_words
@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello world", "Hello World"),
        ("pYTHON is FUN", "Python Is Fun"),
        ("a", "A"),
        ("", ""),
        ("i love python", "I Love Python"),
    ],
)
def test_15_capitalize_words(s, expected):
    assert capitalize_words(s) == expected


# 16. caesar_cipher
@pytest.mark.parametrize(
    "s, shift, expected",
    [
        ("abc", 1, "bcd"),
        ("xyz", 3, "abc"),
        ("Hello!", 1, "Ifmmp!"),
        ("bcd", -1, "abc"),
        ("abc", -1, "zab"),
        ("Hello, World 2026", 13, "Uryyb, Jbeyq 2026"),
        ("abc", 26, "abc"),
        ("", 5, ""),
    ],
)
def test_16_caesar_cipher(s, shift, expected):
    assert caesar_cipher(s, shift) == expected


# ---------- D. 딕셔너리 ----------

# 17. count_words
@pytest.mark.parametrize(
    "s, expected",
    [
        ("the cat and the hat", {"the": 2, "cat": 1, "and": 1, "hat": 1}),
        ("Hi hi HI", {"hi": 3}),
        ("", {}),
        ("python", {"python": 1}),
    ],
)
def test_17_count_words(s, expected):
    assert count_words(s) == expected


# 18. most_common_char
@pytest.mark.parametrize(
    "s, expected",
    [("hello", "l"), ("abab", "a"), ("a b b", "b"), ("x", "x"), ("banana", "a"), ("  zz  y", "z"), ("baab", "b")],
)
def test_18_most_common_char(s, expected):
    assert most_common_char(s) == expected


# ---------- E. 2차원 리스트 ----------

# 19. matrix_sum
@pytest.mark.parametrize(
    "matrix, expected",
    [([[1, 2], [3, 4]], 10), ([], 0), ([[5]], 5), ([[1, 2, 3], [4, 5, 6]], 21), ([[-1, 1], [0, 0]], 0)],
)
def test_19_matrix_sum(matrix, expected):
    assert matrix_sum(matrix) == expected


# 20. transpose
@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([], []),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
    ],
)
def test_20_transpose(matrix, expected):
    assert transpose(matrix) == expected


def test_20_transpose_does_not_change_input():
    matrix = [[1, 2], [3, 4]]
    assert transpose(matrix) == [[1, 3], [2, 4]]
    assert matrix == [[1, 2], [3, 4]], "원래 리스트를 바꾸지 말고 새 리스트를 만들어 돌려주세요"
