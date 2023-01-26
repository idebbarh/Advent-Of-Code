input = open("input.txt","r").read().split("\n\n")
monkeys = [] 

class Monkey:
    def __init__(self,items,operation,test,throw,inspectsTimes):
        self.items = items;
        self.operation = operation;
        self.test = test;
        self.throw = throw;
        self.inspectsTimes = inspectsTimes;

for monkey in input :
    monkey = [line.strip().replace(",","").replace(":","") for line in monkey.split("\n")]

    monkeyNumber = monkey[0].split(" ")[-1]

    monkeyStartingItems = [int(item) for item in monkey[1].split(" ")[2:]]

    monkeyOperation = [monkey[2].split(" ")[-2],monkey[2].split(" ")[-1]]

    monkeyTest = monkey[3].split(" ")[-1]

    monkeyThrow = [monkey[4].split(" ")[-1],monkey[5].split(" ")[-1]]

    monkeys.append(Monkey(monkeyStartingItems,monkeyOperation,int(monkeyTest),monkeyThrow,0))


curRound = 0
bigMod =1 

for monkey in monkeys :
    bigMod*=monkey.test

while curRound < 10000:
    for monkey in monkeys :

        for item in monkey.items :
            monkey.inspectsTimes+=1

            op = monkey.operation[0]
            n = int(monkey.operation[1]) if monkey.operation[1] != "old" else item

            if op == "*" :
                item*=n

            else :
                item+=n

            item%=bigMod

            testNum = monkey.test
            monkeyOne,monkeyTwo = monkey.throw

            if item % testNum == 0 :
                monkeys[int(monkeyOne)].items.append(item)

            else :
                monkeys[int(monkeyTwo)].items.append(item)

        monkey.items = []

    curRound+=1


times = []

for monkey in monkeys:
    times.append(monkey.inspectsTimes)

times.sort(reverse=True)

print(times[0] * times[1])
