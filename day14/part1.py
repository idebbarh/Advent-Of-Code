paths = [[(int(p.split(",")[1]),int(p.split(",")[0])) for p in row.split(" -> ")] for row in open("input.txt","r").read().split("\n") if row]
maxX = float("-inf") 
minX = float("inf")  
maxY = float("-inf")  

for path in paths :
    for p in path :
        y,x = p
        maxX = max(maxX,x)
        minX = min(minX,x)
        maxY = max(maxY,y)

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
        if (curY+y,curX+x) not in rocksPos and (curY+y,curX+x) not in sandsPos:
            sandCurPos = (curY+y,curX+x)
            isSandFall = True
            break

    if not isSandFall :
        sandsPos.add(sandCurPos)
        sandCurPos = sandStartPos
        res +=1

    else :
        curY,curX = sandCurPos
        if curY > maxY :
            break

grid = [[0 for j in range(minX,maxX+1)] for i in range(0,maxY+1)]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = "." if (i,j+minX) not in rocksPos and (i,j+minX) not in sandsPos else ("#" if (i,j+minX) in rocksPos else "O")

for row in grid :
    print(row)

print(res)
