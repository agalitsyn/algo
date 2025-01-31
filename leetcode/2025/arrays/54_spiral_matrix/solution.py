"""
https://leetcode.com/problems/spiral-matrix/

level: medium
tags: arrays
"""

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # Порядок движения: вправо, вниз, влево, вверх
    res = []
    # Пока матрица не пуста мы продолжаем обходить ее
    while matrix:
        # Сперва целиком вытаскиваем первую строку, это движение вправо
        res += matrix.pop(0)

        # Потом вытаскиваем последний элемент из каждой строки, это движение вниз
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())

        # Потом целиком вытаскиваем последнюю строку в обратном порядке, это движение влево
        if matrix:
            res += matrix.pop()[::-1]

        # Потом вытаскиваем первый элемент из каждой строки в обратном порядке, это движение вверх
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res


if __name__ == "__main__":
    inputs = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = spiralOrder(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
