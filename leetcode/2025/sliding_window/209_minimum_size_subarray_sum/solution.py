"""
https://leetcode.com/problems/minimum-size-subarray-sum/

level: medium
tags: sliding window
"""

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    """
    Общая идея:
    - Используем два указателя, один справа, другой слева
    - Идем циклом и суммируем числа в подмассиве пока не получим сумму больше либо равно цели
    - С этого момента нужно икать наименьшее число элементов, которое может дать сумму, поэтону надо уменьшать окно
    - Если сумма больше цели, двигаем левый указатель
    - Если сумма меньше, по while прерывается и двигается правый указатель
    - Сохраняем минимальную длину
    - Передвигаем оба указателя
    - Возвращаем минимальную длину

    Сложность: O(n)
    """
    l = 0
    total = 0
    min_len = float("inf")

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            min_len = min(min_len, r - l + 1)
            total -= nums[l]
            l += 1

    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    inputs = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ]
    for target, nums, expected in inputs:
        print(f"==> input: {target} {nums}")
        actual = minSubArrayLen(target, nums)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
