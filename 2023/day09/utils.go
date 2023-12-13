package main

func is_all_zeros(nums []int) bool {
	for _, n := range nums {
		if n != 0 {
			return false
		}
	}
	return true
}
