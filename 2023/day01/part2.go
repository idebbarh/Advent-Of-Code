package main

import (
	"fmt"
	"strconv"
	"strings"
)

func spelled_out_number() func() map[string]int {
	spelled_out_number := map[string]int{"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

	return func() map[string]int {
		return spelled_out_number
	}
}

func is_spelled_out_with_letter(line string) (bool, int) {
	for k, v := range spelled_out_number()() {
		if len(k) > len(line) {
			continue
		}

		if line[0:len(k)] == k {
			return true, v
		}
	}
	return false, -1
}

func part2(content string) int {
	lines := strings.Split(content, "\n")
	res := 0

	for _, line := range lines {
		calibration_string_value := ""
		left_checked := false
		right_checked := false
		for l, r := 0, len(line)-1; l < len(line); r, l = r-1, l+1 {
			left_char := string(line[l])
			right_char := string(line[r])
			if !left_checked {
				is_spelled_num, spelled_num := is_spelled_out_with_letter(line[l:])
				if is_spelled_num {
					calibration_string_value = fmt.Sprint(spelled_num) + calibration_string_value
					left_checked = true
				} else if _, err := strconv.Atoi(left_char); err == nil {
					calibration_string_value = left_char + calibration_string_value
					left_checked = true
				}
			}

			if !right_checked {
				is_spelled_num, spelled_num := is_spelled_out_with_letter(line[r:])
				if is_spelled_num {
					calibration_string_value += fmt.Sprint(spelled_num)
					right_checked = true
				} else if _, err := strconv.Atoi(right_char); err == nil {
					calibration_string_value += right_char
					right_checked = true
				}
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
