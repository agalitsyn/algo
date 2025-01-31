"""
https://leetcode.com/problems/missing-number/

level: easy
tags: two pointers
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    # Левый указатель это первый день, правый это следующий за ним. Идем слева направо
    l = 0
    r = 1
    res = 0

    # Пока правый указатель не достигнет конца массива
    while r < len(prices):
        # Если цена в правом указателе больше чем в левом
        if prices[l] < prices[r]:
            # Посчитать разницу между ценами и обновим результат, который хранит максимальную разницу
            tmp = prices[r] - prices[l]
            res = max(res, tmp)
        else:
            # Если цена в правом указателе меньше чем в левом, обновим левый указатель
            l = r
        # Всегда передвигаем правый указатель
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
