package main

import (
	"fmt"
	"sort"
)

// combinationSum2 function is the main function that takes an array of candidates and a target number as input.
// It sorts the candidates array and then calls the helper function findcombinationSum2 to find all unique combinations
// that add up to the target.
func combinationSum2(candidates []int, target int) [][]int {
	if len(candidates) == 0 {
		return [][]int{}
	}
	sort.Ints(candidates) // Here is the key logic of deduplication

	current := []int{}
	res := [][]int{}

	findcombinationSum2(candidates, target, 0, current, &res)
	return res
}

// findcombinationSum2 function is a recursive function that uses backtracking to find all combinations.
// It iterates over the candidates starting from the given index.
//
//	If the current candidate is the same as the previous one, it skips to avoid duplicates.
//	If the current candidate is less than or equal to the target, it includes the candidate
//		in the current combination and calls itself with the updated target and index.
//	After the recursive call, it removes the current candidate from the combination to backtrack.
func findcombinationSum2(nums []int, target, index int, current []int, res *[][]int) {
	if target == 0 {
		b := make([]int, len(current))
		copy(b, current)
		*res = append(*res, b)
		return
	}
	for i := index; i < len(nums); i++ {
		if i > index &&
			nums[i] == nums[i-1] { // Here is the key logic of deduplication. This time, duplicate numbers are not taken. Repeated numbers may be taken next time in the cycle.
			continue
		}
		if target >= nums[i] {
			current = append(current, nums[i])
			findcombinationSum2(nums, target-nums[i], i+1, current, res)
			current = current[:len(current)-1]
		}
	}
}

func main() {
	fmt.Println(combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8))
}
