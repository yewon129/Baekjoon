from itertools import combinations

def solution(nums):
    have = len(nums) // 2
    nums = list(set(nums))
    if len(nums) <= have:
        return len(nums)
    else:
        return have