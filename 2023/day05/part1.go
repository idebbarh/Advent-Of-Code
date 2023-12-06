package main

func part1(input string) int {
	output := -1
	almanac := get_almanac(input)

	var cur_value int

	for _, s := range almanac.seeds {
		cur_value = s
		for _, m := range almanac.maps {
			for _, line := range m {
				if cur_value >= line[1] && cur_value < line[1]+line[2] {
					diff := cur_value - line[1]
					cur_value = line[0] + diff
					break
				}
			}
		}

		if output < 0 {
			output = cur_value
		} else {
			output = min(output, cur_value)
		}
	}

	return output
}
