# 5세트 모범 답안 (다 풀고 나서 확인하세요)
from collections import deque


def is_valid_brackets(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


def remove_adjacent_duplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def josephus(n, k):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.rotate(-(k - 1))
        q.popleft()
    return q[0]


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # 아직 답을 못 찾은 인덱스들
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result


def largest_rectangle(heights):
    stack = []  # 높이가 증가하는 인덱스들
    best = 0
    for i, h in enumerate(list(heights) + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best
