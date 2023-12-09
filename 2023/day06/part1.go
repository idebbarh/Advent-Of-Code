package main

import (
    "strings"
    "strconv"
)


func part1(input string) int {
	output := 0
    games := Games{}
    lines := strings.Split(input,"\n")
    times := strings.Fields(strings.TrimSpace(strings.Split(lines[0],":")[1]))
    distances := strings.Fields(strings.TrimSpace(strings.Split(lines[1],":")[1]))

    for i := range times {
        time := 0

        if t,err :=strconv.Atoi(times[i]); err == nil {
            time = t
        }

        dis := 0

        if d,err := strconv.Atoi(distances[i]); err == nil {
            dis = d 
        }

        games = append(games,Game{time:time,distance:dis})
    }

    for _,game:= range games {
        ways := 0
        time := game.time
        dis := game.distance

        for i:=0 ; i <= time;i=i+1 {
            cur_dis := (time-i) * i  
            if cur_dis > dis {
                ways+=1
            }
        } 
        if ways > 0 {
            if output > 0 {
                output *= ways
            }else {
                output = ways
            }
        }
    }


	return output
}
