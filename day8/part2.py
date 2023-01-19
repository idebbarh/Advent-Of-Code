input = open("input.txt","r").read()
grid = [[int(c) for c in row] for row in input.split("\n") if row]
edges = set() 
res = 0

for i in range(len(grid[0])):
    edges.add((0,i))
    edges.add((len(grid)-1,i))

for i in range(len(grid)):
    edges.add((i,0))
    edges.add((i,len(grid[0])-1))


def dfs(origin,row,col,direction,views) :
    views[direction]+=1

    if (row,col) in edges or (grid[origin[0]][origin[1]] <= grid[row][col] and origin != (row,col)):
        return

    if direction == "down":
        newR = row+1
        if newR < len(grid) :
            dfs(origin,newR,col,direction,views)

    if direction == "up":
        newR = row-1
        if newR >= 0:
            dfs(origin,newR,col,direction,views)

    if direction == "left":
        newC = col+1
        if newC < len(grid[0]):
            dfs(origin,row,newC,direction,views)
            
    if direction == "right":
        newC = col-1
        if newC >= 0 :
            dfs(origin,row,newC,direction,views)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        row = i
        col = j
        views = {
            "down":-1,
            "up":-1,
            "left":-1,
            "right":-1,
        }
        for d in ["down","up","left","right"] :
            dfs((row,col),row,col,d,views)
        res = max(res,views["down"]*views["up"]*views["left"]*views["right"])


print(res)
        
    
    
