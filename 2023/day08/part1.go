package main

func part1(input string) int {
	instructions, graph, _ := get_map(input)
	output := 0
	cur := "AAA"
	cur_inst := 0

	for {
		if cur == "ZZZ" {
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

		output += 1
		cur_inst += 1
	}

	return output
}
