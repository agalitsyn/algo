from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums) // 2

    left = nums[0:n]
    right = nums[n : len(nums) - 1]

    if nums[n] < target:
        return search(left, target)
    return search(right, target)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    res = search(nums, target)
    print(res)
