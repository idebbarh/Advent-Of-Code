package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getLines(s string) []int {
	stringLines := strings.Split(s, "\n")
	var numberLines []int

	for _, line := range stringLines {
		if len(line) == 0 {
			continue
		}
		n, err := strconv.Atoi(line)
		if err != nil {
			fmt.Printf("ERROR: could not convert string %+v to int", line)
			os.Exit(1)
		}

		numberLines = append(numberLines, n)
	}

	return numberLines
}

func openFile(filePath string) string {
	fileData, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Printf("ERROR: could not read file %+v: %+v", filePath, err)
		os.Exit(1)
	}
	return string(fileData)
}

func getFuelRequiredForLine(startNumber int) int {
	if startNumber <= 0 {
		return 0
	}

	return startNumber + getFuelRequiredForLine((startNumber/3)-2)
}

func part2() int {
	fileData := openFile("./real-input.txt")
	lines := getLines(fileData)
	fuelRequired := 0

	for _, line := range lines {
		fuelRequired += getFuelRequiredForLine((line / 3) - 2)
	}
	return fuelRequired
}
