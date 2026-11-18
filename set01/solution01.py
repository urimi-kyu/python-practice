# 1세트: 기초 10문제
# 문제 설명은 problems.md 를 보세요.
# 각 함수의 `pass`를 지우고 코드를 작성하면 됩니다.


def is_even(n):
    """1. n이 짝수면 True, 홀수면 False"""
    if n % 2 == 0:
        return True
    else:
        return False


def max_of_three(a, b, c):
    """2. 세 수 중 가장 큰 값 (max() 사용 금지)"""
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c


def sum_to_n(n):
    """3. 1부터 n까지의 합 (n <= 0 이면 0)"""
    sum_init = 0
    if n <= 0:
        return 0
    else:
        for i in range(n + 1):
            sum_init += i
    return sum_init


def count_vowels(s):
    """4. 영어 모음(a, e, i, o, u) 개수, 대문자 포함"""
    count = 0
    s = s.lower()
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count


def reverse_string(s):
    """5. 문자열 뒤집기"""
    init_list = list(s)
    init_list.reverse()
    re_s = "".join(init_list)
    return re_s


def grade(score):
    """6. 점수 → 학점 ("A" ~ "F")"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def filter_positive(nums):
    """7. 0보다 큰 수만 담은 새 리스트"""
    new_list = []
    for i in nums:
        if i > 0:
            new_list.append(i)
    return new_list


def fizzbuzz(n):
    """8. 1부터 n까지 FizzBuzz 문자열 리스트"""
    new_list8 = []
    for i in range(1, n + 1, 1):
        if i % 3 == 0:
            if i % 5 == 0:
                new_list8.append("FizzBuzz")
            else:
                new_list8.append("Fizz")
        elif i % 5 == 0:
            new_list8.append(("Buzz"))
        else:
            new_list8.append(str(i))
    return new_list8


def second_largest(nums):
    """9. 두 번째로 큰 값 (중복은 한 번만 셈)"""
    nums.sort()
    B = set(nums)
    return list(B)[-2]


def is_palindrome(s):
    """10. 회문이면 True (대소문자, 공백 무시)"""
    A = s.replace(" ", "")
    A = A.lower()
    B = list(A)
    B.reverse()
    B = "".join(B)
    if A == B:
        return True
    else:
        return False


# 직접 실행해 보고 싶으면 아래에 print를 써서 확인해 보세요.
if __name__ == "__main__":
    # print(is_even(4))
    # print(max_of_three(1, 5, 3))
    print(is_palindrome("python"))
