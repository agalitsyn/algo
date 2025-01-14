#!/bin/python3


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            negative += 1
        else:
            positive += 1
    n = len(arr)
    print("%.6f" % (positive / n))
    print("%.6f" % (negative / n))
    print("%.6f" % (zero / n))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
