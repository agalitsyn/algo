from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    if k >= len(nums):
        return sum(nums) / k

    # Initialize currSum and maxSum to the sum of the initial k elements
    curr_sum = sum(nums[0:k])
    max_sum = curr_sum

    # Start the loop from the kth element
    # Iterate until you reach the end
    for i in range(k, len(nums)):
        # Subtract the left element of the window
        # Add the right element of the window
        curr_sum += nums[i] - nums[i - k]

        # Update the max
        max_sum = max(max_sum, curr_sum)

    # Since the problem requires average, we return the average
    return max_sum / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = findMaxAverage(nums, k)
    print(res)
