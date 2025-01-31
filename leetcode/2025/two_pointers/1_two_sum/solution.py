"""
https://leetcode.com/problems/two-sum/

level: easy
tags: two pointers
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
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


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18
    res = twoSum(nums, target)
    print(res)
