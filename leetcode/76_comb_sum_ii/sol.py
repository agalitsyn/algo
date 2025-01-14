# It has duplicates
def comb_sum(arr, s):
    n = len(arr)
    for i in range(1, 2**n + 1):
        tmp = []
        p = 1
        for j in range(n):
            if i & p:
                tmp.append(arr[j])
            p *= 2
        if sum(tmp) == s:
            print(tmp)


if __name__ == "__main__":
    comb_sum([10, 1, 2, 7, 6, 1, 5], 8)
