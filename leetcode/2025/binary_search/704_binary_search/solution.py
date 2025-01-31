"""
https://leetcode.com/problems/binary-search/

level: easy
tags: binary search
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    res = -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1  # налево
        elif nums[m] < target:
            l = m + 1  # направо
    return res


if __name__ == "__main__":
    inputs = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]
    for nums, target, expected in inputs:
        print(f"==> input: {nums} {target}")
        actual = search(nums, target)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
