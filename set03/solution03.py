# 3세트: 20문제
# 문제 설명은 problems.md 를 보세요.
# 각 함수의 `pass`를 지우고 코드를 작성하면 됩니다.


# ---------- A. 숫자와 반복 ----------

def gcd(a, b):
    """1. 최대공약수 (유클리드 호제법)"""
    pass


def lcm(a, b):
    """2. 최소공배수 (gcd 활용)"""
    pass


def reverse_number(n):
    """3. 숫자 뒤집기 (str 사용 금지)"""
    pass


def is_perfect_number(n):
    """4. 완전수면 True"""
    pass


def collatz_steps(n):
    """5. 1이 될 때까지 걸리는 횟수"""
    pass


def binary_to_decimal(s):
    """6. 2진수 문자열 → 10진수 정수 (int(s, 2) 사용 금지)"""
    pass


def decimal_to_binary(n):
    """7. 10진수 정수 → 2진수 문자열 (bin() 사용 금지)"""
    pass


# ---------- B. 리스트 알고리즘 ----------

def bubble_sort(nums):
    """8. 버블 정렬한 새 리스트 (sort/sorted 사용 금지)"""
    pass


def binary_search(nums, target):
    """9. 이진 탐색으로 target의 인덱스, 없으면 -1"""
    pass


def running_sum(nums):
    """10. 누적 합 리스트"""
    pass


def rotate_list(nums, k):
    """11. 오른쪽으로 k칸 회전한 새 리스트"""
    pass


def chunk_list(nums, size):
    """12. size개씩 나눈 2차원 리스트"""
    pass


def flatten(matrix):
    """13. 2차원 리스트를 1차원으로"""
    pass


def min_max(nums):
    """14. (최솟값, 최댓값) 튜플"""
    pass


# ---------- C. 문자열 ----------

def is_anagram(a, b):
    """15. 애너그램이면 True (대소문자, 공백 무시)"""
    pass


def compress_string(s):
    """16. 연속된 글자를 '글자+개수'로 압축"""
    pass


def longest_word(s):
    """17. 가장 긴 단어 (같으면 먼저 나온 것, 빈 문자열이면 "")"""
    pass


# ---------- D. 딕셔너리 응용 ----------

def group_by_length(words):
    """18. {길이: [단어들]} 딕셔너리"""
    pass


def invert_dict(d):
    """19. 키와 값을 뒤집은 딕셔너리"""
    pass


def top_student(students):
    """20. 점수가 가장 높은 학생 이름 (같으면 먼저 나온 학생, 빈 리스트면 None)"""
    pass


# 직접 실행해 보고 싶으면 아래에 print를 써서 확인해 보세요.
if __name__ == "__main__":
    print(gcd(12, 18))
