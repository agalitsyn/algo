"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

level: easy
tags: array
"""

from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    uniques = set(nums)
    res = []
    for i in range(1, len(nums) + 1):
        if i not in uniques:
            res.append(i)
    return res


if __name__ == "__main__":
    inputs = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = findDisappearedNumbers(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
