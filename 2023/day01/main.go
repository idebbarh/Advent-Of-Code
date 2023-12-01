package main

import (
	"fmt"
	"os"
)

func main() {
	args := os.Args

	if len(args) < 2 {
		fmt.Println("Error: input file not found")
		os.Exit(1)
	}

	file := args[1]

	content, err := os.ReadFile(file)
	if err != nil {
		fmt.Printf("Error: could not open %s: %v", file, err)
		os.Exit(1)
	}

	part1_sol := part1(string(content))
	part2_sol := part2(string(content))

	fmt.Printf("part1 solution is: %d\n", part1_sol)
	fmt.Printf("part2 solution is: %d\n", part2_sol)
}
