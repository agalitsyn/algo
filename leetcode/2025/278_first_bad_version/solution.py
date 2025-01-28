"""
https://leetcode.com/problems/first-bad-version/

level: easy
tags: binary search
"""


def isBadVersion(version: int) -> bool:
    return [False, False, False, False, True, True][version]


def firstBadVersion(n: int) -> int:
    # Search for the first bad with binary search
    res = n
    l = 1
    r = res

    while l <= r:
        m = (l + r) // 2
        if isBadVersion(m):
            res = m  # Update result to current middle
            r = m - 1  # Narrow search to the left half
        else:
            l = m + 1  # Narrow search to the right half

        # print("=" * 50)
        # print(f"DEBUG: {type(l)} l: {l}")
        # print(f"DEBUG: {type(r)} r: {r}")
        # print(f"DEBUG: {type(m)} m: {m}")
        # print(f"DEBUG: {type(isBadVersion(m))} isBadVersion(mi): {isBadVersion(m)}")

    return res


if __name__ == "__main__":
    inputs = [
        (5, 4),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = firstBadVersion(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
