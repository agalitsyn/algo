"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

level: easy
tags: arrays
"""

from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    # создаем отсортированный список
    nums_sorted = sorted(nums)

    # создаем словарь, где ключ - число, а значение - индекс в отсортированном списке
    num2idx = {}
    for i, num in enumerate(nums_sorted):
        if num not in num2idx:
            num2idx[num] = i

    # создаем список, где каждый элемент - индекс числа в отсортированном списке
    # это и есть количество чисел меньше текущего
    res = []
    for i in nums:
        res.append(num2idx[i])

    return res


if __name__ == "__main__":
    inputs = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = smallerNumbersThanCurrent(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
