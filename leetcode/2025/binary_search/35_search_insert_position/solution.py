"""
https://leetcode.com/problems/search-insert-position/description/

level: easy
tags: binary search
"""

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    res = len(nums)
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            res = m
            r = m - 1
        elif nums[m] < target:
            l = m + 1
    return res


if __name__ == "__main__":
    inputs = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ]
    for nums, target, expected in inputs:
        print(f"==> input: {nums} {target}")
        actual = searchInsert(nums, target)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
