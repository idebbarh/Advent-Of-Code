package main

func helper(cards_score map[int]int, cur_cards_score map[int]int, memo map[int]int) int {
	if len(cur_cards_score) == 0 {
		return 0
	}

	output := 0

	for card_id, card_score := range cur_cards_score {
		output += card_score

		next_cards := map[int]int{}

		for j := card_id + 1; j < card_score+card_id+1; j = j + 1 {
			next_cards[j] = cards_score[j]
		}

		if cached, ok := memo[card_id]; ok {
			output += cached
		} else {
			res := helper(cards_score, next_cards, memo)
			output += res
			memo[card_id] = res
		}

	}

	return output
}

func part2(input string) int {
	memo := map[int]int{}
	cards := get_cards(input)
	cards_score := map[int]int{}

	for i, card := range cards {
		card_score := 0
		for _, num1 := range card.winningNums {
			for _, num2 := range card.cardNums {
				if num1 == num2 {
					card_score += 1
				}
			}
		}
		cards_score[i+1] = card_score
	}

	return helper(cards_score, cards_score, memo) + len(cards)
}
