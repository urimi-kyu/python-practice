# 4세트: 5문제 (하루치)

`solution04.py` 파일의 각 함수 안에 있는 `pass`를 지우고 코드를 작성하세요.
**`test_set04.py`(채점 파일)는 고치지 마세요.**

코딩테스트에 자주 나오는 **리스트 컴프리헨션, `Counter`, 딕셔너리, 체(sieve)**를 연습해요.

---

### 1. `sum_even_squares(nums)` — 짝수 제곱의 합
정수 리스트에서 **짝수만** 제곱해서 모두 더한 값을 돌려주세요. 짝수가 없으면 `0`이에요.
```
sum_even_squares([1, 2, 3, 4]) → 20     # 2² + 4²
sum_even_squares([1, 3, 5])    → 0
sum_even_squares([])           → 0
```
> 힌트: `sum(x * x for x in nums if ...)`

### 2. `most_common_char(s)` — 가장 많이 나온 문자
소문자로 된 (비어 있지 않은) 문자열에서 **가장 많이 나온 문자**를 돌려주세요. 횟수가 같으면 **사전순으로 앞선 문자**예요.
```
most_common_char("abracadabra") → "a"
most_common_char("abcabc")      → "a"
most_common_char("zzyyx")       → "y"
```
> 힌트: `collections.Counter`, 또는 `min(..., key=...)`

### 3. `group_anagrams(words)` — 애너그램 묶기
문자열 리스트를 **서로 애너그램인 것끼리** 묶어서 돌려주세요.
각 그룹 안의 단어는 사전순, 그룹들은 **첫 단어 기준 사전순**으로 정렬해요.
```
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
→ [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
```
> 힌트: 글자를 정렬한 문자열을 딕셔너리의 key로 쓰면 애너그램끼리 같은 key가 돼요.

### 4. `two_sum(nums, target)` — 두 수의 합
리스트에서 **합이 `target`이 되는 두 원소의 인덱스** `[i, j]`(`i < j`)를 돌려주세요. 답은 항상 하나만 있어요.
```
two_sum([2, 7, 11, 15], 9) → [0, 1]
two_sum([3, 2, 4], 6)      → [1, 2]
```
> 힌트: 이중 반복문도 되지만, 딕셔너리를 쓰면 한 번만 돌아도 풀려요.

### 5. `count_primes(n)` — 소수의 개수
`1`부터 `n`까지의 **소수 개수**를 돌려주세요. (`n`은 최대 1,000,000)
```
count_primes(10)  → 4     # 2, 3, 5, 7
count_primes(1)   → 0
```
> 힌트: 숫자마다 나눠 보면 너무 느려요. **에라토스테네스의 체**를 써 보세요.
