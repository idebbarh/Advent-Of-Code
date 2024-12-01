package main

import (
	"fmt"
	"slices"
)

type Point struct {
	x int
	y int
}

type Edge struct {
	p1 Point
	p2 Point
}

type Edges = []Edge

func is_inside(node Node, grid Grid, polygon_nodes Nodes) bool {
	inter_count := 0
	for j := node.col + 1; j < len(grid[0]); j++ {
		inter_node := Node{row: node.row, col: j, pipe: grid[node.row][j]}
		if slices.Contains(polygon_nodes, inter_node) {
			inter_count++
			if j < len(grid[0])-1 {
				is_next_same := slices.Contains(polygon_nodes, Node{row: node.row, col: j + 1, pipe: grid[node.row][j+1]})
				if is_next_same {
					inter_count++
				}
				for j < len(grid[0]) && is_next_same {
					is_next_same = slices.Contains(polygon_nodes, Node{row: node.row, col: j, pipe: grid[node.row][j]})
					j += 1
				}
			}
		}
	}

	return inter_count%2 != 0
}

func get_polygon(cur_node Node, graph Graph, vis map[Node]bool, nodes Nodes) Nodes {
	if _, ok := vis[cur_node]; ok {
		if cur_node.pipe == "S" {
			return nodes
		}
		return Nodes{}
	}

	vis[cur_node] = true
	res := []Node{}
	neighbrs := graph[cur_node]

	for _, nei := range neighbrs {
		cur_res := get_polygon(nei, graph, vis, append(nodes, cur_node))

		if len(res) < len(cur_res) {
			res = cur_res
		}

	}
	return res
}

func part2(input string) int {
	output := 0
	encloses := Nodes{}
	graph, start_node, grid := get_graph(input)
	polygon_nodes := get_polygon(start_node, graph, map[Node]bool{}, Nodes{})
	polygon_edges := Edges{}

	for _, edge := range polygon_edges {
		fmt.Printf("p1=(%d,%d), p2=(%d,%d)\n", edge.p1.y, edge.p1.x, edge.p2.y, edge.p2.x)
	}

	for i, row := range grid {
		for j, col := range row {
			node := Node{row: i, col: j, pipe: col}
			if !slices.Contains(polygon_nodes, node) {
				res := is_inside(node, grid, polygon_nodes)
				if res {
					output += 1
					encloses = append(encloses, node)
				}
			}
		}
	}

	for _, node := range encloses {
		grid[node.row][node.col] = "I"
	}

	for _, row := range grid {
		fmt.Println(row)
	}

	return output
}
