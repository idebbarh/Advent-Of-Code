package main

import (
	"strings"
)

type Node struct {
	row  int
	col  int
	pipe string
}

type Nodes = []Node

type Graph = map[Node]Nodes

type (
	Col  = string
	Row  = []Col
	Grid = []Row
)

type Pipe = string

const (
	NORTH_SOUTH Pipe = "|"
	EAST_WEST   Pipe = "-"
	NORTH_EAST  Pipe = "L"
	NORTH_WEST  Pipe = "J"
	SOUTH_WEST  Pipe = "7"
	SOUTH_EAST  Pipe = "F"
)

func node_connected_neighbrs(node Node, grid Grid) Nodes {
	neibrs := Nodes{}
	M := len(grid)
	N := len(grid[0])
	nr := node.row
	nc := node.col
	//    north
	// west-|-east
	//    south

	// | is a vertical pipe connecting north and south.
	// - is a horizontal pipe connecting east and west.
	// L is a 90-degree bend connecting north and east.
	// J is a 90-degree bend connecting north and west.
	// 7 is a 90-degree bend connecting south and west.
	// F is a 90-degree bend connecting south and east.
	// . is ground; there is no pipe in this tile.
	// S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

	switch node.pipe {
	case NORTH_SOUTH:
		if nr-1 >= 0 && grid[nr-1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr - 1, col: nc, pipe: grid[nr-1][nc]})
		}
		if nr+1 < M && grid[nr+1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr + 1, col: nc, pipe: grid[nr+1][nc]})
		}
	case EAST_WEST:
		if nc-1 >= 0 && grid[nr][nc-1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc - 1, pipe: grid[nr][nc-1]})
		}
		if nc+1 < N && grid[nr][nc+1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc + 1, pipe: grid[nr][nc+1]})
		}
	case NORTH_EAST:
		if nr-1 >= 0 && grid[nr-1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr - 1, col: nc, pipe: grid[nr-1][nc]})
		}

		if nc+1 < N && grid[nr][nc+1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc + 1, pipe: grid[nr][nc+1]})
		}
	case NORTH_WEST:
		if nr-1 >= 0 && grid[nr-1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr - 1, col: nc, pipe: grid[nr-1][nc]})
		}
		if nc-1 >= 0 && grid[nr][nc-1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc - 1, pipe: grid[nr][nc-1]})
		}
	case SOUTH_WEST:
		if nr+1 < M && grid[nr+1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr + 1, col: nc, pipe: grid[nr+1][nc]})
		}
		if nc-1 >= 0 && grid[nr][nc-1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc - 1, pipe: grid[nr][nc-1]})
		}
	case SOUTH_EAST:
		if nr+1 < M && grid[nr+1][nc] != "." {
			neibrs = append(neibrs, Node{row: nr + 1, col: nc, pipe: grid[nr+1][nc]})
		}
		if nc+1 < N && grid[nr][nc+1] != "." {
			neibrs = append(neibrs, Node{row: nr, col: nc + 1, pipe: grid[nr][nc+1]})
		}

	}
	return neibrs
}

func get_graph(input string) (Graph, Node, Grid) {
	lines := strings.Split(input, "\n")
	grid := Grid{}
	start_node := Node{row: 0, col: 0, pipe: "S"}
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		row := strings.Split(line, "")
		grid = append(grid, row)
	}

	M := len(grid)
	N := len(grid[0])
	graph := Graph{}

	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			pipe := grid[i][j]
			if pipe == "." || pipe == "S" {
				if pipe == "S" {
					start_node.row = i
					start_node.col = j
				}
				continue
			}

			node := Node{row: i, col: j, pipe: pipe}
			graph[node] = node_connected_neighbrs(node, grid)
		}
	}
	start_node_neighbrs := Nodes{}

	for node, neibrs := range graph {
		for _, n := range neibrs {
			if n.pipe == "S" {
				start_node_neighbrs = append(start_node_neighbrs, node)
			}
		}
	}

	graph[start_node] = start_node_neighbrs
	return graph, start_node, grid
}
