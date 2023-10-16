package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseFileData(fileData string) []int {
	var res []int
	stringNumbers := strings.Split(fileData, ",")

	for _, sn := range stringNumbers {
		sn = strings.TrimRight(sn, "\n")
		num, err := strconv.Atoi(sn)
		if err != nil {
			fmt.Printf("ERROR: count not convert string %+s to int: %+v", sn, err)
			os.Exit(1)
		}
		res = append(res, num)
	}
	return res
}

func openFile(filePath string) string {
	fileData, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Printf("ERROR: count not open file %+v : %+v", filePath, err)
		os.Exit(1)
	}
	return string(fileData)
}

func runProgram(program []int) {
	for i := 0; i < len(program); i = i + 4 {
		opcode := program[i]
		switch opcode {
		case 1:
			n1 := program[i+1]
			n2 := program[i+2]
			overrideIndex := program[i+3]
			sum := program[n1] + program[n2]
			program[overrideIndex] = sum
		case 2:
			n1 := program[i+1]
			n2 := program[i+2]
			overrideIndex := program[i+3]
			mult := program[n1] * program[n2]
			program[overrideIndex] = mult

		default:
			break
		}
	}
}

func part1(filePath string) int {
	fileData := openFile(filePath)
	program := parseFileData(fileData)

	program[1] = 12
	program[2] = 2

	runProgram(program)

	return program[0]
}
