"""
https://leetcode.com/problems/contains-duplicate/description/
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
            count = seen[num]
            if count >= 2:
                return True
        else:
            seen[num] = 1
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    res = containsDuplicate(nums)
    print(res)
