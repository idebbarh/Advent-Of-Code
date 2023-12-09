package main

import (
    "strings"
    "strconv"
)

func part2(input string) int {
	output := 0
    lines := strings.Split(input,"\n")
    time := 0
    if t,err:= strconv.Atoi(strings.Replace(strings.TrimSpace(strings.Split(lines[0],":")[1])," ","",-1)) ; err == nil {
        time = t

    }

    distance :=  0

    if d,err := strconv.Atoi(strings.Replace(strings.TrimSpace(strings.Split(lines[1],":")[1])," ","",-1)); err == nil {
        distance = d
    }

    game := Game{time:time,distance:distance}

    for i:=0 ; i <= game.time;i=i+1 {
        cur_dis := (game.time-i) * i  

        if cur_dis > game.distance {
            output+=1
        }
    } 

	return output
}

