package main

import (
	"strconv"
	"strings"
)

type (
	Seeds = []int
	Map   = [][]int
	Maps  = []Map
)

type Almanac struct {
	seeds Seeds
	maps  Maps
}

func get_almanac(input string) Almanac {
	lines := strings.Split(input, "\n\n")
	seeds := Seeds{}
	maps := Maps{}

	for _, n := range strings.Split(strings.Split(lines[0], ": ")[1], " ") {
		if num, err := strconv.Atoi(n); err == nil {
			seeds = append(seeds, num)
		}
	}

	for _, group := range lines[1:] {
		map_lines := Map{}
		if len(group) == 0 {
			continue
		}
		for _, line2 := range strings.Split(group, "\n")[1:] {
			if len(line2) == 0 {
				continue
			}
			destination := 0

			if d, err := strconv.Atoi(strings.Split(line2, " ")[0]); err == nil {
				destination = d
			}

			source := 0
			if s, err := strconv.Atoi(strings.Split(line2, " ")[1]); err == nil {
				source = s
			}

			rng := 0
			if r, err := strconv.Atoi(strings.Split(line2, " ")[2]); err == nil {
				rng = r
			}
			map_lines = append(map_lines, []int{destination, source, rng})

		}
		maps = append(maps, map_lines)
	}
	return Almanac{seeds: seeds, maps: maps}
}

func generate_range_values(start, length int) func() int {
	current := start - 1

	return func() int {
		current++

		if current >= start+length {
			return -1
		}
		return current
	}
}
