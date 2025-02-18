"""
https://leetcode.com/problems/single-number/description/

level: easy
tags: bit manipulation
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res


if __name__ == "__main__":
    inputs = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = singleNumber(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
