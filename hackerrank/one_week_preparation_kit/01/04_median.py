#!/bin/python3


def median(l):
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]


if __name__ == "__main__":
    print(median([1, 8, 3, 2]))
