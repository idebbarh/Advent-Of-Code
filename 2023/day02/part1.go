package main

func part1(input string) int {
	games_info := input_parser(input)
	output := 0
	for id, info := range games_info {
		out_of_limit := false
		for _, set := range info {
			colors_limits := map[string]int{"red": RED_LOAD_LIMIT, "green": GREEN_LOAD_LIMIT, "blue": BLUE_LOAD_LIMIT}
			for color_name, color_num := range set {
				colors_limits[color_name] -= color_num
				if colors_limits[color_name] < 0 {
					out_of_limit = true
					break
				}
			}
			if out_of_limit {
				break
			}
		}

		if !out_of_limit {
			output += id
		}
	}

	return output
}
