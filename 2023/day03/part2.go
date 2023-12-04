package main

import (
	"fmt"
	"strconv"
)

func part2(input string) int {
	grid := get_grid(input)
	output := 0

	for i, row := range grid {
		for j, col := range row {
			parts := []int{}
			fake_set := map[string]bool{}
			if col == "*" {
				for _, rv := range []int{1, -1, 0} {
					for _, cv := range []int{1, -1, 0} {
						row_pos := strconv.Itoa(i + rv)
						col_pos := strconv.Itoa(j + cv)
						pos := row_pos + col_pos
						_, is_vis := fake_set[pos]
						if !is_vis && i+rv < len(grid) && i+rv >= 0 && j+cv < len(row) && j+cv >= 0 {
							if _, err := strconv.Atoi(grid[i+rv][j+cv]); err == nil {
								full_num := get_full_num(grid[i+rv], i+rv, cv+j, fake_set)
								fmt.Println(full_num)
								parts = append(parts, full_num)
							}
						}
					}
				}
				if len(parts) == 2 {
					output += (parts[0] * parts[1])
				}
			}
		}
	}

	return output
}
