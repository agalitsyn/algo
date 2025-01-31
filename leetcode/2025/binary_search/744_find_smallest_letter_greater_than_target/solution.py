"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

level: easy
tags: binary search
"""

from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    res = letters[0]
    l = 0
    r = len(letters) - 1
    while l <= r:
        m = (l + r) // 2
        if letters[m] > target:
            res = letters[m]
            r = m - 1
        else:
            l = m + 1
    return res


if __name__ == "__main__":
    inputs = [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["x", "x", "y", "y"], "z", "x"),
    ]
    for letters, target, expected in inputs:
        print(f"==> input: {input}")
        actual = nextGreatestLetter(letters, target)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
