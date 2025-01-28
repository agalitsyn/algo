"""
https://leetcode.com/problems/arranging-coins/description/

level: easy
tags: binary search
"""


def isGood(n: int) -> int:
    return n * (n + 1) // 2 <= n


def arrangeCoins(n: int) -> int:
    res = -1
    l = 0
    r = 2**32  # max int, see constraints section
    while l <= r:
        m = (l + r) // 2
        if isGood(m):
            res = m
            l = m + 1
        else:
            r = m - 1
    return res


if __name__ == "__main__":
    inputs = [
        (5, 2),
        (8, 3),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = arrangeCoins(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
