# 4세트 모범 답안 (다 풀고 나서 확인하세요)
from collections import Counter, defaultdict


def sum_even_squares(nums):
    return sum(x * x for x in nums if x % 2 == 0)


def most_common_char(s):
    counts = Counter(s)
    return min(counts, key=lambda c: (-counts[c], c))


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return sorted(sorted(g) for g in groups.values())


def two_sum(nums, target):
    seen = {}
    for j, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], j]
        seen[x] = j


def count_primes(n):
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(range(i * i, n + 1, i)))
    return sum(sieve)
