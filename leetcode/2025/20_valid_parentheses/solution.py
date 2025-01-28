"""
https://leetcode.com/problems/valid-parentheses/

level: easy
tags: stack
"""


def isValid(s: str) -> bool:
    if (len(s) % 2) != 0:
        return False

    stack = []
    for ch in s:
        if stack and ch in [")", "}", "]"]:
            prev_ch = stack[-1]
            if stack and (
                (prev_ch == "(" and ch == ")")
                or (prev_ch == "[" and ch == "]")
                or prev_ch == "{"
                and ch == "}"
            ):
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False


if __name__ == "__main__":
    s = "(([]{}))"
    res = isValid(s)
    print(res)
