"""
https://leetcode.com/problems/missing-number/
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    l = 0
    r = 1
    res = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            tmp = prices[r] - prices[l]
            res = max(res, tmp)
        else:
            l = r
        r += 1

    return res


if __name__ == "__main__":
    inputs = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9], 9),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = maxProfit(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
