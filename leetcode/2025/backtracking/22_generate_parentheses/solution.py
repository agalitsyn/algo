from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []
    stack = []

    def backtrack(openNum, closedNum):
        # base case (stop recursion)
        if openNum == closedNum == n:
            res.append("".join(stack))
            return

        if openNum < n:
            stack.append("(")
            backtrack(openNum + 1, closedNum)
            stack.pop()

        if closedNum < openNum:
            stack.append(")")
            backtrack(openNum, closedNum + 1)
            stack.pop()

    backtrack(0, 0)
    return res


if __name__ == "__main__":
    res = generateParenthesis(3)
    print(res)
