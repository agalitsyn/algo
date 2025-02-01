"""
https://www.youtube.com/watch?v=QloMLtxNe0Q

Дан массив целых неотрицательных чисел. Необходимо сгруппировать друг с другом числа
которые можно получить путем перестановки их составляющих при этом игнорируя нули
"""

from typing import List


def solve(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    inputs = [
        (
            [1230, 99, 23001, 123, 111, 300021, 101010, 90000009, 9],
            [[99, 90000009], [111, 101010], [123, 23001, 300021, 1230], [9]],
        ),
        ([11, 22], [[11], [22]]),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = solve(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
