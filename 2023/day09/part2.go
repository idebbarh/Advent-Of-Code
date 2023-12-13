package main

import (
	"strconv"
	"strings"
)

func part2(input string) int {
	output := 0
	lines := strings.Split(input, "\n")

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		line_nums := []int{}

		for _, num := range strings.Split(line, " ") {
			if n, err := strconv.Atoi(num); err == nil {
				line_nums = append(line_nums, n)
			}
		}

		diff_lines := [][]int{}
		cur_diff_line := line_nums

		for {
			is_break := is_all_zeros(cur_diff_line)

			if is_break {
				cur_diff_line = append([]int{0}, cur_diff_line...)
			}

			diff_lines = append(diff_lines, cur_diff_line)

			if is_break {
				break
			}

			tmp := []int{}

			for i := 0; i < len(cur_diff_line)-1; i = i + 1 {
				tmp = append(tmp, cur_diff_line[i+1]-cur_diff_line[i])
			}
			cur_diff_line = tmp
		}

		M := len(diff_lines)
		for i := M - 2; i >= 0; i = i - 1 {
			new_n := diff_lines[i][0] - diff_lines[i+1][0]
			diff_lines[i] = append([]int{new_n}, diff_lines[i]...)
			if i == 0 {
				output += new_n
			}
		}

	}
	return output
}
