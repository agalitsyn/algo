"""
https://leetcode.com/problems/NAME
"""

from typing import List


def solve(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    inputs = [
        ([3, 0, 1], 2),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = solve(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
