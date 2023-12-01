package main

import (
	"strconv"
	"strings"
)

func part1(content string) int {
	lines := strings.Split(content, "\n")
	res := 0
	for _, line := range lines {
		calibration_string_value := ""
		left_checked := false
		right_checked := false
		for l, r := 0, len(line)-1; l < len(line); r, l = r-1, l+1 {
			left_char := string(line[l])
			right_char := string(line[r])

			if _, err := strconv.Atoi(left_char); err == nil && !left_checked {
				calibration_string_value = left_char + calibration_string_value
				left_checked = true
			}

			if _, err := strconv.Atoi(right_char); err == nil && !right_checked {
				calibration_string_value += right_char
				right_checked = true
			}

			if left_checked && right_checked {
				break
			}

		}

		if calibration_int_value, err := strconv.Atoi(calibration_string_value); err == nil {
			res += calibration_int_value
		}
	}

	return res
}
