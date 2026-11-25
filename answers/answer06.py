# 6세트 모범 답안 (다 풀고 나서 확인하세요)
from functools import cmp_to_key


def sort_words(words):
    return sorted(words, key=lambda w: (len(w), w))


def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def largest_number(nums):
    strs = [str(x) for x in nums]
    strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)))
    result = "".join(strs)
    return "0" if result[0] == "0" else result


def min_ship_capacity(weights, days):
    def can_ship(capacity):
        used_days, load = 1, 0
        for w in weights:
            if load + w > capacity:
                used_days += 1
                load = 0
            load += w
        return used_days <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def min_meeting_rooms(intervals):
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)
    rooms = 0
    j = 0
    for s in starts:
        if ends[j] <= s:
            j += 1  # 끝난 회의의 방을 재사용
        else:
            rooms += 1
    return rooms
