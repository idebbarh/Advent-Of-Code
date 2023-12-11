package main

type Hand struct {
	hand_cards string
	hand_bid   int
}

type (
	CardsRank = map[string]int
	HandsRank = map[string]int
	Hands     = []Hand
)

func get_cards_rank() CardsRank {
	cards_type := []string{"A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"}
	cards_rank := CardsRank{}
	for i, t := range cards_type {
		cards_rank[t] = len(cards_type) - i
	}
	return cards_rank
}

func get_hands_rank() HandsRank {
	hands_type := []string{"Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair", "One pair", "High card"}
	hands_rank := HandsRank{}

	for i, h := range hands_type {
		hands_rank[h] = len(hands_type) - i
	}

	return hands_rank
}
