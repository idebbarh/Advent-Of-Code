package main

import (
	"strconv"
	"strings"
)

const (
	RED_LOAD_LIMIT   = 12
	GREEN_LOAD_LIMIT = 13
	BLUE_LOAD_LIMIT  = 14
)

type ColorsSet = map[string]int

type Info = []ColorsSet

type GamesInfo = map[int]Info

func input_parser(input string) GamesInfo {
	games_info := GamesInfo{}
	lines := strings.Split(input, "\n")

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}

		parts := strings.Split(line, ":")
		game_id := strings.Split(parts[0], " ")[1]

		info := Info{}

		for _, set := range strings.Split(parts[1], ";") {
			set = strings.Trim(set, " ")
			colors_info := strings.Split(set, ",")
			for _, color := range colors_info {
				colors_set := ColorsSet{}
				color = strings.Trim(color, " ")
				color_info := strings.Split(color, " ")
				if color_num, err := strconv.Atoi(color_info[0]); err == nil {
					color_name := color_info[1]
					colors_set[color_name] = color_num
				}
				info = append(info, colors_set)
			}
		}
		if id, err := strconv.Atoi(game_id); err == nil {
			games_info[id] = info
		}
	}

	return games_info
}
