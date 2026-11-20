# 채점용 테스트 파일입니다. 이 파일은 고치지 마세요!
import pytest

from solution03 import (
    binary_search,
    binary_to_decimal,
    bubble_sort,
    chunk_list,
    collatz_steps,
    compress_string,
    decimal_to_binary,
    flatten,
    gcd,
    group_by_length,
    invert_dict,
    is_anagram,
    is_perfect_number,
    lcm,
    longest_word,
    min_max,
    reverse_number,
    rotate_list,
    running_sum,
    top_student,
)


# ---------- A. 숫자와 반복 ----------

# 1. gcd
@pytest.mark.parametrize("a, b, expected", [(12, 18, 6), (18, 12, 6), (7, 13, 1), (0, 5, 5), (5, 0, 5), (100, 75, 25), (9, 9, 9)])
def test_01_gcd(a, b, expected):
    assert gcd(a, b) == expected


# 2. lcm
@pytest.mark.parametrize("a, b, expected", [(4, 6, 12), (3, 7, 21), (5, 5, 5), (1, 9, 9), (12, 18, 36)])
def test_02_lcm(a, b, expected):
    assert lcm(a, b) == expected


# 3. reverse_number
@pytest.mark.parametrize("n, expected", [(1234, 4321), (1200, 21), (0, 0), (7, 7), (10, 1), (12321, 12321)])
def test_03_reverse_number(n, expected):
    assert reverse_number(n) == expected


# 4. is_perfect_number
@pytest.mark.parametrize(
    "n, expected",
    [(6, True), (28, True), (496, True), (1, False), (12, False), (2, False), (27, False)],
)
def test_04_is_perfect_number(n, expected):
    assert is_perfect_number(n) == expected


# 5. collatz_steps
@pytest.mark.parametrize("n, expected", [(6, 8), (1, 0), (2, 1), (3, 7), (27, 111)])
def test_05_collatz_steps(n, expected):
    assert collatz_steps(n) == expected


# 6. binary_to_decimal
@pytest.mark.parametrize("s, expected", [("1011", 11), ("0", 0), ("1", 1), ("1000", 8), ("11111111", 255), ("0010", 2)])
def test_06_binary_to_decimal(s, expected):
    assert binary_to_decimal(s) == expected


# 7. decimal_to_binary
@pytest.mark.parametrize("n, expected", [(11, "1011"), (0, "0"), (1, "1"), (8, "1000"), (255, "11111111"), (2, "10")])
def test_07_decimal_to_binary(n, expected):
    assert decimal_to_binary(n) == expected


# ---------- B. 리스트 알고리즘 ----------

# 8. bubble_sort
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 2, 9, 1], [1, 2, 5, 9]),
        ([], []),
        ([1], [1]),
        ([3, 3, 1], [1, 3, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-1, 10, 0, -5], [-5, -1, 0, 10]),
    ],
)
def test_08_bubble_sort(nums, expected):
    assert bubble_sort(nums) == expected


def test_08_bubble_sort_does_not_change_input():
    nums = [3, 1, 2]
    assert bubble_sort(nums) == [1, 2, 3]
    assert nums == [3, 1, 2], "원래 리스트를 바꾸지 말고 새 리스트를 만들어 돌려주세요"


# 9. binary_search
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 7, 9], 7, 3),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([1, 3, 5, 7, 9], 10, -1),
        ([], 1, -1),
        ([5], 5, 0),
        ([2, 4], 4, 1),
    ],
)
def test_09_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected


# 10. running_sum
@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 3, 4], [1, 3, 6, 10]), ([], []), ([5], [5]), ([1, -1, 1], [1, 0, 1])],
)
def test_10_running_sum(nums, expected):
    assert running_sum(nums) == expected


# 11. rotate_list
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 4, [3, 1, 2]),
        ([], 3, []),
        ([1], 5, [1]),
    ],
)
def test_11_rotate_list(nums, k, expected):
    assert rotate_list(nums, k) == expected


# 12. chunk_list
@pytest.mark.parametrize(
    "nums, size, expected",
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3], 5, [[1, 2, 3]]),
        ([], 2, []),
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
        ([1, 2, 3], 1, [[1], [2], [3]]),
    ],
)
def test_12_chunk_list(nums, size, expected):
    assert chunk_list(nums, size) == expected


# 13. flatten
@pytest.mark.parametrize(
    "matrix, expected",
    [([[1, 2], [3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]), ([], []), ([[]], []), ([[1]], [1]), ([[1, 2], [3, 4]], [1, 2, 3, 4])],
)
def test_13_flatten(matrix, expected):
    assert flatten(matrix) == expected


# 14. min_max
@pytest.mark.parametrize("nums, expected", [([3, 1, 4, 1, 5], (1, 5)), ([7], (7, 7)), ([-3, -1, -2], (-3, -1))])
def test_14_min_max(nums, expected):
    assert min_max(nums) == expected


def test_14_min_max_is_tuple():
    assert isinstance(min_max([1, 2]), tuple), "리스트가 아니라 튜플로 돌려주세요"


# ---------- C. 문자열 ----------

# 15. is_anagram
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("listen", "silent", True),
        ("Dormitory", "dirty room", True),
        ("abc", "abd", False),
        ("aab", "abb", False),
        ("abc", "ab", False),
        ("", "", True),
        ("Astronomer", "Moon starer", True),
    ],
)
def test_15_is_anagram(a, b, expected):
    assert is_anagram(a, b) == expected


# 16. compress_string
@pytest.mark.parametrize(
    "s, expected",
    [("aaabcc", "a3b1c2"), ("abc", "a1b1c1"), ("aabaa", "a2b1a2"), ("", ""), ("a", "a1"), ("zzzzzzzzzzzz", "z12")],
)
def test_16_compress_string(s, expected):
    assert compress_string(s) == expected


# 17. longest_word
@pytest.mark.parametrize(
    "s, expected",
    [("I love python", "python"), ("aa bb", "aa"), ("", ""), ("hello", "hello"), ("a bb ccc dd", "ccc")],
)
def test_17_longest_word(s, expected):
    assert longest_word(s) == expected


# ---------- D. 딕셔너리 응용 ----------

# 18. group_by_length
@pytest.mark.parametrize(
    "words, expected",
    [
        (["hi", "cat", "to", "dog"], {2: ["hi", "to"], 3: ["cat", "dog"]}),
        ([], {}),
        (["a"], {1: ["a"]}),
        (["abc", "de", "fgh", "i"], {3: ["abc", "fgh"], 2: ["de"], 1: ["i"]}),
    ],
)
def test_18_group_by_length(words, expected):
    assert group_by_length(words) == expected


# 19. invert_dict
@pytest.mark.parametrize(
    "d, expected",
    [({"a": 1, "b": 2}, {1: "a", 2: "b"}), ({}, {}), ({"x": "y"}, {"y": "x"})],
)
def test_19_invert_dict(d, expected):
    assert invert_dict(d) == expected


def test_19_invert_dict_does_not_change_input():
    d = {"a": 1}
    assert invert_dict(d) == {1: "a"}
    assert d == {"a": 1}, "원래 딕셔너리를 바꾸지 말고 새 딕셔너리를 만들어 돌려주세요"


# 20. top_student
STUDENTS = [
    {"name": "민수", "score": 85},
    {"name": "지영", "score": 92},
    {"name": "철수", "score": 78},
]


def test_20_top_student():
    assert top_student(STUDENTS) == "지영"


def test_20_top_student_empty():
    assert top_student(STUDENTS) == "지영"
    assert top_student([]) is None, "빈 리스트면 None을 돌려주세요"


def test_20_top_student_tie():
    tie = [{"name": "가", "score": 90}, {"name": "나", "score": 95}, {"name": "다", "score": 95}]
    assert top_student(tie) == "나"


def test_20_top_student_one():
    assert top_student([{"name": "혼자", "score": 0}]) == "혼자"
