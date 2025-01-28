"""
https://leetcode.com/problems/move-zeroes/

level: easy
tags: two pointers, fast and slow
"""

from typing import List


def moveZeroes(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    inputs = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        moveZeroes(input)
        assert input == expected, f"ERR: expected: {expected}, actual: {input}"
        print("PASS")
