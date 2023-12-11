package main

import (
	"strconv"
	"strings"
)

func get_hand_type(hand_cards string) string {
	cards_count := map[string]int{}
	max_count := 0
	var hand_type string
	var min_count int

	for _, c := range hand_cards {
		if _, ok := cards_count[string(c)]; !ok {
			cards_count[string(c)] = 0
		}
		cards_count[string(c)] += 1
		min_count = cards_count[string(c)]
	}

	pairs_count := 0
	for _, count := range cards_count {
		max_count = max(count, max_count)
		min_count = min(count, min_count)

		if count == 2 {
			pairs_count += 1
		}
	}

	if count, ok := cards_count["J"]; ok && count != 5 {
		if count < max_count {
			if max_count == 2 {
				pairs_count -= 1
			}
			max_count += count
			if count == 2 {
				pairs_count -= 1
			}
		} else if count == max_count && pairs_count == 2 {
			max_count += count
			if count == 2 {
				pairs_count -= 2
			}
		} else if count >= max_count {
			max_count += min_count
			if min_count == 2 || count == 2 {
				pairs_count -= 1
			}
		}
	}

	if pairs_count == 2 {
		hand_type = "Two pair"
	} else if max_count == 5 {
		hand_type = "Five of a kind"
	} else if max_count == 4 {
		hand_type = "Four of a kind"
	} else if max_count == 3 && pairs_count == 0 {
		hand_type = "Three of a kind"
	} else if max_count == 3 && pairs_count == 1 {
		hand_type = "Full house"
	} else if max_count == 2 {
		hand_type = "One pair"
	} else {
		hand_type = "High card"
	}

	return hand_type
}

func get_hand_rank(hand_cards string, hands_list Hands, hand_index int) int {
	hand_type := get_hand_type(hand_cards)
	hand_rank := len(hands_list)
	hands_rank := get_hands_rank()
	cards_rank := get_cards_rank()

	for i, hand := range hands_list {
		if i == hand_index {
			continue
		}

		cur_hand_type := get_hand_type(hand.hand_cards)
		if hands_rank[hand_type] < hands_rank[cur_hand_type] {
			hand_rank -= 1
		} else if hands_rank[hand_type] == hands_rank[cur_hand_type] {
			for j := 0; j < 5; j++ {
				if cards_rank[string(hand_cards[j])] == cards_rank[string(hand.hand_cards[j])] {
					continue
				}
				if cards_rank[string(hand_cards[j])] < cards_rank[string(hand.hand_cards[j])] {
					hand_rank -= 1
				}
				break
			}
		}
	}

	return hand_rank
}

func solution(input string) int {
	output := 0
	hands_list := Hands{}

	for _, line := range strings.Split(input, "\n") {
		if len(line) == 0 {
			continue
		}

		parts := strings.Split(line, " ")
		hand_cards := parts[0]
		bid := 0
		if b, err := strconv.Atoi(parts[1]); err == nil {
			bid = b
		}
		hand := Hand{}

		hand.hand_cards = hand_cards
		hand.hand_bid = bid

		hands_list = append(hands_list, hand)
	}

	for i, hand := range hands_list {
		hand_full_rank := get_hand_rank(hand.hand_cards, hands_list, i)
		output += (hand_full_rank * hand.hand_bid)
	}

	return output
}
