#!/bin/python3


def diagonalDifference(arr):
    primary_diagonal_sum = 0
    start_col_i = 0
    for row in arr:
        primary_diagonal_sum += row[start_col_i]
        if start_col_i == len(row):
            break
        start_col_i += 1

    secondary_diagonal_sum = 0
    start_col_j = len(arr[0]) - 1
    for row in arr:
        secondary_diagonal_sum += row[start_col_j]
        if start_col_j == 0:
            break
        start_col_j -= 1
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


if __name__ == "__main__":
    print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
