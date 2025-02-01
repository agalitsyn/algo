"""
https://leetcode.com/problems/minimum-absolute-difference/

level: easy
tags: sliding window
"""

from typing import List


# O(n log(n))
def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    # 1. сортируем массив
    arr.sort()

    # 2. находим минимальную разницу
    # за дефолтный минимум берем максимально допустимое значение типо max int
    min_diff = float("inf")
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        min_diff = min(min_diff, diff)

    # 3. находим пары по минимальной разнице
    res = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff == min_diff:
            res.append([arr[i - 1], arr[i]])

    return res


# O(n) можно достичь используя counting sort

if __name__ == "__main__":
    inputs = [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ([1, 3, 6, 10, 15], [[1, 3]]),
        ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = minimumAbsDifference(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
