"""
https://leetcode.com/problems/two-sum/

level: easy
tags: two pointers
"""
from typing import List


def twoSumHashTable(nums: List[int], target: int) -> List[int]:
    """
    Решение через хеш-таблицу

    Временная сложность O(n)
    Память O(n)
    """
    # Создаем словарь для хранения индексов чисел
    indexes = {}
    for i, num in enumerate(nums):
        # Считаем разницу между целью и числом, это и будет второе число которое нужно для суммы
        diff = target - num
        # Если разница есть в словаре, значит мы нашли два числа, которые в сумме дают цель
        if diff in indexes:
            return [indexes[diff], i]
        # Иначе сохраняем число в словарь
        indexes[num] = i
    return []


def twoSum2Pointers(nums: List[int], target: int) -> List[int]:
    """
    Решение методом 2х указателей
    Только для условий когда массив отсортирован!

    Время O(n)
    Память O(1)
    """
    l = 0
    r = len(nums) - 1

    while l < r:
        curr_sum = nums[l] + nums[r]
        if curr_sum == target:
            return [l, r]
        elif curr_sum > target:
            r -= 1
        else:
            l += 1

    return []


if __name__ == "__main__":
    inputs = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in inputs:
        print(f"==> input: {nums} {target}")
        actual = twoSumHashTable(nums, target)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
