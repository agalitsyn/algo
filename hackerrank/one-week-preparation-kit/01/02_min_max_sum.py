#!/bin/python3


def miniMaxSum(arr):
    min_i = min(arr)
    max_i = max(arr)
    all_sum = sum(arr)
    print(all_sum - max_i, all_sum - min_i)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
