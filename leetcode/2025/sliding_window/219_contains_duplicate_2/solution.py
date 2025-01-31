"""
https://leetcode.com/problems/contains-duplicate-ii

level: easy
tags: sliding window
"""

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            if i - seen[num] <= k:
                return True
        seen[num] = i
    return False


if __name__ == "__main__":
    inputs = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]
    for nums, k, expected in inputs:
        print(f"==> input: {nums} {k}")
        actual = containsNearbyDuplicate(nums, k)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
