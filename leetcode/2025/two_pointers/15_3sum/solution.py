"""
https://leetcode.com/problems/3sum/

level: medium
tags: two pointers
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Общая идея:
    - Сортируем массив
    - Итерируем по массиву
    - Для каждого числа ищем два других числа, которые в сумме дают 0
    - Для этого используем два указателя, один справа, другой слева
    - Если сумма меньше 0, двигаем левый указатель
    - Если сумма больше 0, двигаем правый указатель
    - Если сумма равна 0, добавляем тройку в результат
    - Передвигаем оба указателя
    - Пропускаем дубликаты

    Сложность:
    - Временная O(n^2)
    - Пространственная O(1)
    """
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return res


if __name__ == "__main__":
    inputs = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
        ([-2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [[-2, 0, 2]]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = threeSum(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
