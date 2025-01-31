def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    w1 = {}
    w2 = {}

    for i in range(0, len(s)):
        if s[i] in w1:
            v = w1[s[i]]
            w1[s[i]] = v + 1
        else:
            w1[s[i]] = 1

        if t[i] in w2:
            v = w2[t[i]]
            w2[t[i]] = v + 1
        else:
            w2[t[i]] = 1

    return w1 == w2


if __name__ == "__main__":
    s = "aacc"
    t = "ccac"
    res = isAnagram(s, t)
    print(res)
