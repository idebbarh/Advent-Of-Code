package main

import (
	"fmt"
	"os"
)

func main() {
	args := os.Args

	if len(args) < 2 {
		fmt.Println("Error: input not fout")
		os.Exit(1)
	}

	file := args[len(args)-1]

	content, err := os.ReadFile(file)
	if err != nil {
		fmt.Printf("Error: could not read %s: %v", file, err)
		os.Exit(1)
	}

	sol := solution(string(content))

	fmt.Printf("solution is: %d\n", sol)
}
