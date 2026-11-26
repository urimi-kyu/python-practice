# 7세트 모범 답안 (다 풀고 나서 확인하세요)
from collections import Counter, defaultdict


def max_window_sum(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


def range_sums(nums, queries):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return [prefix[r + 1] - prefix[l] for l, r in queries]


def longest_unique_substring(s):
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def count_subarrays_with_sum(nums, k):
    seen = defaultdict(int)
    seen[0] = 1
    total = 0
    count = 0
    for x in nums:
        total += x
        count += seen[total - k]
        seen[total] += 1
    return count


def min_window_length(s, t):
    need = Counter(t)
    missing = len(need)  # 아직 개수를 못 채운 글자 종류 수
    window = Counter()
    best = 0
    left = 0
    for right, ch in enumerate(s):
        if ch in need:
            window[ch] += 1
            if window[ch] == need[ch]:
                missing -= 1
        while missing == 0:
            length = right - left + 1
            if best == 0 or length < best:
                best = length
            out = s[left]
            if out in need:
                if window[out] == need[out]:
                    missing += 1
                window[out] -= 1
            left += 1
    return best
