"""
https://leetcode.com/problems/missing-number/
"""

from typing import List


def missingNumber1(nums: List[int]) -> int:
    nums = sorted(nums)

    for i in range(0, len(nums) + 1):
        if i == len(nums):
            return i
        else:
            if i != nums[i]:
                return i


def missingNumber2(nums: List[int]) -> int:
    return sum(range(0, len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    inputs = [
        ([1], 0),
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]
    for input, expected in inputs:
        actual = missingNumber1(input)
        assert (
            actual == expected
        ), f"ERR: 1 input: {input}, expected: {expected}, actual: {actual}"
        print("PASS 1")

        actual = missingNumber2(input)
        assert (
            actual == expected
        ), f"ERR: 2 input: {input}, expected: {expected}, actual: {actual}"
        print("PASS 2")
