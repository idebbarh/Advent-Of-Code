package main

import (
	"math/big"
	"strings"
)

type Next struct {
	left  string
	right string
}

type Graph = map[string]Next

func get_map(input string) ([]string, Graph, []string) {
	parts := strings.Split(input, "\n\n")
	instructions := strings.Split(parts[0], "")
	graph := Graph{}
	starts := []string{}
	for _, line := range strings.Split(parts[1], "\n") {
		if len(line) == 0 {
			continue
		}

		line_parts := strings.Split(line, " = ")
		nexts := strings.Split(line_parts[1], ", ")
		left := strings.Replace(nexts[0], "(", "", -1)
		right := strings.Replace(nexts[1], ")", "", -1)
		cur := line_parts[0]

		if string(cur[len(cur)-1]) == "A" {
			starts = append(starts, cur)
		}

		graph[cur] = Next{left: left, right: right}
	}

	return instructions, graph, starts
}

func gcd(a, b *big.Int) *big.Int {
	for b.Cmp(big.NewInt(0)) != 0 {
		a, b = b, new(big.Int).Mod(a, b)
	}
	return a
}

func lcm(a, b *big.Int) *big.Int {
	return new(big.Int).Div(new(big.Int).Mul(a, b), gcd(a, b))
}

func lcmSlice(numbers []int64) *big.Int {
	if len(numbers) == 0 {
		return big.NewInt(0)
	}

	result := big.NewInt(numbers[0])

	for i := 1; i < len(numbers); i++ {
		result.Set(lcm(result, big.NewInt(numbers[i])))
	}

	return result
}
