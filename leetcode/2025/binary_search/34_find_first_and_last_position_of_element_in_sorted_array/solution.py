"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

level: medium
tags: binary search
"""

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    pass


if __name__ == "__main__":
    inputs = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ]
    for nums, target, expected in inputs:
        print(f"==> input: {input}")
        actual = searchRange(nums, target)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
