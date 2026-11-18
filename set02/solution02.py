# 2세트: 20문제
# 문제 설명은 problems.md 를 보세요.
# 각 함수의 `pass`를 지우고 코드를 작성하면 됩니다.


# ---------- A. 숫자 다루기 ----------

def absolute_value(n):
    """1. 절댓값 (abs() 사용 금지)"""
    ans = 0
    if n > 0:
        while(n != 0):
            ans += 1
            n -= 1
    elif n < 0:
        while(n != 0):
            ans += 1
            n += 1
    else:
        return ans



def is_leap_year(year):
    """2. 윤년이면 True"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def factorial(n):
    """3. n! (0! = 1)"""
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def count_digits(n):
    """4. 자릿수 (while + // 10, str/len 사용 금지)"""
    ans = 1
    while (n // 10 != 0):
        n = n // 10
        ans += 1
    return ans


def sum_of_digits(n):
    """5. 각 자리 숫자의 합"""
    ans = 0
    while (n != 0):
        ans += n % 10
        n = n // 10
    return ans


def is_prime(n):
    """6. 소수면 True"""
    if n == 1:
        return False
    elif n <= 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def primes_up_to(n):
    """7. 2부터 n까지의 소수 리스트"""
    new_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            new_list.append(i)
    return new_list


def fibonacci(n):
    """8. 피보나치 수열 처음 n개"""


# ---------- B. 리스트 다루기 ----------

def min_of_list(nums):
    """9. 가장 작은 값 (min/sort/sorted 사용 금지)"""
    ans = nums[0]
    for i in range(len(nums)):
        if nums[i] < ans:
            ans = nums[i]
    return ans


def average(nums):
    """10. 평균 (빈 리스트면 0)"""
    ans = 0
    total = 0
    for i in nums:
        total += i
    if len(nums) == 0:
        return 0
    else:
        ans = total / len(nums)
        return ans


def remove_duplicates(nums):
    """11. 중복 제거, 처음 나온 순서 유지"""
    A = []
    for i in nums:
        if i not in A:
            A.append(i)
    return A

def common_elements(a, b):
    """12. a와 b에 모두 있는 값 (a의 순서, 중복 없이)"""
    ans = []
    for n in a:
        if n in b:
            if n not in ans:
                ans.append(n)
    return ans

def multiplication_table(n):
    """13. n단 구구단 문자열 리스트 ("3 x 1 = 3" 모양)"""
    ans = []
    for i in range(2,10):
        ans.append(f"{n} x {i} = {n * i}")
    return ans


# ---------- C. 문자열 다루기 ----------

def count_char(s, ch):
    """14. s 안의 ch 개수 (.count() 사용 금지)"""
    ans = 0
    for i in s:
        if ch in s:
            ans += 1
    return ans


def capitalize_words(s):
    """15. 각 단어 첫 글자 대문자, 나머지 소문자"""

    s = s.split()
    s_2 = []
    for k in s:
        s_2.append(k[0].upper() + k[1:].lower())
    ans = " ".join(s_2)

    return ans

def caesar_cipher(s, shift):
    """16. 알파벳을 shift칸 밀기 (대소문자 유지, 나머지 글자는 그대로)"""
    pass


# ---------- D. 딕셔너리 ----------

def count_words(s):
    """17. 단어별 개수 딕셔너리 (소문자로)"""
    pass


def most_common_char(s):
    """18. 가장 많이 나온 글자 (공백 제외, 같으면 먼저 나온 글자)"""
    pass


# ---------- E. 2차원 리스트 ----------

def matrix_sum(matrix):
    """19. 2차원 리스트의 모든 값의 합"""
    ans = 0
    for i in matrix:
        for j in i:
            ans += j
    return ans


def transpose(matrix):
    """20. 행과 열 바꾸기"""
    
    a = []
    if not matrix:
        return a
    else:
        i = len(matrix)
        j = len(matrix[0])

        for n in range(j):
            b = []
            for m in range(i):
                b.append(matrix[m][n])
            a.append(b)
        return a


# 직접 실행해 보고 싶으면 아래에 print를 써서 확인해 보세요.
if __name__ == "__main__":
    print(primes_up_to(10))
