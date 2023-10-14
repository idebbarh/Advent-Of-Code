input = open("input.txt","r").read().split("\n\n")
charInLine = 0
stacksPos = []
for i in range(len(input[0])):
    if input[0][i] == "\n" :
        charInLine = i + 1
        break

for i in range(charInLine-3,0,-4) :
    stacksPos = [i] + stacksPos 

shipe = [[] for _ in range(9)]
    
for i,c in enumerate(input[0]) :
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
        index = i
        while index not in stacksPos and index > 1:
            index-=charInLine
        shipe[stacksPos.index(index)]=[c]+shipe[stacksPos.index(index)]

tasks = input[1].split("\n")[::-1][1:][::-1]

for t in tasks :
    l = list(map(lambda n : int(n),list(filter(lambda text : text.isnumeric(),t.split(" ")))))
    stack = shipe[l[1]-1]
    #part one need to reverse the moved containers but in the part two you did not
    # movedContainers = stack[len(stack)-l[0]:][::-1]
    movedContainers = stack[len(stack)-l[0]:]
    shipe[l[1]-1]=stack[0:len(stack)-l[0]]
    shipe[l[2]-1]+=movedContainers

res = "".join([stack[-1] for stack in shipe if stack])
print(res)
