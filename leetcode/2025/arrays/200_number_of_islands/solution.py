"""
https://leetcode.com/problems/number-of-islands/description/

level: medium
tags: dfs, bfs, union-find
"""

from typing import List


def dfs(grid: List[List[str]], i: int, j: int):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
        return

    grid[i][j] = "0"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    return count


if __name__ == "__main__":
    inputs = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ]
    for input, expected in inputs:
        print(f"==> input: {input}")
        actual = numIslands(input)
        assert actual == expected, f"ERR: expected: {expected}, actual: {actual}"
        print("PASS")
