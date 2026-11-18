# 1세트: 기초 10문제

`solution01.py` 파일의 각 함수 안에 있는 `pass`를 지우고 코드를 작성하세요.
**`test_set01.py`(채점 파일)는 고치지 마세요.**

---

### 1. `is_even(n)` — 짝수 판별
정수 `n`이 짝수면 `True`, 홀수면 `False`를 돌려주세요.
```
is_even(4)  → True
is_even(7)  → False
is_even(0)  → True
```

### 2. `max_of_three(a, b, c)` — 셋 중 가장 큰 수
세 숫자 중 가장 큰 값을 돌려주세요. **`max()` 함수는 쓰지 말고 `if`문으로** 풀어보세요.
```
max_of_three(1, 5, 3)    → 5
max_of_three(-1, -5, -3) → -1
```

### 3. `sum_to_n(n)` — 1부터 n까지의 합
`1 + 2 + ... + n`을 돌려주세요. `n`이 0 이하이면 `0`을 돌려주세요. **`for`문으로** 풀어보세요.
```
sum_to_n(10) → 55
sum_to_n(0)  → 0
```

### 4. `count_vowels(s)` — 모음 개수 세기
문자열 `s`에 들어 있는 영어 모음(a, e, i, o, u)의 개수를 돌려주세요. 대문자도 셉니다.
```
count_vowels("hello")  → 2
count_vowels("PYTHON") → 1
count_vowels("")       → 0
```

### 5. `reverse_string(s)` — 문자열 뒤집기
문자열을 거꾸로 뒤집어 돌려주세요.
```
reverse_string("abc")   → "cba"
reverse_string("파이썬") → "썬이파"
```
> 도전: `s[::-1]`로 먼저 풀어보고, `for`문으로도 풀어보세요.

### 6. `grade(score)` — 학점 계산
점수(0~100)를 받아서 학점을 돌려주세요.
| 점수 | 학점 |
|---|---|
| 90 이상 | `"A"` |
| 80 이상 | `"B"` |
| 70 이상 | `"C"` |
| 60 이상 | `"D"` |
| 그 외 | `"F"` |
```
grade(95) → "A"
grade(80) → "B"
grade(59) → "F"
```

### 7. `filter_positive(nums)` — 양수만 고르기
숫자 리스트에서 0보다 큰 수만 골라, 원래 순서대로 새 리스트로 돌려주세요.
```
filter_positive([3, -1, 0, 5, -2]) → [3, 5]
filter_positive([])                → []
```

### 8. `fizzbuzz(n)` — FizzBuzz
1부터 `n`까지의 숫자를 문자열 리스트로 만들어 돌려주세요. 단,
- 3의 배수는 `"Fizz"`
- 5의 배수는 `"Buzz"`
- 3과 5의 공배수는 `"FizzBuzz"`
- 나머지는 숫자를 문자열로 (`"1"`, `"2"` …)
```
fizzbuzz(5)  → ["1", "2", "Fizz", "4", "Buzz"]
fizzbuzz(15) → [..., "14", "FizzBuzz"]
```

### 9. `second_largest(nums)` — 두 번째로 큰 수
리스트에서 **두 번째로 큰 값**을 돌려주세요. 같은 값이 여러 번 나오면 한 번만 친 것으로 생각합니다.
리스트에는 서로 다른 값이 항상 2개 이상 있다고 가정해도 됩니다.
```
second_largest([3, 1, 4, 1, 5]) → 4
second_largest([5, 5, 4])       → 4
```

### 10. `is_palindrome(s)` — 회문 판별
앞으로 읽어도 뒤로 읽어도 같으면 `True`, 아니면 `False`를 돌려주세요.
**대소문자와 공백은 무시**합니다.
```
is_palindrome("level")         → True
is_palindrome("Never odd or even") → True
is_palindrome("python")        → False
```
