input = open("input.txt","r").read().split("\n\n")
monkeys = {}

for monkey in input :
    monkey = [line.strip().replace(",","").replace(":","") for line in monkey.split("\n")]

    monkeyNumber = monkey[0].split(" ")[-1]

    monkeyStartingItems = [int(item) for item in monkey[1].split(" ")[2:]]

    monkeyOperation = [monkey[2].split(" ")[-2],monkey[2].split(" ")[-1]]

    monkeyTest = monkey[3].split(" ")[-1]

    monkeyThrow = [monkey[4].split(" ")[-1],monkey[5].split(" ")[-1]]

    monkeys[monkeyNumber] = {"items":monkeyStartingItems,"operation":monkeyOperation,"test":int(monkeyTest),"throw":monkeyThrow,"inspectsTimes":0}


curRound = 0
while curRound < 20:
    for key in monkeys.keys() :
        monkey = monkeys[key]
        for item in monkey["items"] :
            monkeys[key]["inspectsTimes"]+=1

            op = monkey["operation"][0]
            n = int(monkey["operation"][1]) if monkey["operation"][1] != "old" else item
            if op == "*" :
                item*=n

            else :
                item+=n

            item//=3

            testNum = monkey["test"]
            monkeyOne,monkeyTwo = monkey["throw"]
            if item % testNum == 0 :
                monkeys[monkeyOne]["items"].append(item)

            else :
                monkeys[monkeyTwo]["items"].append(item)

        monkeys[key]["items"] = []

    curRound+=1
    print(curRound)

times = []

for key in monkeys.keys() :
    times.append(monkeys[key]["inspectsTimes"])

times.sort(reverse=True)

print(times[0] * times[1])
