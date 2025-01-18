from typing import List


def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0

    curr_sum = 0
    max_sum = nums[0]
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(nums)
    print(res)
