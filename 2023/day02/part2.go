package main

func part2(input string) int {
	games_info := input_parser(input)
	output := 0

	for _, info := range games_info {
		rgb_num := map[string]int{"red": 1, "blue": 1, "green": 1}
		for _, set := range info {
			for color_name, color_num := range set {
				rgb_num[color_name] = max(rgb_num[color_name], color_num)
			}
		}
		output += (rgb_num["red"] * rgb_num["blue"] * rgb_num["green"])
	}

	return output
}
