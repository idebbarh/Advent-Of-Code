package main

import (
	"strconv"
	"strings"
)

type Card struct {
	winningNums []int
	cardNums    []int
}

type Cards []Card

func get_cards(input string) Cards {
	lines := strings.Split(input, "\n")
	cards := Cards{}

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		sides := strings.Split(line, ":")
		card_winning_nums := []int{}
		for _, num := range strings.Split(strings.Split(sides[1], " | ")[0], " ") {
			if num2, err := strconv.Atoi(strings.Trim(num, " ")); err == nil {
				card_winning_nums = append(card_winning_nums, num2)
			}
		}

		card_numbers := []int{}
		for _, num := range strings.Split(strings.Split(sides[1], " | ")[1], " ") {
			if num2, err := strconv.Atoi(strings.Trim(num, " ")); err == nil {
				card_numbers = append(card_numbers, num2)
			}
		}
		cards = append(cards, Card{winningNums: card_winning_nums, cardNums: card_numbers})
	}
	return cards
}
