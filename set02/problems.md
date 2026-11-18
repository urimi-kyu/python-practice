# 2세트: 20문제

`solution02.py` 파일의 각 함수 안에 있는 `pass`를 지우고 코드를 작성하세요.
**`test_set02.py`(채점 파일)는 고치지 마세요.**

1세트보다 조금 어려워요. `while`문, 딕셔너리(`dict`), 2차원 리스트가 새로 나와요.

---

## A. 숫자 다루기

### 1. `absolute_value(n)` — 절댓값
`n`의 절댓값을 돌려주세요. **`abs()`는 쓰지 마세요.**
```
absolute_value(-5) → 5
absolute_value(3)  → 3
```

### 2. `is_leap_year(year)` — 윤년 판별
윤년이면 `True`, 아니면 `False`를 돌려주세요. 윤년 규칙은 이래요.
- 4로 나누어떨어지면 윤년이에요.
- 그런데 100으로도 나누어떨어지면 윤년이 **아니에요**.
- 그런데 400으로도 나누어떨어지면 다시 윤년이에요.
```
is_leap_year(2024) → True
is_leap_year(1900) → False
is_leap_year(2000) → True
```

### 3. `factorial(n)` — 팩토리얼
`n! = 1 × 2 × ... × n`을 돌려주세요. `0! = 1`이에요. `n`은 0 이상이에요.
```
factorial(5) → 120
factorial(0) → 1
```

### 4. `count_digits(n)` — 자릿수 세기
0 이상의 정수 `n`이 몇 자리인지 돌려주세요.
**`str()`이나 `len()`은 쓰지 말고, `while`문과 `// 10`으로** 풀어보세요.
```
count_digits(12345) → 5
count_digits(7)     → 1
count_digits(0)     → 1
```

### 5. `sum_of_digits(n)` — 각 자리 숫자의 합
0 이상의 정수 `n`의 각 자리 숫자를 모두 더해 돌려주세요.
```
sum_of_digits(1234) → 10   (1 + 2 + 3 + 4)
sum_of_digits(0)    → 0
```
> 힌트: `n % 10`은 맨 끝자리, `n // 10`은 맨 끝자리를 뗀 나머지예요.

### 6. `is_prime(n)` — 소수 판별
`n`이 소수(1과 자기 자신으로만 나누어떨어지는 2 이상의 수)이면 `True`를 돌려주세요.
```
is_prime(7)  → True
is_prime(1)  → False
is_prime(9)  → False
```

### 7. `primes_up_to(n)` — n 이하의 소수 목록
2부터 `n`까지의 소수를 작은 순서대로 리스트로 돌려주세요.
```
primes_up_to(10) → [2, 3, 5, 7]
primes_up_to(1)  → []
```
> 6번에서 만든 `is_prime`을 불러 써도 돼요!

### 8. `fibonacci(n)` — 피보나치 수열
피보나치 수열의 **처음 `n`개**를 리스트로 돌려주세요.
`0, 1`로 시작하고, 그다음부터는 앞의 두 수를 더한 값이에요.
```
fibonacci(7) → [0, 1, 1, 2, 3, 5, 8]
fibonacci(1) → [0]
fibonacci(0) → []
```

---

## B. 리스트 다루기

### 9. `min_of_list(nums)` — 가장 작은 값
리스트에서 가장 작은 값을 돌려주세요. **`min()`과 `sort()`, `sorted()`는 쓰지 마세요.** 리스트는 비어 있지 않아요.
```
min_of_list([3, 1, 4, 1, 5]) → 1
min_of_list([-2, -8, 0])     → -8
```

### 10. `average(nums)` — 평균
리스트의 평균을 돌려주세요. **빈 리스트면 `0`**을 돌려주세요.
```
average([1, 2, 3, 4]) → 2.5
average([])           → 0
```

### 11. `remove_duplicates(nums)` — 중복 없애기 (순서 유지)
중복을 없앤 새 리스트를 돌려주세요. **처음 나온 순서는 그대로** 지켜야 해요.
```
remove_duplicates([3, 1, 3, 2, 1]) → [3, 1, 2]
```
> 주의: `set`은 순서가 없어서 이 문제에는 그대로 쓰면 안 돼요!

### 12. `common_elements(a, b)` — 두 리스트에 모두 있는 값
`a`와 `b`에 **모두** 들어 있는 값을 리스트로 돌려주세요.
`a`에 나온 순서대로, 중복 없이 담아요.
```
common_elements([1, 2, 3, 4], [4, 3, 5])   → [3, 4]
common_elements([1, 1, 2], [1])            → [1]
common_elements([1, 2], [3, 4])            → []
```

### 13. `multiplication_table(n)` — 구구단
`n`단을 아래 모양의 문자열 리스트로 돌려주세요. (1부터 9까지, 9줄)
```
multiplication_table(3) → ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 9 = 27"]
```
> 띄어쓰기 위치까지 똑같아야 채점에서 통과해요. `f"{n} x {i} = {n * i}"`를 써 보세요.

---

## C. 문자열 다루기

### 14. `count_char(s, ch)` — 특정 글자 개수
문자열 `s` 안에 글자 `ch`가 몇 번 나오는지 돌려주세요. **`.count()`는 쓰지 마세요.** 대소문자는 구분해요.
```
count_char("banana", "a") → 3
count_char("Banana", "b") → 0
```

### 15. `capitalize_words(s)` — 단어 첫 글자만 대문자
각 단어의 **첫 글자는 대문자, 나머지는 소문자**로 바꿔 돌려주세요. 단어는 공백 한 칸으로 나뉘어 있어요.
```
capitalize_words("hello world")  → "Hello World"
capitalize_words("pYTHON is FUN") → "Python Is Fun"
```
> 힌트: `split()`으로 나누고, 바꾼 다음 `" ".join(...)`으로 다시 붙여요.

### 16. `caesar_cipher(s, shift)` — 카이사르 암호
영어 알파벳을 `shift`칸씩 밀어서 바꾼 문자열을 돌려주세요.
- `z` 다음은 다시 `a`로 돌아가요.
- 대문자는 대문자로, 소문자는 소문자로 바꿔요.
- 알파벳이 아닌 글자(공백, 숫자, 문장부호)는 그대로 둬요.
- `shift`가 음수면 반대 방향으로 밀어요.
```
caesar_cipher("abc", 1)     → "bcd"
caesar_cipher("xyz", 3)     → "abc"
caesar_cipher("Hello!", 1)  → "Ifmmp!"
caesar_cipher("bcd", -1)    → "abc"
```
> 힌트: `ord("a")` → `97`, `chr(98)` → `"b"`. 글자를 숫자로 바꿔서 계산하고, `% 26`으로 한 바퀴 돌리세요.

---

## D. 딕셔너리 (새로 나와요!)

딕셔너리는 `키: 값` 쌍을 저장해요.
```python
d = {}
d["apple"] = 3        # 키 "apple"에 값 3 저장
d["apple"] += 1       # 값 바꾸기 → 4
"apple" in d          # True (키가 있는지 확인)
d.get("banana", 0)    # 키가 없으면 0을 돌려줌
```

### 17. `count_words(s)` — 단어별 개수 세기
문장 속 단어마다 몇 번 나왔는지 딕셔너리로 돌려주세요. **소문자로 바꿔서** 세요. 단어는 공백으로 나뉘어 있어요.
```
count_words("the cat and the hat") → {"the": 2, "cat": 1, "and": 1, "hat": 1}
count_words("Hi hi HI")            → {"hi": 3}
count_words("")                    → {}
```

### 18. `most_common_char(s)` — 가장 많이 나온 글자
`s`에서 가장 많이 나온 글자를 돌려주세요.
- **공백은 세지 않아요.**
- 횟수가 같으면 **`s`에서 먼저 나온 글자**를 돌려주세요.
- `s`에는 공백이 아닌 글자가 하나 이상 있어요.
```
most_common_char("hello")  → "l"
most_common_char("abab")   → "a"
most_common_char("a b b")  → "b"
```

---

## E. 2차원 리스트 (리스트 안의 리스트)

```python
matrix = [[1, 2, 3],
          [4, 5, 6]]
matrix[0]      # [1, 2, 3]  (첫 번째 줄)
matrix[1][2]   # 6          (두 번째 줄의 세 번째 값)
```

### 19. `matrix_sum(matrix)` — 모든 값의 합
2차원 리스트 안의 모든 숫자를 더해 돌려주세요.
```
matrix_sum([[1, 2], [3, 4]]) → 10
matrix_sum([])               → 0
```
> 힌트: `for`문 안에 `for`문을 넣어 보세요.

### 20. `transpose(matrix)` — 행과 열 바꾸기
줄(행)과 칸(열)을 바꾼 새 2차원 리스트를 돌려주세요. 모든 줄의 길이는 같아요.
```
transpose([[1, 2, 3],
           [4, 5, 6]])
→ [[1, 4],
   [2, 5],
   [3, 6]]

transpose([]) → []
```
