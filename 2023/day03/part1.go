package main

import (
	"strconv"
)

func part1(input string) int {
	output := 0
	grid := get_grid(input)

	for i, row := range grid {
		is_number_schematic := false
		full_number := ""
		is_negatif := false
		for j, char := range row {
			if char == "-" && len(full_number) == 0 {
				is_negatif = true
			}
			if _, err := strconv.Atoi(char); err == nil {
				full_number += char
				for _, rv := range []int{-1, 1, 0} {
					for _, cv := range []int{-1, 1, 0} {
						if i+rv < len(grid) && i+rv >= 0 && j+cv < len(row) && j+cv >= 0 && is_schematic(grid[i+rv][j+cv]) {
							is_number_schematic = true
						}
					}
				}
			}

			if _, err := strconv.Atoi(char); err != nil || j == len(row)-1 {
				if len(full_number) > 0 && is_number_schematic {
					if num, err := strconv.Atoi(full_number); err == nil {
						if is_negatif {
							num = num * -1
						}
						output += num
					}
				}
				is_number_schematic = false
				full_number = ""
				is_negatif = false
			}
		}
	}

	return output
}
