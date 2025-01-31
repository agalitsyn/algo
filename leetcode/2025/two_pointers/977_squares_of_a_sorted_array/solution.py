"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/

level: easy
tags: two pointers
"""

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    # Объяснение: https://www.youtube.com/watch?v=4eWKHLSRHPY
    # По условию массив отсортирован по возрастанию, но квадраты всегда дают положительные числа
    # Идем с двух концов массива, сравниваем квадраты чисел и вставляем в начало результата большее число
    # Поэтому вставляем в начало результата, чтобы не делать reverse в конце
    # Временная сложность O(n), где n - длина массива
    # Пространственная сложность O(1)
    l = 0
    r = len(nums) - 1
    res = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res.insert(0, nums[l] ** 2)
            l += 1
        else:
            res.insert(0, nums[r] ** 2)
            r -= 1
    return res


if __name__ == "__main__":
    inputs = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = sortedSquares(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
