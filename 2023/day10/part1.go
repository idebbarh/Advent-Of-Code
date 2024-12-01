package main

func graph_traverse(cur_node Node, vis map[Node]bool, graph Graph, total int, steps []int) []int {
	if cur_node.pipe == "S" {
		return steps
	}

	if _, ok := graph[cur_node]; !ok {
		return []int{}
	}

	vis[cur_node] = true

	neibrs := graph[cur_node]

	res := []int{}

	for _, nei := range neibrs {
		if _, ok := vis[nei]; ok {
			continue
		}

		cur_res := graph_traverse(nei, vis, graph, total+1, append(steps, total))

		if len(res) < len(cur_res) {
			res = cur_res
		}
	}

	return res
}

func part1(input string) int {
	output := 0
	graph, start_node, _ := get_graph(input)
	start_node_neighbrs := graph[start_node]

	cicle := graph_traverse(start_node_neighbrs[0], map[Node]bool{}, graph, 1, []int{})
	rev_cicle := []int{}

	for i := 0; i < len(cicle); i++ {
		rev_cicle = append(rev_cicle, cicle[len(cicle)-1-i])
	}

	for i := 0; i < len(cicle); i++ {
		if cicle[i] == rev_cicle[i] {
			return cicle[i]
		}
	}

	return output
}
