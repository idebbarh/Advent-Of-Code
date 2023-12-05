package main

func part1(input string) int {
	cards := get_cards(input)
	output := 0
	for _, card := range cards {
		card_score := 0
		for _, num1 := range card.winningNums {
			for _, num2 := range card.cardNums {
				if num1 == num2 {
					if card_score == 0 {
						card_score += 1
					} else {
						card_score *= 2
					}
				}
			}
		}
		output += card_score
	}
	return output
}
