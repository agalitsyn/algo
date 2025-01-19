from typing import List


def twoSum(nums: List[int], target: int) -> List[int] | None:
    indexes = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in indexes:
            return [indexes[diff], i]
        indexes[num] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18
    res = twoSum(nums, target)
    print(res)
