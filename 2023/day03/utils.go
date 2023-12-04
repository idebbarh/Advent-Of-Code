package main

import (
	"strconv"
	"strings"
)

type (
	Row  = []string
	Grid = []Row
)

func is_schematic(c string) bool {
	if c != "." {
		if _, err := strconv.Atoi(c); err != nil {
			return true
		}
	}

	return false
}

func get_grid(input string) Grid {
	lines := strings.Split(input, "\n")
	grid := Grid{}

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		grid = append(grid, strings.Split(line, ""))
	}
	return grid
}

func get_full_num(row Row, row_pos int, col_pos int, visited map[string]bool) int {
	full_num := ""
	is_neg := false
	str_row_pos := strconv.Itoa(row_pos)

	for r := col_pos; r < len(row); r = r + 1 {
		str_col_pos := strconv.Itoa(r)
		vis_pos := str_row_pos + str_col_pos
		visited[vis_pos] = true

		if _, err := strconv.Atoi(row[r]); err != nil {
			break
		}

		full_num += row[r]
	}

	for l := col_pos - 1; l >= 0; l = l - 1 {
		str_col_pos := strconv.Itoa(l)
		vis_pos := str_row_pos + str_col_pos
		visited[vis_pos] = true
		if _, err := strconv.Atoi(row[l]); err != nil {
			if row[l] == "-" {
				is_neg = true
			}
			break
		}
		full_num = row[l] + full_num
	}

	if num, err := strconv.Atoi(full_num); err == nil {
		if is_neg {
			num *= -1
		}
		return num
	}

	return 0
}
