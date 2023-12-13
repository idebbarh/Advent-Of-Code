package main

import (
	"math/big"
)

func part2(input string) *big.Int {
	instructions, graph, starts := get_map(input)
	ends := []int64{}

	var iter int64

	for _, cur := range starts {
		cur_inst := 0
		iter = 0
		for {
			if string(cur[len(cur)-1]) == "Z" {
				ends = append(ends, iter)
				break
			}

			if cur_inst >= len(instructions) {
				cur_inst = 0
			}

			switch instructions[cur_inst] {
			case "L":
				cur = graph[cur].left
			case "R":

				cur = graph[cur].right
			}
			iter += 1
			cur_inst += 1
		}
	}

	return lcmSlice(ends)
}
