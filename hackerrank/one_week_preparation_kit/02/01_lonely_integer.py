#!/bin/python3

import os


def lonelyinteger(a):
    x = 0
    for i in a:
        x ^= i
    return x


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
