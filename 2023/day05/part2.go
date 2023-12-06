package main

func part2(input string) int {
	output := -1
	almanac := get_almanac(input)

	var cur_value int

	for i := 0; i < len(almanac.seeds); i = i + 2 {
		start := almanac.seeds[i]
		get_next_value := generate_range_values(start, almanac.seeds[i+1])
		for {
			cur_value = get_next_value()
			if cur_value == -1 {
				break
			}
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

	}
	return output
}
