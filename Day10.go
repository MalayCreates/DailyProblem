///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given a sorted (in ascending order)
// integer array nums of n elements and
// a target value, write a function to
// search target in nums. If target
// exists, then return its index,
// otherwise return -1.
///////////////////////////////////////////

package judgeCircle

import (
	"fmt"
)

func search(nums []int, target int) int {
	hi := len(nums) - 1
	lo := 0
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			hi = mid - 1
		} else if nums[mid] < target {
			lo = mid + 1
		}
	}
	return -1
}

func main() {
	testNums := []int{1, 2, 3, 4, 5}
	testTarget := 4
	fmt.Println(search(testNums, testTarget))
}
