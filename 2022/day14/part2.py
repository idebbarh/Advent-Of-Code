paths = [[(int(p.split(",")[1]),int(p.split(",")[0])) for p in row.split(" -> ")] for row in open("input.txt","r").read().split("\n") if row]
maxY = float("-inf")  

for path in paths :
    for p in path :
        y,x = p
        maxY = max(maxY,y)

maxY += 2
dirs = [(1,0),(1,-1),(1,1)]
rocksPos = set()
sandsPos = set()


for i in range(len(paths)):
    for j in range(len(paths[i])-1) :
        y,x = paths[i][j]
        y1,x1 = paths[i][j+1]

        for k in range(y,y1+(1 if y <= y1 else -1),(1 if y <= y1 else -1)) :
            rocksPos.add((k,x))

        for k in range(x,x1+(1 if x <= x1 else -1),(1 if x <= x1 else -1)) :
            rocksPos.add((y,k))

sandStartPos = (0,500)
sandCurPos = (0,500)
res = 0
while True :
    isSandFall = False
    for d in dirs :
        y,x = d
        curY,curX = sandCurPos
        if (curY+y,curX+x) not in rocksPos and (curY+y,curX+x) not in sandsPos and curY+y < maxY:
            sandCurPos = (curY+y,curX+x)
            isSandFall = True
            break

    if not isSandFall :
        sandsPos.add(sandCurPos)
        res +=1
        if sandCurPos == sandStartPos : break
        sandCurPos = sandStartPos

print(res)
